# infovis-Final

Grupo 1. Integrantes: Tamara Puig, Felipe Gorostiaga y Ximena Zuberbuhler.

## Requisitos previos para el correcto funcionamiento:

  Se debe tener instalado y corriendo a la hora de ejecutar la api una instancia de postgreSQL.

  Se debe tener instalado python y las siguientes librerias:

    * typing
    * sqlalchemy
    * fastapi
    * pydantic
    * uvicorn
    * starlette
    
  Para la visualización:
 
    * pandas
    * geopandas
    * altair
    * jupyter
    * matplotlib

 ## Para importar o actualizar los datos de la base de datos se debe correr:
 
 ```
 ./import.sh <host> <database> <user> <password>
 ```
 
 Siendo user y password los asociados a su usuario de postgreSQL.
 
 Por default se debe utilizar `host = localhost`, `database = infovis`, `user = postgres` y `password = password`. __Si se desea utlizar alguno diferente, se debe actualizar en el archivo `sql_app/database.py` en la linea 6__.
 
 Ejemplo:
 
  ```
  ./import.sh localhost infovis postgres password 
  ```

  ## Para ejecutar la api se debe correr:

  ```
  uvicorn main:app --reload
  ```
  
  Por default se corre en localhost en el puerto 8000, en caso de querer cambiar esto se debe agregar `--host <host>` y `--port <port>`.
  
  ## Para ver la visualización:
  
  Se debe correr el jupyter notebook:
  
  ```
  jupyter notebook
  ```
  
  
