/**
 * @param {number[]} nums
 * @return {number}
 */
var singleNumber = function(nums) {
    let uniqueNum = nums[0];
  nums.sort((a, b) => a - b);
  for (let i = 0; i < nums.length; i = i + 3) {
    if (nums[i] !== nums[i + 1]) {
      uniqueNum = nums[i];
      break;
    }
  }
  return uniqueNum;
  
};