from abc import ABC, abstractmethod


class DefinitionProvider(ABC):
    @abstractmethod
    def get_definiton(self):
        pass

    @abstractmethod
    def check_answer(self, user_answer, correct_answer):
        pass
