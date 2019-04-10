import glob
import cv2, sys, os
from math import copysign, log10

def HuMoments():
    
    showLogTransformedHuMoments = True

    database_images = glob.glob('images/*')
    image_test = len(database_images)
    database_images = database_images[:image_test]
    
    
    for filename in database_images:

        # Obtain filename from command line argument
        #filename = sys.argv[i]
        
        # Read image
        im = cv2.imread(filename,cv2.IMREAD_GRAYSCALE)
        
         # Threshold image
        _,im = cv2.threshold(im, 128, 255, cv2.THRESH_BINARY)

        # Calculate Moments
        moment = cv2.moments(im)

        # Calculate Hu Moments
        huMoments = cv2.HuMoments(moment)
        
        # Print Hu Moments
        print("{}: ".format(filename))
        
        for i in range(0,7):
            if showLogTransformedHuMoments:
                # Log transform Hu Moments to make
                # squash the range
                print("{:.5f}".format(-1*copysign(1.0,\
                        huMoments[i])*log10(abs(huMoments[i]))),\
                        )
            else:
                # Hu Moments without log transform
                print("{:.5f}".format(huMoments[i]))
        print()
        




