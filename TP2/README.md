## Problema:
Criar em Python um pequeno conversor de MarkDown para HTML para os elementos descritos na "Basic Syntax" da Cheat Sheet:

### 1. Titulos
   O primeiro desafio imposto foi o de converter linhas iniciadas por #; seguindo o exemplo:
    In: `# Exemplo`

    Out: `<h1>Exemplo</h1>`

    A parte do meu código que resolve este problema é:
    "    regex1 = r"^(#{1,3})\s+(.*)$"
    match1 = re.match(regex1, linha)
    
    if match1:
        cardinais, texto = match.groups()
        nivel = len(cardinais)
        return f"<h{nivel}>{texto}</h{nivel}>"
   "

   Aqui criamos uma variavel regex com a expressão regular que analisa a partir do inicio da linha se tem algum # de 1 a 3, depois o \s+ verifica se tem pelo menos um espaço q separa dos restantes caracteres representados pelo conjunto (.*).
   De seguida o match1 verifica se o texto introduzido respeita essa condições se sim separa os grupos em cardinais e texto. com o grupo dos cardinais conta os numeros e da return de h mais a quantidade de hastags e o  texto no meio
