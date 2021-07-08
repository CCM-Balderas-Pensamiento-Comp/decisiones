# IMPORTANT: The length of the lists has to be the same

# List of lists, where each of the inner lists has all the inputs for a single test
input_values = [
    ["50", "1.7"],
    ["65", "1.7"],
    ["66", "1.54"],
    ["95", "1.7"],
    ["120", "1.7"],
    ["0", "1.54"],
    ["66", "-2"],
    ]

# List of lists, where each inner list has all the output/prints that end in the terminal
output_values = [
    ["Peso en kg: ", "Altura en m: ", "PESO BAJO"],
    ["Peso en kg: ", "Altura en m: ", "NORMAL"],
    ["Peso en kg: ", "Altura en m: ", "SOBREPESO"],
    ["Peso en kg: ", "Altura en m: ", "OBESIDAD"],
    ["Peso en kg: ", "Altura en m: ", "OBESIDAD MORBIDA"],
    ["Peso en kg: ", "Altura en m: ", "Revisa tus datos, alguno de ellos es erróneo."],
    ["Peso en kg: ", "Altura en m: ", "Revisa tus datos, alguno de ellos es erróneo."],
    ]

# List of hints for each test, in case of an error
error_messages = [
    ["No se cumple con el caso de prueba\nRevisa todos los posibles casos que genera el problema"], 
    ["No se cumple con el caso de prueba\nRevisa todos los posibles casos que genera el problema"],
    ["No se cumple con el caso de prueba\nRevisa todos los posibles casos que genera el problema"],
    ["No se cumple con el caso de prueba\nRevisa todos los posibles casos que genera el problema"],
    ["No se cumple con el caso de prueba\nRevisa todos los posibles casos que genera el problema"],
    ["No se cumple con el caso de prueba\nRevisa todos los posibles casos limite o de error que genera el problema"],
    ["No se cumple con el caso de prueba\nRevisa todos los posibles casos limite o de error que genera el problema"],
    ]