# 정수 nums와 target이 주어질 때, 더했을 때 target이 되는 num의 인덱스를 출력
# 중복 사용 안됨. 답은 오직 하나
# 출력 순서 무관

def twoSum(self, nums: List[int], target: int) -> List[int]:
    answer = []
    length = len(nums)
    for i in range(length):
        for j in range(i + 1, length):
            if nums[i] + nums[j] == target:
                answer.extend([i, j])
    return answer