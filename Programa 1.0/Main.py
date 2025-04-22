import random

from Startup import startup

startups = []
qnt_stuartups = len(startups) - 1
ganhou = ""
next_startup = ""
menu = "main"
competidores = 0
fase_atual = 0
torneio_iniciado = False
fase_final = False
sera_adminstrador = False
is_admin = False
Ja_Administrado = []
derrotados = []

def finalizacao(vencedor):
    placar = [vencedor]
    while len(derrotados) > 0:
        maior_pontuacao = 0
        proximo = ""
        for a,i in enumerate(derrotados):
            if i.pontuacao > maior_pontuacao:
                maior_pontuacao = i.pontuacao
                proximo = i
                derrotados.pop(a)

        placar.append(proximo)
    
    print(f"{vencedor.slogan}")
    colocacao = 0
    for i in placar:
        colocacao += 1
        print(f"{colocacao}) {i.nome}")
    


#Esta função prepara as duplas selecionadas para a batalha, iniciando suas rodadas internas
def iniciador_batalhas():
    for e,i in enumerate(duplas):
        if sera_adminstrador == True:  
            print("Escolha qual batalha administrar ou insira C para continuar: ")
            batalha_escolhida = str(input("Insira o numero da batalha: "))

            if batalha_escolhida == "1":
                if i == dupla1:
                    for unidade in i:
                        unidade.round_start()
                    Ja_Administrado.append(i)
                    #print(Ja_Administrado)
                    duplas.pop(e)
                    
                    for adm_idx in Ja_Administrado:
                        if adm_idx == dupla1:
                            battle_admin(adm_idx[0], adm_idx[1])
            #####################################################
            elif batalha_escolhida == "2":
                print("Aceito")
                if competidores >= 4:
                    print("passou no check")
                    for n,d in enumerate(duplas):
                        if d == dupla2:
                            for unidade in d:
                                print("Achou a unidade")
                                unidade.round_start()
                            Ja_Administrado.append(d)
                            #print(Ja_Administrado)
                            duplas.pop(n)

                            for adm_idx in Ja_Administrado:
                                if adm_idx == dupla2:
                                    print("Entrou no adm")
                                    battle_admin(adm_idx[0], adm_idx[1])
                else:
                    print("invalido")
            #########################################################
            elif batalha_escolhida == "3":
                print("Aceito")
                if competidores >= 6:
                    print("passou no check")
                    for n,d in enumerate(duplas):
                        if d == dupla3:
                            for unidade in d:
                                print("Achou a unidade")
                                unidade.round_start()
                            Ja_Administrado.append(d)
                            #print(Ja_Administrado)
                            duplas.pop(n)

                            for adm_idx in Ja_Administrado:
                                if adm_idx == dupla3:
                                    print("Entrou no adm")
                                    battle_admin(adm_idx[0], adm_idx[1])
                else:
                    print("invalido")
            ##########################################################
            elif batalha_escolhida == "4":
                print("Aceito")
                if competidores >= 8:
                    print("passou no check")
                    for n,d in enumerate(duplas):
                        if d == dupla4:
                            for unidade in d:
                                print("Achou a unidade")
                                unidade.round_start()
                            Ja_Administrado.append(d)
                            #print(Ja_Administrado)
                            duplas.pop(n)

                            for adm_idx in Ja_Administrado:
                                if adm_idx == dupla4:
                                    print("Entrou no adm")
                                    battle_admin(adm_idx[0], adm_idx[1])
                else:
                    print("invalido")

                    
            elif batalha_escolhida.upper() == "C":
                for c in Ja_Administrado:
                    for d in c:
                        d.vere()
                    batalha(c[0],c[1])
                break

        print("=====================================================================================")

        for dup in duplas:
            for sta in dup:
                sta.round_start()
            batalha(dup[0], dup[1])
        break

def battle_admin(start1, start2):
    print("Qual das startups deseja administrar?")
    print(f"Startup 1: {start1.nome}")
    print(f"Startup 2: {start2.nome}")
    resposta = str(input("1 / 2: "))
    if resposta == "1":
        veredito_list = start1.ver2
        print("Qual seu veredito?")
        #print(start1.nome)
        #print(veredito_list)
        for a in veredito_list:
            if a == "C":
                print("C = Pitch convincente")
            if a == "B":
                print("B = Produto com bugs")
            if a == "T":
                print("T = Boa tração de usuários")
            if a == "I":
                print("I = Investidor irritado")
            if a == "F":
                print("F = Fake news no pitch")
        ver = str(input(": "))

        pos = 0
        for i in veredito_list:
            if i == ver.upper():
                start1.veredito.append(veredito_list.pop(pos))    
            else:
                pos += 1
        
    elif resposta == "2":
        veredito_list = start2.ver2
        print("Qual seu veredito?")
        for a in veredito_list:
            if a == "C":
                print("C = Pitch convincente")
            if a == "B":
                print("B = Produto com bugs")
            if a == "T":
                print("T = Boa tração de usuários")
            if a == "I":
                print("I = Investidor irritado")
            if a == "F":
                print("F = Fake news no pitch")
        ver = str(input(": "))

        pos = 0
        for i in veredito_list:
            if i == ver.upper():
                start2.veredito.append(veredito_list.pop(i))
            else:
                pos += 1
    else: 
        print("Invalido")
    
    print("Gostaria de fazer outro veredito?")
    new_ver = str(input("S/N: "))
    if new_ver.upper() == "N":
        is_admin = False
        iniciador_batalhas()
    
    elif new_ver.upper() == "S":
        pass

