from sys import *
import os
from Tkinter import *
from tkFileDialog import *

class AppWindow():
	def __init__(self):
		self.root = Tk()
		self.menu = Menu(self.root)
		self.title = "app"
	def minSize(self, width, height):
		self.root.minsize(width=width, height=height)
	def maxSize(self, width, height):
		self.root.maxsize(width=width, height=height)
	def fixedSize(self, width, height):
		self.root.minsize(width=width, height=height)
		self.root.maxsize(width=width, height=height)
	def launch(self):
		self.root.config(menu=self.menu)
		self.root.title(self.title)
		self.root.mainloop()

def Compiler(name,version,directory,appfile, iconfile, keepassets):
	print("Writing Files...")
	f = open(directory+"/build.py", "w")
	f.write("'''\nUsage IN TERMINAL .. :\n\tpython build.py py2app\n'''\n\nfrom setuptools import setup\n\nAPP = [\"zuryapp.py\"]\nDATA_FILES = [('', ['images']), ('', ['Audio'])]\nOPTIONS = {\n\t'iconfile': \""+iconfile+"\"\n}\n\nsetup(\n\tname = \""+name+"\",\n\tversion = \""+version+"\",\n\tapp = APP,\n\tdata_files = DATA_FILES,\n\toptions = {'py2app': OPTIONS},\n\t  setup_requires = ['py2app']\n)")
	f.close()

	import os
	print("Making Nessecary Files...")
	os.system("touch zuryapp.py")
	print("Files Created!")
	print("Changing Permissions of Created Files...")
	os.system("chmod 755 zuryapp.py")
	print("Copying Your App File...")
	os.system("cp "+appfile+" zuryapp.py")
	print("Copied!")
	print("")
	print("Making Directory(s)...")
	os.system("mkdir images")
	os.system("mkdir Audio")
	print("")
	print("Using Py2App...")
	os.system("python build.py py2app")
	print("Moving Zury Over...")
	os.system("cp zury.py dist/"+name+".app/Contents/Resources")
	print("Moving App Back Directory...")
	os.system("mv dist/"+name+".app ./")
	print("Deleting Unneccesary Folders...")
	os.system("rm -rd dist")
	os.system("rm -rd build")
	os.system("rm -rf zuryapp.py")
	os.system("rm -rf build.py")
	if keepassets:
		os.system("rm -rf zury.pyc")
		print("Done!")
	else:
		os.system("rm -rd Audio")
		os.system("rm -rd images")
		os.system("rm -rf zury.pyc")
		print("Done!")