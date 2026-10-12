## Lexer para Linguagem de Query (SPARQL-like)

Este código implementa um analisador léxico, desenvolvido para converter consultas estruturadas numa lista de tokens identificáveis.

## Como Funciona

O código lê uma string de texto bruto e utiliza expressões regulares (`re`) com grupos nomeados (`?P<NOME>`) e a flag `re.VERBOSE` para segmentar o código em componentes lógicos. 

A função principal `lertexto(texto)` percorre a string utilizando `re.finditer()` e extrai pares do tipo `(tipo, valor)` para cada elemento reconhecido.

## Regras de Identificação (Tokens)

O padrão reconhece os seguintes elementos da linguagem:

* **`COMENTARIO`**: Comentários iniciados por `#`.
* **`VARIAVEL`**: Identificadores começados por `?` (ex: `?nome`).
* **`LINGUA`**: Indicadores de idioma com `@` e duas letras (ex: `@en`).
* **`STRING`**: Textos delimitados por aspas (ex: `"Chuck Berry"`).
* **`DELIMITADOR`**: Carateres estruturais como `{`, `}` e `.`.
* **`LIMIT`**: Palavra reservada limite da query.
* **`NUMERICO`**: Valores inteiros.
* **`CONCEITO`**: Identificadores, propriedades e palavras-chave alfanuméricas (incluindo namespaces com `:`).

