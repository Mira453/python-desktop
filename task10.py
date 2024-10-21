def check_numbers(array):
    
    for el in array:
        if not isinstance(el, (int, float)):
            return False
    return True

def process(array):
    print("Початковий масив: ", array)
    
    if not check_numbers(array):
        print("Масив містить нечислові елементи.")
        return
    
    average = sum(array) / len(array)
    print("Середнє значення масиву: ", average)
    
    for i in range(len(array)):
        if array[i] > average:
            array[i] -= 18
            
    print("Масив після змін: ", array)
    
array = [5, 87, 5.67, 66, 8]

process(array)