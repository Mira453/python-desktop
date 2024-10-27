
for attempt in range(5):  
    user_input = input("Введіть число: ")  


    if not user_input.isdigit():
        print(f"Спроба {attempt + 1}: Це не число. Будь ласка, введіть число.")
        continue 


    user_number = int(user_input)


    if user_number == 5:
        print("Відмінний вибір! Ви ввели правильне число 5.")
        break 
    else:
        print(f"Спроба {attempt + 1}: Невірне число. Спробуйте ще раз.")


else:
    print("Ваші спроби закінчилися. Ви не ввели число 5.")
