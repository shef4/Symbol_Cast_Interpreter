import symbol_cast
while True:
    text = input('symbol_cast > ')
    result, error = symbol_cast.run('<stdin>',text)

    if error: print(error.as_string())
    else: print(result)
    
    # for loop
    #VAR r = 1
    #LOOP i = 1 TO 6 THEN VAR r =r*i
    
    
    #while loop
    #VAR i = 0 
    #LOOP i < 10 THEN VAR i = i + 1
    
    #- FOR LOOP
    ##LOOP i = 6 TO 1 THEN VAR i = i + 1
    
    #FUN add (a,b) -> a+b