import random

class Character():
    '''Base class for inheritance'''

    def __init__(self, name='Tom Nook', level=1, hp=50):
        '''initializes a new character instance with default
        attributes if no arguments are passed'''
        self.name = name
        self.level = level
        self.hp = hp

    def __str__(self):
        '''returns formatted string to show character details'''
        return f"Name: {self.name}\nCurrent level: {self.level}\nCurrent hit point: {self.hp}"

    def __add__(self, other):
        '''Creates a new team by adding 2 character instances. Combines their hp, level, and name values'''
        new_name = f"Team {self.name} and {other.name}"
        new_level = self.level + other.level
        new_hp =self.hp + other.hp
        return Character(name=new_name, level=new_level, hp=new_hp)


class Player(Character):
    '''represents a video game player character
    Attributes: listed in positional argument order
        name (str): the name of the player character
        level (int): the experience level of the player
        HP (int): the hit points(health) of the player
        XP (int): the experience points of the player'''
    
    def __init__(self, name="Ashen One", level=1, hp=100, base_damage=10):
        '''initializes a new Player instance with default attributes
        if user provides no arguments'''
        super().__init__(name, level, hp)
        self.base_damage = base_damage + (level - 1) * 2.5
        self.xp = 0
        self.defending = False
        
    def __str__(self):
        '''returns formatted string show player details'''
        return f"Player Name: {self.name}\nCurrent level: {self.level}\nCurrent HP: {self.hp}\nXP: {self.xp}"

    def attack(self, target):
        """Deals damage to a target Enemy and grants XP."""
        damage = self.base_damage
        print(f"{self.name} attacks {target.name} for {damage} damage!\n")
        target.take_damage(damage)

        # Add XP for attacking
        xp_per_attack = 10
        self.add_xp(xp_per_attack)

        # Bonus XP if the enemy is defeated
        if target.hp <= 0:
            bonus_xp = 10
            print(f"{self.name} defeated {target.name} and gains {bonus_xp} bonus XP!")
            self.add_xp(bonus_xp)

    def check_level_up(self):
        '''Level up automatically when XP threshold is reached'''
        xp_needed = 100 * self.level
        while self.xp >= xp_needed:
            self.xp -= xp_needed
            self.level_up()
            xp_needed = 100 * self.level
            
    def add_xp(self, amount):
        self.xp += amount
        print(f"{self.name} gains {amount} XP! Total XP: {self.xp}")
        xp_needed = 100 * self.level
        while self.xp >= xp_needed:
            self.xp -= xp_needed
            self.level_up()
            xp_needed = 100 * self.level

    def level_up(self):
        '''increments a player's current level and boost stats'''
        self.level += 1
        self.hp += 10
        self.base_damage += 2.5
        print(f"{self.name} leveled up! Now level {self.level}. Damage is now {self.base_damage}.")

    def take_damage(self, value):
        '''subtracts a player's hit points by the value'''
        self.hp -= value
        print(f"{self.name} takes {value} damage! Remaining HP: {self.hp}")

class Enemy(Character):
    '''represents an enemy character class
    Attributes:
        hp (int): the hit points(health) of the enemy
        base_damage (int): the base damage dealt to opponent'''

    damage_multiplier = 3 #class variable for damage multiplier
    armor_bonus = 10 #class variable for armor bonus

    def __init__(self, name="Goblin", hp=30, base_damage=5):
        '''initializes a new Enemy instance with default attributes if no arguments are provided'''
        super().__init__(name, level=1, hp=hp)
        self.base_damage = base_damage
        self.armor = Enemy.armor_bonus  #tracks armor per instance

    def __str__(self):
        '''returns formatted string show enemy details'''
        return (f"Enemy Name: {self.name}\nLevel: {self.level}\nHP: {self.hp}\nBase damage: {self.base_damage}\nArmor: {self.armor}")

    def attack(self, target):
        '''Deals damage to a target Player'''
        damage = self.base_damage
        print(f"{self.name} attacks {target.name} for {damage} damage!\n")
        target.take_damage(damage)
        
    def deal_damage(self):
        '''multiplies Enemy's base_damage by the damage_multiplier, returns the value of damage to deal to opponent'''
        return self.base_damage * Enemy.damage_multiplier

    def take_damage(self, damage_value):
        '''first applies damage to enemy's instance armor_bonus, once armor_bonus is depleted the remaining
        damage is applied to enemy's hp'''

        #Armor takes all the damage
        if damage_value <= self.armor:
            self.armor -= damage_value

        #Armor is depleted, remaining damage to HP
        else:
            damage_to_hp = damage_value - self.armor
            self.armor = 0
            self.hp -= damage_to_hp


