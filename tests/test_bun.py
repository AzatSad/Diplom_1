import pytest
from praktikum.bun import Bun


class TestBun:

    @pytest.mark.parametrize("name, price", [('Флюоресцентная булка R2-D3', 100), ('Краторная булка N-200i', 200)])
    def test_get_name_bun(self, name, price):
        """Получает название булочки

        Args:
             name: Название булочки
             price: Цена булочки
        """
        bun = Bun(name, price)
        assert bun.get_name() == name

    # Получить цену булочки
    @pytest.mark.parametrize("name, price", [('Флюоресцентная булка R2-D3', 100), ('Краторная булка N-200i', 200)])
    def test_get_price_bun(self, name, price):
        """Получает цену булочки

        Args:
             name: Название булочки
             price: Цена булочки
        """
        bun = Bun(name, price)
        assert bun.get_price() == price
