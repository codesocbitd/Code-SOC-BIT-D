document.addEventListener('DOMContentLoaded',(event)=>{
    var moveSequence = []
    var boardState = []
    var colState = [5,5,5,5,5,5,5]
    for(var i = 0;i<6;i++){
        var row = []
        for(var j=0;j<7;j++){
            row.push(0);
        }
        boardState.push(row);
    }
    var count = 0
    var color = [1,2]

    console.log("Hello World")
    // Code
    var turn = 1;
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
        var circle_elements = document.getElementsByClassName("circle")

        for(var i=0;i<=41;i++){
            var circle =  document.getElementById(i.toString())
            //console.log(circle)
            circle.addEventListener("mouseover",(event)=>{
                //console.log("Circle Click detected")
                var ele = event.srcElement.id;
                row = Math.floor(ele/7)
                col = ele%7;

                if(boardState[row][col] == 0){
                    if(turn == 1)
                    circle_elements[ele].style.backgroundColor = "blue"
                    else
                    circle_elements[ele].style.backgroundColor = "yellow"
    
                }
                else{
                    console.log("Filled")
                }

                
            })
            circle.addEventListener("mouseout",(event)=>{
                //console.log("Circle Click detected")
                var ele = event.srcElement.id;
                row = Math.floor(ele/7)
                col = ele%7;
                if(boardState[row][col] == 0){
                    circle_elements[ele].style.backgroundColor = "brown"
                }
                
            })
            circle.addEventListener("click",(event)=>{
                //console.log("Circle Click detected")
                var ele = event.srcElement.id;
                row = Math.floor(ele/7)
                col = ele%7;
                if(colState[col]>=0){
                    var  filledRow = colState[col]
                    boardState[filledRow][col] =  color[(count++)%2]
                    moveSequence.push(col)
                    if( turn == 1)
                    circle_elements[filledRow*7+col].style.backgroundColor = "blue"
                    else
                    circle_elements[filledRow*7+col].style.backgroundColor = "yellow"
                    turn = 1 - turn 
                    colState[col]--;

                }
                
            })


        }




})
