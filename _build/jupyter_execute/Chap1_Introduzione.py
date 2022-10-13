#!/usr/bin/env python
# coding: utf-8

# # 1. Elementi di Programmazione
# 
# Storicamente, il primo linguaggio di programmazione è stato inventato per istruire una macchina ad eseguire dei calcoli in modo automatico. Ad oggi, viene riconosciuto che un linguaggio di programmazione serve prima di tutto per organizzare le nostre idee su come quei calcoli devono essere svolti da una macchina. Per questo, nella scelta di un linguaggio di programmazione, si deve tener presente quali siano gli strumenti che vengono offerti dal linguaggio per formare, a partire da poche idee semplici, delle idee più complesse.
# 
# Ogni linguaggio di programmazione dovrebbe avere almeno tre elementi per poter permettere di raggiungere l'obiettivo di comporre poche idee semplici in idee più complesse. I tre elementi sono:
# 
# 1. Le **espressioni primitive** che rappresentano le entità più semplici del linguaggio.
# 
# 2. I metodi per **comporre** gli elementi primitivi in elementi derivati.
# 
# 3. I metodi per **astrarre** concetti primitivi in modo che gli elementi derivati possano essere utilizzati a loro volta come elementi primitivi di entità ancora più complesse.
# 
# In un linguaggio di programmazione, le espressioni primitive che possiamo usare sono le *espressioni logiche* e le *espressioni aritmetiche*. Inoltre, si possono usare due tipi di elementi primitive: le **PROCEDURE** e i **DATI**. In modo informale, possiamo definire i **dati** come gli oggetti che vorremmo manipolare, e le **procedure** come la descrizione di regole per manipolare questi dati. Una procedura *implementa* un algoritmo, per trasformare un dato di input in un particolare output.

# ## 1.1 Dati e procedure numeriche
# Iniziamo a illustrare sotto qualche semplice espressione valutata dall'interprete di Python: se digitiamo alla tastiera una **espressione**, l'interprete risponde **valutando** tale espressione. Per esempio se digitiamo la sequenza di caratteri 345 e poi premiamo la combinazione di tasti `shift + enter`, l'interprete valuta l'espressione che abbiamo appena scritto:

# In[1]:


345


# In[2]:


type(345)


# In questo esempio, la sequenza di caratteri *3,4,5* è stato convertita nel numero intero 345, come si può verificare utilizzando la funzione primitiva `type(x)`, che stampa a video il tipo di dato del valore di input `x`. Se avessimo racchiuso la sequenza di caratteri *3,4,5*, l'interprete di Python avrebbe convertito la sequenza in una **stringa** di caratteri, ovvero un dato primitivo di tipo `str`.

# In[3]:


"345"


# In[4]:


type('345')


# Utilizzando le procedure primitive che corrispondono agli operatori aritmetici fondamentali, possiamo comporre delle semplici espressioni aritmetiche che permettono di manipolare dei dati primitivi di tipo numerico (alla pari di qualsiasi calcolatrice). Per esempio:

# In[5]:


339 + 6


# In[6]:


345 - 6


# In[7]:


2.7 / 12.1


# In[8]:


type(345 - 12/6)


# In[9]:


345 % 7


# In[10]:


3//2


# In[11]:


7 + (2*49)
49 * 2 + 7


# In queste semplici espressioni numeriche, è stata implicitamente usata una notazione **postfix**, in cui l'operatore appare dopo il primo operando.
# 
# Importando e utilizzando la libreria di Python `operator` è possibile esprimere le stesse espressioni in notazione **prefix**: prima si specifica l'*operatore* (ovvero la procedura di calcolo corrispondente che si vuole richiamare), e poi si specificano gli *operandi*.

# In[12]:


# Importa tutte le procedure (funzioni) definite nel modulo "operator"
from operator import add, sub, mul, truediv, floordiv, mod


# In[13]:


sub(345, truediv(12, 6))


