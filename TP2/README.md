## Problema:
Criar em Python um pequeno conversor de MarkDown para HTML para os elementos descritos na "Basic Syntax" da Cheat Sheet:

1. O primeiro desafio imposto foi o de converter linhas iniciadas por #; seguindo o exemplo:
    In: `# Exemplo`

    Out: `<h1>Exemplo</h1>`

    A parte do meu código que resolve este problema é:
    ```python
    regex1 = r"^(#{1,3})\s+(.*)$"
    match1 = re.match(regex1, linha)
    
    if match1:
        cardinais, texto = match1.groups()
        nivel = len(cardinais)
        return f"<h{nivel}>{texto}</h{nivel}>"
    ```
### Explicação
A expressão regular ^(#{1,3})\s+(.+)$ é composta por:
- ^ e $, que ancoram o padrão ao início e ao fim da linha;
- (#{1,3}), um grupo de captura que apanha entre 1 e 3 cardinais, correspondendo aos níveis h1 a h3;
- \s+, que exige pelo menos um espaço em branco a separar os cardinais do texto;
- (.+), um segundo grupo de captura com o texto do título (pelo menos um carácter).

A função re.match verifica se a linha respeita este padrão, se sim, groups() devolve os dois grupos, que são guardados em cardinais e texto. O nível do título obtém-se com len(cardinais), e a função devolve o texto envolvido na etiqueta <h{nivel}>.
