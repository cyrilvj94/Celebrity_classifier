import base64


def decodeImage(imgstring, fileName):
    """
    Takes an image string ie, base64 encoded -->>converts to bytes-->>Stores in filename

    :param imgstring: base64 encoded
    :param fileName: file name to store
    :return: creates an img in file name
    """
    imgdata = base64.b64decode(imgstring)
    with open(fileName, 'wb') as f:
        f.write(imgdata)
        f.close()


def encodeImageIntoBase64(croppedImagePath):
    """
    takes  a byte object and returns base64 encoded string
    :param croppedImagePath : bytes obj
    :returns: base64 encoded obj
    """
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read())