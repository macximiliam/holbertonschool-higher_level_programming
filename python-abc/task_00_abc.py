#!/usr/bin/python3
"""Module that shows how to use abstract classes in Python."""

from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract class that defines animal behavior."""

    @abstractmethod
    def sound(self):
        """Method to be implemented by all subclasses."""
        pass


class Dog(Animal):
    """Dog class that inherits from Animal."""

    def sound(self):
        """Return the sound of a dog."""
        return "Bark"


class Cat(Animal):
    """Cat class that inherits from Animal."""

    def sound(self):
        """Return the sound of a cat."""
        return "Meow"
