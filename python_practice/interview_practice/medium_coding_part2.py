# Binary Search
# Search for a target in a sorted list. divide and conquer approach 
# l = [1,2,3,4,5,6,7,8,10] target 3
def search_target(my_list, target):
    i = 0
    j = len(my_list)-1
    while i < j:
        mid_point = j+i//2 # to get a middle integer
        mid_value = my_list[mid_point] # returns 5
        if mid_value == target:
            return mid_point # index
        elif mid_value < target:
            i = mid_point + 1
        else: 
            j = mid_point -1 
    return -1


l = [1, 2, 3, 4, 5, 6, 7, 8, 10]

print(search_target(l, 3))   # 2
print(search_target(l, 9))   # -1



# Implement Queue using Stacks
#skippp


# Find Intersection of Two Arrays
#same as find common 
def find_intersections(array1, array2):
    result = []
    for each in array1:
        for num in array2:
            if each == num:
                result.append(each)
    return result
l =[1,2,3,4]
m = [4,6,7,2]
print(find_intersections(l, m))


# Detect a Cycle in a Linked List -> tortouse and the hare



# Maximum Subarray Sum (Kadane’s Algorithm)
# Find contiguous subarray with largest sum.
#arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
def max_sum_array(my_array):
    max_so_far = current_sum = my_array[0]
    for x in my_array:
        current_sum = max(x, current_sum + x) # -2 = -2 or 1 : current sum is = 1 
        max_so_far = max(max_so_far, current_sum) # -2 or 1: max_so_far 1. 
    return max_so_far

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(max_sum_array(arr)) # 4, -1, 2, 1

# Move Zeroes to End
# Preserve order of non-zero elements.
# arr = [-2, 0, -3, 4, -1, 0, 1, -5, 0]
# output = [0, 0, 0, -2, -3, 4, -1, 1, -5]
def move_zero(my_list):
    result = []
    non_zero = []
    for each in my_list:
        if each == 0:
            result.append(each)
        else:
            non_zero.append(each)
    result.extend(non_zero)
    return result
arr = [-2, 0, -3, 4, -1, 0, 1, -5, 0]
print(move_zero(arr))

# Find kth Largest Element
 # Sort the array in descending order
arr.sort(reverse=True)
print(arr)
# b = [10, 3, 45, 98, 6, 25] k = 4 
# sort : 98, 45, 25, 10, 6, 3 :  output 10
def find_largest_element(my_array, k):
    my_array.sort(reverse = True)
    return my_array[k-1]
b = [10, 3, 45, 98, 6, 25] 
print(find_largest_element(b, 4))
