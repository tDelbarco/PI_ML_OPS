import pandas as pd


def limpieza_lista(df, columna):
    """
    esta funcion es utilizada por la funcion valores listas devuelve una serie de listas
    """
    temp = df[columna].copy()
    temp = temp.str.strip("[]").str.strip("\\'")
    valores =  temp.str.split(",")
    return valores                              #devuelve una serie de listas




def valores_lista(df,columna):
    """
    obtiene un df y su columna y devuelve los valores unicos
    """
    valores_gen = limpieza_lista(df,columna) #serie de listas

    lista_completa = []                          #en esta lista juntaremos todos los valores individuales de las listas de las series 
    for key, value in valores_gen.items():
        lista_completa.extend(value)

    lista_completa = list(set(lista_completa))   #transformamos a set para borrar duplicados

    return lista_completa





def valores_no_numericos(df_col):
    """
    recibe una columna de dataframe y devuelve una lista con los elementos que no pueden ser convertidos a numericos
    """
    import pandas as pd

    lista = []
    for i in df_col:
        try:
            pd.to_numeric(i)
        except:
            if i not in lista:
                lista.append(i)
    return lista




def rellenar_comunes(df1,df1col,df2,df2col,comunes):
    """
    recibe 2 dataframe, columna a rellenar(df1col) y columna de donde se va a tomar los valores(df2col)
      si se cumple que los valores de df2col son valores posibles en la columna a rellenar utilizando comunes(una lista que posee la interseccion entre  los valores de las columnas) 
    """
    for index,row in df1.iterrows():
        if row[df1col] == 'None':
            valores_df2 = set(df2[df2col].at[index].split(','))

            # Encuentra los valores comunes
            valores_actualizados = list(valores_df2.intersection(comunes))

            # Actualiza el valor en df1 si hay valores comunes
            if valores_actualizados:
                df1.at[index, df1col] = str(valores_actualizados)
                df1.at[index, df1col] = df1.at[index, df1col].strip("[]").replace(", ",",").replace("'","")
    return ("fin de ejecucion")


# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



def data_review(df):
    '''
    funcion que recibe un dataframe y devuelve un dataframe con informacion acerca de el dataframe ingresado
    '''

    mi_dict = {"Column": [], "dType": [], "No_Null_%": [], "No_Null_Qty": [], "Null_%": [], "Null_Qty": []}
    duplicated_rows = df[df.duplicated()]
    count_duplicated_rows = len(duplicated_rows)


    for columna in df.columns:
        porcentaje_no_nulos = (df[columna].count() / len(df)) * 100
        mi_dict["Column"].append(columna)
        mi_dict["dType"].append(df[columna].apply(type).unique())
        mi_dict["No_Null_%"].append(round(porcentaje_no_nulos, 2))
        mi_dict["No_Null_Qty"].append(df[columna].count())
        mi_dict["Null_%"].append(round(100-porcentaje_no_nulos, 2))
        mi_dict['Null_Qty'].append(df[columna].isnull().sum())

    df_info = pd.DataFrame(mi_dict)
    
    print("\nTotal rows: ", len(df))
    print("\nTotal full null rows: ", df.isna().all(axis=1).sum())
    print("\nTotal duplicated rows:", count_duplicated_rows)
    
    return df_info
