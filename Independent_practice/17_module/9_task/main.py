import random
nums = [random.randint(-100, 100) for _ in range(10)]
a = random.randint(0, 5)
b = random.randint(5, 10)
print(nums)
print(a, b)
nums = nums[:a] + nums[b:]
print(nums)