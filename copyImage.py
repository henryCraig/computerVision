def copyImgShape(imgToCopy):
    imgWidth, imgHeight, imgChannels = imgToCopy.shape
    newImg = np.zeros([imgWidth, imgHeight, 3])
    return newImg
