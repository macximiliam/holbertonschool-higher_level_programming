#!/usr/bin/python3

class SwimMixin:
    def swim(self):
        print("he creature swims!")


class FlyMixin:
    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    def roar(self):
        print("The dragon roars!")