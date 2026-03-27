Password-Checker

A Python script that evaluates a user's password strength. built to hone my understanding of conditionals and string handling.

Goals

Build a tool that checks password strength

initial thoughts (what makes a good password)

Length and complexity

* 8-12 characters
* Use of numbers and symbols

Hard to decipher (common words or simple patterns)

* I acknowledge there’s a trade-off between security and memorability, but for the initial start of this project, I will try to keep it basic.

Code broken down

* Get user input
* check length
* Check for numbers
* Check for symbols
* produce strength rating

What I Struggled With

1. How to keep track of the character length of the user's password
2. How to know if there are numbers in the password.
2.1. But then I ran into the problem of isdigit() checking to see if the whole string was made of numbers instead of looking for a single character

How I Solved It

1. Implemented the Len() function and used it to calculate the character length of the user's password
2. implementing the isdigit() method, which returns true or false depending on whether numbers are found within the user's password
2.1 I had to implement a generator expression that used any() to check each character until a digit is found

What I Learned
- methods such as,isdigit(),len() and isupper()
- generator expression
-
Future Improvements
