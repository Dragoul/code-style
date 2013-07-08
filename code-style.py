

import re

"""
tokens = ["NUMBER", "[0-9]*",
          "IDENTIFIER", "[a-zA-Z][a-zA-Z0-9]*"]
"""

if (__name__ == "__main__"):
    
    """
    source = open("color.cpp","r")

    context = source.read()

    print(context)
    
    source.close()
    """

    import ply.lex as lex
    lexer = lex.lex()

    # Run a preprocessor
    import sys
    f = open(sys.argv[1])
    input = f.read()

    p = Preprocessor(lexer)
    p.parse(input,sys.argv[1])
    while True:
        tok = p.token()
        if not tok: break
        print(p.source, tok)
