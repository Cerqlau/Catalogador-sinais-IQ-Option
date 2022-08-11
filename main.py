import colorama
from iqoptionapi.stable_api import IQ_Option
from datetime import datetime, timedelta
from colorama import Fore,Back
from dateutil import tz
import ast, configparser,getpass,os,sys,json,time,logging

colorama.init(autoreset=True) # Garante reinício de cor no próximo comando print
logging.disable(level=(logging.DEBUG)) #Desabilita logs de erro para execução via arquivo.exe

datet = '2022-10-01'

ExpirationDate = time.strftime("%Y-%m-%d")
if ExpirationDate > datet:
    print(Fore.YELLOW + '\n   RENOVE A LICENÇA - TEMPO DE TESTE ACABOU!\n\n' + Fore.RESET)
    print(Fore.YELLOW + '\n   ENTRE EM CONTATO COM LAURO BOTS\n\n' + Fore.RESET)
    time.sleep(10)
    sys.exit()
elif ExpirationDate == datet:
    print(Fore.YELLOW + '\n   LICENÇA EXPIRA HOJE!\n\n' +Fore.RESET)

#==============================================#
#Função para apresentação de banner            #
#==============================================#
def banner():
	os.system('cls' if os.name == 'nt' else 'clear')
	print ("")
	print ("")
	print (f"{Fore.GREEN}██╗     █████╗██╗   ██╗██████╗ ███████╗")
	print (f"{Fore.GREEN}██║   ██╔══██╗██║   ██║██╔══██╗██╔══██║")
	print (f"{Fore.GREEN}██║   ███████║██║   ██║██████╔╝██║  ██║")
	print (f"{Fore.GREEN}██╚══╗██╔══██║██║   ██║██╔══██╗██║  ██║")
	print (f"{Fore.GREEN}█████║██║  ██║████████║██║  ██║███████║")
	print (f"{Fore.GREEN}╚════╝╚═╝  ╚═╝╚═══════╝╚═╝  ╚═╝╚══════╝")
	print (f"{Fore.GREEN}██████╗ ███████╗████████╗███████╗")
	print (f"{Fore.GREEN}██╔══██╗██╔══██║╚══██╔══╝██╔════╝")
	print (f"{Fore.GREEN}██████╔╝██║  ██║   ██║   ███████╗")
	print (f"{Fore.GREEN}██╔══██╗██║  ██║   ██║   ╚════██║")
	print (f"{Fore.GREEN}██████╔╝███████║   ██║   ███████║")
	print (f"{Fore.GREEN}╚═════╝ ╚══════╝   ╚═╝   ╚══════╝v0.4")
	print (f"{Fore.GREEN}=======================================")
	print (f"{Fore.LIGHTRED_EX}Written by @laurocerqueira")
	print ("")
	print (f"{Fore.LIGHTBLUE_EX}Este Bot tem como objetivo catalogar direção de velas")
	print (f"{Fore.LIGHTBLUE_EX}a partir de dias anteriores #vamosdominaromercado")
	print (f"{Fore.LIGHTBLUE_EX}este BOT é FREE se você comprou DENUNCIE")
	print ("")
	print(f"{Fore.RESET}")
#==============================================#
#Função para verifcação de login               #
#==============================================#
def verificar_se_fez_a_conexao(_iq: IQ_Option, _account_type: str = 'PRACTICE') -> bool:
    check, reason = _iq.connect()
    error_password = """{"code":"invalid_credentials","message":"Cara estou falando que pode confiar. Verifica seu email e senha e tenta na próxima vacilão."}"""
    requests_limit_exceeded = """{"code":"requests_limit_exceeded","message":"Ai não sei o que ta rolando mas estamos enfrentando problemas técnicos. Tente denovo mais tarde disse a atendente de telemarketing aki ao lado.","ttl":600}"""
    if check:
        print('\nLogin efetuado com sucesso')
        _iq.change_balance(_account_type)
        return True
    else:
        if reason == "[Errno -2] Name or service not known":
            print("No Network")
        elif reason == error_password:
            error_message = ast.literal_eval(error_password)
            print(error_message['message'])
        elif reason == requests_limit_exceeded:
            error_message = ast.literal_eval(requests_limit_exceeded)
            print(error_message['message'])

    print("Ai deu um erro muito sininistro aqui, entra em contato com os caras da IQ e verifica se não estão te hackeando.")
    return False

#==============================================#
#Função para animação de loading               #
#==============================================#
def format_currency_value(_currency_account: str, _value: float) -> str:
    return '$ {:,.2f}'.format(_value) if _currency_account == 'USD' else 'R$ {:,.2f}'.format(_value)
