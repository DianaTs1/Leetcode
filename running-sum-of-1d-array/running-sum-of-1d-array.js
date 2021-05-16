/**
 * @param {number[]} nums
 * @return {number[]}
 */
var runningSum = function(nums) {
    let num = 0;
    let final_list = [];

    for (let elem in nums){
      num += nums[elem]
      final_list.push(num)
    };

    return final_list;
};