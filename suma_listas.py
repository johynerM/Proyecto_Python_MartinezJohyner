primera = [1,3,5,7,9]
segunda = [2,4,6,8,10]

if len(primera) ==len(segunda):
    resultado_suma = []
    for i in range(len(primera)):
        resultado_suma = primera[i] + segunda[i]
        print("la suma de los elementos en la posicion", i, "es:", resultado_suma)
else:
    print("las listas no tienen la misma longitud")