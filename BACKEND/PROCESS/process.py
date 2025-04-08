import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from BACKEND.biblio import request_site, ia_process

def main():
    
    arquivos = ["C:/Users/buzof/Desktop/Programas/SPARROW/BACKEND/FILES/notice01.txt",
                "C:/Users/buzof/Desktop/Programas/SPARROW/BACKEND/FILES/notice02.txt",
                "C:/Users/buzof/Desktop/Programas/SPARROW/BACKEND/FILES/notice03.txt",
                "C:/Users/buzof/Desktop/Programas/SPARROW/BACKEND/FILES/notice04.txt",
                "C:/Users/buzof/Desktop/Programas/SPARROW/BACKEND/FILES/notice05.txt"]

    arquivos_process = ["C:/Users/buzof/Desktop/Programas/SPARROW/BACKEND/FILES/FILES_PROCESS/nt_process01.txt",
                        "C:/Users/buzof/Desktop/Programas/SPARROW/BACKEND/FILES/FILES_PROCESS/nt_process02.txt",
                        "C:/Users/buzof/Desktop/Programas/SPARROW/BACKEND/FILES/FILES_PROCESS/nt_process03.txt",
                        "C:/Users/buzof/Desktop/Programas/SPARROW/BACKEND/FILES/FILES_PROCESS/nt_process04.txt",
                        "C:/Users/buzof/Desktop/Programas/SPARROW/BACKEND/FILES/FILES_PROCESS/nt_process05.txt"]
    
    sites=["https://g1.globo.com/economia/noticia/2025/04/07/dolar-ibovespa.ghtml", "https://revistaquem.globo.com/saude/fitness/noticia/2025/04/maior-fisiculturista-da-atualidade-cbum-diz-que-fez-jejum-de-80-horas.ghtml",
          "https://g1.globo.com/politica/noticia/2025/04/07/datafolha-56percent-sao-contra-anistia-36percent-sao-a-favor.ghtml",
          "https://g1.globo.com/mg/sul-de-minas/noticia/2025/04/07/mulher-e-morta-com-pelo-menos-seis-tiros-em-itajuba-mg.ghtml",
          "https://revistaquem.globo.com/saude/fitness/noticia/2025/04/maior-fisiculturista-da-atualidade-cbum-diz-que-fez-jejum-de-80-horas.ghtml"]

    for i in range(len(arquivos)):

        # Define o diretório do arquivo
        arq = arquivos[i]
        arq_process = arquivos_process[i]

        # Define o site a ser requisitado
        site = sites[i]
    
        # Chama a função para requisitar o site e salvar o conteúdo no arquivo
        request_site(arq, site)

        # Define o prompt para o modelo de linguagem
        chat = "Reescreva o texto abaixo de forma mais detalhada e aprofundada, ampliando as ideias para atingir uma extensão entre 25.000 e 40.000 caracteres. Inicie o conteúdo com uma linha dedicada a um título cativante relacionado ao tema, sem utilizar subtítulos ao longo do texto. Mantenha a redação objetiva, informativa, clara e livre de ambiguidades, garantindo total neutralidade política. Preserve a fidelidade ao conteúdo original, sem incluir dados fictícios, opiniões pessoais ou informações não verificadas. Não explique seu processo de escrita em nenhum momento. Evite o uso de caracteres especiais, como asteriscos, travessões decorativos ou emojis. Ao final de cada parágrafo, adicione a marcação /n para indicar a quebra de parágrafo."
        
        # Chama a função para processar o arquivo e gerar a resposta do modelo
        ia_process(arq, arq_process, chat)

main()