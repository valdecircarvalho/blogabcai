import os
import imageio.v3 as iio

def compress_images(directory, output_directory):
    # Verifica se o diretório de saída existe, se não, cria
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    
    # Percorre todos os arquivos no diretório fornecido
    for filename in os.listdir(directory):
        if filename.endswith(('.png', '.jpg', '.jpeg', '.webp')):  # Adicione outros formatos se necessário
            file_path = os.path.join(directory, filename)
            output_path = os.path.join(output_directory, filename)
                     
            # Lê a imagem
            image = iio.imread(file_path)
            
            # Salva a imagem em formato PNG para compressão lossless
            iio.imwrite(output_path, image, format='PNG')


# Definição dos diretórios de entrada e saída
input_directory = 'C:/Users/valde/OneDrive/workdir/projetos/blogabcai/content/img'
output_directory = 'C:/Users/valde/OneDrive/workdir/projetos/blogabcai/img-fix'

compress_images(input_directory, output_directory)
