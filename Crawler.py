import re
import threading
import requests
from bs4 import BeautifulSoup

# Definindo o domínio base e a URL da página de automóveis
dominio = "https://django-anuncios.solyd.com.br"
url_automoveis = "https://django-anuncios.solyd.com.br/automoveis/"

# Listas para armazenar os links de anúncios e os números de telefone encontrados
links_lista = []
telefones_lista = []

# Função para realizar requisições HTTP
def requisicao(url):
    try:
        resposta = requests.get(url)
        if resposta.status_code == 200:
            return resposta.text
        else:
            print("Ocorreu um erro na requisição")
    except Exception as error:
        print("Ocorreu um erro na requisição")
        print(error)

# Função para realizar o parsing do HTML usando BeautifulSoup
def parsing(resposta_html):
    try:
        soup = BeautifulSoup(resposta_html, 'html.parser')
        return soup
    except Exception as error:
        print("Erro ao fazer o parsing")
        print(error)

# Função para encontrar os links dos anúncios na página
def encontrar_anuncios(soup):
    anuncios = []
    try:
        cards_pai = soup.find("div", class_="ui three doubling link cards")
        cards = cards_pai.find_all("a", class_="card")
        for card in cards:
            try:
                link = card['href']
                anuncios.append(link)
            except:
                print("Erro ao encontrar links")
    except:
        pass
    return anuncios

# Função para encontrar os números de telefone na descrição do anúncio
def encontrar_telefone(soup):
    try:
        descricao = soup.find_all("div", class_="sixteen wide column")[2].p.get_text()
        # [2]: Acessa o terceiro elemento na lista de elementos encontrados.
        # Acessa a tag <p> (parágrafo) dentro do terceiro elemento <div>.
        # .get_text(): Extrai o texto contido na tag <p>
    except:
        print("Erro ao encontrar descrição")
        return None

    regex = re.findall(r"\(?0?([1-9]{2})[ \-\.\)]{0,2}(9[ \-\.]?\d{4})[ \-\.]?(\d{4})", descricao)

    if regex:
        return regex

# Função para descobrir números de telefone
def descobrir_telefone():
    while True:
        try:
            link_anuncio = links_lista.pop(0)
        except:
            return None

        resposta_anuncio = requisicao(dominio + link_anuncio)

        if resposta_anuncio:
            soup_anuncio = parsing(resposta_anuncio)
            if soup_anuncio:
                telefones = encontrar_telefone(soup_anuncio)
                if telefones:
                    for telefone in telefones:
                        print("Telefone encontrado: ", telefone)
                        telefones_lista.append(telefone)
                        salvar_telefones(telefone)



# salvando os telefones em um arquivo csv

def salvar_telefones(telefone):
    string_telefone = f"({telefone[0]}) {telefone[1]}-{telefone[2]}\n"

    try:
        # abrindo o arquivo 
        with open("telefones.csv", "a") as arquivo:
            # convertendo de tupla para string
            arquivo.write(str(string_telefone))
    
    except Exception as error:
        print("Erro ao salvar o arquivo")
        print(error)
   



# Realizando a requisição à página de automóveis

if __name__ == "__main__":
    resposta_busca = requisicao(url_automoveis)
    if resposta_busca:
        soup_busca = parsing(resposta_busca)
        if soup_busca:
            links_lista = encontrar_anuncios(soup_busca)
            threads = []

            # Criando e iniciando threads para descobrir números de telefone
            for i in range(10):  # O 10 representa quantas threads você quer
                t = threading.Thread(target=descobrir_telefone)
                threads.append(t)
            for t in threads:
                t.start()

            # Aguardando o término de todas as threads
            for t in threads:
                t.join()



        


        
        # thread1 = threading.Thread(target=descobrir_telefone)
        # thread2 = threading.Thread(target=descobrir_telefone)
        # thread3 = threading.Thread(target=descobrir_telefone)
        # thread1.start()
        # thread2.start()
        # thread3.start()
        # thread1.join()
        # thread2.join()
        # thread3.join()

        #print(telefones_lista)
        
            
    # print(soup.title.text.strip())
    # links = soup.find_all("a")
    # for link in links:
    #     print(link['href'])






