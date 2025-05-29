=========================
3: Estructuras de Control
=========================

En el flujo normal de ejecución, un programa se ejecuta instrucción por instrucción de forma secuencial. Sin embargo, la programación real requiere la capacidad de tomar decisiones y repetir acciones basándose en ciertas condiciones. Aquí es donde entran en juego las **estructuras de control**.

Las estructuras de control son construcciones fundamentales en cualquier lenguaje de programación que permiten alterar el flujo secuencial del programa, permitiendo que ciertas partes del código se ejecuten (o no), o se repitan, dependiendo de condiciones específicas.

Dominar las estructuras de control es esencial para crear programas que puedan responder de manera inteligente a diferentes situaciones y datos de entrada. Se dividen principalmente en dos categorías:

1.  **Estructuras Condicionales:** Permiten ejecutar bloques de código si, y solo si, se cumple una condición determinada.
2.  **Estructuras Repetitivas (Bucles):** Permiten ejecutar un bloque de código repetidamente mientras se cumpla una condición o un número específico de veces.

En este capítulo, exploraremos las estructuras de control más comunes en PHP, aprendiendo cómo utilizarlas para dirigir el flujo de nuestros programas.

3.1 Estructuras Condicionales
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Las estructuras condicionales son la base para la toma de decisiones en programación. Permiten que tu código evalúe una expresión (una condición) y ejecute diferentes bloques de código dependiendo de si esa condición es verdadera (TRUE) o falsa (FALSE).

Piensa en ellas como preguntas que le haces a tu programa: "¿Es cierto que...? Si es así, haz esto; si no, haz aquello."

El resultado de la evaluación de la condición (que generalmente utiliza operadores de comparación y lógicos) determina qué camino sigue el programa en su ejecución. Esto es crucial para crear lógica adaptativa, validar datos, controlar el acceso y mucho más.

Las estructuras condicionales más comunes son `if`, `else` y `elseif` (o `else if`), que se utilizan para crear ramificaciones en el código.

If Simple:
^^^^^^^^^^
El `if` simple es la estructura condicional más básica. Permite ejecutar un bloque de código *solamente si* una condición especificada es verdadera. Si la condición es falsa, el bloque de código dentro del `if` se ignora por completo, y el programa continúa con la siguiente instrucción después del bloque.

**Propósito:** Ejecutar código de forma condicional.
**Funciona:** Evalúa una única condición. Si es TRUE, ejecuta el bloque. Si es FALSE, lo salta.

.. code-block:: php

   <?php
   $edad = 18;

   if ($edad >= 18) {
       echo "Eres mayor de edad"; // Este código se ejecuta solo si $edad es 18 o más
   }

   echo "Este mensaje siempre aparece."; // Esta línea se ejecuta independientemente de la condición del if
   ?>

If-Else:
^^^^^^^^
La estructura `if-else` te permite definir dos caminos de ejecución mutuamente excluyentes. Si la condición del `if` es verdadera, se ejecuta el bloque de código dentro del `if`. Si la condición es falsa, se ejecuta el bloque de código dentro del `else`. Siempre se ejecutará *uno* de los dos bloques.

**Propósito:** Elegir entre dos acciones posibles basadas en una condición.
**Funciona:** Evalúa una condición. Si es TRUE, ejecuta el bloque del `if`. Si es FALSE, ejecuta el bloque del `else`.

.. code-block:: php

   <?php
   $nota = 85;

   if ($nota >= 70) {
       echo "Aprobaste el examen"; // Se ejecuta si $nota es 70 o más
   } else {
       echo "No aprobaste el examen"; // Se ejecuta si $nota es menor a 70
   }
   ?>

If-ElseIf-Else:
^^^^^^^^^^^^^^^
La estructura `if-elseif-else` (también puedes usar `else if` separado por un espacio) es útil cuando necesitas evaluar múltiples condiciones secuencialmente. El programa evalúa la primera condición del `if`. Si es falsa, evalúa la condición del primer `elseif`. Si esa también es falsa, evalúa la del siguiente `elseif`, y así sucesivamente. Si ninguna de las condiciones `if` o `elseif` es verdadera, se ejecuta el bloque opcional del `else` final. El programa ejecuta el primer bloque cuya condición sea verdadera y luego sale de toda la estructura.

