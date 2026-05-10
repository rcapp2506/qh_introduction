"""
Two Quantum Revolutions diagram --- generator script for fig:revolutions
(Introduction chapter, Cap. 1 of the PhD thesis).

Produces a timeline-style schematic contrasting the First Quantum
Revolution (~1900--1980s, observation and understanding) with the
Second Quantum Revolution (~1980s--present, control and engineering).
The figure adapts the framing of Dowling & Milburn, Phil. Trans. R.
Soc. A (2003) and Deutsch, PRX Quantum (2020), which are cited in the
LaTeX caption.

Output: two_quantum_revolutions_improved_2.png (referenced verbatim by
chapters/introduction_revised.tex in the PhDThesis repository).

Usage:
    python two_quantum_revolutions_diagram.py
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np

# Create figure with high DPI for better quality
fig, ax = plt.subplots(figsize=(16, 10), dpi=150)

# Set white background
fig.patch.set_facecolor('white')
ax.set_facecolor('white')

# Title
plt.text(0.5, 0.95, 'Two Quantum Revolutions:', 
         ha='center', va='top', fontsize=32, fontweight='bold',
         transform=fig.transFigure)
plt.text(0.5, 0.89, 'From Observation to Engineering of Quantum Phenomena',
         ha='center', va='top', fontsize=20, style='italic',
         transform=fig.transFigure, color='gray')

# Timeline axis - positioned above dates, below events (slightly higher than before)
timeline_y = 0.45
ax.plot([1900, 2025], [timeline_y, timeline_y], 'k-', linewidth=2, zorder=1)

# Timeline ticks and labels - dates below the line
years = [1900, 1925, 1950, 1975, 2000, 2025]
for year in years:
    ax.plot([year, year], [timeline_y-0.01, timeline_y+0.01], 'k-', linewidth=2)
    ax.text(year, timeline_y-0.03, str(year), ha='center', va='top', fontsize=14, fontweight='bold')

# First Quantum Revolution box
box1 = FancyBboxPatch((1895, 0.65), 55, 0.25, 
                       boxstyle="round,pad=0.01", 
                       edgecolor='#4A90E2', facecolor='#E3F2FD', 
                       linewidth=3, zorder=2)
ax.add_patch(box1)

ax.text(1922.5, 0.85, 'FIRST QUANTUM REVOLUTION', 
        ha='center', va='center', fontsize=18, fontweight='bold', color='#4A90E2')
ax.text(1922.5, 0.81, '(~1900\u20131980s)',
        ha='center', va='center', fontsize=14, style='italic', color='#4A90E2')
ax.text(1922.5, 0.74, 'Observation & Understanding',
        ha='center', va='center', fontsize=15, fontweight='bold', color='#333')
ax.text(1922.5, 0.69, 'Wave-particle duality • Quantization of energy',
        ha='center', va='center', fontsize=12, color='#555')

# Key discoveries - First Revolution
discoveries_1 = [
    (1900, 'Planck:\nQuantization', 0.56),
    (1913, 'Bohr:\nAtomic model', 0.56),
    (1925, 'Quantum\nMechanics', 0.56),
    (1950, 'QED', 0.56),
    (1960, 'Laser', 0.56)
]

for year, label, y_pos in discoveries_1:
    ax.plot([year, year], [timeline_y, y_pos], 'b--', linewidth=1.5, alpha=0.6)
    ax.plot(year, y_pos, 'o', color='#4A90E2', markersize=12, zorder=3)
    ax.text(year, y_pos+0.01, label, ha='center', va='bottom', fontsize=11, 
            color='#4A90E2', fontweight='bold')

# Second Quantum Revolution box
box2 = FancyBboxPatch((1975, 0.65), 55, 0.25,
                       boxstyle="round,pad=0.01",
                       edgecolor='#E91E63', facecolor='#FCE4EC',
                       linewidth=3, zorder=2)
ax.add_patch(box2)

ax.text(2002.5, 0.85, 'SECOND QUANTUM REVOLUTION',
        ha='center', va='center', fontsize=18, fontweight='bold', color='#E91E63')
ax.text(2002.5, 0.81, '(~1980s\u2013Present)',
        ha='center', va='center', fontsize=14, style='italic', color='#E91E63')
ax.text(2002.5, 0.74, 'Control & Engineering',
        ha='center', va='center', fontsize=15, fontweight='bold', color='#333')
ax.text(2002.5, 0.69, 'Superposition • Entanglement • Individual quantum control',
        ha='center', va='center', fontsize=12, color='#555')

# Key discoveries - Second Revolution (alternating heights to avoid overlap)
discoveries_2 = [
    (1980, 'Aspect:\nBell test', 0.56, 11),
    (1995, 'Shor\nalgorithm', 0.56, 11),
    (2012, 'Haroche:\nQuantum\ncontrol', 0.56, 11),  # Più alto
    (2019, 'Quantum\nsupremacy', 0.52, 11)  # Più basso
]

for year, label, y_pos, fontsize in discoveries_2:
    ax.plot([year, year], [timeline_y, y_pos], color='#E91E63', 
            linestyle='--', linewidth=1.5, alpha=0.6)
    ax.plot(year, y_pos, 'o', color='#E91E63', markersize=12, zorder=3)
    ax.text(year, y_pos+0.01, label, ha='center', va='bottom', fontsize=fontsize,
            color='#E91E63', fontweight='bold')

# Technologies & Applications - First Revolution
tech_y = 0.30
ax.text(1922.5, tech_y+0.05, 'Technologies & Applications:',
        ha='center', va='bottom', fontsize=14, fontweight='bold', color='#4A90E2')

tech_1 = ['Transistors', 'Lasers', 'Atomic\nclocks', 'MRI/NMR',
          'LEDs', 'Solar\ncells', 'Semiconductors']
#tech_x_start = 1897
tech_x_start = 1897 
tech_1_spacing = 77 / (len(tech_1))

for i, tech in enumerate(tech_1):
    x_pos = tech_x_start + 3 + i * tech_1_spacing
    # Auto-fit box via bbox= keyword: width adapts to text content,
    # padding stays uniform across all boxes.
    ax.text(x_pos, tech_y-0.0325, tech, ha='center', va='center',
            fontsize=10.5, color='white', fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.4', facecolor='#4A90E2',
                      edgecolor='none', alpha=0.85))

# Technologies & Applications - Second Revolution
ax.text(2002.5, tech_y+0.05, 'Technologies & Applications:',
        ha='center', va='bottom', fontsize=14, fontweight='bold', color='#E91E63')

tech_2 = ['Quantum\ncomputers', 'Quantum\ncryptography', 'Quantum\nsensors',
          'Quantum\nsimulation', 'Quantum\nnetworks']
tech_2_x_start = 1977
tech_2_spacing = 53 / (len(tech_2))

for i, tech in enumerate(tech_2):
    x_pos = tech_2_x_start + 3 + i * tech_2_spacing
    # Same auto-fit pattern as tech_1: this is the fix for the
    # 'cryptography' truncation bug present in earlier versions of the
    # script, where a fixed-width FancyBboxPatch caused the longest word
    # (cryptography) to overflow into the white background, where the
    # white text became invisible.
    ax.text(x_pos, tech_y-0.0325, tech, ha='center', va='center',
            fontsize=10.5, color='white', fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.4', facecolor='#E91E63',
                      edgecolor='none', alpha=0.85))

# Key Distinction box at bottom
dist_box = FancyBboxPatch((1900, 0.08), 125, 0.13,
                          boxstyle="round,pad=0.01",
                          edgecolor='#333', facecolor='white',
                          linewidth=2.5, zorder=2)
ax.add_patch(dist_box)

ax.text(1962.5, 0.18, 'Key Distinction:',
        ha='center', va='center', fontsize=16, fontweight='bold', color='#333')

# Arrow and labels
arrow = FancyArrowPatch((1920, 0.12), (2000, 0.12),
                        arrowstyle='->', mutation_scale=30, 
                        linewidth=3, color='#333', zorder=3)
ax.add_patch(arrow)

ax.text(1920, 0.12, 'Using quantum effects\n in classical systems',
        ha='center', va='center', fontsize=12, color='#4A90E2',
        fontweight='bold', bbox=dict(boxstyle='round', facecolor='#E3F2FD', 
                                     edgecolor='#4A90E2', linewidth=2))

ax.text(2000, 0.12, 'Engineering quantum states\n at individual particle level',
        ha='center', va='center', fontsize=12, color='#E91E63',
        fontweight='bold', bbox=dict(boxstyle='round', facecolor='#FCE4EC',
                                     edgecolor='#E91E63', linewidth=2))

# Attribution: handled by the LaTeX caption in
# chapters/introduction_revised.tex (Dowling & Milburn 2003;
# Deutsch 2020). Intentionally not duplicated inside the PNG so
# that the asset can be reused in other contexts (slides, etc.)
# without locking in the attribution.

# Set axis limits and remove axes
ax.set_xlim(1890, 2035)
ax.set_ylim(0, 1)
ax.axis('off')

plt.tight_layout()
plt.savefig('two_quantum_revolutions_improved_2.png',
            dpi=300, bbox_inches='tight', facecolor='white')
print("Figure saved successfully!")
#plt.show()
