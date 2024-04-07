import os
import stat
import json

from utils.singleton import Singleton


USER_CONFIG_PATH = "user_config.json"


class UserConfig(metaclass=Singleton):

    def __init__(self):

        self._config_dict = {}
        if os.path.exists(USER_CONFIG_PATH):
            self._load_config_file()
        else:
            self._save_config_file()    # create a new config file

    def _load_config_file(self):
        if os.path.exists(USER_CONFIG_PATH):
            with open(USER_CONFIG_PATH, "r", encoding="utf-8") as f:
                self._config_dict = json.load(f)

    def _save_config_file(self):
        if os.path.exists(USER_CONFIG_PATH):
            # set write permission
            os.chmod(USER_CONFIG_PATH, stat.S_IWRITE)
        with open(USER_CONFIG_PATH, "w", encoding="utf-8") as f:
            json.dump(self._config_dict, f, indent=4)

    def get_config(self, key: str, default_value: any):
        if key in self._config_dict:
            return self._config_dict[key]
        else:
            self._config_dict[key] = default_value
            self._save_config_file()
            return default_value

    def set_config(self, key: str, value: any):
        self._config_dict[key] = value
        self._save_config_file()

    def set_configs(self, configs_dict: dict):
        for key, value in configs_dict.items():
            self._config_dict[key] = value
        self._save_config_file()
