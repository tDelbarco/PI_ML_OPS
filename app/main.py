from fastapi import FastAPI
import numpy as np
import pandas as pd

app = FastAPI()


df_sg = pd.read_parquet("steam_games.parquet")

df_ud = pd.read_parquet("user_data.parquet")
df_ur = pd.read_parquet("reviews_dict.parquet")

df_ui = pd.read_parquet("users_items.parquet")
df_dict_ui = pd.read_parquet("uitems.parquet")





@app.get("/")
async def root():
    return "¡Hola FastAPI!"

print("todo se ejecuto")

#./venv/Scripts/Activate
#deactivate

#pip install "fastapi[all]" esto instala uvicorn tambien

#o puedes instalarlo por partes
#pip install fastapi

#pip install "uvicorn[standard]"

#pip freeze > Requeriment.txt crea el archivo requeriments.txt~(dentro de el venv)

#python main.py (hay que correrlo desde dentro de el venv)
#uvicorn api:app --reload


#pip install -r "requirements.txt"

#-------------------------------------------------------------------------------------------------------------------------------------


@app.get("/PlayTimeGenre")
async def PlayTimeGenre( genero : str ): #Debe devolver año con mas horas jugadas para dicho género.
    
    return {}#Ejemplo de retorno: {"Año de lanzamiento con más horas jugadas para Género X" : 2013}

@app.get("/UserForGenre")
async def UserForGenre( genero : str ): #Debe devolver el usuario que acumula más horas jugadas para el género dado y una lista de la acumulación de horas jugadas por año.
    return {} #Ejemplo de retorno: {"Usuario con más horas jugadas para Género X" : us213ndjss09sdf, "Horas jugadas":[{Año: 2013, Horas: 203}, {Año: 2012, Horas: 100}, {Año: 2011, Horas: 23}]}







@app.get("/UsersRecommend")
async def UsersRecommend( año : int ): #Devuelve el top 3 de juegos MÁS recomendados por usuarios para el año dado. (reviews.recommend = True y comentarios positivos/neutrales)
    return {} #Ejemplo de retorno: [{"Puesto 1" : X}, {"Puesto 2" : Y},{"Puesto 3" : Z}]

@app.get("/UsersWorstDeveloper")
async def UsersWorstDeveloper( año : int ): #Devuelve el top 3 de desarrolladoras con juegos MENOS recomendados por usuarios para el año dado. (reviews.recommend = False y comentarios negativos)
    return {} #Ejemplo de retorno: [{"Puesto 1" : X}, {"Puesto 2" : Y},{"Puesto 3" : Z}]



@app.get("/sentiment_analysis")
async def sentiment_analysis( empresa_desarrolladora : str ): #Según la empresa desarrolladora, se devuelve un diccionario con el nombre de la desarrolladora como llave y una lista con la cantidad total de registros de reseñas de usuarios que se encuentren categorizados con un análisis de sentimiento como valor.
    return {} #Ejemplo de retorno: {'Valve' : [Negative = 182, Neutral = 120, Positive = 278]}

#Modelo de aprendizaje automático:
#
#Una vez que toda la data es consumible por la API, está lista para consumir por los departamentos de Analytics y Machine Learning,
# y nuestro EDA nos permite entender bien los datos a los que tenemos acceso, es hora de entrenar nuestro modelo de machine learning para armar un sistema de recomendación.
# Para ello, te ofrecen dos propuestas de trabajo: En la primera, el modelo deberá tener una relación ítem-ítem, esto es se toma un item, en base a que tan similar esa ese ítem al resto,
# se recomiendan similares. Aquí el input es un juego y el output es una lista de juegos recomendados, para ello recomendamos aplicar la similitud del coseno.
# La otra propuesta para el sistema de recomendación debe aplicar el filtro user-item, esto es tomar un usuario,
# se encuentran usuarios similares y se recomiendan ítems que a esos usuarios similares les gustaron.
# En este caso el input es un usuario y el output es una lista de juegos que se le recomienda a ese usuario, en general se explican como “A usuarios que son similares a tí también les gustó…”.
# Deben crear al menos uno de los dos sistemas de recomendación (Si se atreven a tomar el desafío, para mostrar su capacidad al equipo, ¡pueden hacer ambos!).
# Tu líder pide que el modelo derive obligatoriamente en un GET/POST en la API símil al siguiente formato:

#Si es un sistema de recomendación item-item:

@app.get("/recomendacion_juego")
async def recomendacion_juego( id_producto : int ): #Ingresando el id de producto, deberíamos recibir una lista con 5 juegos recomendados similares al ingresado.
    return {}

#Si es un sistema de recomendación user-item:
@app.get("/recommendacion_usuario")
async def recomendacion_usuario( id_de_usuario : int ): #Ingresando el id de un usuario, deberíamos recibir una lista con 5 juegos recomendados para dicho usuario.
    return {}
