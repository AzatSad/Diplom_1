from unittest.mock import patch
from praktikum.bun import Bun
from praktikum.database import Database
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING,INGREDIENT_TYPE_SAUCE


class TestDatabase:

    def test_database_available_buns(self):
        """Проверяет доступность булочки
        """
        mock_bun = [Bun("Флюоресцентная булка R2-D3", 100)]
        database = Database()
        with patch.object(database, 'buns', mock_bun):
            result = database.available_buns()
            assert result == mock_bun


    def test_database_available_fillings_ingredients(self):
        """Проверяет доступность начинок
        """
        mock_ingredient = [Ingredient(INGREDIENT_TYPE_FILLING, "Говяжий метеорит (отбивная)", 200)]
        database = Database()
        with patch.object(database, 'ingredients', mock_ingredient):
            result = database.available_ingredients()
            assert result == mock_ingredient


    def test_database_available_sauce_ingredients(self):
        """Проверяет доступность соусов
        """
        mock_ingredient = [Ingredient(INGREDIENT_TYPE_SAUCE, "Соус традиционный галактический", 150)]
        database = Database()
        with patch.object(database,'ingredients', mock_ingredient):
            result = database.available_ingredients()
            assert result == mock_ingredient
