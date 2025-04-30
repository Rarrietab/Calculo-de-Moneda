----------------------------------------
Problemática:
"La empresa mexicana SuperTech está perdiendo dinero porque en las transacciones desde moneda internacional 
hay muchos errores del personal al realizar cálculos a mano para pasar de Euro a Peso Mexicano y Dólar a 
Peso Mexicano en los pagos de importaciones”
----------------------------------------

----------------------------------------
Algoritmo:
1. Definir el valor actual del Euro y Dolar con respecto al Peso Mexicano
2. Solicitar al usuario el tipo de conversión (Euro a Mxn o Dólar a Mxn)
3. Solicitar al usuario el monto a convertir
4. Realizar la conversión utilizando el tipo de cambio correspondiente
5. Mostrar el reusltado de la conversión al usuario
----------------------------------------

----------------------------------------
Pseudocódigo:

Inicio 

    # Paso 1: Definir el valor actual del Euro y Dolar con respecto al Peso Mexicano
    Definir tipo_cambio_eur_a_mxn = 22.34
    Definir tipo_cambio_usd_a_mxn = 19.60

    # Paso 2: Solicitar al usuario el tipo de conversión (Euro a Mex o Dólar a Mex)
    Mostrar mensaje: "Ingrese la moneda origen para la conversión (EUR/USD): "

    # Paso 3: Solicitar al usuario el monto a convertir
    Mostrar mensaje: "Ingrese el monto a convertir: "

    # Paso 4: Realizar la conversión utilizando el tipo de cambio correspondiente
    # Paso 5: Mostrar el reusltado de la conversión al usuario
    
    Si tipo_conversion == "EUR":
        Calcular resultado = monto_a_convertir * tipo_cambio_eur_a_mxn
        Mostrar "El resultado de la conversión de EUR a MXN es:", resultado
    Sino si tipo_conversion == "USD":
        Calcular resultado = monto_a_convertir * tipo_cambio_usd_a_mxn
        Mostrar "El resultado de la conversión de USD a MXN es:", resultado
    Sino
        Mostrar: "No está disponible este tipo de conversión actualmente"
    
    # Paso 6: Pedimos al usuario si desea realizar otra conversión

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

Fin
