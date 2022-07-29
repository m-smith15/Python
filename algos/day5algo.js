export function arrayOddOccurances(arr) {
    var temp = {}
    for(var i = 0; i < arr.length; i++){
      if(temp[arr[i]] == null){
        temp[arr[i]] = 0;
      }
      temp[arr[i]] += 1;
  
    }
    for(var key in temp){
      if(temp[key] % 2 == 1){
        return key;
      }
    }
  }

//given an array, return ODD occurance of values within array.
//arrays only have 1 odd occurance of value

//to convert to return ALL occurances of odd occurance, create array and push odd occurances to arry