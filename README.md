# sistema de recomendacion steam

## hola bienvenido a mi proyecto

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

