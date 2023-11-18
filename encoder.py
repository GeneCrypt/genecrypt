from PIL import Image
import numpy as np

def image_to_binary(image_path):
    img = Image.open(image_path)
    img_array = np.array(img)
    height, width, _ = img_array.shape

    binary_data = ''
    for i in range(height):
        for j in range(width):
            for value in img_array[i, j]:
                binary_data += format(value, '08b')

    return binary_data, height, width




def encode_dna(binary_data):
    dna_mapping = {'00': 'A', '01': 'C', '10': 'T', '11': 'G'}
    encoded_data = ''.join(dna_mapping[binary_data[i:i+2]] for i in range(0, len(binary_data), 2))
    return encoded_data

def encode_image(image_path, output_path):
    binary_data, height, width = image_to_binary(image_path)
    encoded_data = encode_dna(binary_data)

    with open(output_path, 'w') as file:
        file.write(f"{height} {width}\n")
        file.write(encoded_data)

if __name__ == "__main__":
    input_image = "input_image.jpg"
    output_encoded = "encoded_image.txt"
    encode_image(input_image, output_encoded)
from PIL import Image
import numpy as np

def image_to_binary(image_path):
    img = Image.open(image_path)
    img_array = np.array(img)
    height, width, _ = img_array.shape
    binary_data = ''.join(format(pixel, '08b') for row in img_array for pixel in row)
    return binary_data, height, width

def encode_dna(binary_data):
    dna_mapping = {'00': 'A', '01': 'C', '10': 'T', '11': 'G'}
    encoded_data = ''.join(dna_mapping[binary_data[i:i+2]] for i in range(0, len(binary_data), 2))
    return encoded_data

def encode_image(image_path, output_path):
    binary_data, height, width = image_to_binary(image_path)
    encoded_data = encode_dna(binary_data)

    with open(output_path, 'w') as file:
        file.write(f"{height} {width}\n")
        file.write(encoded_data)

if __name__ == "__main__":
    input_image = "input_image.jpg"
    output_encoded = "encoded_image.txt"
    encode_image(input_image, output_encoded)
