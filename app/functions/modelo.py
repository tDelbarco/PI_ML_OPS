import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel # calcular la similitud coseno entre los juegos

#cargamos el archivo que creeamos con user_id ,genres y app_name
df_juegos = pd.read_parquet(r"../app/df_modelo.parquet")

#df_juegos
#el archivo tiene 32k de filas y es muy pesado  para pasarle todoslos datos

vectorizer = TfidfVectorizer(stop_words='english',max_features=5000)
#stop_words parametro paraque ignore las palabras comunes de el ingles como (and,the,to) ya que el tfid vectorizer va a sacar el peso de cada palabra individual y tenemos algunos como free to play y pueden haber mas 
#max_features fue mi primer intento de reducir el espacio en memoria que ocupaba la matriz redujo casi 3/4 de lo que ocupaba de memoria


df_muestra = df_juegos.sample(frac=0.1,random_state=42)#tomo una muestra de 10% de el data frame


df_muestra = df_muestra.reset_index(drop=True)#reseteo los indices para poder acceder a travez de indices dentro de la funcion

matriz_tfidf = vectorizer.fit_transform(df_muestra["genres"])#hago una matriz tfidf 

similitud_juegos = linear_kernel(matriz_tfidf, matriz_tfidf) #calcular la similitud entre los juegos basándose en la matriz tfidf

def obtener_recomendaciones(item_id_ingresado, n=5):
    try:
        item_id_ingresado = float(item_id_ingresado)
        indice_juego_ingresado = df_muestra[df_muestra['id'] == item_id_ingresado].index[0]
    except IndexError:
        return f"El juego con ID {int(item_id_ingresado)} no está en el conjunto de datos de entrenamiento."

    similitudes = similitud_juegos[indice_juego_ingresado]

    # Obtener los índices de los juegos más similares
    indices_similares = similitudes.argsort()[::-1][1:n+1]

    # Obtener los item_id de los juegos recomendados
    juegos_recomendados = df_muestra.loc[indices_similares, 'app_name'].tolist()

    return str({"recomendaciones": juegos_recomendados})





#from sklearn.metrics.pairwise import cosine_similarity

