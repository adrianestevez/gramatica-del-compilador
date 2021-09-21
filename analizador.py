from pila import Estado, NoTerminal, Pila, Terminal
from regla import Regla

#Símbolos
ERROR = -1;
INICIAL = 55;
IDENTIFICADOR = 0;
ENTERO = 1;
REAL = 2;
CADENA = 3;
TIPO =  4;
OPSUMA = 5;
OPMUL = 6;
OPRELAC = 7;
OPOR = 8;
OPAND = 9;
OPNOT = 10;
OPIGUALDAD = 11;
PUNTOCOMA = 12;
COMA = 13;
ABREPARENTESIS = 14;
CIERRAPARENTESIS = 15;
ABRELLAVE = 16;
CIERRALLAVE = 17;
IGUAL = 18;
IF = 19;
WHILE = 20;
RETURN = 21;
ELSE = 22;
SIGNOPESOS = 23;

class AnalizadorLexico:
    tipoDatos = {"int","float","void"}
    reservadas = {"if","while","return","else"}

    listaErrores = []
    listaTokens = []
    listaSintactico = []
    salidaSintactico = []
    listaReglas = []

    pila = Pila()
    matriz = []

    def __init__(self):
        self.cargarMatriz()
        self.cargarReglas()
        self.cont = 0

    def cargarMatriz(self):
        archivo = open("compilador.lr","r")
        lineas = archivo.readlines()
        #print(lineas)
        for linea in lineas:
            linea = linea.rstrip()
            self.matriz.append(linea.split("\t"))
        
        #convertir matriz
        for i in range(len(self.matriz)):
            for j in range(len(self.matriz[i])):
                self.matriz[i][j] = int(self.matriz[i][j])
        #print(matriz)
        archivo.close()

    def cargarReglas(self):
        archivo = open("reglas.txt","r")
        aux = []
        lineas = archivo.readlines()
        for linea in lineas: 
            linea = linea.rstrip()
            aux.append(linea.split("\t"))

        #convertir datos 
        for regla in aux:
            regla = Regla(int (regla[0]), int (regla[1]), str(regla[2]))
            self.listaReglas.append(regla)
        
        archivo.close()
  
    def agregarToken(self,token,tipo):
        nuevoToken = ""

        if tipo == IDENTIFICADOR:
            nuevoToken = token + " es un identificador" + "\n"
            self.listaTokens.append(nuevoToken)

        elif tipo == ENTERO:
            nuevoToken = token + " es un entero" + "\n"
            self.listaTokens.append(nuevoToken)
        
        elif tipo == REAL:
            nuevoToken = token + " es un real" + "\n"
            self.listaTokens.append(nuevoToken)

        elif tipo == CADENA:
            nuevoToken = token + " es una cadena" + "\n"
            self.listaTokens.append(nuevoToken)
        
        elif tipo == TIPO:
            nuevoToken = token + " es un tipo de dato" + "\n"
            self.listaTokens.append(nuevoToken)
        
        elif tipo == OPSUMA:
            if token == "+":
                nuevoToken = token + " operador suma" + "\n"
                self.listaTokens.append(nuevoToken)
            elif token == "-":
                nuevoToken = token + " operador resta" + "\n"
                self.listaTokens.append(nuevoToken)
        
        elif tipo == OPMUL:
            if token == "*":
                nuevoToken = token + " operador multiplicacion" + "\n"
                self.listaTokens.append(nuevoToken)
            elif token == "/":
                nuevoToken = token + " operador division" + "\n"
                self.listaTokens.append(nuevoToken)
        
        elif tipo == OPRELAC:
            nuevoToken = token + " es un operador relacional" + "\n"
            self.listaTokens.append(nuevoToken)

        elif tipo == OPOR:
            nuevoToken = token + " es un operador or" + "\n"
            self.listaTokens.append(nuevoToken)
        
        elif tipo == OPAND:
            nuevoToken = token + " es un operador and" + "\n"
            self.listaTokens.append(nuevoToken)
        
        elif tipo == OPNOT:
            nuevoToken = token + " es un operador not" + "\n"
            self.listaTokens.append(nuevoToken)
        
        elif tipo == OPIGUALDAD:
            nuevoToken = token + " es un operador igualdad" + "\n"
            self.listaTokens.append(nuevoToken)
        
        elif tipo == PUNTOCOMA:
            nuevoToken = token + " es un punto y coma" + "\n"
            self.listaTokens.append(nuevoToken)
        
        elif tipo == COMA:
            nuevoToken = token + " es una coma" + "\n"
            self.listaTokens.append(nuevoToken)
        
        elif tipo == ABREPARENTESIS:
            nuevoToken = token + " es un parentesis abierto" + "\n"
            self.listaTokens.append(nuevoToken)
        
        elif tipo == CIERRAPARENTESIS:
            nuevoToken = token + " es un parentesis cerrado" + "\n"
            self.listaTokens.append(nuevoToken)
        
        elif tipo == ABRELLAVE:
            nuevoToken = token + " es una llave abierta" + "\n"
            self.listaTokens.append(nuevoToken)
        
        elif tipo == CIERRALLAVE:
            nuevoToken = token + " es una llave cerrada" + "\n"
            self.listaTokens.append(nuevoToken)
        
        elif tipo == IGUAL:
            nuevoToken = token + " es un operador igual" + "\n"
            self.listaTokens.append(nuevoToken)
        
        elif tipo == IF or tipo == WHILE or tipo == ELSE or tipo == RETURN:
            nuevoToken = token + " es una palabra reservada" + "\n"
            self.listaTokens.append(nuevoToken)
        
        elif tipo == SIGNOPESOS:
            nuevoToken = token + " es un signo de $" + "\n"
            self.listaTokens.append(nuevoToken)
        
        else:
            nuevoToken = token + " es un error" + "\n"
            self.listaTokens.append(nuevoToken)
        
    def agregarError(self, error):
        nuevoError = ""
        nuevoError = error + "es un error" + "\n"
        self.listaErrores.append(nuevoError)

    def imprimirSintactico(self):
        for elem in self.listaSintactico:
            print(elem)

    def imprimirSalida(self):
        for elem in self.salidaSintactico:
            print(elem)

    def getListaTokens(self):
        for token in self.listaTokens:
            print(token)

    def getListaPila(self):
        s = ""
        for elementoPila in self.pila.items:
            s = s + str(elementoPila.simbolo) + str(elementoPila.tipo) + " "
        s = s + "\n"
        return s

    def getListaErrores(self):
        s = ""
        for elementoError in self.listaErrores:
            s = s + elementoError + "\n"
        return s
    
    def getListaSintactico(self):
        return self.listaSintactico
    
    def getSalida(self):
        return self.salidaSintactico

    def tipoReservada(self, lexema):
        if lexema == "if":
            return IF
        elif lexema == "while":
            return WHILE
        elif lexema == "return":
            return RETURN
        elif lexema == "else":
            return ELSE
        else:
            return ERROR
        
    def esReservada(self, lexema):
        if lexema == "if":
            return True
        elif lexema == "while":
            return True
        elif lexema == "return":
            return True
        elif lexema == "else":
            return True
        else:
            return False

    def isReal(self, c):
        if (ord(c) >= 48 and ord(c) <= 57):
            return True
        else:
            return False

    def es_Letra(self, c):
        if (((ord(c) >= 65 and ord(c) <= 90) or ord(c) == 95) or ((ord(c)>=97 and ord(c)<=122) or ord(c) == 95)):
            return True
        else:
            return False

    def esTipoDato(self, lexema):
        for tipo in self.tipoDatos:
            if lexema == tipo:
                return True
        return False

    def analizadorSintactico(self, estado, lexema):
        
        if estado == SIGNOPESOS:
            i = (self.matriz[self.cont][estado] * -1)-2

            if i == -1:
                self.salidaSintactico.append("R" + "0")
                return
            else:
                if self.listaReglas[i].numva == 0:
                    num_regla = self.listaReglas[i].num
                    self.cont = self.matriz[self.cont][num_regla]
                    self.pila.push(Terminal(self.cont, self.listaReglas[i].nombre))
                    self.listaSintactico.append(self.getListaPila())
                    self.salidaSintactico.append("R" + str(i+1))
                    self.analizadorSintactico(estado, lexema)
                else:
                    num_regla = self.listaReglas[i].num
                    self.pila.clear()
                    self.pila.push(NoTerminal(0, "$"))
                    self.cont = self.matriz[0][num_regla]
                    self.pila.push(Terminal(self.cont, self.listaReglas[i].nombre))
                    self.listaSintactico.append(self.getListaPila())
                    self.salidaSintactico.append("R" + str(i+1))
                    self.analizadorSintactico(estado, lexema)
        else:
            if self.matriz[self.cont][estado] > 0:
                self.cont = self.matriz[self.cont][estado]
                self.pila.push(NoTerminal(self.cont, lexema))
                self.listaSintactico.append(self.getListaPila())
                self.salidaSintactico.append("D" + str(self.cont))

            elif self.matriz[self.cont][estado] < 0:
                i = (self.matriz[self.cont][estado] * -1) - 1
                num_regla = self.listaReglas[i].num
                self.cont = self.matriz[self.cont][num_regla]
                self.pila.push(NoTerminal(self.cont, self.listaReglas[i].nombre))
                self.listaSintactico.append(self.getListaPila())
                self.salidaSintactico.append("R" + str(i))
                self.analizadorSintactico(estado, lexema)

    def analizador(self, texto):
        #analizareglas
        estado = 0
        lexema = ""
        hayPunto = False
        texto = texto + "$"
        self.pila.push(NoTerminal(0,"$"))
        self.listaSintactico.append(self.getListaPila())

        i = 0
        while i < len(texto):
            caracter = texto[i]
            if estado == INICIAL:
                if self.es_Letra(caracter) or caracter == "_" :
                    estado = IDENTIFICADOR
                    lexema = lexema + caracter
                elif self.isReal(caracter):
                    estado = ENTERO
                    lexema = lexema + caracter
                elif caracter == '"':
                    estado = CADENA
                    lexema = lexema + caracter
                elif caracter == '+' or caracter == '-':
                    lexema = lexema + caracter
                    self.agregarToken(lexema,OPSUMA)
                    self.analizadorSintactico(OPSUMA, lexema)
                    estado = INICIAL
                    lexema = ""
                elif caracter == '*' or caracter == '/':
                    lexema = lexema + caracter
                    self.agregarToken(lexema,OPMUL)
                    self.analizadorSintactico(OPMUL, lexema)
                    estado = INICIAL
                    lexema = ""
                elif caracter == '>' or caracter == '<':
                    estado = OPRELAC
                    lexema = lexema + caracter
                elif caracter == '|':
                    estado = OPOR
                    lexema = lexema + caracter
                elif caracter == '&':
                    estado = OPAND
                    lexema = lexema + caracter
                elif caracter == '=' or caracter == '!':
                    if texto[i+1] != "=":
                        if caracter == '=':
                            lexema = lexema + caracter
                            self.agregarToken(lexema,IGUAL)
                            self.analizadorSintactico(IGUAL, lexema)
                            lexema = ""
                            estado = INICIAL
                        elif caracter == '!':
                            lexema = lexema + caracter
                            self.agregarToken(lexema,OPNOT)
                            self.analizadorSintactico(OPNOT, lexema)
                            lexema = ""
                            estado = INICIAL
                    else:
                        estado = OPIGUALDAD
                        lexema = lexema + caracter
                
                elif caracter == ';':
                    lexema = lexema + caracter
                    self.agregarToken(lexema,PUNTOCOMA)
                    self.analizadorSintactico(PUNTOCOMA, lexema)
                    estado = INICIAL
                    lexema = ""

                elif caracter == ',':
                    lexema = lexema + caracter
                    self.agregarToken(lexema,COMA)
                    self.analizadorSintactico(COMA, lexema)
                    estado = INICIAL
                    lexema = ""
                
                elif caracter == '(':
                    lexema = lexema + caracter
                    self.agregarToken(lexema,ABREPARENTESIS)
                    self.analizadorSintactico(ABREPARENTESIS, lexema)
                    estado = INICIAL
                    lexema = ""
                
                elif caracter == ')':
                    lexema = lexema + caracter
                    self.agregarToken(lexema,CIERRAPARENTESIS)
                    self.analizadorSintactico(CIERRAPARENTESIS, lexema)
                    estado = INICIAL
                    lexema = ""
                
                elif caracter == '{':
                    lexema = lexema + caracter
                    self.agregarToken(lexema,ABRELLAVE)
                    self.analizadorSintactico(ABRELLAVE, lexema)
                    estado = INICIAL
                    lexema = ""
                
                elif caracter == '}':
                    lexema = lexema + caracter
                    self.agregarToken(lexema,CIERRALLAVE)
                    self.analizadorSintactico(CIERRALLAVE, lexema)
                    estado = INICIAL
                    lexema = ""
                
                elif caracter == '$':
                    lexema = lexema + caracter
                    self.agregarToken(lexema,SIGNOPESOS)
                    self.analizadorSintactico(SIGNOPESOS, lexema)
                    estado = INICIAL
                    lexema = ""
            
            elif estado == IDENTIFICADOR:
                if self.es_Letra(caracter) or self.isReal(caracter) or caracter == "_":
                    estado = IDENTIFICADOR
                    lexema = lexema + caracter
                else:
                    if self.esTipoDato(lexema):
                        self.agregarToken(lexema,TIPO)
                        self.analizadorSintactico(TIPO, lexema)
                        estado = INICIAL
                        lexema = ""
                    elif self.esReservada(lexema):
                        self.agregarToken(lexema,self.tipoReservada(lexema))
                        self.analizadorSintactico(self.tipoReservada(lexema), lexema)
                        estado = INICIAL
                        lexema = ""
                    
                    else:
                        self.agregarToken(lexema,IDENTIFICADOR)
                        self.analizadorSintactico(IDENTIFICADOR, lexema)
                        estado = INICIAL
                        lexema = ""
                        i = i - 1
                    
                    
            elif estado == ENTERO:
                if self.isReal(caracter):
                    lexema = lexema + caracter
                    estado = ENTERO
                elif caracter == '.':
                    if hayPunto == False:
                        estado = REAL
                        lexema = lexema + caracter
                        hayPunto = True
                    else:
                        lexema = lexema + caracter
                        self.agregarError(lexema)
                        estado = INICIAL
                        lexema = ""
                else:
                    self.agregarToken(lexema,ENTERO)
                    self.analizadorSintactico(ENTERO, lexema)
                    estado = INICIAL
                    lexema = ""
                    i = i - 1
            
            elif estado == REAL:
                if self.isReal(caracter):
                    lexema = lexema + caracter
                    estado = REAL
                elif caracter == '.':
                    if hayPunto == True:
                        lexema = lexema + caracter
                        self.agregarError(lexema)
                        estado = INICIAL
                        lexema = ""
                else:
                    self.agregarToken(lexema,REAL)
                    self.analizadorSintactico(REAL, lexema)
                    estado = INICIAL
                    lexema = ""
                    i = i - 1
            
            elif estado == CADENA:
                if caracter == '"':
                    lexema = lexema + caracter
                    self.agregarToken(lexema,CADENA)
                    self.analizadorSintactico(CADENA, lexema)
                    estado = INICIAL
                    lexema = ""
                else:
                    lexema = lexema + caracter
                    estado = CADENA

            elif estado == OPRELAC:
                if caracter == '=':
                    lexema = lexema + caracter
                    self.agregarToken(lexema,OPRELAC)
                    self.analizadorSintactico(OPRELAC, lexema)
                    estado = INICIAL
                    lexema = ""
                else:
                    self.agregarToken(lexema,OPRELAC)
                    self.analizadorSintactico(OPRELAC, lexema)
                    estado = INICIAL
                    lexema = ""

            elif estado == OPOR:
                if caracter == '|':
                    lexema = lexema + caracter
                    self.agregarToken(lexema,OPOR)
                    self.analizadorSintactico(OPOR, lexema)
                    estado = INICIAL
                    lexema = ""
                else:
                    self.agregarToken(lexema,OPOR)
                    self.analizadorSintactico(OPOR, lexema)
                    estado = INICIAL
                    lexema = ""
            
            elif estado == OPAND:
                if caracter == '&':
                    lexema = lexema + caracter
                    self.agregarToken(lexema,OPAND)
                    self.analizadorSintactico(OPAND, lexema)
                    estado = INICIAL
                    lexema = ""
                else:
                    self.agregarToken(lexema,OPAND)
                    self.analizadorSintactico(OPAND, lexema)
                    estado = INICIAL
                    lexema = ""
            
            elif estado == OPIGUALDAD:
                lexema = lexema + caracter
                self.agregarToken(lexema,OPIGUALDAD)
                self.analizadorSintactico(OPIGUALDAD, lexema)
                estado = INICIAL
                lexema = ""   
            i += 1
                











