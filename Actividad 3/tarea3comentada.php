<!DOCTYPE html>
<!-- La declaración DOCTYPE le dice al navegador qué versión de HTML esperar -->
<html lang="es">
<head>
    <meta charset="UTF-8">
    <!-- El título del documento que aparecerá en la pestaña del navegador -->
    <title>Calculadora Simple</title>
    <!-- Vincula un archivo CSS externo que define el estilo de la página -->
    <link rel="stylesheet" href="style.css">
    <script>
        // Esta función valida los campos del formulario antes de enviarlos
        function validarFormulario() {
            // Obtiene los valores de los campos numéricos
            var num1 = document.forms["calculadora"]["num1"].value;
            var num2 = document.forms["calculadora"]["num2"].value;
            // Verifica si ambos campos están llenos
            if (num1 === "" || num2 === "") {
                alert("Ambos números son requeridos.");
                return false;
            }
            // Verifica si ambos campos son números válidos
            if (isNaN(num1) || isNaN(num2)) {
                alert("Por favor, ingrese solo números válidos.");
                return false;
            }
            // Si todo es correcto, permite que el formulario se envíe
            return true;
        }
    </script>
</head>
<body>
<div class="contenedor">
    <!-- Título de la página visible para el usuario -->
    <h1>Calculadora Simple</h1>
    <!-- El formulario que recoge los números y la operación deseada -->
    <form name="calculadora" action="<?php echo htmlspecialchars($_SERVER['PHP_SELF']); ?>" onsubmit="return validarFormulario()" method="post">
        <!-- Campos para ingresar los números. El atributo 'pattern' asegura que solo se ingresen números válidos -->
        <input type="text" pattern="-?[0-9]*(\.[0-9]+)?" title="Ingrese un número válido, positivo o negativo con o sin decimales." name="num1" required>
        <input type="text" pattern="-?[0-9]*(\.[0-9]+)?" title="Ingrese un número válido, positivo o negativo con o sin decimales." name="num2" required>

        <!-- Un menú desplegable para seleccionar la operación matemática -->
        <select name="operacion">
            <option value="suma">Suma</option>
            <option value="resta">Resta</option>
            <option value="multiplicacion">Multiplicación</option>
            <option value="division">División</option>
        </select>

        <!-- Botón para enviar el formulario -->
        <input type="submit" name="calcular" value="Calcular">
    </form>
</div>
<div id="resultado">
    <?php
    // Este bloque PHP se ejecuta cuando se envía el formulario
    if (isset($_POST['calcular'])) {
        // Filtra y valida los números ingresados como flotantes
        $num1 = filter_input(INPUT_POST, 'num1', FILTER_VALIDATE_FLOAT);
        $num2 = filter_input(INPUT_POST, 'num2', FILTER_VALIDATE_FLOAT);
        // Obtiene la operación seleccionada del formulario
        $operacion = $_POST['operacion'];

        // Verifica si los números son válidos
        if ($num1 === false || $num2 === false) {
            echo "Número(s) inválido(s).";
        } else {
            // Realiza la operación matemática seleccionada
            switch ($operacion) {
                case 'suma':
                    $resultado = $num1 + $num2;
                    break;
                case 'resta':
                    $resultado = $num1 - $num2;
                    break;
                case 'multiplicacion':
                    $resultado = $num1 * $num2;
                    break;
                case 'division':
                    // Verifica que no se divida por cero
                    if ($num2 != 0) {
                        $resultado = $num1 / $num2;
                    } else {
                        $resultado = "No se puede dividir por cero.";
                    }
                    break;
                default:
                    $resultado = "Operación no válida.";
                    break;
            }
            // Muestra el resultado de la operación
            echo "El resultado es: " . htmlspecialchars($resultado) ;
        }
    }
    ?>
</div>
</body>
</html>
