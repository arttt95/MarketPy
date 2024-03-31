def formata_float_str_moeda(valor: float) -> str:
    valor = f'R$ {valor:_}'
    valor = valor.replace('.', ',')
    valor = valor.replace('_', '.')
    return valor


def formata_str_float_moeda(valor: str) -> float:
    valor = valor.replace(',', '.')
    return float(valor)
