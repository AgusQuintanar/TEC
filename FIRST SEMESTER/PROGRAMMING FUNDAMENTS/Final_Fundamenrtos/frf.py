from pathlib import Path

def ls(ruta = '/Users/agusquintanar/Desktop/Siil/'):
    return [arch.name for arch in Path(ruta).iterdir() if arch.is_file()]

print(ls())