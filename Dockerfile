FROM tiangolo/uvicorn-gunicorn-fastapi

COPY ./app /app

# directorio de trabajo de la app
WORKDIR /app

#copia los requerimentos dentro de la  imagen
COPY requirements.txt ./requirements.txt

#instala los requerimentos dentro de la imagen
RUN pip install -r requirements.txt

# Argumentos para el comando entrypoint
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]