'''
    Lógica con abstracciones para construir un medidor de consumos y gastos genericos.\n
'''
class Auto:
    # Hago sin atributos para hacer una clase mas flexible y menos dependiente del contexto
    '''
        Representa caracteristicas de un auto de forma flexible e independiente de en que orden y que datos se reciban sobre dicho vehículo.\n
    '''
    def __init__(self):
        '''
            \n[ATRIBUTOS]
            \n\t\u25cf Auto.nombre, texto con nombre de modelo para ese auto
            \n\t\u25cf Auto.marca, texto con la marca del vehículo
            \n\t\u25cf Auto.peso, lista que tiene primero un número con la medida\n\tdel peso del vehículo y segundo el nombre como texto corto\n\tde la unidad de medida
        '''
        self.nombre:str = ''

        self.marca:str = ''

        self.peso:list = []

    def completa(self) -> bool:
        '''
            \nVerifica que todos los datos estén completados y\nsean del tipo correcto\n
        '''
        # Uso variables solo para hacer mas legible el código
        # Es bueno evitar choclos en el codigo para que sea mas mantenible y depurable
        # Inicializo a verdadero tipo de dato correcto para corregirlo ya que se llevara mejor con el operador Y lógico
        correctos = True
        completos = True
        # Enumero datos agrupados por los tipos recomendados así hago de forma escalable las verificaciones
        atributos_textos = [self.nombre, self.marca]
        atributos_medidas = [self.peso]
        # Hago la verificacion para cada dato:
        # Para tipo de dato: datos del tipo correctos
        for datos_1 in atributos_textos:
            # Uso valor anterorio para validar que cada atributo tenga su tipo
            # Si en la variable correctos usara valor falso me daría error eterno aunque los datos estén bien
            correctos = (correctos and (type(datos_1) == str))
        for datos_2 in atributos_medidas:
        # Listas con un numero y una cadena de texto, una estructura de datos bastante versatil y simple
            correctos = (correctos and (type(datos_2 == list)))
            if (correctos and datos_2.__len__() == 2):
            # Ya verifique que sea una lista, ahora verifico si los elementos son correctos
                correctos = (correctos and ((type(datos_2[0]) == int) or (type(datos_2[0]) == float)))
                correctos = (correctos and (type(datos_2[1]) == str))
        # Para valor de dato: datos completos
        if (correctos):
        # Solo lo ejecuto si los datos son correctos para ahorrar tiempo
        # Para no perderlo con objetos con errores y actuar sobre algo conocido
            for completo_1 in atributos_textos:
                completos = (completos and (completo_1 != ''))
            # Por esto debo asegurarme que sean del tipo correcto lista con int o float y un str
            # ademas que la lista sea de dos elementos
            for comleto_2 in atributos_medidas:
                completos = (completos and (comleto_2.__len__() == 2))
        # Devuelvo resultado de la operacion
        return (correctos and completos)

    def pesar(self, medida:float, unidad:str):
        '''
            \n[PARÁMETROS]
            \n\t\u25cf medida: numero real segun cuanto pesa
            \n\t\u25cf unidad: texto con un nombre de unidad de peso
            \nDESCRIPCIÓN:\n
            \tDefine peso del vehiculo usando parametros recibidos para\n\taumentar seguridad en el manejo de datos complejos.\n
        '''
        # Refuerzo extra para que otras variantes para ingresar datos se acomoden al formato
        self.peso[0] = float(medida)
        self.peso[1] = str(unidad)

