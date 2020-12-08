from importer import Importer
import json


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, file_name):
        if file_name.endswith('.json'):
            with open(file_name) as file:
                prod_list = json.load(file)
                return prod_list

        else:
            raise ValueError("Arquivo inválido")