#Esta função ira comparar a pontuação das startups em dupla baseando-se na pontuação final de cada rodada
def batalha(startup1, startup2):
    if startup1.pontuacao > startup2.pontuacao:
        print(f"Vencedor é  {startup1.nome}")
        startup1.pontuacao += 30 
        #Caso esta seja a ultima rodada do torneio, a boolean "fase_final" se tornará verdadeira, fazendo com que o vencedor da batalha seja adicionado a variavel "vencedor". Caso contrario o looping continuará normalmente
        if fase_final == True:
            vencedor = startup1
            finalizacao(vencedor)
        else:
            startups.append(startup1)
            derrotados.append(startup2)
    
    #Aqui acontece o sharkfight. O programa decide entre as duas startups da batalha e adiciona dois pontos a uma delas.
    elif startup1.pontuacao == startup2.pontuacao:
        sharkfight = random.randint(0,1)
        if sharkfight == 0:
            startup1.pontuacao += 2
        else: 
            startup2.pontuacao += 2
        batalha(startup1, startup2)

    #A qui acontece o mesmo que no inicio da função, porem no caso da startup2 ser vencedora
    else:
        print(f"Vencedor é  {startup2.nome}")
        startup2.pontuacao += 30 
        if fase_final == True:
            vencedor = startup2
            finalizacao(vencedor)
        else:
            startups.append(startup2)
            derrotados.append(startup1)


#esta função adiciona startups á lista "startups". 
def adicionar_startup(company):
    #As linhas abaixo utilizam o imput do usuario para cadastrar informações sobre a startup.
    company = startup("","",0,70,0,0,0,0,0,0,0,0,0, [], [])
    company.nome = str(input("Insira o nome da startup: "))
    company.slogan = str(input("Insira o slogan da startup: "))
    company.ano_fundacao = int(input("Insira o ano de fundação da startup: "))

    company.set_rand_stats()
    #As informações são mostradas ao usuario aqui
    print(f"Nome: {company.nome}" )
    print(f"Slogan: {company.slogan}" )
    print(f"Ano de fundação: {company.ano_fundacao}" )

    print("-------------")
    print("Deseja continuar?")

    #Será pedido do usuario que confirme as informações sobre a startup antes de continuar
    resposta = str(input("S/N: "))
    if resposta == "s" or resposta =="S":
        startups.append(company)
        print("Startup inserida!")
        print(startups)
        #A startup foi inserida na lista "startups" 
    elif resposta == "n" or resposta == "N":
        pass
        #Cancela a operação
    else:
        print("Erro: resposta inserida invalida")
        #notifica erro caso o input seja invalido
   

#loop de interação do programa

