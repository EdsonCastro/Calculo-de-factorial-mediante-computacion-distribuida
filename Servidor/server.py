#!/usr/bin/python2

import zmq

def server():
    #prepara el contexto de los sockets
    context1 = zmq.Context(1)
    context2 = zmq.Context(2)
    context3 = zmq.Context(3)
	#Prepara los sockets para recibir del cliente y mandar las tareas
    #a los auxiliares.
    sock1 = context1.socket(zmq.REP)
    sock2 = context2.socket(zmq.REQ)
    sock3 = context2.socket(zmq.REQ)
	#Levanta el servidor y conecta con los auxiliares
    sock1.bind('tcp://*:4545')
    sock2.connect('tcp://127.0.0.1:4546')
    sock3.connect('tcp://127.0.0.1:4547')
	
    print "servidor preparado..."
	#Cuerpo principal del servidor que recibe las peticiones.
    while True:
	    #creamos una variable para guardar el resultado con el caso
		#base del producto.
        total = 1
		#recibimos el numero del cliente.
        num = sock1.recv()
		#mandamos el numero a los auxiliares.
        sock2.send(num)
        sock3.send(num)
		#recibimos los resultados de los auxiliares.
    	total *= int(sock2.recv())
    	total *= int(sock3.recv())
		#devolvemos el resultado del factorial al cliente.
        sock1.send(str(total))
#ejecuta la funcion server al iniciar el servidor.
if __name__ == '__main__':
    server()