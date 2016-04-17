import cv2

face_cascade = cv2.CascadeClassifier("./cascades/haarcascade_frontalface_alt.xml")

img = cv2.imread("kstn.jpg")

# resize hinh
base_height = 800
height, width = img.shape[:2]
new_width = int((width / float(height)) * base_height)
img = cv2.resize(img, (new_width, base_height))

# chuyen hinh sang muc xam
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# phat hien nhung vung chua khuon mat
faces = face_cascade.detectMultiScale(gray_img)
for (x,y,w,h) in faces:
    img = cv2.rectangle(img, (x-2, y-2),(x+w+2, y+h+2), (0, 0, 255), 2)

cv2. namedWindow("image")
cv2.imshow("image", img)
#cv2.imwrite("hinhdetected.jpg", img)
cv2.waitKey(0)
cv2.destroyAllWindows()