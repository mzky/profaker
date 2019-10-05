#!/usr/bin/python
# some functions
import string
import random

def random_number():
    return random.choice(string.digits)

def random_lowercase():
    return random.choice(string.ascii_lowercase)

def random_uppercase():
    return random.choice(string.ascii_uppercase)

def random_lettercase():
    return random.choice(string.ascii_letters)

def random_all():
    return random.choice(string.ascii_lowercase+string.digits)

def get_number(n=10):
    s = ''
    for i in range(n):
        s += random_number()
    return s

def get_lowercase(n=10):
    s = ''
    for i in range(n):
        s += random_lowercase()
    return s

def get_letter(n=10):
    s = ''
    for i in range(n):
        s += random_lettercase()
    return s

def get_mix(n=10):
    s = ''
    for i in range(n):
        s += random_all()
    return s

