from abc import abstractmethod


class ParserInterface:
    @abstractmethod
    def parse(self, data):
        pass
