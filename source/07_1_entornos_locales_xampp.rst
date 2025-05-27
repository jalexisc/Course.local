====================================================================
7.1 Fundamentos y Configuración de Entornos Locales (XAMPP)
====================================================================

Cuando hablamos de un **entorno de desarrollo local** (o simplemente "entorno local"), nos referimos a una configuración de software instalada y ejecutándose directamente en tu propia computadora personal (sea laptop o de escritorio). Este entorno simula el comportamiento de un servidor web real, pero opera de forma completamente autónoma y privada en tu máquina, sin necesidad de una conexión a Internet para acceder a las aplicaciones que desarrollas en él (a menos que la aplicación misma requiera servicios externos).

**Ventajas Clave de un Entorno Local:**

-   **Autonomía y Control Total:** Tienes control completo sobre la configuración del servidor web (Apache, Nginx), la versión de PHP, el sistema de base de datos (MySQL/MariaDB), y todas las extensiones y herramientas asociadas. Puedes instalar, modificar y experimentar sin afectar a nadie más.
-   **Velocidad de Desarrollo:** Al ejecutarse en tu propia máquina, la respuesta es inmediata. No hay latencia de red al cargar páginas o ejecutar scripts, lo que agiliza enormemente el ciclo de desarrollo: codificar, probar, depurar.
-   **Desarrollo Offline:** Puedes seguir trabajando en tus proyectos incluso sin conexión a Internet.
-   **Costo Cero (Generalmente):** La mayoría de las herramientas para crear entornos locales (como XAMPP) son gratuitas y de código abierto.
-   **Seguridad para Experimentar:** Puedes probar código nuevo, experimentar con configuraciones arriesgadas o incluso cometer errores graves sin temor a romper un servidor en vivo o afectar datos de producción. Es un "sandbox" (caja de arena) seguro.

En esta sección, nos centraremos en **XAMPP**, una de las herramientas más populares y sencillas para establecer rápidamente un entorno de desarrollo local completo para PHP. XAMPP agrupa todos los componentes necesarios (Apache, MariaDB, PHP, Perl) en un único paquete fácil de instalar.

Instalación Detallada y Configuración de XAMPP
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

XAMPP es una de las formas más populares y sencillas de instalar un stack completo de Apache, MariaDB, PHP y Perl en tu sistema local. Aunque la instalación básica es directa, algunos detalles y configuraciones adicionales pueden optimizar tu flujo de trabajo.

Requisitos Previos:
^^^^^^^^^^^^^^^^^^^
-   Sistema Operativo: Windows, Linux o macOS.
-   Privilegios de administrador para la instalación.
-   Desactivar temporalmente el software antivirus si causa problemas durante la instalación (poco común).
-   Asegurarse de que no haya otros servicios utilizando los puertos por defecto de Apache (80, 443) o MySQL (3306), como otra instancia de Apache, IIS, Skype, etc.

Pasos Detallados de Instalación (Windows):
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
1.  **Descarga del Instalador:**
    -   Visita la `página oficial de descargas de Apache Friends <https://www.apachefriends.org/index.html>`_.
    -   Descarga la versión de XAMPP para tu sistema operativo. Se recomienda descargar la versión más reciente que incluya una versión estable y moderna de PHP (e.g., PHP 8.x).

2.  **Ejecución del Instalador:**
    -   Una vez descargado, ejecuta el archivo instalador (e.g., ``xampp-windows-x64-8.x.x-0-VS16-installer.exe``).
    -   **Control de Cuentas de Usuario (UAC):** Si el UAC de Windows está activo, podría mostrar una advertencia sobre permisos. Es recomendable no instalar XAMPP en ``C:\Program Files\`` debido a restricciones de escritura. El instalador usualmente sugiere ``C:\xampp`` por defecto, lo cual es una buena opción. Haz clic en "OK" si aparece esta advertencia.
    -   **Componentes a Instalar:** El asistente te permitirá seleccionar los componentes. Como mínimo, asegúrate de que estén seleccionados:

        -   Apache (Servidor Web)
        -   MySQL (o MariaDB, que es el SGBD incluido)
        -   PHP (Lenguaje de scripting)
        -   phpMyAdmin (Herramienta web para administrar bases de datos MySQL/MariaDB)

        Otros componentes como Fake Sendmail, Webalizer, Tomcat, Perl, etc., son opcionales y puedes desmarcarlos si no los necesitas.

3.  **Directorio de Instalación:**
    -   Selecciona el directorio de instalación. Como se mencionó, ``C:\xampp\`` es la opción recomendada en Windows.

4.  **Idioma y Bitnami:**
    -   Selecciona el idioma.
    -   El instalador podría ofrecer instalar software adicional a través de Bitnami para XAMPP (para instalar WordPress, Drupal, etc., fácilmente). Puedes desmarcar esta opción si solo necesitas el stack base.

