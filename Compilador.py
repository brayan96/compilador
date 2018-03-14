#!/usr/bin/python
# -*- coding: utf-8 -*-

from Pila import *

class Compilador:

    def __init__(self):
        self.pila = Pila()
        self.operadores = ['-','+','*','/']

    def posOrden(self,operacion):
        # Inicializa un nuevo objeto tipo Pila
        self.pila.__init__()
        for i in operacion:
            # Compara con un arreglo de operaciones definido
            if i in self.operadores:
                # Tienen que existir por lo menos dos numeros en la pila para una operación
                if self.pila.get_size() >= 2:
                    a = self.pila.desapilar()
                    b = self.pila.desapilar()
                    if i == '-':
                        self.pila.apilar(b-a)
                    elif i == '+':
                        self.pila.apilar(b+a)
                    elif i == '*':
                        self.pila.apilar(b*a)
                    else:
                        if a != 0:
                            self.pila.apilar(round((b/a),2))
                        else:
                            return "Error - Division por cero"
                else:
                    return "Error - Operacion incompleta faltan operandos o valores"
            # Todo lo que no se una operación lo apila
            # TODO: Faltaria un elif para comparar si es una variable ej: x,y,z
            else:
                try:
                    self.pila.apilar(float(i))
                except ValueError:
                    return "Error - Valor no valido: '" + i + "'"
        # Tiene que existir un unico valor en la pila al finalizar las operaciones
        if self.pila.get_size() == 1:
            return self.pila.desapilar()
        else:
            return "Error - Valores sin evaluar"
