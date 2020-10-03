import tkinter as tk
from tkinter import ttk
from tkinter import font,colorchooser,filedialog,messagebox
import os
root=tk.Tk()
root.geometry("1000x600")
root.title('Text Editor')
root.wm_iconbitmap("Hopstarter-Soft-Scraps-Text-Edit.ico")
# .............Main Menu...............................................
#.............End main Menu............................................
main_menu=tk.Menu()
# ........file icon.....
new_icon=tk.PhotoImage(file="Icon/new.png")
open_icon=tk.PhotoImage(file="Icon\open.png")
save_icon=tk.PhotoImage(file='Icon\save.png')
exit_icon=tk.PhotoImage(file='Icon\exit(13).png')
# .....edit..............................................................
copy_icon=tk.PhotoImage(file='Icon\Copy.png')
paste_icon=tk.PhotoImage(file='Icon\paste.png')
cut_icon=tk.PhotoImage(file='Icon\icons8-cut-48.png')
clear_all_icon=tk.PhotoImage(file='Icon\Clear_all.png')
find_icon=tk.PhotoImage(file='Icon/find1.png')
# .......View..............................................................
tool=tk.PhotoImage(file='Icon/tool_bar.png')
status=tk.PhotoImage(file='Icon\status.png')
# ......color theme>........................................................
white_icon=tk.PhotoImage(file='Icon\circle-32 (5).png')
blue_icon=tk.PhotoImage(file='Icon\circle-32 (2).png')
black_icon=tk.PhotoImage(file='Icon\circle-32 (6).png')
red_icon=tk.PhotoImage(file='Icon\circle-32 (1).png')
cyan_icon=tk.PhotoImage(file='Icon\circle-32 (7).png')
them_choice=tk.StringVar()
color_icon=(white_icon,blue_icon,black_icon,red_icon,cyan_icon)
color_dict={
    # Within tuple first one is text value and second background color
    'Light Default' :('#000000','#ffffff'),
    'Green':('#000000','#000fff000'),
    'Dark':('#c4c4c4','#2d2d2d'),
    'Red':('#2d2d2d','#ffe8e8'),
    'Cyan':('#000000','#00ffff')
}


file=tk.Menu(main_menu,tearoff=False)

edit=tk.Menu(main_menu,tearoff=False)

view=tk.Menu(main_menu,tearoff=False)

color_theme=tk.Menu(main_menu,tearoff=False)

#......... cascade.......................................................................
main_menu.add_cascade(label='File',menu=file)
main_menu.add_cascade(label='Edit',menu=edit)
main_menu.add_cascade(label='View',menu=view)
main_menu.add_cascade(label='Color Theme',menu=color_theme)
# .............toolbar.....................................................................
tool_bar=ttk.Label(root)
tool_bar.pack(side=tk.TOP,fill=tk.X)
# font box
font_tuple=tk.font.families()
font_family=tk.StringVar()
font_box=ttk.Combobox(tool_bar,width=30,textvariable=font_family,state='readonly')
font_box['values']=font_tuple
font_box.current(font_tuple.index('Arial'))
font_box.grid(row=0,column=0)
# size box
size_var=tk.IntVar()
font_size=ttk.Combobox(tool_bar,width=14,textvariable=size_var,state='readonly')
font_size['values']=tuple(range(8,80,2))
font_size.current(3)
font_size.grid(row=0,column=1,padx=5)
# bold button
bold_icon=tk.PhotoImage(file='Icon\icons8-bold-26.png')
bold_button=ttk.Button(tool_bar,image=bold_icon)
bold_button.grid(row=0,column=2,padx=5)
#italic button
italic_icon=tk.PhotoImage(file='Icon\icons8-italic-26.png')
italic_button=ttk.Button(tool_bar,image=italic_icon)
italic_button.grid(row=0,column=3,padx=5)
# under line button
underline_icon=tk.PhotoImage(file='Icon\icons8-underline-24.png')
underline_button=ttk.Button(tool_bar,image=underline_icon)
underline_button.grid(row=0,column=4,padx=5)
# font color button
font_color_icon=tk.PhotoImage(file='Icon\icons8-text-color-30.png')
font_color_button=ttk.Button(tool_bar,image=font_color_icon)
font_color_button.grid(row=0,column=5,padx=5)
# align left
align_left=tk.PhotoImage(file='Icon\icons8-align-left-24.png')
align_left_button=ttk.Button(tool_bar,image=align_left)
align_left_button.grid(row=0,column=6,padx=5)
# align center
align_center=tk.PhotoImage(file='Icon\icons8-align-center-24.png')
align_center_button=ttk.Button(tool_bar,image=align_center)
align_center_button.grid(row=0,column=7,padx=5)
# align right
align_right=tk.PhotoImage(file='Icon\icons8-align-right-24.png')
align_right_button=ttk.Button(tool_bar,image=align_right)
align_right_button.grid(row=0,column=8,padx=5)
#.............End main Menu......,.......................................................

