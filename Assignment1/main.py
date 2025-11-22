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
        self.sharedQueue.put(None, self.name)  # poison pill to tell consumer to stop


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
            time.sleep(0.4)  # simulate artificial delay (without this the prints were instant which did not look good visually)


# Basic controller will just use the objects I wrote 
class Controller:
    def __init__(self, source, capacity):
        self.source = source
        self.destination = []
        self.sharedQueue = CustomQueue(capacity)

    def start(self):
        producer = Producer(self.source, self.sharedQueue, name="Producer-1")
        consumer = Consumer(self.sharedQueue, self.destination, name="Consumer-1")

        t1 = threading.Thread(target=producer.run)
        t2 = threading.Thread(target=consumer.run)

        t1.start()
        t2.start()

        t1.join()
        t2.join()

        print(f"Final Destination: {self.destination}")


def main():
    source = [1, 2, 3, 4, 5]
    controller = Controller(source, capacity=2)
    controller.start()


if __name__ == "__main__":
    main()
