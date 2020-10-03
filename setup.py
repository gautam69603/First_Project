import cx_Freeze
from cx_Freeze import setup,Executable
import sys
import os
base=None
if sys.platform=='win32':
    base="Win32GUI"
    os.environ['TCL_LIBRARY']=r"C:\Users\DELL\AppData\Local\Programs\Python\Python37-32\tcl\tcl8.6"
    os.environ['L_LIBRARY']=r"C:\Users\DELL\AppData\Local\Programs\Python\Python37-32\tcl\tk8.6"
    executables=[cx_Freeze.Executable('second_project.py',base=base,shortcutName='Text Editor',
    shortcutDir='DesktopFolder',icon='Hopstarter-Soft-Scraps-Text-Edit.ico')]
cx_Freeze.setup(
    name = "Text Editor" ,
    author="Nitin",
    options={'build_exe':{"packages":['tkinter','os'],
    'include_files':['Hopstarter-Soft-Scraps-Text-Edit.ico',
    'tcl86t.dll','tk86t.dll','Icon']}} ,
    version='1.5' ,
    description='Tkinter Application' ,
    executables=executables

)
