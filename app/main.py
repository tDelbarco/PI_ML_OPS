from fastapi import FastAPI
from starlette.responses import RedirectResponse
import functions.modelo as ml
import numpy as np
import pandas as pd
import functions.funciones as f
from enum import Enum


app = FastAPI()


@app.get("/")
async def root():
    url_destino = "/docs"
    return RedirectResponse(url_destino)



#class GeneroEnum(str, Enum):
#    alexnet = "alexnet"
#    resnet = "resnet"
#    lenet = "lenet"


class ValorNumericoEnum(int, Enum):#lista de algunos de los valores posibles de el campo de recomendacion de juegos
    motogp_13_champions = 240612
    euro_truck_simulator_raven_pack = 318521
    warhammer_space_wolf_great_awakening = 760720
    hunter_x_hunter = 545630
    final_fantasy_vi = 382900
    berserk_golden_age_arc_ii = 464420
    gotham_city_impostors_beaky = 216450
    inuyasha_movie_affections = 488370
    euro_truck_simulator_going_east = 227310
    lego_pirates_caribbean = 311770
    payday_shadow_raid_heist = 267382
    star_wars_tie_fighter = 355250
    tales_of_zestiria_costumes_set = 382464
    driver_pro_2017 = 710540
    rpg_maker_casino_tile_pack = 283541
    castlevania_mirror_of_fate_hd = 282530
    lego_marvel_super_heroes_2_guardians = 720690
    battle_of_empires_blazing_guns = 340620
    total_war_rome_ii_culture_pack = 273381
    call_of_duty_rezurrection_mac = 214649
    wwe_2k18_myplayer_kick_start = 706080
    yugioh_duel_links = 601510





#-------------------------------------------------------------------------------------------------------------------------------------


@app.get("/PlayTimeGenre/{genero}")
async def PlayTimeGenre( genero : str ):
    """
    recibe un genero

    Devuelve el año con más horas jugadas para el género dado.

    Ejemplo de retorno:
    {"Año de lanzamiento con más horas jugadas para Género X": 2013}
    """
    return f.horas_año_genero(genero)





@app.get("/UserForGenre/")
async def UserForGenre( genero : str ): 
    """
    recibe un genero

    Devuelve el usuario que acumula más horas jugadas para el género dado y una lista de la acumulación de horas jugadas por año.

    Ejemplo de retorno:
    {"Usuario con más horas jugadas para Género X": "us213ndjss09sdf", "Horas jugadas": [{"Año": 2013, "Horas": 203}, {"Año": 2012, "Horas": 100}, {"Año": 2011, "Horas": 23}]}
    """
    return f.usuario_genero(genero) 





#Devuelve el top 3 de juegos MÁS recomendados por usuarios para el año dado. (reviews.recommend = True y comentarios positivos/neutrales)
@app.get("/UsersRecommend")
async def UsersRecommend( año : int ):
    """
    recibe un año

    Devuelve el top 3 de juegos MÁS recomendados por usuarios para el año dado.

    Ejemplo de retorno:
    [{"Puesto 1": X}, {"Puesto 2": Y}, {"Puesto 3": Z}]
    """
    return f.juegos_mas_recomendados(año)





#Devuelve el top 3 de desarrolladoras con juegos MENOS recomendados por usuarios para el año dado. (reviews.recommend = False y comentarios negativos)
@app.get("/UsersWorstDeveloper")
async def UsersWorstDeveloper( año : int ):
    """
    recibe un año

    Devuelve el top 3 de desarrolladoras con juegos MENOS recomendados por usuarios para el año dado.

    Ejemplo de retorno:
    [{"Puesto 1": X}, {"Puesto 2": Y}, {"Puesto 3": Z}]
    """
    return f.developer_menos_recomendadas(año)





#Según la empresa desarrolladora, se devuelve un diccionario con el nombre de la desarrolladora como llave y una lista con la cantidad total de registros de reseñas de usuarios que se encuentren categorizados con un análisis de sentimiento como valor.
@app.get("/sentiment_analysis")
async def sentiment_analysis( empresa_desarrolladora : str ): 
    """
    recibe el nombre de una empresa

    Según la empresa desarrolladora, se devuelve un diccionario con el nombre de la desarrolladora como llave y una lista con la cantidad total de registros de reseñas de usuarios que se encuentren categorizados con un análisis de sentimiento como valor.

    Ejemplo de retorno:
    {'Valve': {'Negative': 182, 'Neutral': 120, 'Positive': 278}}
    """
    return f.contar_sentimientos_por_desarrollador(empresa_desarrolladora)





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



#Ingresando el id de producto, deberíamos recibir una lista con 5 juegos recomendados similares al ingresado.
@app.get("/recomendacion_juego")
async def recomendacion_juego( id_producto : ValorNumericoEnum ): 
    """
    recibe el id de un juego

    Devuelve una lista con 5 juegos recomendados similares al ingresado.

    Returns:
        List[int]: Una lista con los IDs de los juegos recomendados.
    """
    return ml.obtener_recomendaciones(id_producto)



##Si es un sistema de recomendación user-item:
#@app.get("/recommendacion_usuario")
#async def recomendacion_usuario( id_de_usuario : int ): #Ingresando el id de un usuario, deberíamos recibir una lista con 5 juegos recomendados para dicho usuario.
#    return {}