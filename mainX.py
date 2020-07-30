from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog

root =  Tk()
root.title("Sophisticated Fingerprint Authentication System")
e= Entry(root , borderwidth=5)
e.get()
root.configure(bg="black")
root.geometry("900x500")


def open():
	global my_image,my_label,my_image_label
	top=Toplevel()
	top.filename = filedialog.askopenfilename(initialdir = "D:/downloads2/FAER/Enhancement CodeBase", title="Select A File", filetypes=(("jpg files", "*.jpg"),("all files", "*.*")))
	my_label = Label(top, text=top.filename).pack()
	my_image = ImageTk.PhotoImage(Image.open(top.filename))
	my_image_label  = Label(image=my_image).pack()
	#top.pack()

def get_enhanced():
	top = Toplevel()
	top.configure(bg="yellow")
	top.geometry("700x500")

	
	top.title("Fingerprint Enhancement")
	#open_button = Button(top, text= "Open File",command=open).pack()
	#my_image_label.pack()
	#my_label.pack()

def get_validated():
	top = Toplevel()
	top.configure(bg="black")
	top.title("Fingerprint Validation")
	top.geometry("700x400")
	

Enhancement = Button(root, text="Enhancement",command=get_enhanced,fg="white",bg="green",padx=60,pady=30)
Validation = Button(root, text="Validation",command=get_validated,fg="white",bg="green",padx=70,pady=30)
Upload = Button(root, text= "Upload",command=open,fg="white",bg="green",padx=60,pady=30)
Enhancement.grid(row =1,column=6)
Validation.grid(row=2,column=6)
Upload.grid(row=1,column=4)
Enhancement.place(x=500,y=50)
Validation.place(x=500,y=200)
Upload.place(x=100,y=368)
#fingerimage = ImageTk.PhotoImage(Image.open("fingerbgm.jpg"))
#finger_label=Label(image=fingerimage)
#finger_label.place(relx = 0.3, rely = 0.3, anchor = 'e') 

root.mainloop()

