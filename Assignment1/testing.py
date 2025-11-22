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



def main():
    test1()
    test2()
    test3()

if __name__ == "__main__":
    main()