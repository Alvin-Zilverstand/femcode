# Femcode Language Documentation

Femcode is a femboy-themed programming language designed to be simple, expressive, and fun. It features a unique syntax inspired by femboy terminology, making coding an adorable experience.

## Table of Contents

1.  [Getting Started](#getting-started)
2.  [Basic Syntax](#basic-syntax)
3.  [Variables and Assignment](#variables-and-assignment)
4.  [Data Types](#data-types)
    *   [Numbers](#numbers)
    *   [Floating-Point Numbers](#floating-point-numbers)
    *   [Strings](#strings)
    *   [Booleans](#booleans)
    *   [Lists](#lists)
    *   [Dictionaries](#dictionaries)
    *   [Null Type](#null-type)
5.  [Operators](#operators)
    *   [Arithmetic Operators](#arithmetic-operators)
    *   [Comparison Operators](#comparison-operators)
    *   [Logical Operators](#logical-operators)
6.  [Control Flow](#control-flow)
    *   [Conditional Statements (If/Else)](#conditional-statements-ifelse)
    *   [Loops (While)](#loops-while)
    *   [For Loops](#for-loops)
    *   [Break and Continue](#break-and-continue)
7.  [Functions](#functions)
    *   [Defining Functions](#defining-functions)
    *   [Calling Functions](#calling-functions)
    *   [Return Values](#return-values)
    *   [Built-in Functions](#built-in-functions)
8.  [Comments](#comments)
9.  [Input/Output](#inputoutput)

## 1. Getting Started

To run Femcode programs, you can use the `femterpreter` wrapper script. This script simplifies running your `.fem` files without needing to navigate to the `src` directory or explicitly call `python3 main.py`.

### Running Femcode Programs

Once you have the `femterpreter` script, you can run your Femcode programs like this:

```bash
./femterpreter examples/your_program.fem
```

Or, if you add `femterpreter` to your system's PATH or create an alias (recommended for convenience):

```bash
femterpreter examples/your_program.fem
```

### Setting up `femterpreter` (Optional, but Recommended)

To use `femterpreter` from any directory, you can either add it to your system's PATH or create a shell alias.

**Option 1: Add to PATH**

1.  Open your shell's configuration file (e.g., `~/.bashrc`, `~/.zshrc`, or `~/.profile`).
2.  Add the following line, replacing `/path/to/femboy-coding-language` with the actual absolute path to your `femboy-coding-language` directory:

    ```bash
    export PATH="/path/to/femboy-coding-language/femcode:$PATH"
    ```

3.  Save the file and restart your terminal or run `source ~/.bashrc` (or your respective config file).

**Option 2: Create an Alias**

1.  Open your shell's configuration file (e.g., `~/.bashrc`, `~/.zshrc`, or `~/.profile`).
2.  Add the following line, replacing `/path/to/femboy-coding-language` with the actual absolute path to your `femboy-coding-language` directory:

    ```bash
    alias femterpreter="/path/to/femboy-coding-language/femcode/femterpreter"
    ```

3.  Save the file and restart your terminal or run `source ~/.bashrc` (or your respective config file).

## 2. Basic Syntax

### Running Femcode Programs

Once you have the `femterpreter` script, you can run your Femcode programs like this:

```bash
./femterpreter examples/your_program.fem
```

Or, if you add `femterpreter` to your system's PATH or create an alias (recommended for convenience):

```bash
femterpreter examples/your_program.fem
```

### Setting up `femterpreter` (Optional, but Recommended)

To use `femterpreter` from any directory, you can either add it to your system's PATH or create a shell alias.

**Option 1: Add to PATH**

1.  Open your shell's configuration file (e.g., `~/.bashrc`, `~/.zshrc`, or `~/.profile`).
2.  Add the following line, replacing `/path/to/femboy-coding-language` with the actual absolute path to your `femboy-coding-language` directory:

    ```bash
    export PATH="/path/to/femboy-coding-language/femcode:$PATH"
    ```

3.  Save the file and restart your terminal or run `source ~/.bashrc` (or your respective config file).

**Option 2: Create an Alias**

1.  Open your shell's configuration file (e.g., `~/.bashrc`, `~/.zshrc`, or `~/.profile`).
2.  Add the following line, replacing `/path/to/femboy-coding-language` with the actual absolute path to your `femboy-coding-language` directory:

    ```bash
    alias femterpreter="/path/to/femboy-coding-language/femcode/femterpreter"
    ```

3.  Save the file and restart your terminal or run `source ~/.bashrc` (or your respective config file).

## 2. Basic Syntax

## 2. Basic Syntax

Femcode uses keywords inspired by femboy terminology. Code blocks are defined using `Femboycore` to start a block and `Periodt` to end it.

## 3. Variables and Assignment

Variables are declared and assigned values using the `is` keyword.

```femcode
my_variable is 10
my_name is "Femboy"
```

## 4. Data Types

### Numbers

Femcode supports integer numbers.

```femcode
my_number is 123
```

### Floating-Point Numbers

Femcode supports floating-point numbers (decimals).

```femcode
my_float is 3.14
```

### Strings

Strings are sequences of characters enclosed in double quotes.

```femcode
my_string is "Hello, world!"
```

### Booleans

Femcode has two boolean values: `Kawaii` (True) and `Cringe` (False).

```femcode
is_cute is Kawaii
is_bad is Cringe
```

### Lists

Lists are ordered collections of items, enclosed in square brackets `[]` and separated by commas.

```femcode
my_list is [1, "apple", Kawaii]
```

Elements can be accessed using zero-based indexing:

```femcode
UwU Boy my_list[0] # Prints 1
```

### Dictionaries

Dictionaries are unordered collections of key-value pairs, enclosed in curly braces `{}`. Keys and values are separated by a colon `:`, and pairs are separated by commas.

```femcode
my_dict is {"name": "Femboy", "version": 1.0}
```

Values can be accessed using dot notation (property access):

```femcode
UwU Boy my_dict.name # Prints "Femboy"
```

### Null Type

Femcode introduces `Ghosted` to represent the absence of a value, similar to `null` or `None` in other languages.

```femcode
my_null_variable is Ghosted
UwU Boy my_null_variable # Prints Ghosted
```

## 5. Operators

### Arithmetic Operators

Femcode supports standard arithmetic operations:

*   `+` (addition)
*   `-` (subtraction)
*   `*` (multiplication)
*   `/` (division)

```femcode
result is 10 + 5 * 2
UwU Boy result # Prints 20
```

### Comparison Operators

Used for comparing values:

*   `==` (equal to)
*   `!=` (not equal to)
*   `>` (greater than)
*   `<` (less than)
*   `>=` (greater than or equal to)
*   `<=` (less than or equal to)

```femcode
UwU Boy 5 == 5 # Prints Kawaii
UwU Boy 10 < 5 # Prints Cringe
```

### Logical Operators

Used for combining boolean expressions:

*   `and` (logical AND)
*   `or` (logical OR)
*   `not` (logical NOT)

```femcode
UwU Boy Kawaii and Cringe # Prints Cringe
UwU Boy Kawaii or Cringe # Prints Kawaii
UwU Boy not Kawaii # Prints Cringe
```

## 6. Control Flow

### Conditional Statements (If/Else)

Use `Femboy Feminine` for `if` and `Androgyny` for `else` to control program flow based on conditions.

```femcode
my_age is 20
Femboy Feminine my_age > 18 Femboycore
    UwU Boy "You are an adult femboy!"
Periodt
Androgyny Femboycore
    UwU Boy "You are a young femboy!"
Periodt
```

### Loops (While)

Use `Otokonoko` for `while` loops to repeatedly execute a block of code as long as a condition is true.

```femcode
counter is 0
Otokonoko counter < 5 Femboycore
    UwU Boy counter
    counter is counter + 1
Periodt
```

### For Loops

Use `Tomgirl` for `for` loops to iterate over elements in a list or string.

```femcode
my_list is ["apple", "banana", "cherry"]
Tomgirl item is my_list Femboycore
    UwU Boy item
Periodt

my_string is "Femboy"
Tomgirl char is my_string Femboycore
    UwU Boy char
Periodt
```

### Break and Continue

*   `Break`: Immediately exits the current loop.
*   `Continue`: Skips the rest of the current loop iteration and proceeds to the next.

```femcode
counter is 0
Otokonoko counter < 10 Femboycore
    counter is counter + 1
    Femboy Feminine counter == 5 Femboycore
        Break
    Periodt
    Femboy Feminine counter == 2 Femboycore
        Continue
    Periodt
    UwU Boy counter
Periodt
```

## 7. Functions

### Defining Functions

Functions are defined using the `Femboy` keyword, followed by the function name, optional parameters in parentheses, and a code block enclosed by `Femboycore` and `Periodt`.

```femcode
Femboy say_hello() Femboycore
    UwU Boy "Hello from function!"
Periodt

Femboy add_numbers(a, b) Femboycore
    Femme a + b
Periodt
```

### Calling Functions

Functions are called by their name followed by parentheses, enclosing any arguments.

```femcode
say_hello()
result is add_numbers(10, 5)
```

### Return Values

Use the `Femme` keyword to return a value from a function.

```femcode
Femboy get_kawaii_status() Femboycore
    Femme Kawaii
Periodt

status is get_kawaii_status()
UwU Boy status # Prints Kawaii
```

### Built-in Functions

Femcode provides several built-in functions for common tasks:

*   `ask(prompt)`: Prompts the user for input and returns it as a string.
    ```femcode
    name is ask("What's your name, femboy? ")
    UwU Boy "Hello, " + name + "!"
    ```

*   `len(value)`: Returns the length of a string or a list.
    ```femcode
    my_string is "Cute"
    my_list is [1, 2, 3]
    UwU Boy len(my_string) # Prints 4
    UwU Boy len(my_list) # Prints 3
    ```

*   `type(value)`: Returns the type of a value as a string (e.g., "int", "str", "list", "dict", "bool").
    ```femcode
    UwU Boy type(123) # Prints "int"
    UwU Boy type("hello") # Prints "str"
    UwU Boy type(Kawaii) # Prints "bool"
    ```

## 8. Comments

Single-line comments start with a `#` symbol. Anything after `#` on the same line is ignored by the interpreter.

```femcode
# This is a single-line comment
UwU Boy "Hello, Femcode!" # This is also a comment
```

## 9. Input/Output

Input is handled via the `ask` built-in function, and output is handled via the `UwU Boy` (print) command.

```femcode
name is ask("Enter your name: ")
UwU Boy "Your name is: " + name
```

## 10. Error Handling

Femcode supports basic error handling using `Twink` (try) and `Bimboy` (except) blocks.

```femcode
Twink Femboycore
    # Code that might cause an error
    result is 10 / 0 # This will cause a division by zero error
    UwU Boy result
Periodt
Bimboy Femboycore
    UwU Boy "An error occurred!"
Periodt
```

## 11. Syntactic Sugar

### Compound Assignment Operators

Shorthand operators for common assignment operations:

*   `+=` (add and assign)
*   `-=` (subtract and assign)
*   `*=` (multiply and assign)
*   `/=` (divide and assign)

```femcode
count is 5
count += 3 # Equivalent to: count is count + 3
UwU Boy count # Prints 8
```

### Increment/Decrement Operators

*   `++` (increment by 1)
*   `--` (decrement by 1)

```femcode
value is 10
value++ # Equivalent to: value is value + 1
UwU Boy value # Prints 11
value-- # Equivalent to: value is value - 1
UwU Boy value # Prints 10
```