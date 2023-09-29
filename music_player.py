import os
import tkinter as tk
from tkinter import filedialog
from pygame import mixer

def play_music():
    selected_song = playlist_listbox.get(tk.ACTIVE)
    if selected_song:
        selected_song_path = os.path.join(music_directory, selected_song)
        mixer.music.load(selected_song_path)
        mixer.music.play()

def stop_music():
    mixer.music.stop()

def pause_music():
    mixer.music.pause()

def unpause_music():
    mixer.music.unpause()

def select_music_directory():
    global music_directory
    music_directory = filedialog.askdirectory()
    update_playlist()

def add_song_to_playlist():
    song = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3 *.wav")])
    if song:
        song = os.path.basename(song)
        playlist_listbox.insert(tk.END, song)

def remove_song_from_playlist():
    selected_song_index = playlist_listbox.curselection()
    if selected_song_index:
        playlist_listbox.delete(selected_song_index)

def update_playlist():
    playlist_listbox.delete(0, tk.END)
    if music_directory:
        for root, dirs, files in os.walk(music_directory):
            for file in files:
                if file.endswith((".mp3", ".wav")):
                    playlist_listbox.insert(tk.END, file)

# Initialize the pygame mixer
mixer.init()

# Create the main window
root = tk.Tk()
root.title("Advanced Music Player")

# Create and configure buttons
play_button = tk.Button(root, text="Play", command=play_music)
stop_button = tk.Button(root, text="Stop", command=stop_music)
pause_button = tk.Button(root, text="Pause", command=pause_music)
unpause_button = tk.Button(root, text="Unpause", command=unpause_music)
select_dir_button = tk.Button(root, text="Select Music Directory", command=select_music_directory)
add_song_button = tk.Button(root, text="Add Song to Playlist", command=add_song_to_playlist)
remove_song_button = tk.Button(root, text="Remove Song from Playlist", command=remove_song_from_playlist)

# Create a listbox for the playlist
playlist_listbox = tk.Listbox(root, selectmode=tk.SINGLE, height=15, width=50)

# Grid layout for buttons and listbox
play_button.grid(row=0, column=0, padx=10, pady=10)
stop_button.grid(row=0, column=1, padx=10, pady=10)
pause_button.grid(row=0, column=2, padx=10, pady=10)
unpause_button.grid(row=0, column=3, padx=10, pady=10)
select_dir_button.grid(row=1, column=0, padx=10, pady=10)
add_song_button.grid(row=1, column=1, padx=10, pady=10)
remove_song_button.grid(row=1, column=2, padx=10, pady=10)
playlist_listbox.grid(row=2, column=0, columnspan=4, padx=10, pady=10)

# Initialize music_directory variable
music_directory = ""

# Update the playlist with songs from the selected directory
update_playlist()

# Run the application
root.mainloop()
