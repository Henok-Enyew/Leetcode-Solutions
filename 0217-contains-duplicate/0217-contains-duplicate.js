/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
    const setFromArr = new Set(nums);
  const newArray = Array.from(setFromArr);
  if (nums.length !== newArray.length) return true;
  return false;
};