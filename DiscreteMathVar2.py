def generate_power_set(s):

    """Генерация булеана (всех подмножеств) заданного множества."""

    power_set = []
    n = len(s)

    for i in range(2 ** n):
        subset = []
        for j in range(n):
            if (i & (1 << j)):
                subset.append(s[j])
        power_set.append(subset)

    return power_set

     
def is_natural(n):
    """Проверка на натуральное число."""
    return n.isdigit() and int(n) > 0

def is_integer(n):
    """Проверка на целое число."""
    return n.lstrip('-').isdigit()

def is_float(n):
    """Проверка на число с плавающей точкой."""
    try:
        float(n)
        return '.' in n or 'e' in n.lower()
    except ValueError:
        return False

def is_complex(n):
    """Проверка на комплексное число."""
    try:
        complex(n.replace('i', 'j'))
        return True
    except ValueError:
        return False

def is_fraction(n):
    """Проверка на дробь"""
    return '/' in n

def main():
    INPUT_PROMPT_NUM = "Введите количество элементов множества: "
    INPUT_PROMPT_ELEMENTS = "Введите элементы множества через запятую: "
    
    while True:
        num_elements = input(INPUT_PROMPT_NUM).strip()
        if num_elements.isdigit() and int(num_elements) > 0:
            num_elements = int(num_elements)
            break
        else:
            print("Пожалуйста, введите натуральное число.")

    input_set = input(INPUT_PROMPT_ELEMENTS).split(",")
    
    input_set = [item.strip() for item in input_set]

    input_set = [item for item in input_set if item]


    valid_set = []
    invalid_elements = []

    for item in input_set:
        if is_natural(item):
            valid_set.append(int(item)) 
        elif is_integer(item):
            valid_set.append(int(item))
            valid_set.append(float(item))
        elif is_complex(item):
            valid_set.append(complex(item.replace('i', 'j'))) 
        elif is_fraction(item):
            valid_set.append(item)  
        else:
            invalid_elements.append(item) 

    if invalid_elements:
        print("Вы ввели недопустимые элементы:", invalid_elements)

    power_set = generate_power_set(valid_set)
    print("Булеан заданного множества:", power_set)

if __name__ == "__main__":
    main()