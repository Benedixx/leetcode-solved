class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        for idx, value in enumerate(nums):
            if target - value in nums[idx+1:]:
                result.append(idx)
                result.append(nums.index(target - value, idx+1))
                break
        return result
