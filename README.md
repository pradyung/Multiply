# Multiply

## Introduction
This module contains four functions, the most important of which is the ```multiply()``` function. The ```multiply()``` function can be used to multiply two arbitrarily large decimal numbers. The numbers are passed to the function as strings and the product is also returned as a string. The module also contains an ```add()``` function, which is similar to ```multiply()```, but returns the sum of the two numbers instead.

## Details
The ```multiply()``` function iterates through the digits of the first input backwards, multiplies each digit by the second input, and keeps a cumulative sum of the products, similiarly to how you would work out a long multiplication problem on paper. In order to multiply each digit of the first number with the second one, it uses a helper function ```multiplySingleDig()``` which takes in one number of any length and another number which is a single digit and returns the product.

## Purpose
The ```multiply()``` and ```add()``` functions can be used to handle numbers which cannot be stored with traditional forms of integer storage. They can also be expanded upon to support fractional and mixed inputs. These functions can be useful for statisticians who work with extremely precise values and who need to perform calculations with them.