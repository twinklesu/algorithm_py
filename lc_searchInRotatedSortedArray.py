
def search(nums, target):
    N = len(nums)
    return binarySearch(0, N, nums, target)

def binarySearch(start, end, nums, target):
    if end - start < 2:
        if nums[start] == target:
            return start
        else:
            return -1
    mid = (start+end)//2
    if nums[start] < nums[mid]:
        if nums[start] <= target < nums[mid]:
            # 맞는 순서
            return binarySearch(start, mid, nums, target)
        else:
            # 맞는 순서 우측
            return binarySearch(mid, end, nums, target)
    else:
        # 꼬인 순서
        if nums[mid] <= target <= nums[end]:
            # 우측 탐색
            return binarySearch(mid, end, nums, target)
        else:
            # 좌측 탐색
            return binarySearch(start, mid, nums, target)


nums = [4,5,6,7,0,1,2]
target = 0
print(search(nums, target))