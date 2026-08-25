comentario =input("Porfavor deje su comentario sobre el servicio: ").lower()
positivas = ["ama", "gusta", "genial", "excelente", "bueno", "maravilloso", "perfecto", "increible", "feliz", "contento", "satisfecho"]
negativas = ["odia", "malo", "terrible", "decepcionante", "pésimo", "pesimo" , "horrible", "insatisfecho", "frustrante", "triste", "enojado"]

buena = 0
mala = 0

for palabra in comentario.split():
    if palabra in positivas:
        buena +=1
    else:
        if palabra in negativas:
            mala +=1

if buena > mala:
    print("El comentario es positivo")
elif buena < mala:
    print("El comentario es negativo")
else:
    print("El comentario es neutral")
