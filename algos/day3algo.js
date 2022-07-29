/**
 * @param arr is a list<int>
 * @returns list<int>
 */
 export function deduplicateSortedArray(arr) {
    for(var i =0;i<arr.length;i++){
      if( arr[i-1]== arr[i]){
        console.log(arr[i],arr[i+1])
        arr.splice(i, 1)
        i--
      }
      else {
        continue
      }
    }
  return arr
    // Write your solution here!
  }