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
- **Description:** Established the foundational lexical analysis, parsing, and interpretation framework for Femcode. This involved defining basic token types, parsing simple expressions and statements, and setting up a rudimentary execution environment.
- **Technical Details:**
    - **`lexer.py`:** Initial implementation of `Token` class and `Lexer` with `get_next_token` for basic token recognition (integers, strings, basic operators, keywords).
    - **`parser.py`:** Defined core AST nodes (`Number`, `String`, `BinOp`, `Print`, `Assign`, `Variable`, `Block`, `IfStatement`, `WhileStatement`, `FunctionDefinition`, `FunctionCall`, `ReturnStatement`). Implemented recursive descent parsing methods (`expression`, `term`, `factor`, `parse_statement`, etc.).
    - **`interpreter.py`:** Implemented `Interpreter` class with `visit_*` methods for each AST node, defining their runtime behavior. Introduced `scope_stack` for variable management and `ReturnValue` exception for function returns.
- **Files Modified:**
    - `femcode/src/lexer.py`
    - `femcode/src/parser.py`
    - `femcode/src/interpreter.py`

### 2. Dictionaries and Property Access
- **Description:** Added support for creating dictionary (object) data structures and accessing their properties using dot notation. This allows for more complex data representation.
- **Keywords/Syntax:** `{}` (dictionary literal), `.` (property access)
- **Technical Details:**
    - **`lexer.py`:** Added token patterns for `LBRACE` (`{`), `RBRACE` (`}`), `COLON` (`:`), and `DOT` (`.`).
    - **`parser.py`:**
        -   New AST nodes: `Dictionary` (to represent dictionary literals) and `PropertyAccess` (to represent accessing a property of an object).
        -   `parse_dictionary_literal()` method: Parses key-value pairs within `{}`. It consumes `LBRACE`, then iteratively parses `expression` (for key), `COLON`, `expression` (for value), and `COMMA` until `RBRACE` is encountered.
        -   `factor()` method: Modified to recognize `LBRACE` for dictionary literals and `DOT` for property access. It now correctly dispatches to `parse_dictionary_literal()` and `parse_property_access()`. 
        -   `parse_property_access(target_node)` method: Consumes `DOT`, then an `ID` token for the property name, creating a `PropertyAccess` AST node.
    - **`interpreter.py`:**
        -   `visit_Dictionary(node)`: Evaluates key and value expressions for each pair and constructs a Python dictionary.
        -   `visit_PropertyAccess(node)`: Evaluates the `target` node (expected to be a dictionary) and retrieves the property using `target.get(property_name)`. Includes type checking to ensure the target is a dictionary.
- **Files Modified:**
    - `femcode/src/lexer.py`
    - `femcode/src/parser.py`
    - `femcode/src/interpreter.py`
    - `femcode/examples/dictionaries.fem`

### 3. Input/Output (`ask` built-in function)
- **Description:** Introduced a built-in function `ask` to prompt the user for input, enhancing interactivity. This allows Femcode programs to receive data from the user.
- **Keywords/Syntax:** `ask(prompt_string)`
- **Technical Details:**
    - **`interpreter.py`:**
        -   Added `_ask_builtin(prompt)` method: This method directly uses Python's `input()` function to get user input.
        -   Modified `Interpreter.__init__`: Registered `_ask_builtin` as a callable function under the name "ask" in the `self.functions` dictionary.
        -   Modified `visit_FunctionCall(node)`: Added logic to check if `func_info` is a callable (i.e., a built-in function). If so, it calls the function directly with evaluated arguments. Otherwise, it proceeds with the logic for user-defined functions.
- **Files Modified:**
    - `femcode/src/interpreter.py`
    - `femcode/examples/io.fem`

### 4. Built-in Functions (`len`, `type`)
- **Description:** Added utility built-in functions `len` for getting the length of strings/lists and `type` for determining the type of a value. These functions provide basic introspection and data manipulation capabilities.
- **Keywords/Syntax:** `len(value)`, `type(value)`
- **Technical Details:**
    - **`interpreter.py`:**
        -   Added `_len_builtin(obj)` method: Uses Python's built-in `len()` function. Marked as `@staticmethod`.
        -   Added `_type_builtin(obj)` method: Uses Python's `type(obj).__name__` to get the type string. Marked as `@staticmethod`.
        -   Modified `Interpreter.__init__`: Registered `_len_builtin` and `_type_builtin` in the `self.functions` dictionary.
- **Files Modified:**
    - `femcode/src/interpreter.py`
    - `femcode/examples/built_ins.fem`

