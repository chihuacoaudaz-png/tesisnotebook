# INSPECCIÓN TÉCNICA DEL SCRIPT DE HOLMBERG EXISTENTE

```python
import matplotlib.pyplot as plt
import numpy as np
import math as mt
import pandas as pd
from matplotlib.backends.backend_pdf import PdfPages
#METODO DE HOLDMERG
print("SOTWARE DE CÁLCULO Y DISEÑO DE MALLA DE PERFORACIÓN CON MÉTODO DE HOLDMERG:\n")

#PASO 1:Considerando la barra perforadora y diametro de brocas, calculamos el número de taladros de alivio

print("Coloque las medidas de la sección con la que desea trabajar")
Ancho=float(input("Ancho de la labor(m): "))
Altura=float(input("Altura de la labor(m): "))
a=0
while a<a+1:
    fl=float(input("Coloque la flecha de arco con la que quiera trabajar(recomendación: 1.25): "))
    if fl<=(Ancho/2) and fl>0:
        break
    else:
        print(f"El valor de la flecha de arco debe ser mayor a 0 y menor a {Ancho/2}, corrige el valor")
        a += 1

print("Indícame los datos de perforación:\n")
Hp=float(input("Coloque la longitud de la barra de perforación (ft): "))*0.3048


I=Hp*0.95
i=1
while i<i+1:
    z=input("Ostenta broca rimadora? (si/no): ")
    if z == "no":
        D1=float(input("Coloque el diametro de la broca de producción (mm): "))/1000
        n=1
        H=0
        while n:
            if H < I:
                Dv=D1*mt.sqrt(n)
                H=0.15+34.1*(Dv)-39.4*(Dv)**2
                n +=1
            else:
                n -=1
                print(f"\nEl número de taladros vacios de alivio que utilizará es {n}\n")  
                break
        break    
    elif z == "si":
        D2=float(input("Coloque el diametro de la broca rimadora (mm): "))/1000
        D1=float(input("Coloque el diametro de la broca de producción (mm): "))/1000
        n=1
        H=0
        while n:
            if H < Hp:
                Dv=D2*mt.sqrt(n)
                H=0.15+34.1*(Dv)-39.4*(Dv)**2
                n +=1
            else:
                n -=1
                print(f"\nEl número de taladros vacios de alivio que utilizará es {n}\n")
                break
        break    
    else:
        print("Coloque una respuesta valida (si/no)")
        i+=1
        
"""De aca tengo el valor de Dv y n"""
NB=n

#PASO 2: Obtener Burden, Espaciamiento y Factor de carga de los taladros    

#2.1.-PRIMER CUADRANTE


print("\nIndicame los datos de la roca perteneciente al frente: \n")
#Calculamos el consumo de explosivo con la formula Ashby
σ_trac=float(input("Coloque el esfuerzo de tracción de la roca en (Mpa): "))
σ_comp=float(input("Coloque el esfuerzo de compresión de la roca en (Mpa): "))
dr=float(input("Coloque la densidad de roca atacada (Tm/m3): "))
GSI=float(input("Coloque el GSI de la roca: "))
RQD=float(input("Coloque el RQD de la roca(%): "))
Ce=(0.56*dr*mt.tan(mt.radians((GSI+15)/2)))/(((115-RQD)/3.3)**(1/3))
#Calculamos la constante de roca sueca C con la siguiente ecuación
C=0.878*Ce+0.0052

#Calculo del BT1 y BP1 (burden teorico y practico) (m)
i=0
while i<i+1:
    desv=float(input("Coloque el porcentaje de desviación de perforación que presenta (0.5 - 2)(%): "))
    if desv < 1 and desv >=0.5:      
       α=float(input("Coloque la desviación angular en mm/m (recomendación:10): "))/1000
       β=float(input("Coloque el error de emboquillado en mm (recomendación: 20): "))/1000
       F=α*Hp+β
       BT1O=1.5*Dv
       BP1O=1.5*Dv-F
       break
    elif desv >= 1 and desv <= 2:
        α=float(input("Coloque la desviación angular en mm/m (recomendación:10): "))/1000
        β=float(input("Coloque el error de emboquillado en mm (recomendación: 20): "))/1000
        F=α*Hp+β
        BT1O=1.7*Dv
        BP1O=1.7*Dv-F
        break
    else:
        print("Coloca una desviación valida")
        i +=1


print("\nIndicame los datos del explosivo (encartuchado) que desear usar (Saque todos estos datos de su ficha tecnica): \n")
#Calculo de concentracion de carga lineal minima q1 en el primer cuadrante (Kg/m)
m=1
while m<m+1: 
    i=1
    while i<i+1:
        if D1 <= 0.0318:
            P_explo=float(input("Coloque el peso neto de un cartucho de tu explosivo elegido(kg): "))
            S_anfo=float(input("Coloque la potencia relativa en peso de su explosivo referida al ANFO(%): " ))/100
            Dc=float(input("Coloque el diametro del encartuchado de explosivo(mm): "))
            Long_cartucho=float(input("Coloque la longitud del encartuchado de explosivo(pulg): "))*0.0254
            de=float(input("Coloque la densidad del explosivo(g/cc): "))
            q1O=(D1/0.032)*(3/2)*(BT1O/Dv)**(3/2)*(BT1O-(Dv/2))
            q1=(de*mt.pi*(Dc**2)*10**(-3))/4
            if q1 >= q1O:
                print(f"\nLa concentracion de carga lineal de su explosivo {q1} (kg/m) es mayor que la mínima concentración que debe utilizar {q1O} (kg/m)")   
                break
            else:
                print(f"\nERROR, describa otro explosivo con mayor concentración de carga lineal que {q1O} (kg/m), su explosivo tiene una concentración de carga {q1} (kg/m)\n")
                i +=1
        else:
            P_explo=float(input("Coloque el peso neto de un cartucho de tu explosivo elegido(kg): "))
            S_anfo=float(input("Coloque la potencia relativa en peso de su explosivo referida al ANFO(%): " ))/100
            Dc=float(input("Coloque el diametro del encartuchado de explosivo(mm): "))
            Long_cartucho=float(input("Coloque la longitud del encartuchado de explosivo(pulg): "))*0.0254
            de=float(input("Coloque la densidad del explosivo(g/cc): "))
            q1O=55*D1*(BT1O/Dv)**(3/2)*(BT1O-(Dv/2))*(C/0.4)/S_anfo
            q1=(de*mt.pi*(Dc**2)*10**(-3))/4
            if q1 >= q1O:
                print(f"\nLa concentracion de carga lineal de su explosico {q1} (kg/m) es mayor que la mínima concentración que debe utilizar {q1O} (kg/m)")
                break
            else:
                print(f"\nERROR, describa otro explosivo con mayor concentración de carga lineal que {q1O} (kg/m)\n")
                i +=1
    
    #Calculo del BT1
    if D1 <= 0.0318:
        Coeficientes=[1,-(Dv),(Dv**2)/4,0,0,-(((q1*0.032*2*(Dv**1.5))/(D1*3))**2)]
        def resolver_ecuacion(coeficientes):
              soluciones = np.roots(coeficientes)
              soluciones_reales_positivas = [sol.real for sol in soluciones if np.isreal(sol) and sol.real > 0]  
              return soluciones_reales_positivas
    
        def encontrar_valor_mas_cercano(lista, numero):
              valor_mas_cercano = min(lista, key=lambda x: abs(x - numero))
              return valor_mas_cercano
        BT1_soluciones=resolver_ecuacion(Coeficientes)
        BT1_solucion=encontrar_valor_mas_cercano(BT1_soluciones, BT1O)
        BT1=BT1_solucion
    else:
        Coeficientes=[1,-(Dv),(Dv**2)/4,0,0,-(((q1*S_anfo*0.4*(Dv**1.5))/(55*D1*C))**2)]
        def resolver_ecuacion(coeficientes):
              soluciones = np.roots(coeficientes)
              soluciones_reales_positivas = [sol.real for sol in soluciones if np.isreal(sol) and sol.real > 0]  
              return soluciones_reales_positivas
    
        def encontrar_valor_mas_cercano(lista, numero):
              valor_mas_cercano = min(lista, key=lambda x: abs(x - numero))
              return valor_mas_cercano
        BT1_soluciones=resolver_ecuacion(Coeficientes)
        BT1_solucion=encontrar_valor_mas_cercano(BT1_soluciones, BT1O)
        BT1=BT1_solucion
    
    #Calculo del buerdem practico
    BP1=BT1-F
    
    #Calculo de abertura del primer cuadrante A1 (m)
    A1=BP1*mt.sqrt(2)
    
    #Calculo de taco para el primer cuadeante
    T1=10*D1
    
    #Calculo de longitud de carga para taladros del primer cuadrante
    LC1=Hp-T1
    
    #Calculo de numero de cartuchos en primer cuadrnate
    N1=int(q1*(LC1)/P_explo)
    
    List_BT=[BT1]
    List_BP=[BP1]
    List_A=[0,A1]
    List_q=[q1]
    List_T=[T1]
    List_LC=[LC1]
    List_NC=[N1]
    
    #2.2.-CUADRANTES RESTANTES
    BP=BP1
    lista_q2=[]
    i=0
    Ah= A1
    while i<i+1:
        
        Ak=(BP+List_A[i]/2-F)*mt.sqrt(2)
        
        #Calculo de Burden maximo
        BT=8.8*10**(-2)*mt.sqrt((Ak*q1*S_anfo)/(D1*C))         
        
        #Calculo de burden practico
        BP=BT-F
        
        #Calculo de la nueva apertura
        Ah=mt.sqrt(2)*(BP+(Ah/2))
         
        #calculo del taco
        T2=10*D1
        
        #Calculo de longitud de carga para taladros del priemr cuadrante
        LC2=Hp-T2
    
        #Calculo de numero de cartuchos en primer cuadrante
        N2=int(q1*(LC2)/P_explo)
        
        q2=q2=(540*D1*C*2*Ak)/S_anfo
        lista_q2.append(q2)
        
        if Ah<mt.sqrt(Hp):
            List_BT.append(BT)
            List_BP.append(BP)
            List_A.append(Ah)
            List_q.append(q1)
            List_T.append(T2)
            List_LC.append(LC2)
            List_NC.append(N2)
            i+=1
            Cuadrantes=i
        else:
            List_A.pop(0)
            break
    if q1>lista_q2[0]:
        m +=1
    else:
        break   
        
print(f"Ademas, ostenta una concentración de carga lineal menor a la oncentracion de carga maxima {lista_q2[0]} (kg/m)")  
print(f"\nSe han creado {Cuadrantes+1} cuadrantes de corte\n")

#2.3.-CALCULO DE ARRASTES

f=1.45   
rela_esp_burd=1
if List_BP[-1]>=1.4:
    c=C+0.05
else:
    c=C+(0.07/List_BP[-1])

#UTILIZACION DEL METIDO GUSTAFFSON (calculo de burden teorico de arrastres)
BTA=0.9*mt.sqrt((q1*S_anfo)/(c*f*(rela_esp_burd)))
if BTA>0.6*Hp:
    BTA=0.6*Hp
    
#Calculo de concentracion lineal de carga 
qa=q1

#Calulo del numero de taladros
ϕ=float(input("Coloque el ángulo de realce maximo que realiza el jumbero(se recomientas 3): "))
NTA=int((Ancho+2*Hp*mt.sin(mt.radians(ϕ)))/BTA+1)

#Calculo de espaciamiento teorico
STA=(Ancho+2*Hp*mt.sin(mt.radians(ϕ)))/(NTA-1)

#Calculo del espaciamiento practico
SPA=STA-Hp*mt.sin(mt.radians(ϕ))

#Calculo de Burden Practico
BPA=BTA-Hp*mt.sin(mt.radians(ϕ))-F

#Altura de carga en el fondo
HFA=1.25*BPA

#Concentracion de carga en el fondo
qfa=qa

#Numero de cartuchos para carga de fondo de taladro
NFA=int(HFA/Long_cartucho)

#Longitus de taco
TA=T1

#Altura de carga de la columna de taladro
HCA=Hp-HFA-10*D1

#Conectracion de carga en la columna
qca=qfa*0.7

#Numero de cartuchos para carga de columna de taladro
NCA=int(HCA/Long_cartucho)



#2.4.-CALCULO DE CORONA

print("\nPara la CORONA se debe usar un explosivo con menor fuerza rompedora, es por ello, que se solicitan los siguientes datos:\n")

#Calculo de espaciamiento (Precorte)
#a.-presion de taladro
i=0
while i<i+1:
    peso_explo=float(input("Coloque el peso de una unidad de explosivo (Kg): "))
    drC=float(input("Coloque la densidad del explosivo que se usara en la CORONA(g/cm3): "))
    VOD=float(input("Coloque la velocidad de detonacion del explosivo usado en la CORONA (m/seg): "))
    Dcc=float(input("Coloque el diametro del explosivo que se usara en la CORONA (mm): "))
    Pt=228*10**(-6)*drC*(((VOD)**2)/(1+0.8*drC))
    #b.-presion de taladro efectivo
    Pte=Pt*(((Dcc)**0.42)/(D1*1000))
    #calculo de concentracion lineal de carga minima
    qc=90*(D1)**2
    qce=drC*1000*mt.pi+(Dcc)**2*(10**(-6))/4
    if σ_comp>Pte and qce>qc:
        print(f"COORECTO, Escogiste un explosivo con presion efectiva {Pte} (Mpa) menor a {σ_comp} y concentración de carga lineal {qce} mayor a la minima {qc}")
        break
    else:
        print(f"La presión efectiva del explosivo {Pte} (Mpa) es mayor que el ezfuerso de compresion de la roca {σ_comp} (Mpa), tiene que probar con otro explosivo ")
        i +=1

#Espaciamiento de CORONA
SC=D1*(Pte+σ_trac)/σ_trac

#Calculo de BTC (Como la relación S/B debe ser 0.8)
BTC=SC/0.8

#Calculo de burden práctico
BPC=BTC-Hp*mt.sin(mt.radians(ϕ))-F

#Longitus de taco
TC=T1

#Longitud de carga en columna
LCC=LC1
a=(4*Ancho*fl)/((Ancho**2)+(4*fl**2))
b=((Ancho**2)+(4*fl**2))/(4*fl)

#Calculo numero de taladros
long_arc_corona=(((Ancho**2)+(4*fl**2))/(4*fl))*np.arcsin((4*Ancho*fl)/((Ancho**2)+(4*fl**2)))
NTC=int((long_arc_corona/SC)+1)

#Calculo de numero de cartuchos por taladro
NCC=int(((LCC)*qce/peso_explo)+0.5)


#2.5.-CALCULO DE HASTIALES

#espacimiento hastial
SH=SC

#Calculo de BPH(BURDEN TEORICO HASTIAL)
BTH=BTC

#Calculo de BPH(BURDEN PRACTICO HASTIAL)
BPH=BPC

#Calculo de longitud disponible para taladros de hastiales
Long_disponible_H=Altura-BPA-fl

#Numero de taladros
NTH=int((Long_disponible_H/(SC))+1)

#Longitus de taco
TH=T1

#Calculo de concentracion lineal de carga 
qh=qce

#Altura de carga columna
LCH=LCC

#Numero de cartucho por talado
NCH=int(((LCC)*qce/peso_explo)+0.5)


#Grafica de resultados

fig1, ax1 = plt.subplots(figsize=(10,10))

#Linea base
ax1.plot([0,Ancho],[0,0],color='black', linewidth=0.5)
#Lineas laterales
ax1.plot([0,0],[0,Altura-fl],color='black', linewidth=0.5)
ax1.plot([Ancho,Ancho],[0,Altura-fl],color='black', linewidth=0.5)
#Linea de corona
centro = (Ancho/2, Altura-(((Ancho**2)+(4*fl**2))/(8*fl)))  
radio = (((Ancho**2)+(4*fl**2))/(8*fl))
theta_inicio = (np.pi/2)-np.arcsin((4*Ancho*fl)/((Ancho**2)+(4*fl**2)))
theta_fin = (np.pi/2)+  np.arcsin((4*Ancho*fl)/((Ancho**2)+(4*fl**2)))
theta = np.linspace(theta_inicio, theta_fin, 100)
x = centro[0] + radio * np.cos(theta)
y = centro[1] + radio * np.sin(theta)
ax1.plot(x, y,color='black', linewidth=0.5)

#Dibujo de taladros en la Corona
angulos = np.linspace((np.pi/2)-np.arcsin((4*Ancho*fl)/((Ancho**2)+(4*fl**2))),(np.pi/2)+  np.arcsin((4*Ancho*fl)/((Ancho**2)+(4*fl**2))), NTC)
x_corona = centro[0] + radio * np.cos(angulos)
y_corona = centro[1] + radio * np.sin(angulos)
plt.scatter(x_corona, y_corona,facecolors='orange', edgecolors='black', s=50)

#Dibujo de taladros de arraste
#Taladros de esquina
plt.scatter([0,Ancho],[0,0],facecolors='red', edgecolors='black', s=50)
#Taladros intermedios
y_arrastre=[]
x_arrastre=np.linspace(SPA, Ancho-SPA,NTA-2)
for  i in x_arrastre:
    y=0
    y_arrastre.append(y)
y_arrastre=tuple(y_arrastre)
plt.scatter(x_arrastre, y_arrastre,facecolors='red', edgecolors='black', s=50)    

#Genera puntos de los Hastiales
#Hastiales derechos

x_Hastial=[]
y_Hastial=np.linspace(BPA, Altura-fl,NTH-1,endpoint=False)
for  i in y_Hastial:
    x_values=0
    x_Hastial.append(x_values)
x_Hastial=tuple(x_Hastial)

plt.scatter(x_Hastial, y_Hastial,facecolors='orange', edgecolors='black', s=50)  

#Hastiales izquierdos

x_Hastial=[]
y_Hastial=np.linspace(BPA, Altura-fl,NTH-1,endpoint=False)
for  i in y_Hastial:
    x_values=Ancho
    x_Hastial.append(x_values)
x_Hastial=tuple(x_Hastial)

plt.scatter(x_Hastial, y_Hastial,facecolors='orange', edgecolors='black', s=50)  

#Genera punto de los cuadradores

for i in range(len(List_A)):   
    if i % 2 == 0:
        h=(Altura-fl+1)/2
        A=(List_A[i]*np.sqrt(2))/2
        vertices = [
            [Ancho/2+A, h],            
            [Ancho/2,h+A],         
            [(Ancho/2)-A, h],      
            [Ancho/2,h-A],         
            [Ancho/2+A, h]            
        ]
        vertices = np.array(vertices)
        plt.plot(vertices[:, 0], vertices[:, 1],color='black', linewidth=0.5)
        plt.scatter(vertices[:, 0], vertices[:, 1],facecolors='y', edgecolors='black', s=50)
        
    else:
        h=(Altura-fl+1)/2
        A=(List_A[i]/2)
        vertices = [
            [Ancho/2+A, h+A],            
            [Ancho/2-A,h+A],         
            [(Ancho/2)-A, h-A],      
            [Ancho/2+A,h-A],         
            [Ancho/2+A, h+A]             
        ]
        vertices = np.array(vertices)
        plt.plot(vertices[:, 0], vertices[:, 1],color='black', linewidth=0.5)
        plt.scatter(vertices[:, 0], vertices[:, 1],facecolors='y', edgecolors='black', s=50)


if Altura<=3:
    ax1.plot([Ancho/2,  Ancho/2],[0,Altura],linestyle='--',color='black', linewidth=0.5)
    ax1.plot([0,Ancho], [1,1],label= 'Gradiente',linestyle='--',color='m', linewidth=0.5)
    ax1.plot([0,Ancho], [(Altura-fl+1)/2,(Altura-fl+1)/2],linestyle='--',color='black', linewidth=0.5)
else: 
    ax1.plot([Ancho/2,  Ancho/2],[0,Altura],linestyle='--',color='black', linewidth=0.5)
    ax1.plot([0,Ancho], [1.5,1.5],label= 'Gradiente',linestyle='--',color='m', linewidth=0.5)
    ax1.plot([0,Ancho], [(Altura-fl+1)/2,(Altura-fl+1)/2],linestyle='--',color='black', linewidth=0.5)   


#Taladro de alivio equivalente
plt.scatter(Ancho/2, (Altura-fl+1)/2,facecolors='none', edgecolors='black', s=300)  
plt.legend()
plt.title('MALLA DE PERFORACIÓN PRE-CORTE',fontsize=20)
# Agregar texto en la figura
plt.text(0, Altura-0.2, f'Numero de taladros de alivio={NB}\nDiametro equivalente={Dv*1000:.2f} mm\nGSI={GSI}\nRQD={RQD}', fontsize=10)
pdf_filename = 'documento.pdf'
with PdfPages(pdf_filename) as pdf:
    pdf.savefig(fig1)  
    plt.close(fig1)

    # Unidades correspondientes a cada parámetro
    Unidades = ['m', 'm', 'm', 'm', 'kg/m', '[]']
    
    # Inicializar el diccionario con 'Descripción de Parametros'
    Data_Cuadradores = {
        'Descripción de Parametros': ['Burden', 'Espaciamiento', 'Taco', 'Longitud de carga de columna','Concentracion de carga lineal','Numero de cartuchos'],
    }
    
    # Crear dinámicamente los cuadrantes y las unidades
    for i in range(len(List_BP)):
        cuadrante_key = f'Cuadrante {i + 1}'  # Nombre de la clave del cuadrante (Cuadrante 1, Cuadrante 2, ...)
        
        # Crear una lista de valores del cuadrante (sin unidades por ahora)
        cuadrante_values = [
            List_BP[i], List_A[i], List_T[i], List_LC[i], List_q[i], List_NC[i]
        ]
        
        # Agregar el cuadrante al diccionario
        Data_Cuadradores[cuadrante_key] = cuadrante_values
    
    # Agregar las unidades como la última columna
    Data_Cuadradores['Unidades'] = Unidades

    Data_Arrastres = {
        'Descripción de Parametros': ['Burden', 'Espaciamiento de esquinas', 'Espaciamiento de taladros intermedios', 'Número de taladros','Taco','Longitud de carga de fondo','Concentracion de carga lineal en el fondo','Número de cartuchos en el fondo','Longitud de carga de columna','Concentracion de carga lineal en la columna','Número de cartuchos en la columna'],
        'Parametros': [BPA, STA, SPA, NTA,TA,HFA,qfa,NFA,HCA,qca,NCA],
        'Unidades': ['m', 'm', 'm', '[]', 'm', 'm', 'kg/m', '[]', 'm', 'kg/m', '[]']
    }
    
    Data_Corona = {
        'Descripción de Parametros': ['Burden', 'Espaciamiento', 'Numero de taladros', 'Taco', 'Longitud de Columna','Concentracion de carga lineal','Numero de cartuchos','Numero de cartuchos cebado'],
        'Parametros': [BPC, SC, NTC, TC,LCC,qce,NCC-1,1],
        'Unidades': ['m', 'm','[]', 'm', 'm','kg/m','[]','[]']
    }
    Data_Hastiales = {
        'Descripción de Parametros': ['Burden', 'Espaciamiento' , 'Número de taladros','Taco','Longitud de Columna','Concentracion de carga lineal','Numero de cartuchos','Numero de cartuchos cebado'],
        'Parametros': [BPH, SH, 2*(NTH-1), TH,LCH,qh,NCH-1,1],
        'Unidades': ['m', 'm', '[]', 'm', 'm', 'kg/m', '[]','[]']
    }
      
    tabla1 = pd.DataFrame(Data_Cuadradores)
    tabla2 = pd.DataFrame(Data_Arrastres)
    tabla3 = pd.DataFrame(Data_Corona)
    tabla4 = pd.DataFrame(Data_Hastiales)
    tabla1 = tabla1.round(2)
    tabla2 = tabla2.round(2)
    tabla3 = tabla3.round(2)
    tabla4 = tabla4.round(2)
    
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.axis('tight')
    ax.axis('off')
    ax.set_title('SECCIÓN DE CORTE', fontsize=14)
    tabla1=ax.table(cellText=tabla1.values, colLabels=tabla1.columns, cellLoc='center', loc='center')
    tabla1.auto_set_font_size(False)
    tabla1.set_fontsize(6)
    pdf.savefig(fig)
    plt.close(fig)

    
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.axis('tight')
    ax.axis('off')
    ax.set_title('SECCIÓN DE ARRASTRES', fontsize=14)
    tabla2=ax.table(cellText=tabla2.values, colLabels=tabla2.columns, cellLoc='center', loc='center')
    tabla2.auto_set_font_size(False)
    tabla2.set_fontsize(6)
    pdf.savefig(fig)
    plt.close(fig)

    
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.axis('tight')
    ax.axis('off')
    ax.set_title('SECCIÓN DE CORONA', fontsize=14)
    tabla3=ax.table(cellText=tabla3.values, colLabels=tabla3.columns, cellLoc='center', loc='center')
    tabla3.auto_set_font_size(False)
    tabla3.set_fontsize(6)
    pdf.savefig(fig)
    plt.close(fig)

    
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.axis('tight')
    ax.axis('off')
    ax.set_title('SECCIÓN DE HASTIALES', fontsize=14)
    tabla4=ax.table(cellText=tabla4.values, colLabels=tabla4.columns, cellLoc='center', loc='center')
    tabla4.auto_set_font_size(False)
    tabla4.set_fontsize(6)
    pdf.savefig(fig)
    plt.close(fig)

import os
os.startfile(pdf_filename)  



```
