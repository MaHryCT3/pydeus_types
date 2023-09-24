from datetime import datetime
from pathlib import Path

from json import dumps, load
from datamodel_code_generator import load_yaml, DataModelType, PythonVersion
from datamodel_code_generator.model import get_data_model_types
from datamodel_code_generator.parser.jsonschema import JsonSchemaParser
from script.builders import ModeusSchemaBuilder


class ModeusJsonToModel:
    TARGET_PYTHON = PythonVersion.PY_39
    PARSER_CLASS: JsonSchemaParser = JsonSchemaParser
    DATA_MODEL_TYPE = get_data_model_types(
        DataModelType.PydanticV2BaseModel,
        TARGET_PYTHON,
    )
    TYPES_DIR: str = 'pydeus_types'

    def __init__(self, path_where_json: Path,  model_name: str | None = None):
        self.path_where_json = path_where_json
        self.model_name = model_name or path_where_json.stem.capitalize()

    def parse(self) -> None:
        with open(self.path_where_json, 'r', encoding='utf-8') as f:
            json = load(f)
        schema = self.get_schema(json)
        pydantic_models_text = self.schema_to_pydantic_v2(schema)
        model_path = self.get_model_path()
        self.create_model_file(model_path, pydantic_models_text)

    def get_schema(self, json: dict) -> dict:
        schema = self.json_to_schema(dumps(json))
        return self._reduce_emdeded(schema)

    def json_to_schema(self, raw_json: str) -> dict:
        obj = load_yaml(raw_json)
        builder = ModeusSchemaBuilder()
        builder.add_object(obj)
        return builder.to_schema()
    
    def schema_to_pydantic_v2(self, schema: dict) -> str:
        parser = self.PARSER_CLASS(
            dumps(schema),
            data_model_type=self.DATA_MODEL_TYPE.data_model,
            data_model_root_type=self.DATA_MODEL_TYPE.root_model,
            data_model_field_type=self.DATA_MODEL_TYPE.field_model,
            data_type_manager_type=self.DATA_MODEL_TYPE.data_type_manager,
            dump_resolve_reference_action=self.DATA_MODEL_TYPE.dump_resolve_reference_action,
            target_python_version=self.TARGET_PYTHON,
            snake_case_field=True,
        )
        return parser.parse()

    def get_model_path(self):
        string_path = str(self.path_where_json)
        replaced_json_to_py = string_path.replace('.json', '.py')
        replaced_parent_dir = replaced_json_to_py.replace(str(self.path_where_json.parent), self.TYPES_DIR)
        return Path(replaced_parent_dir)

    def create_model_file(self, model_path: Path | str, pydantic_models_text: str):
        pydantic_models_text = self._model_header() + pydantic_models_text
        with open(model_path, 'wt', encoding='utf-8') as file:
            file.write(pydantic_models_text.rstrip())

    def _reduce_emdeded(self, schema: dict):
        """Убирает поле embeded, и перенесет всю информацию в прошлое properties"""
        try:
            if embedded_data := schema['properties']['_embedded']:
                schema['type'] = embedded_data['type']
                schema['properties'] = embedded_data['properties']
        except KeyError:
            pass
        return schema

    def _model_header(self) -> str:
        return f"""#  Схема для модели {self.model_name}
#  Сгенерирована {datetime.now().strftime('%d.%m.%Y %H:%M:%S')}

"""
