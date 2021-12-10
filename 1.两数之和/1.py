from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tmp = {}
        for x in range(0, len(nums)):
            if target - nums[x] in tmp:
                return(tmp[target-nums[x]], x)
            else:
                tmp[nums[x]] = x

if __name__ == '__main__':
    nums = [2,7,11,15]
    target = 9
    sol = Solution()
    print(sol.twoSum(nums, target))
    nums = [3, 2, 4]
    target = 6
    print(sol.twoSum(nums, target))