$(document).ready(function(){

    getProdutosAdolescentes()

})

async function getProdutosAdolescentes(){

    try {

        const response = await fetch("./dados/adolescentes.json")
        const data = await response.text()
        const dados = JSON.parse(data)

        var tabAdolescentes = document.getElementById('adolescentes')
        tabAdolescentes.innerHTML = ''

        dados.forEach(elemento => {
            
            tabAdolescentes.innerHTML += '<tr>'+
                                        '<td>' + elemento.nome + '</td>'+
                                        '<td>' + 'R$ ' + elemento.preco + '</td>'+
                                        '<td>' + elemento.status + '</td>'+
                                    '</tr>'
        });

    } catch (error) {
        console.error(error)
    }
}