C++ Basic Structure
===================


.. code:: cpp

    #include <iostream>

    int main() {
      std::cout << "Hello, World!";
    }


**Explanation**


1. ``#include`` is a directive, a preprocessor command that tells the C++ compiler to paste the contents of a specified file directly into your code before compilation begins.

Syntax Forms

- **Angle brackets** (``<>``): Used for standard library or system headers like ``#include <iostream>``. The preprocessor searches standard system directories first.

- **Double quotes** (``""``): Used for local or user-defined files like ``#include "myheader.h"``. The preprocessor searches the current project directory first.


2. ``int main() {}`` is the mandatory entry point where C++ program begins execution.

3. ``std::cout`` is the standard output stream object in C++ used to print text, numbers, and variables to the console.

4. ``<<`` is the insertion operator to pass data into the stream.

5. ``"Hello, World!"`` is a string to print.

6. Lines shall end with a semicolon ``;``.