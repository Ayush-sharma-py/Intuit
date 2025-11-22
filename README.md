# Intuit
My Repo for Intuit Build Challenge

## Assignment 1
Setup is pretty simple just run the testing.py file from inside the Inuit directory and you should get the output printed in console

Please see result.txt for the output related to each of the testcases I designed and ran. All the classes are in pattern.py/

Producer-N is when any producer thread writes to the buffer
Consumer-N is when any consumer gets from the buffer
A None poison pill terminates them
Queue is the buffer
Destination is the final output 
And Success/Fail is the final result of the test

I have inline comments explaining what the code does

Sample Output:
``
TEST 1 -----------------------------------------------------------------
[Producer-1] Produced: 1 | Queue: [1]
[Consumer-1] Consumed: 1 | Queue: []
[Producer-2] Produced: 4 | Queue: [4]
[Consumer-2] Consumed: 4 | Queue: []
[Producer-1] Produced: 2 | Queue: [2]
[Consumer-3] Consumed: 2 | Queue: []
[Producer-2] Produced: 5 | Queue: [5]
[Consumer-2] Consumed: 5 | Queue: []
[Producer-1] Produced: 3 | Queue: [3]
[Consumer-2] Consumed: 3 | Queue: []
[Producer-2] Produced: 6 | Queue: [6]
[Consumer-5] Consumed: 6 | Queue: []
[Controller] Produced: None | Queue: [None]
[Controller] Produced: None | Queue: [None, None]
[Controller] Produced: None | Queue: [None, None, None]
[Consumer-9] Consumed: None | Queue: [None, None]
[Controller] Produced: None | Queue: [None, None, None]
[Consumer-7] Consumed: None | Queue: [None, None]
[Controller] Produced: None | Queue: [None, None, None]
[Consumer-1] Consumed: None | Queue: [None, None]
[Consumer-6] Consumed: None | Queue: [None]
[Consumer-8] Consumed: None | Queue: []
[Controller] Produced: None | Queue: [None]
[Controller] Produced: None | Queue: [None, None]
[Controller] Produced: None | Queue: [None, None, None]
[Consumer-4] Consumed: None | Queue: [None, None]
[Controller] Produced: None | Queue: [None, None, None]
[Consumer-10] Consumed: None | Queue: [None, None]
[Consumer-3] Consumed: None | Queue: [None]
[Controller] Produced: None | Queue: [None, None]
[Consumer-2] Consumed: None | Queue: [None]
[Consumer-5] Consumed: None | Queue: []
Destination: [1, 4, 2, 5, 3, 6]
SUCCESS
``
## Assignment 2

Dataset link -> https://www.kaggle.com/datasets/carlosaguayo/usa-hospitals

I used this dataset because it is small in size enough to fit on github with enough data for analysis. Using this does not violate any licenses as it is a part of public data dump by the US Gov. 