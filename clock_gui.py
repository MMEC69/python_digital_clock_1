from tkinter import Label, Tk
import clock_time as ct

app_window = Tk()
app_window.title("digital_clock")
app_window.geometry("580x200")
app_window.resizable(1,1)

text_font = ("Lato", 100, 'bold')
background_color = "red"
foreground_color = "white"
border_width = 25

label = Label(app_window, font=text_font, bg=background_color, fg=foreground_color, bd=border_width)
label.grid(row=0, column=1)


def time_clock_gui_connector():
    live_time = ct.get_time()
    label.config(text=live_time)
    label.after(200, time_clock_gui_connector)

time_clock_gui_connector()

app_window.mainloop()




