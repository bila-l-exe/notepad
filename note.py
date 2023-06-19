from tkinter import*
from tkinter.filedialog import asksaveasfile, askopenfile
from tkinter.colorchooser import askcolor
root=Tk()
root.title('Notepad')
root.geometry("720x720")
root.iconbitmap("a.ico")
def create():
    t1.delete(0.1, END)
def save():
    files = [('All Files', '*.*'), 
             ('Python Files', '*.py'),
             ('Text Document', '*.txt')]
    file = asksaveasfile(filetypes = files, defaultextension = files)
    text2save=str(t1.get(0.0,END))
    file.write(text2save)
    file.close
def ope():  
    t1.delete(0.1,END)
    file = askopenfile(mode ='r', filetypes =[('All Files', '*.*'), 
             ('Python Files', '*.py'),
             ('Text Document', '*.txt')])
    if file is not None:
        content = file.read()
        t1.insert(0.1,content)
def exit():
    root.quit()
def selectall():
    t1.tag_add("start","1.0","end")
    t1.tag_configure("start", background="blue", foreground="white")
def delete():
     t1.delete("0.1","end")
def bold():
    t1.tag_add("start","1.0","end")
    t1.tag_configure("start", font="Helvetica 12 bold")
def italic():
    t1.tag_add("start","1.0","end")
    t1.tag_configure("start", font="Helvetica 12 italic")
def underlinee():
    t1.tag_add("start","1.0","end")
    t1.tag_configure("start",underline=TRUE)
def bgg():
    colors = askcolor(title="Tkinter Color Chooser")
    t1.configure(bg=colors[1])
def fgg():
    colors = askcolor(title="Tkinter Color Chooser")
    t1.configure(fg=colors[1])
def zomm():
    a=10
    t1.tag_add("start","1.0","end")
    t1.tag_configure("start", font="Helvetica "+str(int(a+100))+"")
    
def zoom():
    a=100
    t1.tag_add("start","1.0","end")
    t1.tag_configure("start", font="Helvetica "+str(int(a-90))+"")


t1=Text(width=200, height=200)
t1.place(x=1,y=1)
menubar = Menu(root)
file=Menu(menubar, tearoff=0)
menubar.add_cascade(label="File" , menu=file)
file.add_command(label="New", command=create)
file.add_command(label="Open", command=ope)
file.add_command(label="Save", command=save)
file.add_command(label="Save As")
file.add_command(label="Exit",command=exit)
edit=Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit" , menu=edit)
edit.add_command(label="cut", command=lambda:t1.event_generate("<<Cut>>"))
edit.add_command(label="Copy", command=lambda:t1.event_generate("<<Copy>>"))
edit.add_command(label="Paste", command=lambda:t1.event_generate("<<Paste>>"))
edit.add_command(label="Select All", command=selectall)
edit.add_command(label="Delete", command=delete)
format=Menu(menubar, tearoff=0)
menubar.add_cascade(label="Format" , menu=format)
format.add_command(label="Word wrap")
format.add_command(label="Font")
format.add_separator()
format.add_command(label="Bold", command=bold)
format.add_command(label="Italic", command=italic)
format.add_command(label="Underline", command=underlinee)
format.add_command(label="Background", command=bgg)
format.add_command(label="Forground", command=fgg)
view=Menu(menubar, tearoff=0)
menubar.add_cascade(label="View" , menu=view)
sub_menu = Menu(view, tearoff=0)
sub_menu.add_command(label='Zoom in', command=zomm)
sub_menu.add_command(label='Zoom out', command=zoom)
sub_menu.add_command(label='Restore Default Zoom')
view.add_cascade(
    label="zoom",
    menu=sub_menu
)
help=Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help" , menu=help)
help.add_cascade(label="Status Bar")
help.add_cascade(label="View Help")
help.add_cascade(label="Send Feedback")
help.add_separator()
help.add_command(
    label='About Notepad',
    command=root.destroy
)

root.config(menu=menubar)

root.mainloop()