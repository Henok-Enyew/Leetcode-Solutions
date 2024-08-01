/**
 * @param {number[]} nums
 * @return {number[]}
 */
var singleNumber = function(nums) {
let uniqueNum;
  let uniqueNum2;
  nums.sort((a, b) => a - b);
  for (let i = 0; i < nums.length; ) {
    if (nums[i] !== nums[i + 1]) {
      if (!uniqueNum && uniqueNum !== 0) uniqueNum = nums[i];
       else uniqueNum2 = nums[i];
                i++;
    } else i = i + 2;
  }
  return [uniqueNum, uniqueNum2];
};