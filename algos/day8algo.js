function isAnagram(string_a, string_b) {
    var emptyArr = string_a.toLowerCase();
    var emptyArr2 = string_b.toLowerCase();
    emptyArr = emptyArr.replace(/ /g,"");
    emptyArr2 = emptyArr2.replace(/ /g,"");

    if(emptyArr.length !== emptyArr2.length){
        return false
    }
    
    var emptyDict = {};
    for(var x=0; x < emptyArr.length; x++){
        if(emptyDict[emptyArr[x]] == null){
            emptyDict[emptyArr[x]] = 0
        }
        emptyDict[emptyArr[x]] += 1;
    }

    var emptyDict2 = {};
    for(var x=0; x < emptyArr2.length; x++){
        if(emptyDict2[emptyArr2[x]] == null){
            emptyDict2[emptyArr2[x]] = 0
        }
        emptyDict2[emptyArr2[x]] += 1;
    }

    if(Object.keys(emptyDict).length !== Object.keys(emptyDict2).length){
        return false
    }
    for(var key in emptyDict){
        if(emptyDict[key] !== emptyDict2[key]){
            return false
        } 
        else{
            return true
        }
    }
}


console.log(isAnagram("abbba","abbba"))