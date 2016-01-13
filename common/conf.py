from ConfigParser import ConfigParser, Error

class ConfigurationError(Exception):
    pass

class EnvironmentConfig(object):

    def initialize(self, ini_file_path):
        self.parser = ConfigParser()
        try:
            self.parser.read(ini_file_path)
        except Error as e:
            raise ConfigurationError("Error reading config ini file. {0}"
                .format(ini_file_path))

    def _get(self, method, section, key):
        try:
            return method(section, key)
        except Error as e:
            raise ConfigurationError(
                "Error reading config value. Section: {0}, Key: {1}"
                .format(section, key))

    def get(self, section, key):
        return self._get(self.parser.get, section, key)

    def getint(self, section, key):
        return self._get(self.parser.getint, section, key)

    def getfloat(self, section, key):
        return self._get(self.parser.getfloat, section, key)

