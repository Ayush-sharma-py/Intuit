from pattern import *

def test1():
    print("TEST 1 -----------------------------------------------------------------")
    sources = [
        [1, 2, 3],
        [4, 5, 6],
    ]
    controller = Controller(sources, capacity=3, num_producers=2, num_consumers=10)
    controller.start()

    # For quick testing, not production worthy will take wayyyyyyyyyyy tooo long for large N
    if(sorted(controller.destination) == sorted([item for sublist in sources for item in sublist])):
        print("SUCCESS")
    else:
        print("FAIL")
    print("-----------------------------------------------------------------------")

def main():
    test1()

if __name__ == "__main__":
    main()