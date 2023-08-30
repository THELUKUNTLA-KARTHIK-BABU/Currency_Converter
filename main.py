with open('main.txt') as f:
    lines=f.readlines()
# print(a)
currencyDict={}
for line in lines:
    parsed = line.split("\t")
    print(parsed)
    currencyDict[parsed[0]] =parsed[1]
print(currencyDict)
amount = int(input("enter the anoumt:\n"))
print("enter the name of the currency you want to convertthis amount to?:\n")
[print(item) for item in currencyDict.keys()]
currency = input("please enter one of the values:\n")
print(f"{amount}INR is equal to {amount*float(currencyDict[currency])}{currency}")
