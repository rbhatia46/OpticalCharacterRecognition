# OpticalCharacterRecognition
Using Tesseract, an open source library for performing Optical Character Recognition in Python.

## How to use :
This repository contains 2 python scripts for 2 different use cases:
* For performing OCR on images
* For performing OCR on PDFs

Run the respective python scripts for respective use-cases.

## Dependencies required :
* Tesseract Core Library
* PyTesseract (Python wrapper for Tesseract Core)
* Pillow (For Image Processing)
* [ImageMagick](https://legacy.imagemagick.org/script/binary-releases.php#windows)
* wand(Python binding for ImageMagick)

## Run in Docker

First build docker image
```
docker build -t ocr .
```

Run Docker container
```
docker run -it --rm -p 5000:5000 ocr
```

Or run using docker-compose

```
docker-compose up
```

***
**[Tesseract](https://github.com/tesseract-ocr/tesseract)** was originally written in C++ and uses an LSTM Network behind the scenes, for more reading and installation guide, you can check out this very helpful [blog post](https://appliedmachinelearning.blog/2018/06/30/performing-ocr-by-running-parallel-instances-of-tesseract-4-0-python/). This will explain you the essential stuff. I have also extended this for PDFs to make it more useful for real-world use-case.
