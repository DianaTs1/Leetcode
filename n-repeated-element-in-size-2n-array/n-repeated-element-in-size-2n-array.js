/**
 * @param {number[]} A
 * @return {number}
 */
var repeatedNTimes = function(nums) {
    var temp_arr = [];
    for (let element of nums) {
        if (temp_arr[element]) {
            return element;
        }
        temp_arr[element] = true;        
    }
};
