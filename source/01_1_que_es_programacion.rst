============================
1.1 ¿Qué es la Programación?
============================

La programación, en su esencia, es el arte y la ciencia de instruir a una computadora para que realice tareas específicas. Implica diseñar y escribir **código fuente** en un **lenguaje de programación**, que es un conjunto formal de reglas y símbolos que permiten a los humanos comunicar algoritmos a las máquinas. El resultado tangible de la programación es un **programa** o **software**, una secuencia de instrucciones lógicas que, una vez procesadas por la computadora, resuelven un problema, automatizan un proceso o proporcionan una funcionalidad.

Conceptos Fundamentales en Programación:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
- **Algoritmo:**
    Un algoritmo es una secuencia finita y bien definida de pasos lógicos y ordenados, diseñada para resolver un problema específico o realizar una computación. Es la "receta" que un programador traduce a código. Características clave de un algoritmo incluyen:
    - **Precisión:** Cada paso debe estar definido de forma inequívoca.
    - **Finitud:** Debe terminar después de un número finito de pasos.
    - **Efectividad:** Cada paso debe ser realizable.
    - **Entrada/Salida:** Generalmente toma cero o más entradas y produce una o más salidas.

- **Código Fuente (Source Code):**
    Es el conjunto de instrucciones escritas por un programador utilizando la sintaxis de un lenguaje de programación específico (e.g., PHP, Python, Java, C++). El código fuente es legible por humanos y sirve como el plano maestro del programa. Para que una computadora lo ejecute, debe ser traducido a un formato que la máquina pueda entender.

- **Traducción de Código: Compilación vs. Interpretación:**
    El proceso de convertir el código fuente legible por humanos en instrucciones ejecutables por la máquina se puede realizar principalmente de dos maneras:

    - **Compilación:** Un programa llamado **compilador** traduce *todo* el código fuente a **código máquina** (o un código intermedio como bytecode) de una sola vez, generando un archivo ejecutable independiente. Este ejecutable puede luego ser corrido directamente por el sistema operativo. Lenguajes como C, C++, Go y Rust son típicamente compilados.
        *Ventajas:* Generalmente resulta en una ejecución más rápida del programa.
        *Desventajas:* El proceso de compilación puede ser lento y el ejecutable es específico de la plataforma para la que se compiló.

    - **Interpretación:** Un programa llamado **intérprete** lee el código fuente línea por línea (o en pequeñas unidades) y lo ejecuta directamente, traduciendo y ejecutando cada instrucción sobre la marcha. Lenguajes como PHP (en su modo clásico), Python, JavaScript y Ruby son típicamente interpretados.
        *Ventajas:* Mayor portabilidad del código fuente entre plataformas (siempre que haya un intérprete disponible), y un ciclo de desarrollo más rápido (sin paso de compilación explícito).
        *Desventajas:* Generalmente una ejecución más lenta en comparación con los lenguajes compilados, ya que la traducción ocurre durante el tiempo de ejecución.

    *Nota:* Algunos lenguajes, incluido PHP moderno, pueden usar una combinación de técnicas, como la compilación a un bytecode intermedio que luego es interpretado por una máquina virtual (e.g., Zend Engine en PHP).
