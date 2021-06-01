/**
 * @param {string} s
 * @return {string}
 */
var sortSentence = function(s) {
        let temp_list = s.split(" ");
        temp_dict = {};
        
        for (let elem of temp_list){
            let index = elem.slice(-1);
            temp_dict[index] = elem.substring(0, elem.length-1);
        };
        final_list = Object.values(temp_dict);
    
    return final_list.join(" ");
};