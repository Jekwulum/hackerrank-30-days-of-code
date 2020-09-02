T =int(input())

mylist=[]
for i in range(T):
    each_input=input()
    mylist.append(each_input)

def num(mylist):
 
    for i in mylist:
        string1=[]
        string2=[]
        string =list(i)
        
        for j in range(len(string)):
            if j % 2 == 0:
                string1.append(string[j])
            else:
                string2.append(string[j])
        print(''.join(string1),  ''.join(string2))
        
if __name__ == '__main__':   
    num(mylist)
