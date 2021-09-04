/**
 * @param {number[]} nums
 * @return {number[]}
 */
var sortedSquares = function(nums) {
    let result = [];
    
    for (elem of nums){
        elem = elem * elem;
        result.push(elem)
    };
    result.sort((a,b) => a-b)
    
    return result
};
