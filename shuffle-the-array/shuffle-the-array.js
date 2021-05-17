/**
 * @param {number[]} nums
 * @param {number} n
 * @return {number[]}
 */
var shuffle = function(nums, n) {
    let array1 = nums.slice(0, n);
    let array2 = nums.slice(n);
    let final_array = [];
    
    for (let elem in array1){
        final_array.push(array1[elem])
        final_array.push(array2[elem])
    };
    return final_array; 
};