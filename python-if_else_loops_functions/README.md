# Project Title

Python - If/else, loops, functions.

## Description

This project is a foundation of Python learning programme Holberton School Laval.

## Getting Started

### General
* Why Python programming is awesome
* Why indentation is so important in Python
* How to use the if, if ... else statements
* How to use comments
* How to affect values to variables
* How to use the while and for loops
* How is Python’s for different from C‘s?
* How to use the break and continues statements
* How to use else clauses on loops
* What does the pass statement do, and when to use it
* How to use range
* What is a function and how do you use functions
* What does return a function that does not use any return statement
* Scope of variables
* What’s a traceback
* What are the arithmetic operators and how to use them


### Requirements

* Allowed editors: vi, vim, emacs
* All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
* All your files should end with a new line
* The first line of all your files should be exactly #!/usr/bin/python3
* A README.md file, at the root of the folder of the project, is mandatory
* Your code should use the pycodestyle (version 2.7.*)
* All your files must be executable
* The length of your files will be tested using wc

### Executing program

* How to run the program
* Step-by-step bullets
```
code blocks for commands
```
### Task 0

## 0. Positive anything is better than negative nothing
mandatory
This program will assign a random signed number to the variable number each time it is executed. Complete the source code in order to print whether the number stored in the variable number is positive or negative.

	* You can find the source code here
	* The variable number will store a different value every time you will run this program
	* You don’t have to understand what import, random. randint do. Please do not touch this code
	* The output of the program should be:
	* The number, followed by
	* if the number is greater than 0: is positive
	* if the number is 0: is zero
	* if the number is less than 0: is negative
	* followed by a new line
```
guillaume@ubuntu:~/$ ./0-positive_or_negative.py 
-4 is negative
guillaume@ubuntu:~/$ ./0-positive_or_negative.py 
0 is zero
guillaume@ubuntu:~/$ ./0-positive_or_negative.py 
-3 is negative
guillaume@ubuntu:~/$ ./0-positive_or_negative.py 
-10 is negative
guillaume@ubuntu:~/$ ./0-positive_or_negative.py 
10 is positive
guillaume@ubuntu:~/$ ./0-positive_or_negative.py 
-5 is negative
guillaume@ubuntu:~/$ ./0-positive_or_negative.py 
6 is positive
guillaume@ubuntu:~/$ ./0-positive_or_negative.py 
7 is positive
guillaume@ubuntu:~/$ ./0-positive_or_negative.py 
5 is positive
guillaume@ubuntu:~/$ 
```
## 1. The last digit
	* This program will assign a random signed number to the variable number each time it is executed. Complete the source code in order to print the last digit of the number stored in the variable number.
	* You can find the source code here
	* The variable number will store a different value every time you will run this program
	* You don’t have to understand what import, random.randint do. Please do not touch this code. This line should not change: number = random.randint(-10000, 10000)
	* The output of the program should be:
	* The string Last digit of, followed by
the number, followed by
		* the string is, followed by the last digit of number, followed by
		* if the last digit is greater than 5: the string and is greater than 5
		* if the last digit is 0: the string and is 0
		* if the last digit is less than 6 and not 0: the string and is less than 6 and not 0
		* followed by a new line
```
guillaume@ubuntu:~/$ ./1-last_digit.py
Last digit of 4205 is 5 and is less than 6 and not 0
guillaume@ubuntu:~/$ ./1-last_digit.py
Last digit of -626 is -6 and is less than 6 and not 0
guillaume@ubuntu:~/$ ./1-last_digit.py
Last digit of 1144 is 4 and is less than 6 and not 0
guillaume@ubuntu:~/$ ./1-last_digit.py
Last digit of -9200 is 0 and is 0
guillaume@ubuntu:~/$ ./1-last_digit.py
Last digit of 5247 is 7 and is greater than 5
guillaume@ubuntu:~/$ ./1-last_digit.py
Last digit of -9318 is -8 and is less than 6 and not 0
guillaume@ubuntu:~/$ ./1-last_digit.py
Last digit of 3369 is 9 and is greater than 5
guillaume@ubuntu:~/$ ./1-last_digit.py
Last digit of -5224 is -4 and is less than 6 and not 0
guillaume@ubuntu:~/$ ./1-last_digit.py
Last digit of -4485 is -5 and is less than 6 and not 0
guillaume@ubuntu:~/$ ./1-last_digit.py
Last digit of 3850 is 0 and is 0
guillaume@ubuntu:~/$ ./1-last_digit.py
Last digit of 5169 is 9 and is greater than 5
guillaume@ubuntu:~/$ 
```

## 2. I sometimes suffer from insomnia. And when I can't fall asleep, I play what I call the alphabet game
mandatory
Write a program that prints the ASCII alphabet, in lowercase, not followed by a new line.

* You can only use one print function with string format
* You can only use one loop in your code
* You are not allowed to store characters in a variable
* You are not allowed to import any module

```
guillaume@ubuntu:~/$ ./2-print_alphabet.py
abcdefghijklmnopqrstuvwxyzguillaume@ubuntu:~/$
```













## Help

Any advise for common problems or issues.
```
command to run if program contains helper info
```

## Authors

Contributors names and contact info

ex. Dominique Pizzie
ex. [@DomPizzie](https://twitter.com/dompizzie)

## Version History

* 0.2
    * Various bug fixes and optimizations
    * See [commit change]() or See [release history]()
* 0.1
    * Initial Release

## License

This project is licensed under the [NAME HERE] License - see the LICENSE.md file for details

## Acknowledgments

Inspiration, code snippets, etc.
* [awesome-readme](https://github.com/matiassingers/awesome-readme)
* [PurpleBooth](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2)
* [dbader](https://github.com/dbader/readme-template)
* [zenorocha](https://gist.github.com/zenorocha/4526327)
* [fvcproductions](https://gist.github.com/fvcproductions/1bfc2d4aecb01a834b46)

