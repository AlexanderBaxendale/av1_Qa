import pytest
from src.Av1.Sistema_descontos.aplicarDescontos import calcular_desconto


@pytest.mark.parametrize(
    "valor_compra, tipo_cliente, esperado",
    [
        # Compras abaixo de R$ 100,00
        (0, "COMUM", 0.00),
        (50, "COMUM", 0.00),
        (50, "VIP", 2.50),
        (99.99, "COMUM", 0.00),

        # Limite de R$ 100,00
        (100, "COMUM", 10.00),
        (100, "VIP", 15.00),

        # Compras entre R$ 100,00 e R$ 500,00
        (200, "COMUM", 20.00),
        (200, "VIP", 30.00),
        (200, "vip", 30.00),
        (200, "Vip", 30.00),
        (499.99, "COMUM", 50.00),

        # Limite de R$ 500,00
        (500, "COMUM", 100.00),
        (500, "VIP", 125.00),

        # Regra do teto de R$ 200,00
        (1000, "COMUM", 200.00),
        (1000, "VIP", 200.00),
        (2000, "COMUM", 200.00),

        # Arredondamento para duas casas decimais
        (123.45, "COMUM", 12.35),
    ],
)
def test_calcular_desconto(valor_compra, tipo_cliente, esperado):
    resultado = calcular_desconto(valor_compra, tipo_cliente)

    assert resultado == pytest.approx(esperado)


def test_valor_compra_negativo():
    with pytest.raises(ValueError):
        calcular_desconto(-10, "COMUM")
