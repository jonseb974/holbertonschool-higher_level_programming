# Python - import & modules


## Description


## Getting Started

### Dependencies

* 
* 

## Task-0

### 0. Import a simple function from a simple file
mandatory
Write a program that imports the function def add(a, b): from the file add_0.py and prints the result of the addition 1 + 2 = 3

* You have to use print function with string format to display integers
* You have to assign:
	* the value 1 to a variable called a
	* the value 2 to a variable called b
	* and use those two variables as arguments when calling the functions add and print
	* a and b must be defined in 2 different lines: a = 1 and another b = 2

* Your program should print: <a value> + <b value> = <add(a, b) value> followed with a new line
* You can only use the word add_0 once in your code
* You are not allowed to use * for importing or __import__
* Your code should not be executed when imported - by using __import__, like the example below
```
guillaume@ubuntu:~/$ cat add_0.py
#!/usr/bin/python3
def add(a, b):
    """My addition function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a + b
    """
    return (a + b)

guillaume@ubuntu:~/$ ./0-add.py
1 + 2 = 3
guillaume@ubuntu:~/$ cat 0-import_add.py
__import__("0-add")
guillaume@ubuntu:~/$ python3 0-import_add.py 
guillaume@ubuntu:~/$ 
```
* 
* 

### Executing program

* 
* 
```
code blocks for commands
```

## Help

Any advise for common problems or issues.
```
command to run if program contains helper info
```

## Authors
Sebastien JONAD
ex. [](5151@holbertonstudents.com)

## 

* 
    * 
    * 
* 
    * 

## License

This project is licensed under the [NAME HERE] License - see the LICENSE.md file for details

## Acknowledgments

Inspiration, code snippets, etc.
* [awesome-readme](https://github.com/matiassingers/awesome-readme)
* [PurpleBooth](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2)
* [dbader](https://github.com/dbader/readme-template)
* [zenorocha](https://gist.github.com/zenorocha/4526327)
* [fvcproductions](https://gist.github.com/fvcproductions/1bfc2d4aecb01a834b46)

