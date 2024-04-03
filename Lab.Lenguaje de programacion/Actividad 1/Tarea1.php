<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Verificador de Variables</title>
</head>
<body>
    <form method="post">
        <label for="variable">Introduce tu variable:</label>
        <input type="text" id="variable" name="variable">
        <input type="submit" value="Verificar">
    </form>

    <?php
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        // Función optimizada para verificar el tipo de variable ingresada
        function verificarVariable($input) {
            // Elimina espacios en blanco al principio y al final
            $trimmedInput = trim($input);

            // Verifica si el input está vacío
            if (empty($trimmedInput)) {
                return "Por favor, escribe algo para continuar.";
            }

            // Verifica si es numérico (entero o decimal)
            if (is_numeric($trimmedInput)) {
                // Verifica si es un número entero
                if (ctype_digit($trimmedInput)) {
                    return "Has ingresado un número entero.";
                }
                // Si es numérico pero no entero, entonces es decimal
                return "Números decimales no son válidos. Intenta de nuevo.";
            }

            // Verifica si es booleano (true o false)
            if ($trimmedInput === "true" || $trimmedInput === "false") {
                return "Has ingresado un valor booleano.";
            }

            // Verifica si contiene caracteres no alfanuméricos
            if (!ctype_alnum($trimmedInput)) {
                return "Caracteres especiales no son válidos. Intenta de nuevo.";
            }

            // Si pasa todas las verificaciones, asume que es una cadena de caracteres
            return "Has ingresado una cadena de caracteres.";
        }

        // Captura la variable 'variable' del formulario
        $inputUsuario = $_POST['variable'];
        echo verificarVariable($inputUsuario);
    }
    ?>
</body>
</html>
