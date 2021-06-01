/**
 * @param {number} n
 * @return {string[]}
 */
var fizzBuzz = function(n) {
    let final_array = []
    for (let i=1; i<n+1; i++){
        if (i % 15 === 0){
            final_array.push("FizzBuzz")
            }
        else if (i % 5 === 0){
            final_array.push("Buzz")
        }
        else if (i % 3 === 0){
            final_array.push("Fizz")
        }
        else {
            num = i.toString()
            final_array.push(num)
        };
    };
    return final_array
};
