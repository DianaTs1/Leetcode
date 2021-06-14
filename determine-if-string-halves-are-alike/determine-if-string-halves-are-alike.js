/**
 * @param {string} s
 * @return {boolean}
 */
var halvesAreAlike = function(s) {
    let vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'];
    
    // Split the word
    let half = s.length/2;
    let partA = s.slice(0,half);
    let partB = s.slice(half, s.lenght);
    
    // Count vowels
    let countA = 0;
    let countB = 0;
    for (let i=0; i<partA.length; i++){
        if (vowels.includes(partA[i])){
            countA ++;
        };
        if (vowels.includes(partB[i])){
            countB ++;
        };
    };
    return countA === countB; 
};
