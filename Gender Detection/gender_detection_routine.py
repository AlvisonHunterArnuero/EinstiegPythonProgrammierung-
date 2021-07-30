import cv2
import cvlib as cv
import numpy as np
from numpy.lib.type_check import imag

# first, assign the image that we'll work with in a variable
# img = cv2.imread("henry_cavill.png")
# img = cv2.imread("morrison.jpeg")
img = cv2.imread("wonderwoman.jpeg")

# call the detect_face method to get coordinates & face boundaries
# faces: list of list containing bounding box co-ordinates for each detected face.
# confidences: list of confidence scores for each detected face.
faces_lst, confidence = cv.detect_face(img)

# The padding from the center to the edges of the face
padding = 20

for i in faces_lst:
    # Getting initial coordinates for the face shape
    (x, y) = max(0, i[0]-padding), max(0, i[1]-padding)
    (x2, y2) = min(img.shape[1]-1, i[2] +
                   padding), min(img.shape[0]-1, i[3]+padding)

    # Drawing a rectangle around the face of the subject
    # top left corner of rectangle
    start_point = (x, y)
    
    # bottom right corner of rectangle
    end_point = (x2, y2)
    
    # Red color in BGR
    color = (0, 0, 255)
    
    # Line thickness in px
    thickness = 2
    cv2.rectangle(img, start_point, end_point, color, thickness)
    
    # Cropping the image region that  we will highlight on the photo
    crop = np.copy(img[y:y2, x:x2])
    
    # get label to get the gender(male, female) &  its levels of confidence
    (label, confidence) = cv.detect_gender(crop)
    
    # from the level of confidence results, let's take the highest value
    idx = np.argmax(confidence)
    
    # let's change the casing for this label to Uppercase, shall we?
    label = label[idx].upper()
    
    # Preparing the label that we will add to the img, mostly formatting
    label = "{}: {:.2f}%".format(label, confidence[idx] * 100)
    Y = y - 10 if y - 10 > 10 else y + 10

    # Adding text on top of the img(BGR format for text color)
    cv2.putText(img, label, (y, Y),
                cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 255), 3)

# Create the window with a title on it
cv2.imshow("Gender Detection", img)

# display this windows until the user hits a key
cv2.waitKey(0)

# Let us destroy all these element to free up memory
cv2.destroyAllWindows()

print("-"*80)
print("All set, folks! Don't forget  to  Subscribe, buddies!")
print("-"*80)
