import cv2
import time
import numpy as np

# Liste pour stocker les timestamps des frappes
timestamps = []
bpm = 0

# Fonction pour calculer le BPM
def calculate_bpm():
    if len(timestamps) > 1:
        intervals = [timestamps[i] - timestamps[i - 1] for i in range(1, len(timestamps))]
        average_interval = sum(intervals) / len(intervals)
        return int(60 / average_interval)
    return 0

# Fonction pour afficher le BPM à l'écran
def display_bpm(bpm, frame):
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, f"BPM: {bpm}", (50, 50), font, 1, (0, 255, 0), 2, cv2.LINE_AA)
    return frame

# Initialisation de la fenêtre OpenCV
cv2.namedWindow("BPM Detector")

# Capturer les événements de frappes
while True:
    # Capturer une image vide (juste pour avoir une fenêtre)
    frame = 255 * np.ones(shape=[500, 500, 3], dtype=np.uint8)

    # Afficher les instructions
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, "Press Space to record a beat", (50, 150), font, 1, (255, 0, 0), 2, cv2.LINE_AA)

    # Afficher le BPM
    frame = display_bpm(bpm, frame)

    # Afficher la fenêtre
    cv2.imshow("BPM Detector", frame)

    # Attendre un événement clavier
    key = cv2.waitKey(1) & 0xFF

    # Si la touche Espace est pressée, enregistrer le timestamp
    if key == ord(' '):  # Touche espace
        current_time = time.time()
        timestamps.append(current_time)

        # Calculer le BPM
        bpm = calculate_bpm()

    # Si la touche 'q' est pressée, quitter
    elif key == ord('q'):
        break

# Fermer toutes les fenêtres OpenCV
cv2.destroyAllWindows()
