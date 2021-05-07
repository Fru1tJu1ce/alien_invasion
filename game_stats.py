import json


class GameStats():
    """Отслеживание статистики для игры Alien Invasion."""
    
    def __init__(self, ai_settings):
        """Инициализирует статистику."""
        self.ai_settings = ai_settings
        self.reset_stats()
        # Игра Alien Invasion запускается в неактивном состоянии.
        self.game_active = False
        
        self.high_score = self.get_high_score()
            
    
    def get_high_score(self):
        """Получает значение рекорда, если оно существует"""
        # Данные рекорда загружаются из файла
        filename = "high_score.json"
        try:
            with open(filename) as f_obj:
                high_score = json.load(f_obj)
            return high_score
        except FileNotFoundError:
            high_score = self.create_high_score_file()
            return high_score
            
    
    def create_high_score_file(self):
        """Создает файл с рекордом."""
        filename = "high_score.json"
        high_score = 0
        with open(filename, 'w') as f_obj:
            json.dump(high_score, f_obj)
        return high_score
 
        
    def reset_stats(self):
        """Инициализирует статистику, изменяющуюся в ходе игры."""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
        
    
