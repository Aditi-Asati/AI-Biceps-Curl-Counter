# AI-Biceps-Curl-Counter
## Overview
The **AI Bicep Curls Counter** program counts the number of Bicep Curls as the trainer performs it in real time and displays it on the GUI screen along with the live camera recording of the trainer doing Bicep Curls. It uses Machine Learning to identify the "contracted" and "extended" positions of the arms when a trainer is performing Bicep Curls in front of the camera and counts accordingly.
## Graphical User Interface of the Program
The GUI looks like this one.
<p align="center"> 
	<img src="./AI tkinter interface sc.png" height="380px">
</p>
It consists of the following 5 buttons as shown above:

- **Toggle Counting** - Pressing this button will allow the program to start counting the Bicep Curls of a trainer performing it in front of the camera.

- **Extended** - Every time this button is pressed, the program will click and save the picture of the trainer as seen by the camera as "extended". Thus make sure to orient your arm in the extended position while clicking this button. These images will be used to train the model!

- **Contracted** - Likewise, pressing this button would ask the program to click and save the images of the trainer as seen by the camera as "contracted", hence make sure to orient your arm in the contracted position while pressing this button.
- **Train Model** - After taking approx 40 images of each "contracted" and "extended" positions of the arm, the program trains the Machine learning model on these images once the **Train Model** button is clicked.
- **Reset** - This button resets the counter which is located at the bottom of the GUI to 0.

## Guidelines
- You have to first click approx 40 images of both extended and contracted positions of the arm by pressing the ```Extended``` and ```Contracted``` buttons each time you wanna take a picture
- Now, press the ```Train Model``` button to train the model. 
- Once the model has been trained, you are all set to start performing Bicep Curls and letting the program to count the number of reps for you by pressing the ```Toggle Counting``` button.
# Installation
## Using Git
Type the following command in your Git Bash:

- For SSH:
```git clone git@github.com:Aditi-Asati/AI-Biceps-Curl-Counter.git```
- For HTTPS: ```git clone https://github.com/Aditi-Asati/AI-Biceps-Curl-Counter.git```

The whole repository would be cloned in the directory you opened the Git Bash in.

## Using GitHub ZIP download
You can alternatively download the repository as a zip file using the GitHub **Download ZIP** feature. 

*External modules used-*
- Pillow
- numpy
- opencv_python
- scikit_learn


Run the command ```pip install -r requirements.txt``` to install all these dependencies at once.

You are good to go!