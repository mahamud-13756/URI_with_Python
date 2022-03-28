# A,B,C= list(map(float, input("Enter a multiple value: ").split()))
A=float(input())
B=float(input())
C=float(input())
pi = 3.14159
a= 0.5*A*C
b= pi*C*C
c= (A+B)/2.0*C
d= B*B
e= A*B

print(f"TRIANGULO: {a:.3f}")
print(f"CIRCULO: {b:.3f}")
print(f"TRAPEZIO: {c:.3f}")
print(f"QUADRADO: {d:.3f}")
print(f"RETANGULO: {e:.3f}")
