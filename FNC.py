# -*- coding: utf-8 -*-

# Subrutinas para la transformacion de una
# formula a su forma clausal

# Subrutina de Tseitin para encontrar la FNC de
# la formula en la pila
# Input: A (cadena) de la forma
#                   p=-q
#                   p=(qYr)
#                   p=(qOr)
#                   p=(q>r)
# Output: B (cadena), equivalente en FNC
def enFNC(A):
    assert(len(A)==5 or len(A)==8), u"Fórmula incorrecta!"
    B = ''
    p = A[0]
    # print('p', p)
    if "-" in A:
        q = A[-1]
        # print('q', q)
        B = "-"+p+"O-"+q+"Y"+p+"O"+q
    elif "Y" in A:
        q = A[4]
        # print('q', q)
        r = A[6]
        # print('r', r)
        B = q+"O-"+p+"Y"+r+"O-"+p+"Y-"+q+"O-"+r+"O"+p
    elif "O" in A:
        q = A[4]
        # print('q', q)
        r = A[6]
        # print('r', r)
        B = "-"+q+"O"+p+"Y-"+r+"O"+p+"Y"+q+"O"+r+"O-"+p
    elif ">" in A:
        q = A[4]
        # print('q', q)
        r = A[6]
        # print('r', r)
        B = q+"O"+p+"Y-"+r+"O"+p+"Y-"+q+"O"+r+"O-"+p
    else:
        print(u'Error enENC(): Fórmula incorrecta!')
    #print(B)
    return B

# Algoritmo de transformacion de Tseitin
# Input: A (cadena) en notacion inorder
# Output: B (cadena), Tseitin
def Tseitin(A, letrasProposicionalesA):
    letrasProposicionalesB = [chr(x) for x in range(256, 1200)]
    assert(not bool(set(letrasProposicionalesA) & set(letrasProposicionalesB))), u"¡Hay letras proposicionales en común!"

    #  IMPLEMENTAR AQUI ALGORITMO TSEITIN
    #=================|Inicio de implementación|=========================
    #===========================|AUTOR: ESTEFANIA LAVERDE|==================================
    L=[]#Inicializamos lista de conjunciones||aquí se guardan todos los <>
    Pila=[]#Inicializamos Pila
    I=-1#Inicializamos contador de variables nuevas
    s=A[0]#Inicializamos símbolo de trabajo

    while len(A)>0:
        if (s in letrasProposicionalesA or s in letrasProposicionalesB) and len(Pila)!=0 and Pila[-1]=='-': #Si s es un átomo y Pila no vacía y Pila[-1] = ’¬’
            I+=1
            Atomo = letrasProposicionalesB[I]
            Pila=Pila[0:-1]#Se van eliminando caracteres uno por uno
            Pila.append(Atomo)
            L.append(Atomo+"<>"+"-"+s)
            A=A[1:]
            if len(A)>0:
                s=A[0]
        elif s==")":#Para las formulas con conectores binarios
            w=Pila[-1]
            u=Pila[-2]#El conector binario
            v=Pila[-3]
            Pila=Pila[:len(Pila)-4]
            I+=1
            Atomo=letrasProposicionalesB[I]
            L.append(Atomo+"<>"+"("+v+u+w+")")
            s= Atomo
        else:
            Pila.append(s)
            A=A[1:]
            if len(A)>0:
                s=A[0]
    B=""
    if I<0:
        Atomo=Pila[-1]
    else:
        Atomo=letrasProposicionalesB[I]

    for x in L:

        y=enFNC(x)
        #print(y)
        B+="Y"+y


    B= Atomo+B

    print("todos los iff: ",L)
    #print(B)
    return B

    #=================|Fin de implemetación|================================
    pass

#========================|PRUEBA|===============================
#letrasProposicionalesprubeaA=["p","q","r"]
#f="-p"
#print(Tseitin(f,letrasProposicionalesprubeaA))
#===========================|LA PRUEBA FUNCIONA|===========================

# Subrutina Clausula para obtener lista de literales
# Input: C (cadena) una clausula sin paréntesis
# Output: L (lista), lista de literales
# Se asume que cada literal es un solo caracter
def Clausula(C):

    #  IMPLEMENTAR AQUI ALGORITMO CLAUSULA
    #===============================|INICIO DE IMPLEMENTACIÓN|==========================
    #===============================|AUTOR: JULIAN CASTRO|===========================================
    L=[]
    while len(C)>0:

        s=C[0]
        if s=="-":
            L.append(s+C[1])
            C=C[3:]
        else:
            L.append(s)
            C=C[2:]
    return L
    #===============================|FIN DE IMPLEMENTACIÓN|=============================
    pass
#========================|PRUEBA|===============================
#clausula="ĀY-ĀO-pYĀOp"
#print(Clausula(clausula))
#===========================|LA PRUEBA FUNCIONA|===========================

# Algoritmo para obtencion de forma clausal
# Input: A (cadena) en notacion inorder en FNC y sin paréntesis
# Output: L (lista), lista de listas de literales
def formaClausal(A):

    #  IMPLEMENTAR AQUI ALGORITMO FORMA CLAUSAL
    #===============================|INICIO DE IMPLEMENTACIÓN|=============================
    #===============================|AUTOR: JULIAN CASTRO|===============================================
    L=[]
    i=0

    while len(A)>0:
        if i>=len(A):
            L.append(Clausula(A))
            A=[]
        else:
            if A[i]=="Y":
                L.append(Clausula(A[:i]))
                A=A[i+1:]
                i=0
            else:
                i+=1
    return L
    #===============================|FIN DE IMPLEMENTACIÓN|================================
    pass
#
