document.addEventListener('DOMContentLoaded',(event)=>{

    console.log("Hello World")
    // Code
    var board1= document.getElementById("board1")
    var count = 0;
    for(var i=0;i<6;i++){
        var row1 = document.createElement("div");
        row1.classList.add("row")
        for(var j=0;j<7;j++){
            var circle = document.createElement("div")
            circle.classList.add("circle")
            circle.id = count.toString();
            row1.appendChild(circle);
            count++;
        }
        board1.appendChild(row1);

    }


})