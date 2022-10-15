def histogramm(string):
    sym_dict = dict()
    for sym in string:
        if sym in sym_dict:
            sym_dict[sym] += 1
        else:
            sym_dict[sym] = 1
    return sym_dict

text = input('Введите текст: ').lower()
hist = histogramm(text)
print('Оригинальный словарь частот:')

for i_sym in sorted(hist.keys()):
    print(i_sym, '-', hist[i_sym])

inv_list = []
print('\nИнвертированный словарь частот:')

for i_inv in set(sorted(hist.values())):
    for let in hist.keys():
        if hist[let] == i_inv:
            inv_list.extend(let)
    print(i_inv, ':', inv_list)
    inv_list = []