class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        map = {}
        for left in range(len(nums)):
            if nums[left] in map and abs( map[nums[left]] - left ) <= k:
                return True
            map[nums[left]] = left
            
        return False