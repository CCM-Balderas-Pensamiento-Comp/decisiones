# IMPORTANT: The length of the lists has to be the same

# List of lists, where each of the inner lists has all the inputs for a single test
input_values = [
    ["10", "20", "30"],
    ["10", "30", "20"],
    ["20", "10", "30"],
    ["20", "30", "10"],
    ["30", "20", "10"],
    ["30", "10", "20"],
    ["-10", "-10", "-10"]
    ]

# List of lists, where each inner list has all the output/prints that end in the terminal
output_values = [
    ["Ingresa el primer número: ", "Ingresa el segundo número: ", "Ingresa el tercer número: ", 10,20,30],
    ["Ingresa el primer número: ", "Ingresa el segundo número: ", "Ingresa el tercer número: ", 10,20,30],
    ["Ingresa el primer número: ", "Ingresa el segundo número: ", "Ingresa el tercer número: ", 10,20,30],
    ["Ingresa el primer número: ", "Ingresa el segundo número: ", "Ingresa el tercer número: ", 10,20,30],
    ["Ingresa el primer número: ", "Ingresa el segundo número: ", "Ingresa el tercer número: ", 10,20,30],
    ["Ingresa el primer número: ", "Ingresa el segundo número: ", "Ingresa el tercer número: ", 10,20,30],
    ["Ingresa el primer número: ", "Ingresa el segundo número: ", "Ingresa el tercer número: ",-10,-10,-10],
    ]

# List of hints for each test, in case of an error
error_messages = [
    ["Revisa todas las posibilidades que tienes al ingresar 3 números"], 
    ["Revisa todas las posibilidades que tienes al ingresar 3 números"],
    ["Revisa todas las posibilidades que tienes al ingresar 3 números"],
    ["Revisa todas las posibilidades que tienes al ingresar 3 números"],
    ["Revisa todas las posibilidades que tienes al ingresar 3 números"],
    ["Revisa todas las posibilidades que tienes al ingresar 3 números"],
    ["Revisa todas las posibilidades que tienes al ingresar 3 números"],
    ]