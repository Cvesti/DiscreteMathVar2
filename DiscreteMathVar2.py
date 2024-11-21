def generate_power_set(s):

    power_set = []
    n = len(s)
    for i in range(2**n):
        subset = []
        for j in range(n):
            if (i & (1 << j)):
                subset.append(s[j])
        power_set.append(subset)
    return power_set