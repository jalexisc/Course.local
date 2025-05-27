================================
6: Manejo de Archivos y Sesiones
================================

6.1 Manipulación de Archivos
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Leer Archivos:
^^^^^^^^^^^^^
.. code-block:: php

   <?php
   // Leer archivo completo
   $contenido = file_get_contents('datos.txt');
   echo $contenido;

   // Leer línea por línea
   $archivo = fopen('datos.txt', 'r');
   if ($archivo) {
       while (($linea = fgets($archivo)) !== false) {
           echo $linea . "<br>";
       }
       fclose($archivo);
   }

   // Leer como array
   $lineas = file('datos.txt');
   foreach ($lineas as $numero => $linea) {
       echo "Línea #$numero: $linea<br>";
   }
   ?>

Escribir Archivos:
^^^^^^^^^^^^^^^^^
.. code-block:: php

   <?php
   // Escribir texto simple
   $texto = "¡Hola, mundo desde PHP!";
   file_put_contents('saludo.txt', $texto);

   // Agregar contenido
   $nuevo_texto = "\nEsta es una nueva línea";
   file_put_contents('saludo.txt', $nuevo_texto, FILE_APPEND);

   // Escribir con fopen
   $archivo = fopen('log.txt', 'a'); // 'a' para append
   if ($archivo) {
       $fecha = date('Y-m-d H:i:s');
       fwrite($archivo, "[$fecha] Usuario visitó la página\n");
       fclose($archivo);
   }
   ?>

6.2 Sistema de Registro de Usuarios
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

registro_archivo.php:
^^^^^^^^^^^^^^^^^^^^^
.. code-block:: php

   <?php
   $mensaje = "";

   if ($_POST) {
       $nombre = trim($_POST['nombre']);
       $email = trim($_POST['email']);
       $edad = trim($_POST['edad']);

       // Validar datos
       if (!empty($nombre) && !empty($email) && is_numeric($edad)) {
           // Crear línea de datos
           $fecha_registro = date('Y-m-d H:i:s');
           $linea_datos = "$fecha_registro|$nombre|$email|$edad\n";

           // Guardar en archivo
           if (file_put_contents('usuarios.txt', $linea_datos, FILE_APPEND)) {
               $mensaje = "<p style='color: green;'>Usuario registrado exitosamente</p>";
           } else {
               $mensaje = "<p style='color: red;'>Error al guardar usuario</p>";
           }
       } else {
           $mensaje = "<p style='color: red;'>Por favor complete todos los campos</p>";
       }
   }
   ?>

   <!DOCTYPE html>
   <html>
   <body>
       <h2>Registro de Usuario</h2>
       <?php echo $mensaje; ?>

       <form method="POST">
           <p>
               <label>Nombre:</label><br>
               <input type="text" name="nombre" required>
           </p>
           <p>
               <label>Email:</label><br>
               <input type="email" name="email" required>
           </p>
           <p>
               <label>Edad:</label><br>
               <input type="number" name="edad" required>
           </p>
           <p>
               <input type="submit" value="Registrar">
           </p>
       </form>

       <h3>Usuarios Registrados:</h3>

   ```

   ### Ejercicios Semana 6:

   1. **Contador de Visitas:** Guardar el número de visitas en un archivo
   2. **Libro de Visitas Simple:** Permitir a los usuarios dejar mensajes que se guardan en un archivo
   3. **Gestor de Tareas:** Crear tareas y guardarlas/leerlas desde un archivo de texto
   4. **Login con Sesiones:** Implementar inicio y cierre de sesión usando `$_SESSION`
