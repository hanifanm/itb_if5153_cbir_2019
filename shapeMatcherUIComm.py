import cv2
import glob
import numpy as np

global codenames
codenames = []
def shapeMatcher(query_image):

    global codenames
    codenames = []
    database_images = glob.glob('images/*')
    image_test = len(database_images)
    database_images = database_images[:image_test]
    
    print("Shape Distances Between \n-------------------------")
    query = cv2.imread(query_image,cv2.IMREAD_GRAYSCALE)
    all_results = []
    all_distance = []
    all_names = []
    for filename in database_images:

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
        print("Distance : {}".format(all_distance[i]))
        counter = counter + 1
        if counter == 24:
            break
    return sorted_results
    #return all_results

def get_codenames():
    return codenames
