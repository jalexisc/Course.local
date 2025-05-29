import subprocess
import os
import fileinput # Para modificar archivos in-place

# Directorios de origen y construcción
source_dir = 'source'
build_dir = 'docs'
output_html_dir = os.path.join(build_dir, 'html')
old_static_dir = os.path.join(output_html_dir, '_static')
new_static_dir = os.path.join(output_html_dir, 'static')

print("Iniciando la compilación de Sphinx...")

# Comando para compilar Sphinx (equivalente a sphinx-build -b html source docs)
# Usamos el mismo patrón que make.bat usa para ser consistentes
command = ['sphinx-build', '-M', 'html', source_dir, build_dir]

try:
    # Ejecutar el comando de compilación
    result = subprocess.run(command, cwd='.', check=True, capture_output=True, text=True)
    print("Compilación de Sphinx completada.")
    print("Salida de Sphinx:")
    print(result.stdout)
    if result.stderr:
        print("Errores/Advertencias de Sphinx:")
        print(result.stderr)

    # Renombrar la carpeta _static a static
    if os.path.exists(old_static_dir):
        print(f"Renombrando '{old_static_dir}' a '{new_static_dir}'...")
        # Check if the destination directory exists and remove it if it does
        if os.path.exists(new_static_dir):
            print(f"Eliminando directorio existente '{new_static_dir}'...")
            # Use subprocess to remove the directory on Windows
            try:
                subprocess.run(['rmdir', '/S', '/Q', new_static_dir], check=True, shell=True)
                print(f"Directorio '{new_static_dir}' eliminado.")
            except subprocess.CalledProcessError as e:
                print(f"Error al eliminar el directorio '{new_static_dir}': {e}")
                # Depending on how critical this is, you might want to exit or raise the exception
                # For now, let's just print and continue, the os.rename will likely fail again if removal failed.
            except FileNotFoundError:
                 print(f"Error: rmdir command not found. Make sure it's in your PATH.")


        os.rename(old_static_dir, new_static_dir)
        print("Renombrado completado.")
    else:
        print(f"El directorio '{old_static_dir}' no se encontró. Saltando el paso de renombrado.")

    # Modificar archivos HTML para actualizar las referencias estáticas
    print(f"Actualizando enlaces estáticos en archivos HTML en '{output_html_dir}'...")
    
    for root, _, files in os.walk(output_html_dir):
        for file in files:
            if file.endswith(".html"):
                filepath = os.path.join(root, file)
                # Usar fileinput para modificar el archivo in-place
                # Use fileinput para modificar el archivo in-place
                # Specify utf-8 encoding to handle potential character issues
                with fileinput.FileInput(filepath, inplace=True, encoding='utf-8') as f:
                    for line in f:
                        # Reemplazar _static/ por static/ en cada línea
                        #rstrip() es importante para no añadir saltos de línea adicionales
                        print(line.replace("_static/", "static/"), end='')
                # fileinput cierra y renombra el archivo temporal automáticamente

    print("Actualización de enlaces estáticos completada.")
    print("Proceso de compilación y modificación finalizado.")

except subprocess.CalledProcessError as e:
    print(f"Error durante la compilación de Sphinx: {e}")
    print("Salida estándar:")
    print(e.stdout)
    print("Salida de error:")
    print(e.stderr)
except FileNotFoundError:
    print("Error: No se encontró el comando 'sphinx-build'. Asegúrate de que Sphinx esté instalado y accesible en tu PATH.")
except Exception as e:
    print(f"Ocurrió un error: {e}")