### 5. `femterpreter` Wrapper Script
- **Description:** Created a standalone executable wrapper script to run Femcode programs directly from the command line, simplifying execution and removing the need to specify `python3 main.py`. This greatly improves the user experience.
- **Technical Details:**
    - **`femcode/femterpreter` (new file):** A bash script that calls the compiled Python executable (`femcode/dist/femcode_linux`) with the provided arguments. It handles path resolution to ensure the executable is found.
    - **`femcode/src/main.py`:** Modified to accept the Femcode file path as a command-line argument using `sys.argv`. Includes basic error handling for missing files.
    - **Build Process:** Instructions were provided for creating a virtual environment, installing `pyinstaller`, and compiling the Linux executable (`femcode/dist/femcode_linux`).
- **Files Modified:**
    - `femcode/femterpreter` (new file)
    - `femcode/src/main.py`

### 6. Enhanced Data Types
#### Floating-Point Numbers
- **Description:** Extended numerical support to include decimal values, allowing for more precise calculations.
- **Technical Details:**
    - **`lexer.py`:** Modified the `isdigit()` block to check for a decimal point (`.`) and subsequent digits, tokenizing them as `FLOAT`. The `token_patterns` list was updated to include `FLOAT` regex.
    - **`parser.py`:** The `factor()` method was updated to recognize `FLOAT` tokens and create `Number` AST nodes (reusing the existing `Number` AST node, as the interpreter can handle both `int` and `float` Python types).
- **Files Modified:**
    - `femcode/src/lexer.py`
    - `femcode/src/parser.py`

#### Null/None Type
- **Description:** Introduced a specific keyword (`Ghosted`) to represent the absence of a value, similar to `null` or `None` in other languages.
- **Keywords/Syntax:** `Ghosted`
- **Technical Details:**
    - **`lexer.py`:** Added a regex pattern to recognize the `Ghosted` keyword and tokenize it as `NULL`. This pattern was added to the `token_patterns` list.
    - **`parser.py`:**
        -   New AST node: `Null` (a simple placeholder AST node).
        -   `factor()` method: Modified to recognize `NULL` tokens and create `Null` AST nodes.
    - **`interpreter.py`:**
        -   `visit_Null(node)`: Returns Python's `None` when a `Null` AST node is visited.
- **Files Modified:**
    - `femcode/src/lexer.py`
    - `femcode/src/parser.py`

### 7. Advanced Control Flow
#### `for` Loops
- **Description:** Implemented iteration over sequences (lists and strings), enabling more flexible looping constructs.
- **Keywords/Syntax:** `Tomgirl` (for loop keyword)
- **Technical Details:**
    - **`lexer.py`:** Added a regex pattern to recognize `Tomgirl` and tokenize it as `FOR`. This pattern was added to the `token_patterns` list.
    - **`parser.py`:**
        -   New AST node: `ForStatement` (stores the loop variable name, the iterable expression, and the loop body).
        -   `parse_statement()`: Modified to recognize `FOR` and dispatch to `parse_for_statement()`. 
        -   `parse_for_statement()`: Parses the loop variable (ID), the `ASSIGN` token (acting as 'in' for now, a more specific 'IN' token could be introduced later), the iterable expression, and the loop body (block).
    - **`interpreter.py`:**
        -   `visit_ForStatement(node)`: Evaluates the `iterable`. It then iterates through each item, creates a new scope for each iteration, assigns the item to the loop variable in that scope, and then visits the loop body. Includes type checking to ensure the iterable is a list or string.
- **Files Modified:**
    - `femcode/src/lexer.py`
    - `femcode/src/parser.py`
    - `femcode/src/interpreter.py`
    - `femcode/examples/loops_advanced.fem`

#### `break` and `continue` Statements
- **Description:** Added statements to provide more granular control over loop execution, allowing early exit (`Break`) or skipping to the next iteration (`Continue`).
- **Keywords/Syntax:** `Break`, `Continue`
- **Technical Details:**
    - **`lexer.py`:** Added regex patterns to recognize `Break` and `Continue` keywords, tokenizing them as `BREAK` and `CONTINUE` respectively. These patterns were added to the `token_patterns` list.
    - **`parser.py`:**
        -   New AST nodes: `BreakStatement` and `ContinueStatement` (simple marker nodes).
        -   `parse_statement()`: Modified to recognize `BREAK` and `CONTINUE` tokens and create the corresponding AST nodes.
    - **`interpreter.py`:**
        -   New exception classes: `BreakLoop(Exception)` and `ContinueLoop(Exception)`. These are custom exceptions raised by `visit_BreakStatement` and `visit_ContinueStatement` respectively.
        -   `visit_BreakStatement(node)`: Raises `BreakLoop`.
        -   `visit_ContinueStatement(node)`: Raises `ContinueLoop`.
        -   `visit_WhileStatement(node)` and `visit_ForStatement(node)`: Wrapped their loop body execution in `try-except` blocks to catch `BreakLoop` and `ContinueLoop` exceptions, implementing the desired loop control flow. The `scope_stack` is properly managed (popped) when a `break` or `continue` occurs.
