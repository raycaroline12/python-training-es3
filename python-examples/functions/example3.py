'''Exemplo semelhante ao example1.py, utilizando um return em vez de um print.'''

def retorna_idade(nome,	idade=None):
    if(idade is not None):
        return ('nome:	{}	\nidade:	{}'.format(nome,	idade))
    else:
        return ('nome:	{}	\nidade:	não	informada'.format(nome))

print(retorna_idade('José'))
print(retorna_idade('José', 45))

