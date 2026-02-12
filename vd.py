import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import numpy as np

fig, ax = plt.subplots(figsize=(8, 8))

ax.set_facecolor('#E5E5E5')
fig.patch.set_facecolor('#E5E5E5')

radius = 3.2
linewidth = 5
edgecolor = 'black'

center1 = (-1.8, 1.2)  # Top Left
center2 = (1.8, 1.2)   # Top Right
center3 = (0, -1.8)    # Bottom

c1 = Circle(center1, radius, facecolor='none', edgecolor=edgecolor, linewidth=linewidth)
c2 = Circle(center2, radius, facecolor='none', edgecolor=edgecolor, linewidth=linewidth)
c3 = Circle(center3, radius, facecolor='none', edgecolor=edgecolor, linewidth=linewidth)

# Add circles to plot
ax.add_patch(c1)
ax.add_patch(c2)
ax.add_patch(c3)

# Define function to add text
def add_text(x, y, text, color='black', size=20, weight='normal'):
    ax.text(x, y, text, fontsize=size, color=color, ha='center', va='center', fontname='DejaVu Sans', fontweight=weight)


add_text(-2.8, 2.5, 'A', size=24)
add_text(-3.2, 1.5, 'B', size=24)
add_text(-2.2, 1.8, 'C', size=24)
add_text(-2.5, 0.8, 'D', size=24)
add_text(-3.0, 2.8, 'α', color='blue', size=28, weight='bold') # Colored greek letter

add_text(2.8, 2.5, 'E', size=24)
add_text(3.2, 1.5, 'F', size=24)
add_text(2.2, 1.8, 'G', size=24)
add_text(2.5, 0.8, 'H', size=24)
add_text(3.0, 2.8, 'β', color='red', size=28, weight='bold') # Colored greek letter

add_text(0, -3.5, 'I', size=24)
add_text(-1.2, -3.0, 'J', size=24)
add_text(1.2, -3.0, 'K', size=24)
add_text(0, -2.8, 'L', size=24)
add_text(-0.5, -4.0, 'γ', color='green', size=28, weight='bold') # Colored greek letter

add_text(0, 2.5, 'M', size=24)
add_text(0, 1.8, 'N', size=24)
add_text(0, 3.2, 'δ', color='purple', size=28)

add_text(-1.5, -0.5, 'O', size=24)
add_text(-2.0, -1.0, 'P', size=24)
add_text(-1.2, -1.5, 'Q', size=24)

add_text(1.5, -0.5, 'R', size=24)
add_text(2.0, -1.0, 'S', size=24)
add_text(1.2, -1.5, 'T', size=24)

add_text(0, 0, 'U', size=28, weight='bold')
add_text(0, 0.8, 'V', size=24)
add_text(0, -0.8, 'W', size=24)

ax.set_xlim(-6, 6)
ax.set_ylim(-6, 6)
ax.set_aspect('equal')
ax.axis('off')

plt.tight_layout()
plt.show()
