from models.dispositivo import DispositivoDB

def calcular_consumo(eletrodomesticos: list[DispositivoDB]):
    consumo_diario_total = sum(
        d.consumo * d.uso_diario for d in eletrodomesticos
    )
    consumo_mensal_total = consumo_diario_total * 30
    consumo_anual_total = consumo_diario_total * 365

    return consumo_diario_total, consumo_mensal_total, consumo_anual_total
