choice = 0
ip1 = [0,0,1,1]
ip2 = [0,1,0,1]
def checksum(arr):
    #X1, X2 = input("Enter the two inputs: ").split()
    W1, W2 = input("Enter the weights : ").split()
    
    W1 = int(W1)
    W2 = int(W2)

    t = int(input("Enter the threshold: "))
    flag = 0
    for i, j, k in zip(ip1, ip2, arr):
        current_sum = i*W1 + j*W2
        if current_sum>=t:
            current_sum = 1
        else:
            current_sum = 0

        if current_sum != k:
            print('Please Enter the values again.\n')
            checksum(arr)
    print('The model is training.\n')
        
        
def not_checksum():
    w = int(input("Enter the weight: "))
    t = int(input("Enter the threshold: "))
    if t < w or w > 0:
        print('Please enter the values again.\n')
        not_checksum()
    else:
        print('The model is training.\n')

OR = [0,1,1,1]
AND = [0,0,0,1]

while choice in (0,1,2,3):
    choice = int(input('1. AND Gate \n2. OR Gate \n3. NOT Gate\n'))
    if choice == 1:
        checksum(AND)
    elif choice == 2:
        checksum(OR)
    elif choice == 3:
        not_checksum()
    else:
        pass
