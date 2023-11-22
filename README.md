# sistema de recomendacion steam

###hola bienvenido a mi proyecto

#imagen tipo portada mas ancho que larvo para que no ocupe tanto

###el proyecto

###que papel tendre que desempeñar
en este proyecto debere tomar tanto el papel de data enginer y data scientist.
asi teniendo que realizar el proceso de extraccion, transformacion y carga de los datos(ETL) , analisis exploratorio de datos(EDA) , y generar un modelo de aprendizaje automatico para la recomendacion de juegos
para este proyecto se me pide un MVP(minimo producto viable)
generar una API que pueda ser consumida segun los criterios de API REST o RESTful desde cualquier dispositivo conectado a internet y que cuente con varias consultas.

<!--endpoints(funciones)-->
<nombre que reciben y que devuelven>
### consultas / funciones
*
*
*
*
*

#las herramientas que utilize fueron las siguientes

#python,pandas,numpy,fast Api,uvicorn,render

###estructura de mi proyecto

PI_ML_OPS
  /app
    /
    data_procesada
       /steam_games.parquet
       /user_reviews.parquet
       /user_itrms.parquet
    main.py
    funciones
   /Datasets
     /.json.gz
     /
     /

  /Dockerfile
  /.gitignore



<!--
Propuesta de trabajo (requerimientos de aprobación)
Transformaciones: Para este MVP no se te pide transformaciones de datos(aunque encuentres una motivo para hacerlo) pero trabajaremos en leer el dataset con el formato correcto. Puedes eliminar las columnas que no necesitan para responder las consultas o preparar los modelos de aprendizaje automático, y de esa manera optimizar el rendimiento de la API y el entrenamiento del modelo.

Feature Engineering: En el dataset user_reviews se incluyen reseñas de juegos hechos por distintos usuarios. Debes crear la columna 'sentiment_analysis' aplicando análisis de sentimiento con NLP con la siguiente escala: debe tomar el valor '0' si es malo, '1' si es neutral y '2' si es positivo. Esta nueva columna debe reemplazar la de user_reviews.review para facilitar el trabajo de los modelos de machine learning y el análisis de datos. De no ser posible este análisis por estar ausente la reseña escrita, debe tomar el valor de 1.

Desarrollo API: Propones disponibilizar los datos de la empresa usando el framework FastAPI. Las consultas que propones son las siguientes:

Debes crear las siguientes funciones para los endpoints que se consumirán en la API, recuerden que deben tener un decorador por cada una (@app.get(‘/’)).

def PlayTimeGenre( genero : str ): Debe devolver año con mas horas jugadas para dicho género.
Ejemplo de retorno: {"Año de lanzamiento con más horas jugadas para Género X" : 2013}

def UserForGenre( genero : str ): Debe devolver el usuario que acumula más horas jugadas para el género dado y una lista de la acumulación de horas jugadas por año.
Ejemplo de retorno: {"Usuario con más horas jugadas para Género X" : us213ndjss09sdf, "Horas jugadas":[{Año: 2013, Horas: 203}, {Año: 2012, Horas: 100}, {Año: 2011, Horas: 23}]}

def UsersRecommend( año : int ): Devuelve el top 3 de juegos MÁS recomendados por usuarios para el año dado. (reviews.recommend = True y comentarios positivos/neutrales)
Ejemplo de retorno: [{"Puesto 1" : X}, {"Puesto 2" : Y},{"Puesto 3" : Z}]

def UsersWorstDeveloper( año : int ): Devuelve el top 3 de desarrolladoras con juegos MENOS recomendados por usuarios para el año dado. (reviews.recommend = False y comentarios negativos)
Ejemplo de retorno: [{"Puesto 1" : X}, {"Puesto 2" : Y},{"Puesto 3" : Z}]

def sentiment_analysis( empresa desarrolladora : str ): Según la empresa desarrolladora, se devuelve un diccionario con el nombre de la desarrolladora como llave y una lista con la cantidad total de registros de reseñas de usuarios que se encuentren categorizados con un análisis de sentimiento como valor.
Ejemplo de retorno: {'Valve' : [Negative = 182, Neutral = 120, Positive = 278]}


Importante
El MVP tiene que ser una API que pueda ser consumida segun los criterios de API REST o RESTful desde cualquier dispositivo conectado a internet. Algunas herramientas como por ejemplo, Streamlit, si bien pueden brindar una interfaz de consulta, no cumplen con las condiciones para ser consideradas una API, sin workarounds.

Deployment: Conoces sobre Render y tienes un tutorial de Render que te hace la vida mas fácil 😄 . 


Análisis exploratorio de los datos: (Exploratory Data Analysis-EDA)

Ya los datos están limpios, ahora es tiempo de investigar las relaciones que hay entre las variables del dataset, ver si hay outliers o anomalías (que no tienen que ser errores necesariamente 👀 ), y ver si hay algún patrón interesante que valga la pena explorar en un análisis posterior. Las nubes de palabras dan una buena idea de cuáles palabras son más frecuentes en los títulos, ¡podría ayudar al sistema de predicción! En esta ocasión vamos a pedirte que no uses librerías para hacer EDA automático ya que queremos que pongas en práctica los conceptos y tareas involucrados en el mismo. Puedes leer un poco más sobre EDA en este articulo

Modelo de aprendizaje automático:

