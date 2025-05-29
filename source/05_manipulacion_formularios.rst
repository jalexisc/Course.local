==============================
5: Manipulación de Formularios
==============================

5.1 Fundamentos de Formularios HTML
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Formulario Básico:
^^^^^^^^^^^^^^^^^^
.. code-block:: html

   <!DOCTYPE html>
   <html>
   <head>
       <title>Mi Formulario</title>
   </head>
   <body>
       <form action="procesar.php" method="POST">
           <label for="nombre">Nombre:</label>
           <input type="text" id="nombre" name="nombre" required>

           <label for="email">Email:</label>
           <input type="email" id="email" name="email" required>

           <label for="edad">Edad:</label>
           <input type="number" id="edad" name="edad" min="1" max="120">

           <input type="submit" value="Enviar">
       </form>
   </body>
   </html>

5.2 Procesamiento con PHP
~~~~~~~~~~~~~~~~~~~~~~~~~

Archivo procesar.php:
^^^^^^^^^^^^^^^^^^^^^
.. code-block:: php

   <?php
   // Verificar si el formulario fue enviado
   if ($_POST) {
       // Obtener datos del formulario
       $nombre = $_POST['nombre'];
       $email = $_POST['email'];
       $edad = $_POST['edad'];

       // Mostrar los datos
       echo "<h2>Datos Recibidos:</h2>";
       echo "Nombre: $nombre<br>";
       echo "Email: $email<br>";
       echo "Edad: $edad años<br>";
   }
   ?>

5.3 Métodos GET y POST
~~~~~~~~~~~~~~~~~~~~~~

Método GET:
^^^^^^^^^^^
.. code-block:: php

   <?php
   // URL: ejemplo.php?nombre=Juan&edad=25
   if (isset($_GET['nombre'])) {
       $nombre = $_GET['nombre'];
       $edad = $_GET['edad'];
       echo "Hola $nombre, tienes $edad años";
   }
   ?>

Método POST (Recomendado para formularios):
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code-block:: php

   <?php
   if ($_SERVER['REQUEST_METHOD'] == 'POST') {
       $usuario = $_POST['usuario'];
       $password = $_POST['password'];

       // Procesar datos de forma segura
       echo "Usuario: " . htmlspecialchars($usuario);
   }
   ?>

5.4 Validación de Formularios
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Validación Básica:
^^^^^^^^^^^^^^^^^^
.. code-block:: php

   <?php
   $errores = [];

   if ($_POST) {
       // Validar nombre
       if (empty($_POST['nombre'])) {
           $errores[] = "El nombre es obligatorio";
       } elseif (strlen($_POST['nombre']) < 2) {
           $errores[] = "El nombre debe tener al menos 2 caracteres";
       }

       // Validar email
       if (empty($_POST['email'])) {
           $errores[] = "El email es obligatorio";
       } elseif (!filter_var($_POST['email'], FILTER_VALIDATE_EMAIL)) {
           $errores[] = "El email no es válido";
       }

       // Validar edad
       if (empty($_POST['edad'])) {
           $errores[] = "La edad es obligatoria";
       } elseif ($_POST['edad'] < 1 || $_POST['edad'] > 120) {
           $errores[] = "La edad debe estar entre 1 y 120 años";
       }

       // Si no hay errores, procesar
       if (empty($errores)) {
           echo "Formulario válido, procesando datos...";
           // Aquí iría el código para guardar en base de datos
       } else {
           echo "<ul>";
           foreach ($errores as $error) {
               echo "<li style='color: red;'>$error</li>";
           }
           echo "</ul>";
       }
   }
   ?>

5.5 Formulario Completo con Validación
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

