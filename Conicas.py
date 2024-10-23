class Conicas:
    def conicas(self):
        print("ESTE PROGRAMA ESTA HECHO PARA PODER CONSEGUIR CUALQUIER FORMULA EN SU FORMA CANONICA DE TODAS LAS CONICAS")
        print("LAS OPCIONES SON: Parabola, Circulo, Elipse e Hiperbola")
        conicas={"parabola": "PARABOLA", "circulo": "CIRCULO"}
        seleccion=str(input("ELIGE UNA OPCCION (INGRESELA CON TODAS LAS LETRAS EN MINUSCULAS): "))
        metodo=conicas[seleccion]
        print("HAS SELECCIONADO: " +metodo)
        obj=Conicas()
        res=0
        if metodo=="PARABOLA":
            res=obj.parabola()
        elif metodo=="CIRCULO":
            res=obj.circulo()
            
    def parabola(self):
        opcion="sinERROR"
        
        while opcion=="sinERROR":
            try:
                print("INGRESA LAS COORDENADAS DE TU VERTICE")
                x=int(input("INGRESA EL VALOR DE X EN TU COORDENADA: "))
                y=int(input("INGRESA EL VALOR DE Y EN TU COORDENADA: "))
                print("LA COORDENADA DE TU VERTICE ES: ({},{})".format(x, y))
                p=int(input("INGRESA LA DISTANCIA QUE HAY ENTRE TU VERTICE Y EL FOCO, O ENTRE TU VERTICE Y LA DIRECTRIZ: "))
                opcion=("ELEMENTOS VALIDOS")
            except ValueError:
                print("ELEMENTO NO VALIDO")
                opcion= "sinERROR"
        print(opcion)
        posicion_pa={"v":"VERTICAL", "h": "HORIZONTAL"}
        seleccion_pa=str(input("INGRESA v PARA VERTICAL O h PARA HORIZONTAL (INGRESALA EN MINUSCULA): "))
        metodo_pa=posicion_pa[seleccion_pa]
        print("HAS SELECCIONADO: "+metodo_pa)
        obj=Conicas()
        opp=0
        opcion=("TODO BIEN")           
        if metodo_pa=="VERTICAL":
            opp=obj.vertical(x, y, p)
        elif metodo_pa=="HORIZONTAL":
            opp=obj.horizontal(x, y, p)
    def vertical(self, x, y, p):
        if (y>0):
            pos_y=("(y-{})^2".format(y))
        elif (y<0):
            y=y*-1
            pos_y=("(y+{})^2".format(y))
        elif (y==0):
            pos_y=("(y)^2")
        if (x>0):
            neg_x=("(x-{})".format(x))
        elif (x<0):
            x=x*-1
            neg_x=("(x+{})".format(x))
        elif (x==0):
            neg_x=("(x)")
        print("LA ECUACION CANONICA DE TU PARABOLA ES: ")
        print(pos_y+"=4(",p,")"+neg_x)
    def horizontal(self, x, y, p):
        if (y>0):
            pos_y=("(y-{})".format(y))
        elif (y<0):
            y=y*-1
            pos_y=("(y+{})".format(y))
        elif (y==0):
            pos_y=("(y)")
        if (x>0):
            neg_x=("(x-{})^2".format(x))
        elif (x<0):
            x=x*-1
            neg_x=("(x+{})^2".format(x))
        elif (x==0):
            neg_x=("(x)^2")
        print("LA ECUACION CANONICA DE TU PARABOLA ES: ")
        print(neg_x+" =4(",p,")"+pos_y)
            

    def circulo(self):
        opcion_dos="sinERROR"
        while opcion_dos=="sinERROR":
            try:
                print("INGRESA LAS COORDENADAS DE TU CENTRO: ")
                x=int(input("INGRESA EL VALOR DE X EN TU COORDENADA: "))
                y=int(input("INGRESA EL VALOR DE Y EN TU COORDENADA: "))
                r=int(input("INGRESA EL VALOR DE EL RADIO DE TU CIRCUNGERENCIA: "))
                opcion_dos=("ELEMENTOS VALIDOS.")
            except ValueError:
                print("ELEMENTO NO VALIDO")
                opcion_dos=("sinERROR")
        print(opcion_dos)
        if (y>0):
            pos_y=("(y-{})^2".format(y))
        elif (y<0):
            y=y*-1
            pos_y=("(y+{})^2".format(y))
        elif (y==0):
            pos_y=("(y)^2")
        if (x>0):
            neg_x=("(x-{})^2".format(x))
        elif (x<0):
            x=x*-1
            neg_x=("(x+{}^2)".format(x))
        elif (x==0):
            neg_x=("(x^2)")
        print("LA ECUACION CANONICA DE TU CIRCUNFERENCIA ES: ")
        print(neg_x+"+"+pos_y+"={}^2".format(r))













        
        
