# Block recoloring program for Minecraft, poorly made by Hwoai :D
from PIL import Image, ImageChops
from tkinter import colorchooser

name = input('\nEnter block name: ')
choice1 = input('Convert Block to grayscale first (Y/n): ')
choice2 = input('Use custom color mask (y/N): ')

block = Image.open('block.png')

if not choice1.lower() == 'n':
    block = block.convert('LA')

block = block.convert('RGBA')

if choice2.lower() == 'y':
    try:
        mask = Image.open('mask.png')
        mask = mask.convert('RGBA')
    except FileNotFoundError:
        print('Mask not found.\n')
        exit(0)
else:
    color = colorchooser.askcolor(title ="Choose block mask color")[0]
    print('Blade color: ', color)

    mask = Image.new('RGB', block.size ,color=color)
    mask = mask.convert('RGBA')

block = ImageChops.multiply(block, mask)
block.save(name + '.png', 'PNG')

print()