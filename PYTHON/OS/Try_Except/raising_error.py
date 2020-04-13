#!/usr/bin/env python3

def validate_user(username, minlen):
    #   Assert keyword tries to verify that a conditional expression is true, and if it's false it
    #  raises an assertion error with the indicated message.
    assert type(username) == str, "Username must be a string"
    if minlen < 1:
        raise ValueError("Minlen must be atleast 1")
    if len(username) < minlen:
        return False
    if not username.isalnum():
        return False
    return True