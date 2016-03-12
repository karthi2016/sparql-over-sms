
class ConfigManager:
    """Configuration Manager"""

    def __init__(self, appconfig):
        self.appconfig = appconfig

    def get_configurations(self):
        return [k[2:] for k in self.appconfig.keys() if k.startswith('c_')]

    def get_configuration(self, name):
        config = self.appconfig['c_' + name]
        return self._configasdict(config)

    def get_section(self, name, section):
        section = self.appconfig['c_' + name][section]
        return self._sectionasdict(section)

    def get_option(self, configuration, section, option):
        return self.appconfig['c_' + configuration][section][option]

    def update_configuration(self, name, section, keyvalue):
        config = self.appconfig['c_' + name][section]

        for key, value in keyvalue.items():
            if config[key] is not None:
                config[key] = value

        filepath = self.appconfig['f_' + name]
        with open(filepath, 'w') as file:
            self.appconfig['c_' + name].write(file)

    def _configasdict(self, config):
        return {s: self._sectionasdict(config[s]) for s in config.sections()}

    def _sectionasdict(self, section):
        return {k: section[k] for k in section}
