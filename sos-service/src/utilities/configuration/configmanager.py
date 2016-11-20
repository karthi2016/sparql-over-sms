
class ConfigManager:
    """Configuration Manager"""

    def __init__(self):
        self.configuration = {}
        pass

    def get_config(self, key, default=None):
        return self.configuration.get(key, default)

    def set_config(self, key, value):
        self.configuration[key] = value
