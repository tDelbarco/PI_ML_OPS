import pandas as pd










#Devuelve el top 3 de juegos MÁS recomendados por usuarios para el año dado. (reviews.recommend = True y comentarios positivos/neutrales)
    #return {} #Ejemplo de retorno: [{"Puesto 1" : X}, {"Puesto 2" : Y},{"Puesto 3" : Z}]
def usersbestdeveloper(anio,df):
    df_f = df[df['posted'].str.contains(str(anio))] #filtro el df al año
    df_f = df_f[(df_f['sentimiento'] == 2) | (df_f['recommend'] == True)]#filtro el df a los que al menos poseen uno de las 2 cosas que vamos a contar

    conteo_sentimiento = df_f[df_f['sentimiento'] == 2].groupby('item_id')['sentimiento'].count()
    conteo_recommend = df_f[df_f['recommend'] == False].groupby('item_id')['recommend'].count()

    conteo_df = pd.df( conteo_recommend,conteo_sentimiento, on='item_id', how='inner')

    df_f = df_f.df(conteo_df,how="inner",left_on="id",right_on="item_id")

    df_f = df_f.drop_duplicates(subset=['item_id'])

    df_f = df_f.sort_values(by=['recommend_y','sentimiento_y'], ascending=[False, False])

    return df_f





#Devuelve el top 3 de desarrolladoras con juegos MENOS recomendados por usuarios para el año dado. (reviews.recommend = False y comentarios negativos)
    #return {} #Ejemplo de retorno: [{"Puesto 1" : X}, {"Puesto 2" : Y},{"Puesto 3" : Z}]
def usersworstdeveloper(anio,df):
    df_f = df[df['posted'].str.contains(str(anio))] #filtro el df al año
    df_f = df_f[(df_f['sentimiento'] == 0) | (df_f['recommend'] == False)]#filtro el df a los que al menos poseen uno de las 2 cosas que vamos a contar

    conteo_sentimiento = df_f[df_f['sentimiento'] == 2].groupby('item_id')['sentimiento'].count()
    conteo_recommend = df_f[df_f['recommend'] == False].groupby('item_id')['recommend'].count()

    conteo_df = pd.df( conteo_recommend,conteo_sentimiento, on='item_id', how='inner')

    df_f = df_f.df(conteo_df,how="inner",left_on="id",right_on="item_id")

    df_f = df_f.drop_duplicates(subset=['item_id'])

    df_f = df_f.sort_values(by=['recommend_y','sentimiento_y'], ascending=[False, False])

    return df_f




#Según la empresa desarrolladora, se devuelve un diccionario con el nombre de la desarrolladora como llave y una lista con la cantidad total de registros de reseñas de usuarios que se encuentren categorizados con un análisis de sentimiento como valor.
   # return {} #Ejemplo de retorno: {'Valve' : [Negative = 182, Neutral = 120, Positive = 278]}
def contar_sentimientos_por_desarrollador(developer,df):
    # Filtra el DataFrame para obtener solo las filas correspondientes al desarrollador dado
    #carga el df sentiment analisis

    df_temporal = df[df['developer'] == developer]#filtra el df donde las columnas correspondan al input

    # Cuenta la cantidad de sentimientos 0, 1 y 2
    count_sentimiento_0 = df_temporal[df_temporal['sentimiento'] == 0].count()
    count_sentimiento_1 = df_temporal[df_temporal['sentimiento'] == 1].count()
    count_sentimiento_2 = df_temporal[df_temporal['sentimiento'] == 2].count()

    # Devuelve los resultados
    return {
        'sentimiento_0': count_sentimiento_0.values[0],
        'sentimiento_1': count_sentimiento_1.values[0],
        'sentimiento_2': count_sentimiento_2.values[0]
    }

# Ejemplo de uso
developer_stats = contar_sentimientos_por_desarrollador('Tripwire Interactive')
print(developer_stats)