## Cálculo de factorial mediante computación distribuida

Trabajo de la asignatura de Sistemas Distribuidos de la Universidad de Cadiz.


### 1. Autores.

* Borrego Fajardo,Carlos
* Cabeza de Vaca Román ,Germán
* Castro Monterrosa, Edson Anatoly


### 2. Descripción.

El proyecto pretende resolver el cálculo del factorial de un número, utilizando el lenguaje Python, ZeroMQ y computación distribuida, de tal manera que el cliente que necesita el factorial de un número entero positivo, ejecute mediante terminarl el programa cliente.py pasando mediante argumento el número del cuál se necesita el factorial, y se envíe la petición a un servidor, que de manera transparente al usuario utiliza dos servidores auxiliares que hacen los cálculos por medio de la división de este numero en dos, el servidor recibe la respuesta de cada uno de los servidores auxiliares y envía el resultado final al cliente que ha realizado la petición, logrando de esta manera independencia del usuario en el cálculo y velocidad de respuesta.

### 3. Entorno de pruebas.

El proyecto consta de dos partes, el servidor y servidores auxiliares están en la carpeta de Servidor y el cliente que se encuentra en la carpeta de Cliente.

Para poner el funcionamiento el servidor y los servidores auxiliares los cuales se encargan de realizan el cálculo,en terminales independientes acceder a la carpeta donde estén los archivos y ejecutarlos:

1. *python auxserv1.py*
2. *python auxserv2.py*
3. *python server.py*

Para poner en funcionamiento el cliente, en un terminal acceder a la carpeta donde este el cliente y ponerlo en  ejecución, remplazar num por el número entero positivo del cual se desea obtener el factorial.

1. *python client.py num*

El cliente devuelve el resultado del factorial en su terminal, y el servidor queda a la espera de la siguiente petición.

### 4. Pruebas realizadas.

* Con el servidor y los auxiliares lanzados se hace prueba del factorial de 1 en el cliente ejecutando *python client.py 1* el resultado obtenido es 1.

* Con el servidor y los auxiliares lanzados se hace prueba del factorial de 5 en el cliente ejecutando *python client.py 5* el resultado obtenido es 120.

* Con el servidor y los auxiliares lanzados se hace prueba del factorial de 10 en el cliente ejecutando *python client.py 10* el resultado obtenido es 3628800.
  
* Con el servidor y los auxiliares lanzados se hace prueba del factorial de 12 en el cliente ejecutando *python client.py 12* el resultado obtenido es 479001600.
