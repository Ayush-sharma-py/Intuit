import threading
import time


# Built a custom queue instead of using Queue library by python to demonstarte thread locking
# The main 'container' used here is just a standard python list 
# I added inline comments where it was a bit more interesting

class CustomQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = [] # Python list that is used as the container

        # Input validation to make sure no goofy stuff
        if(capacity <= 0):
            raise Exception("Capacity has to be more than 0")

        # Semaphores that I use for thread safety
        self.lock = threading.Lock()
        self.items = threading.Semaphore(0)
        self.space = threading.Semaphore(capacity)

    def put(self, item, thread_name):
        self.space.acquire() # Semaphore lock 0 or -1

        with self.lock:
            self.buffer.append(item)
            print(f"[{thread_name}] Produced: {item} | Queue: {self.buffer}") # I added this to demonstrate visual adding
        
        self.items.release() # Signal sempahore

    def get(self, thread_name):
        self.items.acquire() # Semaphore lock till capacity

        with self.lock:
            item = self.buffer.pop(0)
            print(f"[{thread_name}] Consumed: {item} | Queue: {self.buffer}") # I added this to demonstrate visual getting
        
        self.space.release() # Signal sempahore
        return item


class Producer:
    def __init__(self, source, sharedQueue, name="Producer"):
        self.source = source
        self.sharedQueue = sharedQueue
        self.name = name # To add custom name like in ROS or Kafka

    def run(self):
        for item in self.source:
            time.sleep(0.1)  # simulate artificial delay (without this the prints were instant which did not look good visually)
            self.sharedQueue.put(item, self.name)


class Consumer:
    def __init__(self, sharedQueue, destination, name="Consumer"):
        self.sharedQueue = sharedQueue
        self.destination = destination
        self.name = name # To add custom name like in ROS or Kafka

    def run(self):
        while True:
            item = self.sharedQueue.get(self.name)
            if item is None:
                break
            self.destination.append(item)
            time.sleep(0.2)  # simulate artificial delay (without this the prints were instant which did not look good visually)


# Basic controller will just use the objects I wrote 
class Controller:
    def __init__(self, sources, capacity, num_producers=2, num_consumers=2):
        self.sources = sources
        self.num_producers = num_producers
        self.num_consumers = num_consumers

        # Input validation
        if(num_consumers < 1 or num_producers < 1):
            raise Exception("Please have more than 0 producer and consumer")

        if(num_producers > len(sources)):
            print("INFO : Reducing number of producer threads to match source") # Warning liek spark 
            self.num_producers = len(sources)
        
        self.destination = []
        self.sharedQueue = CustomQueue(capacity)

    def start(self):
        producers = [] # keep track of prod
        consumers = [] # keep track of cons

        for i in range(self.num_producers):
            producer = Producer(self.sources[i % len(self.sources)], self.sharedQueue, name=f"Producer-{i+1}")
            producers.append(threading.Thread(target=producer.run))

        for i in range(self.num_consumers):
            consumer = Consumer(self.sharedQueue, self.destination, name=f"Consumer-{i+1}")
            consumers.append(threading.Thread(target=consumer.run))

        for t in producers + consumers:
            t.start()

        for t in producers:
            t.join()

        # After all producers are done, send one poison pill per consumer
        for _ in range(self.num_consumers):
            self.sharedQueue.put(None, "Controller")

        for t in consumers:
            t.join()

        print(f"Destination: {self.destination}")


def main():
    sources = [
        [1, 2, 3],
        [4, 5, 6],
    ]
    controller = Controller(sources, capacity=3, num_producers=2, num_consumers=10)
    controller.start()


if __name__ == "__main__":
    main()
