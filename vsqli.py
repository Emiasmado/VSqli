import requests
import difflib

def verificador():
        url = input("Digite a url:")
        request1 = requests.get(url)
        html = request1.text
#parte da verificaçao
        ver = url + "\'"
        request2 = requests.get(ver)
        html2 = request2.text
        if html != html2:
                print("pagina mudou")
                diferenca = difflib.ndiff(                      #1.) verifica as diferenças
                        html.splitlines(),                      #2.) divide a string em uma lista de linhas
                        html2.splitlines()                      #3.) mesma coisa do 2 comentario
                )

                for linha in diferenca:
                        if linha.startswith("+ "):
                                print(linha[2:])

        else:
                print("nada mudou")

verificador()
