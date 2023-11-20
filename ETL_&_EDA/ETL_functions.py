

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
