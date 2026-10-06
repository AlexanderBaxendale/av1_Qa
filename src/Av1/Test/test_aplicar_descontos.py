import pytest

from src.Av1.Sistema_descontos.aplicarDescontos import calcular_desconto


@pytest.mark.parametrize(
    ("valor_compra", "tipo_cliente", "esperado"),
    [
        (99.99, "COMUM", 0.00),
        (99.99, "VIP", 5.00),
        (100, "COMUM", 10.00),
        (100, "VIP", 15.00),
        (100, "vip", 15.00),
        (499.99, "COMUM", 50.00),
        (500, "COMUM", 100.00),
        (500, "VIP", 125.00),
        (1000, "VIP", 250.00),
    ],
    ids=[
        "abaixo_minimo_comum",
        "abaixo_minimo_vip",
        "limite_100_comum",
        "limite_100_vip",
        "vip_minusculo",
        "abaixo_500_comum",
        "limite_500_comum",
        "limite_500_vip",
        "vip_sem_teto_de_200",
    ],
)
def test_calcular_desconto(valor_compra, tipo_cliente, esperado):
    assert calcular_desconto(valor_compra, tipo_cliente) == esperado
