function binarySearch(arr, target, searchParam = []) {
    length = Math.floor(arr.length)

    if (arr[length/2] = target){ 
        return true
    }
    if(arr[lenght/2] > target){ //greater than
        searchParam = arr.slice(0,length/2);
        binarySearch(arr, target)
    }
    if(arr[length/2] < target){ //less than
        searchParam = arr.slice(arr.length/2, arr.length);
        binarySearch(arr, target)
    }

}

var arr = [1, 2, 3, 4, 6, 7, 9, 11, 12]
console.log(binarySearch(arr, 1) == true)
console.log(binarySearch(arr, 2) == true)
console.log(binarySearch(arr, 3) == true)
console.log(binarySearch(arr, 4) == true)
console.log(binarySearch(arr, 6) == true)
console.log(binarySearch(arr, 7) == true)
console.log(binarySearch(arr, 9) == true)
console.log(binarySearch(arr, 11) == true)
console.log(binarySearch(arr, 12) == true)

console.log(binarySearch(arr, 5) == false)
console.log(binarySearch(arr, 8) == false)
console.log(binarySearch(arr, 10) == false)

console.log(binarySearch(arr, -3) == false)
console.log(binarySearch(arr, 21) == false)