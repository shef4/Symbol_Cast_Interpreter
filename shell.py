import symbolkast

while True:
	text = input('symbolkast > ')
	if text.strip() == "": continue
	result, error = symbolkast.run('<stdin>', text)

	if error:
		print(error.as_string())
	elif result:
		if len(result.elements) == 1:
			print(repr(result.elements[0]))
		else:
			print(repr(result))
    
    # for loop
    #VAR r = 1
    #LOOP i = 1 TO 6 THEN VAR r =r*i
    
    
    #while loop
    #VAR i = 0 
    #LOOP i < 10 THEN VAR i = i + 1
    
    #- FOR LOOP
    ##LOOP i = 6 TO 1 THEN VAR i = i + 1
    
    #FUN add (a,b) -> a+b
    
    #RUN("example.sk")