# -*- coding: utf-8 -*-

# Transformación de una formula en forma clausal
# Input: cadena de la formula en notacion inorder
# Output: lista de listas de literales

# Importando la libreria FNC
import FNC as fn
letrasProposicionalesA = ['p', 'q', 'r', 's', 't']
# # Formula a la cual encontrar su forma clausal
#formula = "-p"

#========================|descripción de funcionamiento esperado|===================
#1) Se encuentran las subfórmulas de "-p" excepto la las letras proposicionales que componen a la fórmula: RESULTADO "-p"
#2) Se asigna una nueva letra proposicional para cada subfórmula: RESULTADO a "-p" se le asigna "x1"
#3) Se asocia la subfórmula con su respectiva letra proposicional, y si aparece como subfórmula de otra subfórmula,
#se coloca la letra proposicional correspondiente en vez de la subfórmula: RESULTADO "x1 <> -p"
#4) Se crea una nueva fórmula compuesta por la fórmula origina y la conjunción de todos los sii del paso anterior: RESULTADO "-pY(x1<>-p)"
#Hasta aquí llega el funcionamiento de Tsteitin, ahora empieza formaClausal
#5) Se cambian las fórmulas que no están en FNC con su equivalencia lógica que si está en FNC (son las equivalencias vistan en clase): RESULTADO "-pY(-x1O-p)Y(pOx1)"
#6) Del anterior paso quedan uniones de Y. Se separa la cadena cada vez que se encuentre una conjunción, y nos
#quedamos solo con los la fórmula original y las que están entre paréntesis: RESULTADO "-p","(-x1O-p)","(pOx1)"
#7) Se toman los átomos de las formulas ya separadas y se meten en listas. Cada paréntesis conforma una lista: RESULTADO [-p],[-x1,-p], [x1,p]
#8) Cada lista se mete en una lista, la cual va a retornar formaClausal: RESULTADO [[-p],[-x1,-p],[x1,p]]
#===================================================================================
#formula="((p>q)>r)"
formula="(pY(-qY-r))"
#formula = "(pYq)"
#formula = "(pOq)"
#formula = "(p>q)"
print("La fórmula que probamos es: ",formula)
# Aplicando el algoritmo de Tseitin a formula
# Se obtiene una cada que representa la formula en FNC
fFNC = fn.Tseitin(formula, letrasProposicionalesA)

#===============|funcionamiento|=====================
#input: lista de letras proposicionales y formula tipo string en modo inorder
#outpu: fórmula (str) a la que se le ha aplicado el algoritmo de Tseitin (sin parentesis)
#=======================================================

# Se obtiene la forma clausal como lista de listas de literales
fClaus = fn.formaClausal(fFNC)

#==============|funcionamiento|========================
#input: formula resultada del algorítmo de Tseitin (sin parentesis)
#output: lista de listas literadas, que muestran la forma clausal
#=======================================================

# Imprime el resultado en consola
print(fClaus)
