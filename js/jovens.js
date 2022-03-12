$(document).ready(function(){

    getProdutos()
    
})

async function getProdutos(){

    try {
        
        const response = await fetch("./dados/jovens.json")
        const data = await response.text()
        const dados = JSON.parse(data)

        var tabJovens = document.getElementById('jovens')
        tabJovens.innerHTML = ''

        dados.forEach(elemento => {
            
            tabJovens.innerHTML += '<tr>'+
                                        '<td>' + elemento.nome + '</td>'+
                                        '<td>' + 'R$ ' + elemento.preco + '</td>'+
                                        '<td>' + elemento.status + '</td>'+
                                    '</tr>'
        });

    } catch (error) {
        console.error(error)
    }
}