# Photo Enhancer

## Overview

Photo Enhancer is an application for improving image quality using
machine learning--based image processing techniques. The project focuses
on reducing noise, improving sharpness, and enhancing overall visual
quality of photos.

## Features

-   Image enhancement using a neural network
-   Noise reduction and detail enhancement
-   Support for JPG, JPEG, and PNG formats
-   Automatic processing without manual tuning
-   Can be used with or without a GUI

## Project Structure

    photo-enhancer/
    ├── core/
    ├── gui/
    ├── resources/
    └── main.py

## How It Works

1.  Load an image
2.  Preprocess the image
3.  Apply the neural network model
4.  Postprocess the result
5.  Save or display the enhanced image

## Installation

### Requirements

- Python 3.9+
- TensorFlow-cpu
- NumPy
- OpenCV
- PySide6

Install dependencies:

    pip install -r requirements.txt

## Running from Git

1.  Clone the repository:

    ```bash
    git clone https://github.com/yourusername/photo-enhancer.git
    cd photo-enhancer
    ```

2.  Create a virtual environment (recommended):

    ```bash
    python -m venv venv
    # Linux / macOS:
    source venv/bin/activate
    # Windows:
    venv\Scripts\activate
    ```

3.  Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4.  Run the application:

    ```bash
    python main.py
    ```

> If you prefer not to use a virtual environment, you can install dependencies globally, but this is **not recommended** as it may cause conflicts with other Python projects.

## Usage

    python main.py

## Limitations

-   Strongly blurred images may not be fully restored
-   The model enhances visual quality but does not recover true lost
    details

## License

Educational and research use only. Commercial use requires permission
from the author.