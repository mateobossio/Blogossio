boton = document.getElementById("btn1");
    var cont=0;
    function Change(button){
        if (cont==0){
            number = Math.floor((Math.random() * 80) + 1);
            boton.setAttribute("style" , "margin-left:" + number + "%");
            console.log(number+"%");
            window.alert("MUY LENTOSSIO");
            cont=1;
        }else{
            number = Math.floor((Math.random() * 80) + 1);
            boton.setAttribute("style" , "margin-left:" + number + "%");
            console.log(number+"%");
        }
    }
    function Mensaje(){
        var name=document.getElementById("name").value;
        if (name!=""){
            window.alert("Bienvenido "+name+" al clubossio");
        }else{
            window.alert("No tiene lo que hace falta para ser un Bossio");    
        }
    }