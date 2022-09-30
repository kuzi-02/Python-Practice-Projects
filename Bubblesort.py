import random
unsorted = [random.randint(0,100)for i in range (10)]
print(unsorted)
def bubble_sort(arr):
  swapped = True
  while swapped:
   swapped = False
   for i in range(len(arr)-1):
     if arr[i] > arr[i+1]:
      temp = arr[i]
      arr[i]=arr[i+1]
      arr[i+1] = temp
      swapped = True
  return arr
sorted_arr=bubble_sort(unsorted)
print(unsorted)


# Python program for implementation of Bubble Sort

# def bubbleSort(arr):
# 	n = len(arr)
#
# 	# Traverse through all array elements
# 	for i in range(n-1):
# 	# range(n) also work but outer loop will
# 	# repeat one time more than needed.
#
# 		# Last i elements are already in place
# 		for j in range(0, n-i-1):
#
# 			# traverse the array from 0 to n-i-1
# 			# Swap if the element found is greater
# 			# than the next element
# 			if arr[j] > arr[j + 1] :
# 				arr[j], arr[j + 1] = arr[j + 1], arr[j]
#
# # Driver code to test above
# arr = [64, 34, 25, 12, 22, 11, 90]
#
# bubbleSort(arr)
#
# print ("Sorted array is:")
# for i in range(len(arr)):
# #	print ("% d" % arr[i],end=" ")
