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
    for match in re.finditer(padrao.strip(),texto,re.VERBOSE):
        tipo = match.lastgroup
        valor = match.group()
        tokens.append((tipo,valor))
    
    return tokens

resultado = lertexto("""# DBPedia: obras de Chuck Berry
                    select ?nome ?desc where {
                    ?s a dbo:MusicalArtist.
                    ?s foaf:name "Chuck Berry"@en .
                    ?w dbo:artist ?s.
                    ?w foaf:name ?nome.
                    ?w dbo:abstract ?desc
                    } LIMIT 1000""")
print(resultado)