- **Files Modified:**
    - `femcode/src/lexer.py`
    - `femcode/src/parser.py`
    - `femcode/src/interpreter.py`
    - `femcode/examples/loops_advanced.fem`

### 8. Error Handling (`try-except`)
- **Description:** Implemented basic error handling mechanisms to gracefully manage runtime errors and prevent program crashes. This allows Femcode programs to define blocks of code that can "catch" and respond to errors.
- **Keywords/Syntax:** `Twink` (try block), `Bimboy` (except block)
- **Technical Details:**
    - **`lexer.py`:** Added regex patterns to recognize `Twink` and `Bimboy` keywords, tokenizing them as `TRY` and `EXCEPT` respectively. These patterns were added to the `token_patterns` list.
    - **`parser.py`:**
        -   New AST node: `TryExceptStatement` (stores the `try_block` and `except_block`).
        -   `parse_statement()`: Modified to recognize `TRY` and dispatch to `parse_try_except_statement()`. 
        -   `parse_try_except_statement()`: Parses the `TRY` keyword, `FEMBOYCORE`, the `try_block` (a `Block` of statements), `PERIODT`, then `EXCEPT`, `FEMBOYCORE`, the `except_block` (another `Block` of statements), and `PERIODT`. It ensures proper block termination.
    - **`interpreter.py`:**
        -   `visit_TryExceptStatement(node)`: Wraps the execution of `node.try_block` in a Python `try-except Exception` block. If any Python `Exception` occurs during the execution of the `try_block`, it catches the exception and then executes `node.except_block`. This provides a basic catch-all error handling mechanism.
- **Files Modified:**
    - `femcode/src/lexer.py`
    - `femcode/src/parser.py`
    - `femcode/src/interpreter.py`
    - `femcode/examples/error_handling.fem`

### 9. Syntactic Sugar
#### Compound Assignment Operators
- **Description:** Added shorthand operators for common arithmetic assignments, improving code conciseness and readability.
- **Keywords/Syntax:** `+=`, `-=`, `*=`, `/=`
- **Technical Details:**
    - **`lexer.py`:** Added token patterns for `PLUS_ASSIGN`, `MINUS_ASSIGN`, `MUL_ASSIGN`, and `DIV_ASSIGN`. These are matched as two-character operators and placed before single-character operators in `token_patterns` to ensure correct precedence.
    - **`parser.py`:**
        -   `parse_assignment_statement()`: Modified to check for these new compound assignment token types (`PLUS_ASSIGN`, `MINUS_ASSIGN`, etc.). If a compound assignment is found, it transforms it into a standard `Assign` AST node where the right-hand side is a `BinOp` representing the equivalent arithmetic operation (e.g., `count += 3` is parsed as `count = count + 3`). This simplifies interpreter logic.
    - **`interpreter.py`:** The `visit_Assign` method implicitly handles the compound assignments because the parser transforms them into standard `Assign` and `BinOp` nodes, requiring no special handling in the interpreter itself.
- **Files Modified:**
    - `femcode/src/lexer.py`
    - `femcode/src/parser.py`
    - `femcode/src/interpreter.py`
    - `femcode/examples/syntactic_sugar.fem`

#### Increment/Decrement Operators
- **Description:** Introduced operators for easily increasing or decreasing numerical variables by one, providing a more concise syntax for common operations.
- **Keywords/Syntax:** `++`, `--`
- **Technical Details:**
    - **`lexer.py`:** Added token patterns for `INCREMENT` (`++`) and `DECREMENT` (`--`). These are matched as two-character operators and placed before single-character operators in `token_patterns` to ensure correct precedence.
    - **`parser.py`:**
        -   New AST nodes: `Increment` and `Decrement` (each storing the `Variable` node to be modified).
        -   `factor()` method: Modified to recognize `INCREMENT` and `DECREMENT` tokens immediately following an `ID` (variable name). It creates the corresponding `Increment` or `Decrement` AST node.
        -   `parse_statement()`: Modified to handle `Increment` and `Decrement` AST nodes as standalone statements.
    - **`interpreter.py`:**
        -   `visit_Increment(node)`: Retrieves the current value of the variable (from `node.var_name`), increments it by 1, and updates the variable in the current scope. Includes type checking to ensure the variable is numeric.
        -   `visit_Decrement(node)`: Retrieves the current value of the variable, decrements it by 1, and updates the variable in the current scope. Includes type checking for numeric values.
- **Files Modified:**
    - `femcode/src/lexer.py`
    - `femcode/src/parser.py`
    - `femcode/src/interpreter.py`
    - `femcode/examples/syntactic_sugar.fem`

### 10. Documentation Updates
- **Description:** Continuously updated the `README.md` documentation to accurately reflect all new features, syntax, and usage instructions, including the `femterpreter` script. This ensures that users have up-to-date information on how to use the language.
- **Files Modified:**
    - `femcode/docs/README.md`
