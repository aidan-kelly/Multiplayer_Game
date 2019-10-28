class Player(object):
    char_name = ""
    health_points = 0
    armor_class = 0
    to_hit_bonus = 0
    damage_bonus = 0

    def __init__(self, char_name, health_points, armor_class, to_hit_bonus, damage_bonus):
        self.char_name = char_name
        self.health_points = health_points
        self.armor_class = armor_class
        self.to_hit_bonus = to_hit_bonus
        self.damage_bonus = damage_bonus