# Si consiglia di leggere la **documentazione** della libreria `operator` sul sito di [python](https://docs.python.org/3.10/library/operator.html). Le funzioni principali che useremo in questo notebook sono:
# 
# * `add(a,b)` corrisponde ad `a+b`
# * `sub(a,b)` corrisponde ad `a-b`
# * `mul(a,b)` corrisponde ad `a*b`
# * `truediv(a,b)` corrisponde ad `a/b`
# * `floordiv(a,b)` corrisponde ad `a//b` (divisione tra numeri interi, senza resto)
# * `mod(a,b)` corrisponde ad `a%b` (resto della divisione tra numeri interi
# 
# Per esempio:

# In[14]:


add(339, 6)


# Uno dei vantaggi della notazione **prefix** è che rende sempre chiaro qual'è l'operatore (ovvero quale procedura) che deve essere utilizzato prima, applicandola a quali dati: `add` è il nome dell'operatore, mentre tra parentesi sono specificati gli operandi, i due dati numerici a cui deve essere applicata l'operazione.
# 
# Per esempio, si consideri l'espressione seguente:
# 
# `345 % 11 // 3`
# 
# Quale operazione si devono svolgere prima? Perché?
# 
# Qual'è il risultato corretto, 0 oppure 1?:
# 
# * 345 % 11 // 3 = 0 ?
# * 345 % 11 // 3 = 1 ?

# In[15]:


345 % 11 // 3


# In[16]:


mod(345, floordiv(11,3))


# In[17]:


floordiv(mod(345, 11), 3)


# Si consideri l'espressione seguente:

# In[18]:


mul(add(2,3), 
    (sub(add(2,2), add(3,2))))


# Si noti come questa espressione risulta essere più chiara se riscritta come:
# 
# ```
# mul(
#     add(2, 3),
#     sub(
#         add(2, 2),
#         add(3, 2)
#     )
# )
# ```

# ## 1.2 La valutazione di espressioni composte: Read-Evaluate-Print-Loop
# Per elaborare delle espressioni composte, l'interprete di un linguaggio di programmazione lavora in un ciclo chiamato "*leggi-valuta-stampa*" (in inglese **REPL**, acronimo di **Read-Evaluate-Print-Loop**): legge le espressioni composte e le riduce in espressioni primitive, valuta le espressione con un ordine prestabilito, e alla fine stampa a video il risultato finale. L'ordine in cui vengono valutate le espressioni dipende dal linguaggio di programmazione usato.
# 
# Proviamo ad analizzare come l'interprete del linguaggio valuta operazioni composte come quelle viste prima. La valutazione di operazioni composte avviene attraverso la procedura seguente:
# 
# Per valutare un'espressione composta:
# 
# ```
# 1. Valuta l'espressione composta (ad esempio, operatore e operandi)
# 
# 2. Valuta le sottoespressioni dell'espressione composta (gli operandi)
# 
# 2. Applica la procedura indicata dalla sottoespressione più a sinistra (l'operatore), agli argomenti che sono i valori che risultano dall'avere valutato la sottoespressione (gli operandi).
# ```    
# Si noti come questa procedura per valutare un'operazione composta, per prima cosa deve applicare il processo di valutazione ad ogni elemento dell'espressione composta. Quindi, la regola di valutazione di un'espressione è intrinsecamente **RICORSIVA**, ovvero include come uno dei suoi passi la chiamata a se stessa.

# ### ESERCIZIO 1.1
# Disegnare il *recursion tree* (albero di ricorsione) dell'espressione seguente:

# In[19]:


mul(add(2, mul(4, 6)), mul(3, 5))


# <img src="RecursionTree.PNG" alt="Recursion Tree" style="width: 400px;"/>

# ## 1.3 Assegnazione di nomi ad oggetti
# Un aspetto critico della programmazione è l'assegnazione dei nomi agli oggetti computazionali.
# Si dice che un **nome** identifica una **variabile** il cui **valore** è l'oggetto a cui viene associato. Per esempio:

# In[20]:


giusy = 13


# In questo caso abbiamo una **variabile**, per la quale abbiamo scelto il **nome** `giusy`, il cui **valore** è il numero 13. A questo punto possiamo usare la variabile `giusy` come un oggetto di tipo numerico:

