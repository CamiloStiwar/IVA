#paso1: Pedir el total de la factura
totalFactura = int(input("Por favor digite el total de la factura: "))
#paso2: Pedir el porcentaje de propina que se quiere entregar
totalPropina = int(input("Por favor dijite el porcentaje de propina que desea entregar: "))
#paso3: Calcular el valor del IVA del 19%
totalIVA = int(totalFactura * 0.19)
#Paso4: Calcular el subtotal (total de la factura - valor del iva)
totalSubTotal = int(totalFactura - totalIVA)
#paso5: Calcular el valor de la propina (subtotal * propina/100)
valorPropina = int(totalSubTotal * totalPropina /100)
totalDeCuenta = int(valorPropina + totalSubTotal + totalIVA)
#paso6: Mostrar el resultado
print(f"El valor total del iba cobrado es {totalIVA} pesos")
print(f"El subtotal es {totalSubTotal} pesos")
print(f"El valor de la propina es {valorPropina} pesos")
print(f"El valor total de la factura con propina incluida es {totalDeCuenta} pesos")