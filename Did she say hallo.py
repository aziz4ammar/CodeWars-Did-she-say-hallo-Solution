def validate_hello(greetings):
    valid_greetings = ['hello', 'ciao', 'salut', 'hallo', 'hola', 'ahoj', 'czesc']
    
    greetings_lower = greetings.lower()
    
    for greeting in valid_greetings:
        if greeting in greetings_lower:
            return True
    
    return False