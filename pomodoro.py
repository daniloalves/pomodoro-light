from tkinter import Tk, Toplevel, Button, Frame, Label
import tkinter.messagebox as tk_msg
from time import sleep
from datetime import datetime as date

TK_TITLE = "POMO LiGHT"
tk = Tk()
tk.title(TK_TITLE)
tk.focus_get()
Toplevel(tk)

def timer(time=0):
    print(f"Starting sleep {time}")
    sleep(time)
    print("Sleep finish")

def popup(text="null"):   
    tk_msg.showinfo(title="Alert!",message=text,parent=tk)

def log(msg,type="INFO"):
    print(f"[{type}] {msg}")

def main():
    work_hard = 40 # minutes
    soft_time = 7 # minutes

    work_hard = work_hard*60
    soft_time = soft_time*60

    # work_hard = 5 # minutes
    # soft_time = 3 # minutes

    while True:
        popup("Work Hard Now!")
        log(f"[Start] Work Hard Now! - {date.now()}")
        sleep(work_hard)
        log(f"[End] Work Hard Now! - {date.now()}")

        log(f"Soft time by {soft_time} seconds..")
        popup(f"Soft time by {soft_time/60} minutes..")
        log(f"[Start] Soft time by! - {date.now()}")
        sleep(soft_time)
        log(f"[End] Soft time by! - {date.now()}")
        
main()