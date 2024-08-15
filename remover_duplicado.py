
def remover_duplicado(param: list) -> list:
    if not isinstance(param, list):
        raise Exception('Valor recebido noo e uma list')

    ret_list = []
    for element in param:
        if isinstance(element, int):
            # print('int')
            if isinstance(element, bool):
                continue
            if element not in ret_list:
                ret_list.append(element)
        elif isinstance(element, str):
            # print('str')
            try:
                element_int = int(element)
            except:
                # string não tem numero
                pass
            else:
                if element_int not in ret_list:
                    ret_list.append(element_int)
        # else:
        #     raise Exception('Tipo do elemento da lista nao e um numero ou string')

    return ret_list
