""" Copyright 2015  Institution, sta256+mpskit at gmail.com
    
    This file is part of mpskit.

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as
    published by the Free Software Foundation, either version 3 of the
    License, or (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY.

    See LICENSE file for more details.
"""
from common import *
from madspack import read_madspack, write_madspack, save_madspack, load_madspack
from collections import namedtuple
from PIL import Image, ImageDraw
from PIL.ImagePalette import ImagePalette
from fab import read_fab
from pallete import read_pallete_col, read_pallete_rex

ext = 'png'




def save_header(name, h):
	oname = name + '.json'
	with open(oname, 'w') as f:
		json.dump(h.as_dict(), f, indent=2)	
	print(oname)



	
	

def attach_palette(img, pal):
	R,G,B = [],[],[]
	for c in pal:
		R.append(c[0])
		G.append(c[1])
		B.append(c[2])

	img.putpalette(
		ImagePalette(
			mode = 'RGB', 
			palette = R + G + B, 		
			size = len(pal) * 3,
		)
	)
	

def export_pallete(pal, name_ss):

	img = Image.new('P', (16,16), 0)

	attach_palette(img, pal)
	
	d = ImageDraw.ImageDraw(img)
	d.rectangle((0, 0, 16, 16), fill=0)
	for k in range(len(pal)):
		i = k % 16
		j = k // 16
		d.rectangle((i, j, i+1, j+1), fill=k)
		
	name_pal = '{}.pal.png'.format(name_ss)
	img.save(name_pal)
	print(name_pal)



	







def read_art(art_name):
	check_ext(art_name, '.ART')
			
	verbose = 0	
	
	parts = read_madspack(art_name)
	
	
	save_madspack(art_name, parts)
		
	# parts[0] -- dimensions + pallete
	# parts[1] -- image data
		
		
	# header	
	h = Header()
	h.width = read_uint16(parts[0])
	h.height = read_uint16(parts[0])
	
	save_header(art_name, h)
	
	# pallete
	pal = read_pallete_rex(parts[0])
	
	export_pallete(pal, art_name)
	
	
	
	# image -- read indexed image
	img = Image.new('P', (h.width, h.height))	
	attach_palette(img, pal)	
	pix = img.load()	 
	for j in range(h.height):
		for i in range(h.width):
			ind = read_uint8(parts[1])
			pix[i,j] = ind

	save_image(art_name, img)
	

def load_header(name):
	with open('{}.json'.format(name), 'r') as f:
		return Header.from_dict(json.load(f))
	

def write_art(art_name):
	check_ext(art_name, '.ART')
			
	verbose = 0	
	
	# parts[0] -- dimensions + pallete
	# parts[1] -- image data
		
		
	# load header	
	h = load_header(art_name)
	
	
	
	# load image
	part1 = BytesIO()
			
	img = Image.open('{}.png'.format(art_name))		
	
	inds = [x for x in img.getdata()]
	assert len(inds) == h.width * h.height	
	write_raw(part1, len(inds), inds)

	img.close()
	
	parts = load_madspack(art_name)
	part1.seek(0)
	parts[1] = part1
	write_madspack(art_name, parts)
