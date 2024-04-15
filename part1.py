# Concatenar cadenas de caracteres 
# SUpongamos que queremos crear una cadena que diga :
# Variable es simplemente algo que le asignamos un nombre 
# Una buena economia es una buena 

#organizacion = "Politica"

#en python usamops print para mostrar un mensaje 

#print("Una buena economia es una buena " + organizacion)
#print("Una buena economia es una buena {}".format(organizacion))      #Por el metodo format()
#print(f"una buena economia es una buena {organizacion}")                                                            #f-string


#MaD Libs (historias Locas)

adj = input("adjetivo: ")
verbo1 = input("verbo1: ")
verbo2 = input("verbo2: ")
sustantivo_plural = input("sustantivo_plural: ")

madlib = f"¡Programar es tan {adj}!\nSiempre me emociona porque me encanta {verbo1} problemas.\nAprende a {verbo2} con free code camp y alcanza tus {sustantivo_plural}"
print(madlib)
