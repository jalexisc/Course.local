=====================
4: Arrays y Funciones
=====================


4.1 Arrays (Arreglos)
~~~~~~~~~~~~~~~~~~~~~

Los arrays son estructuras que pueden almacenar múltiples valores.

Arrays Indexados:
^^^^^^^^^^^^^^^^^
.. code-block:: php

   <?php
   $frutas = array("manzana", "banana", "naranja");
   // O sintaxis corta (PHP 5.4+)
   $colores = ["rojo", "verde", "azul"];

   echo $frutas[0]; // manzana
   echo $colores[2]; // azul
   ?>

Arrays Asociativos:
^^^^^^^^^^^^^^^^^^^
.. code-block:: php

   <?php
   $persona = array(
       "nombre" => "Carlos",
       "edad" => 30,
       "ciudad" => "Madrid"
   );

   // O sintaxis corta
   $producto = [
       "nombre" => "Laptop",
       "precio" => 899.99,
       "categoria" => "Tecnología"
   ];

   echo $persona["nombre"]; // Carlos
   echo $producto["precio"]; // 899.99
   ?>

Arrays Multidimensionales:
^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code-block:: php

   <?php
   $estudiantes = [
       [
           "nombre" => "Ana",
           "calificaciones" => [85, 92, 78]
       ],
       [
           "nombre" => "Luis",
           "calificaciones" => [90, 88, 85]
       ]
   ];

   echo $estudiantes[0]["nombre"]; // Ana
   echo $estudiantes[0]["calificaciones"][1]; // 92
   ?>

4.2 Operaciones con Arrays
~~~~~~~~~~~~~~~~~~~~~~~~~~

Agregar Elementos:
^^^^^^^^^^^^^^^^^^
.. code-block:: php

   <?php
   $numeros = [1, 2, 3];

   // Agregar al final
   $numeros[] = 4;
   array_push($numeros, 5, 6);

   // Agregar al inicio
   array_unshift($numeros, 0);

   print_r($numeros); // [0, 1, 2, 3, 4, 5, 6]
   ?>

Recorrer Arrays:
^^^^^^^^^^^^^^^^
.. code-block:: php

   <?php
   $frutas = ["manzana", "banana", "naranja"];

   // Con for
   for ($i = 0; $i < count($frutas); $i++) {
       echo $frutas[$i] . "<br>";
   }

   // Con foreach (recomendado)
   foreach ($frutas as $fruta) {
       echo $fruta . "<br>";
   }

   // Con foreach e índice
   foreach ($frutas as $indice => $fruta) {
       echo "$indice: $fruta<br>";
   }
   ?>

4.3 Funciones Útiles para Arrays
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: php

   <?php
   $numeros = [3, 1, 4, 1, 5, 9];

   // Contar elementos
   echo count($numeros); // 6

   // Buscar elemento
   if (in_array(4, $numeros)) {
       echo "El 4 está en el array";
   }

   // Ordenar
   sort($numeros); // Ascendente
   rsort($numeros); // Descendente

   // Obtener valores únicos
   $unicos = array_unique($numeros);

   // Combinar arrays
   $array1 = [1, 2, 3];
   $array2 = [4, 5, 6];
   $combinado = array_merge($array1, $array2);
   ?>

4.4 Funciones Definidas por el Usuario
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Función Básica:
^^^^^^^^^^^^^^^
.. code-block:: php

   <?php
   function saludar() {
       echo "¡Hola desde una función!";
   }

   // Llamar la función
   saludar();
   ?>

Funciones con Parámetros:
^^^^^^^^^^^^^^^^^^^^^^^^^
.. code-block:: php

   <?php
   function saludar_persona($nombre, $apellido = "") {
       if ($apellido != "") {
           echo "Hola, $nombre $apellido";
       } else {
           echo "Hola, $nombre";
       }
   }

   saludar_persona("Ana");           // Hola, Ana
   saludar_persona("Carlos", "Pérez"); // Hola, Carlos Pérez
   ?>

Funciones que Retornan Valores:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code-block:: php

   <?php
   function sumar($a, $b) {
       return $a + $b;
   }

   function calcular_area_rectangulo($largo, $ancho) {
       return $largo * $ancho;
   }

   $resultado = sumar(5, 3);
   echo $resultado; // 8

   $area = calcular_area_rectangulo(10, 5);
   echo "El área es: $area"; // El área es: 50
   ?>

Funciones con Arrays:
^^^^^^^^^^^^^^^^^^^^^
.. code-block:: php

   <?php
   function obtener_promedio($calificaciones) {
       $suma = array_sum($calificaciones);
       $cantidad = count($calificaciones);
       return $suma / $cantidad;
   }

   function obtener_mayor($numeros) {
       return max($numeros);
   }

   $mis_notas = [85, 92, 78, 90];
   $promedio = obtener_promedio($mis_notas);
   echo "Promedio: $promedio"; // Promedio: 86.25
   ?>

4.5 Alcance de Variables (Scope)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: php

   <?php
   $variable_global = "Soy global";

   function ejemplo_scope() {
       $variable_local = "Soy local";
       global $variable_global; // Para usar variable global

       echo $variable_global;   // Funciona
       echo $variable_local;    // Funciona
   }

   echo $variable_global;   // Funciona
   // echo $variable_local; // Error: variable no existe aquí
   ?>

Ejercicios Semana 4:
~~~~~~~~~~~~~~~~~~~~

1. **Gestión de Estudiantes:** Crear array de estudiantes con calificaciones y calcular promedios
2. **Inventario Simple:** Sistema para agregar, eliminar y buscar productos
3. **Calculadora con Funciones:** Crear funciones para operaciones matemáticas básicas
4. **Análisis de Datos:** Funciones para encontrar máximo, mínimo y promedio de un array
