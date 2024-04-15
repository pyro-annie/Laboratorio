<?php
// Inicio del código PHP.

// Definición de la clase 'Figura', que representa una figura geométrica.
class Figura {
    // Propiedades de la clase que definen las características de la figura.
    public $tipo;       // Tipo de figura (cuadrado, círculo, triángulo).
    public $posicionX;  // Posición horizontal inicial de la figura en la pantalla.
    public $posicionY;  // Posición vertical inicial de la figura en la pantalla.
    public $color;      // Color inicial de la figura.
    public $nombre;     // Nombre asignado a la figura para identificarla.

    // Constructor de la clase que se ejecuta al crear un objeto 'Figura'.
    // Inicializa las propiedades del objeto con los valores proporcionados.
    public function __construct($tipo, $posicionX, $posicionY, $color, $nombre) {
        $this->tipo = $tipo;
        $this->posicionX = $posicionX;
        $this->posicionY = $posicionY;
        $this->color = $color;
        $this->nombre = $nombre;
    }
}

// Creación de un arreglo asociativo llamado 'figuras'.
// Este arreglo contiene objetos 'Figura' con valores predefinidos.
$figuras = [
    "figura1" => new Figura("cuadrado", 50, 400, "red", "Figura 1"),
    "figura2" => new Figura("circulo", 200, 400, "blue", "Figura 2"),
    "figura3" => new Figura("triangulo", 350, 400, "green", "Figura 3")
];
?>
<!-- Aquí comienza el código HTML que define la estructura de la página web. -->
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <!-- Título de la página web visible en la pestaña del navegador. -->
    <title>Ventana Interactiva con PHP y Objetos Múltiples</title>
    <!-- Enlace al archivo de estilos CSS que define la apariencia de la página. -->
    <link rel="stylesheet" href="styles.css">
    <!-- Inclusión de bibliotecas jQuery y jQuery UI para funcionalidades interactivas. -->
    <script src="https://code.jquery.com/jquery-3.5.1.min.js"></script>
    <script src="https://code.jquery.com/ui/1.12.1/jquery-ui.min.js"></script>
    <script>
    // Código JavaScript que utiliza jQuery para añadir interactividad a la página.
    $(function() {
        // Hacemos que los elementos con la clase 'draggable' sean arrastrables.
        $(".draggable").draggable({
            // Función que se ejecuta al detener el arrastre de una figura.
            stop: function() {
                // Obtenemos la posición final de la figura y la mostramos en consola.
                var finalPosition = $(this).position();
                console.log("Posición X: " + finalPosition.left + ", Posición Y: " + finalPosition.top);
                // Aquí se podría enviar la posición final al servidor con AJAX si fuera necesario.
            }
        });

        // Evento que detecta cambios en los selectores de forma de las figuras.
        $(".formaFigura").change(function() {
        var figuraSeleccionada = $(this).val();
        var idFigura = $(this).data('figura');
        var figuraElement = $("#" + idFigura);

        // Removemos las clases de todas las formas y añadimos la seleccionada.
        figuraElement.removeClass("cuadrado circulo triangulo").addClass(figuraSeleccionada);

        // Restablecemos los estilos CSS predeterminados antes de aplicar los nuevos.
        figuraElement.css({
            "background-color": "", // Limpia el color de fondo para cuadrados y círculos.
            "border-bottom-color": "" // Limpia el color del borde para triángulos.
        });

        // Aplicamos el color actualmente seleccionado para la figura.
        var colorActual = figuraElement.data('colorActual');
        if (figuraSeleccionada === 'triangulo') {
            figuraElement.css("border-bottom-color", colorActual);
        } else {
            figuraElement.css("background-color", colorActual);
        }

        // Actualizamos el color actual en el elemento de datos.
        figuraElement.data('colorActual', colorActual);
    });

        // Evento que detecta cambios en los selectores de color de las figuras.
        $(".colorFigura").change(function() {
            // Obtenemos el color seleccionado y el ID de la figura afectada.
            var colorSeleccionado = $(this).val();
            var idFigura = $(this).data('figura');
            var figuraElement = $("#" + idFigura);
            // Guardamos el color seleccionado como el color actual de la figura.
        figuraElement.data('colorActual', colorSeleccionado);
                // Aplicamos el color seleccionado dependiendo del tipo de figura.
            if (figuraElement.hasClass('triangulo')) {
            figuraElement.css("border-bottom-color", colorSeleccionado);
        } else {
            figuraElement.css("background-color", colorSeleccionado);
        }
            // Cambiamos el color de la figura según su tipo (borde o fondo).
            if ($("#" + idFigura).hasClass('triangulo')) {
                $("#" + idFigura).css("border-bottom-color", colorSeleccionado);
            } else {
                $("#" + idFigura).css("background-color", colorSeleccionado);
            }
            // Ajustamos el color del texto para mejorar la visibilidad según el color de fondo.
            var luminance = getLuminance(colorSeleccionado);
            if (luminance < 0.5 && !$("#" + idFigura).hasClass('triangulo')) {
                $("#" + idFigura + " span").css("color", "white");
            } else {
                $("#" + idFigura + " span").css("color", "black");
            }
        });

        // Evento que detecta cambios en los campos de texto para el nombre de las figuras.
        $(".nombreFigura").change(function() {
            // Obtenemos el nombre ingresado y el ID de la figura afectada.
            var nombreSeleccionado = $(this).val();
            var idFigura = $(this).data('figura');
            // Actualizamos el nombre visualizado en la figura.
            $("#" + idFigura + " span").text(nombreSeleccionado);
        });
        // Función para calcular la luminancia de un color y determinar si es claro u oscuro.
        function getLuminance(color) {
            var rgb = hexToRgb(color);
            return (0.2126 * rgb.r + 0.7152 * rgb.g + 0.0722 * rgb.b) / 255;
        }

        // Función para convertir un color en formato hexadecimal a su representación RGB.
        function hexToRgb(hex) {
            var shorthandRegex = /^#?([a-f\\d])([a-f\\d])([a-f\\d])$/i;
            hex = hex.replace(shorthandRegex, function(m, r, g, b) {
                return r + r + g + g + b + b;
            });
            var result = /^#?([a-f\\d]{2})([a-f\\d]{2})([a-f\\d]{2})$/i.exec(hex);
            return result ? {
                r: parseInt(result[1], 16),
                g: parseInt(result[2], 16),
                b: parseInt(result[3], 16)
            } : null;
        }
    });
    </script>
