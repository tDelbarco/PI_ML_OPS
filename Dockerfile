FROM tiangolo/uvicorn-gunicorn-fastapi

COPY ./app /app

# directorio de trabajo de la app
WORKDIR /app

#instala los requerimentos dentro de la imagen
RUN pip install -r /app/requirements_docker.txt

# Argumentos para el comando entrypoint
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]