# In[21]:


3*giusy


# In[22]:


add(giusy, add(giusy,giusy))


# Altri esempi sono:

# In[23]:


pi = 3.14159


# In[24]:


raggio = 5


# In[25]:


circonferenza = 2*pi*raggio


# In questi tre casi, il ciclo **REPL** si è concluso con un assegnamento, e quindi non è stato stampato nulla a video. Per stampare a video il valore della variabile `circonferenza` abbiamo due possibilità. La prima è semplicemente far valutare dall'interprete il nome della variabile:

# In[26]:


circonferenza


# Il secondo è di utilizzare esplicitamente la procedure `print(x)`:

# In[27]:


print(circonferenza)


# Cosa succede alla variabile `circonferenza` se ora cambiamo il valore della variabile `raggio`, come nell'esempio seguente?

# In[28]:


raggio = 10


# In[29]:


circonferenza


# Cosa è successo? Come mai non ha stampato a video il valore 62.8318?
# 
# L'interprete del linguaggio, prima, ha letto e valutato l'espressione `2*pi*raggio`, e, dopo, ha assegnato il **valore** ottenuto dalla valutazione dell'**espressione** alla variabile di nome `circonferenza`.
# 
# In questo contesto, l'operatore di assegnamento `=` rappresenta il più semplice meccanismo di astrazione, perché permette di assegnare un **nome** al risultato di operazioni più complesse, eseguite da una o più procedure. 
# 
# In pratica, qualsiasi programma viene definito partendo dalla costruzione, passo passo, di oggetti computazionali via via più complessi e più astratti.
# 
# L'uso di un **interprete**, che in modo incrementale valuta le **espressioni** che li vengono passate in input, favorisce la definizione di tante piccole procedure, innestate l'una nell'altra.
# 
# Dovrebbe essere chiaro a questo punto, che l'interprete deve mantenere una sorta di **MEMORIA GLOBALE** in cui tiene traccia di tutti gli assegnamenti di nomi a oggetti. Questa memoria viene chiamata il `global environment`. In Python, per visualizzare quali sono i nomi di variabili attualmente in memoria si usa il comando `who`:

# In[30]:


who


# In un notebook di Python, per cancellare tutte le variabili del global environment si può riavviare il kernel utilizzando il menu' `Kernel->Restart`.

# In[31]:


who


# ## 1.4 Definizione di nuove procedure composte
# Abbiamo identificato alcuni elementi che devono appartenere ad un linguaggio di programmazione:
# 
# 1. I numeri sono dei **dati primitivi**.
# 2. Le operazioni aritmetiche delle **procedure primitive** (in gergo, vengono chiamate *builtin*).
# 3. L'**annidamento di espressioni** composte offre un meccanismo per comporre delle operazioni.
# 4. L'**assegnamento** di nomi di variabili a valori offre un livello di astrazione limitato.
# 
# Abbiamo quindi bisogno di un modo per poter **definire nuove procedure**, in modo che una nuova operazione possa essere definita come composizione di operazioni più semplici.
# 
# Consideriamo, per esempio, come possiamo definire una procedura che realizzi la funzione di elevamento al quadrato di un numero dato.

# In[32]:


quadrato = mul(3, 3)


# In[33]:


quadrato


# In[34]:


power = mul(x,x)
print(power)


# **NOTA:** è molto importante imparare a leggere e capire i messaggi di errore dell'interprete.

# In[ ]:


x = 7


