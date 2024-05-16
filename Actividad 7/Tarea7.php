<?php
// Definición de la clase MiClase
class MiClase {
    public $atributo1;
    // ... otros atributos ...

    public function __construct($var1, /* ... */) {
        $this->atributo1 = $var1;
        // ... inicialización de otros atributos ...
    }

    // Métodos para obtener y cambiar atributos
    public function obtenerAtributo1() {
        return $this->atributo1;
    }

    public function cambiarAtributo1($nuevoValor) {
        $this->atributo1 = $nuevoValor;
    }
}

// Procesamiento del formulario
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Crear una instancia de MiClase con los valores del formulario
    $objeto = new MiClase($_POST['var1'], /* ... otros valores ... */);
    // ... más código para procesar la instancia ...
}
?>
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Formulario con PHP</title>
</head>
<body>
<!-- El formulario HTML para ingresar los valores -->
<form method="post" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>">
    Variable 1: <input type="text" name="var1"><br>
    <!-- Campos para las otras 14 variables -->
    <input type="submit" value="Enviar">
</form>

</body>
</html>
