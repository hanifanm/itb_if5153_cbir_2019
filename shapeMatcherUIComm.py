import cv2
import glob

def shapeMatcher(query_image):

    database_images = glob.glob('images/*')
    image_test = len(database_images)
    database_images = database_images[:image_test]
    
    print("Shape Distances Between \n-------------------------")
    query = cv2.imread(query_image,cv2.IMREAD_GRAYSCALE)
    results = []
    for filename in database_images:

        # Obtain filename from command line argument
        #filename = sys.argv[i]
        
        # Read image
        im = cv2.imread(filename,cv2.IMREAD_GRAYSCALE)

        m1 = cv2.matchShapes(query,im,cv2.CONTOURS_MATCH_I2,0)
        if m1 < 0.1:
            print("Query dengan gambar ")
            print(filename)
            print(" : {}".format(m1))
            results.append(cv2.imread(filename))

    return results
