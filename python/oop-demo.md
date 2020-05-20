Brief demo of object-oriented programming concepts in Python

```python
"""oop_demo.py

Player is a base class. Wizard and Dragon inherit from Player.

All Player objects have name, level, and move() method.
Wizard and Dragon objects implement a few specialized attributes and methods.

Concepts: inheritance, attributes, methods, super()

References:
    https://realpython.com/python3-object-oriented-programming/

"""

class Player():
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def move(self):
        print(f"{self.name} is moving")

    def __repr__(self):
        return f"name: {self.name}, 'level': {self.level}"

class Wizard(Player):
    def __init__(self, name, level, hat_color):
        self.hat_color = hat_color
        super().__init__(name, level)

    def cast_spell(self, spell):
        print(f"{self.name} casting: {spell}")

class Dragon(Player):
    def __init__(self, name, level, color):
        self.color = color
        super().__init__(name, level)

    def breathe_fire(self, color):
        print(f"{self.name} breathing {color} fire")


if __name__ == "__main__":
    p = Player(name="Pikachu", level=10)
    w = Wizard(name="Gandolf", level=12, hat_color="red")
    d = Dragon(name="Charizard", level=20, color="orange")

    # methods
    w.move()
    p.move()
    w.cast_spell("wingardium")
    d.breathe_fire("blue")
    d.breathe_fire("red")

    # attributes
    print("wizard name is:", w.name)
    print("wizard level is:", w.level)
    print("dragon -->", d)
    print("wizard -->", w)

"""
# Classes can have more than 1 parent (multiple inheritance). 
# let's say that a Wizard can inherit from both Player and Bot classes
>>> class Wizard(Player, Bot):
        pass
>>> b = Wizard(name="bot1", level=100)
"""
```
___

Output
```
Gandolf is moving
Pikachu is moving
Gandolf casting: wingardium
Charizard breathing blue fire
Charizard breathing red fire
wizard name is: Gandolf
wizard level is: 12
dragon --> name: Charizard, 'level': 20
wizard --> name: Gandolf, 'level': 12
```
