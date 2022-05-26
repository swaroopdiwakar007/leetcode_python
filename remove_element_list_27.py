class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        i = 0
        for i in range(len(nums)):
            if nums[i] == val:
                k += 1
            elif k!=0:
                nums[i-k] = nums[i]
        return i-k+1
