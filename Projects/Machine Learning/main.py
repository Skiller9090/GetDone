import numpy as np

data = np.array([[0,1,0],[0,0,1],[1,0,0],[1,1,0]])
labels = np.array([[2,1,0,3]])
labels = labels.reshape(4,1)

weights = np.random.rand(3,1)
bias = np.random.rand(1)

lr = 0.05
def sigmoid(x):
    return (1/(1+np.exp(-x)))

def sigmoider(x):
    return sigmoid(x)*(1-sigmoid(x))


for epoch in range(100000):
    #x[0,1,2] *+ w[0,1,2] + bias 
    inputs = data
    allxallw = np.dot(inputs,weights)+bias
    #cost calc
    predictedOutcome = sigmoid(allxallw)
    
    error = predictedOutcome - labels
    
    dcost_dpred = error
    dpred_dz = sigmoider(predictedOutcome)
    
    zd = dcost_dpred * dpred_dz
    inputs = data.T
    weights -= lr * np.dot(inputs, zd)  

while True:
    a = int(input("Smoking: "))
    b = int(input("Obesity: "))
    c = int(input("Exercise: "))
    sp = np.array([a,b,c])
    result = sigmoid(np.dot(sp, weights) + bias)
    if int(round(result[0])) == 1:
        print("Is Diabetic")
    else:
        print("Is Not Diabetic")
    print("Is "+result)
