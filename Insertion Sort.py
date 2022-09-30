# import random
unsorted = ["X", "F", "B", "H", "A"]


def Insertion_Sort(unsorted):
    # set boundary between the sorted and unsorted
    # take elements from the unsorted side to the sorted one
    # compare with every element of sorted
    # insert element in the right position
    # index of first element of unsorted
    for boundary in range(1, len(unsorted)):
        previous = boundary - 1
        while unsorted[previous + 1] < unsorted[previous] and previous >= 0:
            unsorted[previous], unsorted[previous + 1] = unsorted[previous + 1], unsorted[previous]

            previous = previous - 1


print(unsorted)
Insertion_Sort(unsorted)
print(unsorted)


# Python program for implementation of Insertion Sort

# Function to do insertion sort
def insertionSort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):

        key = arr[i]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


# Driver code to test above
arr = [12, 11, 13, 5, 6]
insertionSort(arr)
print("Sorted array is:")
for i in range(len(arr)):
    print("%d" % arr[i])

# This code is contributed by Mohit Kumra