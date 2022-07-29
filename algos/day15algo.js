// binary string expansion
// given an input like "1?0?", return an array of all possible outputs you can
// create by replacing the characters "?" with either "0" or "1"
// in the example "1?0?", our output would be something like
// ["1101", "1100", "1001", "1000"]
// (the order may be different depending on how you write the function)
// this algorithm probably needs at least one or two other parameters to
// function properly - there's a few different ways of imagining it
// remember some of the things we've talked about, like passing data between
// function calls, and using default parameters

function binaryStringExpansion(input, output = []) {

    
    var string = input.split("")
    
    for(var x = 0; x < string.length; x++){
        if(string[x] == "?")
            console.log("question")
    }

    return output;
}

console.log(binaryStringExpansion("1?0?")) // should contain 4 items
//console.log(binaryStringExpansion("?1?0?")) // should contain 6 items
//console.log(binaryStringExpansion("????")) // should contain 8 items

// with group -

function binaryStringExpansion(input, resultsArr){
    if (typeof(resultsArr)==='undefined') resultsArr = [];
    for( var i = 0; i<input.length; i++ ){
        if(input[i] === "?"){
            break
        }
    }

    if ( i >= input.length ){
        resultsArr.push(input);
        return
    }

    // branch for 0
    input0 = input.slice(0,i) + 0 + input.slice(i+1)
    binaryStringExpansion(input0, resultsArr);

    // branch for 1
    input1 = input.slice(0,i) + 1 + input.slice(i+1)
    binaryStringExpansion(input1, resultsArr);

    return resultsArr
}