**Propósito:** Evaluar múltiples condiciones para elegir entre varias acciones posibles.
**Funciona:** Evalúa condiciones en orden. Ejecuta el bloque de la primera condición que sea TRUE. Si ninguna es TRUE, ejecuta el bloque del `else` (si existe).

.. code-block:: php

   <?php
   $calificacion = 88;

   if ($calificacion >= 90) {
       echo "Excelente"; // Se evalúa primero
   } elseif ($calificacion >= 80) {
       echo "Muy bueno"; // Se evalúa si la primera es falsa
   } elseif ($calificacion >= 70) {
       echo "Bueno"; // Se evalúa si las anteriores son falsas
   } else {
       echo "Necesita mejorar"; // Se ejecuta si ninguna de las anteriores es verdadera
   }
   ?>

3.2 Operadores de Comparación
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
=======
=========================
3: Estructuras de Control
=========================

En el flujo normal de ejecución, un programa se ejecuta instrucción por instrucción de forma secuencial. Sin embargo, la programación real requiere la capacidad de tomar decisiones y repetir acciones basándose en ciertas condiciones. Aquí es donde entran en juego las **estructuras de control**.

Las estructuras de control son construcciones fundamentales en cualquier lenguaje de programación que permiten alterar el flujo secuencial del programa, permitiendo que ciertas partes del código se ejecuten (o no), o se repitan, dependiendo de condiciones específicas.

Dominar las estructuras de control es esencial para crear programas que puedan responder de manera inteligente a diferentes situaciones y datos de entrada. Se dividen principalmente en dos categorías:

1.  **Estructuras Condicionales:** Permiten ejecutar bloques de código si, y solo si, se cumple una condición determinada.
2.  **Estructuras Repetitivas (Bucles):** Permiten ejecutar un bloque de código repetidamente mientras se cumpla una condición o un número específico de veces.

En este capítulo, exploraremos las estructuras de control más comunes en PHP, aprendiendo cómo utilizarlas para dirigir el flujo de nuestros programas.

3.1 Estructuras Condicionales
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Las estructuras condicionales son la base para la toma de decisiones en programación. Permiten que tu código evalúe una expresión (una condición) y ejecute diferentes bloques de código dependiendo de si esa condición es verdadera (TRUE) o falsa (FALSE).

Piensa en ellas como preguntas que le haces a tu programa: "¿Es cierto que...? Si es así, haz esto; si no, haz aquello."

El resultado de la evaluación de la condición (que generalmente utiliza operadores de comparación y lógicos) determina qué camino sigue el programa en su ejecución. Esto es crucial para crear lógica adaptativa, validar datos, controlar el acceso y mucho más.

Las estructuras condicionales más comunes son `if`, `else` y `elseif` (o `else if`), que se utilizan para crear ramificaciones en el código.

If Simple:
^^^^^^^^^^
El `if` simple es la estructura condicional más básica. Permite ejecutar un bloque de código *solamente si* una condición especificada es verdadera. Si la condición es falsa, el bloque de código dentro del `if` se ignora por completo, y el programa continúa con la siguiente instrucción después del bloque.

**Propósito:** Ejecutar código de forma condicional.
**Funciona:** Evalúa una única condición. Si es TRUE, ejecuta el bloque. Si es FALSE, lo salta.

.. code-block:: php

   <?php
   $edad = 18;

   if ($edad >= 18) {
       echo "Eres mayor de edad"; // Este código se ejecuta solo si $edad es 18 o más
   }

   echo "Este mensaje siempre aparece."; // Esta línea se ejecuta independientemente de la condición del if
   ?>

If-Else:
^^^^^^^^
La estructura `if-else` te permite definir dos caminos de ejecución mutuamente excluyentes. Si la condición del `if` es verdadera, se ejecuta el bloque de código dentro del `if`. Si la condición es falsa, se ejecuta el bloque de código dentro del `else`. Siempre se ejecutará *uno* de los dos bloques.

