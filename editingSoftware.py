import tkinter as tk
from tkinter import filedialog
from moviepy.editor import *

window = tk.Tk()
window.title("Video Editor")
window.geometry("400x200")

def open_video():
    global video_file
    video_file = filedialog.askopenfilename()
    lbl = tk.Label(window)
    lbl.pack()
    video = tk.Label(window)
    video.pack()
    video_clip = tk.PhotoImage(file=video_file)
    video.configure(image=video_clip)

def edit_video():
    clip = VideoFileClip(video_file)
    clip.audio.write_audiofile(video_file.replace(".mp4", ".mp3"))
    clip.close()
    edited_clip = VideoFileClip(video_file.replace(".mp4", ".mp3"))
    edited_clip.write_videofile(video_file.replace(".mp4", "_edited.mp4"))

btn = tk.Button(window, text="Open Video", command=open_video)
btn.pack()
btn2 = tk.Button(window, text="Edit Video", command=edit_video)
btn2.pack()

window.mainloop()

