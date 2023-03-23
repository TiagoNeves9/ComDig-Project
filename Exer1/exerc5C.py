import collections


def symb_freq(file):
    with open(file, 'r') as f:
        text = f.read()
        
    cnt = collections.Counter(text)
    symbol_frequencie, frequencie = cnt.most_common(1)[0]
    symb_less_freq, less_frequencie = cnt.most_common()[-1]
    
    print(f'Most frequent symbol is {symbol_frequencie}, {frequencie} times')
    print(f'Less frequent symbol is {symb_less_freq}, {less_frequencie} times')
    
    
    
z = {'aaaaaa bbbb cc t dd'}   
    
x = symb_freq('text.txt')
print(x)    