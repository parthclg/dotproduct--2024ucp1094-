#vect1 = []
#while True:
#    x = int(input("Enter value for vector1: "))
 #   vect1.append(x)
#    y = int(input("Enter 0 to stop: "))
 #   if y == 0:
 #   	break
vec1=[1,2,3,4]
vect2=[4,5,6,7]

dot_product = 0
for i in range(len(vect1)):
	dot_product += vect1[i] * vect2[i]

print("Dot product:", dot_product)

