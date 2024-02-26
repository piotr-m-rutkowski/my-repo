import tkinter
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk

def enter_data():
    firstname=first_name_entry.get()
    lastname=last_name_entry.get()
    reg_check=str(reg_status_var.get())
    age_check=age_spinbox.get()
    tkinter.messagebox.showwarning(title="Warning", message=("Potatoes detected.\n"+str(reg_check)+str(firstname)+" "+str(lastname)))
    
def show_image():
    # Create a Toplevel window
    dialog = tkinter.Toplevel(frame)
    dialog.title("Image Viewer")
    image = Image.open("F:/Work/VisualStudio/IMG_0089.jpg")  # Replace "example.png" with your image file
    photo = ImageTk.PhotoImage(image)
    label = tkinter.Label(dialog, image=photo)
    label.image = photo  # Keep a reference to avoid garbage collection
    label.pack()
    
def show_image2():
    # Create a Toplevel window
    dialog = tkinter.Toplevel(frame)
    dialog.title("Image Viewer")
    pic2check=pic2_spinbox.get()
    filepath="F:/Work/VisualStudio/img"+pic2check+".jpg"
    image = Image.open(filepath)  # Replace "example.png" with your image file
    photo = ImageTk.PhotoImage(image)
    label = tkinter.Label(dialog, image=photo)
    label.image = photo  # Keep a reference to avoid garbage collection
    label.pack()

     
def show_image3():
    # Create a Toplevel window
    dialog = tkinter.Toplevel(frame)
    dialog.title("Image Viewer")
    pic3check=str(var.get())
    filepath2="F:/Work/VisualStudio/i"+pic3check+".jpg"
    image = Image.open(filepath2)  # Replace "example.png" with your image file
    photo = ImageTk.PhotoImage(image)
    label = tkinter.Label(dialog, image=photo)
    label.image = photo  # Keep a reference to avoid garbage collection
    label.pack()   
    print(var.get())

def show_selected():
    selected_value = var.get()
    
#v = tkinter.StringVar(frame, "1") 

options = {" Picture 1" : "1", 
		"Picture 2" : "2", 
		"Picture 3" : "3"
		} 

# the largest, root box
window = tkinter.Tk()
window.title("data entry form")

# frame is contained inside the window
frame=tkinter.Frame(window)

# widgets are being packed, placed, or gridded
frame.pack()

#------- FRAMES
# frame 1 inside main frame with a border and a title
user_info_frame=tkinter.LabelFrame(frame,text="User Information")
user_info_frame.grid(row=0, column=0, padx=10, pady=10)

course_info_frame=tkinter.LabelFrame(frame,text="Employment Status")
course_info_frame.grid(row=1, column=0, sticky="news", padx=10, pady=5)

pics_info_frame=tkinter.LabelFrame(frame,text="Light Entertainment")
pics_info_frame.grid(row=2, column=0, sticky="news", padx=10, pady=5)

pics_info_frame2=tkinter.LabelFrame(frame,text="Not-So-Light Entertainment (!)")
pics_info_frame2.grid(row=3, column=0, sticky="news", padx=10, pady=5)

pics_info_frame3=tkinter.LabelFrame(frame,text="!!- Heavy Stuff -!!")
pics_info_frame3.grid(row=4, column=0, sticky="news", padx=10, pady=5)

# frames inside frame 1
first_name_label=tkinter.Label(user_info_frame, text="first name")
first_name_label.grid(column=0, row=0)
last_name_label=tkinter.Label(user_info_frame, text="last name")
last_name_label.grid(column=1, row=0)

first_name_entry=tkinter.Entry(user_info_frame)
last_name_entry=tkinter.Entry(user_info_frame)
first_name_entry.grid(column = 0, row = 1)
last_name_entry.grid(column=1, row=1)

title_label=tkinter.Label(user_info_frame, text="Title")
title_combobox=ttk.Combobox(user_info_frame, values=["","Mrs","Mr", "Dr", "Potato"])
title_label.grid(column=2, row=0)
title_combobox.grid(column=2, row=1)

age_label=tkinter.Label(user_info_frame, text="Age")
age_spinbox=tkinter.Spinbox(user_info_frame, from_=0, to=110)
age_label.grid(column=0, row=2)
age_spinbox.grid(column=0, row=3)

nationality_label=tkinter.Label(user_info_frame, text="nationality")
nationality_label.grid(column=1, row=2)
nationality_combobox=ttk.Combobox(user_info_frame,values=["","No Nationality","Actual Potato"])
nationality_combobox.grid(column=1, row=3)

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=20, pady=6)

#reg_status_var_str="Well done "+str(first_name_entry.get())
reg_status_var=tkinter.StringVar(value="Well done, keep up the good work ")
reg_label=tkinter.Label(course_info_frame, text="")
reg_check=tkinter.Checkbutton(course_info_frame, text="Do you need a job?", variable=reg_status_var, offvalue="Well done, keep up the good work ", 
                               onvalue="Sounds like maybe you should get a job ")
reg_label.grid(row=0, column=0)
reg_check.grid(row=1, column=0)

for widget in course_info_frame.winfo_children():
    widget.grid_configure(padx=20, pady=0)

terms_label=tkinter.Label(course_info_frame, text="Terms and Conditions")
terms_check=tkinter.Checkbutton(course_info_frame, text="Accept T&C?")
terms_label.grid(row=0, column=1)
terms_check.grid(row=1, column=1)

#Button -> when button is clicked, function enter_data is executed
button=tkinter.Button(course_info_frame, text="Get free life advice.", command=enter_data)
button.grid(row=2, column=0, sticky='news', padx=50, pady=10)

#img viewer button
pic_label=tkinter.Label(pics_info_frame, text="Surprise pics for your enjoyment")
pic_label.grid(column=0, row=0)

button=tkinter.Button(pics_info_frame, text="Show Mischief Image", command=show_image)
button.grid(row=0, column=1, padx=10, pady=10)

pic2_label=tkinter.Label(pics_info_frame2, text="Select number form 1 to 3")
pic2_label.grid(column=0,row=0, padx=10, pady=10)
pic2_spinbox=tkinter.Spinbox(pics_info_frame2, from_=1, to=3)
pic2_spinbox.grid(column=1, row=0, padx=10, pady=10)
pic2button=tkinter.Button(pics_info_frame2, text="Show  Image", command=show_image2)
pic2button.grid(row=0, column=2, padx=10, pady=10)

#button2=tkinter.Button(pics_info_frame, text="Show Photo", command=show_image2)
#button2.grid(row=1, column=0)

var = tkinter.IntVar()

radio_button1 = tkinter.Radiobutton(pics_info_frame3, text="Pic 1", variable=var, value=1, command=show_selected)
radio_button2 = tkinter.Radiobutton(pics_info_frame3, text="Pic 2", variable=var, value=2, command=show_selected)
radio_button3 = tkinter.Radiobutton(pics_info_frame3, text="Pic 3", variable=var, value=3, command=show_selected)
radio_button1.grid(row=0, column=0)
radio_button2.grid(row=0, column=1)
radio_button3.grid(row=0, column=2)
pic3button=tkinter.Button(pics_info_frame3, text="Show  Image", command=show_image3)
pic3button.grid(row=0, column=3, sticky='news',padx=10, pady=10)

# this runs the main application
window.mainloop()



