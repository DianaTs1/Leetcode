/**
 * @param {number[]} nums
 * @return {number[]}
 */
var getConcatenation = function(nums) {
    const ans = nums.map((elem) => elem)
    nums.map((elem) => ans.push(elem))
    return ans
}; 