# Con gli elementi del linguaggio visti sino ad ora non siamo in grado di definire l'elevamento al quadrato in un modo generico, più astratto.
# 
# Per ottenere un livello di astrazione più alto abbiamo quindi bisogno di un meccanismo (una sintassi del linguaggio) che ci permetta di definire nuove procedure (funzioni). In Python, la sintassi è la seguente:
# 
# ```
# def <NomeProcedura>(<lista di parametri formali>):
#     <corpo della procedura>
#     return <valore>
# ```
# 
# Si noti come siano apparse le prime due *parole chiave riservate* del linguaggio: **def** e **return**. Inoltre, `<Nome>` è il nome che noi vogliamo associare alla procedura (funzione) che stiamo definendo, e la `<lista parametri formali>` (chiamati argomenti della procedura) sono le variabili che non appartengono direttamente al *working eniviroment* (ovvero alla MEMORIA GLOBALE dell'interprete), ma sono "visibili" solo internamente alla procedura in cui sono definite.
# 
# Utilizzando questa nuova sintassi, possiamo scrivere la definizione di una procedura per l'elevamento al quadrato nel modo seguente:

# In[ ]:


def Quadrato(numero):
    return mul(numero, numero)


# In[ ]:


Quadrato


# In[ ]:


who


# Per utilizzare la nuova procedura per calcolare il quadrato di un numero, dobbiamo "richiamarla" passandogli dei valori numerici come argomento:

# In[ ]:


Quadrato(12)


# In[ ]:


Quadrato(139)


# In[ ]:


Quadrato(mul(3,2))


# Nella definizione della sintassi per definire nuove procedure, non abbiamo posto nessuna condizione sulle procedure che possono essere richiamate. In pratica, possiamo definire nuove procedure in termini della procedura appena definita `Quadrato(x)`, definendo una nuova procedura chiamata `SommaDiQuadrati(x, y)`:

# In[ ]:


def SommaQuadrati(x, y):
    return add(Quadrato(x), Quadrato(y))


# In[ ]:


SommaQuadrati(4,3)


# ### Applicative Order vs. Normal Order Evaluations
# Ora che abbiamo introdotto le procedure composte, rivediamo in quale ordine è possibile valutare un'espressione composta. Consideriamo la procedura:
# 
# ```SommaQuadrati(add(3,2), mul(3,2))```
# 
# Seguendo l'ordine di valutazione specificato sopra, prima valutiamo gli argomenti (gli operandi), valutando la somme $3+2=5$ e il prodotto $3*2=6$, e poi valutiamo la somma $5^2 + 6^2$. Questo ordine di valutazione in cui prima si valutano gli argomenti e poi si applica la procedura, si chiama *Applicative-order Evaluation*.
# 
# ```
#     SommaQuadrati( add(3,2), mul(3,2) )
#     SommaQuadrati( 5, 6 )
#     add( Quadrato(5), Quadrato(6) )
#     add(   mul(5,5) ,   mul(6,6)  )
#     add(     25     ,     36      )
#                     61    
# ```
# 
# In alternativa, si sarebbe potuto seguire un ordine diverso, in cui prima si applicano le procedure e solo dopo si valutano gli argomenti. Nell'esempio precedente, avremmo avuto l'ordine di valutazione seguente:
# 
# ```
#     SommaQuadrati( add(3,2), mul(3,2) )   
#     add(    Quadrato(add(3,2)),      Quadrato(mul(3,2))    )
#     add(  mul(add(3,2), add(3,2)), mul(mul(3,2), mul(3,2))  )
#     add(          mul(5, 5)      ,        mul(6, 6)        )
#     add(              25         ,            36           )
#                                 61
# ```
# Questo ordine di valutazione si chiama *Normal-order Evaluation*. Si noti che in questo caso, la somma $3+2$ e il prodotto $3*2$ sono eseguiti entrambi due volte. Tuttavia, in alcuni casi questo ordine di valutazione può essere vantaggioso (si veda l'esercizio 1.7).

# In[ ]:


SommaQuadrati(add(3,2), mul(3,2))


# ### ESERCIZIO 1.2
# Si consideri la seguente espressione composta:

# In[ ]:


def F(a):
    return SommaQuadrati(add(a, 1), mul(a, 2))


# In[ ]:


print("Il risultato di F(5):", F(5))


# Come è stata valutata questa procedura?

# **OSSERVAZIONE**: con gli elementi del linguaggio sin qui introdotti, possiamo definire una funzione `ValoreAssoluto(x)`, ovvero: 
# 
# $|x| = x$ se $x \geq 0$, e $|x|=-x$ se $x < 0$? 

