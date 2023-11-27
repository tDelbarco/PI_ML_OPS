# sistema de recomendacion steam

## hola bienvenido a mi proyecto


<img src="https://camo.githubusercontent.com/35b81f213ddb0e019b3567f6982d740bb2d01ae5dd712a1537e09e826e940228/68747470733a2f2f643331757a386c77666d796e38672e636c6f756466726f6e742e6e65742f4173736574732f6c6f676f2d68656e72792d77686974652d6c672e706e67" style="width:50%">
#imagen tipo portada mas ancho que larvo para que no ocupe tanto

###el proyecto

###que papel tendre que desempeñar
en este proyecto debere tomar tanto el papel de data enginer y data scientist.
asi teniendo que realizar el proceso de extraccion, transformacion y carga de los datos(ETL) , analisis exploratorio de datos(EDA) , y generar un modelo de aprendizaje automatico para la recomendacion de juegos
para este proyecto se me pide un MVP(minimo producto viable)
generar una API que pueda ser consumida segun los criterios de API REST o RESTful desde cualquier dispositivo conectado a internet y que cuente con varias consultas.

## la api

#las herramientas que utilize fueron las siguientes

#python,pandas,numpy,fast Api,uvicorn,render

### estructura de mi proyecto

	|-- PI_ML_Ops/                # Carpeta raíz del repositorio de GitHub

        	|-- Datasets/             # Almacena los archivos JSON comprimidos con los datos
	 
        		|-- steam_games.json.gz
        
	  		|-- user_reviews.json.gz
        		
	  		|-- user_items.json.gz
    		
      		|-- app/                  # Contiene los archivos esenciales para la API
        	
	  		|-- main.py           # Archivo principal de la aplicación FastAPI
        		
	  		|-- funciones/        # Módulo con funciones auxiliares para la API
            		
	       			|-- funciones.py  # Funciones de manipulación y procesamiento de datos
            			
	       			|-- modelo.py      # Implementación del modelo de machine learning
        		
	  		|-- df_sentimiento.parquet  # Archivo de datos parquet para análisis de sentimiento
        		
	  		|-- df_recommend.parquet    # Archivo de datos parquet para recomendaciones
       			
	  		|-- df_genero.parquet       # Archivo de datos parquet para géneros de juegos
        		
	  		|-- df_modelo.parquet       # Archivo de datos parquet para el modelo entrenado
        		
	  		|-- requirements.txt        # Archivo de dependencias del proyecto
    		
      		|-- venv/                 # Entorno virtual para pruebas locales
    		
      		|-- ETL/                  # Carpeta que contiene el proceso de manipulación de datos
        	
	  		|-- ETL.ipynb        # Jupyter Notebook para el proceso ETL
        	
	 		|-- EDA.ipynb        # Jupyter Notebook para el Análisis Exploratorio de Datos
        	
	 	|-- ETL_functions.ipynb  # Jupyter Notebook con funciones específicas para el ETL






Sistema de Recomendación Steam
¡Hola, bienvenido a mi proyecto!
Imagen de Portada <!-- Reemplaza "url_de_la_imagen" con la URL de tu imagen de portada -->

El Proyecto
En este proyecto, asumiré los roles de Data Engineer y Data Scientist. Mi tarea principal será realizar el proceso de Extracción, Transformación y Carga de datos (ETL), así como realizar un Análisis Exploratorio de Datos (EDA) y desarrollar un modelo de aprendizaje automático para la recomendación de juegos. El objetivo es crear un MVP (Mínimo Producto Viable) que consista en una API accesible desde cualquier dispositivo conectado a internet, con consultas y funciones específicas.

Consultas / Funciones
PlayTimeGenre(genero: str):

Devuelve el año con más horas jugadas para el género especificado.
Ejemplo de retorno: {"Año de lanzamiento con más horas jugadas para Género X" : 2013}
UserForGenre(genero: str):

Devuelve el usuario que acumula más horas jugadas para el género especificado y una lista de la acumulación de horas jugadas por año.
Ejemplo de retorno: {"Usuario con más horas jugadas para Género X" : us213ndjss09sdf, "Horas jugadas":[{Año: 2013, Horas: 203}, {Año: 2012, Horas: 100}, {Año: 2011, Horas: 23}]}
UsersRecommend(año: int):

Devuelve el top 3 de juegos MÁS recomendados por usuarios para el año dado (reviews.recommend = True y comentarios positivos/neutrales).
Ejemplo de retorno: [{"Puesto 1" : X}, {"Puesto 2" : Y},{"Puesto 3" : Z}]
UsersWorstDeveloper(año: int):

Devuelve el top 3 de desarrolladoras con juegos MENOS recomendados por usuarios para el año dado (reviews.recommend = False y comentarios negativos).
Ejemplo de retorno: [{"Puesto 1" : X}, {"Puesto 2" : Y},{"Puesto 3" : Z}]
sentiment_analysis(empresa_desarrolladora: str):

Según la empresa desarrolladora, devuelve un diccionario con el nombre de la desarrolladora como llave y una lista con la cantidad total de registros de reseñas de usuarios categorizados con un análisis de sentimiento como valor.
Ejemplo de retorno: {'Valve' : [Negative = 182, Neutral = 120, Positive = 278]}
Herramientas Utilizadas
Python
Pandas
NumPy
FastAPI
Uvicorn
Render (Plataforma de implementación)
Este proyecto se enfoca en la creación de una API robusta y funcional que cumple con los estándares RESTful y puede ser consumida de manera eficiente desde cualquier dispositivo conectado a internet. ¡Gracias por explorar mi proyecto! Si tienes alguna pregunta o necesitas más información, no dudes en contactarme.

pasos para deployar de forma local 

forkear el repositorio

./venv/Scripts/Activate(esto desde el directorio raiz de el el prouecto PI_ML_OPS)

cd app

uvicorn main:app --reload

ctrl + c

deactivate











   

