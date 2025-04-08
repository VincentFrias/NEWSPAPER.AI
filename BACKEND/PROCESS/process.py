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
        chat = "Reescreva o texto abaixo de forma mais detalhada, reserve a primeira linha para um titulo cativante sobre a matéria, expandindo as ideias para alcançar uma extensão entre 20.000 e 30.000 caracteres. Certifique-se de que a redação seja objetiva, informativa e livre de ambiguidades, garantindo neutralidade política. Mantenha a fidelidade às informações originais sem adicionar elementos fictícios. Não revele seu processo de raciocínio e não utilize caracteres especiais(como * ao redor do titulo e sub-titulo) ou emojis, adicione /n no final de cada paragrafo"

        # Chama a função para processar o arquivo e gerar a resposta do modelo
        ia_process(arq, arq_process, chat)

main()