# IMPORTANT: The length of the lists has to be the same

# List of lists, where each of the inner lists has all the inputs for a single test
input_values = [
    ["2","3","9"],
    ["3", "3", "3"],
    ["2", "3", "2"],
    ["2", "2", "3"],
    ["3", "2", "2"],
    ["2", "3", "4"],
    ["3", "2", "-4"],
    ["0", "3", "4"]
    ]

# List of lists, where each inner list has all the output/prints that end in the terminal
output_values = [
    ["Ingresa la medida del lado 1: ", "Ingresa la medida del lado 2: ", "Ingresa la medida del lado 3: ", "NO ES TRIANGULO"],
    ["Ingresa la medida del lado 1: ", "Ingresa la medida del lado 2: ", "Ingresa la medida del lado 3: ", "ES UN TRIANGULO EQUILATERO"],
    ["Ingresa la medida del lado 1: ", "Ingresa la medida del lado 2: ", "Ingresa la medida del lado 3: ", "ES UN TRIANGULO ISOSCELES"],
    ["Ingresa la medida del lado 1: ", "Ingresa la medida del lado 2: ", "Ingresa la medida del lado 3: ", "ES UN TRIANGULO ISOSCELES"],
    ["Ingresa la medida del lado 1: ", "Ingresa la medida del lado 2: ", "Ingresa la medida del lado 3: ", "ES UN TRIANGULO ISOSCELES"],
    ["Ingresa la medida del lado 1: ", "Ingresa la medida del lado 2: ", "Ingresa la medida del lado 3: ", "ES UN TRIANGULO ESCALENO"],
    ["Ingresa la medida del lado 1: ", "Ingresa la medida del lado 2: ", "Ingresa la medida del lado 3: ", "NO ES TRIANGULO"],
    ["Ingresa la medida del lado 1: ", "Ingresa la medida del lado 2: ", "Ingresa la medida del lado 3: ", "NO ES TRIANGULO"]
    ]

# List of hints for each test, in case of an error
error_messages = [
    ["Revisa todas las opciones en las que se cumple que NO es un triangulo"], 
    ["Revisa todas las opciones en las que se cumple que es un Equilatero"],
    ["Revisa todas las opciones en las que se cumple que es un Isósceles"],
    ["Revisa todas las opciones en las que se cumple que es un Isósceles"],
    ["Revisa todas las opciones en las que se cumple que es un Isósceles"],
    ["Revisa todas las opciones en las que se cumple que es un Escaleno"],
    ["Revisa todas las opciones en las que se cumple que NO es un triangulo"],
    ["Revisa todas las opciones en las que se cumple que NO es un triangulo"]
    ]