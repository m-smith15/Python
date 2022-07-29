// floodFill(canvas, x, y, target)
// canvas is an array of array of numbers representing
// colored pixels (think MSPaint)
// x, y is your start point, target is your new "color"
// change the value at x, y on the canvas to
// the target value, then all points on the canvas 
// that were the original color and contiguous with the 
// point at x, y (no diagonals!) to the target color.
//
// example, if canvas is:
// [[3, 2, 4, 4, 4],
//  [4, 4, 4, 3, 3],
//  [4, 1, 1, 4, 4]]
// x, y is 2, 1  and target is 0
// canvas becomes:
// [[3, 2, 0, 0, 0],
//  [0, 0, 0, 3, 3],
//  [0, 1, 1, 4, 4]]
//
// another example, if canvas is:
// [[1, 0, 2, 0, 1],
//  [1, 0, 1, 1, 0],
//  [1, 0, 1, 0, 0],
//  [2, 0, 0, 2, 1]]
// x, y is 1, 2 and target is 9
// canvas becomes:
// [[1, 9, 2, 0, 1],
//  [1, 9, 1, 1, 0],
//  [1, 9, 1, 0, 0],
//  [2, 9, 9, 2, 1]]
// if x, y was intead 2, 1 and target was 9
// canvas would become:
// [[1, 0, 2, 0, 1],
//  [1, 0, 9, 9, 0],
//  [1, 0, 9, 0, 0],
//  [2, 0, 0, 2, 1]]
// you don't need to return anything,
// but if you feel the need to, use null or undefined
// make sure you don't modify anything outside your canvas area


function floodFill(canvas, x, y, target) {
    console.log(sample_input[y][x])
    var varValue = sample_input[y][x]
    sample_input[y][x] = target
    console.log(sample_input[y][x])

if(sample_input[y-1] != undefined){
    if(sample_input[y - 1][x] == varValue){ // x - 1
        // x = x - 1
        // console.log("x - 1" + x)
        floodFill(sample_input,x,y - 1,target)
    }
}

if(sample_input[y+1] != undefined){
    if(sample_input[y + 1][x] == varValue){ // x + 1
        // x = x + 1
        // console.log("x + 1" + x)
        floodFill(sample_input,x,y + 1,target)
    }
}

if(sample_input[x-1] != undefined){
    if(sample_input[y][x - 1] == varValue){ // y - 1
        // y = y - 1
        // console.log("y - 1" + y)
        floodFill(sample_input,x - 1,y,target)
    }
}
if(sample_input[x-1] != undefined){
    if(sample_input[y][x + 1] == varValue){ // y + 1
        // y = y + 1
        // console.log("y + 1" + y)
        floodFill(sample_input,x + 1,y,target)
    }
}

}

var sample_input = [[1, 0, 1, 1, 1],
                    [0, 1, 1, 1, 0],
                    [1, 0, 1, 0, 0]]
floodFill(sample_input, 1, 1, 9)

console.log(sample_input)
// should return:
// [[1, 0, 9, 9, 9],
//  [0, 9, 9, 9, 0],
//  [1, 0, 9, 0, 0]]

// create your own test cases!