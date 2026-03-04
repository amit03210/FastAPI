# FILE: rpg_hero.py
"""
SCENARIO: Design a character system where classes mix abilities.
INSTRUCTIONS:
1. Create a class 'Spellcaster' with a 'cast_spell()' method.
2. Create a class 'Warrior' with a 'melee_attack()' method.
3. Create a class 'BattleMage' that inherits from BOTH Spellcaster and Warrior.
4. Add a method to BattleMage called 'special_move' that calls both parent methods.
5. Use `print(BattleMage.mro())` to visualize the Method Resolution Order.
"""

class Spellcaster:
    def cast_spell(self):
        return f"Spell has been casted"
    def info(self):
        return f"I cast spell"

class Warrior:
    def melee_attack(self):
        return f"Attack with weapon"
    def info(self):
        return f"I enable melee attack feature"

class BattleMage(Spellcaster, Warrior):
    def special_move(self):
        return (self.cast_spell(), self.melee_attack())
    
    def info(self):
        return f"I harness power"
    
    def print_info(self):
        return (super().info())

bt = BattleMage()
print(bt.special_move())
print(BattleMage.mro())
print(bt.info())
print(bt.print_info())