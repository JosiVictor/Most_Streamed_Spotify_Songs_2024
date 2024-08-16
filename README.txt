# Instruções de Uso para a Aplicação Streamlit
Este guia orienta você sobre como utilizar a aplicação interativa desenvolvida com Streamlit para analisar as músicas mais reproduzidas no Spotify em 2024.

# Pré-requisitos

## Instalação das Bibliotecas:
As bibliotecas para essa aplicação constam no arquivo 'requirements.txt'

## Arquivos Necessários:
Dados: Um arquivo CSV chamado Most_Streamed_Spotify_Songs_2024.csv com informações sobre as músicas.

## Imagens e Vídeos:
./Medias/Spotify.png (Imagem do Spotify)
./Medias/Video.mp4 (Vídeo para visualização)
./Medias/GIF.gif (GIF para ilustração)
./Medias/Image1.jpeg, ./Medias/Image2.jpeg, ./Medias/Image3.jpeg (Imagens associadas às músicas mais tocadas)
./Medias/Audio1.mp3, ./Medias/Audio2.mp3, ./Medias/Audio3.mp3 (Áudios das músicas mais tocadas)

# Como Executar a Aplicação

## Iniciar a Aplicação:
Navegue até o diretório onde o arquivo Python está localizado e execute o comando para iniciar o Streamlit. Substitua pelo nome do arquivo onde o código está salvo.

## Explorando a Aplicação:
- Imagem Inicial: A aplicação exibirá uma imagem do Spotify no topo da página.
- Título e Descrição: Você verá o título "Análise das Músicas Mais Reproduzidas no Spotify em 2024" e uma breve descrição logo abaixo.
- Exploração da Base de Dados:
- DataFrame: No lado esquerdo da página, o DataFrame com todos os dados das músicas estará visível.
- Ranking de Todos os Tempos: Abaixo do DataFrame, será exibida uma tabela com as três músicas mais bem classificadas historicamente.
- As 3 Músicas Mais Tocadas: Uma tabela apresentará as três músicas mais reproduzidas em 2024.
- Músicas em Destaque: No lado direito da página, você encontrará uma seção com:
- Métricas: Informações sobre o número de reproduções e o artista de cada uma das três músicas mais tocadas.
- Imagens e Áudios: Imagens e clipes de áudio associados às músicas mais populares.

## Interação:
- DataFrame: Utilize as funcionalidades interativas do Streamlit para explorar o DataFrame.
- Tabela de Ranking: As tabelas são exibidas de forma estática, mas você pode rolar para visualizar todas as informações.
- Vídeos e Áudios: Use os controles do Streamlit para reproduzir o vídeo e os clipes de áudio diretamente na aplicação.

## Referências e Fontes:
- Link para o Spotify: O link para o site oficial do Spotify está disponível para mais informações.
- Fonte dos Dados: O link para a fonte dos dados está incluído no DataFrame, com uma referência ao Kaggle.

# Solução de Problemas
- Problemas com Arquivos: Verifique se todos os arquivos necessários estão no diretório correto e com os nomes apropriados.
- Erro ao Ler o CSV: Certifique-se de que o arquivo CSV está no formato esperado e que o separador e a codificação estão corretos.


Estas instruções devem ajudá-lo a configurar e usar a aplicação para analisar as músicas mais populares no Spotify. Aproveite a análise!