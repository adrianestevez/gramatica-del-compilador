import analizador

texto = input("Ingrese el texto a analizar: ")

analizador = analizador.AnalizadorLexico()
analizador.analizador(texto)
analizador.getListaTokens()
print("Salida")
analizador.imprimirSalida()
print("\nPila")
analizador.imprimirSintactico()

