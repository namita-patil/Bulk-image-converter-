import PIL
from PIL import Image
import os
import sys

try:
	input_dir  = str(sys.argv[1].rstrip('/'))  #path to img source folder
	img_size   = str(sys.argv[2])  #The image size (128, 256,etc)
	output_dir  = str(sys.argv[3].rstrip('/')) #output directory
	print ("starting....")
	print ("Colecting data from %s " % input_dir)
	tclass = [ d for d in os.listdir(input_dir ) ]
	print("tclass: ", tclass)
	counter = 0
	strdc = ''
	hasil = []
	new_file=''
	for x in tclass:
		img_path =  input_dir+'/'+x 
		print("\n\nimg_path: ", img_path)
		out_path = output_dir
		print("\n\nout_path: ",out_path)
		if os.path.exists(out_path):
			img = Image.open(img_path)
			img = img.resize((int(img_size),int(img_size)),Image.ANTIALIAS)
			img = img.convert('RGB')
			fname,extension = os.path.splitext(x)
			img.save(out_path+'/'+fname+'.jpg',"JPEG",quality=95)
			print(f"resized : {fname+'.jpg'}")
	print("Success......")
except Exception as e:
	print ("Error, check Input directory etc : ", e)
	sys.exit(1)