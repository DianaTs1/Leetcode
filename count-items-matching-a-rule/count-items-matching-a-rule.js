/**
 * @param {string[][]} items
 * @param {string} ruleKey
 * @param {string} ruleValue
 * @return {number}
 */
var countMatches = function(items, ruleKey, ruleValue) {
    let count = 0;
    
    for (let elem of items){
        if(elem[0] === ruleValue && ruleKey === "type"){
           count ++;
           };
        if(elem[1] === ruleValue && ruleKey === "color"){
           count ++;
           };
        if(elem[2] === ruleValue && ruleKey === "name"){
           count ++;
           };
    };
    
    return count;
};
