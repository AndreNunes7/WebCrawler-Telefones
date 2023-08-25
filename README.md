# Descoberta de Números de Telefone em Anúncios

Este é um programa em Python que utiliza threads para descobrir números de telefone em anúncios de automóveis em um site específico. Ele faz uso das bibliotecas `requests`, `BeautifulSoup` e `re` para realizar as operações necessárias.

## Funcionamento

O programa segue as etapas abaixo:

1. Faz uma requisição HTTP à página de anúncios de automóveis.
2. Analisa o HTML da resposta usando a biblioteca `BeautifulSoup` para extrair informações relevantes.
3. Encontra os links dos anúncios na página.
4. Utiliza threads para processar múltiplos anúncios em paralelo.
5. Procura por números de telefone na descrição de cada anúncio usando expressões regulares.
6. Armazena os números de telefone encontrados em um arquivo CSV.

## Como usar

1. Certifique-se de ter o Python instalado em sua máquina.

2. Instale as bibliotecas necessárias listadas no arquivo `requirements.txt`. Execute o seguinte comando no terminal:

   ```bash
   pip install -r requirements.txt

Observações
Este código ilustra o uso de threads para realizar tarefas simultaneamente. No entanto, é importante lembrar que nem todos os sites permitem a coleta automatizada de dados. Sempre verifique os termos de uso do site antes de realizar scraping.

O código não lida com possíveis erros de conexão, mudanças na estrutura do site ou outras situações excepcionais. Em ambientes de produção, é recomendável adicionar tratamento de erros mais robusto.

Lembre-se de que a utilização responsável e ética de scraping de dados é fundamental. Certifique-se de seguir as políticas e regulamentos do site que você está acessando.

A utilização de threads envolve considerações de concorrência e sincronização. Este exemplo utiliza threads simples, mas em cenários mais complexos, abordagens mais avançadas podem ser necessárias.
