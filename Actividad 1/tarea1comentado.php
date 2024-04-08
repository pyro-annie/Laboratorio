<!DOCTYPE html> <!-- Define que el documento es HTML5 -->
<html lang="es"> <!-- Establece el idioma del documento como español -->
<head>
    <meta charset="UTF-8"> <!-- Define la codificación de caracteres para el documento -->
    <title>Verificador de Variables</title> <!-- Título del documento que aparece en la pestaña del navegador -->
    <link rel="stylesheet" href="styles.css"> <!-- Vincula una hoja de estilos CSS externa para el diseño del documento -->
</head>
<body>
    <!-- Formulario para la entrada de datos por parte del usuario -->
    <form method="post">
        <!-- Etiqueta para el campo de entrada de la variable -->
        <label for="variable">Introduce tu variable:</label>
        <!-- Campo de entrada para que el usuario escriba su variable -->
        <input type="text" id="variable" name="variable">
        <!-- Botón para enviar el formulario -->
        <input type="submit" value="Verificar">
        <!-- División para mostrar mensajes, oculta por defecto -->
        <div id="mensaje" class="mensaje" style="display: none;"></div>
    </form>
    
    <!-- Código PHP para procesar la entrada del formulario -->
    <?php
    // Verifica si el formulario ha sido enviado usando el método POST
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        // Función para verificar la variable ingresada por el usuario
        function verificarVariable($input) {
            // Elimina espacios en blanco al inicio y al final de la entrada
            $trimmedInput = trim($input);
            // Mensaje predeterminado
            $resultado = "Has ingresado una cadena de caracteres.";
            // Verifica si la entrada está vacía
            if (empty($trimmedInput)) {
                $resultado = "Por favor, escribe algo para continuar.";
            // Verifica si la entrada contiene letras y números
            } elseif (preg_match('/[a-z]/i', $trimmedInput) && preg_match('/\d/', $trimmedInput)) {
                $resultado = "La entrada no debe contener una mezcla de letras y números.";
            // Verifica si la entrada es numérica
            } elseif (is_numeric($trimmedInput)) {
                // Verifica si la entrada es un número decimal
                if (strpos($trimmedInput, '.') !== false) {
                    $resultado = "Números decimales no son válidos. Intenta de nuevo.";
                } else {
                    // La entrada es un número entero
                    $resultado = "Has ingresado un número entero.";
                }
            // Verifica si la entrada es un valor booleano
            } elseif ($trimmedInput === "true" || $trimmedInput === "false") {
                $resultado = "Has ingresado un valor booleano.";
            // Verifica si la entrada contiene caracteres especiales
            } elseif (!ctype_alnum($trimmedInput)) {
                $resultado = "Caracteres especiales no son válidos. Intenta de nuevo.";
            }
            // Devuelve el mensaje resultante
            return $resultado;
        }
        // Llama a la función verificarVariable y almacena el mensaje resultante
        $mensaje = verificarVariable($_POST['variable']);
    ?>
    <!-- Muestra el mensaje resultante en una división con clases para estilos de confirmación o error -->
    <div class="mensaje <?php echo (strpos($mensaje, 'Has ingresado') !== false) ? 'confirmacion' : 'error'; ?>">
        <?php echo $mensaje; ?>
    </div>
    <?php } ?>
</body>
</html>
