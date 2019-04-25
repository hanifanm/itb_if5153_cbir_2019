import cv2 as cv
import numpy as np
import glob

global codenames
codenames = []
global relevant_data
relevant_data = 0
def histogram_match_from_beginning(query,result_wanted):
    method=0
    query_image = cv.imread(query)
    global codenames
    codenames = []
    global relevant_data
    relevant_data = 0
    query_code = query.split('images/',1)[1][0:4]
    src_base = query_image
    hsv_base = cv.cvtColor(src_base, cv.COLOR_BGR2HSV)
    all_results = []
    all_distance = []
    database_images = glob.glob('images/*')
    image_test = len(database_images)
    database_images = database_images[:image_test]
    all_names = []
    print('Histogram Match Scores\n--------------------------------------------')
    for one_image in database_images:
        if query_code == one_image[7:11]:
            relevant_data = relevant_data + 1
        image = cv.imread(one_image)
        hsv_test1 = cv.cvtColor(image, cv.COLOR_BGR2HSV)

        h_bins = 50
        s_bins = 600
        histSize = [h_bins, s_bins]
#        histSize = [h_bins]

        # hue varies from 0 to 179, saturation from 0 to 255
        h_ranges = [0, 180]
        s_ranges = [0, 256]
        ranges = h_ranges + s_ranges # concat lists
#        ranges = h_ranges # concat lists

        # Use the 0-th and 1-st channels
        channels = [0, 2]
#        channels = [0]


        hist_base = cv.calcHist([hsv_base], channels, None, histSize, ranges, accumulate=False)
        cv.normalize(hist_base, hist_base, alpha=0, beta=1, norm_type=cv.NORM_MINMAX)
        hist_test1 = cv.calcHist([hsv_test1], channels, None, histSize, ranges, accumulate=False)
        cv.normalize(hist_test1, hist_test1, alpha=0, beta=1, norm_type=cv.NORM_MINMAX)

        base_test1 = cv.compareHist(hist_base, hist_test1, method)
        if method == 0:
            if base_test1 > 0.8:
                all_results.append(image)
                all_distance = np.append(all_distance, base_test1)
                all_names.append(one_image)
##        print(base_test1)

    new = np.argsort(all_distance)
    sorted_results = []
    counter = 0
    i = len(new)
    while i > 0:
        sorted_results.append(all_results[new[i-1]])
        codenames.append(all_names[new[i-1]][7:11])
        #print("Image: ",all_names[new[i-1]][7:11])
        print("Histogram Similarity: {}".format(all_distance[new[i-1]]))
        counter = counter + 1
        if counter == result_wanted:
            break
        i = i - 1
    return sorted_results

def get_codenames():
    return codenames

def get_relevant_data():
    return relevant_data

def histogram_match(query_image, shape_matched_images, result_wanted, prev_codenames):
    global codenames
    codenames = []
    method = 0
    src_base = query_image
    hsv_base = cv.cvtColor(src_base, cv.COLOR_BGR2HSV)
    all_results = []
    all_distance = []
    all_names = []
    print('Histogram Match Scores\n--------------------------------------------')
    counter = 0;
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
        if method == 0:
            if base_test1 > 0.8:
                all_results.append(image)
                all_distance = np.append(all_distance, base_test1)
                all_names.append(prev_codenames[counter])
        counter = counter + 1
##        print(base_test1)

    new = np.argsort(all_distance)
    sorted_results = []
    counter = 0
    i = len(new)
    while i > 0:
        sorted_results.append(all_results[new[i-1]])
        codenames.append(all_names[new[i-1]])
        print("Histogram Similarity: {}".format(all_distance[new[i-1]]))
        counter = counter + 1
        if counter == result_wanted:
            break
        i = i - 1
    return sorted_results
