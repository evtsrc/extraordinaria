# Práctica convocatoria extraordinaria CE3
Tienes hasta el día 21 de Junio para entregar esta práctica
## Enunciado Docker
Para esta parte de la práctica crearemos dos imágenes Docker, una de frontend y otra de midleware.
1. La imagen de midleware, tendrá como mínimo lo siguiente:
    * una imagen base oficial de python
    * el meta-dato necesario que identifique al desarrollador
    * la variable de entorno PORT, que define el puerto en el que escuchará el servicio de python, inicializada a 2000
    * una copia del Dockerfile en el directorio /tmp
    * el fichero server.py que se os proporciona, en una ruta de trabajo definida previamente
    * y el comando que arranque el servicio de python.

2. Para la de Frontend, se os proporciona los ficheros: nginx.conf y el run.sh
    * La imagen se basará en la última versión oficial de nginx
    * se copiará el Dockerfile al directorio /tmp
    * tendrá el meta-dato que identifique al desarrollador
    * dos variables de entorno (PY_SERVER y PY_PORT) inicializadas al valor deseado
    * el directorio de trabajo será el /etc/nginx
    * la imagen contendrá los dos ficheros proporcionados
    * y el script de arranque por defecto será el run.sh

### Notas 
  * Las imágenes se generarán con el nombre <USER>_img_python y <USER>_img_nginx

##  Enunciado docker-compose
Definir en el fichero yaml dos servicios:
  * <USER>_python_srv y <USER>_nginx_srv especificando la dependencia entre ellos
  * cambiar el puerto donde escucha el servicio de python por el 6000
  * definir las variables de entorno necesarios para que se conecten entre ellos
  * montar el directorio /data del servicio <USER>_python_srv con un volumen llamado <USER>_data



### Notas
  * No se volverá a construir ninguna imagen, se utilizarán las imágenes construidas en el apartado anterior <USER>_img_python y <USER>_img_nginx).
  * Se comprobará que ambos servicios están bien integrados llamando al método /hostname del servicio de python a través del Frontend (puerto 80 del nginx). 
  ```bash 
  wget -qO- <URL_NGINX>:80/hostname
  ```
  * Para validar que el volumen está bien definido e integrado
  * llamaremos a los métodos /write y /read
  ```bash 
  wget -qO- <URL_NGINX>:80/write
  wget -qO- <URL_NGINX>:80/read
 ```
  * reiniciaremos docker-compose
  * llamaremos al método /read 
  ```bash 
  wget -qO- <URL_NGINX>:80/read
  ```

## Enunciado Kubernetes

Para la realización de esta práctica se solicita la creación de un cluster de minikube con un registry configurado. En este cluster habrá que arrancar las imagenes creadas con Docker en un namespace llamado miku:

1. El pod de Python tendrá que:
    * tener un volúmen donde poder persistir los datos
        * El volúmen tiene que montarse desde el directorio /data de minikube y en el /data en la imagen de Python
    * Configurarse con solo una réplica
    * Límite de CPU: 0.2
    * Límite memoria: 128 Mi
    * Levantar el Python en el puerto 4444

2. El pod de nginx tendrá las siguientes características:
    * El número de pods en un inicio tendrá que ser 1
    * Límite de CPU: 0.125
    * Límite memoria: 64 Mi

3. Se tiene que acceder a la aplicación pasando por nginx mediante un servicio de tipo LoadBalancer en el puerto 8080.

## Configuraciones adicionales

* Configuración del escalado automático
* Configuración de liveness y readiness
* Añadir algún componente de kubernetes extra

### Deployment nginx

1. Configurar prueba de readiness para comprobar el puerto en el que levante. La configuración de esta prueba tiene que:
    * empezar con un delay de 10 segundos.
    * comprobarse cada 30 segundos.
    * no dar el testeo por bueno hasta el segundo intento.
2. Configurar el autoescalado para que cuando se supere el 60% de uso memoria se escale automáticamente hasta un límite de 3 (**Cuidado** con la versión del API de esta configuración).

### Deployment Python

1. Configurar un test de liveness de tipo http al /healthz que:
    * empieze con un delay de 20 segundos.
    * se compruebe cada 40 segundos.
    * se reinicie en el primer testeo con error.

## Entregables

1. Entregar en un paquete tar comprimido con tu nombre y apellido (p.e. NombreApellido.tar.gz) que contenga:
    * Los dos Dockerfile para la creación de imágenes
    * docker-compose.yaml
    * los yaml de definición de todos los objetos pedidos en el enunciado.

> En caso de creerlo conveniente, añadir un fichero README.txt con lo que se quiera comentar: comandos de despliegue, configuraciones a tener en cuenta, problemas encontrados y soluciones, etc.

# Evaluación
No se evaluará nada que no arranque con los ficheros entregados. Esto quiere decir que si no se puede crear la imagen con los ficheros Dockerfile entregados o no se arrancan los objetos de k8s con los yaml de definición no se podrá obtener un aprobado.

|Entrega|Valor|
|------------------|-----------|	
|Dockerfiles|20%|
|Docker-compose|+5%|
|Despliegue en k8s|+25%|
|Escalado automático|+10%|
|Liveness & Readiness|+15%|
