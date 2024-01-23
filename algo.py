def combinations(string):
    combis = []
    for num in range(1, 2 ** len(string)):
        combiner = bin(num).replace('0b', '')
        while len(combiner) < len(string):
            combiner = '0' + combiner
        combi = ''
        for index, state in enumerate(combiner):
            if state == '1':
                combi += string[index]
        combis.append(combi)
    return combis
    
