# instalar o pyqrcode e o qrcode antes de rodar o codigo

import pyqrcode

# Dados de contato
nome = "Seu Nome"
empresa = "Sua Empresa"
email = "seuemail@suaempresa.com"
telefone = "+55 11 1234-5678"

# Concatenação dos dados
dados_contato = f"BEGIN:VCARD\nVERSION:3.0\nFN:{nome}\nORG:{empresa}\nEMAIL:{email}\nTEL;TYPE=CELL:{telefone}\nEND:VCARD"

# Criação do QR Code
qr_code = pyqrcode.create(dados_contato)

# Salva o QR Code em um arquivo PNG
qr_code.png("contato.png", scale=10)
