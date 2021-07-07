# IMPORTANT: The length of the lists has to be the same

# List of lists, where each of the inner lists has all the inputs for a single test
input_values = [
    ["19", "n"],
    ["20", "s"],
    ["18", "r"],
    ["0"],
    ["12"]
    ]

# List of lists, where each inner list has all the output/prints that end in the terminal
output_values = [
    ["Ingresa tu edad: ","¿Tienes identificación oficial? (s/n): ", "No cumples requisitos" ],
    ["Ingresa tu edad: ","¿Tienes identificación oficial? (s/n): ", "Trámite de licencia concedido"],
    ["Ingresa tu edad: ","¿Tienes identificación oficial? (s/n): ", "Respuesta incorrecta"],
    ["Ingresa tu edad: ", "Respuesta incorrecta"],
    ["Ingresa tu edad: ", "No cumples requisitos"]
    ]

# List of hints for each test, in case of an error
error_messages = [
    ["Revisa que pasa si cumples edad, pero no con credencial"], 
    ["Revisa qué debe pasar si cumples con los dos requisitos"],
    ["Revisa qué debes pasar si tecleas de manera incorrecta la respuesta de s/n"],
    ["Revisa qué debe pasar si te mandan un dato inválido para la edad"],
    ["Revisa qué deb pasar si es un menor de edad"]
    ]