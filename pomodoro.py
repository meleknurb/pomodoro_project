from tkinter import  *

root = Tk()
root.title('Pomodoro Timer')
root.geometry('720x350+500+150')
root.config(bg='#4682b4')

title_label = Label(root,text='POMODORO TIMER',fg='white',bg='#4682b4',font='Georgia,serif 30 bold')
title_label.place(x=160,y=20)

info_label = Label(root,text='FREESTYLE MODE(You Can Set Your Own Studying Time)',fg='white',bg='#4682b4',font='Georgia,serif 8 bold')
info_label.place(x=190,y=80)

time_display = Label(root,fg='white',bg='#4682b4',font='Georgia,serif 60 bold',width=10,height=1)
time_display.place(x=110,y=115)

study_time = 25
break_time = 5
remaining_time = study_time*60
timer_running = False
back_ground = False
current_mode = 'study'

def update_timer():
    global remaining_time
    if timer_running:
        minutes = remaining_time // 60
        seconds = remaining_time % 60
        time_format = f'{minutes:02}:{seconds:02}'
        time_display.config(text=time_format)

        if remaining_time > 0:
            remaining_time -= 1
            root.after(1000,update_timer)
        else:
            time_display.config(text='Time\'s Up!')
            stop_timer()

def start_timer():
    global remaining_time
    global timer_running
    if not timer_running:
        timer_running = True
        reset_button.place_forget()
        start_button.place_forget()
        study_button.place_forget()
        break_button.place_forget()
        mode_button.place_forget()
        stop_button.place(x=250,y=230)

        if remaining_time == study_time * 60 or remaining_time == break_time*60:

            if current_mode == 'study':
                remaining_time = study_time * 60
            else:
                remaining_time = break_time * 60

        update_timer()

def stop_timer():
    global timer_running
    timer_running = False
    stop_button.place_forget()
    start_button.place(x=250,y=230)
    study_button.place(x=50,y=110)
    break_button.place(x=50,y=205)
    mode_button.place(x=620,y=110)
    check_reset_button()

def set_study_time():
    global remaining_time
    global current_mode
    if not timer_running:
        current_mode = 'study'
        remaining_time = study_time * 60
        update_display()

def set_break_time():
    global remaining_time
    global current_mode
    if not timer_running:
        current_mode = 'break'
        remaining_time = break_time * 60
        update_display()

def toggle_mode():
    global back_ground
    back_ground = not back_ground
    if back_ground:
        apply_dark_mode()
    else:
        apply_light_mode()

def apply_light_mode():
    root.config(bg='#4682b4')
    title_label.place(x=160,y=20)
    info_label.place(x=190,y=80)
    settings_button.place(x=610,y=20)
    update_labels_bg_light()

def apply_dark_mode():
    root.config(bg='#d02090')
    update_labels_bg_dark()

def update_labels_bg_light():
    title_label.config(bg='#4682b4')
    info_label.config(bg='#4682b4')
    time_display.config(bg='#4682b4')
    start_button.config(bg='#4682b4',activebackground='#4682b4')
    stop_button.config(bg='#4682b4',activebackground='#4682b4')
    mode_button.config(bg='#d02090',activebackground='#d02090')

def update_labels_bg_dark():
    title_label.config(bg='#d02090')
    info_label.config(bg='#d02090')
    time_display.config(bg='#d02090')
    start_button.config(bg='#d02090',activebackground='#d02090')
    stop_button.config(bg='#d02090',activebackground='#d02090')
    mode_button.config(bg='#4682b4',activebackground='#4682b4')
    break_button.config(bg='#27408b',activebackground='#27408b')

def check_reset_button():
    global remaining_time
    if remaining_time in [study_time*60,break_time*60]:
        reset_button.place_forget()
    else:
        reset_button.place(x=620,y=205)

def reset_timer():
    global remaining_time
    if not timer_running:
        if current_mode == 'break':
            remaining_time = break_time * 60
        else:
            remaining_time = study_time * 60
        
        update_display()
        check_reset_button()

def update_display():
    minutes = remaining_time // 60
    seconds = remaining_time % 60
    time_display.config(text=f'{minutes:02}:{seconds:02}')

def open_settings():
    global study_time,break_time
    settings_window = Toplevel(root)
    settings_window.title('Settings')
    settings_window.geometry('400x200+660+260')
    settings_window.config(bg='#8db6cd')

    Label(settings_window,text='Study Time (minutes)',fg='black',bg='#8db6cd',font='Georgia,serif 12 bold').pack(pady=10)
    study_entry = Entry(settings_window)
    study_entry.pack()

    Label(settings_window,text='Break Time (minutes)',fg='black',bg='#8db6cd',font='Georgia,serif 12 bold').pack(pady=10)
    break_entry = Entry(settings_window)
    break_entry.pack()

    def save_settings():
        global study_time,break_time
        try:
            study_time = int(study_entry.get())
            break_time = int(break_entry.get())
        except ValueError:
            study_time = 25
            break_time = 5
        
        settings_window.destroy()
        reset_timer()
    
    Button(settings_window,text='Save',fg='#191970',bg='#8db6cd',activeforeground='#191970',activebackground='#8db6cd',
           font='Georgia,serif 16 bold',borderwidth=0,relief='flat',command=save_settings).pack(pady=20)

time_display.config(text=f'{study_time:02}:00')

start_button = Button(root,text='TOUCH TO START',fg='white',bg='#4682b4',activeforeground='white',activebackground='#4682b4',
                      font='Georgia,serif 17 bold',borderwidth=0,relief='flat',command=start_timer)
start_button.place(x=250,y=230)

stop_button = Button(root,text='TOUCH TO STOP',fg='white',bg='#4682b4',activeforeground='white',activebackground='#4682b4',
                      font='Georgia,serif 17 bold',borderwidth=0,relief='flat',command=stop_timer)
stop_button.place_forget()


study_button = Button(root,text='Study',fg='white',bg='#eead0e',activeforeground='white',activebackground='#eead0e',
                      font='Georgia,serif 15 bold',borderwidth=0,relief='flat',command=set_study_time)
study_button.place(x=50,y=110)

break_button = Button(root,text='Break',fg='white',bg='#cd6600',activeforeground='white',activebackground='#cd6600',
                      font='Georgia,serif 15 bold',borderwidth=0,relief='flat',command=set_break_time)
break_button.place(x=50,y=205)

mode_button = Button(root,text='Mode',fg='white',bg='#d02090',activeforeground='white',activebackground='#d02090',
                     font='Georgia,serif 15 bold',borderwidth=0,relief='flat',command=toggle_mode)
mode_button.place(x=620,y=110)

reset_button = Button(root,text='Reset',fg='white',bg='#ff82ab',activeforeground='white',activebackground='#ff82ab',
                      font='Georgia,serif 15 bold',borderwidth=0,relief='flat',command=reset_timer)
reset_button.place(x=620,y=205)

settings_button = Button(root,text='Settings',fg='white',bg='#696969',activeforeground='black',activebackground='#696969',
                         font='Georgia,serif 14 bold',borderwidth=0,relief='flat',command=open_settings)
settings_button.place(x=610,y=20)

root.mainloop()
