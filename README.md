# License Plate Detection and Recognition.

## Project Overview
This project aims to develop a deep learning-based system for detecting license plates and recognizing characters on them in both images and videos. The project is divided into three main sections:

1. **License Plate Detection in Images**
2. **License Plate and Character Recognition in Images**
3. **License Plate and Character Recognition in Videos**

## YOLOv5 for Object Detection
For the object detection tasks in this project, we will be using YOLOv5, which stands for "You Only Look Once." YOLOv5 is the latest version of the YOLO (You Only Look Once) object detection system, which is known for its real-time object detection capabilities.

### Key Features of YOLOv5:
- **State-of-the-art Performance**: YOLOv5 offers significant improvements in both accuracy and speed compared to its predecessors.
- **Real-time Object Detection**: YOLOv5 is capable of real-time object detection, making it suitable for various applications, including this license plate detection and recognition project.
- **Easy to Use and Implement**: YOLOv5 is easy to use and implement, making it an excellent choice for object detection tasks for both images and videos.

![123](https://github.com/MohammadAmini1998/iranian-plate-recognition/assets/49214384/13a6d1b5-6f71-48e3-b751-35dc08b748a5)

*Architecture of YOLO5*

For more details, please refer to the [YOLOv5 paper](https://arxiv.org/pdf/1506.02640.pdf).

## 1. License Plate Detection in Images
In this section, our goal is to design a deep learning model that can detect license plates in images. We will train the model using a dataset containing images of cars with annotated license plates. The output of the model will be bounding boxes around the detected license plates.

In this section, our goal is to design a deep learning model that can detect license plates in images. We will use a dataset obtained from the internet for this task. The dataset is available on Kaggle at the following link: [Car Plate Detection Dataset](https://www.kaggle.com/datasets/andrewmvd/car-plate-detection).

The dataset contains 432 images of cars along with their license plates. Since the goal of this section is only to detect license plates and not the characters on them, the license plates in this dataset do not contain Persian characters, which is not a problem for our task.

The dataset is in XML format and will be converted to YOLO format for this project.

## 2. License Plate and Character Recognition in Images 
Building upon the license plate detection model developed in the previous section, we will extend the model to not only detect license plates but also recognize the characters on them. The input to the model will be an image containing one or more cars, and the output will be the detected license plates along with the recognized characters.

For this section, we have been provided with the dataset required. However, the format of the provided dataset is not in YOLO format. 

The difference between the provided format and YOLO format is that the provided format gives us the coordinates of the top-left point of the rectangle along with its width and height, while in the YOLO format, we need the coordinates of the center point along with its width and height.

In the provided JSON file, the class of each character (which can be from 0 to 36) and the coordinates of the top-left point along with the width and height of this rectangle are given.

We need to convert this information to YOLO format, where the label for each image should be a .txt file containing the class number, the coordinates of the center point (y, x), and the width and height of this rectangle.

## 3. License Plate and Character Recognition in Videos 
In this section, we will apply the trained model to a chosen video and detect all the license plates and characters present in the cars in the video.

For this section, we need to feed the video to the first network. By doing this, the first network will crop the parts of the video where it detects license plates.

Now we feed these cropped images to the second network. By doing this, all license plates and their characters in the video will be detected.

## Dataset
The dataset required for this project contains images of Iranian cars with annotated license plates. Each image in the dataset is annotated with bounding boxes around the license plates, along with labels for the characters on the license plates.

If you need the dataset for the second and third part which contains images for iranian car, please email me at mohammad.aminiiii98@gmail.com, and I will send it to you as soon as possible.

## Results

<p float="left">
  <img src="https://github.com/MohammadAmini1998/iranian-plate-recognition/assets/49214384/44fa0453-2658-4b61-a7e9-71971ac25226" alt="Car1" width="400" />
  <img src="https://github.com/MohammadAmini1998/iranian-plate-recognition/assets/49214384/b78f5018-af23-4b15-9794-94f25467ed35" alt="Car2" width="400" /> 
  <img src="https://github.com/MohammadAmini1998/iranian-plate-recognition/assets/49214384/d6baffc3-8a39-44e2-be82-72ffc776b119" alt="CarCar" width="400" />
</p>
