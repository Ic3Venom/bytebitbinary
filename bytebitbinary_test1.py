from PIL import Image
def main():
    img = Image.new('RGB', (100,100), "black")
    pixels = img.load()
    
    #credit @https://en.wikibooks.org/wiki/Python_Imaging_Library/Editing_Pixels
    for x in xaxis:
        for y in yaxis:
            pixels[x,y] = (255, 255, 255)
            
    img.show()
    
    

if __name__ == '__main__':
    main()
    
    EXIT
