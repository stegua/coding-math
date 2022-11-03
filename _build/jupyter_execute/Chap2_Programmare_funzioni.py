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

# ## 2.2 Procedure, funzioni e processi di calcolo
# Una procedura definisce uno "schema" di evoluzione *locale* di un processo computazionale. La procedura specifica in ogni fase del processo, come il processo stesso viene eseguito a partire dalla fase precedente. È interessante studiare il comportamento *globale* di un processo la cui evoluzione locale è stata specificata da una procedura. In generale, andare a studiare questo comportamento è molto complicato, ma in alcuni casi semplici si possono identificare degli schemi ricorrenti (in inglese **pattern**).
# 
# Proviamo ora a studiare la "forma" che prendono alcuni processi generati da procedure molto semplici. Studieremo anche velocemente la velocità con cui questi processi consumano le due risorse di calcolo fondamentali:
# 
# 1. IL TEMPO
# 2. LA MEMORIA
# 
# Come nelle lezioni precedenti, le procedure che consideriamo sono semplici. Il loro ruolo è lo stesso ricoperto dai *test patterns* in [fotografia](http://www.bealecorner.org/red/test-patterns/): uno schema prototipale ipersemplificato, piuttosto che un caso d'uso reale.

# ### 2.2.1 Ricorsione lineare e iterazione lineare
# Si consideri la funzione fattoriale definita come segue: si definisce il *fattoriale* di un numero naturale $n$, indicato con $n!$, il prodotto dei numeri naturali uguali o minori a $n$, ovvero:
# 
# $$n! = \prod_{k=1}^n k = 1 \cdot 2 \cdot 3 \cdot \cdot \cdot (n-2) \cdot (n-1) \cdot n$$
# 
# Esistono molti modi di calcolare il fattoriale di un numero naturale. Un modo è di osservare che $n!$ è uguale ad $n$ volte $(n-1)!$ per qualsiasi intero $n$:
# 
# $$ n! = n \cdot [(n-1)\cdot(n-2)\cdots 3 \cdot 2 \cdot 1] = n \cdot (n-1)!$$
# 
# In questo modo possiamo calcolare $n!$ calcolando **prima** $(n-1)!$ e moltiplicando **poi** il risultato per $n$. Se aggiungiamo la definizione che $1!$ è uguale a 1, possiamo definire la procedura seguente:

# In[10]:


def Fact(n):
    if n == 1:
        return 1
    else:
        return n*Fact(n-1)
    
print(Fact(5))


# Se usiamo il *substitution model* per valutare la procedure per $5!$, otteniamo lo schema seguente:
# 
# ```
# Fattoriale(5)
# 5 * Fattoriale(4)
# 5 * (4 * Fattoriale(3))
# 5 * (4 * (3 * Fattoriale(2)))
# 5 * (4 * (3 * (2 * Fattoriale(1))))
# 5 * (4 * (3 * (2 * 1)))
# 5 * (4 * (3 * 2)) 
# 5 * (4 * 6) 
# 5 * 24
# 120
# ```
# 
# Ora, questa procedura è corretta, in quanto produce il risultato richiesto (si può dimostrare formalmente la correttezza, ma non è lo scopo di questa capitolo).
# 
# Possiamo tuttavia calcolare il fattoriale di un numero usando un approccio diverso. Potremmo descrivere una regola per calcolare il fattoriale di un numero naturale $n$ specificando che prima moltiplichiamo 1 per 2, poi moltiplichiamo il risultato per 3, poi il risultato per 4, e cosi via, sino a raggiungere il valore di $n$. 
# 
# Più formalmente, manteniamo una variabile per il prodotto corrente (chiamata in gergo un **accumulator**), insieme a una variabile che "tiene il conto" da 1 a $n$ (un **counter**). Possiamo descrivere il processo di calcolo dicendo che l'accumulator e il counter aggiornano il loro stato "contemporaneamente" ad ogni fase del processo di calcolo:
# 
# ```
# accumulator <- counter * accumulator
# counter <- counter + 1
# ```
# 
# Chiaramente, sia l'accumulator che il counter sono inizializzati a 1.
# 
# Data questa regola per calcolare $n!$, possiamo scrivere le due procedure seguenti:

# In[11]:


def FactI(x):
    def R(acc, count):
        print('R', acc, count)
        if count == x:
            return acc*x
        return R(acc * count, count+1)
    
    print('Fact', x)
    return R(1, 1)


# In[12]:


print(FactI(5))


