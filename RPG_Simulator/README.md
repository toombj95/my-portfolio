\# ⚔️ RPG Battle Simulator



A turn-based, text-based Python battle simulator where players create heroes, battle enemies, gain XP, and level up.  

This project showcases \*\*object-oriented programming\*\*, \*\*class inheritance\*\*, and \*\*interactive user input\*\* in a console-based RPG environment.





\## 🚀 Features



\- 🎮 Interactive, turn-based combat between players and enemies  

\- 💥 Player leveling system with XP gained from attacks and defeated enemies  

\- 🧙‍♂️ Custom character creation (with default fallbacks)  

\- 🛡️ Defend mechanic to halve incoming damage  

\- 🧱 Enemy armor system that absorbs damage before HP loss  

\- 📈 Automatic level-up system that increases stats dynamically  

\- 🧩 Modular, object-oriented design with clean code and docstrings  

\- 🖥️ Console-based interface for easy interaction  





\## 🧩 Program Overview



\### 1. Character Class (`Character`)

Base class for all characters in the game.  

Defines shared attributes (`name`, `level`, `hp`) and core functionality.  



\*\*Key Features:\*\*

\- Inheritance base for `Player` and `Enemy`

\- Combine characters using `\_\_add\_\_`

\- Compare or print characters cleanly with `\_\_str\_\_`







\### 2. Player Class (`Player`)

Represents the player-controlled character.  

Tracks experience points (XP), manages attacks, defenses, and leveling.  



* Attributes:

&nbsp;	- `xp`: Experience points  

&nbsp;	- `base\_damage`: Attack power that scales with level  

&nbsp;	- `defending`: Flag for reducing damage when defending  



\*\*Key Methods:\*\*

\- `attack(target)`: Deals damage and grants XP per attack  

\- `add\_xp(amount)`: Increases XP and triggers level-ups  

\- `level\_up()`: Boosts HP and base damage  

\- `take\_damage(value)`: Reduces HP based on incoming attacks  



🧮 \*\*XP System:\*\*  

\- +5 XP for each attack  

\- +10 bonus XP for defeating an enemy  

\- Level-up every 100 × current level XP  





\### 3. \*\*Enemy Class (`Enemy`)\*\*

Represents AI-controlled foes with armor and attack power.  



\*\*Attributes:\*\*

\- `armor`: Damage buffer before HP loss  

\- `base\_damage`: Attack power  



\*\*Key Methods:\*\*

\- `attack(target)`: Attacks a random player  

\- `deal\_damage()`: Applies a class-based damage multiplier  

\- `take\_damage(value)`: Reduces armor first, then HP  



🧱 \*\*Armor Mechanics:\*\*  

Damage applies to armor first; only leftover damage reduces HP.  



---



\### 4. \*\*Battle Function (`battle(players, enemies)`)\*\*

Runs the \*\*interactive turn-based battle loop\*\*.  

Players choose to \*\*Attack\*\* or \*\*Defend\*\* each round.  



\*\*Flow:\*\*

1\. Each player takes a turn  

2\. Enemies retaliate  

3\. XP and bonus XP are awarded  

4\. Status is displayed  

5\. User decides to continue or quit  



The battle ends when all players or enemies are defeated.  



---



\## 🧠 Skills Demonstrated



\- \*\*Object-Oriented Programming\*\*: inheritance, polymorphism, and encapsulation  

\- \*\*Game Design Logic\*\*: player/enemy turns, XP progression  

\- \*\*User Interaction\*\*: input handling and real-time feedback  

\- \*\*Dynamic Lists\*\*: tracking live player/enemy status  

\- \*\*Data Validation\*\*: preventing invalid user choices  

\- \*\*Code Readability\*\*: modular design and docstring documentation  



---



\## ▶️ How to Run



1\. \*\*Install Python 3.8+\*\*  

&nbsp;  Verify installation with:

&nbsp;  ```bash

&nbsp;  python --version



