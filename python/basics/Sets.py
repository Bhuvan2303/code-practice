# Set = unordered collection with no duplicates(Duplicates disappear automatically)
nums = {1, 2, 3, 3, 2}
print(nums)
nums.add(10)
nums.remove(3)
print(nums)

A = {1, 2, 3}
B = {3, 4, 5}
print(A.union(B))
print(A.intersection(B))