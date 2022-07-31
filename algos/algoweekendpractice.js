function removeRotten(bagOfFruits){
    if(bagOfFruits[0] == null){
        return bagOfFruits;
    }
    
    for(var x = 0; x < bagOfFruits.length; x++){
        console.log(bagOfFruits[x])
        if(bagOfFruits[x].includes("rotten")){
            bagOfFruits[x] = bagOfFruits[x].replace('rotten','');
            bagOfFruits[x] = bagOfFruits[x].toLowerCase();
        }
    }
    return bagOfFruits
}

bagOfFruits = ["apple","rottenBanana","apple"]
console.log(removeRotten(bagOfFruits))

bagOfFruits = []
console.log(removeRotten(bagOfFruits))