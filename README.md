# voice_recognition_using_voice
Recognizing the speaker's gender is useful in automatic salutations, tagging audio recordings, seperating sounds belonging to a specific gender for analysis, etc. that can help digital personal assistants in reproducing male, female generic results.  
```
This Project contains the dataset of 3,168 recorded voice samples, collected from male and female speakers.  
The voice samples are pre-processed by acoustic analysis in R using the seewave and tuneR packages,  
with an analyzed frequency range of 0hz-280hz (human vocal range).
```
  
 ## VOICE ATTRIBUTES  
 
Each voice sample format is a .WAV file. The .WAV format 
files have been pre-processed for acoustic analysis using the 
specan function by the WarbleR R package 
The pre-processed WAV files have been saved into a CSV 
file. The CSV file is contained 3168 rows and 21 columns. 
There are features and the classification of male or female in 
these 21 columns.
### ATTRIBUTES: 

![image](https://user-images.githubusercontent.com/114367518/219280414-9fa97e06-7387-4c2c-9949-3553c18d905d.png)    
![image](https://user-images.githubusercontent.com/114367518/219279987-58766ee2-f7e1-4fa4-881c-02acc8c9f692.png)  
![image](https://user-images.githubusercontent.com/114367518/219280012-e15613f6-ee44-4a48-99b9-c728d1eab976.png)  
![image](https://user-images.githubusercontent.com/114367518/219280036-b90541f0-1a92-441c-aaa6-31b68df84d60.png)  


## PYTHON LIBRARIES:
```
SKLEARN  
MATPLOTLIB    
PANDAS  
PYAUDIO  
NUMPY  
PYTHON-SPEECH-FEATURES  
SCIKIT-LEARN  
SCIPY  
PICKLE  
```
![image](https://user-images.githubusercontent.com/114367518/219280821-45ce97af-c991-45c0-ab71-95350b0f71ce.png)  
![image](https://user-images.githubusercontent.com/114367518/219280837-634c27d6-e0e5-4f0c-ae18-d6ea45fc6781.png)  
![image](https://user-images.githubusercontent.com/114367518/219280847-71be532c-15e2-4a34-97e7-2e729b048d5e.png)  
![image](https://user-images.githubusercontent.com/114367518/219280853-fbb8861e-b9df-4e14-9d28-a43d6a6aa1a1.png)  
![image](https://user-images.githubusercontent.com/114367518/219280864-b915ff34-74ee-44ec-adea-6c8211958303.png)  



## R LIBRARIES:

```
TUNER
SEEWAVE
WARBLER
```

![image](https://user-images.githubusercontent.com/114367518/219280982-fd4170cc-64af-408d-a518-5a3bd73c33cc.png)  
![image](https://user-images.githubusercontent.com/114367518/219280992-a6ecccd6-2207-40e0-8780-fda4b81a4a48.png)  
![image](https://user-images.githubusercontent.com/114367518/219280996-a5b69134-fa36-4122-ba5f-b3224c5e62cf.png)  
![image](https://user-images.githubusercontent.com/114367518/219281036-9c2cc0be-4dba-4a50-a58c-cd915e2b2d0e.png)  


## VOICE DATA 

This database was created to identify a voice as male or female, based upon acoustic properties of the voice and speech. The dataset consists of 3,168 recorded voice samples, collected from male and female speakers. The voice samples are pre-processed by acoustic analysis in R using the seewave and tuneR packages, with an analyzed frequency range of 0hz-280hz (human vocal range).  
[Gender Recognition by Voice | Kaggle](https://www.kaggle.com/datasets/primaryobjects/voicegender)  
  

[RESEARCH PAPER](https://drive.google.com/file/d/16EbNPzD8YwqQR0rYQOAS_SfUxIQHllXz/view?usp=sharing)  
[PPT_REPORT](https://drive.google.com/drive/folders/1ctAaZCYXuHrUk3IkxVOdwuSnJtoZUz8t?usp=sharing)


# VER-2.0  

We have implemented the GUI in ver-2.0 with multiple different features,  
like Variable Dataset append value every time a use uses it, just like AI which collects and saves data from user for every use and improve itselt   
The GUI also gives the interface to plot  
>LOSS CURVE ( GOOD FIT )  
>ACCURACY CURVE  
>PRECISION CURVE using ( matplotlib )   

## GUI LIBRAIES

```
Tkinter
CustomTkinter
Pandas
numpy

```
![image](https://github.com/krmahi/Gender_recognition_using_voice/assets/114367518/d45ef6ff-5026-45f6-8976-5cc16d79b093)

## LIMITATIONS

>Voice Recording should have an active BACKGROUND NOISE CANCELLATION , pre or post recording, to get the precise output.

>Using variable Dataset increases accuracy of algorithms but, might arise the problem of OVERFITTINS, to remove this problem we can monitor the LOSS CURVE and and as soon has the LOSS CURVE values start going UP again it will be the cue for OVERFITTING so then our program will stop incrementing the DATASET, then we can start it again as soon as the curve is stable again , this will be looped , making the dataset almost always variable and convert a STATIC ML PROJECT to SEMI - AI PROJECT. 


```
Ver-2.0 in RELEASED as an Executable
```
  
>MIT LICENCE   
>Licence FILE included





