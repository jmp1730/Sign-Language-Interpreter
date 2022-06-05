# Sign Language Interpreter
### Developed by Joshua Mathew Philip from Cochin University of Science and Technology.
### Made for UG Mini Project.

In this project, we have proposed a marker-free, visual Sign Language recognition system using image processing, computer vision and neural network methodologies, to identify the characteristics of the hand in images taken from a video through web camera. 

## Features
- Sign Language Interpretation:
Purpose: The program will translate the given sign language into ordinary alphabets.
Input: American Sign Language gestures.
Output: Corresponding alphabets.<br>
- Speech Synthesis:
Purpose: To convert the translated gestures into speech. 
Input: American Sign language gestures. 
Output: Corresponding sound of the letters.<br>


## How this works?
This approach will convert video of daily frequently used full sentences gesture into a text and speak. Identification of hand shape from continuous frames will be done by using series of image processing operations. Interpretation of signs and corresponding meaning will be identified by OpenCV.

### Steps workflow:
- Setting up 
- Download/Update latest data.
- Activate Virtual Environment.
- Start the program. 

### Hardware and Software Requirements
## Hardware:
- Does not require any particular hardware. The application works on any computer with standard processing speeds.<br>
## Software:
- Tkinter :The frontend development is entirely done with Tkinter. Tkinter is a Python binding to the Tk GUI toolkit. It is the standard Python interface to the Tk GUI toolkit, and is Python’s de facto standard GUI.<br>
- Python 3.7 : The entire application is written in the python program- ming language, the deep learning modules used are also based on python.<br>
- Tensorflow v2.1 : It’s the backbone of the back-end part of the system. Focused on training and inference of the neural networks.<br>
- OpenCV : It’s also a part of backend part, mainly aimed at real-time computer vision.<br>
- Keras: It provides a Python interface for artificial neural networks and acts as an interface for the TensorFlow library.<br>

## STEPS

### Installing Prerequisites
- 1.1 - Download and Install Python IDLE.<br>
- 1.2 - Download and install anaconda3 from given link : 
https://www.filehorse.com/download-anaconda-64/download/ <br>
- 1.3 - Adding data set 
https://drive.google.com/file/d/190de2TiXndAyfSfNOZhmFWjuojrIanEC/view?usp=sharing
Extract mydata.zip file to `Sign-Language-Interpreter folder`.<br>
- 1.4 - Setting Virtual Environment 
https://drive.google.com/file/d/1MXNbgoSwyFXuxJF4-rPzH0TAG2braJ7Q/view?usp=sharing
Extract virtual.zip file in the `c/users/user/anaconda3/envs folder`.<br>

### Running the Program
- 2.1 - Open anaconda prompt.<br>
- 2.2 - Run command : `activate virtual` .<br>
- 2.3 - Change directory to project folder.<br>
- 2.4 - Run command : `main.py`.<br>
- 2.5 - Click the button on the pop up window to start detection.<br>
- 2.6 - Set the values of the trackbars as given in the screenshot below.<br>


NOTE:
Please run the project in plan environment. Here I’m attaching a portion. Set the trackbars as mentioned in the screenshot. `_` symbol can be used for speaking.<br>

![TrackBar](/images/tb.png)

### Brief of given files
1. `main.py` - to run the program.<br>
2. `training.py` - to train the model.<br>
3. `recognize.py` - for recognition of gestures.<br>
4. `gui.py` - for creation of user interface.<br>
5. `mymo.h5` - is an already created model.<br>
6. `virtual.zip` - to set up the virtual environment.<br>
7. `mydata` - contains the dataset.<br>

### Screenshots
# Dataset Creation-
![Dataset Creation](/images/dc.png) <br>
# Gesture Recognition-
![Gesture Recognition](/images/gr.png) <br>


Any improvement to this Documentation or any new contributions are always welcome! 

Thanks,
Joshua Mathew Philip