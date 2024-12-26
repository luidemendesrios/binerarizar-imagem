from PIL import Image  #A biblioteca Pillow é usada para carregar e manipular imagens

# Função para carregar uma imagem
def load_image(image_path):
    try:
        img = Image.open(image_path)
        print("Imagem carregada com sucesso!")
        return img
    except FileNotFoundError:
        print("Erro: O arquivo não foi encontrado. Verifique o caminho fornecido.")
        return None
    except Exception as e:
        print(f"Erro ao carregar a imagem: {e}")
        return None

# Função para converter uma imagem colorida para tons de cinza
def convert_to_gray(image):
    # Criando uma nova imagem em tons de cinza
    # O modo 'L' indica que a imagem será em tons de cinza (luminance), com 8 bits por pixel.
    # O método .size do objeto 'image' retorna uma tupla (largura, altura) da imagem original.
    gray_image = Image.new('L', image.size)
    # Início de um loop for que iterará através de cada coluna da imagem.
    for x in range(image.width):
        # Loop interno que iterará através de cada linha da imagem.
        for y in range(image.height):
            # Obtendo o pixel na posição (x, y)
            # O método .getpixel((x, y)) retorna os valores de vermelho (r), verde (g) e azul (b) para o pixel na posição (x, y).
            r, g, b = image.getpixel((x, y))
            # Calculando o valor de cinza com a fórmula de luminance.
            # A fórmula (0.299*R + 0.587*G + 0.114*B) é uma maneira padrão de converter cores RGB para um valor de luminância.
            # O uso da função int() garante que o resultado seja um inteiro.
            gray_value = int(0.299 * r + 0.587 * g + 0.114 * b)
            # Colocando o pixel na imagem em tons de cinza
            # O método .putpixel((x, y), valor) insere o valor de cinza calculado na posição (x, y) da nova imagem.
            gray_image.putpixel((x, y), gray_value)
    # Após processar todos os pixels, a função retorna a nova imagem em tons de cinza.
    return gray_image

# Função para binarizar uma imagem em tons de cinza
def convert_to_binary(gray_image, threshold=127):
    """
    Esta função recebe uma imagem em tons de cinza e um valor de threshold (limite) e retorna
    uma nova imagem binarizada. Pixels com valor acima do threshold serão definidos como branco (255),
    e aqueles com valor igual ou abaixo do threshold serão definidos como preto (0).
    O parâmetro 'gray_image' é um objeto da classe Image do Pillow, que representa a imagem em tons de cinza.
    O parâmetro 'threshold' é opcional e tem um valor padrão de 127.
    """
    # Criando uma nova imagem binária
    # O modo '1' indica que a imagem será binária (1-bit pixels, preto e branco, também conhecido como modo bitmap).
    # O método .size do objeto 'gray_image' retorna uma tupla (largura, altura) da imagem original em tons de cinza.
    binary_image = Image.new('1', gray_image.size)
    # Início de um loop for que iterará através de cada coluna da imagem em tons de cinza.
    for x in range(gray_image.width):
        # Loop interno que iterará através de cada linha da imagem.
        for y in range(gray_image.height):
            # Obtendo o valor de cinza do pixel na posição (x, y) da imagem em tons de cinza.
            # O método .getpixel((x, y)) é usado para obter o valor do pixel.
            # Obtendo o valor de cinza do pixel
            gray_value = gray_image.getpixel((x, y))
           
            # Binarizando o valor com base no threshold fornecido.
            # Se o valor do pixel em tons de cinza for maior que o threshold, ele será definido como branco (255).
            # Caso contrário, será definido como preto (0).
            binary_value = 255 if gray_value > threshold else 0

            # Colocando o pixel binarizado na nova imagem.
            # O método .putpixel((x, y), valor) é usado para definir o valor do pixel na posição (x, y) da nova imagem.
            binary_image.putpixel((x, y), binary_value)
    return binary_image

# Função para mostrar as imagens lado a lado

def show_images(images, titles):
    """
    Esta função recebe duas listas: 'images', que contém os objetos de imagem que deseja exibir,
    e 'titles', que contém os títulos correspondentes para cada imagem.
    A função combina as imagens lado a lado e mostra o resultado final.
    Os objetos de imagem são esperados estar no formato suportado pelo Pillow.
    """
    # List comprehension para obter a largura de cada imagem.
    widths = [i.width for i in images]
    # List comprehension para obter a altura de cada imagem.
    heights = [i.height for i in images]
    # Calcula a largura total necessária para colocar todas as imagens lado a lado.
    total_width = sum(widths)
    # Obtém a maior altura entre todas as imagens para definir a altura da imagem resultante.
    max_height = max(heights)

    # Criando uma nova imagem vazia no modo RGB com o tamanho total calculado.
    # O modo 'RGB' indica que a imagem resultante será colorida.
    new_image = Image.new('RGB', (total_width, max_height))

    # Inicializa um offset (deslocamento) na direção horizontal para saber onde colar a próxima imagem.
    x_offset = 0

    # Loop para iterar sobre cada imagem na lista.
    for im in images:
        # Garantir que todas as imagens estejam no modo RGB

        # Verifica se a imagem atual está no modo RGB. Se não estiver, converte para esse modo.
        # Isso é necessário porque a função .paste exige que a imagem colada esteja no mesmo modo da imagem de destino
        if im.mode != 'RGB':
            im = im.convert('RGB') 

        # Cola a imagem atual 'im' na nova imagem 'new_image' na posição (x_offset, 0).
        # O segundo argumento do .paste é a posição onde a imagem será colada.
        new_image.paste(im, (x_offset, 0))

        # Atualiza o offset horizontal para a próxima imagem.
        # O offset é atualizado somando a largura da imagem atual.
        x_offset += im.width

    # Exibe a nova imagem composta que contém todas as imagens lado a lado.
    new_image.show()

# Caminho para a imagem no computador
image_path = "C:/Users/Luide/Documents/esquilo.jpg"

# Carregar a imagem colorida
image_color = load_image(image_path)

if image_color:
    # Converter para tons de cinza
    image_gray = convert_to_gray(image_color)

    # Converter para binária
    image_binary = convert_to_binary(image_gray)

    # Mostrar as imagens lado a lado
    show_images([image_color, image_gray, image_binary], ['Colorida', 'Tons de Cinza', 'Binarizada'])
