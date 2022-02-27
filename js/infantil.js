$(document).ready(function(){
    fetch("https://omahteu.github.io/dados/infantil.json", {
        method: 'get',
        headers: new Headers({
            'test': 'test'
        })
    })
    .then(response => {
       return response.json();
    })
    .then(function(myBlob) {
        var objectURL = myBlob;

        var tabInfantil = document.getElementById('infantil')
        tabInfantil.innerHTML = ''
        
        for(var i = 0; i < objectURL.length; i++){
            //console.log(objectURL[i])

            Object.keys(objectURL[i]).forEach(function(item){
                // console.log(item + " X " + objectURL[i][item]);
                // console.log(objectURL[i][item][1]);
                var nomes = item
                var preco = objectURL[i][item][0]
                var status = objectURL[i][item][1]


                tabInfantil.innerHTML += '<tr>'+
                                    '<td>' + nomes + '</td>'+
                                    '<td>' + 'R$ ' + preco + '</td>'+
                                    '<td>' + status + '</td>'+
                                '</tr>'
                
               });

        }
    })
})