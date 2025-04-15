import cv2
import time
import threading
import numpy as np

# Liste pour stocker les timestamps des frappes
timestamps = []
bpm = 0
lock = threading.Lock()  # Verrou pour synchroniser l'accès aux timestamps et BPM
key = 0

# Fonction pour calculer le BPM
def calculate_bpm():
    global bpm
    if len(timestamps) > 1:
        if len(timestamps) > 6:
            timestamps.pop(0)
        intervals = [timestamps[i] - timestamps[i - 1] for i in range(1, len(timestamps))]
        average_interval = sum(intervals) / len(intervals)
        bpm = int(60 / average_interval)

# Fonction qui s'exécute dans le thread pour détecter les frappes et calculer le BPM
def bpm_detection_thread():
    global timestamps, bpm, key
    while True:
        time.sleep(0.1)  # Attendre un peu avant de vérifier (détection périodique)
        key = cv2.waitKey(0) & 0xFF
        if key == ord(' '):  # Touche espace
            current_time = time.time()
            # with lock:
            timestamps.append(current_time)

        # Calculer le BPM dans le thread
        # with lock:
            calculate_bpm()

# Fonction pour afficher le BPM à l'écran
def display_bpm(bpm, frame):
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, f"BPM: {bpm}", (50, 50), font, 1, (0, 255, 0), 2, cv2.LINE_AA)
    return frame

# Initialisation de la fenêtre OpenCV
cv2.namedWindow("BPM Detector")

# Démarrer le thread de détection du BPM
bpm_thread = threading.Thread(target=bpm_detection_thread, daemon=True)
bpm_thread.start()

# Capturer les événements de frappes
while True:
    # Capturer une image vide (juste pour avoir une fenêtre)
    frame = 255 * np.ones(shape=[500, 500, 3], dtype=np.uint8)

    # Afficher les instructions
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, "Press Space to record a beat", (50, 150), font, 1, (255, 0, 0), 2, cv2.LINE_AA)

    # Afficher le BPM
    with lock:
        frame = display_bpm(bpm, frame)

    # Afficher la fenêtre
    cv2.imshow("BPM Detector", frame)

    # Attendre un événement clavier
    # key = cv2.waitKey(1) & 0xFF

    # Si la touche Espace est pressée, enregistrer le timestamp
    # if key == ord(' '):  # Touche espace
    #     current_time = time.time()
    #     with lock:
    #         timestamps.append(current_time)

    # Si la touche 'q' est pressée, quitter
    # elif key == ord('q'):
    if key == ord('q'):
        break

# Fermer toutes les fenêtres OpenCV
cv2.destroyAllWindows()
