# test_calculator.py
import lib

tests = [
    # Nombres positifs simples
    ("5+3", 8),
    ("10-7", 3),
    ("2*3", 6),
    ("8/2", 4.0),

    # Nombres négatifs simples
    ("-5+3", -2),
    ("5+-3", 2),
    ("-5-3", -8),
    ("-5*-2", 10),
    ("-10/-2", 5.0),

    # Parenthèses
    ("(2+3)*4", 20),
    ("-(2+3)*4", -20),
    ("(-2+5)*3", 9),
    ("-(3+(-2))*2", -2),
    ("((-1+2)*(-3+4))/2", 0.5),

    # Virgules / floats
    ("3.5+2.5", 6.0),
    ("-3.5+2.5", -1.0),
    ("4.2*2", 8.4),
    ("-4.2*2", -8.4),
    ("3.5/-0.5", -7.0),
    ("0.1+0.2", 0.3),

    # Combinaisons
    ("-3+5*2", 7),
    ("(-3+5)*2", 4),
    ("-3+5*-2", -13),
    ("(-3+5)*-2", -4),
    ("-(-3+5)*-2", 4),
    ("-(-3+-5)*2", 16),

    # Chaines avec plusieurs opérateurs
    ("5+3-2", 6),
    ("5*2/2", 5.0),
    ("-5*2+10/2", -5.0),
    ("(-5+2)*(-3+4)", -3),

    # Cas d'erreur syntaxique
    ("5++2", None),
    ("--3", None),
    ("2**3", None),
    ("4//2", None),
    ("(3+2", None),
    ("3+2)", None),
    ("5..2+1", None),
    ("5+*2", None),
    ("5+/", None),
    ("*/2", None),
    ("", None),
    ("   ", None),

    # Division par zéro
    ("5/0", None),
    ("5/(3-3)", None),

    # Signes unaires devant parenthèses
    ("-(3+2)", -5),
    ("+(-3+2)", -1),
    ("-(-3+2)", 1),
    ("-(-(2+3)*2)", 10),

    # Parenthèses imbriquées
    ("((2+3)*(1+1))", 10),
    ("-(1+(2+3)*2)", -11),
    ("-(1+(2+3)*(2-1))", -6),
]

for expr, expected in tests:
    rpn = lib.shunting_yard(expr)
    result = None
    if rpn['value'] is not None:
        result = lib.evaluate_rpn(rpn['value'])['value']
    
    if result == expected:
        print(f"{expr} = {result}")
    else:
        print(f"{expr} -> expected {expected}, obtained {result}")
