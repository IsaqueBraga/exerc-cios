def soma_lista(list: list) -> int:
    """Recebe uma lista de inteiros e retorna a soma dos elementos."""
    if len(list) == 1:
        return list[0]

    return list[0] + soma_lista(list[1:])