def maxSubArray(nums) -> int:
    lenNums = len(nums)
    accSum = [0 for _ in range(lenNums)]

    maxAccSum = -10 ** 4 - 1
    maxAccSumInd = -1
    for ind, el in enumerate(nums):
        accSum[ind] = accSum[ind - 1] + el  # 어차피 accSum[-1]이 첨에 0
        if accSum[ind] > maxAccSum:
            maxAccSum = accSum[ind]
            maxAccSumInd = ind

    negativeMinAccSum = 0
    for i in range(maxAccSumInd):
        if nums[i] < negativeMinAccSum:
            negativeMinAccSum = nums[i]

    return maxAccSum - negativeMinAccSum



nums = [-2,1,-3,4,-1,2,1,-5,4]
maxSubArray(nums)
