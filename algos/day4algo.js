export function bubbleSort(arr) {
    var temp = 0;
    for(var y=0; y<arr.length; y++){
    for(var x=0; x<arr.length; x++){
        var current = arr[x]
        var ahead = arr[x+1]
        if(current > ahead){
            arr[x] = ahead;
            arr[x+1] = current;
        }
    }
    }
    return arr
}