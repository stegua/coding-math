#!/usr/bin/env python
# coding: utf-8

# # 2. Programmare funzioni
# **ULTIMA MODIFICA: 13.10.2022**

# ## 2.1 Calcolo della radice quadrata di un numero
# Le procedure che abbiamo introdotto sino ad ora sono essenzialmente delle **funzioni matematiche** che specificano un valore di *output* che viene calcolato a partire da uno o più parametri di *input*. A differenze delle funzioni definite in matematica "*teorica*", le procedure definite al calcolatore devono essere anche **efficienti**, ovvero devono terminare la loro esecuzione in tempo breve. Proviamo a vedere un semplice esempio pratico di cosa vuol dire avere una procedura efficiente.
# 
# Si consideri la definizione matematica seguente:
# 
# $$\sqrt{x} = y \quad \mbox{ se e solo se }\quad y \geq 0 \mbox{ e } y^2 = x$$
# 
# Queste definizione è senz'altro corretta da un punto di vista matematico. Potremmo usare questa definizione per controllare se un dato numero $y$, esso sia la radice quadrata di un altro numero $x$. Tuttavia, questa definizione non descrive una procedura per calcolare la radice quadrata di $x$.
# 
# Per poter calcolare la radice quadrata di un numero abbiamo bisogno di un **Algoritmo** che viene *implementato* con una o più procedure di supporto.
# 
# In questa sezione, usiamo l'esempio del calcolo della radice quadrata per mostrare tre metodi fondamentali per risolvere dei problemi:
# 
# 1. Ricerca di una soluzione per **Enumerazione Esaustiva** (ovvero per semplice *forza bruta*).
# 2. Ricerca di una soluzione usando un **Metodo di Bisezione**: lo spazio di ricerca viene ripetutamente ristretto, sfruttando delle semplici assunzioni di ordinamento sullo spazio di ricerca.
# 3. Ricerca di una soluzione con un **metodo dedicato** (ovvero il *medoto di Newton*) che sfrutta la struttura del problema che vogliamo risolvere per ottenere un algoritmo efficiente.
# 
# Prima di procedere, diamo sotto una definzione formale di *Algoritmo*:
# 
# **TODO: aggiungi definizione formale**.

# ### 2.1.1 Enumerazione Esaustiva
# Se ci limitiamo a considerare i numeri interi, potremmo utilizzare la definizione precedente per trovare la radice quadrata di un numero intero positivo attraverso una **enumerazione esaustiva**: per trovare la radice quadrata di $x$, possiamo provare tutti i numeri da $x$ a 1, e verificare ogni volta se il numero "tentativo" sia il quadrato dell'altro. 
# 
# **ESERCIZIO 2.1**: Scrivere una procedura (funzione) che prende in input un numero intero maggiore o uguale a 1, e prova tutti i numeri da $x$ a 1. Se la funzione trova la radice quadrata esatta la restituisce, altrimenti restituisce `nan` (ovvero, *not a number*).

# In[1]:


