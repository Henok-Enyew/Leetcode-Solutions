/**
 * @param {number[]} nums
 * @return {number[]}
 */
var majorityElement = function(nums) {
    const counter = {};
  for (let i = 0; i < nums.length; i++) {
    if (!(nums[i] in counter)) {
      counter[nums[i]] = 0;
    }
    counter[nums[i]] = counter[nums[i]] + 1;
  }
  let majorityItems = [];
  for (let num in counter) {
    if (counter[num] > nums.length / 3) {
      majorityItems.push(Number(num));
    }
  }
  return majorityItems;
};