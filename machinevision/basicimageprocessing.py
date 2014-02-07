#code examples from: Programming computer vision with python by Jan Eric Solem
#are used

from PIL import Image
import os
from numpy import *


def main():
	imlist=get_imlist('testpictures')
	greylevel_transform(imlist)


def get_imlist(path):
	#returns a list of filenames for all jpg in a directory
	return [os.path.join(path,f) for f in os.listdir(path) if f.endswith('.jpg')]

def convert_file_type(filelist):
	for infile in filelist:
		outfile=os.path.splitext(infile)[0]+".jpg"
		if infile != outfile:
			try:
				Image.open(infile).save(outfile)
			except IOError:
				print "cannot convert", infile

def greylevel_transform(filelist):
	
	for infile in filelist:
		im=array(Image.open(infile).convert('L'))
		im2=255-im
		im3=(100.0/255)*im+100
		im4=255.0*(im/255.0)**2
		print int(im.min()), int(im.max())
		pil_im=Image.fromarray(uint8(im))
		outfile=os.path.splitext(infile)[0]+"greyscale"+".jpg"
		pil_im.save(outfile)

	#pil_im=Image.open('raspberries.jpg').convert('L').save('raspberriesbw.jpg')

main()