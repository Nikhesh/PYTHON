def main():
    a=input('number:')
    i=2
    flag=0
    while(i<a):
        if (a%i==0):
            flag=flag+1
        i=i+1
    if(flag==0):
        print "Prime"
    else:
        print "Not prime"        
if(__name__)==('__main__'):
    main()
        
