/**
 * @param {number[]} nums
 * @return {number}
 */
var thirdMax = function(nums) {
    const setFromArr = new Set(nums);
    const newArray = Array.from(setFromArr);
    newArray.sort((a, b) => b - a);
    if (newArray.length < 3) {
      return newArray[0];
    }
    return newArray[2];
};