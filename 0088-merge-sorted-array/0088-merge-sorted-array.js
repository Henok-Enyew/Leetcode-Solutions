/**
 * @param {number[]} nums1
 * @param {number} m
 * @param {number[]} nums2
 * @param {number} n
 * @return {void} Do not return anything, modify nums1 in-place instead.
 */
var merge = function(array1, m, array2, n) {
  const array1Copy = [...array1];
  let array1Item = array1Copy[0];
  let array2Item = array2[0];

  let i1 = 1;
  let i2 = 1;
  let j = 0;
  while (array1Item || array2Item || array2Item === 0) {
    if (array1Item === undefined || array1Item > array2Item) {
      array1[j] = array2Item;
      array2Item = array2[i2];
      i2++;
      j++;
      console.log(array1);
    } else {
      if (i1 <= m) {
        array1[j] = array1Item;
        j++;
      }
      array1Item = array1Copy[i1];
      i1++;
    }
  }};

