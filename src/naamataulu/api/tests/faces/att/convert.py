import glob
from PIL import Image

faces = glob.glob('./**/*.pgm')

for face in faces:
	im = Image.open(face)
	rgb_im = im.convert('RGB')
	new_name = face.replace('pgm', 'jpg')
	rgb_im.save(new_name)
