# images to video (windows 7,10?)

import cv2

n = 429    # number of images
image = cv2.imread('imageslocation!!!!!!\img0.png')
height, width, layers = image.shape
video = cv2.VideoWriter('movielocation!!!!!\movie_name.avi', -1,5,(width,height))
for i in range(n):
    image = cv2.imread('movielocation!!!!!\img%d.png' % i)
    video.write(image)
    print(i)
cv2.destroyAllWindows()
video.release()

# cv2.destroyAllWindows()
# video.release()

# type these two last commands manually at the end
# select microsoft video 1