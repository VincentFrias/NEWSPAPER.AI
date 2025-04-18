import requests
import re
import os
import glob
from bs4 import BeautifulSoup

tag_html=["h1", "h2", "p", "article", "div", "section"] # Tags HTML que serão utilizadas para buscar os elementos no HTML
class_title_html=["content-head__title", "text-3xl md:text-5xl font-bold tracking-tighter text-wl-neutral-950","single-header__title", "inner-page-section__title title-1", "title"]
class_subtitle_html=["content-head__subtitle","text-lg md:text-xl font-medium tracking-tight text-wl-neutral-600","single-header__excerpt", "inner-page-section__line","solar-author-origin has-authors", "description"]
class_materia_html=["content-text__container","im-article clear-fix","single-content","inner-page-section__section","bullet","content"]

def request_site(arq, site): # Seleciona o diretório e Grava conforme o HTML
    
    for i in range(len(site)):
        # Seleciona o diretório onde o arquivo será salvo
        # Se o diretório não existir, ele será criado
        nome_arquivo = f"{arq}arq0{i}.txt" # "001/files/arq01.txt"
        print(f"[DEBUG] URL recebida: {site[i]}")
        # Faz a requisição para o site
        # em formato de HTML --> TXT
        url = site[i] # 'https://g1.globo.com/politica/noticia/2025/03/19/stf-tem-maioria-para-manter-dino-zanin-e-moraes-em-julgamento-de-denuncia-de-golpe-contra-bolsonaro-e-aliados.ghtml'
        request = requests.get(url)
        soup = BeautifulSoup(request.text, 'html.parser')
        titulo=soup.find(tag_html, class_=class_title_html)  
        sub_titulo=soup.find(tag_html, class_=class_subtitle_html)

        # Abre o arquivo para escrita
        # Escreve o título e o subtítulo   
        with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
            arquivo.write(titulo.text + "\n")
            arquivo.write(sub_titulo.text + "\n")
    
            # Chama os parágrafos de MATERIAS
            # Grava os MATERIAS no arquivo TXT
            materias = soup.find_all(tag_html, class_=class_materia_html)
            for m in materias:
                arquivo.write(m.text + "\n")

def ia_process(arq, arq_process, chat): # Processa o arquivo e gera a resposta do modelo
    pasta =arq
    arquivos_txt = glob.glob(os.path.join(pasta, '*.txt'))

    conteudo_total = ""
    for arquivo in arquivos_txt:
        with open(arquivo, 'r', encoding='utf-8') as f:
            conteudo_total += f.read()
    
    #arquivo = [f for f in os.listdir(arq) if f.endswith('.txt')] #"001/files/arq01.txt"
    #with open(arquivo, 'r', encoding='utf-8') as f:
    #    prompt = f.read()
    #print(prompt) #teste de entrada do arquivo

    # Configuração da API do LM Studio
    url = "http://192.168.1.10:1234/v1/chat/completions"  # Ajuste conforme a porta do LM Studio
            
    #Definição do prompt
    payload = {
    "model": "deepseek-r1-distill-llama-8b",  # Troque pelo nome do seu modelo
    "messages": [{"role": "user", "content": chat + conteudo_total}], #"Reescreva o texto abaixo de forma mais detalhada, reserve a primeira linha para um titulo cativante sobre a matéria, expandindo as ideias para alcançar uma extensão entre 20.000 e 30.000 caracteres. Certifique-se de que a redação seja objetiva, informativa e livre de ambiguidades, garantindo neutralidade política. Mantenha a fidelidade às informações originais sem adicionar elementos fictícios. Não revele seu processo de raciocínio e não utilize caracteres especiais(como * ao redor do titulo e sub-titulo) ou emojis, adicione /n no final de cada paragrafo"
    "temperature": 0.75
    }

    # Enviar requisição para o LM Studio
    response = requests.post(url, json=payload)

    texto_filtrado = re.sub(r'<think>.*?</think>', '', response.json()["choices"][0]["message"]["content"], flags=re.DOTALL)
    texto_filtrado = re.sub(r'\*', '', texto_filtrado)
    texto_final = "\n".join([linha for linha in texto_filtrado.splitlines() if linha.strip()])


    # Exibir resposta do modelo
    # if response.status_code == 200:
    #     print(response.json()["choices"][0]["message"]["content"])
    # else:
    #     print("Erro:", response.text)

    arquivo=arq_process
    # Salva a resposta do modelo em um arquivo
    arquivo_process = arquivo #"001/files/files_process/arq_process01.txt"
    with open(arquivo_process, "w", encoding="utf-8") as arquivo:
        arquivo.write(texto_final + "\n")
