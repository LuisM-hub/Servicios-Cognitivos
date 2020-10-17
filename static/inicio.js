var btn = document.getElementById('boton');

btn.addEventListener("click", function(){
    var info = document.getElementById('text').value;
    var consulta = new XMLHttpRequest();
    consulta.open('GET','http://127.0.0.1:5000/json');
    consulta.onload = function() {
        console.log("Cargo");
        var datos = JSON.parse(consulta.responseText);
        console.log(datos[0].text)
    };
    consulta.send();
});


