//https://www.learnwithtrace.com/problems/6069286/code
var arr = [1,2,3,4,5];
var shiftBy = 3

function rotateArray(arr, shiftBy) {
    for(var x=0;x<arr.length;x++){ //pushing first vals to array
        var temp = arr[arr.length-shiftBy];
        arr.push(temp);
    }
        return arr;
    // Write your solution here!
}
rotateArray();