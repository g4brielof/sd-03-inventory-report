from datetime import datetime


class SimpleReport:
    @classmethod
    def generate(cls, data):
        qty_products_per_company = cls.get_companies_dict(data)
        company_with_more_products = {"name": "", "qty": 0}
        manufacturing_date = cls.get_manufacturing_date(data)
        due_date = cls.get_due_date(data)
        for company in qty_products_per_company.items():
            if company[1] > company_with_more_products["qty"]:
                company_with_more_products["qty"] = company[1]
                company_with_more_products["name"] = company[0]
        company_name = company_with_more_products["name"]
        report = f"""
            Data de fabricação mais antiga: {manufacturing_date}
            Data de validade mais próxima: {due_date}
            Empresa com maior quantidade de produtos estocados: {company_name}
        """
        return report

    @classmethod
    def get_manufacturing_date(cls, data):
        manufacturing_date = datetime.now().strftime("%Y-%m-%d")
        for product in data:
            if datetime.strptime(
                product["data_de_fabricacao"], "%Y-%m-%d"
            ) < datetime.strptime(manufacturing_date, "%Y-%m-%d"):
                manufacturing_date = product["data_de_fabricacao"]
        return manufacturing_date

    @classmethod
    def get_due_date(cls, data):
        due_date = datetime.now().strftime("%Y-%m-%d")
        for product in data:
            if datetime.strptime(
                product["data_de_fabricacao"], "%Y-%m-%d"
            ) > datetime.now() and datetime.strptime(
                product["data_de_fabricacao"], "%Y-%m-%d"
            ) < datetime.strptime(
                due_date, "%Y-%m-%d"
            ):
                due_date = product["data_de_validade"]
        return due_date

    @classmethod
    def get_companies_dict(cls, data):
        qty_products_per_company = {}
        for product in data:
            name = product["nome_da_empresa"]
            if name in qty_products_per_company:
                qty_products_per_company[name] += 1
            if name not in qty_products_per_company:
                qty_products_per_company[name] = 1
        return qty_products_per_company
