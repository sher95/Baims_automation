import configparser


def read_configuration(category, key):
    config = configparser.ConfigParser()
    config.read("../configurations/biams_config_auto.ini")
    return config.get(category, key)
