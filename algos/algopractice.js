function closestMultiple10(num){
    var decimal = num % 10;
    var num2 = 0
    if(decimal < 5){
        num2 = Math.floor(num/10)*10;
    }
    else if(decimal >= 5)
        num2 =Math.ceil(num/10)*10;

    return num2
}

console.log(closestMultiple10(22))
console.log(closestMultiple10(25))
console.log(closestMultiple10(37))