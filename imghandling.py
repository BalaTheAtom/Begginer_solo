def file():
    buffersize=50000
    infile=open('Picture_byt.jpg','rb')
    print(infile)
    outfile=open('copy.jpg','wb')
    buffer=infile.read(buffersize)
    while(len(buffer)):
        outfile.write(buffer)
        print('.',end='')
        buffer=infile.read(buffersize)
    print('Done')
file()