</head>
<body>
    <!-- PHP incrustado en HTML para mostrar las figuras en la página. -->
    <?php foreach ($figuras as $key => $figura): ?>
        <!-- Div que representa una figura, con estilos y clases que definen su apariencia y comportamiento. -->
        <div id="<?= $key; ?>" class="draggable <?= $figura->tipo; ?>" style="top: <?= $figura->posicionY; ?>px; left: <?= $figura->posicionX; ?>px;">
            <!-- Nombre de la figura mostrado dentro de cada div. -->
            <span class="nombreFigura"><?= $figura->nombre; ?></span>
        </div>
    <?php endforeach; ?>
    <!-- Formulario HTML para cambiar las propiedades de las figuras. -->
    <form class="propiedad">
    <?php foreach ($figuras as $key => $figura): ?>
        <!-- Fieldset que agrupa los controles para una figura específica. -->
        <fieldset>
            <legend>Propiedades de <?= $figura->nombre; ?></legend>
            <!-- Selector de forma con opciones para cambiar la forma de la figura. -->
            <label for="forma<?= ucfirst($key); ?>">Forma:</label>
            <select id="forma<?= ucfirst($key); ?>" class="formaFigura" data-figura="<?= $key; ?>">
                <option value="cuadrado" <?= $figura->tipo == 'cuadrado' ? 'selected' : ''; ?>>Cuadrado</option>
                <option value="circulo" <?= $figura->tipo == 'circulo' ? 'selected' : ''; ?>>Círculo</option>
                <option value="triangulo" <?= $figura->tipo == 'triangulo' ? 'selected' : ''; ?>>Triángulo</option>
            </select>
            <!-- Selector de color para cambiar el color de la figura. -->
            <input type="color" class="colorFigura" data-figura="<?= $key; ?>" value="<?= $figura->color; ?>">
            <!-- Campo de texto para cambiar el nombre de la figura. -->
            <input type="text" class="nombreFigura" data-figura="<?= $key; ?>" value="<?= $figura->nombre; ?>">
        </fieldset>
        <br>
    <?php endforeach; ?>
    </form>
</body>
</html>