# **RISPOSTA**: No, il linguaggio non ancora è abbastanza *espressivo*. Abbiamo bisogno di aggiungere altri elementi al linguaggio di programmazione.

# ## 1.5 Variabili Booleane ed Espressioni Logiche
# Una variabile booleana `p` è un simbolo che prende un valore booleano: `p` è uguale a *vero*, oppure è uguale a *falso*, non può mai assumere i due valori allo stesso tempo, e deve sempre essere uguale a uno (e uno solo) dei due. L'aggettivo *booleano* si deve a [George Boole](https://en.wikipedia.org/wiki/George_Boole), il pioniere della [logica booleana](https://en.wikipedia.org/wiki/Boolean_algebra).
# 
# In Python, i due valori booleani sono dati primitivi, rappresentati dai simboli `True` e `False`. In pratica, `True` e `False` sono altre due parole chiave (*keywords*) che sono riservate all'interprete del linguaggio, e non possono essere usate per definire variabili o funzioni.
# 

# In[ ]:


True


# In[ ]:


True = 13


# In[ ]:


return = 12


# In qualsiasi linguaggio di programmazione, oltre alle espressioni aritmetiche, è possibile valutare delle espressioni logiche, utilizzando gli operatori logici `and`, `or`, e `not`. Le tabelle logiche degli operatori `and` e `or` sono:
# 
# | Primo operando | Secondo operando | `and` | `or` |
# |:--:|:--:|:--:|:--:|
# | `False` | `False` | `False` | `False` | 
# | `False` | `True ` | `False` | `True`  |
# | `True`  | `False` | `False` | `True`  |
# | `True`  | `True`  | `True`  | `True`  |
# 

# In[ ]:


True and False


# In[ ]:


True or False


# In[ ]:


False and False or True


# In[ ]:


True or False and False


# **DOMANDA**: guardando gli ultimi due esempi, si riesce a capire se l'operatore `and` ha la precedenza sull'operatore `or`? La descrizione completa delle precedenze sugli operatori si trova nella [documentazione ufficiale](https://docs.python.org/3/reference/expressions.html#operator-precedence).
# 
# Anche per gli operatori logici è possibile usare una notazione prefix, importando la libreria `operator`:

# In[ ]:


# Importa dalla libreria solo i tre operatori logici
from operator import and_, or_, not_


# In[ ]:


not_(or_(True, and_(False, True)))


# In[ ]:


In alternativa, per dichiarare una precedenza tra gli operatori si possono usare le parentesi tonde:


# In[ ]:


not (True or (False and True))


# ### Operatori logici di confronto
# Oltre agli operatori logici è possibile utilizzare gli operatori di confronto seguenti:
# 
# | Simbolo matematico | Keyword Python | Notazione prefix |
# |:--:|:--:|:--:|
# |  $a < b$  | `a < b`   | `lt(a, b)` | 
# |  $a \leq b$  | `a <= b`   | `le(a, b)` | 
# |  $a > b$  | `a > b`   | `gt(a, b)` | 
# |  $a \geq b$  | `a >= b`   | `ge(a, b)` | 
# |  $a = b$  | `a == b`   | `eq(a, b)` | 
# |  $a <> b$  | `a != b`   | `neq(a, b)` | 

# In[ ]:


# Importa dalla libreria solo i tre operatori logici
from operator import lt, le, gt, ge, eq


# **IMPORTANTE:** non si confonda l'operatore di assegnamento `=` con l'operatore di confronto `==`, in quanto hanno due significati completamente diversi.
# 

# In[ ]:


True == True


# In[ ]:


6*3 < 7*2


# In[ ]:


14*2 == 4*7


# In[ ]:


eq(14*2, 4*7)


# In[ ]:


le(3*2, ge(2,3))


# **DOMANDA**: Cosa osservate dall'espressione precedente? La **sintassi** è corretta? Qual'è la sua **semantica** (come viene valutata l'espressione)?
# 

