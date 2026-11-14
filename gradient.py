import numpy as np
import matplotlib.pyplot as pp


#T(x, y) = T₀ exp[−(x² + y²)/σ²]
sigma = 1 #m
T0 = 100 #K
dx = 0.1
dy = 0.1

x = np.arange(-3, 3 + dx, dx)
y = np.arange(-3, 3+dy, dy)

X,Y= np.meshgrid(x,y)
#print(np.shape(X)) #(61, 61)
#print(X)

#Part A

temperature = T0*np.exp(-(X**2+Y**2)/(sigma**2))
fig, ax1 = pp.subplots(figsize=(6, 5))
CS = ax1.contourf(X,Y,temperature, levels=100, cmap='bone')
ax1.set_title('Temperature of plate')
ax1.set_xlabel('X position (m)')
ax1.set_ylabel('Y postion (m)')
cbar = fig.colorbar(CS)
cbar.set_label('Temperature (K)')
pp.savefig('t_plate.png', dpi=300)

#Part B - central differencing
dTdx = (temperature[1:-1, 2:] - temperature[1:-1, :-2]) / (2*dx)
dTdy = (temperature[2:, 1:-1] - temperature[:-2, 1:-1]) / (2*dy)


print(dTdx.shape, dTdy.shape)

#Part C - np.gradient partial derivatives

dTdy_np, dTdx_np = np.gradient(temperature, dy, dx)

#Part D - plot on dtdx.png
y0 = np.argmin(np.abs(y))

dTdx_analytic = -2*X/sigma**2 * temperature
fig2, ax2 = pp.subplots(figsize=(7,5))
ax2.plot(x, dTdx_analytic[y0, :],'k-', label='Analytic')
ax2.plot(x[1:-1], dTdx[y0-1, :],'r--', label='Central difference (part B)')
ax2.plot(x, dTdx_np[y0, :], 'b:', label='np.gradient')
ax2.set_xlabel('x (m)')
ax2.set_ylabel('dT/dx (K/m)')
ax2.set_title('dT/dx along y = 0')
ax2.legend()
pp.savefig('dtdx.png', dpi=300)

#i
difference = np.max(np.abs(dTdx - dTdx_np[1:-1, 1:-1]))
print(f"The difference for part i is {difference}")
#ii
err_edge = np.abs(dTdx_np[y0, [0, -1]] - dTdx_analytic[y0, [0, -1]])
err_int = np.abs(dTdx_np[y0, 1:-1] - dTdx_analytic[y0, 1:-1])
print('edge error:', err_edge)
print('interior error:', err_int)
print('max interior error:', err_int.max())
rel_err_edge = np.abs(dTdx_np[y0, [0, -1]] - dTdx_analytic[y0, [0, -1]]) / np.abs(dTdx_analytic[y0, [0, -1]])
rel_err_int = np.abs(dTdx_np[y0, 1:-1] - dTdx_analytic[y0, 1:-1]) / np.abs(dTdx_analytic[y0, 1:-1])
print('relative edge error:', rel_err_edge)
print('relative interior error:', rel_err_int)
print('max relative interior error:', rel_err_int.max())

#Part E
fig3, ax3 = pp.subplots(figsize=(7, 6))
CS3 = ax3.contourf(X, Y, temperature, levels=100, cmap='bone')
cbar3 = fig3.colorbar(CS3)
cbar3.set_label('Temperature (K)')

s = 5  # plot every 5th arrow
ax3.quiver(X[::s, ::s], Y[::s, ::s], -dTdx_np[::s, ::s], -dTdy_np[::s, ::s], color='red')

ax3.set_xlabel('x (m)')
ax3.set_ylabel('y (m)')
ax3.set_title('Heat flow direction (-∇T)')
pp.savefig('t_plate_flow.png', dpi=300)
