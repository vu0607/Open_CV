import cv2
import imutils
#image = cv2.imread("105180399.jpg")

# Read image , gray image
""""
image = cv2.imread("105180399.jpg", cv2.IMREAD_GRAYSCALE)
# Show image
cv2.imshow("testImage",image)
# Stop screen to watch
cv2.waitKey()
# Close all windows
cv2.destroyAllWindows()
# Covert image to gray image
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
cv2.imshow("Gray image",gray_image)
cv2.waitKey()
cv2.destroyAllWindows()
"""
# Resize image
"""
image_rs = cv2.resize(image,dsize=None,fx = 0.5, fy = 0.5)
cv2.imshow("Resized image", image_rs)
cv2.waitKey()
cv2.destroyAllWindows()
"""

# Rotate image
"""
image_rotate = imutils.rotate(image,90)
cv2.imshow("Resized image", image_rotate)
cv2.waitKey()
cv2.destroyAllWindows()
"""
# Threshold function
"""
image_gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
# Apply threshold
ret, thresh_binary = cv2.threshold(image_gray, 127, 255, cv2.THRESH_BINARY )
cv2.imshow("Threshold binary image", thresh_binary)
cv2.waitKey()
cv2.destroyAllWindows()
"""
#Adaptive Threshold : Apply for dark image
#Two AThreshold : Mean and Gaussian

#Find image edges
#Apply for finding how many...in image,...
"""
gray_image = cv2.imread("105180399.jpg", 0)
edges = cv2.Canny(gray_image, threshold1= 100, threshold2= 200)
cv2.imshow("Image edges", edges)
cv2.waitKey()
cv2.destroyAllWindows()
"""
# Blur image, reduce image noise
# ksize la kich thuoc cua hinh vuong nho de quet lam mo anh
# kernel_width va kernel_height la so le, do mo cang cao khi so nay cang lon
# Chong nhieu, lam duong bien cua cac doi tuong lien nhau de lam contours cho de
"""
image = cv2.imread("105180399.jpg")
Blur_image = cv2.GaussianBlur(gray_image, ksize=(3,3), sigmaX=0)
cv2.imshow("Blur image",Blur_image)
cv2.waitKey()
cv2.destroyAllWindows()
"""
#Finding contours
# Contours la tap hop cac diem lien tuc tao thanh duong cong (curve, boundary), khong co khoang ho giua cac duong cong
# Trong opencv, viec tim contour la viec tim mot doi tuong mau trang tren nen den
# Tim doi tuong trong anh va dem so luong, tim bien so xe oto,...

#Face detection without deepLearning
#load the classifiers downloaded
"""
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
image = cv2.imread("105180399.jpg", 0)
faces = face_cascade.detectMultiScale(gray, 1.1, 4)
"""
#Show Camera
#frame la khung hinh doc duoc tu camera
#ret la ket qua tra ve
"""
camera_id = 0
cap = cv2.VideoCapture(camera_id)
while True:
# Read image
    ret, frame = cap.read()
# Show image
    cv2.imshow("Cam",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# Release camera
cap.release()
cv2.destroyAllWindows()
"""



