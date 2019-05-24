from PrepareTheData2 import GetTheInput_Single

df = GetTheInput_Single()
dataset = df.values

X = dataset[:, 0:6]
Y = dataset[:, 6]

print('input:')
print(X)
print('output:')
print(Y)