import collections
import math
import matplotlib.pyplot as plt


def hist_maker(file):
    with open(file, 'r') as f:
        data = f.read()
    
    file_size = len(data)    
    plot = []    
    histogram = collections.Counter(data)
        
    for i in range(file_size):
       plot.append(data[i])    
        
    #histogram = collections.Counter(data)
        
    
    
    entropy = 0
    
    for key in histogram:
        count = histogram.__getitem__(key)
        p = count / file_size
        info = -math.log2(p)
        print(f"Informação Própria: {info} para simbolo {key}")
        entropy += p * info
         
    print(f"Entropia: {entropy}")    
     
     
        
    plt.title("Histogram")
    plt.hist(plot,bins=histogram.__sizeof__())
    plt.show()   

        
        
x = hist_maker('ListaPalavrasPT.txt')                 