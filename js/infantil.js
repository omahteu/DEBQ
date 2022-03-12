$(document).ready(function(){

    getProdutos()
})

async function getProdutos(){

    console.log('iniciando...')

    try {
        const response = await fetch("../dados/infantil.json")
        const data = await response.json()
        
        console.log(data)
        // var stringified = JSON.stringify(data);
        // var parsedObj = JSON.parse(stringified);
    
        // var objectURL = parsedObj;

        var tabInfantil = document.getElementById('infantil')
        tabInfantil.innerHTML = ''

        data.forEach(elemento => {

            tabInfantil.innerHTML += '<tr>'+
                                '<td>' + elemento.nome + '</td>'+
                                '<td>' + 'R$ ' + elemento.preco + '</td>'+
                                '<td>' + elemento.status + '</td>'+
                            '</tr>'
        })

    } catch (error) {
        console.error(error)
    }
}

function show(dados){

    dados.forEach(function(item){
        console.log(item[0])
    })
}
