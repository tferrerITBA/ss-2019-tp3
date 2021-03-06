# ss-2019-tp3

## Compilación

Es necesario tener instalado Maven y Java 8. Comando:
```bash
mvn clean package # compilacion
java -jar target/tpes-1.0-SNAPSHOT.jar # ejecucion
```
También puede importarse el proyecto desde una IDE.

## Visualización

Asegurarse de correr el programa en modo `Single Run` y de que al finalizarse la ejecución se haya creado un archivo llamado `ovito_output.xyz`

Es necesario tener Ovito instalado.

Comandos:
```bash
ovito
# Desde ovito, en la barra de menús:
# Scripting > Run Script file... > render.py
```
*Nota*: para poder dar formato a los archivos importados con Ovito usando el script de python, es necesario editar el script con la ruta correcta a los archivos (no es necesario si se ejecuta ovito desde el directorio del proyecto)

## Análisis

Se necesita Python 3.6.4.  Correr en la carpeta `analysis` el programa:
```
pip install -r requirements.txt 
```
Y ejecutar el script corriendo:
```
python visualizer.py <directory_with_xyz_files> <mode>
```
Donde `<directory_with_xyz_files>` es el path relativo hacia un directorio con archivos output de la simulación (e.g. `test`) y `<mode>` es un entero en el conjunto `{1,2}`, donde `1` corre los analisis requeridos para calcular el coeficiente de difusion y `2` el resto de los analisis. Se separó la ejecución de esta manera ya que el análisis del coeficiente de difusión requiere archivos de tests normalizados (a intervalos regulares), mientras que el resto de los tests requiren los archivos originales.

El programa imprime los resultados por salida estandar y guarda las images calculadas en la carpeta `output`, relativa al directorio en el cual se ejecuta el programa.

Ejemplo de ejecución:
```
python visualizer.py test 2
```