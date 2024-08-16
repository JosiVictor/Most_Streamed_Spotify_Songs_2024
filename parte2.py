import streamlit as st
import pandas as pd

df = pd.read_csv('Most_Streamed_Spotify_Songs_2024.csv', sep=',', header=0, encoding='cp1252')

df['Spotify Streams'] = df['Spotify Streams'].astype(str).str.replace(',','')

df['Spotify Streams'] = pd.to_numeric(df['Spotify Streams'], errors='coerce').astype('Int64')

df = df.drop_duplicates(subset=['Track'])

topmusicas = df.sort_values(by='Spotify Streams', ascending=False).iloc[:,0:2].head(3)

topalltime = df[['Track','Album Name','Artist','All Time Rank']].head(3)

st.set_page_config(layout="wide")

st.image('./Medias/Spotify.png', width= 250)

st.title('Análise das Músicas Mais Reproduzidas no Spotify em 2024')

st.header('Músicas mais populares do ano')

st.text('Esta aplicação fornece insights detalhados sobre as músicas mais populares no Spotify em 2024.')

st.markdown('*Acesse mais informações no [site oficial do Spotify](https://www.spotify.com)*.')

st.subheader('Explorando a base de dados')

col1, col2 = st.columns(2, gap='large')
 

with col1:
    st.video('./Medias/Video.mp4')
    
    st.subheader('DataFrame')
    st.dataframe(df)
    st.markdown('*Fonte: [Kaggle](https://www.kaggle.com/datasets/nelgiriyewithana/most-streamed-spotify-songs-2024)*.')


    st.write('''### Ranking de todos os tempos''',topalltime,'''_*Classificação da música com base em sua popularidade histórica*_''')

    st.subheader('As 3 músicas mais tocadas')
    st.table(topmusicas)

with col2:
    st.write('''### :musical_note: Curta as mais tocadas:''')
    st.image('./Medias/GIF.gif')

 
    topmusicas = df.sort_values(by='Spotify Streams', ascending=False).head(3)

    i=0
    for index, row in topmusicas.iterrows():
        i=i+1
        st.metric(
            value=f"{(round((row['Spotify Streams']/1000000),0))}M tocadas",
            label=row['Track'],
            delta=f"Artista: {row['Artist']}")
        
        st.image(f"./Medias/Image{i}.jpeg", width=100)

        st.audio(f"./Medias/Audio{i}.mp3")

        



