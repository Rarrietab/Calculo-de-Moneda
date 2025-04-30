# Paso 1: Definir el valor actual del Euro y Dolar con respecto al Peso Mexicano

tipo_cambio_eur_a_mxn = 22.34
tipo_cambio_usd_a_mxn = 19.60

# Paso 2: Solicitar al usuario el tipo de conversión (Euro a Mex o Dólar a Mex)
tipo_conversion = input("Ingrese la monedad de origen para realizar la conversión (EUR/USD): ").upper() 

# Paso 3: Solicitar al usuario el monto a convertir
monto_a_convertir = float(input("Ingrese el monto a convertir: "))

# Paso 4: Realizar la conversión utilizando el tipo de cambio correspondiente
# Paso 5: Mostrar el reusltado de la conversión al usuario
    
if tipo_conversion == "EUR":
    resultado = monto_a_convertir * tipo_cambio_eur_a_mxn
    print("El resultado de la conversión de EUR a MXN es:", resultado)
elif tipo_conversion == "USD":
    resultado = monto_a_convertir * tipo_cambio_usd_a_mxn
    print("El resultado de la conversión de USD a MXN es:", resultado)
else:
    print("Tipo de conversión no válido. Por favor, ingrese 'EUR' o 'USD'.")
# Paso 6: Preguntar al usuario si desea realizar otra conversión
otra_conversion = input("¿Desea realizar otra conversión? (S/N): ").upper()
while otra_conversion == "S":
    tipo_conversion = input("Ingrese la moneda de origen para realizar la conversión (EUR/USD): ").upper() 
    monto_a_convertir = float(input("Ingrese el monto a convertir: "))

    if tipo_conversion == "EUR":
        resultado = monto_a_convertir * tipo_cambio_eur_a_mxn
        print("El resultado de la conversión de EUR a MXN es:", resultado)
    elif tipo_conversion == "USD":
        resultado = monto_a_convertir * tipo_cambio_usd_a_mxn
        print("El resultado de la conversión de USD a MXN es:", resultado)
    else:
        print("Tipo de conversión no válido. Por favor, ingrese 'EUR' o 'USD'.")
    
    otra_conversion = input("¿Desea realizar otra conversión? (S/N): ").upper()

