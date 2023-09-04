import cv2
import pytesseract
from PIL import Image

def extract_text_from_region(id: str, image, x: int, y: int, width: int, height: int):
    target = image[y:y+height, x:x+width]

    inverted_image = cv2.bitwise_not(target)
    resized = cv2.resize(inverted_image, (inverted_image.shape[1]*8, inverted_image.shape[0]*8), interpolation=cv2.INTER_CUBIC)
    gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    _, binary = cv2.threshold(blurred, 128, 255, cv2.THRESH_BINARY)
    roi = binary

    # for debug
    # filename = f'out/debug/{id}.jpg'
    # print(filename)
    # cv2.imwrite(filename, roi)

    text = pytesseract.image_to_string(Image.fromarray(roi))

    return text

def extract_value_from_region(id, image, x, y, width, height):
    target = image[y:y+height, x:x+width]

    vertical_scale_factor = 2.0
    height, width, _ = target.shape
    new_height = int(height * vertical_scale_factor)
    fix_height_img = cv2.resize(target, (width, new_height))

    inverted_image = cv2.bitwise_not(fix_height_img)
    resized = cv2.resize(inverted_image, (inverted_image.shape[1]*8, inverted_image.shape[0]*8), interpolation=cv2.INTER_CUBIC)
    gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    _, binary = cv2.threshold(blurred, 128, 255, cv2.THRESH_BINARY)
  
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    dilated_image = cv2.dilate(binary, kernel, iterations=4)
    roi = dilated_image

    # for debug
    filename = f'out/debug/{id}.jpg'
    print(filename)
    cv2.imwrite(filename, roi)

    value = pytesseract.image_to_string(Image.fromarray(roi))

    return value