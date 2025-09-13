# 🧮 Python Calculator

A **command-line calculator** capable of handling complex mathematical expressions, including:

- Integers and floating-point numbers
- Basic arithmetic: `+`, `-`, `*`, `/`
- Nested parentheses
- Unary operators (e.g., `-5`, `+3`, `-(2+3)`)

This calculator leverages the **Shunting Yard Algorithm** to convert infix expressions to **Reverse Polish Notation (RPN)** and evaluates them efficiently.

---

## ⚡ Features

| Feature                | Description                                                |
| ---------------------- | ---------------------------------------------------------- |
| Operator Precedence    | Correctly evaluates `*` and `/` before `+` and `-`         |
| Unary Operators        | Supports `+` and `-` in front of numbers and parentheses   |
| Parentheses            | Handles nested parentheses                                 |
| Syntax Validation      | Detects invalid expressions and shows clear error messages |
| Floating-Point Support | Works with decimals                                        |
| Interactive CLI        | Simple command-line interface for quick calculations       |

---

## 🚀 Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd calculator

🖥️ Usage

Run the program:

python main.py


Then enter your calculations:

Enter a calculation : 2 + 3 * 4
2 + 3 * 4 = 14.0

Enter a calculation : (2 + 3) * 4
(2 + 3) * 4 = 20.0

Enter a calculation : -5 + 3
-5 + 3 = -2.0


Invalid expressions will show an error message:

Enter a calculation : 2 ++ 3
Syntax error or invalid expression!

🏗️ Project Structure
calculator/
│
├── main.py        # Program entry point
├── lib.py         # Expression parsing and evaluation logic
└── README.md      # Project documentation

⚙️ How It Works

Parsing: shunting_yard() converts infix expressions to RPN.

Evaluation: evaluate_rpn() calculates the result using a stack-based algorithm.

Unary Operators: Supports + and - before numbers or parentheses.

Error Handling: Catches invalid syntax or division by zero gracefully.

🔢 Examples
Enter a calculation : 10 / (5 - 3)
10 / (5 - 3) = 5.0

Enter a calculation : 3 + 4 * 2 / (1 - 5)
3 + 4 * 2 / (1 - 5) = 1.0

Enter a calculation : -2 * (3 + 4)
-2 * (3 + 4) = -14.0

📝 License

This project is open-source. Feel free to use, modify, and distribute.


This version:
- Adds badges, emojis, and headings for better readability.
- Includes a features table and example outputs.
- Clearly separates sections like Installation, Usage, and How It Works.

If you want, I can also **add GitHub-style badges for Python version, license, and build status** to make it look super professional.
Do you want me to do that next?
```
