# Femcode Language Documentation

Femcode is a femboy-themed programming language designed to be simple, expressive, and fun. It features a unique syntax inspired by femboy terminology, making coding an adorable experience.

## Table of Contents

1.  [Getting Started](#getting-started)
2.  [Basic Syntax](#basic-syntax)
3.  [Variables and Assignment](#variables-and-assignment)
4.  [Data Types](#data-types)
    *   [Numbers](#numbers)
    *   [Strings](#strings)
    *   [Booleans](#booleans)
    *   [Lists](#lists)
    *   [Dictionaries](#dictionaries)
5.  [Operators](#operators)
    *   [Arithmetic Operators](#arithmetic-operators)
    *   [Comparison Operators](#comparison-operators)
    *   [Logical Operators](#logical-operators)
6.  [Control Flow](#control-flow)
    *   [Conditional Statements (If/Else)](#conditional-statements-ifelse)
    *   [Loops (While)](#loops-while)
7.  [Functions](#functions)
    *   [Defining Functions](#defining-functions)
    *   [Calling Functions](#calling-functions)
    *   [Return Values](#return-values)
    *   [Built-in Functions](#built-in-functions)
8.  [Comments](#comments)
9.  [Input/Output](#inputoutput)

## 1. Getting Started

To run Femcode programs, you need the Femcode interpreter. Navigate to the `femcode/src` directory and run `main.py` with your Femcode file.

```bash
python3 main.py ../examples/your_program.fem
```

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