/**
 * @param {number[][]} mat
 * @return {number}
 */
var diagonalSum = function(mat) {
       let sum = 0
       let length = mat.length-1
        
        // add elments of the primary and secondary diagolans
        for (let i=0; i<mat.length; i++){
            sum += mat[i][i];
            sum += mat[i][length];
            length -= 1;
        };
        
        //if the lenght of mat is odd, subtract the middle number that has been added twice
        if (mat.length % 2 === 1){
            length = mat.length -1;
            sum -= mat[length/2][length/2];
            };
    
        return sum;
};
