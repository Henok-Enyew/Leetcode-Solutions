/**
 * @param {number} rowIndex
 * @return {number[]}
 */
var getRow = function(numRows) {
 const mainArray = [[1]];
  for (let j = 0; j < numRows ; j++) {
    const newArray = [1];
    const array = mainArray[j];
    for (let i = 0; i < array.length; i++) {
      if (i === array.length - 1) {
        newArray.push(1);
      } else {
        newArray.push(array[i] + array[i + 1]);
      }
    }
    mainArray.push(newArray);
  }

  return mainArray[numRows];
};