# Sword recoloring program for Minecraft, poorly made by Hwoai :D
from PIL import Image, ImageChops
from tkinter import colorchooser

name = input('\nEnter texture name: ')
choice1 = input('Convert blade to grayscale first (Y/n): ')
choice2 = input('Use custom color mask (y/N): ')
choice3 = input('Color handle (y/N): ')

if not choice3.lower() == 'n':
    choice4 = input('Convert handle to grayscale first (Y/n): ')

blade = Image.open('blade.png')
handle = Image.open('handle.png')

if not choice1.lower() == 'n':
    blade = blade.convert('LA')

if choice4.lower() != 'n':
    handle = handle.convert('LA')

blade = blade.convert('RGBA')
handle = handle.convert('RGBA')

if choice2.lower() == 'y':
    try:
        mask = Image.open('mask.png')
        mask = mask.convert('RGBA')
    except FileNotFoundError:
        print('Mask not found.\n')
        exit(0)
else:
    color = colorchooser.askcolor(title ="Choose blade mask color")[0]
    print('Blade color: ', color)

    mask = Image.new('RGB', blade.size ,color=color)
    mask = mask.convert('RGBA')

blade = ImageChops.multiply(blade, mask)

if choice4.lower() != 'n':
    handle_color = colorchooser.askcolor(title ="Choose handle mask color")[0]
    print('Handle color:', handle_color)

    handle_mask = Image.new('RGB', blade.size ,color=handle_color)
    handle_mask = handle_mask.convert('RGBA')

    handle = ImageChops.multiply(handle, handle_mask)

output = Image.new('RGBA', blade.size, (255,255,255,0))
output = output.convert('RGBA')
output.paste(handle, (0,0))
output.paste(blade, (0,0), blade)
output.save(name + '.png', 'PNG')

print()