export function intersectionOfSortedArrays(array1, array2) {
    //create dict looping through arrays
    var tempDict = {}
    for(var x=0; x<array1.length; x++){
        if(tempDict[array1[x]] == null){
          tempDict[array1[x]] = 0;
        }
        tempDict[array1[x]] += 1;
    }
    var tempDict2 = {}
    for (x=0; x<array2.length; x++){
        if(tempDict2[array2[x]] == null){
          tempDict2[array2[x]] = 0;
        }
        tempDict2[array2[x]] += 1;
    }
    var output = [];
    for(var key in tempDict){
  
      if(key in tempDict2){
        key = parseInt(key);
        //var deleteMe = Math.abs(tempDict2[key] - tempDict[key]); 
        if(Math.abs(tempDict2[key] - tempDict[key]) == 1 && tempDict[key] > 1){
          output.push(key);
        }
        //key = parseInt(key);
        output.push(key);
        }
      }
      return output;
    // Write your solution here!
  }