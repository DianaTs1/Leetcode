/**
 * @param {number[]} nums
 * @return {number[]}
 */
var sortArrayByParity = function(nums) {
    
    const odd = nums.filter(elem=> elem%2==1)
    const even = nums.filter(elem=> elem%2==0)
    
    return even.concat(odd)
};
