from PIL import Image
import numpy as np

def decode_dna(encoded_data):
    dna_mapping_reverse = {'A': '00', 'C': '01', 'T': '10', 'G': '11'}
    binary_data = ''.join(dna_mapping_reverse[char] for char in encoded_data)
    return binary_data

def binary_to_image(binary_data, height, width):
    pixel_values = [int(binary_data[i:i+8], 2) for i in range(0, len(binary_data), 8)]
    img_array = np.array(pixel_values, dtype=np.uint8).reshape(height, width, 3)
    decoded_image = Image.fromarray(img_array)
    return decoded_image

def decode_image(encoded_path, output_path):
    with open(encoded_path, 'r') as file:
        height, width = map(int, file.readline().split())
        encoded_data = file.read()

    binary_data = decode_dna(encoded_data)
    decoded_image = binary_to_image(binary_data, height, width)
    decoded_image.save(output_path)

if __name__ == "__main__":
    input_encoded = "encoded_image.txt"
    output_image = "decoded_image.jpg"
    decode_image(input_encoded, output_image)
