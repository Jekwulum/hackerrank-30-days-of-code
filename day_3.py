N = int(input())
def weird_no(N):
    # if N%2 != 0:
    #     print("Weird")
    if N%2 == 0:
        if N in range(2, 6):
            print("Not weird")
        elif N in range(6, 21):
            print("Weird")
        elif N > 20:
            print("Not Weird")
    else:
        print("Weird")
            
weird_no(N)
# if __name__ == '__main__':
#     N = int(input())
