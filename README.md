# GESTY
Python music downloader

### Instalacion
 
##### Extraiga los archivos archivos de Python en una carpeta y cree dentro de ella una carpeta llamada Musica

`C:\Example\` Carpeta raiz

`C:\Example\Musica` Carpeta nueva

##### Instale los requerimientos del script 

```python
pip install -r requirements.txt
```

### Uso
Son tres los script disponibles:
##### Gesty.py:
Tiene interfaz grafica creada con WxPython, si todo sale correctamente se abrira una ventana con una barra de busqueda    Solo introduzca el nombre del artista y el nombre de la cancion y se descargara la cancion que mas coincida con su busqueda

##### Gesty_Command.py:
Igual que Gesty pero solo desde la linea de comandos, si todo sale correctamente se abrira la linea de comandos preguntando que cancion desea descargar solo introduzca el nombre del artista y el nombre de la cancion y se descargara la cancion que mas coincida con su busqueda

##### Gesty_Tops.py:
Si no sabe que cancion desea descargar Gesty_Tops.py te mostrara mediante linea de comandos las canciones que se encuentrar en el top 25 del genero que tu decidas.
Al entrar en el script saldran los generos musicales, pon el numero que esta al lado izquerdo de este y se mostrara el top 25 mundial
Puedes elegir si descargar la cancion o no. si lo deseas solo digitando el numero de la cancion comenzara la descarga
