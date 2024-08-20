#elabore un algoritmo que muestre la factura de la siguiente compra
#el sr pedro ramirez compró en falabella dos jeans de 125.000 cada uno, dos camisas de 45.000 cada una, una camisa tipo polo por 30.000 
#tener en cuenta lo siguiente:
#si la compra lleva camisa tipo polo tiene un descuento del 5%
#si la compra es superior a 200.000 se realiza un descuento del 30% 
#mostrar el total a pagar y el total del descuento en pesos 

jeansazul=125000
juansnegro=12.000
camisablanca=45000
camisaazul=45000
polo=30000
descuento_polo=0
descuentosuperior=0
suma=int

compra=[jeansazul, juansnegro, camisaazul, camisablanca, polo]

suma= sum(compra)

if polo in compra:
    descuento_polo= suma * 0.05
    
if suma >= 200000:
    descuentosuperior= suma*0.3

print ("el total de su compra es:", suma)
print ("su descuento de la camisa polo dl 5%", descuento_polo)
print ("si su cuenta es de mas de 200.000 se aplicara un descuento del 30%", descuentosuperior)
