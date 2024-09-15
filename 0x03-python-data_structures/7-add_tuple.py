#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Ensure both tuples have at least 2 elements, filling with 0 if necessary
    tuple_a = tuple_a[:2] + (0, 0)
    tuple_b = tuple_b[:2] + (0, 0)
    
    # Return a new tuple by adding the first and second elements of both tuples
    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
