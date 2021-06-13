/**
 * @param {string[]} words
 * @return {number}
 */
var uniqueMorseRepresentations = function(words) {
    let morseCode = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."];
        
    let alphabet = 'abcdefghijklmnopqrstuvwxyz'.split('');
    
    // Create a dictionary of alphabet
    let alphabetsDict = {};
    for (i=0; i<alphabet.length; i++){
        alphabetsDict[alphabet[i]] = morseCode[i]
    };
    
    // Create a list of unique transformations
    let tempArray = []
    for (let word of words){
        let uniqueTransformation = "";
        for (let letter of word){
            uniqueTransformation += alphabetsDict[letter]
        };
        if (! tempArray.includes(uniqueTransformation)){
            tempArray.push(uniqueTransformation)   
        };
    };    
    return tempArray.length;
};
