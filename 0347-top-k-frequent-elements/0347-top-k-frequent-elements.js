/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function(nums, k) {
    const counter = {};
  for (let i = 0; i < nums.length; i++) {
    if (!(nums[i] in counter)) {
      counter[nums[i]] = 0;
    }
    counter[nums[i]] = counter[nums[i]] + 1;
  }

  let sortable = [];
  for (var num in counter) {
    sortable.push([num, counter[num]]);
  }

  sortable.sort(function (a, b) {
    return b[1] - a[1];
  });

  return sortable.slice(0, k).map((e) => e[0]);
};