5.  **Proceso de Instalación:**
    -   El instalador extraerá los archivos y configurará los componentes. Este proceso puede tardar unos minutos.
    -   Si tu firewall de Windows te pregunta si deseas permitir que Apache se comunique en redes privadas y/o públicas, permítelo (al menos para redes privadas).

6.  **Finalización de la Instalación:**
    -   Una vez completada la instalación, el asistente te preguntará si deseas iniciar el Panel de Control de XAMPP ahora. Marca la casilla y haz clic en "Finish".

Uso del Panel de Control de XAMPP:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
El Panel de Control de XAMPP es tu centro de mando para gestionar los servicios:

-   **Iniciar/Detener Servicios:** Verás una lista de módulos (Apache, MySQL, etc.). Haz clic en el botón "Start" junto a Apache y MySQL para iniciarlos. Si se inician correctamente, sus nombres se resaltarán en verde y se mostrarán los puertos que están utilizando (e.g., Apache: Port 80, 443; MySQL: Port 3306).
-   **Admin:** Al lado de cada módulo iniciado, hay un botón "Admin".
    -   Hacer clic en "Admin" para Apache abrirá ``http://localhost/dashboard/`` en tu navegador.
    -   Hacer clic en "Admin" para MySQL abrirá phpMyAdmin (``http://localhost/phpmyadmin/``).
-   **Config:** Permite acceder a archivos de configuración importantes de cada servicio (e.g., ``httpd.conf`` para Apache, ``php.ini`` para PHP, ``my.ini`` para MySQL).
-   **Logs:** Permite ver los archivos de log de errores y acceso de cada servicio, muy útiles para depurar problemas.
-   **Netstat:** Una herramienta útil para verificar qué puertos están en uso y por qué aplicación.

Verificación y Primeros Pasos:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
1.  **Verificar Apache:** Abre tu navegador y ve a ``http://localhost``. Deberías ver la página de bienvenida de XAMPP o el dashboard.
2.  **Verificar PHP:** Crea un archivo llamado ``info.php`` en ``C:\xampp\htdocs\`` con el siguiente contenido:

    .. code-block:: php

       <?php
       phpinfo();
       ?>

    Luego, navega a ``http://localhost/info.php``. Deberías ver una página detallada con toda la configuración de PHP. Por seguridad, elimina este archivo después de verificar.
3.  **Verificar MySQL y phpMyAdmin:** En el Panel de Control, haz clic en "Admin" para MySQL o navega directamente a ``http://localhost/phpmyadmin``. Deberías poder acceder a la interfaz de phpMyAdmin.


.. Consideraciones Importantes con XAMPP:
.. ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. -   **Seguridad:** XAMPP está configurado por defecto para ser un entorno de desarrollo fácil de usar, no para producción. Las contraseñas de MySQL son débiles o inexistentes por defecto. Si vas a exponer XAMPP a tu red local (no a Internet), considera cambiar la contraseña de root de MySQL y revisar otras configuraciones de seguridad.
.. -   **Virtual Hosts (Hosts Virtuales):** Para desarrollar múltiples proyectos, es altamente recomendable configurar Virtual Hosts en Apache. Esto te permite asignar un nombre de dominio local (e.g., ``proyecto1.local``, ``miapi.test``) a cada proyecto en lugar de acceder a ellos mediante ``http://localhost/proyecto1``. Esto simula mejor un entorno de producción y evita problemas con rutas de archivos.
..    -   La configuración de Virtual Hosts implica editar:
..        1.  ``C:\xampp\apache\conf\httpd.conf``: Descomentar la línea ``Include conf/extra/httpd-vhosts.conf``.
..        2.  ``C:\xampp\apache\conf\extra\httpd-vhosts.conf``: Añadir las directivas ``<VirtualHost>`` para cada proyecto.
..        3.  El archivo ``hosts`` de tu sistema operativo (``C:\Windows\System32\drivers\etc\hosts``) para mapear los dominios locales a ``127.0.0.1``.
.. -   **Archivo ``php.ini``:** Ubicado en ``C:\xampp\php\php.ini``. Algunas directivas comunes a modificar para desarrollo:
..    -   ``display_errors = On`` (Para ver errores en el navegador)
..    -   ``error_reporting = E_ALL`` (Reportar todos los tipos de errores)
..    -   ``memory_limit = 256M`` (O más, si tu aplicación lo requiere)
..    -   Habilitar extensiones PHP necesarias (e.g., ``extension=pdo_mysql``, ``extension=intl``, ``extension=gd``).
..    Recuerda reiniciar Apache desde el Panel de Control de XAMPP después de modificar ``php.ini`` o archivos de configuración de Apache.
