with open('1.txt','r',encoding='utf-8') as f:
    number_of_lines_1 = 0
    text_1 = []
    for line in f:
        number_of_lines_1 += 1
        text_1.append(line)
    text_1.insert(0,'1.txt\n')
    text_1.insert(1, number_of_lines_1)
    text_1.insert(2, '\n') 
total_1 = {number_of_lines_1: text_1}

with open('2.txt','r',encoding='utf-8') as f:
    number_of_lines_2 = 0
    text_2 = []
    for line in f:
        number_of_lines_2 += 1
        text_2.append(line)
    text_2.insert(0,'2.txt\n')
    text_2.insert(1, number_of_lines_2)
    text_2.insert(2, '\n')     
total_2 = {number_of_lines_2: text_2}

with open('3.txt','r',encoding='utf-8') as f:
    number_of_lines_3 = 0
    text_3 = []
    for line in f:
        number_of_lines_3 += 1
        text_3.append(line)
    text_3.insert(0,'2.txt\n')
    text_3.insert(1, number_of_lines_3)
    text_3.insert(2, '\n')     
total_3 = {number_of_lines_3: text_3}

total = {**total_1, **total_2, **total_3}

sorted_total = dict(sorted(total.items(), key=lambda x: x[0]))
#print(sorted_total)

with open('total.txt','at',encoding='utf-8') as f:
    for key, values in sorted_total.items():
        for line in values:
            str_ = str(line)
            f.write(str_)
        f.write('\n')    