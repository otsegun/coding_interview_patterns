# Problem statement: Given an array of integers, return all triplets [a, b, c] such that a + b + C = 0.
# The solution must not contain duplicate triplets. If no such triplets are found, return an empty array. 
# Each triplete can be arranged in any order, and the output can returned in any order. 

# clarifying question? Can we have repeated elements? like [a, a, c] if yes, then the approach below
# works.

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

input_nums = [0, -1, 2, -3, 1]

print(f"Answer is {triplet_sum_brute2(input_nums)}")

# optimized approach
# 1. a + b + c = 0 => b + c = -a
# 2. By fixing a, we want to find all pairs [b, c] that sum to -a
# 3. We have to deal with duplicate by using unique a's and b's
# 4. key: if we sort the list, we  use inward traversal to find paired sums, and eliminate duplicates. 