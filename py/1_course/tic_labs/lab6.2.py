import matplotlib.pyplot as plt
import re
from math import log
alph = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
pattern = '([\W\d\s\])/([a-z])'  # Паттерн для функции "re.sub"
counter = 0

prob = []
inf_chr = []
ent_max = log(len(alph), 2)
ent_real = 0
r_abs = 0
r_rel = 0

with open('py/1_course/tic_labs/text.txt', encoding='utf8') as f:  # открываем текстовый файл
    text = f.readlines()
    s = ''.join(text).lower()
    s = re.sub(pattern, '', s)  # pattern = '([\W\d\s\])/([a-z])'
    
    for i in alph:
        
        #  Вероятности
        prob.append(s.count(i) / len(s))
        
        #  Собственная ин-ция
        inf_chr.append(log(prob[alph.index(i)], 2))
        
        #  Реальная энтропия
        ent_real -= prob[alph.index(i)] * inf_chr[alph.index(i)]
        
    #  Избыточность (абс и отн)
    r_abs = ent_max - ent_real
    r_rel = r_abs / ent_max * 100
    
print(f'Символ с наиб. собств. ин-цией - "{alph[inf_chr.index(max(inf_chr))]}"')
print(f'Символ с наим. собств. ин-цией - "{alph[inf_chr.index(min(inf_chr))]}"')
print(f'Максимальная энтропия - {ent_max}')
print(f'Реальная энтропия - {ent_real}')
print(f'Абсолютная избыточность - {r_abs}')
print(f'Относительная избыточность - {r_rel}')

plt.bar(alph, prob, label='Вероятности символов', color='red') #  Постоение графика вероятностей
plt.xlabel('Символ')
plt.ylabel('Вероятность')
plt.legend()
plt.grid()
plt.show()