Una vez que toda la data es consumible por la API, está lista para consumir por los departamentos de Analytics y Machine Learning, y nuestro EDA nos permite entender bien los datos a los que tenemos acceso, es hora de entrenar nuestro modelo de machine learning para armar un sistema de recomendación. Para ello, te ofrecen dos propuestas de trabajo: En la primera, el modelo deberá tener una relación ítem-ítem, esto es se toma un item, en base a que tan similar esa ese ítem al resto, se recomiendan similares. Aquí el input es un juego y el output es una lista de juegos recomendados, para ello recomendamos aplicar la similitud del coseno. La otra propuesta para el sistema de recomendación debe aplicar el filtro user-item, esto es tomar un usuario, se encuentran usuarios similares y se recomiendan ítems que a esos usuarios similares les gustaron. En este caso el input es un usuario y el output es una lista de juegos que se le recomienda a ese usuario, en general se explican como “A usuarios que son similares a tí también les gustó…”. Deben crear al menos uno de los dos sistemas de recomendación (Si se atreven a tomar el desafío, para mostrar su capacidad al equipo, ¡pueden hacer ambos!). Tu líder pide que el modelo derive obligatoriamente en un GET/POST en la API símil al siguiente formato:

Si es un sistema de recomendación item-item:

def recomendacion_juego( id de producto ): Ingresando el id de producto, deberíamos recibir una lista con 5 juegos recomendados similares al ingresado.
Si es un sistema de recomendación user-item:

def recomendacion_usuario( id de usuario ): Ingresando el id de un usuario, deberíamos recibir una lista con 5 juegos recomendados para dicho usuario.
Video: Necesitas que al equipo le quede claro que tus herramientas funcionan realmente! Haces un video mostrando el resultado de las consultas propuestas y de tu modelo de ML entrenado! Recuerda presentarte, contar muy brevemente de que trata el proyecto y lo que vas a estar mostrando en el video. Para grabarlo, puedes usar la herramienta Zoom, haciendo una videollamada y grabando la pantalla, aunque seguramente buscando, encuentres muchas formas más. 😉

Spoiler: El video NO DEBE durar mas de 7 minutos y DEBE mostrar las consultas requeridas en funcionamiento desde la API y una breve explicación del modelo utilizado para el sistema de recomendación. En caso de que te sobre tiempo luego de grabarlo, puedes mostrar/explicar tu EDA, ETL e incluso cómo desarrollaste la API.

-->

<hr>
steam_games.gz.json

|Columna|Descripción|Ejemplo|
|-------|-----------|-------|
|publisher|	Empresa publicadora del contenido|	[Ubisoft,Dovetail Games - Trains,Degica]|
|genres|Genero del contenido|[Action, Adventure, Racing, Simulation, Strategy]
|app_name|Nombre del contenido|[Warzone, Soundtrack, Puzzle Blocks]
|title|Titulo del contenido|[The Dream Machine: Chapter 4 , Fate/EXTELLA - Sweet Room Dream, Fate/EXTELLA - Charming Bunny]
|url|URL de publicación del contenido|http://store.steampowered.com/app/761140/Lost_Summoner_Kitty/
|release_date|	Fecha de lanzamiento|[2018-01-04]
|tags|etiquetas de contenido|[Simulation, Indie, Action, Adventure, Funny, Open World, First-Person, Sandbox, Free to Play]
|discount_price|precio de descuento|[22.66, 0.49, 0.69]
|reviews_url|Reviews de contenido|http://steamcommunity.com/app/681550/reviews/?browsefilter=mostrecent&p=1
|specs|	Especificaciones|[Multi-player, Co-op, Cross-Platform Multiplayer, Downloadable Content]
|price|	Precio del contenido|[4.99, 9.99, Free to Use, Free to Play]
|early_access|acceso temprano	|[False, True]
|id|identificador unico de contenido|[761140, 643980, 670290]
|developer|	Desarrollador|[Kotoshiro, Secret Level SRL, Poolians.com]
|metascore|	Score por metacritic|[80, 74, 77, 75]
		
<hr>

user_reviews.gz.json		

|Columna|Descripción|Ejemplo|
|-------|-----------|-------|
|user_id	|identificador unico de usuario	[76561197970982479, evcentric, maplemage]|
|user_url|	URL perfil del usuario	http://steamcommunity.com/id/evcentric|
|reviews	|Review de usuario en formato Json	{'funny': '', posted': 'Posted September 8, 2013.','last_edited': '','item_id': '227300','helpful': '0 of 1 people (0%) found this review helpful','recommend': True,'review': "For a simple (it's actually not all that simple but it can be!) truck driving Simulator, it is quite a fun and relaxing game. Playing on simple (or easy?) its just the basic WASD keys for driving but (if you want) the game can be much harder and realistic with having to manually change gears, much harder turning, etc. And reversing in this game is a ♥♥♥♥♥, as I imagine it would be with an actual truck. Luckily, you don't have to reverse park it but you get extra points if you do cause it is bloody hard. But this is suprisingly a nice truck driving game and I had a bit of fun with it."},|
		
<hr>

user_items.gz.json		

|Columna|Descripción|Ejemplo|
|-------|-----------|-------|
|user_id|	identificador unico de usuario	|[76561197970982479, evcentric, maplemage]
|user_url|	URL perfil del usuario	|http://steamcommunity.com/id/evcentric
|items|	Items de usuario en formato Json	|{'item_id': '273350', 'item_name': 'Evolve Stage 2', 'playtime_forever': 58, 'playtime_2weeks': 0}
