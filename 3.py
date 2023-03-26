inputString = "thisisniceone"

count = 0

# Loop through the string
for i in inputString:
    count = count + 1
newString = inputString[0:2] + inputString[count - 2: count]

# Printing the new String
print("Input string = " + inputString)
print("New String = " + newString)
