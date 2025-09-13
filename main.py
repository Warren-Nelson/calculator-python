#//main.py
import lib

while True:
    s = lib.entry()
    x = lib.shunting_yard(s)

    match x['value']:
        case None:
            print("Syntax error or invalid expression!")
        
        case _:
            result = lib.evaluate_rpn(x['value'])['value']
            if result is None:
                print("Expression evaluation error!")
            else:
                print(f"\n{s} = {result}")