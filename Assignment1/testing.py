from pattern import *

def test1():
    print("TEST 1 -----------------------------------------------------------------")
    sources = [
        [1, 2, 3],
        [4, 5, 6],
    ]
    controller = Controller(sources, capacity=3, numProducers=2, numConsumers=10)
    controller.start()

    # For quick testing, not production worthy will take wayyyyyyyyyyy tooo long for large N
    if(sorted(controller.destination) == sorted([item for sublist in sources for item in sublist])):
        print("SUCCESS")
    else:
        print("FAIL")
    print("-----------------------------------------------------------------------")

def test2():
    print("TEST 2 -----------------------------------------------------------------")
    sources = [
        [1, 2, 3],
        [4, 5, 6],
    ]
    controller = Controller(sources, capacity=5, numProducers=10, numConsumers=1)
    controller.start()

    # For quick testing, not production worthy will take wayyyyyyyyyyy tooo long for large N
    if(sorted(controller.destination) == sorted([item for sublist in sources for item in sublist])):
        print("SUCCESS")
    else:
        print("FAIL")
    print("-----------------------------------------------------------------------")

def test3():
    print("TEST 3 -----------------------------------------------------------------")
    sources = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    controller = Controller(sources, capacity=1, numProducers=2, numConsumers=1)
    controller.start()

    # For quick testing, not production worthy will take wayyyyyyyyyyy tooo long for large N
    if(sorted(controller.destination) == sorted([item for sublist in sources for item in sublist])):
        print("SUCCESS")
    else:
        print("FAIL")
    print("-----------------------------------------------------------------------")

def test4():
    print("TEST 4 -----------------------------------------------------------------")
    sources = [
        [10, 20, 30],
        [40, 50],
        [60],
        [70, 80, 90, 100]
    ]
    controller = Controller(sources, capacity=2, numProducers=3, numConsumers=2)
    controller.start()

    # For quick testing, not production worthy will take wayyyyyyyyyyy tooo long for large N
    if(sorted(controller.destination) == sorted([item for sublist in sources for item in sublist])):
        print("SUCCESS")
    else:
        print("FAIL")
    print("-----------------------------------------------------------------------")

def test5():
    print("TEST 5 -----------------------------------------------------------------")
    sources = [
        [1],
        [2],
        [3],
        [4],
        [5]
    ]
    controller = Controller(sources, capacity=2, numProducers=1, numConsumers=5)
    controller.start()

    # For quick testing, not production worthy will take wayyyyyyyyyyy tooo long for large N
    if(sorted(controller.destination) == sorted([item for sublist in sources for item in sublist])):
        print("SUCCESS")
    else:
        print("FAIL")
    print("-----------------------------------------------------------------------")

def test6():
    print("TEST 6 -----------------------------------------------------------------")
    sources = [
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    ]
    controller = Controller(sources, capacity=3, numProducers=2, numConsumers=3)
    controller.start()

    # For quick testing, not production worthy will take wayyyyyyyyyyy tooo long for large N
    if(sorted(controller.destination) == sorted([item for sublist in sources for item in sublist])):
        print("SUCCESS")
    else:
        print("FAIL")
    print("-----------------------------------------------------------------------")

def test7():
    print("TEST 7 -----------------------------------------------------------------")

    sources = [list(range(1, 101))]  # 100 items in a single source 
    controller = Controller(sources, capacity=50, numProducers=3, numConsumers=5)
    controller.start()

    # For quick testing, not production worthy will take way too long for extremely large N
    if(sorted(controller.destination) == sorted([item for sublist in sources for item in sublist])):
        print("SUCCESS")
    else:
        print("FAIL")
    print("-----------------------------------------------------------------------")


def main():
    # Run all tests to validate producer-consumer pattern with various scenarios
    
    # Test 1: Multiple producers, many consumers, moderate queue capacity
    test1()
    
    # Test 2: Many producers, single consumer, larger queue capacity
    test2()
    
    # Test 3: Few producers, single consumer, very small queue capacity
    test3()
    
    # Test 4: Multiple producers and consumers with varied source sizes with small capacity
    test4()
    
    # Test 5: Single producer, many consumers, small sources
    test5()
    
    # Test 6: Single large source, multiple producers and consumers
    test6()

    # Test 7: Very large source to check scalability and performance
    test7() # Ideally would test with even larger N (>10^6 inputs) but performance is not being tested here as it would depend on what the usecase is 


if __name__ == "__main__":
    main()
