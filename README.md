<p align=center><img src=https://d31uz8lwfmyn8g.cloudfront.net/Assets/logo-henry-white-lg.png><p>

# <h1 align=center> **PROYECTO INDIVIDUAL Nº1** </h1>

# <h1 align=center>**`Machine Learning Operations (MLOps)`**</h1>

<p align="center">
<img src="https://user-images.githubusercontent.com/67664604/217914153-1eb00e25-ac08-4dfa-aaf8-53c09038f082.png"  height=300>
</p>

# hola bienvenido a mi proyecto
### el proyecto

en este proyecto que tiene como tematica steam() debere tomar tanto el papel de **data enginer** y **data scientist**.
asi teniendo que realizar el proceso de **extraccion**, **transformacion** y **carga de los datos**(**ETL**) , analisis exploratorio de datos(**EDA**) , y generar un modelo de aprendizaje automatico para la recomendacion de juegos
para este proyecto se me pide un **MVP**(minimo producto viable)
generar una API que pueda ser consumida segun los criterios de **API REST** o **RESTful** desde cualquier dispositivo conectado a internet y que cuente con varias consultas.

### las herramientas que utilize fueron las siguientes

# python,pandas,numpy,fast Api,uvicorn,render

<h1>Índice de Navegación</h1>

<ul>
    <li><a href="#seccion1">Acceso a la api a travez de render y video demostracion de su funcionamiento</a></li>
    <li><a href="#seccion2">Estructura de el proyecto</a></li>
    <li><a href="#seccion3">posibles consultas a la api</a></li>
    <li><a href="#seccion4">Como ejecutar la api de forma local</a></li>
    <li><a href="#seccion5">Contactame a travez de :</a></li>
</ul>



<section id="seccion1">

  <h2><a href="https://pi-ml-ops-c1ks.onrender.com/docs#/">LINK</a> de la api deployada en render</h2>
  <p><a href="https://pi-ml-ops-c1ks.onrender.com/docs#/">https://pi-ml-ops-c1ks.onrender.com/docs#/</a></p>

  <h2><a href="#">LINK</a> de video demostracíon</h2>
  <p><a href="#">https://pi-ml-ops-c1ks.onrender.com/docs#/</a></p>
</section>

<section id="seccion2">
  <h1>estructura de mi proyecto</h1>
  <p>
    en esta seccion hago un resumen de las carpetas y archivos (sus propositos) en este repositorio de github:
  </p>
</section>



	|-- PI_ML_Ops/                # Carpeta raíz del repositorio de GitHub

        	|-- Datasets/             # Almacena los archivos JSON comprimidos con los datos(tambien posee cualquier otro archivo resultante a partir de estos que no sea directamente utilizado por la api)
	 
        	  	|-- steam_games.json.gz
        
	  		      |-- user_reviews.json.gz
        		
	  		      |-- user_items.json.gz
    		
      		|-- app/                  # Contiene los archivos esenciales para la API
        	
	  		      |-- main.py           # Archivo principal de la aplicación FastAPI
        		
	  		      |-- funciones/        # Módulo con funciones auxiliares para la API
            		
	       			    |-- funciones.py  # Funciones de manipulación y procesamiento de datos
            			
	       			    |-- modelo.py      # Implementación del modelo de machine learning
        		
	  		      |-- df_sentimientos.parquet  # Archivo de datos parquet utilizado para la respuesta de la api a la consulta de (sentiment_analysis)

	  		      |-- df_recommend.parquet    # Archivo de datos parquet utilizado para la respuesta de la api a las consultas de (UsersRecommend y UsersWorstDeveloper)

	  		      |-- df_genero.parquet       # Archivo de datos parquet utilizado para la respuesta de la api a las consultas de (PlayTimeGenre y UserForGenre)

	  		      |-- df_modelo.parquet       # Archivo de datos parquet utilizado para la respuesta de la api a la recommendacion de juegos (recomendacion_juego)

	  		      |-- requirements.txt        # Archivo de dependencias del proyecto (este posee todas las librerias necesarias para ejecutar la api)
    		
      		|-- venv/                 # Entorno virtual para pruebas locales(tambien fue utilizado para generar el requirements.txt)
    		
      		|-- ETL_&_EDA/                  # Carpeta que contiene el proceso de manipulación de datos
        	
	        		|-- ETL.ipynb        # Jupyter Notebook para el proceso ETL(extraccion, transformacion y carga de datos)
        	
	 	        	|-- EDA.ipynb        # Jupyter Notebook para el Análisis Exploratorio de Datos
        	
	 	            |-- ETL_functions.ipynb  # Jupyter Notebook con funciones específicas para el ETL







<section id="seccion3">


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









</section>






<section id="seccion4">
    <h2>instrucciones para deployear la api de forma local</h2>
    <p>en caso de querer ejecutar esta api de forma local una vez forkeado el repositorio(windows):</p>
    <p>se debe abrir una consola de comandos en la ruta dentro de la carpeta PI_ML_OPS:</p>
    <code>./venv/Scripts/Activate</code>
    <p>con esto debera salir(venv) al principio de la ruta esto significa que el entorno virtual se encuentra activo</p>
    <p>ahora debemos entrar dentro de la carpeta app que es aquella que tiene la api en si</p>
    <code>cd app</code>
    <p>una vez dentro de el directorio app</p>
    <code>uvicorn main:app --reload</code>
    <p>con esto ya tendriamos nuestra api corriendo de forma local en el el puerto 8000 y podemos acceder a ella a travez de <a href="localhost:8000">localhost:8000</a></p>
    <p>en caso de detener el funcionamiento de la api</p>
    <code>ctrl + c</code>
    <p>en caso de querer desactivar el entorno virtual</p>
    <code>deactivate</code>
</section>






<section id="seccion5">
  contactame en:

  link github

  link linkedin


</section>

   

