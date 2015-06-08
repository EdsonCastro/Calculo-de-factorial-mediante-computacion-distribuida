#!/usr/bin/python2

import zmq

def auxserv():
    #Prepara el socket para recibir datos del servidor.
    context = zmq.Context(5)
    sock = context.socket(zmq.REP)
    #Levanta el servidor auxiliar.
    sock.bind('tcp://*:4547')
	
    print "auxiliar 2 preparado ..."	
    #Cuerpo principal del servidor auxiliar que recibe las peticiones.	
    while True:
        #Recibe el numero desde el servidor.
        num = int(sock.recv())
        #Calcula el limite inferior.
        rango = (num/2)+1	
        print "calculando..."
        #Resultado parcial con el caso base del producto.
        totalparcial=1
        #Bucle que calcula el factorial parcial.
        for i in range(rango,num+1):
            totalparcial*=i
        #Devuelve el calculo parcial al servidor.
        sock.send(str(totalparcial))
#Ejecuta la funcion auxserv al iniciar el auxiliar.	
if __name__ == '__main__':
    auxserv()