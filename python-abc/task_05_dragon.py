#!/usr/bin/python3
"""
This module demonstrates multiple inheritance using mixins.
It includes SwimMixin, FlyMixin, and Dragon classes.
"""

class SwimMixin:
    """Mixin that provides swimming behavior."""
    
    def swim(self):
        """Prints a message showing that the creature can swim."""
        print("The creature swims!")


class FlyMixin:
    """Mixin that provides flying behavior."""
    
    def fly(self):
        """Prints a message showing that the creature can fly."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Represents a dragon that can both swim and fly."""
    
    def roar(self):
        """Prints a message showing that the dragon can roar."""
        print("The dragon roars!")
