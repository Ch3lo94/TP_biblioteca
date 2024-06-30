import json

# Definicion de clase y atributos a Socio
class Prestamo():
    def __init__(self,id_prestamo,id_socio,id_libro,fecha_prestamo,fecha_devolucion,estado_prestamo):
        self._id_prestamo = id_prestamo
        self._id_socio = id_socio
        self._id_libro = id_libro
        self._fecha_prestamo = fecha_prestamo
        self._fecha_devolucion = fecha_devolucion
        self._estado_prestamo = estado_prestamo

#Propiedades de cada atributo de Socio
    @property
    def id_prestamo (self):
        return self._id_prestamo
    @id_prestamo.setter
    def id_prestamo(self, valor):
        self._id_prestamo = valor
    @id_prestamo.deleter
    def id_prestamo(self):
        del self._id_prestamo

    @property
    def id_socio (self):
        return self._id_socio
    @id_socio.setter
    def id_socio(self, valor):
        self._id_socio = valor
    @id_socio.deleter
    def id_socio(self):
        del self._id_socio

    @property
    def id_libro (self):
        return self._id_libro
    @id_libro.setter
    def id_libro(self, valor):
        self._id_libro = valor
    @id_libro.deleter
    def id_libro(self):
        del self._id_libro

    @property
    def fecha_prestamo (self):
        return self._fecha_prestamo
    @fecha_prestamo.setter
    def fecha_prestamo(self, valor):
        self._fecha_prestamo = valor
    @fecha_prestamo.deleter
    def fecha_prestamo(self):
        del self._fecha_prestamo

    @property
    def fecha_devolucion (self):
        return self._fecha_devolucion
    @fecha_devolucion.setter
    def fecha_devolucion(self, valor):
        self._fecha_devolucion = valor
    @fecha_devolucion.deleter
    def fecha_devolucion(self):
        del self._fecha_devolucion

    @property
    def estado_prestamo (self):
        return self._estado_prestamo
    @estado_prestamo.setter
    def estado_prestamo(self, valor):
        self._estado_prestamo = valor
    @estado_prestamo.deleter
    def estado_prestamo(self):
        del self._estado_prestamo

# Metodo String para imprimir
    def __str__ (self):
        Esp = 25
        return f'''{"ID de Prestamo: " : <{Esp}}{self.id_prestamo}
{"ID de Socio: " : <{Esp}}{self.id_socio}
{"ID de Libro: " : <{Esp}}{self.id_libro}
{"Fecha de Prestamo: " : <{Esp}}{self.fecha_prestamo}
{"Fecha de Devolucion: " : <{Esp}}{self.fecha_devolucion}
{"Estado de Prestamo: " : <{Esp}}{self.estado_prestamo}'''

# Convertir objeto a formato JSON
class prestamo_Encoder (json.JSONEncoder):
    def default (self, obj):
        if isinstance(obj, Prestamo):
            return {'id_prestamo':obj.id_prestamo,'id_socio':obj._id_socio,'id_libro':obj.id_libro,'fecha_prestamo':obj.fecha_prestamo,'fecha_devolucion':obj.fecha_devolucion,'estado_prestamo':obj.estado_prestamo}
        return json.JSONEncoder.default(self,obj)

# Convertir JSON a Objeto   
def traer_desde_json_Prestamo (diccionario):
    return Prestamo (diccionario ['id_prestamo'], diccionario ['id_socio'], diccionario ['id_libro'], diccionario ['fecha_prestamo'], diccionario ['fecha_devolucion'], diccionario ['estado_prestamo'])

