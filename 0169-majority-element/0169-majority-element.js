/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function(nums) {
     const counter = {};
  for (let i = 0; i < nums.length; i++) {
    if (!(nums[i] in counter)) {
      counter[nums[i]] = 0;
    }
    counter[nums[i]] = counter[nums[i]] + 1;
  }
  let majorityCount = 0;
  let majorityItem;
  for (let num in counter) {
    if (counter[num] > majorityCount) {
      majorityCount = counter[num];
      majorityItem = num;
    }
  }
  return majorityItem;
};