#==============================================#
#Função para animação de loading               #
#==============================================#
def get_color_candle(_candle: dict) -> str:
    return 'G' if _candle['open'] < _candle['close'] else 'R' if _candle['open'] > _candle['close'] else 'D'
#==============================================#
#Função para animação de loading               #
#==============================================#
def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    # Print New Line on Complete
    if iteration == total:
        print()
#==============================================#
#Função para captura do Perfil do usuário      #
#==============================================#
def perfil():
  perfil = json.loads(json.dumps(iq.get_profile_ansyc()))

  return perfil

  '''
		name
		first_name
		last_name
		email
		city
		nickname
		currency
		currency_char
		address
		created
		postal_index
		gender
		birthdate
		balance
	'''
#==============================================#
#Função para conversão de timestamp em timezone#
#==============================================#
def timestamp_converter(x): # Função para converter timestamp
	hora = datetime.strptime(datetime.utcfromtimestamp(x).strftime('%Y-%m-%d %H:%M:%S'), '%Y-%m-%d %H:%M:%S') # formatação da hora
	hora = hora.replace(tzinfo=tz.gettz('GMT')) # timezone

	return str(hora)[:-6] #indicar a região da timezone

#==============================================#
#Função para catalogação repetição de velas    #
#==============================================#

def cataloga(par, dias, prct_call, prct_put, timeframe):
	data = []
	datas_testadas = []
	time_ = time.time()
	sair = False
	while sair == False:
		velas = iq.get_candles(par, (timeframe * 60), 1000, time_)
		velas.reverse()

		for x in velas:
			if datetime.fromtimestamp(x['from']).strftime('%Y-%m-%d') not in datas_testadas:
				datas_testadas.append(datetime.fromtimestamp(x['from']).strftime('%Y-%m-%d'))

			if len(datas_testadas) <= dias:
				x.update({'cor': 'verde' if x['open'] < x['close'] else 'vermelha' if x['open'] > x['close'] else 'doji'})
				data.append(x)
			else:
				sair = True
				break

		time_ = int(velas[-1]['from'] - 1)

	analise = {}
	for velas in data:
		horario = datetime.fromtimestamp(velas['from']).strftime('%H:%M')
		if horario not in analise : analise.update({horario: {'verde': 0, 'vermelha': 0, 'doji': 0, '%': 0, 'dir': ''}})
		analise[horario][velas['cor']] += 1

		try:
			analise[horario]['%'] = round(100 * (analise[horario]['verde'] / (analise[horario]['verde'] + analise[horario]['vermelha'] + analise[horario]['doji'])))
		except:
			pass

	for horario in analise:
		if analise[horario]['%'] > 50 : analise[horario]['dir'] = 'CALL'
		if analise[horario]['%'] < 50 : analise[horario]['%'],analise[horario]['dir'] = 100 - analise[horario]['%'],'PUT '

	return analise



#==================================================#
#Função configuração de utilização de arquivo txt  #
#==================================================#
def configuracao():
	arquivo = configparser.RawConfigParser()
	thisfolder = os.path.dirname(os.path.abspath(__file__))
	initfile = os.path.join(thisfolder, 'config.txt')
	arquivo.read(initfile)

	return {'parescolha':arquivo.get('GERAL','parescolha'),
	'conta': arquivo.get('CONTA', 'conta'),
	'payout': 0,
	'banca_inicial': 0,  
	'email': arquivo.get('CONTA', 'email'), 
	'senha': arquivo.get('CONTA', 'senha'), 
	'timeframe':arquivo.get('GERAL','timeframe'),
	'dias': arquivo.get('GERAL','dias'), 
	'porcentagem':arquivo.get('GERAL','porcentagem'), 
	'martingaleqtd':arquivo.get('GERAL','martingaleqtd'), 
	'tipoanalise':arquivo.get('GERAL','tipoanalise')}

#==============================================#
#Organização das chamadas principais           #
#==============================================#
banner()
config=configuracao()
login = config['email']
password = config['senha']
account_type = config['conta']

#login na conta da IQ através da API
iq = IQ_Option(login, password) # Variável responsável por ficar com os dados da IQ
if not verificar_se_fez_a_conexao(iq, account_type):
    sys.exit(0)

#Chamada do perfil do usuário
dados=perfil()   # a variável dados recebe todas as informações da função perfil
print("")

# Definição de variáveis para animação
items = list(range(0, 57))
l = len(items)

