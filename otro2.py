import tkinter as tk
from tkinter import messagebox

# Function to validate and retrieve data from entries
def get_data():
    try:
        # Retrieve and validate data from entries
        n = int(n_entry.get())
        m = int(m_entry.get())
        consecutive_high_days_allowed = int(chda_entry.get())
        high_regime_percentage = float(hrp_entry.get())
        capacity = list(map(int, capacity_entry.get().split(',')))
        production_cost = list(map(float, pc_entry.get().split(',')))
        demand = [list(map(int, row.split(','))) for row in demand_text.get("1.0", tk.END).strip().split('\n')]
        payment_per_mw = list(map(float, ppm_entry.get().split(',')))
        G = float(G_entry.get())

        # Check if the lengths of lists match n and m
        if len(capacity) != n or len(production_cost) != n or len(payment_per_mw) != m or len(demand) != m:
            raise ValueError("List lengths do not match n or m.")

        # Display the data
        messagebox.showinfo("Data Retrieved", f"n: {n}\nm: {m}\nConsecutive High Days Allowed: {consecutive_high_days_allowed}\n"
                                             f"High Regime Percentage: {high_regime_percentage}\nCapacity: {capacity}\n"
                                             f"Production Cost: {production_cost}\nDemand: {demand}\n"
                                             f"Payment per MW: {payment_per_mw}\nG: {G}")
    except ValueError as ve:
        messagebox.showerror("Error", f"Invalid input: {ve}")

# Create the main window
root = tk.Tk()
root.title("Data Input Interface")

# Create and place labels and entries for each variable
tk.Label(root, text="Number of days (n):").grid(row=0, column=0)
n_entry = tk.Entry(root)
n_entry.grid(row=0, column=1)

tk.Label(root, text="Number of customers (m):").grid(row=1, column=0)
m_entry = tk.Entry(root)
m_entry.grid(row=1, column=1)

tk.Label(root, text="Consecutive High Days Allowed:").grid(row=2, column=0)
chda_entry = tk.Entry(root)
chda_entry.grid(row=2, column=1)

tk.Label(root, text="High Regime Percentage:").grid(row=3, column=0)
hrp_entry = tk.Entry(root)
hrp_entry.grid(row=3, column=1)

tk.Label(root, text="Capacity (comma-separated):").grid(row=4, column=0)
capacity_entry = tk.Entry(root)
capacity_entry.grid(row=4, column=1)

tk.Label(root, text="Production Cost (comma-separated):").grid(row=5, column=0)
pc_entry = tk.Entry(root)
pc_entry.grid(row=5, column=1)

tk.Label(root, text="Demand (rows comma-separated, new line for each day):").grid(row=6, column=0)
demand_text = tk.Text(root, height=5, width=30)
demand_text.grid(row=6, column=1)

tk.Label(root, text="Payment per MW (comma-separated):").grid(row=7, column=0)
ppm_entry = tk.Entry(root)
ppm_entry.grid(row=7, column=1)

tk.Label(root, text="Minimum satisfaction percentage for each customer (G):").grid(row=8, column=0)
G_entry = tk.Entry(root)
G_entry.grid(row=8, column=1)

# Create and place the submit button
submit_button = tk.Button(root, text="Submit", command=get_data)
submit_button.grid(row=9, column=0, columnspan=2)

# Run the main loop
root.mainloop()
