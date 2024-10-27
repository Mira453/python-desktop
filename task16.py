first_string = "hello world "


try:
   first_string[0] = "J"  
except TypeError as e:
    print("Помилка:", e)
    
second_string = "how are you"

combined_string = first_string + second_string
print("Об'єднаний рядок:", combined_string)

multiplied_string = first_string * 10
print("Розмножений рядок:", multiplied_string)

inserted_string = "J" + first_string[1:]
print("Рядок із заміною першого символа:", inserted_string)


mid_index = len(first_string) // 2
modified_string = first_string[:mid_index] + "-" + first_string[mid_index:]
print("Рядок із вставкою символа в середину:", modified_string)

index_to_replace = 2
new_string = first_string[:index_to_replace] + "X" + first_string[index_to_replace + 1:]
print("Рядок із заміною одного символа:", new_string)