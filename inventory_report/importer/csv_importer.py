from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    def import_data(cls, filepath):
        if not filepath.endswith('.csv'):
            raise ValueError('Arquivo inválido')
        with open(f"../{filepath}") as csv_file:
            csv_dict = csv.DictReader(csv_file, delimiter=",")
            output = []
            for dict in csv_dict:
                output.append(dict)
        return output
