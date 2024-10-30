class Solution:
    def search(self, nums: List[int], target: int) -> int:
        map_ = {num: index for index, num in enumerate(nums)}
        if target in map_.keys():
            return map_[target]
        else:
            return -1