function interleaveArrays(arrayA, arrayB) {
    var newArr = [];
    diff = arrayA.length - arrayB.length //if positive arrayA larger if negative arrayB larger if 0 ???
  
    // if(diff > 0){
    //   // arrayA larger than B
    // }
    // if(diff < 0){
    //   // arrayB larger than A
    //   for(var i=0; i<arrayA.length; i++){
    //     newArr.push(arrayA[i])
    //     newArr.push(arrayB[i])
    //   }
      
    // }
    // if(diff == 0){
    //   // array equal length
    // }
    if(arrayB.length == 0){
      return arrayA
    }
    else if(arrayB.length == 0){
      return arrayB
    }
  
    var newArr = [];
    for(var x = 0; x<arrayA.length; x++){
      newArr.push(arrayA[x]);
      newArr.push(arrayB[x])
    }
  
    if(arrayA.length > arrayB.length){
      var diff = arrayA.length - arrayB.length
      for(var i = 0; i<diff; i++){
        newArr.push(arrayA[arrayB.length + i])
      }
    }
    else if(arrayB.length > arrayA.length){
      var diff = arrayB.length - arrayA.length
      for(var i = 0; i<diff; i++){
        newArr.push(arrayB[arrayA.length + i])
      }
    }
    return newArr
    // Write your solution here!
  }
  