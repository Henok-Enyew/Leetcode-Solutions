/**
 * @param {number[]} nums
 * @return {number}
 */
var specialArray = function(nums) {
  const length = nums.length;
  if (length === 1 && nums[0] === 0) return -1;
  else if (length === 1 && nums[0] >= 1) return 1;
  nums.sort((a, b) => a - b);

  for (let i = 0; i < length; i++) {
    for (let s = 1; s <= nums[length - 1]; s++) {
      if (nums[i] >= s && s === length - i) {
        if (i < 1) return s;
        else if (s > nums[i - 1]) return s;
      }
    }
  }

  return -1;
};