# -------------------------
# Mini RPG Battle Simulator
# -------------------------

def battle(players, enemies):
    """Interactive turn-based battle with XP rewards and defend mechanic."""
    round_num = 1
    while any(p.hp > 0 for p in players) and any(e.hp > 0 for e in enemies):
        print(f"\n--- Round {round_num} ---\n")

        # Players' turns
        for p in players:
            if p.hp <= 0:
                continue

            print(f"\n{p.name}'s turn! HP: {p.hp}, Level: {p.level}, XP: {p.xp}")
            print("Choose an action:")
            print("1: Attack")
            print("2: Defend")
            action = input("Enter action number: ")

            while action not in ["1", "2"]:
                action = input("Invalid choice. Enter 1 (Attack) or 2 (Defend): ")

            if action == "1":
                # Choose an enemy to attack
                living_enemies = [e for e in enemies if e.hp > 0]
                print("\nEnemies:")
                for idx, e in enumerate(living_enemies):
                    print(f"{idx + 1}: {e.name} - HP: {e.hp}, Armor: {e.armor}")
                choice = input(f"Choose enemy to attack (1-{len(living_enemies)}): ")
                while not choice.isdigit() or int(choice) < 1 or int(choice) > len(living_enemies):
                    choice = input(f"Invalid choice. Choose enemy (1-{len(living_enemies)}): ")
                target = living_enemies[int(choice) - 1]

                # Attack and award XP
                target_hp_before = target.hp
                p.attack(target)  # attack() now awards XP for attacking
                if target.hp <= 0 and target_hp_before > 0:
                    bonus_xp = 10
                    print(f"{p.name} defeated {target.name}! Gains {bonus_xp} bonus XP!")
                    p.add_xp(bonus_xp)

            elif action == "2":
                # Defend
                print(f"{p.name} is defending this round! Damage will be halved.")
                p.defending = True

        # Enemies' turns
        for e in enemies:
            if e.hp <= 0:
                continue
            living_players = [p for p in players if p.hp > 0]
            target = random.choice(living_players)

            if getattr(target, "defending", False):
                damage = (e.deal_damage() + 1) // 2  # half damage
                print(f"{target.name} is defending! Damage reduced to {damage}.")
                target.take_damage(damage)
                target.defending = False
            else:
                e.attack(target)

        # Remove defeated characters
        enemies = [e for e in enemies if e.hp > 0]
        players = [p for p in players if p.hp > 0]

        # Show status
        print("\nStatus after this round:")
        for p in players:
            print(f"{p.name} - HP: {p.hp}, Level: {p.level}, XP: {p.xp}")
        for e in enemies:
            print(f"{e.name} - HP: {e.hp}, Armor: {e.armor}")

        # Continue?
        choice = input("\nContinue to next round? (y/n) ").lower()
        if choice != "y":
            print("\nGame ended. Thanks for playing")
            break

        round_num += 1

    # Determine outcome
    if all(e.hp <= 0 for e in enemies):
        print("\nPlayers win!")
        for p in players:
            p.level_up()
    elif all(p.hp <= 0 for p in players):
        print("\nEnemies win!")


# -------------------------
# Demo
# -------------------------

if __name__ == "__main__":
    print("Welcome to the RPG Battle Simulator!\n")
    
    # Create players
    num_players_input = input("How many players? (default 1): ")
    num_players = int(num_players_input) if num_players_input.strip() else 1
    players = []
    for i in range(num_players):
        name_input = input(f"Enter Player {i+1} name (default 'Ashen One'): ")
        name = name_input.strip() if name_input.strip() else f"Ashen One {i+1}"
        base_damage_input = input(f"Enter base damage (default 10): ")
        base_damage = float(base_damage_input) if base_damage_input.strip() else 10
        players.append(Player(name=name, base_damage=base_damage))

    # Create enemies
    num_enemies_input = input("How many enemies? (default 1): ")
    num_enemies = int(num_enemies_input) if num_enemies_input.strip() else 1
    enemies = []
    for i in range(num_enemies):
        name_input = input(f"Enter Enemy {i+1} name (default 'Goblin'): ")
        name = name_input.strip() if name_input.strip() else f"Goblin {i+1}"
        hp_input = input(f"Enter HP (default 50): ")
        hp = int(hp_input) if hp_input.strip() else 50
        damage_input = input(f"Enter base damage (default 5): ")
        base_damage = float(damage_input) if damage_input.strip() else 5
        enemies.append(Enemy(name=name, hp=hp, base_damage=base_damage))
        
    # Start battle
    battle(players, enemies)
