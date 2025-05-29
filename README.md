# Curso de Introducción a la Programación con PHP

Este repositorio contiene el material para un curso de introducción a la programación utilizando el lenguaje PHP. El curso está diseñado para guiar a los estudiantes desde los conceptos fundamentales de la programación hasta temas más específicos de PHP como la manipulación de formularios, el manejo de archivos y el uso de sesiones.

## Contenido del Curso

El curso se estructura en varios módulos, cubriendo los siguientes temas principales:

*   **Introducción:**
    *   ¿Qué es la programación?
    *   Introducción a PHP
    *   Configuración del entorno de desarrollo
    *   Tu primer script en PHP
*   **Fundamentos de PHP:**
    *   Variables y Tipos de Datos
    *   Estructuras de Control (condicionales y bucles)
    *   Arrays y Funciones
*   **Desarrollo Web con PHP:**
    *   Manipulación de Formularios
    *   Manejo de Archivos
    *   Sesiones y Cookies
*   **Entornos de Pruebas:**
    *   Configuración de entornos locales (ej. XAMPP)
    *   Configuración de entornos remotos (ej. ByetHost)

## Requisitos Previos

Para seguir este curso, se recomienda tener:

*   Conocimientos básicos de informática y navegación web.
*   Un editor de texto o Entorno de Desarrollo Integrado (IDE), como VS Code, Sublime Text, PhpStorm, etc.
*   Un servidor web local (como XAMPP, WAMP, MAMP) instalado, o acceso a un servicio de hosting que soporte PHP.
*   PHP instalado en tu sistema si no utilizas un paquete como XAMPP.

## Cómo Usar este Repositorio

1.  **Clonar el Repositorio:**
    ```shell
    git clone <URL_DEL_REPOSITORIO_AQUI>
    ```
    (Reemplaza `<URL_DEL_REPOSITORIO_AQUI>` con la URL real del repositorio si lo subes a una plataforma como GitHub/GitLab).

2.  **Navegar el Contenido:**
    *   Los archivos fuente del curso se encuentran en la carpeta `source/` en formato reStructuredText (`.rst`). Puedes leerlos directamente.

3.  **Construir la Documentación (Opcional - Si se usa Sphinx):**
    Este proyecto parece estar configurado para usar Sphinx para generar una documentación más navegable (HTML, PDF, etc.).
    *   Asegúrate de tener Python y `pip` instalados en tu sistema.
    *   Instala las dependencias del proyecto:
        ```shell
        pip install -r requirements.txt
        ```
    *   Construye la documentación (desde la raíz del proyecto):
        *   En Linux/macOS:
            ```shell
            make html
            ```
        *   En Windows:
            ```shell
            make.bat html
            ```
    *   La documentación generada en formato HTML estará disponible en la carpeta `docs/html/`. Abre `docs/html/index.html` en tu navegador.

## Estructura del Proyecto

*   `README.md`: Este archivo.
*   `source/`: Contiene los archivos fuente del curso en formato reStructuredText (`.rst`), así como archivos estáticos (CSS, imágenes, JS) y scripts auxiliares de Python.
*   `docs/`: Carpeta donde se genera la documentación compilada por Sphinx (si se construye).
*   `Makefile` y `make.bat`: Scripts para automatizar tareas comunes, como la construcción de la documentación con Sphinx.
*   `requirements.txt`: Lista las dependencias de Python necesarias para el proyecto (principalmente Sphinx y sus extensiones).
*   `conf.py`: Archivo de configuración de Sphinx, ubicado en `source/conf.py`.
