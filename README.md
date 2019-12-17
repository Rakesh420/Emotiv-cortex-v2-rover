# Emotiv-cortex-v2-rover
Controlling a rover with mental commands using Emotiv Insight.
![Image of Yaktocat](https://camo.githubusercontent.com/652813c2717c0f845483367d278abd2d66329f26/68747470733a2f2f63646e2d696d616765732d312e6d656469756d2e636f6d2f6d61782f313630302f312a7548337633783672436a6c2d5f69594f6272564c68672e6a706567)
A Brain-Computer Interface implementation to control a rover with real time EEG data.

Using an EEG acquisition - Emotiv Insight to read the brain signals. The official Emotiv BCI software is used to train and classify mental commands. 

In the future, I would like to use signal processing tools to convert the raw EEG time domain data into frequency domain. We can then access the mental activity of the user(i.e. attentive, relaxed, tensed) using the frequency domain singals.

Requirements:

* Python 3.
* Raspberry pi 3.
* Emotiv Insight.
* Rover

How to run the rover:

* Connect the Emotiv Insight to the EMOTIV app and open up the EMOTIV BCI app.
* Run the EEG_Main.py on the compter which is running the Emotiv Cortex App.
* Run the rover.py on the Raspberry pi which also used to run the flask server.