# .............text editor.................................................................
text_editor=tk.Text(root)
text_editor.config(wrap='word',relief=tk.FLAT)
scroll_bar=tk.Scrollbar(root)
text_editor.focus_set()
scroll_bar.pack(side=tk.RIGHT,fill=tk.Y)
text_editor.pack(fill=tk.BOTH,expand=True)
scroll_bar.config(command=text_editor.yview)
text_editor.config(yscrollcommand=scroll_bar.set)


# font family and font size functionality
current_font_faimly='Arial'
current_font_size=12
def change_font(root):
    global current_font_faimly
    current_font_faimly=font_family.get()
    text_editor.config(font=(current_font_faimly,current_font_size))
def change_size(root):
    global current_font_size
    current_font_size=size_var.get()
    text_editor.config(font=(current_font_faimly,current_font_size))
font_box.bind("<<ComboboxSelected>>",change_font)
font_size.bind("<<ComboboxSelected>>",change_size)
# bold button functionality
def change_bold():
    text_property=tk.font.Font(font=text_editor['font'])
    if text_property.actual()['weight']=='normal':
        text_editor.configure(font=(current_font_faimly,current_font_size,'bold'))
    if text_property.actual()['weight']=='bold':
        text_editor.configure(font=(current_font_faimly,current_font_size,'normal'))
bold_button.config(command=change_bold)
# italic button functonality
def change_italic():
    text_property=tk.font.Font(font=text_editor['font'])
    if text_property.actual()['weight']=='normal':
        text_editor.configure(font=(current_font_faimly,current_font_size,'italic'))
    if text_property.actual()['weight']=='italic':
        text_editor.configure(font=(current_font_faimly,current_font_size,'normal'))
italic_button.config(command=change_italic)
# Underline button functionality
def change_Underline():
    text_property=tk.font.Font(font=text_editor['font'])
    if text_property.actual()['weight']=='normal':
        text_editor.configure(font=(current_font_faimly,current_font_size,'underline'))
    if text_property.actual()['weight']=='underline':
        text_editor.configure(font=(current_font_faimly,current_font_size,'normal'))
underline_button.config(command=change_Underline)
# font color functionality
def change_font_color():
    color_var=tk.colorchooser.askcolor()
    text_editor.configure(fg=color_var[1])
font_color_button.configure(command=change_font_color)
# align functionality
# for left align
def align_left1():
    text_content=text_editor.get(1.0,'end')
    text_editor.tag_config('left',justify=tk.LEFT)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_content,'left')
align_left_button.configure(command=align_left1)
# for center align
def align_center1():
    text_content=text_editor.get(1.0,'end')
    text_editor.tag_config('center',justify=tk.CENTER)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_content,'center')
align_center_button.configure(command=align_center1)
# for right align
def align_right1():
    text_content=text_editor.get(1.0,'end')
    text_editor.tag_config('right',justify=tk.RIGHT)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_content,'right')
align_right_button.configure(command=align_right1)



text_editor.config(font=('Arial',20))
#.............End main Menu................................................................

# .............main status bar.............................................................
status_bar=ttk.Label(root,text='Status Bar' )
status_bar.pack_configure(side=tk.BOTTOM)

