# Problema:
## Criar em Python um pequeno conversor de MarkDown para HTML para os elementos descritos na "Basic Syntax" da Cheat Sheet:

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

## Bold: pedaços de texto entre "**":
2. Neste problema queremos encontrar palavras que estejam entre duas aspas:
    In: `Este é um **exemplo** ...`
    
    Out: `Este é um <b>exemplo</b> ...`
