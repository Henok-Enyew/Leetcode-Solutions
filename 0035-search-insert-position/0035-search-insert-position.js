/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
const searchInsert = function (nums, target) {
  if (nums.includes(target)) {
    return nums.indexOf(target);
  }
  for (let i = 0; i < nums.length; i++) {
    if (nums[i] > target) return i;
  }
  return nums.length;
};
