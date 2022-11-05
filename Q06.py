def soma_args_kwargs(*args):
    print(*args, sep='+', end=' ')
    print('=', end=' ')
    soma = args[0] + args[1] + args[2] + args[3] + args[4] + args[5] + args[6] + args[7] + args[8] + args[9]
    print(soma,end=' ')
    
soma_args_kwargs(1,1,1,1,1,1,1,1,1,1)   
    