=====================================
2: Variables y Tipos de Datos
=====================================

Semana 2: Trabajando con Datos
------------------------------

2.1 Variables en PHP
~~~~~~~~~~~~~~~~~~~~

Las variables son contenedores que almacenan datos. En PHP, las variables comienzan con el símbolo ``$``.

.. code-block:: php

   <?php
   $nombre = "Juan";
   $edad = 25;
   $altura = 1.75;
   $estudiante = true;
   ?>

Reglas para Variables:
^^^^^^^^^^^^^^^^^^^^^^
- Comienzan con ``$`` seguido de una letra o guión bajo
- Pueden contener letras, números y guiones bajos
- Son case-sensitive (``$nombre`` ≠ ``$Nombre``)
- No pueden comenzar con números

2.2 Tipos de Datos
~~~~~~~~~~~~~~~~~~

Tipos Primitivos:
^^^^^^^^^^^^^^^^^

**String (Cadena de texto):**

.. code-block:: php

   <?php
   $nombre = "María García";
   $mensaje = 'Bienvenido al curso';
   $multilinea = "Esta es una línea\ny esta es otra línea";
   ?>

**Integer (Entero):**

.. code-block:: php

   <?php
   $edad = 30;
   $temperatura = -5;
   $poblacion = 1000000;
   ?>

**Float (Decimal):**

.. code-block:: php

   <?php
   $precio = 19.99;
   $pi = 3.14159;
   $porcentaje = 85.5;
   ?>

**Boolean (Verdadero/Falso):**

.. code-block:: php

   <?php
   $activo = true;
   $terminado = false;
   $mayor_edad = ($edad >= 18);
   ?>

2.3 Operaciones con Variables
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Concatenación de Strings:
^^^^^^^^^^^^^^^^^^^^^^^^^
.. code-block:: php

   <?php
   $nombre = "Ana";
   $apellido = "López";
   $nombre_completo = $nombre . " " . $apellido;
   echo $nombre_completo; // Resultado: Ana López
   ?>

Interpolación de Variables:
^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code-block:: php

   <?php
   $producto = "Laptop";
   $precio = 899.99;
   echo "El $producto cuesta $$precio"; // El Laptop cuesta $899.99
   ?>

2.4 Constantes
~~~~~~~~~~~~~~

Las constantes son valores que no cambian durante la ejecución:

.. code-block:: php

   <?php
   define("SITIO_NOMBRE", "Mi Blog Personal");
   define("VERSION", "1.0");
   const PI = 3.14159;

   echo SITIO_NOMBRE; // Mi Blog Personal
   echo VERSION;      // 1.0
   ?>

2.5 Conversión de Tipos
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: php

   <?php
   $numero_texto = "123";
   $numero_entero = (int)$numero_texto;
   $numero_decimal = (float)"45.67";
   $texto = (string)100;

   // Verificar tipos
   var_dump($numero_entero); // int(123)
   var_dump($numero_decimal); // float(45.67)
   ?>

Ejercicios Semana 2:
~~~~~~~~~~~~~~~~~~~~

1. **Calculadora Básica:** Crear variables para dos números y mostrar suma, resta, multiplicación y división
2. **Información Personal:** Crear un perfil con nombre, edad, ciudad y mostrar en formato organizado
3. **Conversiones:** Practicar conversión entre diferentes tipos de datos
