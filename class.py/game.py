class Character:
    def __init__(self, health, damage, speed):
        self.health = health
        self.damage = damage
        self.speed = speed

warrior = Character(100, 20, 10)
ninja = Character(80, 25, 15)
print(f'warrior speed: {warrior.speed}')
print(f'ninja health: {ninja.health}')    
