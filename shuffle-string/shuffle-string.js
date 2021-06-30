/**
 * @param {string} s
 * @param {number[]} indices
 * @return {string}
 */
var restoreString = function(s, indices) {
    let tempObject = {};
    let arr_str = [...s];
    for (let i in indices) {
        tempObject[indices[i]] = arr_str[i];
    }
    let finalString = Object.values(tempObject).join('')
    return finalString;
};
