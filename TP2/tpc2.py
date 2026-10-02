import re

def converter_cabecalho(linha):
    regex1 = r"^(#{1,3})\s+(.*)$"
    match1 = re.match(regex1, linha)
    
    if match1:
        cardinais, texto = match.groups()
        nivel = len(cardinais)
        return f"<h{nivel}>{texto}</h{nivel}>"
    
    linha = re.sub(r"\*\*(.*?)\*\*", r"<b>\1</b>", linha)

    linha = re.sub(r"\*(.*?)\*", r"<i>\1</i>", linha)
    
    linha = re.sub(r"\d+\. (.*)$", r"<li>\1</li>", linha, flags=re.MULTILINE)
    linha = re.sub(r"((?:<li>.*?</li>\s*)+)", r"<ol>\n\1\n</ol>", linha, flags=re.DOTALL)
    
    linha = re.sub(r"(?<!!)\[(.*?)\]\((.*?)\)", r'a <href="\2">\1</a>', linha)
    
    linha = re.sub(r"\!\[(.*?)\]\((.*?)\)", r'<img scr="\2" alt="\1"/>', linha)
    return linha


entrada = input("In: ")
resultado = converter_cabecalho(entrada)
print("Out:", resultado)