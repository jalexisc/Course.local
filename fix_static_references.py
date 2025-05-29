#!/usr/bin/env python
"""
Script para reemplazar todas las referencias a '_static' por 'static' en los archivos HTML generados.
Este script debe ejecutarse después de la compilación de Sphinx.
"""

import os
import re
from pathlib import Path

def fix_static_references(html_dir):
    """Reemplaza todas las referencias a '_static' por 'static' en los archivos HTML"""
    html_dir = Path(html_dir)
    pattern = re.compile(r'(href|src)=["\']_static/')
    replacement = r'\1="static/'
    
    print(f"Corrigiendo referencias en: {html_dir}")
    count = 0
    
    for html_file in html_dir.glob('**/*.html'):
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Si hay referencias a _static, corregirlas
        if '_static/' in content:
            modified_content = pattern.sub(replacement, content)
            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(modified_content)
            count += 1
    
    print(f"Se corrigieron referencias en {count} archivos HTML")

if __name__ == "__main__":
    html_dir = "docs/html"
    fix_static_references(html_dir)
