import tkinter as tk
from tkinter import Label, Entry, Frame
from button_heat_map import create_head_map

def create_dual_tables(data0, data1, data2):
    # Create a new top-level window
    ventana = tk.Tk()
    ventana.title("Dual Tables")
    
     # Create frame for net profit
    frame = tk.Frame(ventana, bd=2, relief="solid", bg="yellow")
    frame.grid(row=0, column=0, columnspan=len(data1[0]) + 1, pady=(10, 20), padx=10, sticky="ew")
    
    # Create label for net profit
    net_profit_label = tk.Label(frame, text="Net profit:", font=('Arial', 14, 'bold'), bg="yellow")
    net_profit_label.grid(row=0, column=0, sticky="w", padx=5)

    # Create label for net profit value
    net_profit_value = tk.Label(frame, text=str(data0), font=('Arial', 14), bg="yellow")
    net_profit_value.grid(row=0, column=1, sticky="e", padx=5)

    # Create first table
    create_table(ventana, "Production", "Plant", data1, row_offset=1)

    # Create second table
    create_table(ventana, "Delivered", "Customer" , data2, row_offset=len(data1)+4)
    
    # Insert button
    heatmap_button = create_head_map(frame, data1, data2)
    heatmap_button.grid(row=0, column=2, padx=5)

    # Mostrar la ventana
    ventana.mainloop()

    return ventana

def create_table(parent, title, label, data, row_offset):
    # Create a label for the table title
    title_label = Label(parent, text=title, font=('Arial', 16, 'bold'))
    title_label.grid(row=row_offset, column=0, columnspan=len(data[0])+1, sticky='ew', pady=(10, 20))

    # Create headers
    Label(parent, text=label, font=('Arial', 12, 'bold')).grid(row=row_offset+1, column=0, sticky='ew')
    for i in range(len(data[0])):
        Label(parent, text=f"Day {i+1}", font=('Arial', 12, 'bold')).grid(row=row_offset+1, column=i+1, sticky='ew')

    # Create rows with data
    for idx, row in enumerate(data, start=1):
        Label(parent, text=f"{label} {idx}:", font=('Arial', 12)).grid(row=row_offset+idx+1, column=0, sticky='ew')
        for j, cell in enumerate(row):
            entry = Entry(parent, font=('Arial', 12), justify='center')
            entry.grid(row=row_offset+idx+1, column=j+1, sticky='ew')
            entry.insert(0, str(cell))
            entry.config(state='readonly')

    # Adjust column weights so they expand equally
    for i in range(len(data[0])+1):
        parent.grid_columnconfigure(i, weight=1)

    # Adjust row weights so they expand equally
    for i in range(len(data)+2):
        parent.grid_rowconfigure(row_offset+i+1, weight=1)

    # Set minimum size for the window
    parent.update()
    parent.minsize(parent.winfo_width(), parent.winfo_height())
