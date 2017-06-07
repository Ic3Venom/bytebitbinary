def main():
    range = raw_input('Length and width of image: ')
    size = range.split(',')
    img = Image.new('RGB', (size[0], size[1]), "black")
    
    #credit @https://en.wikibooks.org/wiki/Python_Imaging_Library/Editing_Pixels
    for i in range(int(size[0])):
        for j in range(int(size[0])):
            pixels[i,j] = (i, j, 100)
            
    img.show()
    
    

if __name__ == '__main__':
    main()
    
    exit
