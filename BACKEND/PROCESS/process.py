import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from BACKEND.biblio import request_site, ia_process

def main():
    
    arquivos = ["C:/Users/buzof/Desktop/Programas/SPARROW/BACKEND/FILES/NOTICE01/",
                "C:/Users/buzof/Desktop/Programas/SPARROW/BACKEND/FILES/NOTICE02/",
                "C:/Users/buzof/Desktop/Programas/SPARROW/BACKEND/FILES/NOTICE03/",
                "C:/Users/buzof/Desktop/Programas/SPARROW/BACKEND/FILES/NOTICE04/",
                "C:/Users/buzof/Desktop/Programas/SPARROW/BACKEND/FILES/NOTICE05/"]

    arquivos_process = ["C:/Users/buzof/Desktop/Programas/SPARROW/BACKEND/FILES/FILES_PROCESS/NOTICE_PROCESS01.txt",
                      "C:/Users/buzof/Desktop/Programas/SPARROW/BACKEND/FILES/FILES_PROCESS/NOTICE_PROCESS02.txt",
                      "C:/Users/buzof/Desktop/Programas/SPARROW/BACKEND/FILES/FILES_PROCESS/NOTICE_PROCESS03.txt",
                      "C:/Users/buzof/Desktop/Programas/SPARROW/BACKEND/FILES/FILES_PROCESS/NOTICE_PROCESS04.txt",
                      "C:/Users/buzof/Desktop/Programas/SPARROW/BACKEND/FILES/FILES_PROCESS/NOTICE_PROCESS05.txt"]
    
    sites=[["https://g1.globo.com/economia/noticia/2025/04/09/china-anuncia-tarifas-de-mais-84percent-sobre-produtos-dos-eua.ghtml", 
            "https://g1.globo.com/mundo/noticia/2025/04/09/governo-chines-emite-alerta-de-risco-para-viagens-aos-eua.ghtml", 
            "https://g1.globo.com/economia/noticia/2025/04/09/tarifaco-de-trump-como-esta-a-fortuna-dos-homens-mais-ricos-do-mundo-desde-o-inicio-das-tarifas.ghtml"],
            ["https://ge.globo.com/tenis/noticia/2025/04/09/ex-numero-1-do-mundo-aponta-habilidade-especial-de-joao-fonseca-abre-uma-caixa-de-pandora.ghtml"],
            ["https://oglobo.globo.com/politica/noticia/2025/04/09/mais-de-70-deputados-de-partidos-da-base-de-lula-assinam-urgencia-da-anistia-do-8-de-janeiro.ghtml"],
            ["https://g1.globo.com/pr/parana/noticia/2025/04/09/deputado-do-parana-ataca-roupas-de-deputada-apos-ela-protocolar-pedido-para-que-ele-perca-cargo-na-ccj-por-faltas-consecutivas.ghtml"],
            ["https://oglobo.globo.com/cultura/noticia/2025/04/09/mickey-rourke-surge-irreconhecivel-em-big-brother-de-famosos-na-inglaterra-e-habitos-de-higiene-deixam-fas-enojados.ghtml"]]

    for i in range(len(arquivos)):

        # Define o diretório do arquivo
        arq = arquivos[i]
        arq_process = arquivos_process[i]

        # Define o site a ser requisitado
        site = sites[i]
    
        # Chama a função para requisitar o site e salvar o conteúdo no arquivo
        request_site(arq, site)

        # Define o prompt para o modelo de linguagem
        chat = "Reescreva o texto abaixo de forma mais detalhada e aprofundada, ampliando as ideias para atingir uma extensão entre 25.000 e 40.000 caracteres. Reserve a primeira linha a um título curto e cativante relacionado ao tema, sem utilizar subtítulos ao longo do texto. Mantenha a redação objetiva, informativa, clara e livre de ambiguidades, garantindo total neutralidade política. Preserve a fidelidade ao conteúdo original, sem incluir dados fictícios, opiniões pessoais ou informações não verificadas. Não explique seu processo de escrita em nenhum momento. Evite o uso de caracteres especiais, como asteriscos, travessões decorativos ou emojis. Ao final de cada parágrafo, adicione a marcação /n para indicar a quebra de parágrafo."
        
        # Chama a função para processar o arquivo e gerar a resposta do modelo
        ia_process(arq, arq_process, chat)

main()