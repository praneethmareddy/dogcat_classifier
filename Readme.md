Project Overview: Dog-Cat Classifier Python Package


How to Use the Package:

step 1 :  
        pip install dogcat-classifier


step 2 :

        from dogcat_classifier.classifier import predict_image
        image_path = 'path_to_your_image.jpg'
        result = predict_image(image_path)
        print(f'The image is a {result}.')







This project focuses on creating a machine learning model that classifies images of dogs and cats. The model is encapsulated within a Python package, making it easy to install and use. The package employs TensorFlow for model training and inference, while OpenCV and Pillow are utilized for image processing. It is distributed via PyPI (Python Package Index). 
Project Structure:

dogcat_classifier/

    dogcat_classifier/

            init.py (Marks this directory as a Python package)
            classifier.py (Contains the predict_image function and model loading logic)
            model.h5 (Pre-trained TensorFlow model)
            test_predict.py (Sample test file for predictions)

    dog.jpg (Sample image for testing)

    README.md (Project description and usage details)

    setup.py (Configuration for building and installing the package)

    requirements.txt (Project dependencies)

    MANIFEST.in (Ensures non-code files are included in the package)

    dist/ (Built distributions created after running build commands)--ignored

    build/ (Temporary build artifacts)--ignored

    *.egg-info (Metadata for the package)--ignored


Steps to Build and Distribute the Package
1. Initialize the Project
Set up the project folder with necessary files like setup.py, classifier.py, model.h5, etc., to create the Python package. The setup.py file contains metadata and dependencies, while classifier.py includes functionality for loading the trained model and classifying images.
2. Install Dependencies
Use the following command to install required packages:
    pip install tensorflow pillow numpy matplotlib scikit-learn opencv-python setuptools wheel twine
3. Build the Package
To build the package, run:

    python setup.py sdist bdist_wheel
This command generates distributable .tar.gz and .whl files in the dist/ folder.
4. Test the Package Locally
Install the package locally to verify functionality:

    pip install .
You can test it using test_predict.py, which checks the model's prediction on a sample image (dog.jpg).
5. Upload the Package to PyPI
After testing, upload the package using Twine:

    python -m twine upload dist/*
6. Verify the Package on PyPI
Once uploaded, confirm that it works by installing it from PyPI:




Why This Approach?
Using python setup.py sdist bdist_wheel: This command generates distribution files required for uploading to PyPI.
Uploading with Twine: Twine securely handles uploads to PyPI, ensuring proper management of package files and credentials.
Commands Used Summary
Install dependencies:

    pip install tensorflow pillow numpy matplotlib scikit-learn opencv-python setuptools wheel twine
Build the package:

    python setup.py sdist bdist_wheel
Upload to PyPI:

    python -m twine upload dist/*
Install locally for testing:

    pip install .
Test the package:

    python test_predict.py

This structured approach ensures that you can efficiently create, distribute, and utilize a dog-cat image classifier in Python.
