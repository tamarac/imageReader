from PIL import Image
import pytesseract
import imageTransform as s


image = Image.open('image.png')

initial = s.tranformImage(image)
withContrast = s.addContrast(initial)
withSharpness = s.addSharpness(initial)

# Simple image to string
print(pytesseract.image_to_string(withSharpness))