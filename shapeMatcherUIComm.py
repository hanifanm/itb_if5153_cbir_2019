import cv2
import glob
import numpy as np

def shapeMatcher(query_image):

    database_images = glob.glob('images/*')
    image_test = len(database_images)
    database_images = database_images[:image_test]
    
    print("Shape Distances Between \n-------------------------")
    query = cv2.imread(query_image,cv2.IMREAD_GRAYSCALE)
    all_results = []
    all_distance = []
    for filename in database_images:

        # Read image
        im = cv2.imread(filename,cv2.IMREAD_GRAYSCALE)

        m1 = cv2.matchShapes(query,im,cv2.CONTOURS_MATCH_I2,0)
        if m1 < 0.1:
            all_results.append(cv2.imread(filename))
            all_distance = np.append(all_distance, m1)

    new = np.argsort(all_distance)
    sorted_results = []
    counter = 0
    for i in new:
        sorted_results.append(all_results[i])
        print("Distance : {}".format(all_distance[i]))
        counter = counter + 1
        if counter == 24:
            break
    return sorted_results
    #return all_results
