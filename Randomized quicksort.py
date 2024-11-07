
import random

# Function to partition the array based on pivot
def randomized_partition(A, low, high):
    #Choose a random pivot index between low and high
    pivot_idx = random.randint(low, high)
    
    #Swaping the chosen pivot with the last element
    A[pivot_idx], A[high] = A[high], A[pivot_idx]
    
    # Now use the partition function to sort based on this pivot
    return partition(A, low, high)

#Partition function
def partition(A, low, high):
    pivot = A[high]
    i = low - 1  #index of the smaller element'
    for j in range(low, high):
        if A[j] <= pivot:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[high] = A[high], A[i + 1]
    return i + 1

# Function to implement Randomized Quicksort
def randomized_quicksort(A, low, high):
    if low < high:
        #Finding the partition index
        pivot_idx = randomized_partition(A, low, high)
        
        #Applying quicksort to the subarrays
        randomized_quicksort(A, low, pivot_idx - 1)
        randomized_quicksort(A, pivot_idx + 1, high)


if __name__ == "__main__":
    
    A = [7, 13, 24, 4, 2, 5, 1, 10]  
    
    print("Original array:", A)
    #Applyinh randomized quicksort here
    randomized_quicksort(A, 0, len(A) - 1)
    
    print("Sorted array:", A)
