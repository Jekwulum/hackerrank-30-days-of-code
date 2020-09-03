# Enter your code here. Read input from STDIN. Print output to STDOUT
def phonebook(n):
    for i in list(range(n)):
        record = list(input().split())
        myrecord.append(record)
    records.update(myrecord)

def query():
    for i in list(range(n)):
        name = input()
        if name in records.keys():
            print("{0}={1}".format(name, records[name]))
        else:
            print("Not found")
        
if __name__ == '__main__':
    n = int(input().strip())
    records = {}
    myrecord = []
    phonebook(n)
    query()
