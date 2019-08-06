#Problema 4
#Calcula el error absoluto y relativo de una multiplicación

def errorDistancia(v, t, ev, et):
    dist = v * t
    eAbs = v * et + t * ev
    eRel = (ev / v) + (et / t)
    
    print("Distancia de la particula con el error absoluto: " + str(dist) + " +/- " + str(eAbs))
    print("Error relativo: ", eRel)

if __name__ == "__main__":
    errorDistancia(4, 5, 0.1, 0.1)
