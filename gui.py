import tkinter as tk
from tkinter import *
import customtkinter
import subprocess

import pandas as pd
import matplotlib.pyplot as plt

from pathlib import Path
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import os
import time
import wave
import pyaudio
import threading

from data_process import *
from neural_net import *




#scripts
def voicedetails_modified():
    # Read the CSV file into a DataFrame
    df = pd.read_csv('output/voiceDetails.csv')
    
    # Drop the columns you want to remove
    columns_to_remove = ['sound.files', 'selec', 'duration', 'peakf']
    df = df.drop(columns=columns_to_remove)
    
    # Save the modified DataFrame to a new CSV file
    df.to_csv('voicedetails_modified.csv', index=False)
    
def voice_csv(label):
    voice_df = pd.read_csv('voice.csv')
    voicedetails_df = pd.read_csv('voicedetails_modified.csv')
    #gen = str(label)
    #gen = gen.strip()
    
    gen = label.replace('"', '')
    #print(gen)
    
# Define the "label" variable
    if 'Male' in gen:
        gender = 'male'
    else: 
        gender = 'female'

# Insert the "label" column at the end of "voicedetails_df"
    voicedetails_df['label'] = gender

# Append the data from "voicedetails_modified.csv" to "voice.csv"
    merged_df = voice_df._append(voicedetails_df, ignore_index=True)

# Save the merged DataFrame back to "voice.csv" (overwriting the original file)
    merged_df.to_csv('voice.csv', index=False)
    
    
#dataset row count
def dataset_count():
    df = pd.read_csv('voice.csv')
    count = df.shape[0]
    dataset_update_label.configure(text = count)
    
def run_main_script():
    result = subprocess.check_output(["python", "main.py"])
    update_output(result.decode("utf-8"))
    voicedetails_modified()
    voice_csv(result.decode("utf-8"))
    dataset_count()
    #print(result.decode("utf-8"))
'''
def run_sound_recorder_script():
    result = subprocess.check_output(["python", "sound_recorder.py"])
    update_output(result)

'''

#run_all_scripts

def run_scripts(script_name):
    if script_name == "neural_net.py":
        result = subprocess.check_output(["python", "neural_net.py"])
    elif script_name == "gender.py":
        result = subprocess.check_output(["python", "gender.py"])
    elif script_name == "data_process.py":
        result = subprocess.check_output(["python", "data_process.py"])
    elif script_name == "sound_recorder.py":
        result = subprocess.check_output(["python", "sound_recorder.py"])
    elif script_name == "clf_comparison.py":
        result = subprocess.check_output(["python", "clf_comparison.py"])
    else:
        result = "Script not found or not supported."

    update_output(result)

#text_box widget

def update_output(text):
    output_textbox.configure(state="normal") #enable widget
    output_textbox.delete("0.0", "end")  # delete all text
    output_textbox.insert("0.0", text)  # insert at line 0 character 0
    #text = output_textbox.get("0.0", "end")  # get text from line 0 character 0 till the end
    output_textbox.configure(state="disabled")  # configure textbox to be read-only


    
#system settings
customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("blue")




#frame
root = customtkinter.CTk()
root.geometry("1300x800")
root.title("Voice Genix")

#up_frame
up_frame = customtkinter.CTkFrame(master=root, border_color="grey")
up_frame.pack( side = "top",fill = BOTH)

#theme_switch

def switch_event():
    
    if switch_var.get() == "on":
        customtkinter.set_appearance_mode("dark")
    else:
        customtkinter.set_appearance_mode("light")

switch_var = customtkinter.StringVar(value="on")
switch = customtkinter.CTkSwitch(master = up_frame, text="Theme", command=switch_event,
                                 variable=switch_var, onvalue="on", offvalue="off", progress_color= '#f9c26b')
switch.pack(padx = 5, pady = 5, side = "right")
#ui
title = customtkinter.CTkLabel(master=up_frame, text = "VOICE GENIX" ,font = ("Helvetica", 30, "bold"))
title.pack(padx = 50, pady = 10)


#left_frame

left_frame = customtkinter.CTkFrame(master=root, border_width=1)
left_frame.pack(pady = 10 ,side = "left", fill = Y)

#inside_left_frame

inside_frame = customtkinter.CTkFrame(master=left_frame,width=150, height=30, border_width=1)
inside_frame.pack(padx = 5, pady = 5)

#bottom_left_frame
left_bottom_frame = customtkinter.CTkFrame(master = left_frame, width=150, height=30, border_width=1)
left_bottom_frame.pack(padx = 5, pady = 5,side = "bottom")

#dataset_frame
dataset_frame = customtkinter.CTkFrame(master = left_frame, width= 150, height=30, border_width=1)
dataset_frame.pack()

