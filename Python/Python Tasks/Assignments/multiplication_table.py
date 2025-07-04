print('    ', end="")

for rows in range(1, 10):

	print(f'{rows:3}', end=" ")

print("\n" + "-" * 40)


for rows in range(1, 10):
	
    print(f"{rows: 2} |",  end=" ")

    for columns in range(1, 10):

        print(f"{rows * columns:3}", end=" ")

    print()

