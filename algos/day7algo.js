function bookIndex(pages) {
    var testarr = [];
    i = 0;
    for(var x = 0; x < pages.length; x++){
    while(pages[i]-pages[i+1] == 1){
        testarr.push(pages[i])
        i++;
    }
}
    console.log(testarr);
}
    

bookIndex([1,2,3,6,7,9,11,12,13,17]);