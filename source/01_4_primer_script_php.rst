=======================================
1.4 Tu Primer Script PHP: "Hola, Mundo"
=======================================

Vamos a crear y ejecutar el tradicional programa "Hola, Mundo" para verificar que el entorno de desarrollo está funcionando correctamente y para familiarizarnos con la sintaxis más elemental de PHP.

Pasos para crear y ejecutar el script:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
1.  **Navegar al directorio de proyectos:**
    Abre el directorio raíz de documentos de tu servidor web. Si usas XAMPP, este es ``C:\xampp\htdocs\`` (o la ruta donde lo hayas instalado).

2.  **Crear un nuevo archivo:**
    Dentro de ``htdocs``, crea un nuevo archivo llamado ``hola_mundo.php``. Puedes crear una subcarpeta dentro de ``htdocs`` para organizar tus proyectos, por ejemplo ``htdocs\curso_php\hola_mundo.php``.

3.  **Escribir el código PHP:**
    Abre ``hola_mundo.php`` con tu editor de código e ingresa el siguiente contenido:

    .. code-block:: php
       :linenos:

       <?php
       // Este es un comentario de una sola línea

       /*
        * Este es un comentario
        * de múltiples líneas.
        */

       // La función echo se utiliza para enviar salida al navegador.
       echo "¡Hola, Mundo desde PHP!";

       // Todas las instrucciones en PHP deben terminar con un punto y coma (;).
       ?>

4.  **Guardar el archivo.**

5.  **Ejecutar el script a través del servidor web:**
    Abre tu navegador web y navega a la URL correspondiente.
    -   Si guardaste el archivo directamente en ``htdocs``: ``http://localhost/hola_mundo.php``
    -   Si lo guardaste en ``htdocs\curso_php\``: ``http://localhost/curso_php/hola_mundo.php``

    Deberías ver el texto "¡Hola, Mundo desde PHP!" desplegado en la página.

Anatomía de un Script PHP Básico:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
-   **Delimitadores de PHP (Etiquetas PHP):**
    El código PHP se encierra entre las etiquetas de apertura ``<?php`` y de cierre ``?>``. Todo lo que esté fuera de estas etiquetas es tratado como HTML estándar (o texto plano) y es enviado directamente al cliente.
    -   En archivos que contienen únicamente código PHP, la etiqueta de cierre ``?>`` al final del archivo es opcional y, de hecho, se recomienda omitirla por el estándar PSR-12 para prevenir la inyección accidental de espacios en blanco o líneas nuevas después de la etiqueta de cierre, lo cual podría causar problemas con las cabeceras HTTP.

-   **Instrucciones (Statements):**
    Una instrucción es una unidad de código que realiza una acción. En PHP, la mayoría de las instrucciones simples terminan con un punto y coma (``;``). Por ejemplo, ``echo "¡Hola, Mundo desde PHP!";`` es una instrucción.

-   **La función ``echo``:**
    ``echo`` es una construcción del lenguaje (no técnicamente una función, aunque se comporta como tal en muchos aspectos) que se utiliza para enviar una o más cadenas de texto al flujo de salida, que usualmente es el navegador web del cliente.

-   **Comentarios:**
    Los comentarios son porciones de código que el intérprete de PHP ignora. Se utilizan para documentar el código y hacerlo más comprensible para otros desarrolladores (o para tu yo futuro).
    -   Comentarios de una sola línea: Comienzan con ``//`` o ``#``.
    -   Comentarios multilínea: Comienzan con ``/*`` y terminan con ``*/``.

-   **Sensibilidad a Mayúsculas y Minúsculas (Case-Sensitivity):**
    -   **Variables:** Los nombres de las variables en PHP son sensibles a mayúsculas y minúsculas. ``$miVariable`` es diferente de ``$mivariable``.
    -   **Constantes:** Por convención, los nombres de las constantes se escriben en mayúsculas, pero por defecto también son sensibles a mayúsculas y minúsculas (aunque ``define()`` tiene una opción para hacerlas insensibles, no se recomienda).
    -   **Funciones, nombres de clases y construcciones del lenguaje (e.g., ``echo``, ``if``, ``while``):** Generalmente son insensibles a mayúsculas y minúsculas. ``echo``, ``ECHO``, y ``EcHo`` se refieren a la misma construcción. Sin embargo, la convención es usar minúsculas.

Ejercicios Semana 1:
~~~~~~~~~~~~~~~~~~~~
1. **Ejercicio 1:** Crear un archivo que muestre tu nombre y edad
2. **Ejercicio 2:** Hacer un programa que muestre la fecha actual
3. **Ejercicio 3:** Crear una página que combine HTML y PHP
