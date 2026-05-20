# find duplicates in a list
def find_duplicates(nums):
    duplicates = set()
    seen = set()
    for each in nums:
        if each in seen:
            duplicates.add(each)
        else:
            seen.add(each)
    return duplicates 

print(find_duplicates([1, 2, 3, 4, 2, 5, 1]))  # Output: {1, 2}

####################
#two sum problem
def two_sum(numbers, target):
    existing_nums = {};
    for i, each_num in enumerate(numbers):
        needed_num = target - each_num
        if needed_num in existing_nums:
            return [existing_nums[needed_num], i]
        
        existing_nums[each_num] = i

    return None

print(two_sum([2, 7, 11, 15], 9))  # Output: (2, 7)

def two_sum2(nums, target):
    existing_num = {}
    for i, num in enumerate(nums):
        needed_num = target - num
        if needed_num in existing_num:
            return [existing_num[needed_num], i]
        existing_num[num] = i
    return None
print(two_sum2([2, 7, 11, 15], 9)) # Output: [0, 1]

#Valid parentheses / stack
def is_valid_parentheses(s):   
    stack = []#last in first out data structure
    parentheses_map = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in parentheses_map.values():
            stack.append(char)
        elif char in parentheses_map.keys():
            if not stack or stack[-1] != parentheses_map[char]:
                return False
            stack.pop()
    
    return len(stack) == 0

#Merge sorted lists / two pointers
def merge_sorted_lists(list1, list2):
    merged_list = []
    i, j = 0, 0
    
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1
            
    # If there are remaining elements in list1 or list2, add them to merged_list
    merged_list.extend(list1[i:])
    merged_list.extend(list2[j:])
    
    return merged_list