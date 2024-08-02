/**
 * @param {number[]} nums
 * @param {number} k
 * @return {boolean}
 */
var containsNearbyDuplicate = function(nums, k) {
    const counts = {};
  for (let i = 0; i < nums.length; i++) {
    if (!(nums[i] in counts)) counts[nums[i]] = i;
    else {
      if (Math.abs(counts[nums[i]] - i) <= k) {
        return true;
      }
        if(nums[i] in counts){
        counts[nums[i]] = i;
      }
    }
  }
  return false;
};