registro.php:
^^^^^^^^^^^^^^
.. code-block:: php

   <?php
   $nombre = $email = $edad = "";
   $errores = [];

   if ($_SERVER["REQUEST_METHOD"] == "POST") {
       // Limpiar y validar nombre
       if (empty($_POST["nombre"])) {
           $errores[] = "El nombre es obligatorio";
       } else {
           $nombre = limpiar_entrada($_POST["nombre"]);
           if (!preg_match("/^[a-zA-ZáéíóúÁÉÍÓÚñÑ ]*$/", $nombre)) {
               $errores[] = "Solo se permiten letras y espacios en el nombre";
           }
       }

       // Validar email
       if (empty($_POST["email"])) {
           $errores[] = "El email es obligatorio";
       } else {
           $email = limpiar_entrada($_POST["email"]);
           if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
               $errores[] = "Formato de email inválido";
           }
       }

       // Validar edad
       if (empty($_POST["edad"])) {
           $errores[] = "La edad es obligatoria";
       } else {
           $edad = limpiar_entrada($_POST["edad"]);
           if (!is_numeric($edad) || $edad < 1 || $edad > 120) {
               $errores[] = "La edad debe ser un número entre 1 y 120";
           }
       }

       // Si no hay errores
       if (empty($errores)) {
           echo "<div style='color: green; padding: 10px; border: 1px solid green;'>";
           echo "<h3>¡Registro exitoso!</h3>";
           echo "Nombre: $nombre<br>";
           echo "Email: $email<br>";
           echo "Edad: $edad años<br>";
           echo "</div>";
       }
   }

   function limpiar_entrada($data) {
       $data = trim($data);           // Eliminar espacios
       $data = stripslashes($data);   // Eliminar backslashes
       $data = htmlspecialchars($data); // Convertir caracteres especiales
       return $data;
   }
   ?>

   <!DOCTYPE html>
   <html>
   <head>
       <title>Formulario de Registro</title>
       <style>
           .error { color: red; }
           .form-group { margin-bottom: 15px; }
           label { display: block; margin-bottom: 5px; }
           input[type="text"], input[type="email"], input[type="number"] {
               width: 300px;
               padding: 8px;
               border: 1px solid #ddd;
           }
           input[type="submit"] {
               background-color: #4CAF50;
               color: white;
               padding: 10px 20px;
               border: none;
               cursor: pointer;
           }
       </style>
   </head>
   <body>
       <h2>Formulario de Registro</h2>

       <?php if (!empty($errores)): ?>
           <div style="color: red; border: 1px solid red; padding: 10px; margin-bottom: 20px;">
               <h4>Errores encontrados:</h4>
               <ul>
                   <?php foreach ($errores as $error): ?>
                       <li><?php echo $error; ?></li>
                   <?php endforeach; ?>
               </ul>
           </div>
       <?php endif; ?>

       <form method="post" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]); ?>">
           <div class="form-group">
               <label for="nombre">Nombre:</label>
               <input type="text" name="nombre" value="<?php echo $nombre; ?>">
           </div>

           <div class="form-group">
               <label for="email">Email:</label>
               <input type="email" name="email" value="<?php echo $email; ?>">
           </div>

           <div class="form-group">
               <label for="edad">Edad:</label>
               <input type="number" name="edad" value="<?php echo $edad; ?>">
           </div>

           <input type="submit" name="submit" value="Registrar">
       </form>
   </body>
   </html>

5.6 Tipos de Input Avanzados
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: html

   <!-- Diferentes tipos de input -->
   <form method="POST" action="procesar_avanzado.php">
       <!-- Texto con patrón -->
       <input type="text" name="telefono" pattern="[0-9]{3}-[0-9]{3}-[0-9]{4}"
              placeholder="123-456-7890">

       <!-- Contraseña -->
       <input type="password" name="password" minlength="8">

       <!-- Fecha -->
       <input type="date" name="fecha_nacimiento">

       <!-- Rango -->
       <input type="range" name="puntuacion" min="1" max="10" value="5">

       <!-- Checkbox -->
       <input type="checkbox" name="acepta_terminos" value="si">

       <!-- Radio buttons -->
       <input type="radio" name="genero" value="masculino"> Masculino
       <input type="radio" name="genero" value="femenino"> Femenino

       <!-- Select -->
       <select name="pais">
           <option value="mexico">México</option>
           <option value="españa">España</option>
           <option value="argentina">Argentina</option>
       </select>

       <!-- Textarea -->
       <textarea name="comentarios" rows="4" cols="50"></textarea>
   </form>

Ejercicios Semana 5:
~~~~~~~~~~~~~~~~~~~~

1. **Formulario de Contacto:** Crear formulario completo con validación
2. **Calculadora Web:** Formulario que realice operaciones matemáticas
3. **Encuesta de Satisfacción:** Formulario con diferentes tipos de input
4. **Sistema de Login Simple:** Formulario de inicio de sesión básico
