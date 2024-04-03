<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $numero_decimal = $_POST['numero_decimal'];
    if (filter_var($numero_decimal, FILTER_VALIDATE_FLOAT) === false) {
        echo "<p>Error: Por favor ingresa solo números decimales.</p>";
    } else {
        $parte_entera = intval($numero_decimal);
        $parte_fraccionaria = $numero_decimal - $parte_entera;
        echo "<p>Parte entera: " . $parte_entera . "</p>";
        echo "<p>Parte fraccionaria: " . $parte_fraccionaria . "</p>";
    }
}
?>

<!DOCTYPE html>
<html>
<body>

<form method="post" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>">
  Número Decimal: <input type="text" name="numero_decimal" pattern="[0-9]*[.,]?[0-9]+" title="Por favor ingresa solo números decimales.">
  <input type="submit" value="Enviar">
</form>

</body>
</html>
