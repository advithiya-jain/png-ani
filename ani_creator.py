from PIL import Image
import argparse
import os
		
def ani_creator(direc, output_filename, out_dir):

	# get all the png files in the directory using pillow
	images = [Image.open(direc+"/"+x) for x in os.listdir(direc) if x.endswith(".png")]
	# sort the images by getting the file name and converting it to a string
	images.sort(key=lambda x: str(os.path.splitext(x.filename)[0]))

	# calculate the number of frames
	num_frames = len(images)

	# Debugging print
	for i in range(num_frames):
		print(images[i].filename)

def main():
	# parse the arguments
	parser = argparse.ArgumentParser()
	parser.add_argument("-d", "--directory", type=str)
	parser.add_argument("-od", "--outputdirectory", type=str)
	parser.add_argument("-o", "--output", type=str)
	args = parser.parse_args()

	

	# get the directory
	image_dir = args.directory or os.getcwd()  # default directory is the current directory
	# get the output file name and prepend 'z' to the --output.
	# This is done so that when files are sorted, the outfiles are always at the end of the sorted list
	output_filename = args.output or "zMousecape_ready_ani"  # default output file name is zMousecape_ready_ani.png
	# get the output directory
	out_dir = args.outputdirectory or image_dir  # default output directory is the image directory

	return 0
	


if __name__ == "__main__":
	main()
