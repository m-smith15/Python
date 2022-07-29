// Binary Search. Given sorted array rreturn whether the array contains that value. Don't iterate through the array instead divide and conquer (start at middle, decide to look to left or right)


function searchBinary(array, searchNum, expected) {
    var arraypos = Math.round(array.length/2 - 1); 
    console.log(arraypos +" starting");
    console.log(searchNum)
    console.log(array[arraypos])

    while (arraypos < 0 || arraypos > array.length){

        console.log(array[arraypos])
        console.log(searchNum)
        if(searchNum < array[arraypos]){
            arraypos--
            console.log("increase by 1")
            
        } //if
        if(searchNum > array[arraypos]){
            arraypos++
            console.log("increase by 1")
            
        } //if
        if(searchNum == array[arraypos]){
            expected = true
            console.log("found match at array position" + arraypos)
            break
        }
    } //while
    return expected
}

var array = [1,3,5,6];
var searchNum = 4;
var expected = false;
console.log(searchBinary(array, searchNum, expected))


// const array = [4, 5, 6, 8, 12];
// const searchNum = 5;
// const expected = true;
// console.log(searchBinary())