while ganhou == "":
    #A seção de codigo abaixo representa o menu. O usuario deverá utilizar os inputs corretos para navega-lo
    #A troca de sessões do menu é controlada pela string "menu", seu valor sendo controlado pelo input do usuario
    if menu == "main":
        print("---------------------------------")
        print("Escolha uma das opções abaixo:")
        print("I = Iniciar torneio")
        print("A = Adicionar startups")
        resposta = str(input(""))
        if resposta == "A" or resposta == "a":
            menu = "Adicionar-startups"
        
        elif resposta == "I" or resposta == "i":
            menu = "iniciar-torneio"

        #Esta seção está aqui para teste e será comentada no futuro.        
        elif resposta == "T" or resposta == "t":
            print("Testando")
            while len(startups) < 8:
                startups.append("WAWA")
            menu = "main"
        
        #Esta seção checa os atributos de todas as startups cadastradas
        elif resposta == "C" or resposta == "c":
            menu = "custom"
            print("Customize as startups")
            if len(startups) < 0:
                for i in startups:
                    if i is startup:
                        i.show_everything()
                        menu = "main"
                        
                    #as verificações asseguir servem para qualidade de vida

                    else:
                        print("Algo deu errado. Você provavelmente utilizou o comando T antes de utilizar está função, gostaria de reiniciar?")
                        resposta = str(input("S/N: "))

                        if resposta =="s" or resposta == "S":
                            startups = []
                            print("Startups resetadas")
                            menu = "main"

                        elif resposta == "n" or resposta == "N":
                            print("Nenhuma alteração foi feita")
                            menu = "main"

            else:
                print("Algo deu errado. Verifique se ha startups cadastradas")
                menu = "main"

        #Esta verificação cria automaticamente oito startups para teste
        elif resposta == "G" or resposta == "g":
            print("Adicionado startups base")
            start1 = startup("A","AMA", 1, 70,0,0,0,0,0,0,0,0,0, [], [])
            start2 = startup("B","BMB", 2, 70,0,0,0,0,0,0,0,0,0, [], [])
            start3 = startup("C","CMC", 3, 70,0,0,0,0,0,0,0,0,0, [], [])
            start4 = startup("D","DMD", 4, 70,0,0,0,0,0,0,0,0,0, [], [])
            start5 = startup("E","EME", 5, 70,0,0,0,0,0,0,0,0,0, [], [])
            start6 = startup("F","FMF", 6, 70,0,0,0,0,0,0,0,0,0, [], [])
            start7 = startup("G","GMG", 7, 70,0,0,0,0,0,0,0,0,0, [], [])
            start8 = startup("H","HMH", 8, 70,0,0,0,0,0,0,0,0,0, [], [])
            start1.set_rand_stats()
            start2.set_rand_stats()
            start3.set_rand_stats()
            start4.set_rand_stats()
            start5.set_rand_stats()
            start6.set_rand_stats()
            start7.set_rand_stats()
            start8.set_rand_stats()
            startups = [start1, start2, start3, start4,start5,start6,start7,start8]
            print(len(startups))
        
        #caso o usuario utilize um input invalido, este codigo rodará e recomeçará o loop
        else:
            print("Input invalido, tente novamente")

    #Esta parte do menu controla a adição de novas startups através de um loop.
    if menu == "Adicionar-startups":
        #Caso a lista "startups" possua oito itens, o usuario será enviado de volta ao menu principal com uma mensagem de erro
        if len(startups) < 8:
            adicionar_startup(next_startup)   
            #Caso o numero de startups cadastradas seja inpar, outra startup deverá ser adicionada
            if len(startups) % 2 != 0 and len(startups) <= 8:
                 adicionar_startup(next_startup)
                 menu = "main"
            #as proximas cinco linhas relatam erros e mandam o usuario devolta para o menu inicial
            else:
                print("Algo deu errado...")
        else:
            print("Quantidade maxima de startups atingida.")
            menu = "main"

    #Esta sessão irá criar duplas para todos os competidores

    elif menu == "iniciar-torneio":

        duplas = []
        dupla1 = []
        dupla2 = []
        dupla3 = []
        dupla4 = []
        
        #Esta sessão organiza os competidores em duplas 
        if torneio_iniciado == False and len(startups) < 4:
            print("Quantidade de startups inseridas invalida, é necessario pelo menos quatro startups")
            menu = "main"

        elif len(startups) % 2 == 0:
            competidores = len(startups)

            while len(dupla1) < 2:
                index = random.randint(0, len(startups) - 1)
                escolhida = startups.pop(index)
                dupla1.append(escolhida)
            if competidores >= 4:
                while len(dupla2) < 2:
                    index = random.randint(0, len(startups) - 1)
                    escolhida = startups.pop(index)
                    dupla2.append(escolhida)

            if competidores >= 6:
                while len(dupla3) <2:
                    index = random.randint(0, len(startups) - 1)
                    escolhida = startups.pop(index)
                    dupla3.append(escolhida)

                if competidores >= 8:
                    while len(dupla4) <2:
                        index = random.randint(0, len(startups) - 1)
                        escolhida = startups.pop(index)
                        dupla4.append(escolhida)
        
          #  print(startups)
          #  print(dupla1)
          #  print(dupla2)
         #   print(dupla3)
           # print(dupla4)

            menu = "torneio"
            torneio_iniciado = True


    elif menu == "torneio":
        fase_atual += 1
        print(f"Rodada {fase_atual}")
        print(f"Batalha 1: {dupla1[0].nome} VS {dupla1[1].nome}")
        if len(dupla2) > 0:
            print(f"Batalha 2: {dupla2[0].nome} VS {dupla2[1].nome}")
        if len(dupla3) > 0:
            print(f"Batalha 3: {dupla3[0].nome} VS {dupla3[1].nome}")
    
        if len(dupla4) > 0:
            print(f"Batalha 4: {dupla4[0].nome} VS {dupla4[1].nome}")

        #escolha do usuario
        duplas = [dupla1]
        if competidores >= 4:
            duplas.append(dupla2)
        if competidores >= 6:
            duplas.append(dupla3)
        if competidores >= 8:
            duplas.append(dupla4)
        print("Deseja administrar uma batalha?")
        resposta = str(input("S/N: "))

        if resposta == "S" or resposta =="s":
            sera_adminstrador = True
            resposta = ""

            if len(duplas) > 1:
                print(len(duplas))
                print("")
                iniciador_batalhas()
                menu = "iniciar-torneio"

            else:
                fase_final = True
                print("")
                iniciador_batalhas()
                break
            


        elif resposta == "N" or resposta =="n":
            sera_adminstrador = False

            if len(duplas) > 1:
                print(len(duplas))
                print("")
                iniciador_batalhas()
                menu = "iniciar-torneio"

            else:
                fase_final = True
                print("")
                iniciador_batalhas()
                break
 
