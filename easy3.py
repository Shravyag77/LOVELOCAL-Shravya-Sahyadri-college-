def generate_pascals_triangle(num_rows):
    triangle = []

    for i in range(num_rows):
        row = [1] * (i + 1)
        if i > 1:
            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)

    return triangle

# Take input from the user for the number of rows
num_rows_str = input("Enter the number of rows for Pascal's triangle: ")

# Validate and convert the input to an integer
try:
    num_rows = int(num_rows_str)
except ValueError:
    print("Please enter a valid integer for the number of rows.")
    exit()

# Generate and print Pascal's triangle
result = generate_pascals_triangle(num_rows)
for row in result:
    print(row)
