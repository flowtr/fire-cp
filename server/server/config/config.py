from flowtr_config import Config
from flowtr_config.source.source import YamlConfigSource
from flowtr_config.validator import ValidationField
import logging
from typed_models import Model
from typed_models.fields import StringField, IntegerField


import coloredlogs

logging.basicConfig(level=logging.DEBUG, format="%(asctime)-15s %(message)s")
coloredlogs.install()
logger = logging.getLogger("flowtr.panel")


class AppConfig(Model):
    host = ValidationField(StringField(default="0.0.0.0"))
    port = ValidationField(IntegerField(default=6969))
    db_uri = ValidationField(StringField(default="postgresql://localhost/panel"))
    panel_url = ValidationField(StringField(), url={})
    environment = ValidationField(
        StringField(default="production"), one_of=["production", "development"]
    )


config = Config(AppConfig, sources=[YamlConfigSource(AppConfig)])
config.read(path="config.yaml")
