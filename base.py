from abc import ABC, abstractmethod
from typing import List
from models import Recipe

class BaseRecipeProvider(ABC):
    @abstractmethod
    def get_recipes(self) -> List[Recipe]:
        pass

        