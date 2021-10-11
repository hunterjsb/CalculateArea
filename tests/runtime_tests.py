import numpy as np
import cv2 as cv
import time
from calculatearea import AreaEstimator

# create random color thresholds, make sure one will always be bigger than the other
lower, upper = np.reshape(np.sort(np.random.randint(255, size=6)), (2, 3))
np.random.shuffle(upper)
np.random.shuffle(lower)
print('the bounds are: ', lower, upper)
fill = np.random.randint(120, size=3, dtype=np.uint8)  # make sure the background isn't too bright


def check_pixels(img, l, u, f):

    for i, row in enumerate(img):
        for j, pixel in enumerate(row):
            B, G, R = pixel
            if (l[0]<B<u[0]) and (l[1]<G<u[1]) and (l[2]<R<u[2]):
                continue
            else:
                img[i, j] = f

    return img


pbp_time = 0
ga_time = 0  # get_area
for run in range(100):
    # create a random image
    random_image = np.random.randint(255, size=(679, 860, 3), dtype=np.uint8)

    # 100 tests, pixel-by-pixel
    t = 0
    for _ in range(10):
        begin = time.time()
        s = check_pixels(random_image, lower, upper, (0, 0, 0))
        d = time.time() - begin
        t += d
    print(f'run {run}: average pbp run time: {t/10} s')
    pbp_time += t/10

    # 100 test, get_area
    ae = AreaEstimator()
    ae.img = random_image

    t = 0
    for _ in range(10):
        begin = time.time()
        ae.get_area()
        d = time.time() - begin
        t += d
    print(f'run {run}: average get_area run time: {t/10} s')
    ga_time += t/10
print(f'pixel by pixel: {pbp_time/100}\nget_area {ga_time/100}')
print(f'get_area is {ga_time/pbp_time}x faster')

# get the mask of PartyRockFire
# s = check_pixels(cv.imread('PartyRockFire.jpeg'),
#                  np.array((0, 0, 118), dtype=np.uint8),
#                  np.array((100, 100, 255), dtype=np.uint8),
#                  (0, 0, 0))
#
# cv.imshow('selected pixels', s)
# cv.waitKey(0)
# cv.destroyAllWindows()
