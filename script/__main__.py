from pathlib import Path

from script.modeus_json_parser import ModeusJsonToModel


def main():
    path_to_json = Path('modeus_jsons/test.json')
    parser = ModeusJsonToModel(path_to_json, 'Test')
    parser.parse()


main()