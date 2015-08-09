var num = 0;
    var number = 0;
    function Convertir(){
        e = document.getElementById("comboloco");      
        asd = e.options[e.selectedIndex].value;
        a = document.getElementById("comboloco2");      
        dsa = a.options[a.selectedIndex].value;
        switch (asd) {
            case "1":
            num = 1;
            break;
            case "2":
            num = 8.87;
            break;
            case "3":
            num = 3.05;
            break;
            case "4":
            num = 0.93;
            break;
            case "5":
            num = 0.67;
            break;
            case "6":
            num = 26.60;
            break;
            case "7":
            num = 614.83;
            break;
            }
        switch (dsa) {
            case "1":
            number = 1;
            break;
            case "2":
            number = 8.87;
            break;
            case "3":
            number = 3.05;
            break;
            case "4":
            number = 0.93;
            break;
            case "5":
            number = 0.67;
            break;
            case "6":
            number = 26.60;
            break;
            case "7":
            number = 614.83;
            break;
            }
        var valor = document.getElementById("monto").value;
        if (valor!=""){
            monto = ((valor/num)*number);
            document.getElementById("vuelto").setAttribute("value", monto);
        }
        else{
            window.alert("No ha intrucido un monto");
        }
        }
        function suma(var1, var2) {
            return parseInt(var1) + parseInt(var2);   
        }
        reset=false;

        function ejecutar(botoncitodelacalculadorita) {
            aprieta = botoncitodelacalculadorita.value;
            val = document.getElementById("resultado").value;
            if (reset==true){
                document.getElementById("resultado").setAttribute("value", aprieta);
                reset=false;
            }
            else{
                if (aprieta=="="){
                    if (val.length!=0){
                        result = eval(val);
                        document.getElementById("resultado").setAttribute("value",result);
                        reset=true;
                    }
                }
                else{ document.getElementById("resultado").setAttribute("value",val+aprieta);
                }            

            }

        }

    var reloj=document.getElementById("reloj");
var marcha=0;
var cro=0;
function iniciar() {
         if (marcha==0) {
            emp=new Date();
            elcrono=setInterval(tiempo,10); 
            marcha=1;
          document.getElementById("btnPlay_Restart").innerHTML = '<input type="button" id=restart onclick=continuar() value=Start />';
            }
         }
function tiempo() {
         actual=new Date(); 
         cro=actual-emp;
         cr=new Date();
         cr.setTime(cro); 
         centesimas=cr.getMilliseconds();
         centesimas=centesimas/10;
         centesimas=Math.round(centesimas)
         segundos=cr.getSeconds();
         minutos=cr.getMinutes();
         if (centesimas<10) {centesimas="0"+centesimas;} 
         if (segundos<10) {segundos="0"+segundos;} 
         if (minutos<10) {minutos="0"+minutos;} 
         reloj.innerHTML= minutos+" : "+segundos+" : "+centesimas;
         }

function parar() { 
         if (marcha==1) {
            clearInterval(elcrono);
            marcha=0;
            }		
         }

function vuelta(){
    var vuelta = document.getElementById("reloj").innerHTML;
    var vueltas = document.getElementById("vueltas");
    var h3 = document.createElement("h3");
    h3.innerHTML = vuelta;
    vueltas.appendChild(h3);
}

function continuar() {
         if (marcha==0) { 
            emp2=new Date();
            emp2=emp2.getTime();
            emp3=emp2-cro;
            emp=new Date();
            emp.setTime(emp3);
            elcrono=setInterval(tiempo,10);
            marcha=1;
            }		
         }

function reiniciar() {
         if (marcha==1) { 
            clearInterval(elcrono); 
            marcha=0;
            }
     cro=0;
     reloj.innerHTML = "00 : 00 : 00";
    document.getElementById("btnPlay_Restart").innerHTML = '<input type="button" id=empezar onclick=iniciar() value=Start />';
         }	