# ## 1.6 Espressioni condizionali e predicati
# Qualsiasi linguaggio di programmazione deve avere un modo per poter verificare delle condizioni particolari e applicare delle procedure specifiche in base all'esito di tali condizioni. Ovvero, si devono poter definire delle **espressioni condizionali**. In Python la sintassi per le espressioni condizionali è la seguente:
# 
# ```
# if <predicato1>:
#     <body1>
# elif <predicato2>:
#     <body2>
# else:
#     <body3>
# ```
# 
# Per **predicato** si intende una *espressione logica* o una procedura (meglio, una **funzione**) che restituisce un valore booleano, ovvero `True` o `False`.
# 
# Per definire delle espressioni logiche, si possono utilizzare gli operatori di confronto e gli operatori logici. Oppure, si possono usare nuovi predicati definiti nel programma che si sta scrivendo.
# 
# **ESEMPIO**:

# In[ ]:


if not 3 > 4:
    a = 3*2
else:
    a = 4*2


# In[ ]:


a


# In[ ]:


print(a)


# In[ ]:


def Test(x):
    return x > 5 and x < 10


# In[ ]:


Test(2)


# In[ ]:


Test(6)


# In[ ]:


def ThreeAnd(x,y,z):
    return x and y and z


# In[ ]:


ThreeAnd(2>4, 1<2, 1==3)


# A questo punto, abbiamo tutti gli elementi per poter scrivere la funzione valore assoluto definita nella Sezione 1.4.
# 

# In[ ]:


def Abs(x):
    if x >= 0:
        return x
    else:
        return -x


# In[ ]:


Abs(-3)


# In[ ]:


Abs(5)


# ## Esercizi
# 
# ### Esercizio 1.3
# Viene data sotto una serie di espressioni. Qual è il risultato dell'interprete in risposta a ciascuna espressione? Si assuma che la sequenza viene valutata nell'ordine in cui vi viene presentata.
# 
# 
# ```
# from operator import add, sub, mul
# 10
# 5 + 3 + 4
# sub(9, 1)
# add(mul(2, 4), sub(4, 6))
# a = 3
# b = add(a, 1)
# a = b
# b = add(a, add(b, mul(a, b)))
# if gt(a, b) = lt(b, mul(a, b)):
#     print(b)
# else:
#     print(a)
# ```

# In[ ]:


# Da svolgere su carta


# ### Esercizio 1.4: Si traduca l'espressione seguente in notazione *prefix*:
# 
# $\frac{5+4+(2 - (3 - ( 6 + \frac{4}{5})))}{3(6-2)(2-7)}$

# In[ ]:


# Da svolgere su carta


# ### Esercizio 1.5
# Si scriva una procedura che prenda tre numeri come argomenti e restituisca la somma dei quadrati dei due numeri più grandi.
# 

# In[ ]:


# Risolvi sotto
# ...


# ### Esercizio 1.6
# Si osservi che il modello di valutazione dell'interprete visto sino ad ora permette la valutazione di procedure in cui si hanno procedure composte. Si osservi l'esempio seguente e si commenti il comportamento dell'interprete in questo caso:

# In[ ]:


from operator import add, sub
def F(a, b):
    if b > 0:
        return add
    else:
        return sub
    
def G(a, b):
    return F(a,b)(a,b)


# In[ ]:


# Cosa succede ora?


# In[ ]:


G(-2,-3)


# ### Esercizio 1.7
# Il sig. Bit ha inventato un test per determinare se l'interprete del linguaggio che sta usando segue un *applicative-order evaluation* oppure un *normal-order evaluation*. L'idea è di definire due procedure:
# 

# In[ ]:


def P():
    return P()


# In[ ]:


def Test(x, y):
    if x == 0:
        return 0
    else:
        return y


# e poi de valutare l'espressione:
# 
# ```
# Test(0,P())
# ```
# 
# Quale comportamento osserverà il signor Bit con un interprete che usa una *applicative-order evaluation*? Quale comportamento osserverà con un interprete che usa una *normal-order evaluation*? Spiegare la risposta data.
# 

# In[ ]:


Test(0,P())

