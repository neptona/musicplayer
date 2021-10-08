from tkinter import *
import pygame
from tkinter import filedialog
from tkinter import ttk
import time
from mutagen.mp3 import MP3

win=Tk()
win.title("musicplayer")
win.iconbitmap('icon.ico')
win.geometry('500x450+150+150')
pygame.mixer.init()


master_frame=Frame(win)
master_frame.pack(pady=30)

list_music=Listbox(master_frame, width=60, bg="black", height=15, fg="green",selectbackground="gray",selectforeground="green")
list_music.grid(row=0,column=0,padx=20)
#create openfiledialog####################################################
def openfiles():
    songs=filedialog.askopenfilenames(initialdir='/song/',title="choose a file song",filetypes=(("audio flies","*.mp3"),))
    for song  in songs:
        song=song.replace("B:/project/musicplayer/song/","")
        song=song.replace(".mp3","")
        list_music.insert(END,song)
def openfile():
    song=filedialog.askopenfilename(initialdir='/song/',title="choose a file song",filetypes=(("audio flies","*.mp3"),))
    song=song.replace("B:/project/musicplayer/song/","")
    song=song.replace(".mp3","")

    list_music.insert(0,song)

global pus
pus=False
def play():
    song=list_music.get(ACTIVE)
    song=f'B:/project/musicplayer/song/{song}.mp3'
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)
    pygame.mixer.music.set_volume(volume_slider.get())
    current_volume=pygame.mixer.music.get_volume()
    lblsound.config(text=int(current_volume*100))
    timeplay()
def pause(x):
    global pus
    pus=x
    if pus==False:
        pygame.mixer.music.unpause()
        pus=True
    elif pus==True:
        pygame.mixer.music.pause()
        pus=False
def stop():
    pygame.mixer.music.stop()
    list_music.selection_clear(ACTIVE)
def next_song():
    next_one=list_music.curselection()
    next_one=next_one[0]+1
    song=list_music.get(next_one)
    song=f'B:/project/musicplayer/song/{song}.mp3'
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

    list_music.selection_clear(0,END)
    list_music.activate(next_one)
    list_music.selection_set(next_one)
def back_song():
    next_one=list_music.curselection()
    next_one=next_one[0]-1
    song=list_music.get(next_one)
    song=f'B:/project/musicplayer/song/{song}.mp3'
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

    list_music.selection_clear(0,END)
    list_music.activate(next_one)
    list_music.selection_set(next_one)
def remove_songs():
    list_music.delete(ANCHOR)
    pygame.mixer.music.stop()
def remove_song():
    list_music.delete(0,END)
    pygame.mixer.music.stop()
def volume_song(x):
  

    pygame.mixer.music.set_volume(volume_slider.get())
    
    lbltime.after(1000,timeplay)

    current_volume=pygame.mixer.music.get_volume()
    lblsound.config(text=int(current_volume*100))
def timeplay():
    current_time=pygame.mixer.music.get_pos()/1000
    convert_time=time.strftime('%M:%S',time.gmtime(current_time))
    current_song=list_music.curselection()
    song=list_music.get(current_song)
    song=f'B:/project/musicplayer/song/{song}.mp3'
    song_mut=MP3(song)
    song_length=song_mut.info.length
    covert_song_length=time.strftime('%M:%S',time.gmtime(song_length))
   
    lbltime.config(text= f'{convert_time} of {covert_song_length}')
    lbltime.after(1000,timeplay)
   
# Create menubar##########################################################
menubar=Menu(win)
win.config(menu=menubar,bd=3,relief="groove")
filemenu=Menu(menubar,bg="gray",tearoff=0)
filemenu.add_command(label="open files",command=openfiles)
filemenu.add_command(label="openfile",command=openfile)
menubar.add_cascade(label="file",menu=filemenu)
removemenu=Menu(menubar,bg="gray",tearoff=0)
removemenu.add_command(label="remove_songs",command=remove_songs)
removemenu.add_command(label="remove_song",command=remove_song)
menubar.add_cascade(label="remove",menu=removemenu)

#create image of photo####################################################
frame_control=Frame(master_frame)
frame_control.grid(row=1,column=0)
image_forward=PhotoImage(file='image/forward.png')
image_backward=PhotoImage(file='image/back.png')
image_pause=PhotoImage(file='image/pause.png')
image_play=PhotoImage(file='image/play.png')
image_stop=PhotoImage(file='image/stop.png')
image_volume=PhotoImage(file='image/volume.png')

btn_forward=Button(frame_control,image=image_forward,command=next_song)
btn_back=Button(frame_control,image=image_backward,command=back_song)
btn_play=Button(frame_control,image=image_play,command=play)
btn_pause=Button(frame_control,image=image_pause,command=lambda:pause(pus))
btn_stop=Button(frame_control,image=image_stop,command=stop)


btn_back.grid(row=0,column=0,padx=3,pady=20)
btn_stop.grid(row=0,column=1,padx=3,pady=20)
btn_pause.grid(row=0,column=2,padx=3,pady=20)
btn_play.grid(row=0,column=3,padx=3,pady=20)
btn_forward.grid(row=0,column=4,padx=3,pady=20)

volume_slider=ttk.Scale(frame_control,from_=0, to=1,orient=HORIZONTAL,value=1 ,length=100,command= volume_song)
volume_slider.grid(row=1,column=1,pady=20)
lblvolume=Label(frame_control,image=image_volume)
lblvolume.grid(row=1,column=0)
lblsound=Label(frame_control,text="",fg="blue")
lblsound.grid(row=1,column=2)
lbltime=Label(frame_control,text="Time")
lbltime.grid(row=1,column=3)
win.mainloop()