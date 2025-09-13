#//lib.py
from typing import Generic, TypeVar, Optional, TypedDict

T = TypeVar("T")
type Number = int | float

class Option(TypedDict, Generic[T]):
    value: Optional[T]

def is_ascii_digit(char: str) -> bool:
    return char in '0123456789'

def last(array: list[T]) -> Option[T]:
    if not array:
        return {"value": None}
    
    return {"value": array[-1]}

def entry() -> str:
    while True:
        s = input("\nEnter a calculation : ").replace(" ", "")
        if s:
            return s
        
        print("\nPlease enter a valid mathematical operation only !")

def get_operator_priority(op: str) -> int:
    match op:
        case '+' | '-':
            return 1
        case '*' | '/':
            return 2
        case _:
            return 0

def safe_pop(stack: list[T]):
    return stack.pop() if stack else None

def shunting_yard(token: str) -> Option[list[str]]:
    operators: list[str] = []
    output: list[str] = []

    numbers: str = ""
    expression = list(token)

    last_token_was_operator: bool = True
    index: int = 0

    for char in expression:
        match char:
            case '+' | '-' | '*' | '/':
                if last_token_was_operator and (char == '-' or char == '+'):
                    if index + 1 < len(expression) and expression[index + 1] == '(':
                        operators.append('u-' if char == '-' else 'u+')
                        last_token_was_operator = True
                        index += 1
                        continue
                    else:
                        numbers = char
                        last_token_was_operator = False
                        index += 1
                        continue

                if last_token_was_operator and (char == '*' or char == '/'):
                    if index > 0 and expression[index - 1] == ')':
                        pass
                    else:
                        return  { "value": None }
                
                if len(numbers) == 0 and len(output) == 0 and str(char) != '(':
                    return { "value": None }
                
                if len(numbers) != 0:
                    output.append(numbers)
                    numbers = ""
                
                if index > 0 and expression[index - 1] in '+*/':
                    if char == '-' and index + 1 < len(expression) and is_ascii_digit(expression[index + 1]):
                        numbers += char
                        last_token_was_operator = False
                        index += 1
                        continue

                    return { "value": None }
                
                if char == '/' and expression[index + 1] == '/':
                    return { "value": None }
                
                if char == '*' and expression[index + 1] == '*':
                    return { "value": None }
                
                while True:
                    top_op = last(operators)
                    match top_op['value']:
                        case None:
                            break
                        case _:
                            top_char = top_op['value']
                            top_priority = get_operator_priority(top_char)
                            cuurrent_priority = get_operator_priority(char)
                            if cuurrent_priority <= top_priority:
                                output.append(operators.pop())
                            else:
                                break
                
                operators.append(char)
                last_token_was_operator = True

            case '(':
                operators.append(char)
                last_token_was_operator = True
            
            case ')':
                if len(numbers) != 0:
                    output.append(numbers)
                    numbers = ""
                
                found_open_parenthesis = False
                op: Optional[str] = None
                while (op := safe_pop(operators)) is not None:
                    if op == '(':
                        found_open_parenthesis = True
                        break
                    output.append(op)

                if not found_open_parenthesis:
                    return { "value": None }
                
                if last(operators)['value'] in ('u-', 'u+'):
                    output.append(operators.pop())          
                
                last_token_was_operator = False

            case '.':
                if '.' in numbers:
                    return { "value": None }
                
                if len(numbers) == 0:
                    return { "value": None }
                
                if index + 1 >= len(expression) or not is_ascii_digit(expression[index + 1]):
                    return { 'value': None }
                
                numbers+='.'

            case _:
                if is_ascii_digit(char):
                    numbers += char
                    last_token_was_operator = False
                elif char == " ":
                    pass
                else:
                    return { "value": None }

        index+=1
    
    if len(numbers) != 0:
        output.append(numbers)
    
    op_2: Optional[str] = None
    while (op_2 := safe_pop(operators)) is not None:
        if op_2 == '(':
            return { "value": None }
        
        output.append(op_2)
    
    return { "value": output }


def evaluate_rpn(tokens: list[str]) -> Option[Number]:
    stack: list[Number] = []

    for token in tokens:
        match token:
            case "+":
                b = safe_pop(stack)
                a = safe_pop(stack)

                if a is not None and b is not None:
                    stack.append(a + b)
                else:
                    return { "value": None }
            
            case "-":
                b = safe_pop(stack)
                a = safe_pop(stack)

                if a is not None and b is not None:
                    stack.append(a - b)
                else:
                    return { "value": None }
            
            case "*":
                b = safe_pop(stack)
                a = safe_pop(stack)

                if a is not None and b is not None:
                    stack.append(a * b)
                else:
                    return { "value": None }
            
            case "/":
                b = safe_pop(stack)
                a = safe_pop(stack)

                if a is not None and b is not None:
                    if b == 0:
                        return { "value": None }
                    
                    stack.append(a / b)
                else:
                    return { "value": None }
                
            case "u-":
                a = safe_pop(stack)
                if a is not None:
                    stack.append(-a)
                else:
                    return {"value": None}
            
            case "u+":
                a = safe_pop(stack)
                if a is not None:
                    stack.append(+a)
                else:
                    return {"value": None}
            
            case _:
                try:
                    num: Number = float(token)
                except:
                    return { "value": None }
                stack.append(num)
    
    if len(stack) == 1:
        result = stack.pop()
        return { "value": result }
    else:
        return { "value": None }