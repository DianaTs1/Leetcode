/**
 * @param {string} s
 * @param {number} k
 * @return {string}
 */
var truncateSentence = function(s, k) {
    let first_array = s.split(" ");
    let final_array = first_array.slice(0, k);
    return final_array.join(" ");
};
