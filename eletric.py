import matplotlib.pyplot as plt
import math
import numpy as np


#declarando Formulas


#CA Normal
def v_1(t, volts, hertz):
    return volts * np.sin(((math.tau * hertz) * t))

#diodo padrao retificador
def diodo(t, volts, hertz):
    return  ((volts * np.sin(((math.tau * hertz) * t))) + abs((volts * np.sin(((math.tau * hertz) * t))))) / 2

#diodo Losangulo
def diodo_losango(t, volts, hertz):
    return abs((volts * np.sin(((math.tau * hertz) * t)))) 

#diodo zenner
def diodo_zenner(t,volts,hertz,v_zenner):
    return (((((volts * np.sin(((math.tau * hertz) * t))) + abs((volts * np.sin(((math.tau * hertz) * t))))) / 2) + v_zenner) - abs((((volts * np.sin(((math.tau * hertz) * t))) + abs((volts * np.sin(((math.tau * hertz) * t))))) / 2) - v_zenner)) / 2





#declarando functions


def CA_normal(volts, hertz):    
    #recomendar 12 volts, 1 hertz
    t_valor = np.linspace(-3, 3, 1000) #X
    v_valor = v_1(t_valor, volts, hertz)
    
    plt.plot(t_valor,v_valor, label="V(t)")
    plt.title("CA Normal, 9 Volts, 1 Hertz")
    plt.xlabel("tempo(s)")
    plt.ylabel("Volts/s")
    plt.axhline(0, color='black')
    plt.axvline(0, color='black')
    plt.grid(True)
    plt.legend()
    plt.show()


def diodo_simples(volts, hertz):    
    #recomendar 12 volts, 1 hertz
    t_valor = np.linspace(-3, 3, 1000) #X
    v_valor = diodo(t_valor, volts, hertz)
    
    plt.plot(t_valor,v_valor, label="V(t)")
    plt.title("CA Normal, 9 Volts, 1 Hertz")
    plt.xlabel("tempo(s)")
    plt.ylabel("Volts/s")
    plt.axhline(0, color='black')
    plt.axvline(0, color='black')
    plt.grid(True)
    plt.legend()
    plt.show()

def diodo_retificador_completo(volts, hertz):    
    #recomendar 8 Volts, 1 Hertz
    t_valor = np.linspace(-3, 3, 1000) #X
    v_valor = diodo_losango(t_valor, volts, hertz)
    
    plt.plot(t_valor,v_valor, label="V(t)")
    plt.title("CA Normal, 9 Volts, 1 Hertz")
    plt.xlabel("tempo(s)")
    plt.ylabel("Volts/s")
    plt.axhline(0, color='black')
    plt.axvline(0, color='black')
    plt.grid(True)
    plt.legend()
    plt.show()

def diodo_zeuner(volts, hertz, v_zenner):    
    #recomendar 12 volts, 1 hertz
    t_valor = np.linspace(-3, 3, 1000) #X
    v_valor = diodo_zenner(t_valor, volts, hertz, v_zenner)
    
    plt.plot(t_valor,v_valor, label="V(t)")
    plt.title("CA Normal, 9 Volts, 1 Hertz")
    plt.xlabel("tempo(s)")
    plt.ylabel("Volts/s")
    plt.axhline(0, color='black')
    plt.axvline(0, color='black')
    plt.grid(True)
    plt.legend()
    plt.show()



#executar

diodo_zeuner(12, 1, 10)