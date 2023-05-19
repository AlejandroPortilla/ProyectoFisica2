import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk

# Define the new data function
def new_data():
    theta = float(theta_entry.get())
    g = float(g_entry.get())
    v0 = float(v0_entry.get())

    # Calculate the maximum range
    xm = (v0**2 * np.sin(2 * theta)) / g
    ym = (v0 * np.sin(theta))**2 / (2 * g)
    # ym = 0.5
    tv = (2 * v0 * np.sin(theta)) / g

    if xm > ym:
        escala = xm
    else:
        escala = ym

    #print(tv)
    #print(xm)
    #print(ym)
    #print(escala)

    # Create a list to store the x and y coordinates of the projectile
    x = []
    y = []

    # Calculate the position of the projectile at each time step
    for t in np.arange(0, xm, 0.01):
        # Calculate the horizontal and vertical displacements
        x_t = v0 * t * np.cos(theta)
        # x_t = t
        y_t = v0 * t * np.sin(theta) - 0.5 * g * t**2

        # Add the x and y coordinates to the list
        x.append(x_t)
        y.append(y_t)

    # Plot the trajectory
    plt.xlim([0, escala * 1.1])
    plt.ylim([0, escala * 1.1])
    plt.plot(x, y)
    plt.xlabel("x (m)")
    plt.ylabel("y (m)")
    plt.show()

# Create the main window
window = tk.Tk()
window.title("Graficador de lanzamiento de proyectiles")

# Create the menu bar
menubar = tk.Menu(window)
window.config(menu=menubar)

# Create the file menu
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=new_data)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=window.quit)
menubar.add_cascade(label="File", menu=filemenu)

# Create the help menu
helpmenu = tk.Menu(menubar, tearoff=0)
helpmenu.add_command(label="About")
menubar.add_cascade(label="Help", menu=helpmenu)

# Create the entry widgets
theta_entry = tk.Entry(window)
g_entry = tk.Entry(window)
v0_entry = tk.Entry(window)

# Create the labels
theta_label = tk.Label(window, text="Angulo")
g_label = tk.Label(window, text="Gravedad")
v0_label = tk.Label(window, text="Velocidad Inicial")

# Pack the widgets
theta_label.pack()
theta_entry.pack()
g_label.pack()
g_entry.pack()
v0_label.pack()
v0_entry.pack()

# Start the main loop
window.mainloop()