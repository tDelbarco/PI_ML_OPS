def limpieza_lista(df, columna):
    """
    
    """
    temp = df[columna].copy()
    temp = temp.str.strip("[]").str.strip("\\'")
    valores =  temp.str.split(",")
    return valores                              #devuelva una serie de listas

def valores_lista(df,columna):
    """


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
import pandas as pd
#from textblob import TextBlob

def data_review(df):
    '''
    This function provides detailed information about the dtype and null values present in a dataframe
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

def replace_all_nulls(df):
    '''
    Recieves a df as parameter and fill all the null values per column depending on their dType
    '''

    for column in df.columns:
        mask = df[column].notnull()
        dtype = df[column][mask].apply(type).unique()

        if dtype[0] == str:
            df[column] = df[column].fillna('No data')
        if dtype[0] == float:
            mean = df[column].mean()
            df[column] = df[column].fillna(mean)

#def get_sentiment(review):
#    analysis = TextBlob(review)
#    if analysis.sentiment.polarity < 0:
#        return 0
#    elif analysis.sentiment.polarity == 0:
#        return 1
#    else:
#        return 2