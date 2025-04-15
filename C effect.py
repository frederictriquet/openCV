import cv2 as cv
import numpy as np

capture = cv.VideoCapture(0)# + cv.CAP_DSHOW)


WIDTH, HEIGHT = 800, 600
capture.set(cv.CAP_PROP_FRAME_WIDTH, WIDTH)
capture.set(cv.CAP_PROP_FRAME_HEIGHT, HEIGHT)
font = cv.FONT_HERSHEY_SIMPLEX
cell_width, cell_height = 12, 12
new_width, new_height = int(WIDTH / cell_width), int(HEIGHT / cell_height)

k=None
isTrue, previous = capture.read()
isTrue, previous = capture.read()
isTrue, previous = capture.read()
isTrue, previous = capture.read()

while k != 27:
    isTrue, frame = capture.read()

    # bitwise = cv.compare(frame, previous, cmpop=cv.CMP_EQ)

    black_window = np.zeros((HEIGHT, WIDTH, 3), np.uint8)

    small_image = cv.resize(frame, (new_width, new_height), interpolation=cv.INTER_NEAREST)

    for i in range(new_height):
        for j in range(new_width):
            color = small_image[i, j]
            B = int(color[0])
            G = int(color[1])
            R = int(color[2])

            coord = (j * cell_width + cell_width, i * cell_height)

            cv.circle(black_window, coord, 5, (B, G, R), 2)
            # cv.circle(black_window, coord, 5, (0, G, 0), 2)
            # cv.circle(black_window, coord, 5, (0, G, 0), -1)
            # cv.circle(black_window, coord, 5, (B, G, R), -1)

            # cv.line(black_window, coord, (coord[0] + 8, coord[1]), (0, G, 0), 1)
            # cv.line(black_window, (coord[0] + 4, coord[1] - 4), (coord[0] + 4, coord[1] + 4), (0, G, 0), 1)

            # cv.putText(black_window, 'X', coord, font, 0.4, (B, G, R), 1, cv.LINE_AA)



    cv.imshow('test', black_window)

    previous = frame

    k = cv.waitKey(20)

capture.release()
cv.destroyAllWindows()
