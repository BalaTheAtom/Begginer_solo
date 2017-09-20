def file():
    buffersize=50000
    infile=open('Copy_file.txt','r')
    outfile=open('textfile.txt','a')
    buffer=infile.read(buffersize)
    while(len(buffer)):
        outfile.write(buffer)
        print('.',end='')
        buffer=infile.read(buffersize)
        print(buffersize)
    print('Done')
file()