# Chamada para animação início em 0%
printProgressBar(0, l, prefix = 'Download de dados:', suffix = 'Complete', length = 50)
for i, item in enumerate(items):
    # Do stuff...
    time.sleep(0.1)
    # Update Progress Bar
    printProgressBar(i + 1, l, prefix = 'Download de dados:', suffix = 'Complete', length = 50)

#Impressão de dados do usuário
print('\n#:===============================================================:#')
print(f"Esta é sua versão da API {IQ_Option.__version__}")
print('#:===============================================================:#')
print(f"Bem vindo: {dados['name']}")
#print(f"Apelido: {dados['nickname']}")
print(f"Cidade: {dados['city']}")
print(f"Endereço: {dados['address']}")
#print(f"Data de criação da conta: {timestamp_converter(dados['created'])}")
account_balance = '$ {:,.2f}'.format(iq.get_balance()) if iq.get_currency() == 'USD' else 'R$ {:,.2f}'.format(iq.get_balance())
print(f"{'Saldo da conta de Treinamento' if iq.get_balance_mode() == 'PRACTICE' else 'Saldo da conta REAL'}: {account_balance}")
print('#:===============================================================:#')

# Inicio das chamadas para catalogação de velas
#print('\nQual timeframe deseja analisar?: ', end='')
timeframe = int(config['timeframe'])
print('Timeframe a ser analizado em minutos: ',timeframe)
#x=get_kind_of_acount()
x= str(config['tipoanalise'])
print('Tipo de opcao analisada: ',x)
#print('\nQuantos dias deseja analisar?: ', end='')

dias = int(config['dias'])
print('Qauntidade de dias a ser analisada: ',dias)
#print('\nPorcentagem minima?: ', end='')
porcentagem = int(config['porcentagem'])
print('Porcentagem minima de acertos: ',porcentagem)
#print('\nQuantos Martingales?: ', end='')
martingale = int(config['martingaleqtd'])
print('Quantidade de martingale analisadas: ',martingale)
parescolha=str(config['parescolha'])
print('Par escolhido: ', parescolha)


print("\nDeixa comigo vou iniciar o processo....Pressione enter para continuar")
input()
prct_call = abs(porcentagem)
prct_put = abs(100 - porcentagem)
P = iq.get_all_open_time()

print('\n')


# Chamada para animação início em 0%
printProgressBar(0, l, prefix = 'Coletando dados do servidor:', suffix = 'Complete', length = 50)
for i, item in enumerate(items):
    # Do stuff...
    time.sleep(0.1)
    # Update Progress Bar
    printProgressBar(i + 1, l, prefix = 'Coletando dados do servidor:', suffix = 'Complete', length = 50)
print('\n\n')

