#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import cv2

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def dist_thresholding(des1, des2, threshold_value) -> list: #set a threshold- return all matches from other images within this threshold
    #des1 = query image
    #des2 = reference image 
    bf = cv2.BFMatcher() #Euclidean Distance is used as the distance metric
    matches = bf.knnMatch(des1, des2, k=100) #returns the closest k matches for every descriptor in the query image (i.e., the current image),
    # in order of increasing Euclidean distance.
    finalValues = []
    if (threshold_value != -1):
        for item in matches:
            tempList = []
            for des_match in item:
                dist_value = des_match.distance
                if (dist_value < threshold_value):
                    tempList.append(des_match)
            finalValues.append(tempList)
    else:
        for item in matches:
            tempList = []
            for des_match in item:
                dist_value = des_match.distance
                tempList.append(des_match)
            finalValues.append(tempList)
    return finalValues


def nn(des1, des2, threshold_value) -> list:
    #des1 = query image
    #des2 = reference image 
    bf = cv2.BFMatcher() #Euclidean Distance is used as the distance metric
    matches = bf.knnMatch(des1, des2, k=100) #returns the closest k matches for every descriptor in the query image (i.e., the current image),
    # in order of increasing Euclidean distance.
    finalValues = []
    if (threshold_value != -1):
        for item in matches:
            tempList = []
            dist_value = matches[matches.index(item)][0].distance
            if (dist_value < threshold_value):
                tempList.append(matches[matches.index(item)][0])
            finalValues.append(tempList)
    else:
        for item in matches:
            tempList = []
            dist_value = matches[matches.index(item)][0].distance
            tempList.append(matches[matches.index(item)][0])
            finalValues.append(tempList)
    
    return finalValues


def nndr(des1, des2, threshold_value) -> list:
    bf = cv2.BFMatcher()
    matches = bf.knnMatch(des1, des2, k=100) #returns the closest k matches for every descriptor in the query image (i.e., the current image),
    
    finalValues =[]

    for item in matches:
        temp = []
        nn = item[0]
        nnDistance = nn.distance
        nn2 = item[1]
        nn2Distance = nn2.distance

        ratio = nnDistance/nn2Distance
        if (threshold_value == -1 or ratio < threshold_value):
            temp.append(nn)

        finalValues.append(temp)
    return finalValues

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# vim:set et sw=4 ts=4:
