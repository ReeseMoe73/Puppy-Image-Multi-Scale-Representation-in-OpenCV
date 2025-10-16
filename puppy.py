import cv2
import numpy as np


#Import puppy, give image name and display window
color = cv2.imread("puppy.jpg", 1)
cv2.imshow("Image", color)
cv2.moveWindow("Image", 0, 0)
print(color.shape)

height, width, channels = color.shape

# Split the image into 3 channels (Blue,Green, Red)
b, g, r = cv2.split(color)

# Create a canvas specifying height width times 3 with 3 channels and 0-255 
rgb_split = np.empty((height, width * 3, 3), dtype='uint8')

# Split channels in a separate section
rgb_split[:, 0:width] = cv2.merge([b, b, b])
rgb_split[:, width:width*2] = cv2.merge([g, g, g])
rgb_split[:, width*2:width*3] = cv2.merge([r, r, r])

# Show channels next to each other
cv2.imshow("Channels", rgb_split)
cv2.moveWindow("Channels", 0, height)

cv2.waitKey(0)
cv2.destroyAllWindows()



# Create a 3d channel from the previous split puppy image
# Load split channel image
img = cv2.imread('BGR puppy.JPG', cv2.IMREAD_GRAYSCALE)

# Obtain dimensions
height, width = img.shape
width = width // 3  # Divide into 3 channels

# Slit image into B, G, R channels
b = img[:, 0:width]
g = img[:, width:2*width]
r = img[:, 2*width:3*width]

# Merge channels into a single color image
color_image = cv2.merge([b, g, r])

# Output and save the result
cv2.imshow("Merged puppy image", color_image)
cv2.imwrite("merged_puppy.jpg", color_image)
cv2.waitKey(0)
cv2.destroyAllWindows()



#Import merged puppy image and swap red channel wih green channel
#Import merged puppy, give image name and display window
color = cv2.imread("merged_puppy.jpg", 1)
cv2.imshow("Image2", color)
cv2.moveWindow("Image2", 0, 0)
print(color.shape)

height, width, channels = color.shape

# Split the image into 3 channels (Green,Red, Blue)
g, r, b = cv2.split(color)

# Create a canvas specifying height width times 3 with 3 channels and 0-255 
rgb_split = np.empty((height, width * 3, 3), dtype='uint8')

# Split channels in a separate section
rgb_split[:, 0:width] = cv2.merge([g, g, g])
rgb_split[:, width:width*2] = cv2.merge([r, r, r])
rgb_split[:, width*2:width*3] = cv2.merge([b, b, b])

# Show channels next to each other
cv2.imshow("Channels", rgb_split)
cv2.moveWindow("Channels", 0, height)

cv2.waitKey(0)
cv2.destroyAllWindows()
