def install(package):
	for i in package:
		try:
			exec(f"import {i}")
			pass
		except Exception:
			print("Installing {i}")
			os.system(f"pip3 install {i}")
	return None
install(["kivy","kivymd","requests","plyer"])


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
			text : "By using BaapG-Attack you agree our terms of service . This software is free to use and you can use it free of cost . Any damage to any one using this software by you is not our *take* and we are not completely responsible for this."
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
			text : app.b
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
		on_press : app.get_number()
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
phno="""
MDScreen:
	name:"phnno"
	MDLabel:
		text : "Enter sender'S Phone Number"
		font_name : 'Poppins-Regular.ttf'
		font_size : '35sp'
		pos_hint : {"center_x":0.5,"center_y":8}
	MDTextField:
		hint_text : "Indian Number "
		mode:"rectangle"
		halign :"center"
"""






def check_intr():
	import requests
	try:
		requests.get("https://google.com",timeout=0.5)
	except Exception as e:
		return False
	return  True
screen_manager = ScreenManager()
class MyApp(MDApp):
	a = 0	
	b = f"No internet {a}"
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
		screen_manager.add_widget(Builder.load_string(mainv))
		screen_manager.add_widget(Builder.load_string(phno))
		screen_manager.current = "phnno"
		return screen_manager
	def bahimaro(self):

		screen_manager.current = "mainv"
		
	def on_start(self):
		Clock.schedule_once(self.login,12)
	def login(self,obj):
		if os.path.exists("eula.txt"):
			if check_intr() == True:
				screen_manager.current = "net"
			else:
				a =+1 
				screen_manager.current = "netof"
		else:
			screen_manager.current = "perscreen"
	def get_number(self):
		screen_manager.current = "phnno"

	def permission(self):
		Path("eula.txt").touch()
		if check_intr() == True:
			screen_manager.current = "net"
		else:
			a =+1 
			screen_manager.current = "netof"



                 
if __name__ == "__main__" :
	MyApp().run()