text_changed=False
def changed(event=None):
    global text_changed
    if text_editor.edit_modified():
        text_changed=True
        words=len(text_editor.get(1.0,'end-1c').split())
        chracters=len(text_editor.get(1.0,'end-1c').replace(' ',''))
        status_bar.config(text=f'Characters:{chracters} Words:{words}')
    text_editor.edit_modified(False)
text_editor.bind('<<Modified>>',changed)
#.............End main Menu......

# .............Main menu functinality.......................................................
url=''
def new_file(event=None):
    global url
    url=''
    text_editor.delete(1.0,tk.END)
file.add_command(label='New',compound=tk.LEFT,accelerator='Ctrl+N',image=new_icon,command=new_file)
file.add_separator()
def open_file(event=None):
    global url
    url=filedialog.askopenfilename(initialdir=os.getcwd(),title='Select File',filetypes=(('Text File','*.txt'),('All files','*.*')))
    try:
        with open(url,'r') as fr:
            text_editor.delete(1.0,tk.END)
            text_editor.insert(1.0,fr.read())
    except FileNotFoundError:
        return
    except:
        return
    root.title(os.path.basename(url))
file.add_command(label='Open',compound=tk.LEFT,accelerator='Ctrl+O',image=open_icon,command=open_file)
file.add_separator()


def save_file(event=None):
    global url
    try:
        if url:
            content=str(text_editor.get(1.0,tk.END))
            with open(url,'w',encoding='utf-8') as fr:
                fr.write(content)
        else:
            url=filedialog.asksaveasfile(mode='w',defaultextension='.txt',filetypes=(('Text File','*.txt'),('All files','*.*')))
            content2=text_editor.get(1.0,tk.END)
            url.write(content2)
            url.close()
    except:
        return
# def save_as(event=None):
#     global url
#     try:
#         content=str(text_editor.get(1.0,tk.END))
#         url=filedialog.asksaveasfile(mode='w',defaultextension='.txt',filetypes=(('Text File','*.txt'),('All files','*.*')))
#         url.write(content)
#         url.close()
#     except:
#         return

file.add_command(label='Save',compound=tk.LEFT,accelerator='Ctrl+S',image=save_icon , command=save_file)
file.add_separator()
def exit_func(event=None):
    global url ,text_changed
    try:
        if text_changed:
            mbox=messagebox.askyesnocancel('Warning','Do you want to save file ?')
            if mbox:
                if url:
                    content=text_editor.get(1.0,tk.END)
                    with open(url,'w',encoding='utf-8') as fw:
                        fw.write(content)
                        root.destroy()
                else:
                    content2=str(text_editor.get(1.0,tk.END))
                    url=filedialog.asksaveasfile(mode='w',defaultextension='.txt',filetypes=(('Text File','*.txt'),('All files','*.*')))
                    url.write(content2)
                    url.close()
                    root.destroy()
            elif mbox is False:
                root.destroy()
        else:
            root.destroy()
    except:
        return
file.add_command(label='Exit',compound=tk.LEFT,accelerator='Ctrl+Q',image=exit_icon , command=exit_func)
file.add_separator()

edit.add_command(label='Copy',image=copy_icon,compound=tk.LEFT,accelerator='Ctrl+C',command=lambda:text_editor.event_generate("<Control c>"))
edit.add_separator()
edit.add_command(label='Paste',image=paste_icon,compound=tk.LEFT,accelerator='Ctrl+V',command=lambda:text_editor.event_generate("<Control v>"))
edit.add_separator()
edit.add_command(label='Cut',image=cut_icon,compound=tk.LEFT,accelerator='Ctrl+X',command=lambda:text_editor.event_generate("<Control x>"))
edit.add_separator()
edit.add_command(label='Clear All',image=clear_all_icon,compound=tk.LEFT,accelerator='Ctrl+Alt+C',command=lambda:text_editor.delete(1.0,tk.END))
edit.add_separator()

