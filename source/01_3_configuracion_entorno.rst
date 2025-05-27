=====================================================
1.3 Configuración del Entorno de Desarrollo Local
=====================================================

Para desarrollar y probar aplicaciones PHP, es esencial configurar un entorno de desarrollo local que simule un servidor web real. Este entorno típicamente incluye:

-   Un **Servidor Web:** Software que gestiona las solicitudes HTTP y sirve las páginas web. Apache y Nginx son los más comunes.
-   El **Intérprete de PHP:** El motor que procesa el código PHP.
-   Un **Sistema de Gestión de Bases de Datos (SGBD):** Como MySQL, MariaDB o PostgreSQL, para almacenar y gestionar datos.

Existen varias formas de configurar este stack:

Opciones de Entornos de Desarrollo Integrados (Stacks):
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Para simplificar la instalación y gestión de estos componentes, se utilizan paquetes de software integrados como XAMPP, WAMP, MAMP o Laragon.

-   **XAMPP:** Una solución multiplataforma popular (Windows, Linux, macOS) que incluye Apache, MariaDB (compatible con MySQL), PHP y Perl.
    1.  **Descarga:** Obtener el instalador desde `el sitio web oficial de Apache Friends <https://www.apachefriends.org>`_.
    2.  **Instalación:** Ejecutar el instalador y seguir las instrucciones. Se recomienda instalarlo en una ruta sin espacios (e.g., ``C:\xampp``).
    3.  **Panel de Control:** Utilizar el panel de control de XAMPP para iniciar/detener los módulos de Apache y MySQL.
    4.  **Verificación:** Acceder a ``http://localhost`` en un navegador. Debería mostrar la página de bienvenida de XAMPP. Los proyectos PHP se colocan típicamente en el directorio ``xampp\htdocs\``.

-   **WAMP (Windows, Apache, MySQL, PHP):** Específico para Windows.
-   **MAMP (macOS, Apache, MySQL, PHP):** Específico para macOS.
-   **Laragon:** Un entorno de desarrollo moderno y rápido para Windows, popular entre desarrolladores Laravel pero útil para cualquier proyecto PHP.

Estructura de Directorios Típica (Ejemplo XAMPP en Windows):
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Al instalar XAMPP en ``C:\xampp``, la estructura relevante es:

.. code-block:: text

   C:\xampp\
   ├── apache\             # Archivos de configuración y módulos de Apache
   ├── mysql\              # Archivos de datos y configuración de MariaDB/MySQL
   │   └── data\           # Directorio de las bases de datos
   ├── php\                # Intérprete de PHP, extensiones y archivo php.ini
   ├── htdocs\             # Directorio raíz de documentos del servidor web
   │   ├── tu_proyecto_php\  # Aquí crearás las carpetas para tus aplicaciones
   │   └── index.php       # Archivo por defecto que se sirve (dashboard XAMPP)
   └── ...                 # Otros componentes y herramientas

El archivo de configuración principal de PHP es ``php.ini`` (ubicado en ``C:\xampp\php\php.ini``). Permite ajustar directivas como ``error_reporting``, ``display_errors``, ``memory_limit``, y habilitar/deshabilitar extensiones.

Editores de Código y Entornos de Desarrollo Integrados (IDEs):
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Un buen editor de código o IDE es crucial para la productividad.

-  **Visual Studio Code (VS Code):** Un editor de código fuente ligero pero potente, gratuito y multiplataforma, con un vasto ecosistema de extensiones para PHP.

   -  *Extensiones recomendadas para PHP:*

      -  ``PHP Intelephense`` (de Ben Mewburn) o ``PHP IntelliSense`` (de Felix Becker, aunque menos mantenido): Para autocompletado, análisis de código, y navegación.
      -  ``PHP Debug`` (de Xdebug): Para integración con Xdebug, permitiendo debugging paso a paso.
      -  ``php cs fixer`` o ``phpcbf``: Para formateo de código automático según estándares (PSR-12).
      -  ``GitLens``: Para una mejor integración con Git.

-  **PhpStorm:** Un IDE comercial muy completo y potente, específico para PHP, desarrollado por JetBrains. Ofrece refactorización avanzada, debugging integrado, soporte para frameworks, y muchas otras herramientas profesionales.


-  Otros editores populares incluyen Sublime Text, Atom, y NetBeans (que es un IDE completo).

Independientemente del stack o editor elegido, es vital asegurarse de que la versión de PHP instalada localmente coincida o sea compatible con la versión que se utilizará en el servidor de producción.