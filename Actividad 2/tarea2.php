<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Formulario Decimal</title>
<link rel="stylesheet" href="styles.css">
</head>
<form method="post" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>">
  <label for="numero_decimal">Número Decimal:</label>
  <input type="text" id="numero_decimal" name="numero_decimal" pattern="[0-9]*[.,]?[0-9]+" title="Por favor ingresa solo números decimales.">
  <input type="submit" value="Enviar">
</form>
<div class="contenedor-resultados">
<?php
  if ($_SERVER["REQUEST_METHOD"] == "POST") {
      $numero_decimal = $_POST['numero_decimal'];
      if (filter_var($numero_decimal, FILTER_VALIDATE_FLOAT) === false) {
          echo "<div class='resultado'><p>Error: Por favor ingresa solo números decimales.</p></div>";
      } else {
          $parte_entera = intval($numero_decimal);
          $parte_fraccionaria = $numero_decimal - $parte_entera;
          echo "<div class='resultado'><p>Parte entera: " . $parte_entera . "</p>";
          echo "<p>Parte fraccionaria: " . $parte_fraccionaria . "</p></div>";
      }
  }
  ?>
</body>
</html>
