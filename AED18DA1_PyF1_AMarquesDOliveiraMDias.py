"""
                SIMPAR
Simulação de Passageiros em Partida Aérea

"""
#Imports
from pythonds.basic import Queue
import random
import names

#Main Classes
class Passageiro:
    def __init__(self, bag_pass, ciclo_in):
        self.bag_pass=bag_pass
        self.ciclo_in=ciclo_in
        
    def obtem_bag_pass(self):
        return self.bag_pass
    
    def obtem_ciclo_in(self):
        return self.ciclo_in
    
    def __str__(self):
        return 'Passageiro com {} bagagens no ciclo {} da simulação.'.format(str(self.obtem_bag_pass()), str(self.obtem_ciclo_in()))
    
class Balcao:
    def __init__(self, n_balcao, fila, inic_atend, passt_atend, numt_bag, tempt_esp, bag_utemp):
        super().__init__()
        self.n_balcao=n_balcao
        self.fila=fila
        self.inic_atend=inic_atend
        self.passt_atend=passt_atend
        self.numt_bag=numt_bag
        self.tempt_esp=tempt_esp
        self.bag_utemp=bag_utemp

    def muda_inic_atend(self, ciclos):
        self.inic_atend = ciclos
        return self.inic_atend
        
    def incr_passt_atend(self):
        self.passt_atend = self.passt_atend + 1
        return(self.passt_atend)
        
    def muda_numt_bag(self, bag_pass):
        self.numt_bag=self.numt_bag + bag_pass
        return self.numt_bag
    
    def muda_tempt_esp(self, tempo_de_espera):
        self.tempt_esp=self.tempt_esp + tempo_de_espera
        return self.tempt_esp
    
    def media_bag_pass(self):
        media=self.numt_bag//self.passt_atend
        return media
        
    def temp_med_esp(self):
        media=self.tempt_esp//self.passt_atend
        return media
    
    def obtem_nome(self):
        return self.__class__.__name__
    
    def obtem_n_balcao(self):
        return self.n_balcao
    
    def obtem_fila(self):
        return self.fila
    
    def obtem_inic_atend(self):
        return self.inic_atend
    
    def obtem_passt_atend(self):
        return self.passt_atend
    
    def obtem_numt_bag(self):
        return self.numt_bag
    
    def obtem_tempt_esp(self):
        return self.tempt_esp
    
    def obtem_bag_utemp(self):
        return self.bag_utemp
    
    def __str__(self):
        str_pass = "" #Definição da variável str_pass com string
        for b in range(0, len(self.fila.items), 1):
            str_pass = str_pass + str(self.fila.items[b]) + '\n'
        return self.__class__.__name__ + ' : ' + str(self.obtem_n_balcao()) + ' - Tempo: ' + str(self.obtem_inic_atend()) + '\n' + 'A fila no balcão ' + str(self.obtem_n_balcao()) + ' tem ' + str(self.fila.size()) + ' passageiros. \n - Passageiros na fila de espera: \n' + str_pass

# Implementação de uma BST
global node
class Node(object):
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        
# Imprime segundo o padrão InOrder
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data)
        if self.right:
            self.right.PrintTree()

class BinarySearchTree(object):
    def __init__(self, root=None):
        self.root = root

    # Devolve a raiz
    def get_root(self):
        return self.root

    # Função que insere nós na árvore
    def iterative_insert(self, item):
        if self.root is None:
            self.root = Node(item)
        else:
            nd = self.root
            while nd is not None:
                if item < nd.data:
                    if nd.left is None:
                        nd.left = Node(item)
                        return
                    else:
                        nd = nd.left
                else:
                    if nd.right is None:
                        nd.right = Node(item)
                        return
                    else:
                        nd = nd.right
    # Pesquisa de um elemento na árvore
    def iterative_search(self, item):
        if self.root is None:
            return 'O passageiro não está presente.'
        else:
            nd = self.root
            while nd is not None:
                if nd.data == item:
                    return 'O passageiro está presente.'
                elif nd.data < item:
                    nd = nd.right
                else:
                    nd = nd.left
            return 'O passageiro não está presente.'

        
#####################################################################################################################################################################
# Aquisição de Variáveis - Com introdução das mesma pelo utilizador
if __name__ == '__main__':
    
    #Definição de funções
    #Função que cria os balcões com base no número desejado
    def cria_balcoes(num_balcoes):
        global balcoes #Definição de variáveis globais para serem usadas noutras funções
        balcoes=[]
        for i in range(0, num_balcoes, 1):
            balcao=Balcao(i, Queue(), 1, 0, 0, 0, random.randrange(1, num_bag))
