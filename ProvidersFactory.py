from providers.DataProviderX import DataProviderX
from providers.DataProviderY import DataProviderY


class ProvidersFactory:
    @staticmethod
    def create(provider_name):
        file_name = provider_name.split(".")[0]
        try:
            obj = eval(file_name + "()")
            return obj
        except NameError:
            raise Exception("Provider not implemented")
