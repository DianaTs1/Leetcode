/**
 * @param {number[][]} rectangles
 * @return {number}
 */
var countGoodRectangles = function(rectangles) {
    
    let maxLength = [];
    
    for (let rect of rectangles){
        maxSide = Math.min.apply(null, rect)
        maxLength.push(maxSide)
    };
    
    let maxSideRectangle = Math.max.apply(null, maxLength);    
    
    return maxLength.filter(x => x==maxSideRectangle).length;
};
