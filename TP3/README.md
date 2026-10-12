# Lexer para Linguagem de Query (SPARQL-like)

Este projeto implementa um **analisador léxico (lexer)** em Python, desenvolvido para converter consultas (queries) estruturadas numa lista de tokens identificáveis.

## ⚙️ Como Funciona

O lexer lê uma string de texto bruto e utiliza expressões regulares (`re`) com grupos nomeados (`?P<NOME>`) e a flag `re.VERBOSE` para segmentar o código em componentes lógicos. 

A função principal `lertexto(texto)` percorre a query utilizando `re.finditer()` e extrai pares do tipo `(tipo, valor)` para cada elemento reconhecido.

## 📋 Regras de Identificação (Tokens)

O padrão reconhece os seguintes elementos da linguagem:

* **`COMENTARIO`**: Comentários iniciados por `#`.
* **`VARIAVEL`**: Identificadores começados por `?` (ex: `?nome`).
* **`LINGUA`**: Indicadores de idioma com `@` e duas letras (ex: `@en`).
* **`STRING`**: Textos delimitados por aspas (ex: `"Chuck Berry"`).
* **`DELIMITADOR`**: Carateres estruturais como `{`, `}` e `.`.
* **`LIMIT`**: Palavra reservada limite da query.
* **`NUMERICO`**: Valores inteiros.
* **`CONCEITO`**: Identificadores, propriedades e palavras-chave alfanuméricas (incluindo namespaces com `:`).

## 🚀 Exemplo de Utilização

```python
import re

def lertexto(texto):
    padrao = r"""
        (?P<COMENTARIO>\#.*)|
        (?P<VARIAVEL>\?[a-zA-Z0-9]+)|
        (?P<LINGUA>@[a-zA-Z]{2})|
        (?P<STRING>".*?")|
        (?P<DELIMITADOR>[\{\}\.])|
        (?P<LIMIT>\bLIMIT\b)|
        (?P<NUMERICO>\d+)|
        (?P<CONCEITO>[a-zA-Z0-9:]+)
        """

    tokens = []
    for match in re.finditer(padrao.strip(), texto, re.VERBOSE):
        tipo = match.lastgroup
        valor = match.group()
        tokens.append((tipo, valor))
        
    return tokens
