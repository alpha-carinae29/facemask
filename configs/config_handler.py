import json


class Config:
    def __init__(self, path: str):
        self._path = path
        self._config = self._file_loader()

        self.VALID_FOLDER = self._config["validation"]["validation_image_folder"]

        self.MODEL_NAME = self._config["model"]["backend"]
        self.INCLUDE_TOP = self._config["model"]["include_top"]
        self.TRAINING = self._config["model"]["training"]

        self.PATH = self._config["dataset"]["path"]
        self.INPUT_SIZE = self._config["dataset"]["img_size"]
        self.NO_CHANNEL = self._config["dataset"]["no_channel"]
        self.NO_CLASSES = self._config["dataset"]["no_classes"]

        self.TRAIN_FOLDER = self._config["train"]["train_image_folder"]
        self.SAVED_FOLDER = self._config["train"]["saved_weights_folder"]
        self.BATCH_SIZE = self._config["train"]["batch_size"]
        self.LEARNING_RATE = self._config["train"]["learning_rate"]
        self.EPOCHS = self._config["train"]["epochs"]
        self.EXPORT_DIR = self._config["train"]["export_folder"]
        self.LOAD_PRETRAINED = self._config["model"]["load_pretrained"]
        self.PRETRAINED_MODEL = self._config["model"]["pretrained_model"]

    def _file_loader(self) -> dict:
        cfg = None
        try:
            with open(self._path) as file:
                cfg = json.loads(file.read())
        except FileNotFoundError as e:
            print(e)
            exit(1)
        return cfg
