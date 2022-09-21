# JONAD Seébastien
## Python - Test-driven development

[![N|Solid](https://cldup.com/dTxpPi9lDf.thumb.png)](https://nodesource.com/products/nsolid)

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

- 
- See 
- ✨Magic ✨

## General

- Why Python programming is awesome
- What’s an interactive test
- How to write documentation for each module and function
- Why tests are important
- What are the basic option flags to create tests
- How to find edge cases


> The overriding design goal for Markdown's
> formatting syntax is to make it as readable
> as possible. The idea is that a
> Markdown-formatted document should be
> publishable as-is, as plain text, without
> looking like it's been marked up with tags
> or formatting instructions.

This text you see here is *actually- written in Markdown! To get a feel
for Markdown's syntax, type some text into the left window and
watch the results in the right.

## Temporary reamde file



## 0. Integers addition

Write a function that adds 2 integers.

    * Prototype: def add_integer(a, b=98):
    * a and b must be integers or floats, otherwise raise a TypeError exception with the message a    must be an integer or b must be an integer
    * a and b must be first casted to integers if they are float
    * Returns an integer: the addition of a and b
    * You are not allowed to import any module

```
#!/usr/bin/python3
add_integer = __import__('0-add_integer').add_integer

print(add_integer(1, 2))
print(add_integer(100, -2))
print(add_integer(2))
print(add_integer(100.3, -2))
try:
    print(add_integer(4, "School"))
except Exception as e:
    print(e)
try:
    print(add_integer(None))
except Exception as e:
    print(e)
```
