# IMPORTANT: The length of the lists has to be the same

# List of lists, where each of the inner lists has all the inputs for a single test
input_values = [
    ["2015", "2", "13"],
    ["2015", "2", "28"],
    ["2020", "2", "28"],
    ["2021", "12", "31"],
    ["2019", "4", "30"]
    ]

# List of lists, where each inner list has all the output/prints that end in the terminal
output_values = [
    ["Año: ", "Mes: ", "Día: ", 2015, 2, 14],
    ["Año: ", "Mes: ", "Día: ", 2015, 3, 1],
    ["Año: ", "Mes: ", "Día: ", 2020, 2, 29],
    ["Año: ", "Mes: ", "Día: ", 2022, 1, 1],
    ["Año: ", "Mes: ", "Día: ", 2019, 5, 1]
    ]

# List of hints for each test, in case of an error
error_messages = [
    ["Revisa qué pasa en un día siguiente sin problemas de fin de mes"], 
    ["Revisa qué debe pasar en el mes 2 que no es bisiesto después del día 28"],
    ["Revisa qué debe pasar en el mes 2 que es bisiesto después del día 28"],
    ["Revisa qué debe pasar si el día que te dan es el último del año"],
    ["Revisa qué debe pasar si te dan el último día de un mes de 30 días"]
    ]