# images to video (windows 7, 10?)

import cv2

fps = 25   # number of frames per second desired
n =1490    # number of images

# At each imread and VideoWriter command type the absolute path of the images

image = cv2.imread('image_location!!!!!\img0.png')
height, width, layers = image.shape
print height, width, layers

video = cv2.VideoWriter('image_location!!!!!\movie_name.avi', -1, fps,(width,height))
for i in range(n):
    image = cv2.imread('image_location!!!!!\img%d.png' % i)
    video.write(image)
    print(i)
    
# cv2.destroyAllWindows()
# video.release()
 
# type these two last commands manually at the end
# select microsoft video 1