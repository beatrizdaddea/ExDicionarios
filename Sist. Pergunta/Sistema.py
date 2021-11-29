""" Sistema de Perguntas e Respostas usando Dicionários"""
perguntas = {
    'Pergunta 1 ': {
        'pergunta': 'Quanto é 23+97 ?',
        'respostas': {'a':'120','b': '32', 'c': '133',},
        'resposta_certa': 'a', 
    },
   
    'Pergunta 2 ': {
        'pergunta': 'Atualmente, quantos elementos químicos a tabela periódica possui?',
        'respostas': {'a':'109','b': '122', 'c': '118',},
        'resposta_certa': 'c', 
    },
     'Pergunta 3 ': {
        'pergunta': 'O que significa trigger em inglês?',
        'respostas': {'a':'perdão','b': 'gatilho', 'c': 'tigre',},
        'resposta_certa': 'b', 
    },
}

resposta_certas = 0

for pk,pv in perguntas.items(): # exibe as perguntas 
    print(f'{pk}: {pv["pergunta"]}')
    
    for rk,rv in pv['respostas'].items():
        print(f'[{rk}]: {rv}')
        
    resposta_usuario= input('Sua resposta: ')
    
    if resposta_usuario ==  pv['resposta_certa']:
        print('Você Acertou!!!!')
        resposta_certas += 1 
    else:
        print('Você Errou :(')
    

qnt_perguntas = len(perguntas)
porcentagem_acerto = float(resposta_certas / qnt_perguntas * 100) 
print(f'Sua porcentagem de acerto foi: {porcentagem_acerto}%. ')