**Propósito:** Elegir entre dos acciones posibles basadas en una condición.
**Funciona:** Evalúa una condición. Si es TRUE, ejecuta el bloque del `if`. Si es FALSE, ejecuta el bloque del `else`.

.. code-block:: php

   <?php
   $nota = 85;

   if ($nota >= 70) {
       echo "Aprobaste el examen"; // Se ejecuta si $nota es 70 o más
   } else {
       echo "No aprobaste el examen"; // Se ejecuta si $nota es menor a 70
   }
   ?>

If-ElseIf-Else:
^^^^^^^^^^^^^^^
La estructura `if-elseif-else` (también puedes usar `else if` separado por un espacio) es útil cuando necesitas evaluar múltiples condiciones secuencialmente. El programa evalúa la primera condición del `if`. Si es falsa, evalúa la condición del primer `elseif`. Si esa también es falsa, evalúa la del siguiente `elseif`, y así sucesivamente. Si ninguna de las condiciones `if` o `elseif` es verdadera, se ejecuta el bloque opcional del `else` final. El programa ejecuta el primer bloque cuya condición sea verdadera y luego sale de toda la estructura.

**Propósito:** Evaluar múltiples condiciones para elegir entre varias acciones posibles.
**Funciona:** Evalúa condiciones en orden. Ejecuta el bloque de la primera condición que sea TRUE. Si ninguna es TRUE, ejecuta el bloque del `else` (si existe).

.. code-block:: php

   <?php
   $calificacion = 88;

   if ($calificacion >= 90) {
       echo "Excelente"; // Se evalúa primero
   } elseif ($calificacion >= 80) {
       echo "Muy bueno"; // Se evalúa si la primera es falsa
   } elseif ($calificacion >= 70) {
       echo "Bueno"; // Se evalúa si las anteriores son falsas
   } else {
       echo "Necesita mejorar"; // Se ejecuta si ninguna de las anteriores es verdadera
   }
   ?>

3.2 Operadores de Comparación
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block:: php

   <?php
   $a = 10;
   $b = 20;

   // Operadores de comparación
   $a == $b   // Igual a
   $a != $b   // Diferente de
   $a < $b    // Menor que
   $a > $b    // Mayor que
   $a <= $b   // Menor o igual
   $a >= $b   // Mayor o igual
   $a === $b  // Idéntico (mismo valor y tipo)
   $a !== $b  // No idéntico
   ?>

3.3 Operadores Lógicos
~~~~~~~~~~~~~~~~~~~~~~
.. code-block:: php

   <?php
   $edad = 25;
   $tiene_licencia = true;

   // AND (&&)
   if ($edad >= 18 && $tiene_licencia) {
       echo "Puede conducir";
   }

   // OR (||)
   if ($edad < 18 || !$tiene_licencia) {
       echo "No puede conducir";
   }

   // NOT (!)
   if (!$tiene_licencia) {
       echo "Necesita obtener licencia";
   }
   ?>

3.4 Switch
~~~~~~~~~~
La estructura `switch` (también conocida como "selector múltiple") es una alternativa a las largas cadenas de `if-elseif-else` cuando necesitas comparar una *misma variable* o expresión contra *múltiples valores constantes* discretos.

En lugar de evaluar una condición booleana en cada paso (`true` o `false`), `switch` eval��a una única expresión al principio y luego compara su resultado con una serie de valores definidos en cláusulas `case`. Cuando encuentra una `case` cuyo valor coincide con el de la expresión, ejecuta el bloque de código asociado a esa `case`.

Es importante usar la sentencia `break;` al final de cada bloque `case` para salir de la estructura `switch` una vez que se encuentra una coincidencia y se ejecuta el código. Sin `break`, la ejecución continuará en los siguientes bloques `case` (comportamiento conocido como "fall-through"), lo cual rara vez es deseado.

La cláusula opcional `default` se ejecuta si la expresión no coincide con ninguno de los valores `case`.