class Consumo:
    '''
        Representa datos sobre el consumo y gastos de un producto o servicio, su flexibilidad hace que
        funcione para representar una gran variedad de consumos de todo tipo.\n
    '''
    def __init__(self):

        '''
            \n[ATRIBUTOS]
            \nFORMATO: listas de dos elementos, número con medida del dato y exto con la unidad usada "[medida, unidad]":

            \t\u25cf Consumo.precio, precio y divisa usada para la unidad de producto o servicio a medir\n

            \t\u25cf Consumo.distancia, distancia a recorrer durante el viaje\n

            \t\u25cf Consumo.carga, peso total de toda la carga transportada\n

            \t\u25cf Consumo.tarifas, sumatoria bajo una misma divisa de todos los recargos al viaje y producto\n

            \t\u25cf Consumo.rendimiento, dice hasta cuanto puede rendir un producto de variable a convenir\n
        '''
        self.precio:list = []

        self.distancia:list = []

        self.carga:list = []

        self.tarifas:list = []

        self.rendimiento:list = []

    def completa(self) -> bool:
        '''
            \nVerifica integridad de datos en la clase.\n
        '''
        resultado = True
        # Verifico atributo a atributo ya que todos están en el mismo formato
        for atributo in [self.precio, self.distancia, self.carga, self.tarifas, self.rendimiento]:
            resultado = (resultado and (type(atributo) == list))
            # Ya que verifique que es una lista, verifico que sea del formato correcto
            if (resultado):
                resultado = (resultado and (atributo.__len__() == 2))
                resultado = (resultado and ((type(atributo[0]) == int) or (type(atributo[0]) == float)))
                resultado = (resultado and (type(atributo[1]) == str))
        # Devuelvo el resultado de la verificacion
        return resultado

    def costo(self):
        '''
            \nRetorna lista "[precio, divisa]" con el costo del producto en función de su precio unitario,\nrendimiento y otros costos relacionados con la actividad.\n
        '''
        return [((self.precio[0] * (self.distancia[0] / self.rendimiento[0])) + self.tarifas[0]), self.precio[1]]

    def ponerPrecio(self, nuevoPrecio:float):
        '''
            \n[PARÁMETROS]\n
            \t\u25cf nuevoPrecio: numero real con el nuevo valor para primer elemento de Consumo.precio
            \nDefine un nuevo valor para el atributo Consumo.precio (solo cambia primer elemento)\n
        '''
        self.precio[0] = float(nuevoPrecio)

    def agregarTarifa(self, nuevoValor:float):
        '''
            \n[PARÁMETROS]\n
            \t\u25cf nuevoValor: numero real con nuevo valor total en tarifas
            \nAgrega nueva sumatoria al valor total en primer elemento de lista Consumo.tarifas\npara actualizarla.\n
        '''
        self.tarifas[0] = float(nuevoValor)

    def agregarPeso(self, medida:float, unidad:str):
        '''
            \n[PARÁMETROS]\n
            \t\u25cf medida: número real para Consumo.carfa
            \t\u25cf unidad: texto con el nombre de la unidad de medida usada
            \nIncrementa valor de Consumo.carga\n\tAdvertencia: SOLO usar SI Consumo.carga YA ESTÁ INICIALIZADA Y CON LA MISMA UNIDAD PARA QUE SOLO MANIPULE QUIEN SEPA HACERLO\n
        '''
        if (str(Consumo.carga[1]) == str(unidad)):
            Consumo.carga[0] += float(medida)

    def subioPrecio(self, porcentaje:float):
        '''
            \n[PARÁMETROS]\n
            \t\u25cf porcentaje: número real de 0.00 a 100.00 con cuanto aumentar Consumo.precio
            \nAumenta el precio desde valor actual usando porcentaje indicado (Consumo.precio debe tener valor valido antes de usar)\n
        '''
        # Variable auxiliar para guardar valor anterior sobre cual relizar calculos y no se vaya a las nubes
        total = self.precio[0]
        # realizo el calculo aumento porcentual de la propiedad
        self.precio[0] += (porcentaje * (total / 100))
        # libero memoria porque ya no lo necesitaré
        del total

    def subioTarifa(self, porcentaje:float):
        '''
            \n[PARÁMETROS]\n
            \t\u25cf porcentaje: número real de 0.00 a 100.00 con cuanto aumentar Consumo.tarifas
            \nAumenta valor de Consumo.tarifas desde valor actual en cierto porcentaje.\n
        '''
        # Variable auxiliar para guardar valor anterior sobre cual relizar calculos y no se vaya a las nubes
        total = self.tarifas[0]
        # realizo el calculo aumento porcentual de la propiedad
        self.tarifas[0] += (porcentaje * (total / 100))
        # libero memoria porque ya no lo necesitaré
        del total

    def comparar(self, objetos:list) -> 'objeto de clase Consumo':
        '''
            \n[PARÁMETROS]\n
            \t\u25cf objetos: lista de objetos con cual comparar al objeto que ejecuta este método
            \nEn una lista de objetos de la clase Consumo busca y retorna como valor al que tiene mejores atributos, \nIra cambiando según como se actualize el metodo\n para mejores resultados.\n
        '''
        pass

    def adaptar(self, producto:Auto):
        '''
            \n[PARÁMETROS]\n
            \t\u25cf producto: objeto de la clase Auto para obtener datos
            \nRecalcula Consumo.rendimiento según los nuevos datos.\n
        '''
        pass

    def cargarBaul(self, peso:float, unidad:str):
        '''
        \n[PARÁMETROS]\n
        \t\u25cf peso: número real con el peso que hay en el baul del vehículo
        \t\u25cf unidad: texto con la unidad en la que se mide el peso de la carga
        \nInicializa Consumo.carga con la carga transportada por un vehículo.\n
        '''
        self.carga[0] = float(peso)

        self.carga[1] = str(unidad)


    def recorrer(self, dis:float):
        '''
        \n[PARÁMETROS]\n
        \t\u25cf distancia: número real con el recorrido extra agregado (medido en la misma unidad)
        \nSuma distancia a la ya existente en Consumo.distancia.\n
        '''
        if (self.distancia == 0):
            # Valor de inicializacion
            self.distancia[0] = float(dis)
        else:
            # Recorro mas distancia
            self.distancia[0] += float(dis)

    def corregir_unidades(self, sistema:str):
        '''
            \n[PARÁMETROS]\n
            \t\u25cf sistema: texto con los siguientes valores para referirse a distintos sistemas metricos en los que expresar unidades\n\t\t- 'americano': el que se usa en US, por ejemplo onzas y pulgadas\n\t\t- 'internacional': sistema SI, el estandar mundial, gramos y centimetros\n\t\t- 'britanico'\n\t\t- 'natural', usa constantes para medir las unidades, plank, año-luz, pi\n
            \n\n
        '''
        pass
