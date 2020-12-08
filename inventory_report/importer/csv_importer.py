from importer import Importer
import csv


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, file_name):
        if file_name.endswith('.csv'):
            prod_list = []
            with open(file_name) as file:
                prod_csv = csv.DictReader(file, delimiter=",", quotechar='"')
                for elem in prod_csv:
                    prod_list.append(elem)
            return prod_list

        else:
            raise ValueError("Arquivo inválido")
