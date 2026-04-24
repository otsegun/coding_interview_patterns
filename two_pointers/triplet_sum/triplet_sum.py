# Problem statement: Given an array of integers, return all triplets [a, b, c] such that a + b + C = 0.
# The solution must not contain duplicate triplets. If no such triplets are found, return an empty array. 
# Each triplete can be arranged in any order, and the output can returned in any order. 

# clarifying question? Can we have repeated elements? like [a, a, c] if yes, then the approach below
# works.

def paired_sum_sorted_all_pairs(nums: list[int], target: int, start: int) -> list[list[int]] :
	n: int = len(nums)
	paired_sums: list[list[int]] = []
	left, right = start, n-1
	while start <  n and left < right:
		sum = nums[left] + nums[right]
		if sum == target:
			paired_sums.append([nums[left], nums[right]])
			# increment left pointer to continue looking for pairs
			left += 1
			# if a target is found, make sure next value on left pointer is unique to avoid
			# duplicate [a, b] pairs
			while left < right and nums[left] == nums[left -1]:
				left += 1
		elif sum < target:
			left += 1
		else: 
			right -= 1
	return paired_sums

# brute force approach
def triplet_sum_brute(nums: list[int]) -> list[list[int]]:
    triplets: set = set()
    n = len(nums)

    for i in range(n):
        for j in range(n):
            for k in range(n):
                sum = nums[i] + nums[j] + nums[k]
                if sum == 0:
                    sorted_triplet = tuple(sorted((nums[i], nums[j], nums[k])))
                    triplets.add(sorted_triplet)
    return list(triplets)

# input_nums = [0, -1, 2, -3, 1]

# print(f"Answer is {triplet_sum_brute(input_nums)}")

# brute force apporach
# no duplicate elements, no duplicate triplets
def triplet_sum_brute2(nums: list[int]) -> list[list[int]]:
    triplets:set = set()
    n = len(nums)

    for i in range(n):
        for j in range(i+1, n):
            for k in range (j+1, n) :
                sum = nums[i] + nums[j] + nums[k]
                if sum == 0:
                    sorted_triplets = tuple(sorted([nums[i], nums[j], nums[k]]))
                    triplets.add(sorted_triplets)
    return [list(triplet) for triplet in triplets]



# optimized approach
# 1. a + b + c = 0 => b + c = -a
# 2. By fixing a, we want to find all pairs [b, c] that sum to -a
# 3. We have to deal with duplicate by using unique a's and b's
# 4. key: if we sort the list, we  use inward traversal to find paired sums, and eliminate duplicates. 
# 5. If the list is sorted, and a > 0, then b,  c > 0 and positive triplets will never sum to zero so we can skip loop for a > 0

# time complexity:
# 1. sorting is 0(nlog(n))
# 2. loop is 0(n^2) in worst case scenario
# 3. assuming the paired_sums found are <<  n, then the overall complexity id 0(nlog(n)) + 0(n^2) = 0(n^2)
# 4. 
def triplet_sum(nums: list[int]) -> list[list[int]]: 
    triplets = list()
    n: int = len(nums)

    # sort input
    nums.sort()

    for i in range(n):
        # Positive triplets can't sum to zero. If nums[i] > 0, then nums[j] > 0 for j > i due to ascending order sorting. 
        if nums[i] > 0:
            break
        # avoid duplicate triplets, skip nums[i] if it is the same as the previous number.
        if (i > 0) and (nums[i] == nums[i-1]):
            continue

        target = -nums[i]
        paired_sums = paired_sum_sorted_all_pairs(nums, target= target, start=i+1)
        if paired_sums:
            for pair in paired_sums:
            #     pair.append(-target)
            #     triplets.append(pair)
                triplets.append([-target] + pair )
            
    return triplets
        
            


input_nums = [0, -1, 2, -3, 1]
input_nums =  []
input_nums = [0]
input_nums = [1, -1]
input_nums = [0, 0, 0]
input_nums = [1, 0, 1]
input_nums = [0, 0, 1, -1, 1, -1]

print(f"Answer is {triplet_sum(input_nums)}")
