/**
 * @param {string} allowed
 * @param {string[]} words
 * @return {number}
 */
var countConsistentStrings = function(allowed, words) {
    let count = words.length;
        
    for (let word of words){
        for(let char of word){
            if (!(allowed.includes(char))){
                count --;
                break;
            };
        };
    };
    
    return count;
};
