# to print spaces in the head line row and the end="" prevent the #headline from going to the next line

print("    ", end="") 

#it loops from 1-9 of thr headline row

for rows in range(1, 10):


#this is used to create space between the line
    print(f"{rows:3}", end=" ")


#to print the dash after the first numbers
print("\n" + "-" * 40)





#this loop is to print the first row after the headline from 1-9
for rows in range(1, 10):

#to print the column line and put 2 spaces
    print(f"{rows: 2} |", end=" ")

#this is used to loop the first columns
    for columns in range(1, 10):

#this multiplies the rows by the columns and print it out with 3 spaces between them
        print(f"{rows * columns:3}", end=" ")
#this is used to take the cursor to the next line
    print()