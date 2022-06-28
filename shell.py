import symbol_cast
while True:
    text = input('symbol_cast > ')
    result, error = symbol_cast.run('<stdin>',text)

    if error: print(error.as_string())
    else: print(result)