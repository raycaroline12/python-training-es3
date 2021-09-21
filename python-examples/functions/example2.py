'''O	 código	 da	 função	 abaixo	 recebe	 uma	 idade	 como	 parâmetro	 e	 faz	 uma	 verificação	 com	 uma
instrução	if:	se	a	idade	for	diferente	de	None	ela	vai	imprimir	a	idade,	caso	contrário	vai	imprimir	idade
não	informada.'''

def retorna_idade(nome, idade=None):
    print('nome: {}'.format(nome))
    if(idade is not None):
        print('idade: {}'.format(idade))
    else:
        print('idade: não informada')


retorna_idade('José')
retorna_idade('José', 45)