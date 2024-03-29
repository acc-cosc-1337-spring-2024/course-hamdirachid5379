def test_config():
    return True

def create_dictionary():
    prog_langs= {'C++:1979', 'Java:1992', 'Python:1996', 'C#:2001'}
    
    #value = prog_langs.values(["python"])
    print(prog_langs)
    print(prog_langs.get(['C++']))