# Radice intera di un numero naturale per enumerazione
def SqrtInt(x):
    # Controllo sui dati di input
    if type(x) != int or x < 0:
        print('ERRORE: la funzione prende in input solo numeri interi positivi')
        return float('nan')
        
    # Definisco una funzione interna, in modo che la funzione che "espongo"
    # prende un singolo parametro di input
    def Rec(y):
        if y < 0:
            return -1
        if y*y == x:
            return y
        return Rec(y-1)
    
    # NOTA: per dimezzare il numero di chiamate ricorsive, posso trattare a 
    #       parte il caso x==1, e per x>=2, posso dividere x per 2
    if x == 1:
        return 1
    
    # La radice intera di un numero intero x è minore di x/2
    return Rec(x//2)
    
print('radice di 16', SqrtInt(16))
print('radice di 17', SqrtInt(17))
print('radice di 2.5', SqrtInt(2.5))


# Si osservi che la stringa `nan` può essere convertita ad un dato di tipo `float`.

# In[2]:


type('nan')


# In[3]:


type(float('nan'))


# **DOMANDE:** 
# 1. Come fare per trovare la radice quadrata di un numero reale positivo? 
# 2. Cosa vuol dire che due numeri reali sono **uguali**?
# 3. Come viene valutata l'espressione logica: $$\frac{1}{10}+\frac{1}{10}+\frac{1}{10} = \frac{3}{10}$$

# In[4]:


1/10+1/10+1/10 == 3/10


# **ATTENZIONE**: Bisogna fare molta attenzione quando si **confrontano** i numeri reali al calcolatore.
# 
# Rivediamo quindi leggermente la definizione di radice quadrata, introducendo il concetto di **tolleranza numerica**. In pratica, cerchiamo un numero reale positivo tale che
# 
# $$\sqrt{x} \simeq y \quad \mbox{ tale che } \quad |y^2 - x| < \epsilon,  \quad y \geq 0, \epsilon>0 $$
# 
# dove $\epsilon$ è una costante molto piccola, per esempio $\epsilon=10^{-7}$.
# 
# **DOMANDA:** Quante operazioni aritmetiche e logiche dobbiamo eseguire prima di ottenere un risultato?

# ### 2.1.2 Ricerca per bisezione
# Potremmo cercare di migliorare la procedura di enumerazione esaustiva assumendo che i numeri che dobbiamo controllare siano ordinati in ordine crescente (o decrescente). In questo modo, potremmo evitare di controllare tutti i numeri, uno alla volta, e potremmo cercare di fare dei "salti" sfruttando la proprietà che i numeri sono ordinati.
# 
# **ESERCIZIO 2.2**: Scrivere una procedura che, per trovare la radice quadrata di un numero, ogni volta divide l'intervallo di ricerca in due parti uguali, e continua ad esplorare solo la parte in cui effettivamente si può trovare la radice cercata.

# In[5]:


# Radice di un numero positivo per bisezione
def RadiceBisezione(x, eps=1e-7, verbose=False):
    # NOTA: usando la notazione per "eps=", stiamo assegnando un valore di
    #       default al secondo parametro formale di input
    
    if type(x) != float and type(x) != int:
        print('ERRORE: la funzione prende in input solo dati numerici di tipo int o float')
        return float('nan')
    
    if x < 0:
        print('ERRORE: la funzione prende in input solo numeri positivi')
        return float('nan')
        
    def Rec(a, b):
        # Nuovo valore tentativo per la soluzione
        y = (a+b)/2
        
        # Stampo a video il progresso dell'intervallo e dell'errore        
        # NOTA BENE: la stampa a video serve solo a scopo didattico.
        #            una volta che si è verificata la correttezza dell'implementazione
        #            la stampa a video va rimossa, oppure inserita 
        #            come parametro opzionale (come fatto in questo caso)
        if verbose:
            print(y, a, b, abs(b - a)/2)
        
        # Errore teorico del metodo per bisezione
        if abs(b - a)/2 < eps:
            return y        
        
        y2 = y*y
        
        # Errore sul quadrato del numero
        if abs(y2 - x) < eps:
            return y
        
        # Devo decidere su quale intervallo continuare la ricerca per bisezione
        if y2 < x:
            return Rec(y, b)        
        
        return Rec(a, y)
    
    # Ricordarsi di chiamare almeno una volta la funzione ricorsiva interna
    return Rec(0, x)

# Valore di defualt di eps
print(RadiceBisezione(2))


# In[6]:


# Provare con diversi valori di eps
print(RadiceBisezione(2, 1e-4))


# ### 2.1.3 Il metodo di Newton
# Il metodo numerico più usato per calcolare la radice quadrata è il metodo di approssimazioni successive introdotto da Newton. Il metodo consiste nel trovare la soluzione attraverso aggiustamenti successivi di una soluzione tentativo: se abbiamo un valore $y$ che rappresenta il valore tentativo della radice quadrata di un altro numero $x$  possiamo ottenere una approssimazione più accurata calcolando la media tra $y$ e $x/y$. 
# 
# Il metodo di Newtnon consiste quindi di partire da un $y_0>0$ e ad ogni iterazione di calcolare:
# 
# $$y_{i+1} = \frac{y_i + \frac{x}{y_i}}{2}$$
# 
# **ESEMPIO:** Ricerca della radice quadrata di 2.
# 
# | Valore Tentativo $y$ | Quoziente $x/y$ | Media tra $y$ e $x/y$ |
# |    :--:   |    :--:    |    :--:    |
# |  1  |  2/1  | (1+2)/2=1.5 | 
# |  1.5  |  2/1.5=1.3333  | (1.3333+1.5)/2=1.4167 |
# |  1.4167  |  2/1.4167=1.4118  | (1.4118 + 1.4167)/2=1.4142 |
# | 1.4142 | ... | ... |
# 
# **ESERCIZIO 2.3**: Scrivere una o più procedure per trovare la radice quadrata di un numero, utilizzando il metodo di Newton scritto sopra.

# In[7]:


def RadiceNewton(x, eps=1e-07, verbose=False):
    # Controllo sui dati di input
    if type(x) != float and type(x) != int:
        print('ERRORE: la funzione prende in input solo dati numerici di tipo int o float')
        return float('nan')
    
    if x < 0:
        print('ERRORE: la funzione prende in input solo numeri positivi')
        return float('nan')
        
    def Rec(y):  
        # Calcola il prossimo valore tentativo usando la formula di Newton
        z = 0.5*(y + x/y)
        
        # Stampa a video il progresso della ricorsione (se richiesto)
        if verbose:
            print(z, abs(z*z - x))
        
        # Analisi dell'errore come spiegato sotto nella Sezione 2.1.4
        if abs(z - y) < eps:
            return z
        
        return Rec(z)
    
    # NOTA: attenzione, si deve trattare a parte il caso x==0
    if x == 0:
        return 0
    return Rec(x)

print(RadiceNewton(2, 1e-13, verbose=True))


# In[8]:


print(RadiceNewton(0.5, 1e-13))


# In[9]:


print(RadiceNewton(0.5, 1e-13)*RadiceNewton(0.5, 1e-13))


# **DOMANDA:** è possibile trovare un criterio di arresto alternativo, che sia espresso in funzione dell'errore commesso nel calcolo della radice quadrata? (Ovviamente senza conoscere il valore esatto della radice quadrata...)

# ### 2.1.4 Errore di Approssimazione con il metodo di Newton
# Studiamo ora come stimare l'errore del metodo di Newton, senza conoscere il valore esatto di $\sqrt{x}$. Chiamiamo $E_i$ l'errore di approssimazione commesso al passo $i$-esimo:
# 
# $$E_i = y_i - \sqrt{x}$$
# 
# da cui possiamo anche ricavare
# 
# $$y_i = \sqrt{x} + E_i$$
# 
# L'errore che avremo alla prossima iterazione, sarà pari a
# 
# $$E_{i+1} = y_{i+1} - \sqrt{x} = \frac{y_i + \frac{x}{y_i}}{2} - \sqrt{x} = \frac{y_i^2 - 2 y_i \sqrt{x_i} +x}{2 y_i} = \frac{(y_i - \sqrt{x})^2}{2 y_i}= \frac{E_i^2}{2 y_i}$$
# 
# Facendo un po' di conti a partire dall'espressione precedente, si arriva a far vedere che 
# 
# $$E_{i+1} = \frac{E_i^2}{2 y_i} \geq 0$$
# 
# In pratica, dopo il primo tentativo $y_0 > 0$, tutti gli errori successivi saranno sempre positivi, quindi e l'errore ad ogni iterazione diventa sempre più piccolo, in quanto
# 
# $$E_i = y_i - \sqrt{x} < y_i \quad \mbox{ e quindi } 0 \leq \frac{E_i}{y_i} <1$$
# 
# e inoltre
# 
# $$E_{i+1} = \frac{E_i^2}{2 y_i} = \frac{E_i}{y_i} \times \frac{E_i}{2} < \frac{E_i}{2}$$

# Riassumendo, abbiamo mostrato che l'errore diventa sempre più piccolo in quanto
# 
# $$0 \leq E_{i+1} < \frac{E_i}{2} < E_i.$$
# 
# Vediamo ora come possiamo usare le espressioni precedenti per ottenere un criterio di arresto usando una stima sull'errore. Dalle relazioni precedenti abbiamo che
# 
# $$0 \leq y_{i+1} - \sqrt{x} < y_{i} - \sqrt{x}$$
# 
# da cui 
# 
# $$\sqrt{x} \leq y_{i+1} < y_{i}$$
# 
# **TODO: aggiungi figura**

# Se riprendiamo la definzione di errore ad una data iterazione $i$, abbiamo che 
# 
# $$E_i = y_i - \sqrt{x}= y_i - y_{i+1} + y_{i+1} -\sqrt{x} = (y_i - y_{i+1}) + E_{i+1} < (y_i - y_{i+1}) + \frac{E_{i}}{2}$$
# 
# ovvero
# 
# $$0 \leq \frac{E_i}{2} < y_i - y_{i+1}.$$
# 
# In pratica, se si vuole calcolare la radice quadrata di un numero reale positivo con un margine di errore minore di $\epsilon > 0$, basterà verificare la condizione:
# 
# $$y_i - y_{i+1} < \epsilon.$$

# ### 2.1.5 Confronto tra le tre funzioni trovate
# Possiamo provare a fare un piccolo confronto tra le tre funzioni trovate in termini di efficienza, andando a contare, per esempio, quante volte è stata chiamata la funzione ricorsiva. Per poterlo fare, si deve aggiungere un parametro formale che viene incrementato di uno ogni volta che si effettua una chiamata ricorsiva. Tale valore può essere stampato a video prima di restituire il valore finale.
# 
# **ESERCIZIO 2.4**: Modificare le procedure precedenti per contare il numero di chiamate ricorsive con le tre procedure precedenti: 
# 
# 1. Enumerazione Esaustiva
# 2. Metodo di Bisezione
# 3. Metodo di Newton
