/**
 * @param {string} sentence
 * @return {boolean}
 */
var checkIfPangram = function(sentence) {
    let alphabet = "abcdefghijklmnopqrstuvwxyz";
    
    for (let elem of alphabet){
        if (! sentence.includes(elem)){
            return false;
        };
    };
    return true;
};
