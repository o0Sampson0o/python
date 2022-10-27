import pandas as pd

df = pd.DataFrame({})

var_list = []
exp_list = []
operator = ["+", "*", "(", ")", "^", "~", "->", "<>", "<-"]


def tokenize(exp):
    tokens = []
    temp = ""
    for i in range(len(exp)):
        temp += exp[i]
        if (temp in var_list or temp in operator):
            tokens.append(temp)
            temp = ""
    return tokens


def calc(tokens):
    left = -1
    right = -1

    i = 0
    while (True):
        if (i == len(tokens)):
            break
        if tokens[i] == '(':
            left = i
        elif tokens[i] == ')':
            right = i

        if left != -1 and right != -1:
            tokens = tokens[:left] + \
                [calc(tokens[left+1:right])]+tokens[right+1:]
            left = -1
            right = -1
            i = -1
        i += 1

    i = 0
    while (True):
        if (i == len(tokens)):
            break
        if tokens[i] == "~":
            tokens[i] = ('0' if tokens[i+1] == '1' else '1')
            del tokens[i+1]
        i += 1

    i = 0
    while (True):
        if len(tokens) == 1:
            return tokens[0]
        if tokens[i] in operator:
            if (tokens[i] == '*'):
                tokens[i] = str(int(tokens[0])*int(tokens[2]))
            elif (tokens[1] == '^'):
                tokens[i] = str(int(tokens[0]) ^ int(tokens[2]))
            elif (tokens[1] == '+'):
                tokens[i] = str(int(tokens[0]) | int(tokens[2]))
            elif (tokens[1] == '->'):
                tokens[i] = str((~int(tokens[0]) & 1) | int(tokens[2]))
            elif (tokens[1] == '<>'):
                tokens[i] = str(~(int(tokens[0]) ^ int(tokens[2])) & 1)
            del tokens[i-1]
            del tokens[i]
            i = -1
        i += 1


print("(-1 = next): ")

while (True):
    var = input("var: ")
    if (var == "-1"):
        break
    if (var in var_list or var in operator):
        continue
    df.insert(len(df.axes[1]), var, [], False)
    var_list.append(var)


while (True):
    exp = input("exp: ")
    if (exp == "-1"):
        break
    if (exp in exp_list):
        continue
    df.insert(len(df.axes[1]), exp, [], False)
    exp_list.append(exp)
    tokenize(exp)

for i in range(2**(len(var_list))):
    list = []
    for j in range(len(var_list)):
        list.append(1 if (i & (2**(len(var_list)-1-j))) else 0)
    for k in range(len(exp_list)):
        list.append("p")
    df.loc[i] = list

for j in range(len(df)):
    for i, s in enumerate(exp_list):
        tokens = tokenize(s)
        for (k, t) in enumerate(tokens):
            if (t in var_list):
                tokens[k] = str(df.loc[j].values[var_list.index(t)])
        df.loc[j, s] = calc(tokens)

print(df.to_string(index=False))
