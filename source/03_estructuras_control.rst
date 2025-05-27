=========================
3: Estructuras de Control
=========================

3.1 Estructuras Condicionales
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
If Simple:
^^^^^^^^^^
.. code-block:: php

   <?php
   $edad = 18;

   if ($edad >= 18) {
       echo "Eres mayor de edad";
   }
   ?>

If-Else:
^^^^^^^^
.. code-block:: php

   <?php
   $nota = 85;

   if ($nota >= 70) {
       echo "Aprobaste el examen";
   } else {
       echo "No aprobaste el examen";
   }
   ?>

If-ElseIf-Else:
^^^^^^^^^^^^^^^
.. code-block:: php

   <?php
   $calificacion = 88;

   if ($calificacion >= 90) {
       echo "Excelente";
   } elseif ($calificacion >= 80) {
       echo "Muy bueno";
   } elseif ($calificacion >= 70) {
       echo "Bueno";
   } else {
       echo "Necesita mejorar";
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
While:
^^^^^^
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
