/**
 * @param {number[]} nums
 * @return {number[]}
 */
var getConcatenation = function(nums) {
    let n = nums.length;
	
	// create return array ans of length 2n
    let ans = new Array(2*n);
    
    for(let i = 0; i < n; i++) {
        ans[i] = nums[i]
        ans[i+n] = nums[i]
    }
    return ans;
};
