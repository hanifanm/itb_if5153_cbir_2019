import cv2
import glob
import numpy as np

from skimage.feature import hog
from skimage import data, exposure

global codenames
codenames = []
global relevant_data
relevant_data = 0
def shapeMatcher(query_image, result_wanted):

    global codenames
    codenames = []
    global relevant_data
    relevant_data = 0
    query_code = query_image.split('images/',1)[1][0:4]

    database_images = glob.glob('images/*')
    image_test = len(database_images)
    database_images = database_images[:image_test]

    print("Shape Distances Between \n--------------------------------------------")
    query = cv2.imread(query_image,cv2.IMREAD_GRAYSCALE)
    all_results = []
    all_distance = []
    all_names = []
    for filename in database_images:
        if query_code == filename[7:11]:
            relevant_data = relevant_data + 1

        # Read image
        im = cv2.imread(filename,cv2.IMREAD_GRAYSCALE)

        m1 = cv2.matchShapes(query,im,cv2.CONTOURS_MATCH_I2,0)
        if m1 < 0.1:
            all_results.append(cv2.imread(filename))
            all_distance = np.append(all_distance, m1)
            all_names.append(filename)

    new = np.argsort(all_distance)
    sorted_results = []
    counter = 0
    for i in new:
        sorted_results.append(all_results[i])
        codenames.append(all_names[i][7:11])
        #print("Distance : {}".format(all_distance[i]), "Code: ", (all_names[i][7:11]))
        print("Shape Distance : {}".format(all_distance[i]))
        counter = counter + 1
        if counter == result_wanted:
            break
    return sorted_results
    #return all_results

def shapeMatcherAndHog(query_image, result_wanted):

    global codenames
    codenames = []
    global relevant_data
    relevant_data = 0
    query_code = query_image.split('images/',1)[1][0:4]

    database_images = glob.glob('images/*')
    image_test = len(database_images)
    database_images = database_images[:image_test]

    print("Shape Distances Between \n--------------------------------------------")
    query = cv2.imread(query_image)

    fd, query = hog(query, orientations=8, pixels_per_cell=(2, 2), cells_per_block=(1, 1), block_norm='L2-Hys', visualize=True, multichannel=True)
    ##query = exposure.rescale_intensity(query, in_range=(0, 10))

    all_results = []
    all_distance = []
    all_names = []
    for filename in database_images:
        if query_code == filename[7:11]:
            relevant_data = relevant_data + 1

        # Read image
        im = cv2.imread(filename)

        # Calculate HOG
        fd, hog_image = hog(im, orientations=8, pixels_per_cell=(2, 2), cells_per_block=(1, 1), block_norm='L2-Hys', visualize=True, multichannel=True)
        ##hog_image_rescaled = exposure.rescale_intensity(hog_image, in_range=(0, 10))

        m1 = cv2.matchShapes(query,hog_image,cv2.CONTOURS_MATCH_I2,0)
        print('Processing : {} with value {}'.format(filename, m1))
        if m1 < 10:
            all_results.append(cv2.imread(filename))
            all_distance = np.append(all_distance, m1)
            all_names.append(filename)

    new = np.argsort(all_distance)
    sorted_results = []
    counter = 0
    for i in new:
        sorted_results.append(all_results[i])
        codenames.append(all_names[i][7:11])
        #print("Distance : {}".format(all_distance[i]), "Code: ", (all_names[i][7:11]))
        print("Shape Distance : {}, filename: {}".format(all_distance[i], all_names[i]))
        counter = counter + 1
        if counter == result_wanted:
            break
    return sorted_results
    #return all_results

def get_relevant_data():
    return relevant_data

def get_codenames():
    return codenames
