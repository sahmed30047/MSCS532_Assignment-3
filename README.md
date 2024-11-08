Randomized Quicksort

To Run the Code Install Python 3 on the machine.

Steps-

Download the code. Copy the Python script to a file {Randomized quicksort.py)

randomized_partition - Randomly selects a pivot element and partitions the array according to this pivot.

partition: The standard partition function that rearranges elements in a manner that places smaller elements on one side and larger elements on the other.

randomized_quicksort: Utilizes randomized pivots to recursively sort the array.

Output:- Original array: [7, 13, 24, 4, 2, 5, 1, 10] Sorted array: [1, 2, 4, 5, 7, 10, 13, 24]

Findings
Randomized Quicksort has an average case time complexity as it is capable of avoiding poor pivot choices.

This algorithm is particularly effective for general purpose sorting particularly when the worst case performance of deterministic quicksort is desired.


Hash Table with Chaining

To Run the Code Install Python 3 on the machine.

Steps- 

Download the code. Copy the Python script to a file {Hashtable with Chaining.py).

Run the script.

Output- The script shows the values for the keys 'Kiwi', 'Pineapple' and 'Grapes' after the values have been inserted.

The search for 'Pineapple' returns the value None when the 'Pineapple' key is removed as it is no longer found in the hash table.

Findings-

Chaining efficiently handles hash table collisions with linked lists. This lets multiple key value pairs share an index without overwriting.

Linked lists for chaining allow hash tables to efficiently handle many elements even with collisions.
