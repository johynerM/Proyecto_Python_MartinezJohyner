while True:
   proteina = float(input("ingrese la cantidad en gramos de proteina de la receta: "))
   carbohidratos = float(input("ingrese la cantidad en gramos de carbohidratos de la receta: "))
   grasa = float(input("ingrese la cantidad en gramos de grasa de la receta: "))
   
   calorias_proteina = proteina * 4
   calorias_carbohidratos = carbohidratos * 4
   calorias_grasa = grasa * 9
   total_calorias = calorias_proteina + calorias_carbohidratos + calorias_grasa
   print("El total de calorías de la receta es: ", total_calorias)
        

