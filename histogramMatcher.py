import cv2 as cv
import numpy as np

##def histogram_match_from_beginning(query_image):

def histogram_match(query_image, shape_matched_images, method):
    src_base = query_image
    hsv_base = cv.cvtColor(src_base, cv.COLOR_BGR2HSV)
    print('Scores :')
    for image in shape_matched_images:
        hsv_test1 = cv.cvtColor(image, cv.COLOR_BGR2HSV)

        h_bins = 50
        s_bins = 60
        histSize = [h_bins, s_bins]

        # hue varies from 0 to 179, saturation from 0 to 255
        h_ranges = [0, 180]
        s_ranges = [0, 256]
        ranges = h_ranges + s_ranges # concat lists

        # Use the 0-th and 1-st channels
        channels = [0, 1]


        hist_base = cv.calcHist([hsv_base], channels, None, histSize, ranges, accumulate=False)
        cv.normalize(hist_base, hist_base, alpha=0, beta=1, norm_type=cv.NORM_MINMAX)
        hist_test1 = cv.calcHist([hsv_test1], channels, None, histSize, ranges, accumulate=False)
        cv.normalize(hist_test1, hist_test1, alpha=0, beta=1, norm_type=cv.NORM_MINMAX)

        base_test1 = cv.compareHist(hist_base, hist_test1, method)

        print(base_test1)
