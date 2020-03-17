import sys
import os
from PIL import Image

path1 = sys.argv[1]
path2 = sys.argv[2]


if os.path.isdir(path1):
	if not os.path.isdir(path2):
		os.mkdir(path2)

	with os.scandir(path1) as entries:
		for entry in entries:
			if entry.name.endswith(".jpg"):
				im = Image.open(entry.path)
				string_list = entry.name.split(".")
				file_name = string_list[0]
				path_way = path2 +'/'+ file_name
				print(path_way)
				im.save(f'{path_way}.png', 'png')


else:
	print("Please check the Path-Name!")
	print(f'The Path-name {path1} is not correct:')