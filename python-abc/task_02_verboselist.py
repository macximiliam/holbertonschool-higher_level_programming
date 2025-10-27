#!/usr/bin/python3


class VerboseList(list):

    def append(self, item):
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        super().extend(iterable)
        print(f"Extend the list whith [{len (iterable)}].")

    def remove(self, item):
        super().remove(item)
        print(f"Remove [{item}] from the list.")


    def pop(self, index=-1):
        item = self[index]
        print(f"Popped [{item}] from the list.")
 