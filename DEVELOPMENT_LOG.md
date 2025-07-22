# Femcode Development Log

This log details the features implemented and significant changes made to the Femcode programming language.

## Project Context and Structure

This project, `femboy-coding-language`, is located at the root directory `/home/k1tty/dev/gemini-cli/femboy-coding-language`.

-   `femboy-terminoligy.txt`: A text file containing the custom keywords and their meanings used in Femcode.
-   `femcode/`: This is the main project directory for the Femcode interpreter.
    -   `femcode/femterpreter`: A shell script located in the `femcode/` directory that acts as a wrapper to run compiled Femcode programs. It executes the compiled Linux executable (`femcode/dist/femcode_linux`).
    -   `femcode/src/`: Contains the core source code for the Femcode interpreter.
        -   `femcode/src/lexer.py`: Responsible for lexical analysis, breaking down the source code into tokens.
        -   `femcode/src/parser.py`: Responsible for syntactic analysis, building an Abstract Syntax Tree (AST) from the tokens.
        -   `femcode/src/interpreter.py`: Responsible for semantic analysis and execution of the AST.
        -   `femcode/src/main.py`: The entry point for the interpreter, handling file input and orchestrating the lexing, parsing, and interpretation process.
    -   `femcode/docs/`: Contains documentation for the Femcode language.
        -   `femcode/docs/README.md`: Comprehensive documentation of the Femcode language, including syntax, features, and usage instructions.
    -   `femcode/examples/`: Contains example Femcode programs demonstrating various language features.
    -   `femcode/build/`: Directory created by PyInstaller during the build process, containing intermediate build files.
    -   `femcode/dist/`: Directory created by PyInstaller, containing the compiled standalone executables.
        -   `femcode/dist/femcode_linux`: The compiled Linux executable of the Femcode interpreter.
    -   `femcode/venv/`: A Python virtual environment used for managing project dependencies (e.g., PyInstaller).

## Implemented Features & Changes

### 1. Core Language Setup
- **Description:** Established the foundational lexical analysis, parsing, and interpretation framework for Femcode.
- **Files Modified:**
    - `femcode/src/lexer.py`
    - `femcode/src/parser.py`
    - `femcode/src/interpreter.py`

### 2. Dictionaries and Property Access
- **Description:** Added support for creating dictionary (object) data structures and accessing their properties using dot notation.
- **Keywords/Syntax:** `{}` (dictionary literal), `.` (property access)
- **Files Modified:**
    - `femcode/src/lexer.py`
    - `femcode/src/parser.py`
    - `femcode/src/interpreter.py`
    - `femcode/examples/dictionaries.fem`

### 3. Input/Output (`ask` built-in function)
- **Description:** Introduced a built-in function `ask` to prompt the user for input, enhancing interactivity.
- **Keywords/Syntax:** `ask(prompt_string)`
- **Files Modified:**
    - `femcode/src/interpreter.py`
    - `femcode/examples/io.fem`

### 4. Built-in Functions (`len`, `type`)
- **Description:** Added utility built-in functions `len` for getting the length of strings/lists and `type` for determining the type of a value.
- **Keywords/Syntax:** `len(value)`, `type(value)`
- **Files Modified:**
    - `femcode/src/interpreter.py`
    - `femcode/examples/built_ins.fem`

### 5. `femterpreter` Wrapper Script
- **Description:** Created a standalone executable wrapper script to run Femcode programs directly from the command line, simplifying execution and removing the need to specify `python3 main.py`.
- **Files Modified:**
    - `femcode/femterpreter` (new file)
    - `femcode/src/main.py`

### 6. Enhanced Data Types
#### Floating-Point Numbers
- **Description:** Extended numerical support to include decimal values, allowing for more precise calculations.
- **Files Modified:**
    - `femcode/src/lexer.py`
    - `femcode/src/parser.py`

#### Null/None Type
- **Description:** Introduced a specific keyword to represent the absence of a value.
- **Keywords/Syntax:** `Ghosted`
- **Files Modified:**
    - `femcode/src/lexer.py`
    - `femcode/src/parser.py`

### 7. Advanced Control Flow
#### `for` Loops
- **Description:** Implemented iteration over sequences (lists and strings), enabling more flexible looping constructs.
- **Keywords/Syntax:** `Tomgirl` (for loop keyword)
- **Files Modified:**
    - `femcode/src/lexer.py`
    - `femcode/src/parser.py`
    - `femcode/src/interpreter.py`
    - `femcode/examples/loops_advanced.fem`

#### `break` and `continue` Statements
- **Description:** Added statements to provide more granular control over loop execution, allowing early exit or skipping iterations.
- **Keywords/Syntax:** `Break`, `Continue`
- **Files Modified:**
    - `femcode/src/lexer.py`
    - `femcode/src/parser.py`
    - `femcode/src/interpreter.py`
    - `femcode/examples/loops_advanced.fem`

### 8. Error Handling (`try-except`)
- **Description:** Implemented basic error handling mechanisms to gracefully manage runtime errors and prevent program crashes.
- **Keywords/Syntax:** `Twink` (try block), `Bimboy` (except block)
- **Files Modified:**
    - `femcode/src/lexer.py`
    - `femcode/src/parser.py`
    - `femcode/src/interpreter.py`
    - `femcode/examples/error_handling.fem`

### 9. Syntactic Sugar
#### Compound Assignment Operators
- **Description:** Added shorthand operators for common arithmetic assignments, improving code conciseness.
- **Keywords/Syntax:** `+=`, `-=`, `*=`, `/=`
- **Files Modified:**
    - `femcode/src/lexer.py`
    - `femcode/src/parser.py`
    - `femcode/src/interpreter.py`
    - `femcode/examples/syntactic_sugar.fem`

#### Increment/Decrement Operators
- **Description:** Introduced operators for easily increasing or decreasing numerical variables by one.
- **Keywords/Syntax:** `++`, `--`
- **Files Modified:**
    - `femcode/src/lexer.py`
    - `femcode/src/parser.py`
    - `femcode/src/interpreter.py`
    - `femcode/examples/syntactic_sugar.fem`

### 10. Documentation Updates
- **Description:** Continuously updated the `README.md` documentation to accurately reflect all new features, syntax, and usage instructions, including the `femterpreter` script.
- **Files Modified:**
    - `femcode/docs/README.md`