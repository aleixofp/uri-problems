# 1036 - Fórmula de Bhaskara
# Runtime: 0.040s

a, b, c = [float(i) for i in input().split(" ")]
delta = ((b**2) - (4*a*c))
if (delta < 0 or a == 0):    
	print("Impossivel calcular")
else:    
	sqrt_delta = delta ** 0.5
	x1, x2 = (-b+sqrt_delta)/(2*a), (-b-sqrt_delta)/(2*a)        
	print("R1: %.5f\nR2: %.5f" %(x1, x2))