#            print('Balcão gerado: {}'.format(balcao)) - Print de Debugging
            balcoes.append(balcao)
            
    #Função que cria os passageiros tendo atenção o número máximo permitido pela atribuição de variáveis.
    #Sendo assim, a função introduz metade dos passageiros que serão previstos nas listas de espera dos balcões.
    #Assim poderão ser criados novos passageiros noutras funções sem que seja ultrapassado o número máximo
    def cria_pass(num_pass):
        global num_pass_div, max_pass #Definição de variáveis globais para serem usadas noutras funções
        num_pass_div = num_pass//2 #Divide-se o número total de passageiros em 2 e introduz-se uma parte dessa divisão nas filas dos balcões
        num_pass_div_balc = num_pass_div // num_balcoes #Número máximo de passageiros divididos em cada balcão existente
        max_pass= num_pass - num_pass_div #Limite máximo possivel de passageiros no voo
        for i in range(0, len(balcoes), 1):
            z=0
            while z < num_pass_div_balc: #Enquanto a fila do balcão tiver um número menor de passageiro em relação a num_pass_div_balc insere um passageiro na fila do balcão
                pass_a=Passageiro(random.randrange(1,num_bag), 0)
                balcoes[i].fila.enqueue(pass_a)
                z = z + 1
    
    def cria_nome(): #Função que cria um nome aleatório com base no módulo names
        nome=names.get_full_name()
        return nome

    #Função que cria uma variável global e que atribui a essa variável a função BST
    def cria_passTree():
        global passTree
        passTree=BinarySearchTree()        

    #Função principal que quando invocada atende os passageiros num ciclo
    def atende_passageiros(ciclos, balcoes): #Tempo = Nº de Ciclo
        global lista_tam, nome_pass #Definição de variáveis globais para serem usadas noutras funções
        for b in range(0, len(balcoes), 1):
            if balcoes[b].fila.isEmpty() is not True: #Verifica se a fila do balcão escolhido não está vazia
                pass_off_bag=balcoes[b].fila.items[-1].obtem_bag_pass() #Espreita e ve as bagagens do ultimo passageiro da fila, retirando e armazenando o valor
                print('Balcão: {}'.format(balcoes[b].obtem_n_balcao())) #Output
                adic_fich('\nBalcão: {}'.format(balcoes[b].obtem_n_balcao())) #Adição de um output ao ficheiro criado na função criar_fich
                print(' O Passageiro que está a ser atendido tem {} bagagens. \n'.format(pass_off_bag)) #Output
                adic_fich('\n O Passageiro que está a ser atendido tem {} bagagens. \n'.format(pass_off_bag)) #Adição de um output ao ficheiro criado na função criar_fich
                tempo_de_atendimento = ciclos - balcoes[b].inic_atend
                utbag= pass_off_bag/balcoes[b].obtem_bag_utemp()
                if utbag < tempo_de_atendimento:
                    pass_off=balcoes[b].fila.dequeue()
                    tempo_de_espera = ciclos - pass_off.obtem_ciclo_in()
                    nome_pass=cria_nome() #Cria um nome para o passageiro atendido
                    passTree.iterative_insert(nome_pass) #Insere o nome do passageiro dentro da árvore
                    print(' Atendido passageiro com {} bagagens no balcão {}.\n'.format(pass_off_bag, b)) #Output
                    adic_fich(' Atendido passageiro com {} bagagens no balcão {}.\n'.format(pass_off_bag, b)) #Adição de um output ao ficheiro criado na função criar_fich
                    #Mudanças nas variáveis do objeto Balcão
                    muda_inic=ciclos + 1
                    balcoes[b].muda_inic_atend(muda_inic)
                    balcoes[b].incr_passt_atend()
                    balcoes[b].muda_numt_bag(pass_off_bag)
                    balcoes[b].obtem_numt_bag()
                    balcoes[b].muda_tempt_esp(tempo_de_espera)
                else:
                    if utbag >= tempo_de_atendimento:
                        print(' Não foi atendido o passageiro neste balcão.\n') #Output
                        adic_fich(' Não foi atendido o passageiro neste balcão.\n') #Adição de um output ao ficheiro criado na função criar_fich
                        if balcoes[b].fila.isEmpty() is True:
                            balcoes[b].muda_inic_atend(ciclos)
            else:
                if balcoes[b].fila.isEmpty() is True:
                    balcoes[b].muda_inic_atend(ciclos)
            
    #Função que permite  verificar o tamanho de um fila de um balcão e se esse for o mais pequeno de todos os balcões 
    #passa o objeto respetivo com a fila  mais pequena para uma variável global
    def ver_fila_peq(balcoes):
        global balc_men #Definição de variáveis globais para serem usadas noutras funções
        lista_tam=[]
        for x in range(0, len(balcoes)):
            lista_tam.append(balcoes[x])
        size=[]
        for i in range(0, len(lista_tam)):
            size.append(lista_tam[i].fila.size())
            mn=min(size) #Verifica qual é o elemento mais pequeno da lista size
        for b in range(0, len(lista_tam)):
            if mn == lista_tam[b].fila.size():
                print(' Este é o balcão que tem menos passageiros: Balcão {}'.format(lista_tam[b].obtem_n_balcao()))
                adic_fich(' \nEste é o balcão que tem menos passageiros: Balcão {}'.format(lista_tam[b].obtem_n_balcao())) #Adição de um output ao ficheiro criado na função criar_fich
                balc_men=lista_tam[b]
        adic_fich('\n')                 

    #Função usada para devolver um true or false com base numa probabildade de um acontecimento
    def decisao(prob):
        return random.random() < prob #Devolve um valor do tipo float aleatório entre 0.0 e 1.0

    #Função que adiciona passageiros durante a parte do ciclo for com base numa divisão dos ciclos em 3 partes
    def adic_pass(i, ciclos):
        global pass_x#Definição de variáveis globais para serem usadas noutras funções
        if i < ciclos * ((1/3)):
            print('--- Chegada de um novo passageiro... ---\n') #Output
            adic_fich('\n--- Chegada de um novo passageiro... ---\n') #Adição de um output ao ficheiro criado na função criar_fich
            pass_x=Passageiro(random.randrange(1,num_bag), i)
