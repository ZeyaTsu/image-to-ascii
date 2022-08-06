from PIL import Image


def main(): 
    ascii_char = ' .:-=+*#%@'  # du plus foncé au plus clair

    getname = True
    while getname:
        name = str(input("Image name: "))
        size_x = int(input("Size.x: "))
        size_y = int(input("Size.y: "))
        getname = False


    ext = '.jpg'
    imgname = name + ext
    print("Render for", imgname)

    with Image.open(f"{imgname}") as image:
        image = image.resize((size_x, size_y))

        for y in range(image.height):
            line = ""
            for x in range(image.width):
                rgb = image.getpixel((x, y))
                grey = sum(rgb) // len(rgb)
                index = grey * 9 // 255
                line += ascii_char[index] + " "
            print(line)


    s = True
    while s:
        a = str(input("r - restart | q - quit"))
        if a == 'r':
            main()
            break
        elif a == 'q':
            break

main()

