## Calculo de factorial mediante computacion distribuida

Trabajo de la asignatura de Sistemas Distribuidos de la Universidad de Cadiz.

### 1. Autores.

* Borrego Fajardo,Carlos
* Cabeza de Vaca Román ,Germán
* Castro Monterrosa. Edson Anatoly

### 2. Descripción.


### 3. Guía de funcionamiento.

En terminal acceder a la carpeta donde estén los archivos del servidor.

1. python auxserv1.py
2. python auxserv2.py
3. python server.py

En terminal acceder a la carpeta donde este el cliente.
El cliente recibirá un numero entero por terminal y devolverá su factorial.

1. python client.py num
  
### 4. Entorno de pruebas.

* Con el servidor y los auxialires lanzados se hace prueba del factorial de 1 en el cliente: python client.py 1 el resultado es 1.

* Con el servidor y los auxialires lanzados se hace prueba del factorial de 5 en el cliente: python client.py 5 el resultado es 120.

* Con el servidor y los auxialires lanzados se hace prueba del factorial de 10 en el cliente: python client.py 10 el resultado es 3628800.
  
* Con el servidor y los auxialires lanzados se hace prueba del factorial de 12 en el cliente: python client.py 12 el resultado es 479001600.
