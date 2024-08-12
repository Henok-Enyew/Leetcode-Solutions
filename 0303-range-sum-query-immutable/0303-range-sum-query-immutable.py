class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = nums
    def sumRange(self, left: int, right: int) -> int:
        sum = 0
        counter = left
        while counter <= right:
            sum += self.nums[counter]
            counter += 1
        return sum


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)