# Come prima, se usiamo il *substitution model* possiamo visualizzare il processo di calcolare $5!$ usando la procedura `FactorialI`, come segue:
# 
# ```
# FactorialI(5)
# Rec(1, 1, 5)
# Rec(1, 2, 5)
# Rec(2, 3, 5)
# Rec(6, 4, 5)
# Rec(24, 5, 5)
# Rec(120, 6, 5)
# 120
# ```
# 
# Si provi a confrontare questo schema di calcolo rispetto al precedente.
# 
# A prima vista non sembrano troppo diversi: entrambi calcolano $5!$. Entrambe le procedure richiedono un numero di passi proporzionale al numero $n$. Entrambe le procedure eseguono la stessa sequenza di prodotti, ottenendo gli stessi prodotti parziali. Tuttavia, visualizzando l'evoluzione del processo di calcolo, otteniamo chiaramente una "forma" (uno schema, un *pattern*) diversa per i due processi.
# 
# Si consideri il primo processo. Procedendo con il modello sostitutivo, otteniamo prima una sequenza di espansioni, seguita da una sequenza di contrazioni. Le espansioni si ottengono mentre il processo costruisce una sequenza di operazioni **deferred** (in questo caso la sequenza di moltiplicazioni). Le contrazioni avvengono quando le operazioni **deferred** sono effettivamente calcolate. 
# 
# Questo tipo di processo, caratterizzato da una sequenza di operazioni deffered, viene chiamato **PROCESSO RICORSIVO**. 
# 
# Questo processo richiede che l'interprete tenga memoria delle operazioni che deve eseguire dopo, durante la sequenza di contrazioni. Nel caso del calcolo di $n!$, la lunghezza della sequenza di operazioni deferred, e quindi la quantità di informazioni da mantenere in memoria, è lineare nell'input $n$. Si parla quindi di **PROCESSO RICORSIVO LINEARE**.
# 
# Al contrario, il secondo processo, quello della procedura `FactorialI(n)` non si espande e non si contrae. Ad ogni passo, gli unici valori di cui dobbiamo tener traccia sono le tre variabili `accumulator`, `counter`, e `n`. Questo viene chiamato un **PROCESSO ITERATIVO**. In generale, un processo iterativo può essere descritto da un numero finito di *variabili di stato*, insieme con una regola che descrive come le variabili di stato dovrebbero essere aggiornate quando il processo passo da uno stato al successivo, e dovrebbe avere un test d'arresto (i.e., una espressione condizionale `if`) che specifica sotto quali condizioni il processo dovrebbe terminare. Nel calcolare $n!$ il numero di passo richiesto cresce linearmente con $n$. Tale processo viene chiamato un **PROCESSO ITERATIVO LINEARE** (in inglese vengono chiamate funzioni **tail-recursive**).
# 
# ### IMPORTANTE
# Nel confrontare i due tipi di processi, si deve fare attenzione a non confondere il concetto di *processo ricorsivo* con quello di *procedura e/o funzione ricorsiva*. 
# 
# Quando descriviamo una procedura come ricorsiva, ci stiamo riferendo al fatto di definire una funzione che richiama se stessa.
# 
# Tuttavia, quando descriviamo un processo che segue uno schema linearmente ricorsivo, stiamo parlando di come il processo evolve, non della sintassi che viene usata per scrivere la procedura. Può creare confusione il dire che una procedura ricorsiva, come ad esempio `FactorialI(n)`, genera un processo iterativo. In ogni caso il processo è iterativo: il suo stato è descritto completamente dalle sue tre variabili di stato, e l'interprete deve tener traccia solo di quelle tre variabili per poter eseguire il processo.
# 
# Il motivo principale che genera questa confusione, è che l'implementazione attuale di molti di linguaggi di programmazione comuni (C, Java, e lo stesso Python) sono implementati in modo tale che l'esecuzione di ogni chiamata ricorsiva consuma una quantità di memoria che cresce linearmente con il numero di chiamate ricorsive alla stessa procedura, anche se il processo stesso è iterativo.
# L'implementazione di altri linguaggi di programmazione (per esempio, il LISP e Haskell) è in grado di distinguere i processi ricorsivi e i processi iterativi, che risultano in grado di ottimizzare il processo di calcolo usando una quantità di memoria che dipende solo dal numero di variabili di stato. 
# 
# ### 2.2.2 Ricorsione ad albero
# Un altro schema ricorrente di calcolo è la ricorsione ad albero. Si consideri per esempio la successione dei numeri di Fibonacci, in cui ogni numero è la somma dei due numeri precedenti:
# 
# $$0, 1, 1, 2, 3, 5, 8, 13, 21, ...$$
# 
# ![Mole Antonelliana](images/mole.jpg)
# 
# In generale, l'ennessimo numero di Fibonacci può essere definito dalla regola seguente:
# 
# $$Fib(n) = \left\{ \begin{array}{ll} 
# 0 & \mbox{if } n = 0 \\  
# 1 & \mbox{if } n = 1  \\
# Fib(n-1) + Fib(n-2) & \mbox{altrimenti} \end{array} \right.$$
# 
# **ESERCIZIO**: Tradurre questa definizione in una procedura ricorsiva per calcolare l'ennesimo numero di Fibonacci.

