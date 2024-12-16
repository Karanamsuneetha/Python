list_1 = [1, 1, 1]
list_2 = [1, 1, 1]
list_3 = [1, 1, 1]
final_list = [list_1, list_2, list_3]
print(f"{list_1}\n{list_2}\n{list_3}")
position = input("Enter the position (row-column): ")
row_number = int(position[0])
column_number = int(position[1])
final_list[row_number - 1][column_number - 1] = 'X'
print(f"{list_1}\n{list_2}\n{list_3}")






