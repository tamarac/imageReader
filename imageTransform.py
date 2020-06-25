from PIL import Image,ImageEnhance,ImageFilter
teste = 2

def tranformImage(image):
    gray = image.convert('L')
    return gray.filter(ImageFilter.DETAIL)

def addContrast(image, factor = 2):
    contrast = ImageEnhance.Contrast(image)
    return contrast.enhance(factor)

def addSharpness(image, factor = 2):
    sharpness = ImageEnhance.Sharpness(image)
    return sharpness.enhance(factor)