def find_func(event=None):
    def find():
        word=find_input.get()
        text_editor.tag_remove('match','1.0',tk.END)
        matches=0
        if word:
            start_pos='1.0'
            while True:
                start_pos=text_editor.search(word,start_pos,stopindex=tk.END)
                if not start_pos:
                    break
                end_pos=(f'{start_pos}+{len(word)}c')
                text_editor.tag_add('match',start_pos,end_pos)
                matches+=1
                start_pos=end_pos
                text_editor.tag_configure('match',foreground='red',background='yellow')
    def replace():
        word=find_input.get()
        replace_text=replace_input.get()
        content=text_editor.get(1.0,tk.END)
        new_content=content.replace(word,replace_text)
        text_editor.delete(1.0,tk.END)
        text_editor.insert(1.0,new_content)


    find_dialogue=tk.Toplevel()
    find_dialogue.geometry('450x250+500+200')
    find_dialogue.title("Find")
    find_dialogue.resizable(0,0)
    ## frame
    find_frame=ttk.LabelFrame(find_dialogue,text='Find/Repalce')
    find_frame.pack(pady=20)
    ## labels
    text_find_label=ttk.Label(find_frame,text='Find : ')
    text_replace_label=ttk.Label(find_frame,text='Replace')
    ## entry
    find_input=ttk.Entry(find_frame,width=30)
    replace_input=ttk.Entry(find_frame,width=30)
    ## button
    find_button=ttk.Button(find_frame,text="Find" ,command=find)
    replace_button=ttk.Button(find_frame,text='Replace',command=replace)
    # grid
    text_find_label.grid(row=0,column=0,padx=4,pady=4)
    text_replace_label.grid(row=1,column=0,padx=4,pady=4)

    find_input.grid(row=0,column=1,padx=4,pady=4)
    replace_input.grid(row=1,column=1,padx=4,pady=4)

    find_button.grid(row=2,column=0,padx=8,pady=4)
    replace_button.grid(row=2,column=1,padx=8,pady=4)

    find_dialogue.mainloop()

edit.add_command(label='Find',image=find_icon,compound=tk.LEFT,accelerator='Ctrl+F', command=find_func)
edit.add_separator()

# Toolbar functionalty
show_statusbar=tk.BooleanVar()
show_statusbar.set(True)
show_toolbar=tk.BooleanVar()
show_toolbar.set(True)

def show_toolbar():
    global show_toolbar
    if show_toolbar:
        tool_bar.pack_forget()
        show_toolbar=False
    else:
        text_editor.pack_forget()
        status_bar.pack_forget()
        tool_bar.pack(side=tk.TOP,fill=tk.X)
        text_editor.pack(fill=tk.BOTH,expand=True)
        status_bar.pack(side=tk.BOTTOM)
        show_statusbar=True
def hide_statusbar():
    global show_statusbar
    if show_statusbar:
        status_bar.pack_forget()
        show_statusbar=False
    else:
        status_bar.pack(side=tk.BOTTOM)
        show_statusbar=True

view.add_checkbutton(label='Tool bar',image=tool,onvalue=True,offvalue=False,compound=tk.LEFT,variable=show_toolbar ,command=show_toolbar)
view.add_separator()
view.add_checkbutton(label='Status bar',image=status,onvalue=True,offvalue=False,compound=tk.LEFT,variable=show_statusbar, command=hide_statusbar)
view.add_separator()
# theme functionalty
def change_theme():
    chosen_theme=them_choice.get()
    color_tuple=color_dict.get(chosen_theme)
    fg_color,bg_color=color_tuple[0],color_tuple[1]
    text_editor.config(background=bg_color,fg=fg_color)

count=0
for i in color_dict:
    color_theme.add_radiobutton(label=i,image=color_icon[count],variable=them_choice,compound=tk.LEFT,command=change_theme)
    count+=1
#.............End main Menu.................................................................
root.config(menu=main_menu)

root.bind("<Control-n>",new_file)
root.bind("<Control-o>",open_file)
root.bind("<Control-s>",save_file)
root.bind("<Control-q>",exit_func)
root.bind("<Control-f>",find_func)

root.mainloop()