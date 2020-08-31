my_list_1 = list(range(1, 11))
my_list_2 = list(range(2,21))

def my_loop(n):
    while n in my_list_2:
        for i in my_list_1:
            print("{0} x {1} = {2}".format(n,i,n*i))
        break

if __name__ == '__main__':
    n = int(input())
    my_loop(n)
