# Descoberta de Números de Telefone em Anúncios

Este é um programa em Python que realiza a descoberta de números de telefone em anúncios de automóveis em um site específico. Ele utiliza a biblioteca `requests` para fazer requisições HTTP, a biblioteca `BeautifulSoup` para analisar o HTML da página e a biblioteca `re` para encontrar padrões de números de telefone.

## Funcionamento

O programa realiza as seguintes etapas:

1. Faz uma requisição HTTP à página de automóveis especificada.
2. Analisa o HTML da resposta usando a biblioteca `BeautifulSoup`.
3. Encontra os links dos anúncios na página.
4. Inicia várias threads para descobrir números de telefone em paralelo a partir dos anúncios encontrados.
5. Utiliza expressões regulares para identificar números de telefone na descrição dos anúncios.
6. Salva os números de telefone encontrados em um arquivo CSV.

## Como usar

1. Certifique-se de ter o Python instalado em sua máquina.

2. Instale as bibliotecas necessárias listadas no arquivo `requirements.txt`. Isso pode ser feito com o seguinte comando:

   ```bash
   pip install -r requirements.txt
Copie o código fornecido para um arquivo .py.

Execute o arquivo Python. O programa buscará e descobrirá números de telefone em anúncios de automóveis no site especificado.

Observações
Este código é um exemplo de como utilizar threads para realizar tarefas em paralelo, como a descoberta de números de telefone. No entanto, nem todos os sites permitem a extração de informações dessa forma. Verifique os termos de uso e as políticas do site antes de realizar esse tipo de atividade.

O código não lida com possíveis erros de conexão, problemas na página da web ou mudanças na estrutura do site. Em um ambiente de produção, você deve adicionar tratamento de erros e verificações adicionais.

Lembre-se de que a utilização de threads envolve considerações de concorrência e sincronização. Este exemplo utiliza threads simples, mas em situações mais complexas, outras abordagens podem ser necessárias.
