# 🏆 Automação da Tabela do Brasileirão (Web Scraping)

Este é um projeto em Python desenvolvido para fins de aprendizado de **Web Scraping** (Extração de Dados da Web). O script conecta-se ao site estatístico *Chance de Gol*, extrai a tabela de classificação e probabilidades do Campeonato Brasileiro Série A, limpa os dados e os exibe de forma organizada diretamente no terminal.

---

## 🚀 Tecnologias Utilizadas

O projeto foi construído utilizando as seguintes bibliotecas do ecossistema Python:

*   **Python 3** (Linguagem base)
*   **Requests:** Para fazer a requisição HTTP e baixar o conteúdo HTML do site de forma automatizada.
*   **BeautifulSoup4:** Para analisar (fazer o *parse*) do HTML estruturado da página.
*   **Pandas:** Para capturar as tabelas HTML, processar os dados na memória (via `StringIO`) e limpar espaços indesejados.
*   **Tabulate:** Para renderizar a tabela final no terminal no formato Markdown visualmente limpo.

---

## 🛠️ Como o Projeto Funciona

O script executa os seguintes passos de automação:
1. Simula um acesso humano enviando um `User-Agent` nos cabeçalhos da requisição.
2. Faz o download do código HTML do site *Chance de Gol*.
3. Varre o documento em busca de tabelas específicas que contenham colunas como `Time` ou `Pts`.
4. Utiliza a biblioteca `io.StringIO` para injetar o texto de forma segura na memória do Pandas, evitando bugs de leitura de arquivos locais do sistema operacional.
5. Limpa formatações em branco e quebras de linha (`.strip()`) vindas das tags HTML `<pre>`.
6. Imprime a classificação atualizada formatada em Markdown no terminal.

> **Nota Estatística:** Os dados capturados refletem as projeções matemáticas e probabilísticas da rodada calculada pelo portal, e não necessariamente o placar ao vivo minuto a minuto da rodada de hoje.

---

## 📋 Como Executar o Projeto

### Pré-requisitos
Você precisará do Python instalado e das bibliotecas necessárias. Para instalá-las de uma vez só, execute no seu terminal:

```bash
pip install requests pandas beautifulsoup4 tabulate