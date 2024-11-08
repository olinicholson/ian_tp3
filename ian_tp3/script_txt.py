def procesar_archivo_subtitulos(ruta_archivo):
    """
    Procesa un archivo de subtítulos en formato SRT y extrae solo el diálogo,
    eliminando números, marcas de tiempo, líneas vacías, etiquetas HTML como <i>, y guiones iniciales.
    
    :param ruta_archivo: Ruta al archivo de subtítulos (.txt o .srt).
    :return: Texto limpio con solo los diálogos, como una cadena.
    """
    import re
    
    # Leer todo el archivo
    with open(ruta_archivo, "r", encoding="utf-8") as archivo:
        lineas = archivo.readlines()
    
    texto_importante = []
    
    for linea in lineas:
        # Ignorar líneas que sean números, marcas de tiempo o estén vacías
        if re.match(r"^\d+$", linea.strip()) or "-->" in linea or linea.strip() == "":
            continue
        
        # Eliminar etiquetas como <i> y </i>
        linea_limpia = re.sub(r"<[^>]+>", "", linea.strip())
        
        # Eliminar guiones al principio de la línea
        linea_limpia = re.sub(r"^-+", "", linea_limpia).strip()
        
        # Agregar líneas de texto hablado limpias si no están vacías
        if linea_limpia:
            texto_importante.append(linea_limpia)
    
    # Unir las líneas filtradas con un salto de línea
    return "\n".join(texto_importante)

# Uso de la función
ruta_archivo = "Metegol.txt"
texto_limpio = procesar_archivo_subtitulos(ruta_archivo)

# Guardar el texto limpio en un nuevo archivo
with open("metegol_limpio.txt", "w", encoding="utf-8") as archivo_salida:
    archivo_salida.write(texto_limpio)

print("El texto limpio se ha guardado en 'metegol_limpio.txt'.")
