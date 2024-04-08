<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Verificador de Variables</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <form method="post">
        <label for="variable">Introduce tu variable:</label>
        <input type="text" id="variable" name="variable">
        <input type="submit" value="Verificar">
        <div id="mensaje" class="mensaje" style="display: none;"></div>
    </form>
    
    <?php
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        function verificarVariable($input) {
            $trimmedInput = trim($input);
            $resultado = "Has ingresado una cadena de caracteres.";
            if (empty($trimmedInput)) {
                $resultado = "Por favor, escribe algo para continuar.";
            } elseif (preg_match('/[a-z]/i', $trimmedInput) && preg_match('/\d/', $trimmedInput)) {
                $resultado = "La entrada no debe contener una mezcla de letras y números.";
            } elseif (is_numeric($trimmedInput)) {
                if (strpos($trimmedInput, '.') !== false) {
                    $resultado = "Números decimales no son válidos. Intenta de nuevo.";
                } else {
                    $resultado = "Has ingresado un número entero.";
                }
            } elseif ($trimmedInput === "true" || $trimmedInput === "false") {
                $resultado = "Has ingresado un valor booleano.";
            } elseif (!ctype_alnum($trimmedInput)) {
                $resultado = "Caracteres especiales no son válidos. Intenta de nuevo.";
            }
            return $resultado;
        }
        $mensaje = verificarVariable($_POST['variable']);
    ?>
    <div class="mensaje <?php echo (strpos($mensaje, 'Has ingresado') !== false) ? 'confirmacion' : 'error'; ?>">
        <?php echo $mensaje; ?>
    </div>
    <?php } ?>
</body>
</html>