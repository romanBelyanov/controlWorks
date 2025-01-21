import random
import time
def bubble_sort(nums): # Имеет сложность O(n**2), так как
    swapped = True
    while swapped: # при наихудшей для данного варианта расстановке - по убыванию - цикл выполнится len(nums) раз,
        swapped = False
        for i in range(len(nums) - 1): # а этот цикл выполнится len(nums)-1 раз
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True

nums = [random.randint(1, 10000) for i in range(100)]

start = time.perf_counter()
bubble_sort(nums.copy())
end = time.perf_counter()

start_ = time.perf_counter()
nums.sort()
end_ = time.perf_counter()

print(f"Время выполнения пузырьковой сортировки: {end-start}")
print(f"Время выполнения .sort: {end_-start_}")