from dogcat_classifier.classifier import predict_image

# Path to the image in the current directory
image_path = 'dog.jpg'  # Assuming the image is in the same directory

# Make a prediction
result = predict_image(image_path)

# Print the result (it should print either 'Dog' or 'Cat')
print(f'The image is a {result}.')
