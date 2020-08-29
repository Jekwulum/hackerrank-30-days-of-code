my_list_1 = list(range(2,6))
my_list_2 = list(range(6,21))

def weird_no(N):
    if N%2 == 0:
        if N in my_list_1:
            print("Not weird")
        elif N in my_list_2:
            print("Weird")
        elif N > 20:
            print("Not Weird")
    elif N%2 != 0:
        print("Weird")
            

if __name__ == '__main__':
    N = int(input())
    weird_no(N)
