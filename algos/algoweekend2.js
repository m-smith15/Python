function orderedCount(text) {
    tempArr = text.split("");
    //console.log(tempArr)
    tupleList = [];
    //emptyDict = {};
    //loop through the array given to add key along with count of occurance to dictionary
    for(var x = 0; x< tempArr.length; x++){
        var index = tupleList.map((o) => o[0]).indexOf(tempArr[x].toString())
        if(index == -1){
            // console.log(emptyDict[tempArr[x]])
            //emptyDict[tempArr[x]] = 0;
            tupleList.push([tempArr[x], 1])
            //console.log("added key");
        }
        else{
        //emptyDict[tempArr[x]] += 1;
        //var index = tupleList.map((o) => o[0]).indexOf(tempArr[x].toString());
        // console.log("index of"+tempArr[x]+" in 'tuplesList': " + index);
            tupleList[index][1] += 1
        }
        }
    return tupleList;
}
//console.log(orderedCount("abracadabra"))// [['a', 5], ['b', 2], ['r', 2], ['c', 1], ['d', 1]]
//console.log(orderedCount("Code Wars")) // [['C', 1], ['o', 1], ['d', 1], ['e', 1], [' ', 1], ['W', 1], ['a', 1], ['r', 1], ['s', 1]]
console.log(orderedCount("233312")) // [ [ '2', 2 ], [ '3', 3 ], [ '1', 1 ] ]

//this is nifty for pushing the key and values from dict into another object. Not what we are looking for here but keeping for notes
        // for (const [key,value] of Object.entries(emptyDict)) {
        //     tupleList.push(key, value)
        // }

//leaving in lots of old notes and lessons learned here. The big take away was being able to find the INDEXOF the tupleList to implement a count function accordingly
//Dictionary was used initially, but dictionary would SORT key values - question is asking for results in order they appear.
// also d'oh read the problem before you start hammering away at code, self