# In[13]:


def Fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return Fib(n-1) + Fib(n-2)


# In[14]:


Fib(5)


# Si consideri lo schema di calcolo di tale funzione (FARE ALLA LAVAGNA). Si noti che il processo stesso evolve come un albero: ad ogni nodo il processo di ramifica in due sottoprocessi, tranne che ai nodi foglia. Questo è dovuto al fatto che la procedura chiama se stessa due volte per ogni invocazione.
# 
# Questa procedura per calcolare i numeri di Fibonacci è un ottimo esempio di struttura ad albero, ma è un pessimo modo di calcolare i numeri di Fibonacci. Per rendersi conto di quanto sia inefficiente, si consideri che questo processo usa un numero di passi che cresce esponenzialmente con l'input. Tuttavia, lo spazio richiesto cresce solo linearmente con l'input, in quanto dobbiamo tener traccia dei nodi al di sotto del nodo corrente a qualsiasi momento del processo. 
# In generale, il numero di passi richiesto da un processo ricorsivo ad albero sarà proporzionale al numero di nodi dell'albero, mentre lo spazio richiesto sarà proporzionale alla profondità massima dell'albero.
# 
# Il calcolo dei numeri di Fibonacci può essere formulato anche come un processo iterativo. L'idea è di usare una coppia di numeri $a$ e $b$, inizializzati con $Fib(1)=1$ e $Fib(0)=0$, e di applicare ripetutamente le **trasformazioni simultanee**:
# 
# ```
# a <- a + b
# b <- a
# ```
# 
# Non dovrebbe essere complicato realizzare che dopo aver applicato queste trasformazioni $n$ volte, $a$ e $b$ avranno i valori $Fib(n+1)$ e $Fib(n)$.
# 
# **ESERCIZIO**: Scrivere una procedura che calcoli i numeri di Fibonacci usando un processo iterativo.
# 

# ### 2.2.3 Calcolo di elevamento a potenza
# Si consideri il problema di calcolare l'esponenziale di un numero dato. Vorremo avere una procedura che prende come argomenti la base $b$ e un intero positivo $n$, e calcola il valore $b^n$. Un modo possibile di procedere è utilizzando la definizione ricorsiva:
# 
# $$\begin{array}{ll}b^n = b \cdot b^{n-1}\\
# b^0 = 1\end{array}$$
# 
# **ESERCIZIO**: Scrivere una procedura che applichi direttamente la definizione precedente, tramite un processo ricorsivo lineare.

# In[15]:


# COMPLETARE


# **ESERCIZIO**: Scrivere una procedura che esegue l'elevamento a potenza usando un processo iterativo lineare.

# In[16]:


# COMPLETARE


# ### 2.2.4 Massimo Comun Divisore
# Il Massimo Comun Divisore (MCD) di due numeri intero $a$ e $b$ è definito come il più grande numero intero che divide sia $a$ che $b$ senza resto. Per esempio, il massimo comun divisore di 16 e 28 è il numero 4. Esiste un metodo famoso per calcolare tale numero: l'**algoritmo di Euclide**.
# 
# L'idea dell'algoritmo si basa sull'osservazione che, se $r$ è il resto di quando $a$ è diviso per $b$, allora i divisori comuni di $a$ e $b$ sono esattamente esattamente gli stessi divisori comuni tra $b$ e $r$. Quindi possiamo usare l'equazione:
# 
# $$MCD(a,b) = MCD(n,r)$$
# 
# per ridurre il problema di trovare i divisori comuni calcolando il MCD tra coppie di numeri interi via via più piccoli. Per esempio:
# 
# ```
# MCD(206, 4) = MCD(40, 6)
#             = MCD(6,4)
#             = MCD(4,2)
#             = MCD(2,0)
#             = 2
# ```
# 
# **ESERCIZIO**: Scrivere una procedura che calcola il massimo comun divisore usando l'algoritmo di Euclide (per calcolare il resto di una divisione tra due numeri interi si usa l'operatore modulo `%`).

# In[17]:


# COMPLETARE


# **NOTA:** Per le soluzioni degli esercizi, consultare il sito del corso.

# 
