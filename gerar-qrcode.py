import qrcode
from PIL import Image, ImageDraw, ImageFont
import json

with open("config.json", "r", encoding="utf-8") as f:
  config = json.load(f)

titulo=config.get("titulo", "Página")

def gerar_qrcode_com_coracao_e_texto(dados, texto=titulo, tamanho=450, coracao_tamanho=120):
    qr = qrcode.QRCode(
        version=5,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(dados)
    qr.make(fit=True)

    img_qr = qr.make_image(fill_color="black", back_color="white").convert("RGB")

    draw = ImageDraw.Draw(img_qr)
    largura, altura = img_qr.size

    cx, cy = largura // 2, altura // 2
    box_size = 10

    # Coração 12x12
    matriz_coracao = [
        [0,0,1,1,0,0,0,0,1,1,0,0],
        [0,1,1,1,1,0,0,1,1,1,1,0],
        [1,1,1,1,1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1,1,1,1,1],
        [0,1,1,1,1,1,1,1,1,1,1,0],
        [0,0,1,1,1,1,1,1,1,1,0,0],
        [0,0,0,1,1,1,1,1,1,0,0,0],
        [0,0,0,0,1,1,1,1,0,0,0,0],
        [0,0,0,0,0,1,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0],
    ]

    start_x = cx - (len(matriz_coracao[0]) * box_size) // 2
    start_y = cy - (len(matriz_coracao) * box_size) // 2

    for y, linha in enumerate(matriz_coracao):
        for x, val in enumerate(linha):
            if val == 1:
                px1 = start_x + x * box_size
                py1 = start_y + y * box_size
                px2 = px1 + box_size
                py2 = py1 + box_size
                draw.rectangle([px1, py1, px2, py2], fill="red")

    altura_texto = 40
    nova_imagem = Image.new("RGB", (largura, altura + altura_texto), "white")
    nova_imagem.paste(img_qr, (0,0))

    draw_novo = ImageDraw.Draw(nova_imagem)

    # Tenta fonte Courier New Bold, ou Arial Bold, ou default
    try:
        fonte = ImageFont.truetype("courbd.ttf", 30)  # Courier New Bold
    except:
        try:
            fonte = ImageFont.truetype("arialbd.ttf", 30)  # Arial Bold
        except:
            fonte = ImageFont.load_default()

    bbox = draw_novo.textbbox((0, 0), texto, font=fonte)
    w = bbox[2] - bbox[0]
    h = bbox[3] - bbox[1]

    pos_x = (largura - w) // 2
    pos_y = altura + (altura_texto - h) // 2

    draw_novo.text((pos_x, pos_y), texto, fill="black", font=fonte)

    return nova_imagem

if __name__ == "__main__":
    dados = "https://julia-eduardo.onrender.com/"
    img = gerar_qrcode_com_coracao_e_texto(dados)
    img.show()
    img.save("qrcode_coracao.png")
