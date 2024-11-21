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


def main():
    INPUT_PROMPT = "Введите элементы множества через запятую: "
    input_set = input(INPUT_PROMPT).split(",")
    input_set = [item.strip() for item in input_set] 
    power_set = generate_power_set(input_set)

    print("Булеан заданного множества:", power_set)


if __name__ == "__main__":
    main()