#            print('Foi criado um novo passageiro no primeiro terço de ciclos da simulação. \n') - Output de Debugging
            ver_fila_peq(balcoes) #Verifica através da função  ver_fila_peq qual é o balcão que tem a fila mais pequena
            balc_men.fila.enqueue(pass_x) #Adiciona a esse balcão o passageiro criado
            print('\n--- Foi adicionado um passageiro ao balcao: {} ---\n'.format(balc_men.obtem_n_balcao())) #Output
            adic_fich('\n--- Foi adicionado um passageiro ao balcao: {} ---\n'.format(balc_men.obtem_n_balcao())) #Adição de um output ao ficheiro criado na função criar_fich
            return pass_x
        else :
            if i > ciclos * ((1/3)) and i < ciclos * ((2/3)) and decisao(0.8) == True:
                print('--- Chegada de um novo passageiro... ---\n') #Output
                adic_fich('\n--- Chegada de um novo passageiro... ---\n') #Adição de um output ao ficheiro criado na função criar_fich
                pass_x=Passageiro(random.randrange(1,num_bag), i)
#                print('Foi criado um novo passageiro no segundo terço de ciclos da simulação. \n') - Output de Debugging
                ver_fila_peq(balcoes) #Verifica atravéz da função  ver_fila_peq qual é o balcão que tem a fila mais pequena
                balc_men.fila.enqueue(pass_x) #Adiciona a esse balcão o passageiro criado
                print('\n--- Foi adicionado um passageiro ao balcao: {} ---\n'.format(balc_men.obtem_n_balcao())) #Output
                adic_fich('\n--- Foi adicionado um passageiro ao balcao: {} ---\n'.format(balc_men.obtem_n_balcao())) #Adição de um output ao ficheiro criado na função criar_fich
                return pass_x
            else:
                if i > ciclos * ((2/3)) and decisao(0.6) == True:
                    print('--- Chegada de um novo passageiro... ---\n') #Output
                    adic_fich('\n--- Chegada de um novo passageiro... ---\n') #Adição de um output ao ficheiro criado na função criar_fich
                    pass_x=Passageiro((random.randrange(1,num_bag)), i)
