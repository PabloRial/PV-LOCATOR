import requests #solicitudes url
import os

def download_image(lat, lon, zoom, size, scale, api_key, index, total, output_folder):
    """Descarga una imagen de alta resolución de Google Maps Static API."""
    url = f"https://maps.googleapis.com/maps/api/staticmap?center={lat},{lon}&zoom={zoom}&size={size}&scale={scale}&maptype=satellite&key={api_key}"
    print(f"Descargando imagen {index + 1} de {total}...")
    response = requests.get(url)

    if response.status_code == 200:
        try:
            output_file = os.path.join(output_folder, f'image_{index + 1}.png')
            with open(output_file, 'wb') as file:
                file.write(response.content)
            print(f"Imagen {index + 1} de {total} descargada y guardada como {output_file}")
        except Exception as e:
            print(f"Error al guardar la imagen descargada {index + 1}: {e}")
    else:
        print(f"Error al descargar la imagen {index + 1} de {total}: {response.status_code}")

def main():
    # Configuracion  de los parámetros
    api_key =   # Se completa con la key de la API de Google Maps 
    zoom = 19  # Ajuste del zoom 
    size = '6400x6400'  # Tamaño imagen
    scale = 4  # Aumenta el tamaño de la imagen (1, 2 o 4)

    output_folder = #Dirección de la carpeta en la que se guardaran las fotos
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Definir la región de interés (ROI) se define la esquina superior izquierda y la inferior derecha
    lat_start = 41.6703231663762
    lat_end =  41.62356706965572     #lat_start - (0.00135 * 5)  
    lon_start =  -4.761544664783662
    lon_end = -4.699403250818031 #lon_start + (0.00176 * 5)  

    # Paso ajustado para evitar redundancia para zoom=19
    lat_step = 0.00135  # Paso en latitud
    lon_step = 0.00176  # Paso en longitud

    lat = lat_start
    total_images = 0

    # Calcular el total de imágenes
    while lat > lat_end:  # Nota: decrementamos latitud
        lon = lon_start
        while lon < lon_end:
            total_images += 1
            lon += lon_step
        lat -= lat_step  # Nota: decrementamos latitud

    print(f"Se estima que se descargarán un total de {total_images} imágenes.")

    lat = lat_start
    index = 0

    while lat > lat_end:  # Nota: decrementamos latitud
        lon = lon_start
        while lon < lon_end:
            download_image(lat, lon, zoom, size, scale, api_key, index, total_images, output_folder)
            lon += lon_step
            index += 1
        lat -= lat_step  # Nota: decrementamos latitud

if __name__ == '__main__':
    main()