from PIL import Image, ImageDraw, ImageFont

# Cria uma imagem em branco
width, height = 800, 600  # Tamanho da imagem
image = Image.new('RGB', (width, height), color='white')
draw = ImageDraw.Draw(image)

# Adiciona um fundo simples
draw.rectangle([(0, 0), (width, height)], fill='lightblue')

# Adiciona elementos como a dona de casa e utensílios
# Exemplo: desenha uma figura de uma dona de casa
draw.rectangle([(200, 300), (300, 500)], fill='pink')  # corpo
draw.rectangle([(230, 300), (270, 350)], fill='gray')  # cabeça
draw.line([(200, 380), (300, 380)], fill='black', width=2)  # linha do avental

# Adiciona alguns utensílios ou objetos domésticos
draw.rectangle([(320, 400), (380, 440)], fill='yellow')  # panela
draw.rectangle([(250, 450), (290, 500)], fill='green')  # planta

# Adiciona texto descritivo
font = ImageFont.truetype("arial.ttf", 36)
draw.text((50, 50), "Dona de casa trabalhando", fill='black', font=font)

# Salva a imagem
image.save("donadecasa_trabalhando.png")

# Mostra a imagem (opcional, dependendo do ambiente de execução)
image.show()
