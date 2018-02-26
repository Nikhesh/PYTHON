string=raw_input("Enter the string:")
num=input("Enter the number of copies (n): ")
s=""
string2=string[:2]
for ln in range(1,num+1):
    s=s+string2
print s 
