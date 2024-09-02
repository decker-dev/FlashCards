import random
#para los temas en gral
def temasPreguntados():
    temas = ["Programación", "Inglés", "Química Orgánica", "Estadística", "Química Biológica", "Biología Molecular"]
    indiceAleatorio = random.randit(len(temas))
    temaSugerido = temas[indiceAleatorio]

    return temaSugerido

print("El tema sugerido para practicar es:")


#para las preguntas de cada tema
