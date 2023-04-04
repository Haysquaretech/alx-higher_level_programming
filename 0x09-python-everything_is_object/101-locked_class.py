#!/usr/bin/python3
"""Defines a locked class here"""


class LockedClass:
    """
    Prevents the user from instantiating new LockedClass attributes
    except the attribute is called 'first_name'.
    """

    __slots__ = ["first_name"]
