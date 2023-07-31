import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import numpy as np

# Data for the religious groups and their population in India
religious_groups = ["Hindu", "Muslim", "Christian", "Sikh", "Buddhist", "Jain", "Other"]
population = [61.5 ,14.2, 10.0, 4.0, 2.0, 6.4, 1.9]

# Create a function to display the pie chart
def show_pie_chart():
    fig, ax = plt.subplots()
    ax.pie(population, labels=religious_groups, autopct='%1.1f%%', startangle=50)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.title("Religious Distribution in India (Percentage)")
    plt.show()

# Create a function to display the bar graph
def show_bar_graph():
    plt.bar(religious_groups, population)
    plt.xlabel("Religions in India")
    plt.ylabel("Population (%)")
    plt.title("Religious Distribution in India")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Create the Tkinter application
root = tk.Tk()
root.title("Indian Religious Distribution")

# Create a button to display the pie chart
pie_button = ttk.Button(root, text="Show Pie Chart", command=show_pie_chart)
pie_button.pack(pady=10)

# Create a button to display the bar graph
bar_button = ttk.Button(root, text="Show Bar Graph", command=show_bar_graph)
bar_button.pack(pady=10)

# Run the Tkinter main loop
root.mainloop()
