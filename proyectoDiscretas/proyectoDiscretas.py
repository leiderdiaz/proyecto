import networkx as nx
def main():
    G=nx.Graph()
    e=[('N1','P1',11),
        ('N2','N8',19),('N2','P1',17),
        ('N3', 'N8', 18),('N3', 'P1', 21),
        ('N4', 'P1', 15),
        ('N5', 'P1', 8),
        ('N6', 'P1', 3),
        ('N7', 'P1', 8),
        ('N8', 'N7', 20), ('N8', 'N9', 8), ('N8', 'N10', 22), ('N8', 'P1', 40),
        ('N9', 'N7', 24), ('N9', 'N8', 8), ('N9', 'N10', 18), ('N9', 'P2', 34),
        ('N10', 'N7', 6), ('N10', 'N21', 29), ('N10', 'P2', 16),
        ('N11', 'N17', 14), ('N11', 'P1', 11),
        ('N12', 'N11', 6), ('N12', 'N17', 9),
        ('N13', 'N14', 7), ('N13', 'N17', 13), ('N13', 'P1', 12),
        ('N14', 'N13', 7), ('N14', 'P1', 18),
        ('N15', 'N14', 6), ('N15', 'P1', 16),
        ('N16', 'P2', 8),
        ('N17', 'N11', 14), ('N17', 'N13', 13), ('N17', 'P2', 12),
        ('N18', 'P2', 5), ('N18', 'P3', 23),
        ('N19', 'P2', 13), ('N19', 'P3', 13),
        ('N20', 'P2', 15), ('N20', 'P3', 10),
        ('N21', 'N10', 29), ('N21', 'P2', 18), ('N21', 'P3', 12),
        ('N22', 'N10', 35), ('N22', 'P2', 21), ('N22', 'P3', 14)]
    G.add_weighted_edges_from(e)
    print("Presione: \n")
    print("1 si esta en Fisicomecanicas\n")
    print("2 si esta en Daniel Casas\n")
    print("3 si esta en CEIAM\n")
    print("4 si esta en Uisalud\n")
    print("5 si esta en Jorge Bautista\n")
    print("6 si esta en Ing. Quimica\n")
    print("7 si esta en CENTIC\n")
    print("8 si esta en Mamitza Bayer\n")
    print("9 si esta en Instituto de Lenguas\n")
    print("10 si esta en Biblioteca\n")
    print("11 si esta en Camilo Torres\n")
    print("12 si esta en Ing. Mecanica\n")
    print("13 si esta en Laboratorios Livianos\n")
    print("14 si esta en Laboratorio Postgrados\n")
    print("15 si esta en Planta de Aceros\n")
    print("16 si esta en Planta Fisica\n")
    print("17 si esta en Virginia Gutierrez\n")
    print("18 si esta en Luis A. Calvo\n")
    print("19 si esta en Administracion 1\n")
    print("20 si esta en IPRED\n")
    print("21 si esta en Administracion 2\n")
    print("22 si esta en Bienestar Universitario\n")
    salir = True

    while(salir):
        print("Presione su opcion: ")
        res = input()
        if(int(res)>0 and int(res)<=22):
            resp = 'N' + str(res)
            D1 = nx.dijkstra_path_length(G,resp,'P1')
            D2 = nx.dijkstra_path_length(G,resp,'P2')
            D3 = nx.dijkstra_path_length(G,resp,'P3')
            if(D1 <= D2 and D1 < D3):
                print("\nEl punto mas cercano es el P1, con una distancia de " + str(D1) + " metros" )
                print("El camino a seguir es: " + str(nx.dijkstra_path(G, resp,'P1')))
            if(D2 < D1 and D2 <= D3):
                print("\nEl punto mas cercano es el P2, con una distancia de " + str(D2) + " metros" )
                print("El camino a seguir es: " + str(nx.dijkstra_path(G, resp,'P2')))
            if(D3 <= D1 and D3 < D2):
                print("\nEl punto mas cercano es el P3, con una distancia de " + str(D3) + " metros" )
                print("El camino a seguir es: " + str(nx.dijkstra_path(G, resp,'P3')))
            print("\nDesea seleccionar otra opcion (s/n)?\n")
            r = input()
            r.lower()
            if(r == 'n'):
                salir = False
        else:
            print("Esa opcion no existe")

main()
