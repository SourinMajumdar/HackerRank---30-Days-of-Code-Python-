if __name__ == '__main__':
    N = int(input())
    names = []

    for _ in range(N):
        firstName, emailID = input().split()
        if '@gmail' in emailID:
            names.append(firstName) 

names.sort()
print(*names, sep='\n')