#                    print('Foi criado um passageiro no terceiro terço de ciclos da simulação. \n') - Output de Debugging
                    ver_fila_peq(balcoes)#Verifica atravéz da função  ver_fila_peq qual é o balcão que tem a fila mais pequena
                    balc_men.fila.enqueue(pass_x)#Adiciona a esse balcão o passageiro criado
                    print('\n--- Foi adicionado um passageiro ao balcao: {} ---\n'.format(balc_men.obtem_n_balcao())) #Output
                    adic_fich('\n--- Foi adicionado um passageiro ao balcao: {} ---\n'.format(balc_men.obtem_n_balcao())) #Adição de um output ao ficheiro criado na função criar_fich
                    return pass_x
                else:
                    return '--- Não foram criados ou adicionados passageiros aos balcões. ---' #Output
                
    #Função que imprime cada balcão existente na simulação e os respetivos passageiros nas suas filas de espera    
    def mostra_balcoes(balcoes):
        for i in range(0, len(balcoes)): #Loop que percorre todos os balcões
            dado_1=str(balcoes[i]) #Atribuição de uma variável em forma de string para ser usada na escrita de dados para um ficheiro
            print(balcoes[i]) #Primeira parte do print do str
            adic_fich('\n') #Adiciona um parágrafo ao ficheiro
            adic_fich(dado_1) #Adição de um output ao ficheiro criado na função criar_fich
            
    #Função que verifica no inicio de cada  ciclo while da segunda parte da simulação se ainda existem balcões com filas preenchidas
    def existem_balcoes_com_fila(balcoes):
        for i in range(0, len(balcoes)):
            if balcoes[i].fila.size()  > 0:
                return True
    
    #Função usada no final da simulação, fora dos ciclos para apresentar  resultados estatisticos da simulação
    def apresenta_resultados(balcoes):
        global t_atend
        t_atend=0
        for i in range (0, len(balcoes)):
            if balcoes[i].obtem_passt_atend() > 0:
                t_atend= t_atend + balcoes[i].obtem_passt_atend()
                print(' Balcão {} despachou {} bagagens por ciclo: \n  {} passageiros atendidos com média de bagagens / passageiros de: {} \n  Tempo médio de espera = {}\n'.format(i, balcoes[i].obtem_bag_utemp(), balcoes[i].obtem_passt_atend(), balcoes[i].media_bag_pass(), balcoes[i].temp_med_esp())) #Output
                adic_fich('\n Balcão {} despachou {} bagagens por ciclo: \n  {} passageiros atendidos com média de bagagens / passageiros de: {} \n  Tempo médio de espera = {}\n'.format(i, balcoes[i].obtem_bag_utemp(), balcoes[i].obtem_passt_atend(), balcoes[i].media_bag_pass(), balcoes[i].temp_med_esp())) #Adição de um output ao ficheiro criado na função criar_fich
            elif balcoes[i].obtem_passt_atend() == 0:
                    print(' Balcão {} não atendeu passageiros.'.format(i)) #Output
                    adic_fich('\n Balcão {} não atendeu passageiros.'.format(i)) #Adição de um output ao ficheiro criado na função criar_fich
        print('Número total de passageiros atendidos: {}'.format(t_atend))
        adic_fich('\nNúmero total de passageiros atendidos: {}'.format(t_atend))
                    
    #Função que cria um ficheiro onde é armazenada as informações. Ficheiro.txt com o modo 'w'
    def criar_fich():
        fich_a=open('SimOutput.txt','w') #Cria o ficheiro
        fich_a.write('SIMPAR - SIMULAÇÃO DE PARTIDA DE PASSAGEIROS\n') #Escreve no ficheiro
        fich_a.close() #Fecha o ficheiro
        
    #Função que adiciona informação aos ficheiros em modo 'a', permitindo manter a informação previamente guardada   
    def adic_fich(dados): 
        fich_a=open('SimOutput.txt','a') #Abre o ficheiro SimOutput do tipo .txt
        fich_a.write(dados) #Escreve os dados em modo de a, mantewndo a informação previamente existente
        fich_a.close() #Fecha o Ficheiro
        
    #Função que executa as instruções do BST
    def bst():
        print('\nPara efeitos de utilzação do método search do BST, vamos considerar o seguinte:\n')
        print('Este é um passageiro dentro da árvore: {} \n'.format(nome_pass))
        nome=input('Indique o nome do passageiro que pretende encontrar: ')
        res=passTree.iterative_search(nome)
        print('\n--------------------------------')
        print(res)
        print('--------------------------------')
        print('\nEstes são os passageiros que foram atendidos por ordem alfabética: \n')
        passTree.root.PrintTree()
        
    #Função principal do programa que invoca todas as funções definidas anteriormente e executa a simulação
    def simpar_simula(num_pass, num_bag, num_balcoes, ciclos, n_voo):
        cria_balcoes(num_balcoes) #Cria os balcoes e insere numa lista   
        cria_pass(num_pass) #Insere passageiros nas filas de espera dos balcoes antes de começar o ciclo
        cria_passTree() #Cria a árvore BST passTree
        criar_fich() #Cria um ficheiro onde serão adicionados os outputs da simulação
        print('\n--- Abertura dos balcões e inicio do atendimento de passageiros do voo {} ---\n'.format(n_voo)) #Output
        adic_fich('\n--- Abertura dos balcões e inicio do atendimento de passageiros do voo {} ---\n'.format(n_voo)) #Adição de um output ao ficheiro criado na função criar_fich
        #1ºCiclo -  FOR
        x=0
        for i in range(1, ciclos+1):     
            #Output
            print('\n---------------')
            print('Ciclo Número {}'.format(i))
            print('---------------')
            #Adição de um output ao ficheiro criado na função criar_fich
            adic_fich('\n---------------')
            adic_fich('Ciclo Número {}'.format(i))
            adic_fich('---------------\n')
            
            #1ºPasso - Atende um pass
            atende_passageiros(i, balcoes)
            if x < max_pass: #Controlo máximo de passageiros possiveis
                adic_pass(i, ciclos) #2ºPasso - Cria um pass (ou não), e observa qual das filas é mais pequena para inserir
                x=x+1
            mostra_balcoes(balcoes) #Output dos balcões existentes e as suas filas
        #Output        
        print('-------------------------------------')
        print('\nFechou a chegada de novos passageiros!\n')
        print('-------------------------------------\n')
        #Adição de um output ao ficheiro criado na função criar_fich
        adic_fich('\n-------------------------------------')
        adic_fich('\nFechou a chegada de novos passageiros!\n')
        adic_fich('-------------------------------------\n')
        
        ciclos=ciclos + 1
        
        #2ºCiclo -  WHILE    
        while existem_balcoes_com_fila(balcoes) == True: #Enquanto existem balcões com filas preenchidas
            print('---------------')
            print('Ciclo Número {}'.format(ciclos))
            print('---------------')
            #Adição de um output ao ficheiro criado na função criar_fich
            adic_fich('\n---------------')
            adic_fich('Ciclo Número {}'.format(ciclos))
            adic_fich('---------------\n')
            
            atende_passageiros(ciclos, balcoes)#Atende um passageiro na fila

            mostra_balcoes(balcoes) #Output dos balcões existentes e as suas filas
            
            ciclos=ciclos+1
        #Output
        print('Não existem mais passageiros em espera.\n')
        print('--- Fecho dos balcões e conclusão do atendimento de passageiros... ---\n')
        #Adição de um output ao ficheiro criado na função criar_fich
        adic_fich('\n--- Fecho dos balcões e conclusão do atendimento de passageiros... ---\n')
        adic_fich('\nNão existem mais passageiros em espera.\n')

        print('Fechou o check in do voo: {} \n'.format(n_voo))
        adic_fich('\nFechou o check in do voo: {} \n'.format(n_voo))
        print('--- DADOS ESTATISTICOS ---\n') #Output
        adic_fich('\n--- DADOS ESTATISTICOS ---\n') #Adição de um output ao ficheiro criado na função criar_fich
        apresenta_resultados(balcoes) #Função que expoem os dados estatisticos e transfere o output para o ficheiro

#####################################################################################################################################################################
    print("""
                SIMPAR
Simulação de Passageiros em Partida Aérea
""")
    
    #Atribuição de Variáveis
    print('Seja Bem Vindo!')
    n_voo=int(input('\nIntroduza o número de Voo: '))
    print('\nIntroduza os seguintes dados em relação ao voo: {} '.format(n_voo))
    num_pass=int(input('\nIntroduza o número de passageiros previstos para este voo: '))
    num_bag=int(input('\nIntroduza o número máximo de bagagens permitidas por passageiro: '))
    num_balcoes=int(input('\nIntroduza o número de balcoes que serão abertos para efetuar o check-in: '))
    ciclos=int(input('\nIntroduza o número de ciclos que pretende efetuar: '))
    print('\n')

    
#    #Atribuições locais - Debugging
#    num_pass = 70 
#    num_bag = 4
#    num_balcoes = 4
#    ciclos = 10
    
    #Chamada de Funções Principais
    simpar_simula(num_pass, num_bag, num_balcoes, ciclos, n_voo) #Chamada da função que inicia  a simulação
    bst() #Chamada da função BST com instruções de execução sobre a BST

    