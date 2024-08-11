class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        stackGreaters = []
        stackPivots = []
        counter = 0
        for i,num in enumerate( nums):
            if num == pivot:
                stackPivots.append(num)
            elif num < pivot:
                nums[counter] = num
                counter += 1
            else:
                stackGreaters.append(num)
        for piv in stackPivots:
            nums[counter] = piv
            counter += 1
        for num in stackGreaters:
            nums[counter] = num
            counter += 1
        return nums