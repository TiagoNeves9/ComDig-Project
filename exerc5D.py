import collections
import math

def hist_maker(file):
    with open(file, 'rb') as f:
        data = f.read()
        
    hist = collections.Counter(data)
        
    file_size = len(data)
    
    entropy = 0
    
    for count in hist.values():
        p = count / file_size
        info = -math.log2(p)
        entropy += p *+ info 
        
    print("Histogram:")
    for byte, count in sorted(hist.items()):
                print(f"{byte:02x}: {count}")
    print(f"Informação Própria: {entropy:.2f} bits por simbolo")
    print(f"Entropia: {entropy * file_size:.2f} bits")
        
        
x = hist_maker('text.txt')
print(x)                   