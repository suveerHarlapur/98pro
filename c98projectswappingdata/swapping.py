def swapfiledata():
    filename=input('first file name (format :ex.txt)')
    filename2=input('second file name (format :ex.txt)')
    with open(filename,'r') as a:
        dataA=a.read()
    with open(filename2,'r') as a:
        dataB=a.read()
    with open(filename,'w') as a:
        a.write(dataB)
    with open(filename2,'w') as a:
        a.write(dataA)

swapfiledata()