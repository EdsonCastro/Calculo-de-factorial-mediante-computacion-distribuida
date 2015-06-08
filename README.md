## Cálculo de factorial mediante computación distribuida

Trabajo de la asignatura de Sistemas Distribuidos de la Universidad de Cadiz.

### 1. Autores.

* Borrego Fajardo,Carlos
* Cabeza de Vaca Román ,Germán
* Castro Monterrosa. Edson Anatoly

### 2. Descripción.
El proyecto pretende resolver el cálculo del factorial de un número, utilizando el lenguaje Python, ZeroMQ y computación distribuida, de tal manera que el cliente que necesita el factorial de un número cualquiera, ejecute cliente.py pasando mediante argumento el número del cúal se necesita el factorial, y se envíe la petición a un servidor, que de manera transparente al usuario utiliza dos servidores auxiliares que hacen los cálculos por medio de la division de este numero en dos, el servidor recibe la respuesta de cada uno de los servidores auxiliares y envía el resultado final al cliente que ha realizado la petición, logrando de esta manera independencia del usuario en el calculo y velocidad de cálculo.

### 3. Entorno de pruebas.

En terminal acceder a la carpeta donde estén los archivos del servidor.

1. python auxserv1.py
2. python auxserv2.py
3. python server.py

En terminal acceder a la carpeta donde este el cliente.
El cliente recibirá un numero entero por terminal y devolverá su factorial.

1. python client.py num
  
### 4. Pruebas realizadas. 

* Con el servidor y los auxialires lanzados se hace prueba del factorial de 1 en el cliente: python client.py 1 el resultado es 1.

* Con el servidor y los auxialires lanzados se hace prueba del factorial de 5 en el cliente: python client.py 5 el resultado es 120.

* Con el servidor y los auxialires lanzados se hace prueba del factorial de 10 en el cliente: python client.py 10 el resultado es 3628800.
  
* Con el servidor y los auxialires lanzados se hace prueba del factorial de 12 en el cliente: python client.py 12 el resultado es 479001600.
