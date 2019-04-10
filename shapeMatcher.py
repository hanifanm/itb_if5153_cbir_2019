import cv2

def shapeMatcher():

    im1 = cv2.imread("images/F1.jpg",cv2.IMREAD_GRAYSCALE)
    im2 = cv2.imread("images/F2.jpg",cv2.IMREAD_GRAYSCALE)
    im3 = cv2.imread("images/F3.jpeg",cv2.IMREAD_GRAYSCALE)
    im4 = cv2.imread("images/F4.jpg",cv2.IMREAD_GRAYSCALE)
    im5 = cv2.imread("images/F5.jpeg",cv2.IMREAD_GRAYSCALE)
    im6 = cv2.imread("images/01.jpg",cv2.IMREAD_GRAYSCALE)

    m1 = cv2.matchShapes(im1,im1,cv2.CONTOURS_MATCH_I2,0)
    m2 = cv2.matchShapes(im1,im2,cv2.CONTOURS_MATCH_I2,0)
    m3 = cv2.matchShapes(im1,im3,cv2.CONTOURS_MATCH_I2,0)
    m4 = cv2.matchShapes(im1,im4,cv2.CONTOURS_MATCH_I2,0)
    m5 = cv2.matchShapes(im1,im5,cv2.CONTOURS_MATCH_I2,0)
    m6 = cv2.matchShapes(im1,im6,cv2.CONTOURS_MATCH_I2,0)

    print("Shape Distances Between \n-------------------------")

    print("F1.jpg dengan F1.jpg : {}".format(m1))
    print("F1.jpg dengan F2.jpg : {}".format(m2))
    print("F1.jpg dengan F3.jpeg : {}".format(m3))
    print("F1.jpg dengan F4.jpg : {}".format(m4))
    print("F1.jpg dengan F5.jpeg : {}".format(m5))
    print("F1.jpg dengan O1.jpg : {}".format(m6))


