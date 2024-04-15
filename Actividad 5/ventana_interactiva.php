<?php
class Figura {
    public $tipo;
    public $posicionX;
    public $posicionY;
    public $color;
    public $nombre;

    public function __construct($tipo, $posicionX, $posicionY, $color, $nombre) {
        $this->tipo = $tipo;
        $this->posicionX = $posicionX;
        $this->posicionY = $posicionY;
        $this->color = $color;
        $this->nombre = $nombre;
    }
}


$figuras = [
    "figura1" => new Figura("cuadrado", 50, 400, "red", "Figura 1"),
    "figura2" => new Figura("circulo", 200, 400, "blue", "Figura 2"),
    "figura3" => new Figura("triangulo", 350, 400, "green", "Figura 3")
];
?>
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Ventana Interactiva con PHP y Objetos Múltiples</title>          
    <link rel="stylesheet" href="styles.css">
    <script src="https://code.jquery.com/jquery-3.5.1.min.js"></script>
    <script src="https://code.jquery.com/ui/1.12.1/jquery-ui.min.js"></script>
<script>
    $(function() {

        $(".draggable").draggable({
            stop: function() {
                var finalPosition = $(this).position();
                console.log("Posición X: " + finalPosition.left + ", Posición Y: " + finalPosition.top);

            }
        });

        $(".formaFigura").change(function() {
            var figuraSeleccionada = $(this).val();
            var idFigura = $(this).data('figura');
            $("#" + idFigura).removeClass("cuadrado circulo triangulo").addClass(figuraSeleccionada);
        });

        $(".colorFigura").change(function() {
            var colorSeleccionado = $(this).val();
            var idFigura = $(this).data('figura');
            if ($("#" + idFigura).hasClass('triangulo')) {
                $("#" + idFigura).css("border-bottom-color", colorSeleccionado); 
            } else {
                $("#" + idFigura).css("background-color", colorSeleccionado); 
                var luminance = getLuminance(colorSeleccionado);
                if (luminance < 0.5 && !$("#" + idFigura).hasClass('triangulo')) {
                    $("#" + idFigura + " span").css("color", "white");
                } else {
                    $("#" + idFigura + " span").css("color", "black");
                }
            }
        });

        $(".nombreFigura").change(function() {
            var nombreSeleccionado = $(this).val();
            var idFigura = $(this).data('figura');
            $("#" + idFigura + " span").text(nombreSeleccionado);
        });

        function getLuminance(color) {
            var rgb = hexToRgb(color);
            return (0.2126 * rgb.r + 0.7152 * rgb.g + 0.0722 * rgb.b) / 255;
        }

        function hexToRgb(hex) {
            var shorthandRegex = /^#?([a-f\d])([a-f\d])([a-f\d])$/i;
            hex = hex.replace(shorthandRegex, function(m, r, g, b) {
                return r + r + g + g + b + b;
            });
            var result = /^#?([a-f\d]{2})([a-f\d]{2})([a-f\d]{2})$/i.exec(hex);
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
    <?php foreach ($figuras as $key => $figura): ?>
        <div id="<?= $key; ?>" class="draggable <?= $figura->tipo; ?>" style="top: <?= $figura->posicionY; ?>px; left: <?= $figura->posicionX; ?>px;">
            <span class="nombreFigura"><?= $figura->nombre; ?></span>
        </div>
    <?php endforeach; ?>
    <form class="propiedad">
    <?php foreach ($figuras as $key => $figura): ?>
        <fieldset>
            <legend>Propiedades de <?= $figura->nombre; ?></legend>
            <label for="forma<?= ucfirst($key); ?>">Forma:</label>
            <select id="forma<?= ucfirst($key); ?>" class="formaFigura" data-figura="<?= $key; ?>">
                <option value="cuadrado" <?= $figura->tipo == 'cuadrado' ? 'selected' : ''; ?>>Cuadrado</option>
                <option value="circulo" <?= $figura->tipo == 'circulo' ? 'selected' : ''; ?>>Círculo</option>
                <option value="triangulo" <?= $figura->tipo == 'triangulo' ? 'selected' : ''; ?>>Triángulo</option>
            </select>
            <input type="color" class="colorFigura" data-figura="<?= $key; ?>" value="<?= $figura->color; ?>">
            <input type="text" class="nombreFigura" data-figura="<?= $key; ?>" value="<?= $figura->nombre; ?>">
        </fieldset>
        <br>
    <?php endforeach; ?>
</form>
</body>
</html>
