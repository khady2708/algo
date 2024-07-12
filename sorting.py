# ----------------
# Fonctions d'aide
# ----------------
def swap(T, i, j):
    """Échange la place de deux éléments dans un tableau"""
    raise NotImplementedError


# ---------------
# Tris classiques
# ---------------
def tri_bulles(T):
    n = len(T)
    for i in range(n - 1,0, -1):
        for j in range(i):
            if T[j] > T[j + 1]:  
                T[j], T[j + 1] = T[j + 1], T[j]
              
    return T


def tri_insertion(T):
    n = len(T)
    for i in range(1,n):
        x = T[i]
        j = i
        while j > 0 and T[j - 1] > x:
            T[j] = T[j - 1]
            j -= 1
        T[j] = x
    return T
    
def tri_selection(T, n): 
    n = len(T)
    for i in range( n - 2):
        min = i
        for j in range(i + 1, n - 1):
            if T[j] < T[min]:
                min = j
        if min != i:
            T[i], T[min] = T[min], T[i]
    return T




# --------------
# Tris récursifs
# --------------
def merge_sort(tab):
    """Trie le tableau via le principe de « diviser pour mieux régner »
    avec l'intelligence du tri qui se trouve au moment de la fusion"""
    raise NotImplementedError


def quick_sort(tab):
    """Divise le tableau en deux, trie chacune des sous-parties et fusionne
    intelligemment les deux sous-parties triées"""
    raise NotImplementedError
