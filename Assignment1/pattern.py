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

    def put(self, item, threadName):
        self.space.acquire() # Semaphore lock 0 or -1

        with self.lock:
            self.buffer.append(item)
            print(f"[{threadName}] Produced: {item} | Queue: {self.buffer}") # I added this to demonstrate visual adding
        
        self.items.release() # Signal sempahore

    def get(self, threadName):
        self.items.acquire() # Semaphore lock till capacity

        with self.lock:
            item = self.buffer.pop(0)
            print(f"[{threadName}] Consumed: {item} | Queue: {self.buffer}") # I added this to demonstrate visual getting
        
        self.space.release() # Signal sempahore
        return item


class Producer:
    def __init__(self, sources, sharedQueue, name="Producer"):
        self.sources = sources  # Can be a list of source lists
        self.sharedQueue = sharedQueue
        self.name = name # To add custom name like in ROS or Kafka

    def run(self):
        for source in self.sources:
            for item in source:
                time.sleep(0.1)  # simulate artificial delay
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
            time.sleep(0.1)  # simulate artificial delay


# Basic controller will just use the objects I wrote 
class Controller:
    def __init__(self, sources, capacity, numProducers=2, numConsumers=2):
        self.sources = sources
        self.numProducers = numProducers
        self.numConsumers = numConsumers

        # Input validation
        if(numConsumers < 1 or numProducers < 1):
            raise Exception("Please have more than 0 producer and consumer")

        if(numProducers > len(sources)):
            print("INFO : Reducing number of producer threads to match source") # Warning like spark 
            self.numProducers = len(sources)
        
        self.destination = []
        self.sharedQueue = CustomQueue(capacity)

    def start(self):
        producers = [] # keep track of prod
        consumers = [] # keep track of cons

        # Divide sources among producers evenly
        sourcesPerProducer = [[] for _ in range(self.numProducers)]
        for idx, source in enumerate(self.sources):
            producerIdx = idx % self.numProducers
            sourcesPerProducer[producerIdx].append(source)

        for i in range(self.numProducers):
            producer = Producer(sourcesPerProducer[i], self.sharedQueue, name=f"Producer-{i+1}")
            producers.append(threading.Thread(target=producer.run))

        for i in range(self.numConsumers):
            consumer = Consumer(self.sharedQueue, self.destination, name=f"Consumer-{i+1}")
            consumers.append(threading.Thread(target=consumer.run))

        for t in producers + consumers:
            t.start()

        for t in producers:
            t.join()

        # After all producers are done, send one poison pill per consumer
        for _ in range(self.numConsumers):
            self.sharedQueue.put(None, "Controller")

        for t in consumers:
            t.join()

        print(f"Destination: {self.destination}")


def main():
    import testing
    testing.test1()


if __name__ == "__main__":
    main()
