par = str (input("partition?: "))
ser = str (input("service?: "))
reg = str (input("region?: "))
acc = int (input("account-id?: "))
res = int (input("resourse-id?: "))
arn = f'arn:{par}:{ser}:{reg}:{acc}:{res}'
print(arn)

