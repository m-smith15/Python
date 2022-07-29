//https://www.learnwithtrace.com/problems/b21f5f2/code

//example [3,4,9,2,4,-2,3]

export function arrayBalanceIndex(arr) {
    for(var x=0; x<arr.length; x++){
      //redeclaring vars in JS works...but is it smart? Probs not
      var leftsum = 0;
      var rightsum = 0;
      for(var i=0; i<arr.length; i++){
        if(i > x) {
          rightsum += arr[i];
          //console.log(rightsum);
        }
        else if(i < x){
          leftsum += arr[i]
          //console.log(leftsum)
        }
      }
      if(leftsum == rightsum){
        return x;
      }
    }
      return -1
  }