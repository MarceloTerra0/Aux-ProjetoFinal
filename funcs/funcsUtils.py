def criarIntervaloDate(data):
    #Espera-se uma data 'yyyy-MM'
    dataInicio = data.split('-')
    dataFinal = dataInicio.copy()
    dataFinal[1] = f'0{int(dataInicio[1]) + 1}' if int(dataInicio[1]) + 1 < 10 else f'{int(dataInicio[1]) + 1}'
    if int(dataFinal[1]) > 12:
        dataFinal[0] = int(dataFinal[0]) + 1
        dataFinal[1] = '01'
    return (f'{dataInicio[0]}-{dataInicio[1]}-01', f'{dataFinal[0]}-{dataFinal[1]}-01')
