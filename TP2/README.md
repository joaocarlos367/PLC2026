# Problema:
Criar em Python um pequeno conversor de Markdown para HTML para os elementos descritos na "Basic Syntax" da Cheat Sheet:

## Cabeçalhos: linhas iniciadas por "# texto", ou "## texto" ou "### texto"
1. O primeiro desafio imposto foi o de converter linhas iniciadas por #; seguindo o exemplo:
    In: `# Exemplo`

    Out: `<h1>Exemplo</h1>`

    A parte do meu código que resolve este problema é:
    ```python
    regex1 = r"^(#{1,3})\s+(.+)$"
    match1 = re.match(regex1, linha)
    
    if match1:
        cardinais, texto = match1.groups()
        nivel = len(cardinais)
        return f"<h{nivel}>{texto}</h{nivel}>"
    ```
### Explicação
A expressão regular ^(#{1,3})\s+(.+)$ é composta por:
- ^ assegura que o padrão que queremos está no inicio;
- O (#{1,3}) é um grupo de captura que apanha entre 1 e 3 cardinais;
- \s+, faz com que haja pelo menos um espaço a separar os cardinais do texto;
- (.+) é outro grupo de captura que é onde vai estar o texto.

A função re.match verifica se a linha respeita este padrão, se sim, groups() devolve os dois grupos, que são guardados em cardinais e texto. O nível do título obtém-se com len(cardinais), e a função devolve o texto envolvido na etiqueta <h{nivel}>.

Se a linha for um cabeçalho, a função termina logo com este `return`; caso contrário, segue para as conversões seguintes.

## Bold: pedaços de texto entre "**":
2. Neste problema queremos encontrar palavras que estejam entre dois asteriscos duplos:
    In: `Este é um **exemplo** ...`
    
    Out: `Este é um <b>exemplo</b> ...`

    A parte do código que resolve este problema é:
    ```python
    linha = re.sub(r"\*\*(.*?)\*\*", r"<b>\1</b>", linha)
    ```
### Explicação
A expressão regular \*\*(.*?)\*\* é composta por:
- \*\* corresponde a dois asteriscos literais (o \ é necessário porque o * tem significado especial nas expressões regulares), tanto no início como no fim;
- (.*?) é um grupo de captura com o texto que está entre os asteriscos. O ? torna o * "preguiçoso" (lazy), ou seja, apanha o mínimo de caracteres possível. Assim, em `**a** e **b**` obtemos dois pedaços separados em vez de um só a ir do primeiro ao último asterisco.

A função re.sub substitui cada ocorrência do padrão pelo texto `<b>\1</b>`, onde \1 é o conteúdo do primeiro grupo de captura.

## Itálico: pedaços de texto entre "*":
3. Aqui queremos encontrar palavras entre dois asteriscos simples:
    In: `Este é um *exemplo* ...`

    Out: `Este é um <i>exemplo</i> ...`

    A parte do código que resolve este problema é:
    ```python
    linha = re.sub(r"\*(.*?)\*", r"<i>\1</i>", linha)
    ```
### Explicação
A lógica é a mesma do bold, mas com um único asterisco de cada lado: \* corresponde a um asterisco literal e (.*?) captura, de forma lazy, o texto do meio. O resultado é envolvido em `<i>...</i>`.

A **ordem** é importante: o bold tem de ser convertido antes do itálico. Se fosse ao contrário, o padrão do itálico apanharia os asteriscos de `**exemplo**` e o resultado ficaria errado. Como o bold já foi substituído por `<b>...</b>`, já não restam asteriscos duplos quando chegamos ao itálico.

## Lista numerada: linhas iniciadas por "1. texto", "2. texto", ...
4. Neste problema queremos converter um conjunto de linhas numeradas numa lista ordenada:
    In:
    ```
    1. Primeiro item
    2. Segundo item
    3. Terceiro item
    ```

    Out:
    ```html
    <ol>
    <li>Primeiro item</li>
    <li>Segundo item</li>
    <li>Terceiro item</li>
    </ol>
    ```

    A parte do código que resolve este problema é:
    ```python
    linha = re.sub(r"^\d+\. (.*)$", r"<li>\1</li>", linha, flags=re.MULTILINE)
    linha = re.sub(r"((?:<li>.*?</li>\s*)+)", r"<ol>\n\1\n</ol>", linha, flags=re.DOTALL)
    ```
### Explicação
Este problema resolve-se em dois passos.

**Passo 1: converter cada linha num item.** A expressão regular ^\d+\. (.*)$ é composta por:
- ^ assegura que a linha começa com o número (evita apanhar, por exemplo, "versão 2. algo" a meio de uma frase);
- \d+ apanha um ou mais dígitos;
- \. corresponde a um ponto literal, seguido de um espaço;
- (.*) é o grupo de captura com o texto do item;
- $ assegura que o padrão vai até ao fim da linha.

A flag re.MULTILINE faz com que ^ e $ se apliquem a cada linha do texto e não apenas ao início e fim da string completa. Cada linha é substituída por `<li>\1</li>`.

**Passo 2: juntar os itens numa lista.** A expressão regular ((?:<li>.*?</li>\s*)+) é composta por:
- (?:<li>.*?</li>\s*) é um grupo de não captura (o ?: indica que não é guardado) que representa um item `<li>...</li>` seguido de espaços ou mudanças de linha (\s*);
- o + à frente do grupo faz com que se apanhem um ou mais itens consecutivos;
- os parênteses exteriores capturam todos esses itens como um só bloco.

A flag re.DOTALL faz com que o . também corresponda a mudanças de linha. O bloco capturado é depois envolvido em `<ol>` e `</ol>`, através de `<ol>\n\1\n</ol>`.

## Links: "[texto](url)"
5. Aqui queremos converter a sintaxe de links do Markdown para uma etiqueta de âncora:
    In: `[Universidade do Minho](https://www.uminho.pt)`

    Out: `<a href="https://www.uminho.pt">Universidade do Minho</a>`

    A parte do código que resolve este problema é:
    ```python
    linha = re.sub(r"(?<!!)\[(.*?)\]\((.*?)\)", r'<a href="\2">\1</a>', linha)
    ```
### Explicação
A expressão regular (?<!!)\[(.*?)\]\((.*?)\) é composta por:
- (?<!!) é um lookbehind negativo: só há correspondência se o carácter anterior **não** for um !. Isto é necessário porque as imagens (`![alt](url)`) têm a mesma estrutura dos links, apenas com um ! à frente, e não queremos que sejam tratadas como links;
- \[(.*?)\] apanha o texto entre parênteses retos, guardando-o no grupo 1 (o texto visível do link);
- \((.*?)\) apanha o texto entre parênteses curvos, guardando-o no grupo 2 (o endereço).

Os parênteses são escapados com \ porque, sem isso, seriam interpretados como grupos de captura. Na substituição, \2 é usado como valor do atributo `href` e \1 como texto do link.

## Imagens: "![alt](url)"
6. Por fim, queremos converter a sintaxe de imagens:
    In: `![Logótipo](logo.png)`

    Out: `<img src="logo.png" alt="Logótipo"/>`

    A parte do código que resolve este problema é:
    ```python
    linha = re.sub(r"\!\[(.*?)\]\((.*?)\)", r'<img src="\2" alt="\1"/>', linha)
    ```
### Explicação
A expressão regular é muito parecida com a dos links, mas começa com \!, que corresponde a um ponto de exclamação literal. O grupo 1 (.*?) entre parênteses retos é o texto alternativo (`alt`) e o grupo 2 entre parênteses curvos é o caminho da imagem (`src`).

Esta conversão é feita **depois** da dos links. Como a expressão dos links ignora tudo o que tenha um ! antes do [, as imagens chegam intactas a este passo.

## Resumo do funcionamento
A função `converter_cabecalho` recebe uma linha de texto e aplica as conversões pela seguinte ordem:

1. Cabeçalhos (se a linha for um cabeçalho, devolve logo o resultado);
2. Bold;
3. Itálico;
4. Listas numeradas;
5. Links;
6. Imagens.

O programa pede ao utilizador uma linha com `input("In: ")`, passa-a à função e mostra o resultado com `print("Out:", resultado)`.
