import pandas as pd



df_genero = pd.read_parquet("df_genero.parquet")
df_recommend = pd.read_parquet("df_recommend.parquet")
df_sentimientos = pd.read_parquet("df_sentimientos.parquet")




def horas_año_genero(genero):

    df_hg = df_genero.copy()
    df_hg = df_hg[df_hg['genres'].str.contains(genero, case=False, na=False)]# Filtra el DataFrame para el género específico

        # Agrupa por año y suma las horas jugadas
    horas_por_año = df_hg.groupby('release_date')['playtime_forever'].sum()

    año_mas_jugado = horas_por_año.idxmax()

    return str({"Año de lanzamiento con más horas jugadas para Género": genero, "Año más jugado": año_mas_jugado})




def usuario_genero(genero):
    df_ug = df_genero.copy()  
    df_filtrado = df_ug[df_ug['genres'].str.contains(genero, case=False, na=False)]

    if df_filtrado.empty:
        return {"Usuario con más horas jugadas para Género": None, "Horas jugadas": []}

    horas_por_año = (df_filtrado.groupby(['release_date', 'user_id'])['playtime_forever'].sum() / 60).astype(int).reset_index()

    # Encuentra al usuario con más horas jugadas para cada año
    usuario_mas_jugado_por_año = horas_por_año.loc[horas_por_año.groupby('release_date')['playtime_forever'].idxmax()]

    return str({
        "Usuario con más horas jugadas para Género": usuario_mas_jugado_por_año.groupby('user_id')['playtime_forever'].sum().idxmax(),
        "Horas jugadas": [{"Año": año, "Horas": horas} for año, horas in usuario_mas_jugado_por_año.groupby('release_date')['playtime_forever'].sum().items()]
    }) 






#Devuelve el top 3 de juegos MÁS recomendados por usuarios para el año dado. (reviews.recommend = True y comentarios positivos/neutrales)
    #return {} #Ejemplo de retorno: [{"Puesto 1" : X}, {"Puesto 2" : Y},{"Puesto 3" : Z}]
def juegos_mas_recomendados(anio):
    df_f = df_recommend[df_recommend['posted'].str.contains(str(anio))] #filtro el df al año
    df_f = df_f[(df_f['sentimiento'] == 2) | (df_f['recommend'] == True)]#filtro el df a los que al menos poseen uno de las 2 cosas que vamos a contar

    conteo_sentimiento = df_f[df_f['sentimiento'] == 2].groupby('item_id')['sentimiento'].count()
    conteo_recommend = df_f[df_f['recommend'] == True].groupby('item_id')['recommend'].count()

    conteo_df = pd.merge( conteo_recommend,conteo_sentimiento, on='item_id', how='inner')

    df_f = df_f.merge(conteo_df,how="inner",left_on="id",right_on="item_id")

    df_f = df_f.drop_duplicates(subset=['item_id'])

    df_f = df_f.sort_values(by=['recommend_y','sentimiento_y'], ascending=[False, False])

    result_list = [{"Puesto " + str(i + 1): app_name} for i, app_name in enumerate(df_f['app_name'][:3])]

    return result_list





#Devuelve el top 3 de desarrolladoras con juegos MENOS recomendados por usuarios para el año dado. (reviews.recommend = False y comentarios negativos)
    #return {} #Ejemplo de retorno: [{"Puesto 1" : X}, {"Puesto 2" : Y},{"Puesto 3" : Z}]
def developer_menos_recomendadas(anio):
    df_f = df_recommend[df_recommend['posted'].str.contains(str(anio))] #filtro el df al año
    df_f = df_f[(df_f['sentimiento'] == 0) | (df_f['recommend'] == False)]#filtro el df a los que al menos poseen uno de las 2 cosas que vamos a contar

    conteo_sentimiento = df_f[df_f['sentimiento'] == 0].groupby('developer')['sentimiento'].count()
    conteo_recommend = df_f[df_f['recommend'] == False].groupby('developer')['recommend'].count()

    conteo_df = pd.merge( conteo_recommend,conteo_sentimiento, on='developer', how='inner')

    df_f = df_f.merge(conteo_df,how="inner",on="developer")

    df_f = df_f.drop_duplicates(subset=['developer'])

    df_f = df_f.sort_values(by=['recommend_y','sentimiento_y'], ascending=[False, False])

    result_list = [{"Puesto " + str(i + 1): developer} for i, developer in enumerate(df_f['developer'][:3])]

    return result_list




#Según la empresa desarrolladora, se devuelve un diccionario con el nombre de la desarrolladora como llave y una lista con la cantidad total de registros de reseñas de usuarios que se encuentren categorizados con un análisis de sentimiento como valor.
   # return {} #Ejemplo de retorno: {'Valve' : [Negative = 182, Neutral = 120, Positive = 278]}
def contar_sentimientos_por_desarrollador(developer):
    # Filtra el DataFrame para obtener solo las filas correspondientes al desarrollador dado
    #carga el df sentiment analisis

    df_temporal = df_sentimientos[df_sentimientos['developer'] == developer]#filtra el df donde las columnas correspondan al input

    # Cuenta la cantidad de sentimientos 0, 1 y 2
    count_sentimiento_0 = df_temporal[df_temporal['sentimiento'] == 0].count()
    count_sentimiento_1 = df_temporal[df_temporal['sentimiento'] == 1].count()
    count_sentimiento_2 = df_temporal[df_temporal['sentimiento'] == 2].count()


    # Devuelve los resultados
    return str({'Negative': count_sentimiento_0.values[0],'Neutral': count_sentimiento_1.values[0],'Positive': count_sentimiento_2.values[0]})