#dataset_label
dataset_label = customtkinter.CTkLabel(master=dataset_frame, text = "DATASET COUNT" )
dataset_label.pack(padx = 30, pady = 1)

df = pd.read_csv('voice.csv')
count = df.shape[0]
#dataset_update_label
dataset_update_label = customtkinter.CTkLabel(master=dataset_frame, text = count, text_color = "#FDCA31" )
dataset_update_label.pack()


#bottom_frame
bottom_frame = customtkinter.CTkFrame(master=root, border_width= 1)
bottom_frame.pack(padx = 10, pady = 10, side = "bottom",expand = True, fill = BOTH)

#bottom_left_frame
bottom_left_frame = customtkinter.CTkFrame(master = bottom_frame, border_width=1, fg_color="#313131")
bottom_left_frame.pack( padx = 5, pady = 5,side = "left", fill = BOTH ,expand = True)

#bottom_middle_frame
bottom_middle_frame = customtkinter.CTkFrame(master = bottom_frame, border_width=1, fg_color="#313131")
bottom_middle_frame.pack(padx = 5, pady = 5,fill = BOTH, side = "left" ,expand = True)

#bottom_right_frame
bottom_right_frame = customtkinter.CTkFrame(master = bottom_frame, border_width=1, fg_color="#313131")
bottom_right_frame.pack( padx = 5, pady = 5,side = "left", fill = BOTH ,expand = True)

#buttons
run_main_script_button = customtkinter.CTkButton(master=left_frame, text="Check Gender" ,command=run_main_script , fg_color='#409252', hover_color="#306D3D")
run_main_script_button.pack(padx = 10, pady = 10)


#loss_curve

# Read the loss values from the CSV file
loss_curve_df = pd.read_csv("loss_curve.csv")
df = pd.read_csv("classifier_results.csv")

accuracy_data = df[['Classifier', 'Accuracy', 'Color']]
precision_data = df[['Classifier', 'Precision', 'Color']]

def plot_loss_curve():
    
    # Plot the loss curve
    
    #plt.plot(loss_curve_df["loss"], label="Loss Curve", alpha = 1, color = "purple")
    #plt.fill_between(range(len(loss_curve_df)), loss_curve_df["loss"], alpha=0.5, color="blue")
    
    fig_1 = Figure(figsize = (3.5,3.5), facecolor= "#313131")
    ax_1 = fig_1.add_subplot()
    ax_1.set_facecolor("#313131") 
    ax_1.fill_between(range(len(loss_curve_df)), loss_curve_df["loss"], alpha=0.5, color="#FF6978")
    ax_1.tick_params(labelsize = 9, colors = "white")
    fig_1.autofmt_xdate()
    #ax_1.grid(visible=True)
    ax_1.set_frame_on(False)
    
    Canvas = FigureCanvasTkAgg(figure=fig_1, master = bottom_left_frame)
    Canvas.draw()
    Canvas.get_tk_widget().place(x = 5, y = 0.5)
    
#plot accuracy curve
def plot_accuracy_curve():    
    fig_2 = Figure(figsize = (3.5,3.5), facecolor= "#313131")
    ax_2 = fig_2.add_subplot()
    ax_2.set_facecolor("#313131")
    ax_2.bar(accuracy_data['Classifier'], accuracy_data['Accuracy'], color = accuracy_data['Color'], alpha = 0.7)
    ax_2.tick_params(labelsize = 9, colors = "white")
    ax_2.set_frame_on(False)
    fig_2.autofmt_xdate()
    
    Canvas = FigureCanvasTkAgg(figure=fig_2, master = bottom_middle_frame)
    Canvas.draw()
    Canvas.get_tk_widget().place(x = 20, y = 0.5)
    



#plot precision curve
def plot_precision_curve():    
    fig_3 = Figure(figsize = (3.5,3.5), facecolor= "#313131")
    ax_3 = fig_3.add_subplot()
    ax_3.set_facecolor("#313131")
    ax_3.bar( precision_data['Classifier'], precision_data['Precision'], color = precision_data['Color'], alpha = 0.7)
    ax_3.tick_params(labelsize = 9, colors = "white")
    fig_3.autofmt_xdate()
    ax_3.set_frame_on(False)
    
    Canvas = FigureCanvasTkAgg(figure=fig_3, master = bottom_right_frame)
    Canvas.draw()
    Canvas.get_tk_widget().place(x = 20, y = 0.5)
    
'''
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.legend()
plt.grid(True)

# Show the plot or save it to a file
plt.show()
'''
#end_loss_curve


#record

run_sound_recorder_script = 0



