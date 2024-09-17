import numpy as np

A = np.array([[0.52,0.2,0.25],[0.3,0.5,0.2],[0.18,0.30,0.55]])
B = np.array([[4800],[5810],[5690]])
print("Matriz A: \n"+str(A))
print("Vector B: \n"+str(B))
A_inv = np.linalg.inv(A)
print("\nMatriz_inversa de A: \n"+str(A_inv))
x = A_inv.dot(B)
print("\nCantidades: \n"+str(x))

print("\n<<<<<<< Aplicando SEIDEL >>>>>>>>")
print("")
A_length = len(A)
B_length = len(B)

Cantera1=[0.0,float(((A[0][1]*(-1))/A[0][0])),float(((A[0][2]*(-1))/A[0][0])),float(B[0][0]/A[0][0])]
Cantera2=[float(((A[1][0]*(-1))/A[1][1])),0.0,float(((A[1][2]*(-1))/A[1][1])),float(B[1][0]/A[1][1])]
Cantera3=[float(((A[2][0]*(-1))/A[2][2])),float(((A[2][1]*(-1))/A[2][2])),0.0,float(B[2][0]/A[2][2])]
print(Cantera1)
print(Cantera2)
print(Cantera3)

n=1
c1=0.0
c2=0.0
c3=0.0
valor_max=1

while valor_max >= 0.00001:
    iteracionC1=Cantera1[1]*c2+Cantera1[2]*c3+Cantera1[3]
    iteracionC2=Cantera2[0]*iteracionC1+Cantera2[2]*c3+Cantera2[3]
    iteracionC3=Cantera3[0]*iteracionC1+Cantera3[1]*iteracionC2+Cantera3[3]
    print("\nIteración: "+str(n))
    print("Cantera1: "+str(iteracionC1)+"\nCantera2: "+str(iteracionC2)+"\nCantera3: "+str(iteracionC3))
    
    c1=iteracionC1
    c2=iteracionC2
    c3=iteracionC3

    c1error=Cantera1[1]*c2+Cantera1[2]*c3+Cantera1[3]
    c2error=Cantera2[0]*c1+Cantera2[2]*c3+Cantera2[3]
    c3error=Cantera3[0]*c1+Cantera3[1]*c2+Cantera3[3]
    error=[abs((c1error-iteracionC1)/c1error),abs((c2error-iteracionC2)/c2error),abs((c3error-iteracionC3)/c3error)]
    valor_max=max(error)
    print(">>>> Error: "+str(valor_max))

    n=n+1

    


