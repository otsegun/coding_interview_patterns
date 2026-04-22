# brute force approach
# time complexity: 0(n^2) because we loop traverse input ~ n^2 times in worst case
# space complexity: 0(1) because a constant number of variables are assigned during execution
def paired_sum_sorted_brute(input_list: list[int], target_num: int) -> list[int]:
    input_length: int = len(input_list)

    for i in range(input_length):
        for j in range(i + 1, input_length):
            sum = input_list[i] + input_list[j]
            if sum == target_num:
                return [i, j]
    return []


# two pointer approach
# time complexity: 0(n) because we traverse input n times in the worst case
# space complexity: 0(1) because we allocate a constant number of variables during execution
def paired_sum_sorted(input_list: list[int], target: int) -> list[int]:
	input_length: int = len(input_list)
	left_pointer, right_pointer = 0, input_length-1
	while left_pointer < right_pointer:
		sum: int = input_list[left_pointer] + input_list[right_pointer]
		if sum == target:
			return [left_pointer, right_pointer]
		elif sum < target:
			left_pointer += 1
		else:
			right_pointer -= 1
	return []
	

# two pointers starting from a start point/index
def paired_sum_sorted_starting_point(nums: list[int], target: int, start: int):
	n: int = len(nums)
	left, right = start, n-1
	while start <  n and left < right:
		sum = nums[left] + nums[right]
		if sum == target:
			return [left, right]	
		elif sum < target:
			left += 1
		else: 
			right -= 1
	return []

# find all pairs with two pointers, unique pointers, with start_point
def paired_sum_sorted_all_pairs(nums: list[int], target: int, start: int) -> list[list[int]] :
	n: int = len(nums)
	paired_sums: list[list[int]] = []
	left, right = start, n-1
	while start <  n and left < right:
		sum = nums[left] + nums[right]
		if sum == target:
			paired_sums.append([left, right])
			# increment left pointer to continue looking for pairs
			left += 1
			# if a target is found, make sure next value on left pointer is unique to avoid
			# duplicate [a, b] pairs
			while left < right and nums[left] == nums[left -1]:
				left =+ 1
		elif sum < target:
			left += 1
		else: 
			right -= 1
	return []
	
nums = [1, 1, 1]
target = 2	
print(
    f"{(paired_sum_sorted_brute(input_list=nums, target_num=target))}",
)
