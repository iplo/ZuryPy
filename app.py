from zury import Framework
from Tkinter import *
import sys
import os

class MainApplication():
	def __init__(self):
		self.framework = Framework()
		self.app = self.framework.BrowserApplication()
	def __menu__(self):
		self.menu = Menu(self.app.window)
		filemenu = Menu(self.menu)
		filemenu.add_command(label="Exit", command=sys.exit)
		self.menu.add_cascade(label="File", menu=filemenu)
		self.app.window.config(menu=self.menu)
	def run(self, title):
		self.app.window.title = title
		self.app.window.show(800, 600, True, False)
	class Base():
		def __init__(self):
			self.url = "https://iplo.tk/apps/aad/main.php"
		def __use__(self, Application, url):
			Application.app.window.default_url = url
			return Application

root = MainApplication()
base = root.Base()
root = base.__use__(root, base.url)
root.run("Angels & Demons")