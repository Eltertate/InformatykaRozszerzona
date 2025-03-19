print("\n\n\t\t\t\t\t\t\t\t\t\tZADANIE I\n")
#-------------------------------------------------
array = [[],[],[],[],[],[],[],[],[],[],[],[]]   # |
                                                # |
with open("slowa.txt", 'r') as file:            # |
    for line in file:                           # |
        line = line.strip()                     # |
        x = len(line)                           # |
        if 1 <= x <= 12:                        # |
            array[x - 1].append(line)           # |
                                                # |
for i in range(0,12):                           # |
    print("\n\n\tSłowa ", i+1 , " literowe:\n") # |
    print(array[i])                             # |
#--------------------------------------------------
print("\n\n\t\t\t\t\t\t\t\t\t\tZADANIE II\n")

