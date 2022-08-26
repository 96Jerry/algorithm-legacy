# bisect, 이분탐색 공부

nums = [0,1,2,3,4,5,6,7,8,9]
n = 5

# n을 nums의 어떤 index에 넣어야 하는지?

# 1. 이분탐색을 쓰지 않고 완전탐색으로 확인
'''
for i in range(len(nums)):
    if nums[i] >= n:
        break
print(i)
'''

# 2. 이분탐색으로 확인, r, l 변수를 만듦
'''
l = 0
r = len(nums) - 1
result = 0
while l <= r:
    mid = (l+r) // 2
    if nums[mid] >= n:
        result = mid
        r = mid - 1
    else:
        l = mid + 1
print(result)
'''

# bisect 활용, bisect_left(literable, value) : 왼쪽 인덱스 구하기
from bisect import bisect_left, bisect_right
print(bisect_left(nums,n))
print(bisect_right(nums,n))