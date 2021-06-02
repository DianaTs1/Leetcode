/**
 * @param {string} s
 * @return {string}
 */
var replaceDigits = function(s) {
    
    let finalString = "";
    
    //Create a swift function
    function swift(char, num){
    
        // Change the ascii value of the char variable
        let newAsciiVal = char.charCodeAt() + Number(num);
        
        // Change char value with new ascii value and return new char
        return String.fromCharCode(newAsciiVal);
    };
        
    //replace odd-indexed numbers with characters
    for (let index=0; index < s.length; index ++){
        // push previous value and shift function return values to finalString
        if (index % 2 == 0) finalString += s[index];
        else finalString += swift(s[index-1], s[index]);
    };
    return finalString;
};
