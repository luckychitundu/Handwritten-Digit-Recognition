# Handwritten Digit Recognition System

The Handwritten Digit Recognition System is a Convolutional Neural Network (CNN) model designed to recognize handwritten digits from 0 to 9. It has been trained on a dataset comprising over 75,000 examples from the MNIST dataset. This README provides an overview of the system, how to use it, and its key features.

![Screenshot (11)](https://github.com/luckychitundu/Handwritten-Digit-Recognition/assets/87910852/17f34316-4a4c-40be-a814-4352996229c3)


## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Handwritten digit recognition is a fundamental task in computer vision and machine learning. The Handwritten Digit Recognition System leverages the power of deep learning through a Convolutional Neural Network to accurately classify handwritten digits. This system can find applications in various domains, such as digit-based captcha solving, automatic form recognition, and more.

## Features

- **Digit Recognition**: The system can accurately recognize and classify handwritten digits from 0 to 9.
- **High Accuracy**: It has been trained on a vast dataset of handwritten digits, resulting in high recognition accuracy.
- **User-Friendly Interface**: A user-friendly interface allows users to draw or input handwritten digits for recognition.
- **API Integration**: The model can be integrated into other applications via a RESTful API for seamless digit recognition.
- **Customization**: Developers can fine-tune the model or train it on additional data for specific applications.
- **Open Source**: This project is open source, encouraging collaboration and improvement.

## Requirements

To use the Handwritten Digit Recognition System, you will need the following:

- Python 3.7+
- TensorFlow 2.0+
- Flask (for the API)
- Numpy
- PIL (Python Imaging Library)
- A modern web browser for the web-based interface

## Installation

1. Clone this repository to your local machine:

   ```
   git clone https://github.com/yourusername/handwritten-digit-recognition.git
   ```

2. Install the required Python packages using pip:

   ```
   pip install -r requirements.txt
   ```

## Usage

### Web Interface

1. Start the web-based interface:

   ```
   python app.py
   ```

2. Open a web browser and navigate to `http://localhost:5000` to access the application.

3. Use the drawing canvas to draw or input handwritten digits.

4. Click the "Recognize" button to see the model's prediction.

### API

You can also integrate the model into your applications using the RESTful API.

1. Start the API:

   ```
   python api.py
   ```

2. Send a POST request to `http://localhost:5001/api/predict` with a JSON object containing the pixel values of the handwritten digit you want to recognize.

   Example POST request:

   ```json
   {
       "pixels": [0, 0, 0, 0, 255, 255, 0, 0, ...]
   }
   ```

3. Receive the model's prediction as a response.

## Contributing

Contributions to the Handwritten Digit Recognition System are welcome! Whether you want to improve the model's accuracy, add new features, or enhance the user interface, please feel free to submit pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
