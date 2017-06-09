from PIL import Image

def primes(maxRange):
    numRange= range(3, maxRange +1, 2) #currently has composites, they will be removed @end of program 
    primes = [2]
    
    while numRange: 
        repeat = 1
        guess = numRange[0] 
        primes.append(numRange[0]) 
        
        while repeat * guess <= maxRange: 
            
            if repeat * guess in numRange: 
                numRange.remove(repeat * guess) 
            
            repeat += 1 
            
    return primes

def main():
    size = raw_input("What length/width do you want your canvas to be?")
    img = Image.new('RGB', (size,size), (240, 240, 240))
    pixels = img.load()
    prime = primes(size*size)
    
    for x in range(size):    
        previous = x*size
        for y in range(size):
            if (x*size)+(y+1) in prime:
                pixels[y,x] = (118, 223, 109)
            
    img.show()
    

if __name__ == '__main__':
    main()
