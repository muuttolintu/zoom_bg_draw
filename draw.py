#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw, ImageFont

def bg_draw(password, filename='output.jpeg'):
	'''
	Draws a background image with argGUEST WiFi password for Zoom rooms.
	
	:param password: A text to be drawn.
	:param filename: Filename of the output image.
	'''
	template = 'template.jpeg'
	fontfile = 'calibrib.ttf'

	with Image.open(template) as img:
		draw = ImageDraw.Draw(img)
		font = ImageFont.truetype(fontfile, 64)
		# The size of the text string in pixels
		textsize = draw.textsize(password, font=font)
		# Calculating the text string starting point coordinates
		xy = (img.size[0] / 2 - textsize[0] / 2, 390)
		draw.text(xy, password, font=font)
		img.save(filename)

if __name__ == '__main__':
	import sys

	if len(sys.argv) == 1:
		password = input('Enter the password: ')
	else:
		password = sys.argv[1]

	print(f'\nRunning with password "{password}"...')
	bg_draw(password)
	print('Recorded to output.jpeg\n')
