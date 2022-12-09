# Gesture Controlled PPT

## Inspiration
This project was inspired by a desire to make something simple, yet amazing. Automating the process of switching slides was a good idea, in our opinion. We were also motivated by the fact that not only would we need to learn an entirely new module, which is good practice, but also that this project would need the help of Machine Learning models.

## What it does
Using Python's OpenCV module, Google's MediaPipe and the power of ML models with numpy, we created a way for your computer to recognize the gestures you make with your fingers via a webcam, which is then interpreted as a command. For eg. pointing your finger to the right will go to the next slide, etc.
## How we built it
As mentioned, we used Python's OpenCV module to use the webcam. Then MediaPipe does its job, using the ML pipeline we created to recognize the structure of the human hand and where each finger is. We also required  NumPy and pyautogui (for shortcuts).
## Challenges we ran into
Obviously training the model was a challenge as it requires a lot of time, effort and correction.
Also neither of us actually ever used OpenCV before this, so learning to use it for the first time was a bit tricky.
## Accomplishments that we're proud of
Learning how to use a new model, OpenCV, to use webcam video. We are also proud having having successful created another model as well as trained it to do something useful.


## Using it
```pip install mediapipe cvzone pyautogui```


Then run main.py
