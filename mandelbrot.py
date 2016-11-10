import numpy as np
import matplotlib.pyplot as plt
import sys
sys.setrecursionlimit(2100)

#Exercise 3.1
r=np.arange(-2.5, 1,   0.035)
j=np.arange(-1.5, 1.5, 0.035)
R,J=np.meshgrid(r,j)
x=R+J*1j

# Exercise 3.2
#c = complex(input('Input a complex number c: '))
def in_mandelbrot(c):
    z=0
    for n in range(1,100):
        z=z*z + c
        if np.abs(z)>2:
            return n
            break
    return n
#print(in_mandelbrot(c))

# Exercise 3.3
fn=np.vectorize(in_mandelbrot)

plt.imshow(fn(x),extent=(-2.5,1,-1.5,1.5))
plt.title('Mandelbrot set low resolution')
plt.xlabel('real axis')
plt.ylabel('imaginary axis')
plt.savefig('mandelbrot_lowres.pdf')
plt.show()

# Exercise 3.4
r=np.linspace(-2.5, 1,   1000)
j=np.linspace(-1.3, 1.3, 800)
R,J=np.meshgrid(r,j)
x=R+J*1j

def mandelbrot_set(c,nmax):
	a=np.zeros(c.shape)
	z=np.zeros(c.shape)
	for n in range(1,nmax):
		z=z*z +c
		ind=np.where(np.abs(z)>2)
		notind=np.where(np.abs(z)<=2)
		a[notind]=nmax
		a[ind]=n
	return a

plt.imshow(mandelbrot_set(x,100), cmap='magma_r')
plt.title('Mandelbrot set high resolution')
plt.xlabel('real axis')
plt.ylabel('imaginary axis')
plt.savefig('mandelbrot_lowres.pdf')
plt.show()