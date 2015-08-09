
var Int2;
        Int2 = setInterval(progress, 50);
        var Int1;
        Int1 = setInterval(ChangeImg, 5000);
        var img = [ruta + "originalossio.png", ruta + "diegossio.png", ruta + "chiquitossio.png",ruta + "pequeniossio.png",];
        console.log(img);
        var asd = 0;
        var cont =0;
        function ChangeImg(){
            number = Math.floor((Math.random() * 4) + 0);
            if (asd!=number){
                document.getElementById("imagen").setAttribute("src", img[number]);
                asd = number;
                cont = 0;
            }else{
                cont=cont+1;
                if (cont<3){
                   ChangeImg();
                }else{
                    document.getElementById("imagen").setAttribute("src", img[number+1]);
                }
                }


            }
        count=0; 
        function progress() {
            if (document.images["bar"].width < 493) {
                document.images["bar"].width += 5;
                document.images["bar"].height = 15;
                count = count + 1;
                document.getElementById("%").setAttribute("value",count + " %");
            }else {
                count = 0;
                document.images["bar"].width = 0;
            }
        }