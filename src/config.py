import json


class Config:
    def __init__(self, config_path="../config.json"):
        with open(config_path) as f:
            self._config_raw = json.load(f)
        self.solver = None

        for key in self._config_raw:
            setattr(self, key, self._config_raw[key])