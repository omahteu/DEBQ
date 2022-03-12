$(document).ready(function(){

    getProdutosAdultos()

})

async function getProdutosAdultos(){

    try {
        
        const response = await fetch("./dados/adultos.json")
        const data = await response.text()
        const dados = JSON.parse(data)

        var tabAdultos = document.getElementById('adultos')
        tabAdultos.innerHTML = ''

        dados.forEach(elemento => {
            
            tabAdultos.innerHTML += '<tr>'+
                                        '<td>' + elemento.nome + '</td>'+
                                        '<td>' + 'R$ ' + elemento.preco + '</td>'+
                                        '<td>' + elemento.status + '</td>'+
                                    '</tr>'
        });

    } catch (error) {
        console.error(error)
    }
}