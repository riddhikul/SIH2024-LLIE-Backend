import cv2

def reduce_noise(image):
    return cv2.fastNlMeansDenoisingColored(image, None, 10, 10, 7, 21)

def enhance_low_light_image(input_image, clip_limit=2.0, tile_size=(8, 8)):
    lab = cv2.cvtColor(input_image, cv2.COLOR_RGB2LAB)
    l, a, b = cv2.split(lab)
    clahe = cv2.createCLAHE(clipLimit=clip_limit, tileGridSize=tile_size)
    l_clahe = clahe.apply(l)
    lab_clahe = cv2.merge((l_clahe, a, b))
    output_image = cv2.cvtColor(lab_clahe, cv2.COLOR_LAB2RGB)
    return output_image
