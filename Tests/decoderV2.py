def decodeFromFile(path):
    # Renvoie un tableau de données statistiques à partir d'un chemin de fichier path
    # result[chars | ordering | lenght]
    file = open(path, encoding='latin_1')
    data = file.readlines()
    file.close()

    # Creation d'un array exploitable
    for i in range(len(data)):
        # Chaque data[i] est de la forme 'nombre occurences\n' à cette etape
        data[i] = data[i].replace('\n', '').split()
        if (i != 0):
            data[i][0] = chr(int(data[i][0]))
            data[i][1] = int(data[i][1])
        
    # Creation des familles de lettres
    result = {'lenght': int(data[0][0]), 'ordering': [], 'other': [0.0]}
    families = [['a', 'aâäà'], ['z', 'z'], ['e', 'eéèëê'], ['r', 'r'], ['t', 't'], ['y', 'yÿ'], ['u', 'uùûü'], ['i', 'iîï'], ['o', 'oôö'], ['p', 'p'],
                ['q', 'q'], ['s', 's'], ['d', 'd'], ['f', 'f'], ['g', 'g'], ['h', 'h'], ['j', 'j'], ['k', 'k'], ['l', 'l'], ['m', 'm'],
                ['w', 'w'], ['x', 'x'], ['c', 'cç'], ['v', 'v'], ['b', 'b'], ['n', 'nñ'],
                ['chif', '0123456789'], ['ponc', '"?.,;:!\'"']]
    for char in range(1, len(data)):
        inFamily = False
        for family in range(len(families)):
            if (families[family][1].find(data[char][0]) != -1):
                inFamily = True
                if (families[family][0] in result):
                    result[families[family][0]][0] = result[families[family][0]][0] + data[char][1]/result['lenght']
                    result[families[family][0]].append([data[char][0], data[char][1]/result['lenght']])
                else:
                    result['ordering'].append(families[family][0])
                    result[families[family][0]] = [data[char][1]/result['lenght'], [data[char][0], data[char][1]/result['lenght']]]
        if (not inFamily):
            result['other'][0] = result['other'][0] + data[char][1]/result['lenght']
            result['other'].append([data[char][0], data[char][1]/result['lenght']])
    result['ordering'].append('other')

    
    array = []
    for i in range(len(result['ordering'])):
        array.append([result[result['ordering'][i]][0], result['ordering'][i]])
    result['ordering'] = sorted(array, reverse=True)
    
    return result

data = decodeFromFile('result.txt')

print(data)
