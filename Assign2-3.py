#conversion of heights into centimetere

data= input("Enter heights of customers:")
heights = []
lst_in_cm = []

heights = data.split()
print("L1: ",heights)

for i in range(len (heights)):

 heights[i] = int(heights[i])

for j in range(len(heights)):

 s = heights[j] * 2.54

 lst_in_cm.append(s)

print("Heights are in cm:", lst_in_cm)