#Laço para impressão das velas catalogadas com formatação
catalogacao = {}
entrou = False
if parescolha == 'AUTO':
	for par in P[x]:
		if P[x][par]['open'] == True:
			timer = int(time.time())
			print(Fore.GREEN + '*' + Fore.RESET + ' CATALOGANDO - ' + par + '.. ', end='')
			entrou = True
			catalogacao.update({par: cataloga(par, dias, prct_call, prct_put, timeframe)})

			for par in catalogacao:
				for horario in sorted(catalogacao[par]):
					if martingale != '':

						mg_time = horario
						soma = {'verde': catalogacao[par][horario]['verde'], 'vermelha': catalogacao[par][horario]['vermelha'], 'doji': catalogacao[par][horario]['doji']}

						for i in range(int(martingale)):

							catalogacao[par][horario].update({'mg'+str(i+1): {'verde': 0, 'vermelha': 0, 'doji': 0, '%': 0} })

							mg_time = str(datetime.strptime((datetime.now()).strftime('%Y-%m-%d ') + str(mg_time), '%Y-%m-%d %H:%M') + timedelta(minutes=timeframe))[11:-3]

							if mg_time in catalogacao[par]:
								catalogacao[par][horario]['mg'+str(i+1)]['verde'] += catalogacao[par][mg_time]['verde'] + soma['verde']
								catalogacao[par][horario]['mg'+str(i+1)]['vermelha'] += catalogacao[par][mg_time]['vermelha'] + soma['vermelha']
								catalogacao[par][horario]['mg'+str(i+1)]['doji'] += catalogacao[par][mg_time]['doji'] + soma['doji']

								catalogacao[par][horario]['mg'+str(i+1)]['%'] = round(100 * (catalogacao[par][horario]['mg'+str(i+1)]['verde' if catalogacao[par][horario]['dir'] == 'CALL' else 'vermelha'] / (catalogacao[par][horario]['mg'+str(i+1)]['verde'] + catalogacao[par][horario]['mg'+str(i+1)]['vermelha'] + catalogacao[par][horario]['mg'+str(i+1)]['doji']) ) )

								soma['verde'] += catalogacao[par][mg_time]['verde']
								soma['vermelha'] += catalogacao[par][mg_time]['vermelha']
								soma['doji'] += catalogacao[par][mg_time]['doji']
							else:
								catalogacao[par][horario]['mg'+str(i+1)]['%'] = 'N/A'

			print('finalizado em ' + str(int(time.time()) - timer) + ' segundos')

	print('\n')

	for par in catalogacao:
		for horario in sorted(catalogacao[par]):
			ok = False

			if catalogacao[par][horario]['%'] >= porcentagem:
				ok = True
			else:
				for i in range(int(martingale)):
					if catalogacao[par][horario]['mg'+str(i+1)]['%'] >= porcentagem:
						ok = True
						break

			if ok == True:

				msg = Fore.GREEN + par + Fore.RESET + ' - ' + horario + ' - ' + (Fore.RED if catalogacao[par][horario]['dir'] == 'PUT ' else Fore.BLUE) + catalogacao[par][horario]['dir'] + Fore.RESET + ' - ' + str(catalogacao[par][horario]['%']) + '% - ' + Back.BLUE + Fore.BLACK + str(catalogacao[par][horario]['verde']) + Back.RED + Fore.BLACK + str(catalogacao[par][horario]['vermelha']) + Back.RESET + Fore.RESET + str(catalogacao[par][horario]['doji'])

				if martingale != '':
					for i in range(int(martingale)):
						if str(catalogacao[par][horario]['mg'+str(i+1)]['%']) != 'N/A':
							msg += ' | MG ' + str(i+1) + ' - ' + str(catalogacao[par][horario]['mg'+str(i+1)]['%']) + '% - ' + Back.BLUE + Fore.BLACK + str(catalogacao[par][horario]['mg'+str(i+1)]['verde']) + Back.RED + Fore.BLACK + str(catalogacao[par][horario]['mg'+str(i+1)]['vermelha']) + Back.RESET + Fore.RESET + str(catalogacao[par][horario]['mg'+str(i+1)]['doji'])
						else:
							msg += ' | MG ' + str(i+1) + ' - N/A - N/A'

				msg2 = 'M'+str(timeframe)+';'+ par +';' + horario + ';'+ catalogacao[par][horario]['dir']+';'+' - ' + str(catalogacao[par][horario]['%']) + '% - '

				if martingale != '':
					for i in range(int(martingale)):
						if str(catalogacao[par][horario]['mg'+str(i+1)]['%']) != 'N/A':
							msg2 += ' ; MG ' + str(i+1) + ' - ' + str(catalogacao[par][horario]['mg'+str(i+1)]['%']) + '%  '
						else:
							msg2 += ' ; MG ' + str(i+1) + ' ; N/A - N/A'


				print(msg)
				open('sinais_' + str((datetime.now()).strftime('%Y-%m-%d')) + '_' + str(timeframe) + 'M.csv','a').write('M'+str(timeframe)+';'+par + ';' + horario + ';' + catalogacao[par][horario]['dir'].strip() + '\n')
				open('sinais_completos_' + str((datetime.now()).strftime('%Y-%m-%d')) + '_' + str(timeframe) + 'M.csv','a').write(msg2.strip() + '\n')
