#All the required ouptputs. The code can be extended to any form by input and output, Just by changing the arrays.
AND = [-1,-1,-1,1]
OR = [-1,1,1,1]
ANDNOT = [-1, -1, 1, -1]
NOT =[1,-1]
XOR = [-1, 1, 1, -1]
TC = [1, -1]

T = [1, 1, 1, -1, 1, -1, -1, 1, -1]
C = [1, 1, 1, 1, -1, -1, 1, 1, 1]
ip1 = [-1, -1, 1, 1 ]
ip2 = [-1, 1, -1, 1]
ip3 = [1, 1, 1, 1]
choice = 0

#Check any two bit input, single output logical combination. 
#Perceptron also accounts for a bias as the third input in this case which is tied to 1
def check_Percept_2bit(arr):
    alpha = int(input('Enter the required learning rate :'))
    #Learning rate is used to configure the speed at which the model trains 
    w1 = w2 = w3 = 0
    epoch_count = 0
    correct_count = 0
    while correct_count != 4:
        epoch_count += 1
        correct_count = 0
        #print("Epoch No: ",epoch_count)
        for i in range(1,5):
            #print('Case: ',i)
            y_in = ip1[i-1]*w1 + ip2[i-1]*w2 + ip3[i-1]*w3
            #print(y_in)
            if y_in!=0:
                y_in = y_in/abs(y_in)
            else:
                y_in = 0
            if(y_in != arr[i-1]):
                w1+=ip1[i-1]*arr[i-1]*alpha
                w2+=ip2[i-1]*arr[i-1]*alpha
                w3+=ip3[i-1]*arr[i-1]*alpha
                #print(w1,w2,w3)
                break
            else:
                correct_count += 1
            
        #weights = [w1,w2,w3]
        #print('The weights for implementation on Input 1, Input 2 and the Bias are : ', weights)
    
    weights = [w1,w2,w3]
    print('Calculated in :', epoch_count, 'epochs.')
    return weights

def check_Percept_1bit(arr):
    alpha = int(input('Enter the required learning rate :'))
    w1 = w2 = 0
    ip4 = ip2[:2]
    ip5 = ip3[:2]
    epoch_count = 0
    correct_count = 0
    while correct_count != 2:
        epoch_count += 1
        correct_count = 0
        #print(correct_count)
        #print("Epoch No: ",epoch_count)
        for i in range(1,3):
            #print('Case: ',i)
            y_in = ip4[i-1]*w1 + ip5[i-1]*w2 
            #print(y_in)
            if y_in!=0:
                y_in = y_in/abs(y_in)
            else:
                y_in = 0
            if(y_in != arr[i-1]):
                w1+=ip4[i-1]*arr[i-1]*alpha
                w2+=ip5[i-1]*arr[i-1]*alpha
                #print(w1,w2)
                break
            else:
                correct_count += 1
    weights = [w1,w2]
    print('The number of Epochs ',epoch_count)
    print('The weights for implementation on Input and bias on NOT gate are : ', weights)
    
def check_char(arr):
    weights = [0,0,0,0,0,0,0,0,0,0]
    alpha = int(input('Enter the required learning rate :'))
    y_in = 0
    choices = [T, C]
    epoch_count = 0
    correct_count = 0
    while correct_count != 2:
        epoch_count+=1
        correct_count = 0
        for i in range(2):
            for j, k in zip(choices[i], weights):
                y_in+=j*k
            if y_in!=0:
                y_in = y_in/abs(y_in)
            else:
                y_in = 0
            if y_in != TC[i]:
                for j, k in zip(choices[i], range(9)):
                    weights[k]+=j*alpha*TC[i]
                break
            else:
                correct_count+=1
    print('The number of Epochs ',epoch_count)
    return weights
       
while choice in (0,1,2,3,4,5):
    print('-'*75)
    choice = int(input('1. AND Gate \n2. OR Gate \n3. NOT Gate\n4. ANDNOT Gate\n5. T & C comparion\n'))
    if choice == 1:
        weights = check_Percept_2bit(AND)
        print('The weights for implementation on Input 1, Input 2 and the Bias are : ', weights)
    elif choice == 2:
        weights = check_Percept_2bit(OR)
        print('The weights for implementation on Input 1, Input 2 and the Bias are : ', weights)
    elif choice == 3:
        check_Percept_1bit(NOT)
    elif choice == 4:
        weights = check_Percept_2bit(ANDNOT)
        print('The weights for implementation on Input 1, Input 2 and the Bias are : ', weights)
    elif choice == 5:
        weights = check_char(TC)
        print('The weight for T and C comparison are: ',weights)
    else:
        pass
