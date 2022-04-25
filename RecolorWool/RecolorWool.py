# Wool recoloring program for Minecraft, poorly made by Hwoai :D
# Edit configs for other versions, this is for 1.8.9
from PIL import Image, ImageChops, ImageEnhance

wool_colors = {
    'black': '#181414',
    'blue': '#253193',
    'brown': '#56331c',
    'cyan': '#267191',
    'gray': '#414141',
    'green': '#364b18',
    'light_blue': '#6387d2',
    'lime': '#39ba2e',
    'magenta': '#be49c9',
    'orange': '#ea7e35',
    'pink': '#d98199',
    'purple': '#7e34bf',
    'red': '#9e2b27',
    'silver': '#a0a7a7',
    'white': '#e4e4e4',
    'yellow': '#c2b51c',
}

# Credit to https://gaming.stackexchange.com/questions/47212/what-are-the-color-values-for-dyed-wool for colors

wool_list = [
    'black',
    'blue',
    'brown',
    'cyan',
    'gray',
    'green',
    'light_blue',
    'lime',
    'magenta',
    'orange',
    'pink',
    'purple',
    'red',
    'silver',
    'white',
    'yellow'
]

brighten_image = 2.3
# Edit the config here ^

grayscale = input('\nConvert Block to grayscale first (Y/n): ')

for i in range(len(wool_list)):

    name = wool_list[i]
    color = wool_colors[name]

    wool = Image.open('wool.png')

    if grayscale.lower() != 'n':
        wool = wool.convert('LA')

    wool = wool.convert('RGBA')

    mask = Image.new('RGB', wool.size, color=color)
    mask = mask.convert('RGBA')

    brightness = ImageEnhance.Brightness(wool)
    wool = brightness.enhance(brighten_image)
    wool = ImageChops.multiply(wool, mask)
    wool.save('wool_colored_' + name + '.png', 'PNG')