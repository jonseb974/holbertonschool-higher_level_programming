# Python - More Data Structures: Set, Dictionary



## General

    * Why Python programming is awesome
    * What are sets and how to use them
    * What are the most common methods of set and how to use them
    * When to use sets versus lists 
    * How to iterate into a set
    * What are dictionaries and how to use them
    * When to use dictionaries versus lists or sets
    * What is a key in a dictionary
    * How to iterate over a dictionary
    * What is a lambda function
    * What are the map, reduce and filter functions



## Getting Started

### 0. Squared simple
    mandatory
    Write a function that computes the square value of all integers of a matrix.

    * Prototype: def square_matrix_simple(matrix=[]):
    * matrix is a 2 dimensional array
    * Returns a new matrix:
        * Same size as matrix
        * Each value should be the square of the value of the input
    * Initial matrix should not be modified
    * You are not allowed to import any module
    * You are allowed to use regular loops, map, etc.
```
guillaume@ubuntu:~/$ cat 0-main.py
#!/usr/bin/python3
square_matrix_simple = __import__('0-square_matrix_simple').square_matrix_simple

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

new_matrix = square_matrix_simple(matrix)
print(new_matrix)
print(matrix)

guillaume@ubuntu:~/$ ./0-main.py
[[1, 4, 9], [16, 25, 36], [49, 64, 81]]
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
guillaume@ubuntu:~/$ 
```


















### Dependencies

* 
* 

### Installing

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

