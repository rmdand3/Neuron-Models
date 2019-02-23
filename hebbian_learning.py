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

#For all the 2 bit inputs with a single hebb neuron output.
def checkhebb_2bit(arr,flag):
    w1 = w2 = w3 = 0
    if flag == 0:
        temp1 = ip1
        temp2 = ip2
    else:
        temp1 = ANDNOT #This is special provision to simulate XOR.
        temp2 = ANDNOT[::-1]
    temp3 = ip3
    for i,j,k,l in zip(temp1, temp2, temp3, arr):
        w1+=i*l
        w2+=j*l
        w3+=k*l
        #weights = [w1,w2,w3]
        #print('The weights for implementation on Input 1, Input 2 and the Bias are : ', weights)
    
    weights = [w1,w2,w3]
    return weights

def checkhebb_1bit(arr):
    w1 = w2 = 0
    ip4 = ip2[:2]
    ip5 = ip3[:2]
    for i, j, k in zip(ip4, ip5, arr):
        w1+=i*k
        w2+=j*k
    weight = [w1, w2]
    return weight    


#This classifier function is used to differentiate between two characters in a 3x3 grid.
def checkhebb_char(arr): 
    weights = []
    for i, j in zip(T,C):
        w = 0
        w = w + i*TC[0]
        w = w + j*TC[1]
        weights.append(w)
    return weights
       
while choice in (0,1,2,3,4,5,6):
    print('-'*25)
    choice = int(input('1. AND Gate \n2. OR Gate \n3. NOT Gate\n4. ANDNOT Gate\n5. XOR Gate\n6. T & C comparion\n'))
    if choice == 1:
        weights = checkhebb_2bit(AND,0)
        print('The weights for implementation on Input 1, Input 2 and the Bias are : ', weights)
    elif choice == 2:
        weights = checkhebb_2bit(OR,0)
        print('The weights for implementation on Input 1, Input 2 and the Bias are : ', weights)
    elif choice == 3:
        checkhebb_1bit(NOT)
    elif choice == 4:
        weights = checkhebb_2bit(ANDNOT,0)
        print('The weights for implementation on Input 1, Input 2 and the Bias are : ', weights)
    elif choice == 5:
        wt1 = checkhebb_2bit(ANDNOT,0)
        weights = checkhebb_2bit(XOR,1)
        wt1 = wt1 + wt1[::-1] + weights
        print('The 9 weights in order are: ', wt1)
    elif choice == 6:
        weights = checkhebb_char(TC)
        print('The weight for T and C comparison are: ',weights)
    else:
        pass