#plot_label
plot_label = customtkinter.CTkLabel(master=left_bottom_frame, text = "PLOT GRAPHS" ,font = ("Helvetica", 15, "bold"))
plot_label.pack(padx = 5, pady = 5)

#plot_loss_curve_button
loss_curve_button = customtkinter.CTkButton(master=left_bottom_frame, text="LOSS CURVE",command=plot_loss_curve, fg_color='#92407B', hover_color="#6A2E59")
loss_curve_button.pack(padx = 10, pady = 10)

#plot_accuracy_curve_button
accuracy_curve_button = customtkinter.CTkButton(master=left_bottom_frame, text="ACCURACY CURVE" ,command=plot_accuracy_curve, fg_color='#92407B', hover_color="#6A2E59")
accuracy_curve_button.pack(padx = 10, pady = 10)

#plot_precision_curve_button
precision_curve_button = customtkinter.CTkButton(master=left_bottom_frame, text="Precision CURVE" ,command=plot_precision_curve, fg_color='#92407B', hover_color="#6A2E59")
precision_curve_button.pack(padx = 10, pady = 10)

record = customtkinter.CTkLabel(master = inside_frame, text = "00:00:00")
record.pack(padx = 1, pady = 1,side = "bottom")
recording = False
def click_handler():
    global recording
    if recording:
        recording = False
        run_sound_recorder_script.configure(fg_color="#6b6b6b", hover_color = "#828181")
    else:
        recording = True
        run_sound_recorder_script.configure(fg_color = "#761515", hover_color = "#783636")
        threading.Thread(target=record_audio).start()
def record_audio():
    audio = pyaudio.PyAudio()
    stream = audio.open(format = pyaudio.paInt16, channels=1, rate=44100,
                        input = True, frames_per_buffer=1024)
    
    frames = []
    start = time.time()
    
    while recording:
        data = stream.read(1024)
        frames.append(data)
        
        passed = time.time() - start
        sec = passed % 60
        mins = passed // 60
        hours = mins // 60
        
        record.configure(text = f"{int(hours):02d}:{int(mins):02d}:{int(sec):02d}") 
    stream.stop_stream()
    stream.close()
    audio.terminate()
    
    
    folder_path = 'sounds'
    if os.path.exists(folder_path):
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            try:
                if os.path.isfile(file_path):
                    os.remove(file_path)
            except Exception as e:
                print(f"Error deleting file {file_path}: {str(e)}")

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        
    
    
    while True:
        if not os.path.exists(os.path.join(folder_path, "recording.wav")):
            break
        
            
            
    sound_file = wave.open(os.path.join(folder_path, "recording.wav"), "wb")
    sound_file.setnchannels(1)
    sound_file.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
    sound_file.setframerate(44100)
    sound_file.writeframes(b"".join(frames))
    sound_file.close()
    saved = "Recording saved!"
    update_output(saved)
#record_end
run_sound_recorder_script = customtkinter.CTkButton(master=inside_frame, text = "Record Voice",command = click_handler, fg_color="#6b6b6b", hover_color = "#828181")
run_sound_recorder_script.pack(padx = 10, pady = 10)



run_neural_net = customtkinter.CTkButton(master=left_frame, text = "Train Neural Net",command =lambda: run_scripts("neural_net.py") , fg_color='#409252', hover_color="#306D3D")
run_neural_net.pack(padx = 10, pady = 10)

run_gender = customtkinter.CTkButton(master=left_frame, text = "Get Comparison",command =lambda: run_scripts("clf_comparison.py") , fg_color='#409252', hover_color="#306D3D")
run_gender.pack(padx = 10, pady = 10)

#output_frame
output_frame = customtkinter.CTkFrame(master=root, border_width= 1)
output_frame.pack(padx=10, pady=5, fill = BOTH, expand = False)

#entry
'''
entry = customtkinter.CTkEntry(root, placeholder_text="CTkEntry")
entry.pack()
'''
output_textbox = customtkinter.CTkTextbox(output_frame, state = "disabled", wrap = "word", font = ("Helvetica", 20, "bold"), width = 600, height=300, fg_color= "#373636")
output_textbox.pack(pady = 20)

'''
output_textbox.configure(state="enabled") #enable widget
output_textbox.delete("0.0", "end")  # delete all text
output_textbox.insert("0.0", "new text to insert")  # insert at line 0 character 0
#text = output_textbox.get("0.0", "end")  # get text from line 0 character 0 till the end
output_textbox.configure(state="disabled")  # configure textbox to be read-only
'''

#label
'''
label = customtkinter.CTkLabel(root, text="CTkLabel", fg_color="transparent")
label.pack()
'''

#run root
root.mainloop()