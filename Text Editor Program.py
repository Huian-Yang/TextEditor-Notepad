import os
from tkinter import *
from tkinter import filedialog, colorchooser, font
from tkinter.messagebox import *
from tkinter.filedialog import *

def change_color():
    color = colorchooser.askcolor(title="pick a color....or else")   #create a color chooser
    text_area.config(fg=color[1])                                    #font color chnages to whatever the hex values of the chosen color [index 1]
    
def change_font(*args):
    text_area.config(font=(font_name.get(), size_box.get()))

def new_file():
    window.title("Untitled") #create a window title for new file
    text_area.delete(1.0,END) #delete any text within 

def open_file():
    file = askopenfilename(defaultextension=".txt", 
                           file=[("All Files", "*.*"),
                           ("Text Documents", "*.txt")]) #What is accepted when looking for file
    try:
        window.title(os.path.basename(file))
        text_area.delete(1.0, END)
        
        file = open(file, "r") #open and read file
        
        text_area.insert(1.0, file.read())
        
    except Exception:   #catch all exception
        print("Couldn't read file")
        
    finally:
        file.close() #close our file
        

def save_file():
    global file
    file = filedialog.asksaveasfilename(initialfile='untitled.txt', #initial file name when saving
                                        defaultextension=".txt",  #default save as text file
                                        filetypes=[("All Files", "*.*"), #can save as all files
                                                   ("Text Documents", "*.txt")])  #text document
    
    if file is None: #if file dialog is closed
        return
    
    else:
        try:
            window.title(os.path.basename(file))
            with open(file, "w") as opened_file: #write 
                opened_file.write(text_area.get(1.0, END)) #get our text from 1 to end
            
        except Exception:
            print("couldn't save file")
            
        finally:
            file.close()

def cut():
    text_area.event_generate("<<Cut>>") #cut

def copy():
    text_area.event_generate("<<Copy>>") #copy

def paste():
    text_area.event_generate("<<Paste>>") #paste

def about():
    showinfo("About this program","Write some text in this program...") #title, text (message box)

def quit():
    window.destroy() #close out of window


window = Tk()
window.title("Text Editor Program")
file = None

window_width = 500
window_height = 500
screen_width = window.winfo_screenwidth() #get screen width
screen_height = window.winfo_screenheight() #get screen height

x = int((screen_width / 2) - (window_width / 2)) #how our window will move on x axis
y = int((screen_height / 2) - (window_height / 2)) #how our window will move on y axis 

window.geometry("{}x{}+{}+{}".format(window_width, window_height, x, y)) #window geometry

font_name = StringVar(window)
font_name.set("Arial") #default font

font_size = StringVar(window)
font_size.set("25")

text_area = Text(window, font=(font_name.get(), font_size.get())) #adding text area

scroll_bar = Scrollbar(text_area, command=text_area.yview) #create a scrollbar
window.grid_rowconfigure(0, weight=1) #allow text area to expand
window.grid_columnconfigure(0, weight=1) #allow text area to expand
text_area.grid(sticky=N + E + S + W) #stick N E S W
scroll_bar.pack(side=RIGHT, fill=Y) #create a scrollbar on the right 
text_area.config(yscrollcommand=scroll_bar.set) #configs the text area to have a scroll bar

frame = Frame(window) #create a frame
frame.grid() 

color_button = Button(frame, text="color", command=change_color) #create a color chooge button 
color_button.grid(row=0, column=0) #add the color button to a grid

size_box = Spinbox(frame, from_=1, to=100, textvariable=font_size, command=change_font) #allows us to change the size of font (have to give it a range)
size_box.grid(row=0, column=2) #add spinbox to grid

font_box = OptionMenu(frame, font_name, *font.families(), command=change_font) #add option menu to frame - font.families() will return all the fonts aviable 
font_box.grid(row=0,column=1) #add font box to frame

menu_bar = Menu(window) #create a menu bar
window.config(menu=menu_bar) #config menu bar to our window

file_menu = Menu(menu_bar, tearoff=0)  #create a File menu
menu_bar.add_cascade(label="File", menu=file_menu) #create a drop down menu in the top 
file_menu.add_command(label="New", command=new_file) #add "new" selectiom
file_menu.add_command(label="Open", command=open_file) #add "open" selectiom
file_menu.add_command(label="Save", command=save_file) #add "save" selectiom
file_menu.add_separator() #create a separator between menu bar items 
file_menu.add_command(label="Exit", command=quit) #add "exit" selectiom
 
edit_menu = Menu(menu_bar, tearoff=0) #create a Edit menu
menu_bar.add_cascade(label="Edit",menu=edit_menu) #create a drop down menu
edit_menu.add_command(label="Cut", command=cut) #add "cut" selectiom
edit_menu.add_command(label="Copy", command=copy) #add "copy" selectiom
edit_menu.add_command(label="Paste", command=paste) #add "paste" selectiom

help_menu = Menu(menu_bar, tearoff=0) #create a Help menu
menu_bar.add_cascade(label="Help", menu=help_menu) #create a drop down menu
help_menu.add_command(label="About", command=about) #add "paste" selectiom
 
window.mainloop()






