/**
 * @param {number[]} target
 * @param {number[]} arr
 * @return {boolean}
 */
var canBeEqual = function(target, arr) {
    if(arr.length === 1 && arr[0] === target[0]) return true;
    target.sort((a,b) => a-b);
    arr.sort((a,b) => a-b);
    for(let i = 0; i<= arr.length; i++){
        if(target[i] !== arr[i]) return false;
    }
    return true;
};
[172]
[84]