from bs4 import BeautifulSoup
from urllib.request import urlopen
from json import dump

nomes_revistas = []
precos_revistas = []
dados = []
status = []


class Livia:
    def __init__(self):
        self.url = None

    @staticmethod
    def registrar(caminho):
        with open(f'dados/{caminho}.json', 'w') as json_file:
            dump(dados, json_file, indent=4, ensure_ascii=False)
    
    def infantil(self, url):
        self.url = url
        url = url

        response = urlopen(url)
        html = response.read()
        soup = BeautifulSoup(html, 'html.parser')

        cards_produtos = soup.findAll('tr', {'class': 'GrupoxProduto'})
        cards_precos = soup.findAll('input', {'name': 'valor[]'})

        for produto in cards_produtos:
            nomes_revistas.append(produto.find('label').getText())

        for preco in cards_precos:
            precos_revistas.append(preco.get('value'))

        for it in cards_produtos:
            statu = it.find('b')
            if statu is None:
                statu = 'Disponível'
            status.append(statu)

        for n, p, s in zip(nomes_revistas, precos_revistas, status):
            s1 = str(s).replace('<b>', '')
            s2 = s1.replace('</b>', '')
            dd = {
                'nome': n,
                'preco': p,
                'status': s2
            }
            dados.append(dd)

        Livia.registrar('infantil')
        
        print("Arquivo Criado!")
        
        nomes_revistas.clear()
        precos_revistas.clear()
        dados.clear()
        status.clear()
        
    def adolescente(self, url):
        self.url = url
        url = url

        response = urlopen(url)
        html = response.read()
        soup = BeautifulSoup(html, 'html.parser')

        cards_produtos = soup.findAll('tr', {'class': 'GrupoxProduto'})
        cards_precos = soup.findAll('input', {'name': 'valor[]'})

        for produto in cards_produtos:
            nomes_revistas.append(produto.find('label').getText())

        for preco in cards_precos:
            precos_revistas.append(preco.get('value'))

        for it in cards_produtos:
            statu = it.find('b')
            if statu is None:
                statu = 'Disponível'
            status.append(statu)

        for n, p, s in zip(nomes_revistas, precos_revistas, status):
            s1 = str(s).replace('<b>', '')
            s2 = s1.replace('</b>', '')
            dd = {
                'nome': n,
                'preco': p,
                'status': s2
            }
            dados.append(dd)

        Livia.registrar('adolescentes')
        
        print("Arquivo Criado!")
        
        nomes_revistas.clear()
        precos_revistas.clear()
        dados.clear()
        status.clear()
    
    def jovens(self, url):
        self.url = url
        url = url

        response = urlopen(url)
        html = response.read()
        soup = BeautifulSoup(html, 'html.parser')

        cards_produtos = soup.findAll('tr', {'class': 'GrupoxProduto'})
        cards_precos = soup.findAll('input', {'name': 'valor[]'})

        for produto in cards_produtos:
            nomes_revistas.append(produto.find('label').getText())

        for preco in cards_precos:
            precos_revistas.append(preco.get('value'))

        for it in cards_produtos:
            statu = it.find('b')
            if statu is None:
                statu = 'Disponível'
            status.append(statu)

        for n, p, s in zip(nomes_revistas, precos_revistas, status):
            s1 = str(s).replace('<b>', '')
            s2 = s1.replace('</b>', '')
            dd = {
                'nome': n,
                'preco': p,
                'status': s2
            }
            dados.append(dd)

        Livia.registrar('jovens')
        
        print("Arquivo Criado!")
        
        nomes_revistas.clear()
        precos_revistas.clear()
        dados.clear()
        status.clear()
    
    def adultos(self, url):
        self.url = url
        url = url

        response = urlopen(url)
        html = response.read()
        soup = BeautifulSoup(html, 'html.parser')

        cards_produtos = soup.findAll('tr', {'class': 'GrupoxProduto'})
        cards_precos = soup.findAll('input', {'name': 'valor[]'})

        for produto in cards_produtos:
            nomes_revistas.append(produto.find('label').getText())

        for preco in cards_precos:
            precos_revistas.append(preco.get('value'))

        for it in cards_produtos:
            statu = it.find('b')
            if statu is None:
                statu = 'Disponível'
            status.append(statu)

        for n, p, s in zip(nomes_revistas, precos_revistas, status):
            s1 = str(s).replace('<b>', '')
            s2 = s1.replace('</b>', '')
            dd = {
                'nome': n,
                'preco': p,
                'status': s2
            }
            dados.append(dd)

        Livia.registrar('adultos')
        
        print("Arquivo Criado!")
        
        nomes_revistas.clear()
        precos_revistas.clear()
        dados.clear()
        status.clear()
