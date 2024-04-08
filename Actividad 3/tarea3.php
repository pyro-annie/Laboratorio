<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Calculadora Simple</title>
    <link rel="stylesheet" href="style.css">
    <script>
        function validarFormulario() {
            var num1 = document.forms["calculadora"]["num1"].value;
            var num2 = document.forms["calculadora"]["num2"].value;
            if (num1 === "" || num2 === "") {
                alert("Ambos números son requeridos.");
                return false;
            }
            if (isNaN(num1) || isNaN(num2)) {
                alert("Por favor, ingrese solo números válidos.");
                return false;
            }
            return true;
        }
    </script>
</head>
<body>
<div class="contenedor">
<h1>Calculadora Simple</h1>
    <form name="calculadora" action="<?php echo htmlspecialchars($_SERVER['PHP_SELF']); ?>" onsubmit="return validarFormulario()" method="post">
        <input type="text" pattern="-?[0-9]*(\.[0-9]+)?" title="Ingrese un número válido, positivo o negativo con o sin decimales." name="num1" required>
        <input type="text" pattern="-?[0-9]*(\.[0-9]+)?" title="Ingrese un número válido, positivo o negativo con o sin decimales." name="num2" required>

        <select name="operacion">
            <option value="suma">Suma</option>
            <option value="resta">Resta</option>
            <option value="multiplicacion">Multiplicación</option>
            <option value="division">División</option>
        </select>

        <input type="submit" name="calcular" value="Calcular">
    </form>
    </div>
    <div id="resultado">
    <?php
    if (isset($_POST['calcular'])) {
        $num1 = filter_input(INPUT_POST, 'num1', FILTER_VALIDATE_FLOAT);
        $num2 = filter_input(INPUT_POST, 'num2', FILTER_VALIDATE_FLOAT);
        $operacion = $_POST['operacion'];

        if ($num1 === false || $num2 === false) {
            echo "Número(s) inválido(s).";
        } else {
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
            echo "<div >El resultado es: " . htmlspecialchars($resultado) . "</div>";
        }
    }
    ?>
        </div>
</body>
</html>

