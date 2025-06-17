import time
import os
from capture import capture_frame
from segment import segment_image
from ascii import mask_to_ascii, clear_terminal

tmp_image = "tmp_frame.jpg"

print("🎥 ASCII camera active (Ctrl+C pour arrêter)\n")

try:
    while True:
        # 1. Capture une photo
        capture_frame(tmp_image)

        # 2. Segmente le premier plan
        mask = segment_image(tmp_image)

        # 3. Convertit en ASCII
        ascii_output = mask_to_ascii(mask, cols=150)  # ou 200 si ton terminal est large

        # 4. Affiche
        clear_terminal()
        print(ascii_output)

        # 5. Supprime l'image temporaire
        os.remove(tmp_image)


except KeyboardInterrupt:
    print("\n⏹️ Arrêt par l'utilisateur.")
