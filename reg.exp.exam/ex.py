~                                                                                                                                                    
m re import sub
 
def encode(text):
    '''
    Doctest:
        >>> encode('WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW')
        '12W1B12W3B24W1B14W'    
    '''
    return sub(r'(.)\1*', lambda m: str(len(m.group(0))) + m.group(1),
               text)
~                                                                                                                                                    
~                                                                                                                                                    
~                                                                                                                                                    
~                                                                                                                                                    
~                                                                                                                                                    
~                                                                                                                                                    
~                                                                                                                                                    
~                                                                                                                                                    
~                                                                                                                                                    
~                                                                                                                                                    
~                                                                                                                                                    
~                                                                                                                                                    
                                                                                                                                                    
~                                                                                                                                                    
~                                                                                                                                                    
~                                                                                                                                                    
~                                                                                                                                                    
~                                                                                                                                                    
~                                                                                                                                                    
~                                                                                                                                                    
~                                                                                                                                                    
~                                                                                                                                                    
~                                                                                                                                                    
~                                                                                                                                                    
~                                                                                                                                                    
~                                                                                                                                                    
~                                                                                                                                                    
~                                                                                                                                                    
~                                                                                                                                                    
~                                                                                                                                                    
                                                                                                                                   1,1           All
