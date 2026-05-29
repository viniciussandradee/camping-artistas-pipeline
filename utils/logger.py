from datetime import datetime

def log(tipo, mensagem):
    agora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    print(f"[{agora}] [{tipo.upper()}]: {mensagem}")
