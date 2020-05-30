#  ---		TABLA VENTA 	---

	# Retorna el Monto Vendido
	def monto_vendido(self):
	        monto = 0
	        # Importamos los modelos de pedidos
	        from pedido.models import Pedido, Detalle
	        # Aumentamos el caudal a 5 a cada galon vendido
	        for p in Pedido.objects.filter(fecha=self.fecha_a):
	            monto = p.total + monto
	        return monto

	# Calcula el monto consumo del cuadalimetro diario
    def aumentar_caudalimetro(self):
        caudal = 0
        # Importamos los modelos de pedidos
        from pedido.models import Pedido, Detalle
        # Aumentamos el caudal a 5 a cada galon vendido
        for p in Pedido.objects.filter(fecha=self.fecha_a):
            for det in Detalle.objects.filter(pedido=p):
                # Garrafon se creo con el id 2
                if det.producto.id == 2:
                    caudal = (det.cantidad * 5) + caudal
                # Bolsas se creo con el id 3
                elif det.producto.id == 3:
                    caudal = (det.cantidad * 3) + caudal
        return caudal
        short.description = 'Caudal Utilizado'

    # Calcula los garrafones Vendidos a diario
    def garrafones_vendidos(self):
        cant = 0
        # Importamos los modelos de pedidos
        from pedido.models import Pedido, Detalle
        for p in Pedido.objects.filter(fecha=self.fecha_a):
            for det in Detalle.objects.filter(pedido=p):
                    # Garrafon se creo con el id 2
                    if det.producto.id == 2:
                        cant = det.cantidad + cant
        return cant

    # Calcula las bolsas Vendidas a diario
    def bolsas_vendidas(self):
        cant = 0
        # Importamos los modelos de pedidos
        from pedido.models import Pedido, Detalle
        for p in Pedido.objects.filter(fecha=self.fecha_a):
                for det in Detalle.objects.filter(pedido=p):
                    # Bolsas se creo con el id 3
                    if det.producto.id == 3:
                        cant = det.cantidad + cant
        return cant

    # Obtiene los datos de la venta del dia anterior, si no existe indica que es Primero
    def es_primer(self):
        numero = None
        monto_c = None
        caudal_c = None
        ultimo = None
        n = self.pk-1
        if Venta.objects.filter(estado=0).exists():
            ultimo = Venta.objects.filter(pk=n).get()
            if ultimo.pk != self.pk:
                caudal_c = ultimo.caudal_c
                self.caudal_a = caudal_c
                if self.caudal_a != caudal_c:
                    raise ValidationError(
                        'El numero de apertura del caudal debe conicidir con el cierre')

#  ---		TABLA PEDIDO 	---

	# Realiza la suma de subtotal y descuento
	def suma_sub(self):
        sub_total = 0
        desc = 0
        for d in Detalle.objects.filter(pedido=self.pk):
            sub_total = sub_total + d.subtotal
            des = desc + d.descuento
        self.descuento = desc
        self.subtotal = sub_total

    # Valida que exista una venta abierta para poderse crear el pedido
    def exist_venta(self):
        hoy = datetime.date.today()
        venta = False
        if Venta.objects.filter(fecha_a=hoy, estado=1):
            venta = True
        return venta

#  ---		TABLA CLIENTE 	---

	# Regresa una cadena de texto con el nombre del tipo de cliente
	def tipo_c(self):
        if self.tipo_cliente != '3':
            if self.tipo_cliente == '2':
                return 'Dist'
            elif self.tipo_cliente == '1':
                return 'Norm'
        else:
            return 'Esp'