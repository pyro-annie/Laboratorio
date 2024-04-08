<!DOCTYPE html>
<!-- El tipo de documento, necesario para que los navegadores interpreten correctamente el HTML5 -->
<html lang="es">
<head>
  <meta charset="UTF-8">
  <!-- Define la codificación de caracteres para el documento HTML -->
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <!-- Asegura una correcta visualización y un diseño responsivo en dispositivos móviles -->
  <title>Formulario Decimal</title>
  <!-- Título del documento, se muestra en la pestaña del navegador -->
  <link rel="stylesheet" href="styles.css">
  <!-- Vincula una hoja de estilos CSS externa para dar formato al documento -->
</head>
<body>
  <!-- Contenido principal del documento HTML -->
  <form method="post" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>">
    <!-- Formulario para enviar datos al servidor con el método POST -->
    <label for="numero_decimal">Número Decimal:</label>
    <!-- Etiqueta para el campo de entrada de número decimal -->
    <input type="text" id="numero_decimal" name="numero_decimal" pattern="[0-9]*[.,]?[0-9]+" title="Por favor ingresa solo números decimales.">
    <!-- Campo de entrada para el número decimal con una validación de patrón -->
    <input type="submit" value="Enviar">
    <!-- Botón para enviar el formulario -->
  </form>
  <div class="contenedor-resultados">
    <!-- Contenedor para mostrar los resultados del procesamiento del formulario -->
    <?php
      if ($_SERVER["REQUEST_METHOD"] == "POST") {
          // Verifica si el formulario ha sido enviado usando el método POST
          $numero_decimal = $_POST['numero_decimal'];
          // Almacena el número decimal enviado desde el formulario
          if (filter_var($numero_decimal, FILTER_VALIDATE_FLOAT) === false) {
              // Valida si el número decimal es válido
              echo "<div class='resultado'><p>Error: Por favor ingresa solo números decimales.</p></div>";
              // Muestra un mensaje de error si el número no es válido
          } else {
              // Si el número es válido, procede a separar la parte entera de la fraccionaria
              $parte_entera = intval($numero_decimal);
              // Obtiene la parte entera del número
              $parte_fraccionaria = $numero_decimal - $parte_entera;
              // Calcula la parte fraccionaria restando la parte entera del número total
              echo "<div class='resultado'><p>Parte entera: " . $parte_entera . "</p>";
              // Muestra la parte entera del número
              echo "<p>Parte fraccionaria: " . $parte_fraccionaria . "</p></div>";
              // Muestra la parte fraccionaria del número
          }
      }
    ?>
  </div>
</body>
</html>