else:
    for par in P[x]:
        if P[x][par]['open'] == True:
            if par == parescolha:
                timer = int(time.time())
                print(Fore.GREEN + '*' + Fore.RESET + ' CATALOGANDO - ' + par + '.. ', end='')
                catalogacao.update({par: cataloga(par, dias, prct_call, prct_put, timeframe)})
                entrou = True
                for par in catalogacao:
                    for horario in sorted(catalogacao[par]):
                        if martingale != '':
                            mg_time = horario
                            soma = {'verde': catalogacao[par][horario]['verde'], 'vermelha': catalogacao[par][horario]['vermelha'], 'doji': catalogacao[par][horario]['doji']}
                            for i in range(int(martingale)):
                                catalogacao[par][horario].update({'mg'+str(i+1): {'verde': 0, 'vermelha': 0, 'doji': 0, '%': 0} })
                                mg_time = str(datetime.strptime((datetime.now()).strftime('%Y-%m-%d ') + str(mg_time), '%Y-%m-%d %H:%M') + timedelta(minutes=timeframe))[11:-3]
                                if mg_time in catalogacao[par]:
                                    catalogacao[par][horario]['mg'+str(i+1)]['verde'] += catalogacao[par][mg_time]['verde'] + soma['verde']
                                    catalogacao[par][horario]['mg'+str(i+1)]['vermelha'] += catalogacao[par][mg_time]['vermelha'] + soma['vermelha']
                                    catalogacao[par][horario]['mg'+str(i+1)]['doji'] += catalogacao[par][mg_time]['doji'] + soma['doji']
                                    catalogacao[par][horario]['mg'+str(i+1)]['%'] = round(100 * (catalogacao[par][horario]['mg'+str(i+1)]['verde' if catalogacao[par][horario]['dir'] == 'CALL' else 'vermelha'] / (catalogacao[par][horario]['mg'+str(i+1)]['verde'] + catalogacao[par][horario]['mg'+str(i+1)]['vermelha'] + catalogacao[par][horario]['mg'+str(i+1)]['doji']) ) )
                                    soma['verde'] += catalogacao[par][mg_time]['verde']
                                    soma['vermelha'] += catalogacao[par][mg_time]['vermelha']
                                    soma['doji'] += catalogacao[par][mg_time]['doji']
                                else:
                                    catalogacao[par][horario]['mg'+str(i+1)]['%'] = 'N/A'
                                    print('finalizado em ' + str(int(time.time()) - timer) + ' segundos')
if entrou == False:
    print(f'Pariadade {parescolha} se encontra fechado no momento, escolha outro par')
    sys.exit()	



print('\n')

for par in catalogacao:
	for horario in sorted(catalogacao[par]):
		ok = False

		if catalogacao[par][horario]['%'] >= porcentagem:
			ok = True
		else:
			for i in range(int(martingale)):
				if catalogacao[par][horario]['mg'+str(i+1)]['%'] >= porcentagem:
					ok = True
					break

		if ok == True:

			msg = Fore.GREEN + par + Fore.RESET + ' - ' + horario + ' - ' + (Fore.RED if catalogacao[par][horario]['dir'] == 'PUT ' else Fore.BLUE) + catalogacao[par][horario]['dir'] + Fore.RESET + ' - ' + str(catalogacao[par][horario]['%']) + '% - ' + Back.BLUE + Fore.BLACK + str(catalogacao[par][horario]['verde']) + Back.RED + Fore.BLACK + str(catalogacao[par][horario]['vermelha']) + Back.RESET + Fore.RESET + str(catalogacao[par][horario]['doji'])

			if martingale != '':
				for i in range(int(martingale)):
					if str(catalogacao[par][horario]['mg'+str(i+1)]['%']) != 'N/A':
						msg += ' | MG ' + str(i+1) + ' - ' + str(catalogacao[par][horario]['mg'+str(i+1)]['%']) + '% - ' + Back.BLUE + Fore.BLACK + str(catalogacao[par][horario]['mg'+str(i+1)]['verde']) + Back.RED + Fore.BLACK + str(catalogacao[par][horario]['mg'+str(i+1)]['vermelha']) + Back.RESET + Fore.RESET + str(catalogacao[par][horario]['mg'+str(i+1)]['doji'])
					else:
						msg += ' | MG ' + str(i+1) + ' - N/A - N/A'

			msg2 = 'M'+str(timeframe)+';'+ par +';' + horario + ';'+ catalogacao[par][horario]['dir']+';'+' - ' + str(catalogacao[par][horario]['%']) + '% - '

			if martingale != '':
				for i in range(int(martingale)):
					if str(catalogacao[par][horario]['mg'+str(i+1)]['%']) != 'N/A':
						msg2 += ' ; MG ' + str(i+1) + ' - ' + str(catalogacao[par][horario]['mg'+str(i+1)]['%']) + '%  '
					else:
						msg2 += ' ; MG ' + str(i+1) + ' ; N/A - N/A'


			print(msg)
			open('sinais_' + str((datetime.now()).strftime('%Y-%m-%d')) + '_'+ str(parescolha)+ '_' + str(timeframe) + 'M.csv', 'a').write('M'+str(timeframe)+';'+par + ';' + horario + ';' + catalogacao[par][horario]['dir'].strip() + '\n')
			open('sinais_completos_' + str((datetime.now()).strftime('%Y-%m-%d')) +'_'+ str(parescolha)+ '_' + str(timeframe) + 'M.csv', 'a').write(msg2.strip() + '\n')


print('\nTerminei a tarefa, estou deixando a lista de sinais para você na pasta onde me encontro, confere lá!!!')

# Saída do programa
input('\nPressione enter para deixar o programa')
exit()
