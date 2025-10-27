#!/usr/bin/python3
"""
This module defines classes to demonstrate multiple inheritance in Python.
It includes Fish, Bird, and FlyingFish classes.
"""

class Fish:
    """Represents a fish with swimming ability and aquatic habitat."""
    
    def swim(self):
        """Prints a message showing that the fish is swimming."""
        print("The fish is swimming")

    def habitat(self):
        """Prints a message describing the fish's habitat."""
        print("The fish lives in the water")


class Bird:
    """Represents a bird with flying ability and sky habitat."""
    
    def fly(self):
        """Prints a message showing that the bird is flying."""
        print("The bird is flying")

    def habitat(self):
        """Prints a message describing the bird's habitat."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """Represents a flying fish that inherits from both Fish and Bird."""
    
    def fly(self):
        """Prints a message showing that the flying fish can soar."""
        print("The flying fish is soaring!")

    def swim(self):
        """Prints a message showing that the flying fish can swim."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Prints a message describing the flying fish's dual habitat."""
        print("The flying fish lives both in water and the sky!")
