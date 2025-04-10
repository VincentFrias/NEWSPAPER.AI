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
    

    sites=[["https://oglobo.globo.com/economia/noticia/2025/04/10/casa-branca-confirma-que-tarifa-americana-para-china-sera-de-145percent.ghtml","https://www.infomoney.com.br/economia/tarifa-total-sobre-a-china-vai-a-145-diz-casa-branca/","https://www.cnnbrasil.com.br/economia/macroeconomia/casa-branca-esclarece-que-tarifas-sobre-a-china-chegam-a-145/"],
            ["https://g1.globo.com/politica/noticia/2025/04/10/com-habeas-corpus-deolane-diz-que-nao-vai-comparecer-a-cpi-das-bets-nesta-quinta.ghtml","https://www.poder360.com.br/poder-justica/mendonca-barra-depoimento-de-deolane-na-cpi-das-bets/","https://www.cnnbrasil.com.br/politica/deolane-consegue-habeas-corpus-e-e-liberada-de-comparecer-na-cpi-das-bets/"],
            ["https://noticias.uol.com.br/politica/ultimas-noticias/2025/04/10/operacao-pf-sorocaba-desvio-recursos-publicos.htm","https://valor.globo.com/politica/noticia/2025/04/10/prefeito-tiktoker-de-sorocaba-faz-video-ironizando-operacao-da-pf-veja-o-video.ghtml","https://valor.globo.com/politica/noticia/2025/04/10/prefeito-tiktoker-de-sorocaba-faz-video-ironizando-operacao-da-pf-veja-o-video.ghtml"],
            ["https://valor.globo.com/financas/ao-vivo/2023/06/16/dolar-avanca-e-ibovespa-recua-em-dia-de-correcao-siga-os-mercados.ghtml","https://veja.abril.com.br/economia/bolsa-dispara-e-dolar-desaba-apos-trump-interromper-tarifas-reciprocas-aos-paises/","https://www.infomoney.com.br/mercados/yuan-cai-ao-menor-nivel-frente-ao-dolar-desde-2007/"],
            ["https://www.cnnbrasil.com.br/politica/bolsonaro-e-hugo-motta-se-encontram-em-brasilia-para-discutir-anistia/","https://g1.globo.com/politica/blog/andreia-sadi/post/2025/04/10/bolsonaro-hugo-motta-bastidores-anistia.ghtml","https://veja.abril.com.br/coluna/maquiavel/o-placar-atualizado-de-deputados-que-apoiam-a-urgencia-a-anistia-na-camara/"]]

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