**Propósito:** Seleccionar un bloque de código a ejecutar basado en la igualdad de una expresión con múltiples valores posibles.
**Funciona:** Evalúa una expresión y la compara con valores `case`. Ejecuta el código del primer `case` que coincide. El `default` se ejecuta si no hay coincidencias.
**Ideal para:** Menús basados en opciones numéricas o de texto, manejo de estados, etc.

.. code-block:: php

   <?php
   $dia = "lunes";

   switch ($dia) {
       case "lunes":
           echo "Inicio de semana laboral";
           break;
       case "martes":
       case "miércoles":
       case "jueves":
           echo "Día laboral";
           break;
       case "viernes":
           echo "¡Por fin viernes!";
           break;
       case "sábado":
       case "domingo":
           echo "Fin de semana";
           break;
       default:
           echo "Día no válido";
   }
   ?>

3.5 Bucles (Loops)
~~~~~~~~~~~~~~~~~~
Las estructuras repetitivas, comúnmente conocidas como **bucles** o **loops**, permiten ejecutar un bloque de código múltiples veces de forma automática. Son esenciales para tareas que implican procesar listas de elementos, realizar cálculos iterativos, o esperar a que se cumpla una condición.

En lugar de escribir la misma instrucción repetidamente, los bucles nos permiten definir un conjunto de instrucciones que se repetirán mientras (o hasta que) se cumpla una cierta condición, o un número predeterminado de veces. Esto ahorra tiempo, reduce errores y hace que el código sea mucho más fácil de mantener y modificar.

Los bucles más comunes en PHP son `while` y `for`.

While:
^^^^^^
El bucle `while` ejecuta un bloque de código *mientras* una condición especificada sea verdadera. La condición se evalúa *antes* de cada iteración. Si la condición es verdadera, se ejecuta el código dentro del bucle y luego la condición se evalúa nuevamente. Este proceso continúa hasta que la condición se vuelve falsa. Es crucial asegurarse de que la condición eventualmente cambie para evitar bucles infinitos.

**Propósito:** Repetir un bloque de código un número desconocido de veces, mientras una condición se mantenga verdadera.
**Funciona:** Evalúa la condición al inicio. Si es TRUE, ejecuta el bloque y repite. Si es FALSE, sale del bucle.
**Ideal para:** Leer datos de un archivo hasta el final, procesar elementos de una cola, esperar una entrada del usuario válida.

.. code-block:: php
.. code-block:: php

   <?php
   $contador = 1;

   while ($contador <= 5) {
       echo "Número: $contador<br>";
       $contador++;
   }
   ?>

For:
^^^^
El bucle `for` es ideal cuando sabes de antemano cuántas veces necesitas repetir un bloque de código. Es muy común para iterar sobre rangos numéricos o elementos indexados.

La sintaxis del bucle `for` consta de tres partes principales, separadas por punto y coma `;`, dentro de los paréntesis:

1.  **Inicialización:** Se ejecuta *una sola vez* al comienzo del bucle. Usualmente se usa para inicializar un contador.
2.  **Condición:** Se evalúa *antes de cada iteración*. Si es verdadera, el bucle continúa; si es falsa, el bucle termina.
3.  **Incremento/Decremento:** Se ejecuta *al final de cada iteración* después de que se ha ejecutado el bloque de código del bucle. Usualmente se usa para actualizar el contador.

**Propósito:** Repetir un bloque de código un número *determinado* de veces.
**Funciona:** Inicializa, evalúa condición, ejecuta bloque, actualiza contador, repite hasta que la condición sea falsa.
**Ideal para:** Iterar sobre arrays por índice, ejecutar una acción un número fijo de veces.

.. code-block:: php

   <?php
   for ($i = 1; $i <= 10; $i++) {
       echo "Tabla del 5: 5 x $i = " . (5 * $i) . "<br>";
   }
   ?>

Ejercicios Semana 3:
~~~~~~~~~~~~~~~~~~~~
1. **Sistema de Calificaciones:** Programa que convierta calificaciones numéricas a letras
2. **Calculadora de Edad:** Determinar si una persona es niño, adolescente, adulto o adulto mayor
3. **Tablas de Multiplicar:** Generar tablas del 1 al 10 usando bucles
4. **Número Par o Impar:** Verificar si un número es par o impar
