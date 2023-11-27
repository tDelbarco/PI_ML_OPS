import pandas as pd



df_genero = pd.read_parquet("df_genero.parquet")
df_recommend = pd.read_parquet("df_recommend.parquet")
df_sentimientos = pd.read_parquet("df_sentimientos.parquet")




def horas_año_genero(genero):

    df_hg = df_genero.copy()#copio el dataframe ya que me causa problemas con el original sino
    df_hg = df_hg[df_hg['genres'].str.contains(genero, case=False, na=False)]# Filtra el DataFrame para el género específico

    horas_por_año = df_hg.groupby('release_date')['playtime_forever'].sum()# Agrupa por año y suma las horas jugadas

    año_mas_jugado = horas_por_año.idxmax()#obtengo el año con mas horas jugadas

    return str({"Año de lanzamiento con más horas jugadas para Género": genero, "Año más jugado": año_mas_jugado})




def usuario_genero(genero):
    df_ug = df_genero.copy()  #copio el dataframe ya que me causa problemas con el original sino
    df_filtrado = df_ug[df_ug['genres'].str.contains(genero, case=False, na=False)]

    if df_filtrado.empty:#verifica si el df_filtrado no me dio vacio
        return {"Usuario con más horas jugadas para Género": None, "Horas jugadas": []}#en caso de que el df_filtrado este vacio retorna esto

    horas_por_año = (df_filtrado.groupby(['release_date', 'user_id'])['playtime_forever'].sum() / 60).astype(int).reset_index()# Calcular las horas jugadas por año y usuario (dividimos el tiempo en minutos por 60 para obtener las horas)

    
    usuario_mas_jugado_por_año = horas_por_año.loc[horas_por_año.groupby('release_date')['playtime_forever'].idxmax()]# Encuentro al usuario con más horas jugadas por año

    return str({
        "Usuario con más horas jugadas para Género": usuario_mas_jugado_por_año["user_id"].idxmax(),
        "Horas jugadas": [{"Año": año, "Horas": horas} for año, horas in usuario_mas_jugado_por_año.groupby('release_date')['playtime_forever'].sum().items()]
    }) #diccionario que contiene el genero y una lista con las horas jugadas por año por el usuario que mas jugo al genero






def juegos_mas_recomendados(anio):
    df_f = df_recommend[df_recommend['posted'].str.contains(str(anio))]  #filtro el df al año
    df_f = df_f[(df_f['sentimiento'].isin([1,2]) | (df_f['recommend'] == True))]#filtro el df a los que cumplen las condiciones(comentarios positivos o neutrales y recommend igual a true)
    #df_f = df_f[(df_f['sentimiento'] == 2) | (df_f['recommend'] == True)]

    conteo_sentimiento = df_f[df_f['sentimiento'].isin([1,2])].groupby('item_id')['sentimiento'].count()#cuento la cantidad de sentimiento igual a 1 o 2 para cada item_id
    #conteo_sentimiento = df_f[df_f['sentimiento'] == 2].groupby('item_id')['sentimiento'].count()#cuento la cantidad de sentimiento igual a 1 o 2 para cada item_id
    conteo_recommend = df_f[df_f['recommend'] == True].groupby('item_id')['recommend'].count()   #cuento la cantidad de recommend = True para cada item_id

    conteo_df = pd.merge( conteo_recommend,conteo_sentimiento, on='item_id', how='inner')#junto las 2 series en donde hize los conteo en un conteo_df

    df_f = df_f.merge(conteo_df,how="inner",left_on="id",right_on="item_id")#junto donde df_f y conteo_df se releacionan por item id

    df_f = df_f.drop_duplicates(subset=['item_id'])#dropeo los duplicados ya que solo necesito un unico registro por cada item id que ya posee las columnasde conteo_df

    df_f = df_f.sort_values(by=['recommend_y','sentimiento_y'], ascending=[False, False])#ordeno de forma decendente por mayor cantidad de recommend = true y comentarios neutrales y positivos

    return [{"Puesto " + str(i + 1): app_name} for i, app_name in enumerate(df_f['app_name'][:3])]#lista de diccionarios que posee puesto y app_name de los primeros 3 app_name(las 3 primeras filas el nombre de juego)






def developer_menos_recomendadas(anio):
    df_f = df_recommend[df_recommend['posted'].str.contains(str(anio))]   #filtro el df al año
    df_f = df_f[(df_f['sentimiento'] == 0) | (df_f['recommend'] == False)]#filtro el df a los que cumplen las condiciones(comentarios negativos y recommend = false)

    conteo_sentimiento = df_f[df_f['sentimiento'] == 0].groupby('developer')['sentimiento'].count()#cuento la cantidad de sentimiento igual a 0 para cada desarrolladora
    conteo_recommend = df_f[df_f['recommend'] == False].groupby('developer')['recommend'].count()  #cuento la cantidad de recommend igual a False paraa cada desarrollador

    conteo_df = pd.merge( conteo_recommend,conteo_sentimiento, on='developer', how='inner')# junto las 2 series resultantes de las cantidades por desarrollador para armar conteo_df

    df_f = df_f.merge(conteo_df,how="inner",on="developer")#junto donde conteo_df con df_f se relacionan por la columna desarrollador

    df_f = df_f.drop_duplicates(subset=['developer'])#borro los duplicados en la columna developer de df_f ya que tenia varios registros por desarrollador y solo necesito 1 unico por cada desarrollador

    df_f = df_f.sort_values(by=['recommend_y','sentimiento_y'], ascending=[False, False])#  ordeno de forma decendente por cantidad de recomend = false y comentarios negativos

    return [{"Puesto " + str(i + 1): developer} for i, developer in enumerate(df_f['developer'][:3])]#lista de diccionarios que posee puesto y desarrollador de los primeros 3 desarrollaadores 





def contar_sentimientos_por_desarrollador(developer):

    df_temporal = df_sentimientos[df_sentimientos['developer'] == developer]#filtra el df donde las columnas correspondan al input

    # Cuenta la cantidad de sentimientos 0, 1 y 2
    count_sentimiento_0 = df_temporal[df_temporal['sentimiento'] == 0].count()
    count_sentimiento_1 = df_temporal[df_temporal['sentimiento'] == 1].count()
    count_sentimiento_2 = df_temporal[df_temporal['sentimiento'] == 2].count()


    # Devuelve los resultados en diccionario 
    return str({'Negative': count_sentimiento_0.values[0],'Neutral': count_sentimiento_1.values[0],'Positive': count_sentimiento_2.values[0]}) #el str(diccionario) me permite  que se  pasen a la api si paso diccionario solo me marca error