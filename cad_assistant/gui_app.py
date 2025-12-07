
import tkinter as tk
from tkinter import ttk, messagebox
import sys
import os

# Ensure we can import local modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from cad_assistant import materials, tips, prototype_logger, calculator, cad_basics

class CADAssistantApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("CAD & Prototyping Assistant")
        self.geometry("800x600")

        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill='both', expand=True, padx=10, pady=10)

        # Initialize Tabs
        self.create_materials_tab()
        self.create_tips_tab()
        self.create_logger_tab()
        self.create_calculator_tab()
        self.create_basics_tab()

    def create_materials_tab(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Materials")

        # Layout
        frame_left = ttk.Frame(tab)
        frame_left.pack(side='left', fill='y', padx=10, pady=10)

        frame_right = ttk.Frame(tab)
        frame_right.pack(side='right', fill='both', expand=True, padx=10, pady=10)

        # Listbox for Materials
        lbl_list = ttk.Label(frame_left, text="Select Material:")
        lbl_list.pack(anchor='w')

        self.mat_listbox = tk.Listbox(frame_left, height=20)
        self.mat_listbox.pack(fill='y', expand=True)
        self.mat_listbox.bind('<<ListboxSelect>>', self.on_material_select)

        for mat in materials.list_materials():
            self.mat_listbox.insert(tk.END, mat)

        # Details View
        self.mat_text = tk.Text(frame_right, wrap='word', state='disabled')
        self.mat_text.pack(fill='both', expand=True)

    def on_material_select(self, event):
        selection = self.mat_listbox.curselection()
        if not selection:
            return

        mat_name = self.mat_listbox.get(selection[0])
        info = materials.get_material_info(mat_name)

        content = f"--- {mat_name} ---\n\n"
        content += f"Description: {info['description']}\n\n"
        content += f"Nozzle Temp: {info['nozzle_temp']}\n"
        content += f"Bed Temp:    {info['bed_temp']}\n"
        content += f"Shrinkage:   {info['shrinkage']}\n\n"
        content += "Pros:\n"
        for pro in info['pros']:
            content += f"  + {pro}\n"
        content += "\nCons:\n"
        for con in info['cons']:
            content += f"  - {con}\n"

        self.mat_text.config(state='normal')
        self.mat_text.delete(1.0, tk.END)
        self.mat_text.insert(tk.END, content)
        self.mat_text.config(state='disabled')

    def create_tips_tab(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Design Tips")

        # Categories Combo
        frame_top = ttk.Frame(tab)
        frame_top.pack(fill='x', padx=10, pady=10)

        lbl_cat = ttk.Label(frame_top, text="Category:")
        lbl_cat.pack(side='left', padx=(0, 10))

        self.tips_combo = ttk.Combobox(frame_top, values=tips.get_all_categories(), state="readonly")
        self.tips_combo.pack(side='left', fill='x', expand=True)
        self.tips_combo.bind('<<ComboboxSelected>>', self.on_tip_category_select)

        # Text Area
        self.tips_text = tk.Text(tab, wrap='word', state='disabled')
        self.tips_text.pack(fill='both', expand=True, padx=10, pady=10)

    def on_tip_category_select(self, event):
        cat = self.tips_combo.get()
        cat_tips = tips.get_tips_by_category(cat)

        content = f"--- {cat} Tips ---\n\n"
        for t in cat_tips:
            content += f"* {t}\n\n"

        self.tips_text.config(state='normal')
        self.tips_text.delete(1.0, tk.END)
        self.tips_text.insert(tk.END, content)
        self.tips_text.config(state='disabled')

    def create_logger_tab(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Prototype Logger")

        # Split into List (Left) and Details/Add (Right)
        paned = ttk.PanedWindow(tab, orient='horizontal')
        paned.pack(fill='both', expand=True, padx=10, pady=10)

        frame_list = ttk.Frame(paned)
        frame_details = ttk.Frame(paned)
        paned.add(frame_list, weight=1)
        paned.add(frame_details, weight=2)

        # Left Side: List
        lbl_ideas = ttk.Label(frame_list, text="Saved Ideas:")
        lbl_ideas.pack(anchor='w')

        self.idea_listbox = tk.Listbox(frame_list)
        self.idea_listbox.pack(fill='both', expand=True)
        self.idea_listbox.bind('<<ListboxSelect>>', self.on_idea_select)

        btn_refresh = ttk.Button(frame_list, text="Refresh List", command=self.refresh_ideas)
        btn_refresh.pack(fill='x', pady=5)

        btn_delete = ttk.Button(frame_list, text="Delete Selected", command=self.delete_selected_idea)
        btn_delete.pack(fill='x')

        # Right Side: Details & Add
        lbl_title = ttk.Label(frame_details, text="Title:")
        lbl_title.pack(anchor='w')
        self.entry_title = ttk.Entry(frame_details)
        self.entry_title.pack(fill='x', pady=(0, 10))

        lbl_desc = ttk.Label(frame_details, text="Description:")
        lbl_desc.pack(anchor='w')
        self.text_desc = tk.Text(frame_details, height=10)
        self.text_desc.pack(fill='x', pady=(0, 10))

        btn_save = ttk.Button(frame_details, text="Save New Idea", command=self.save_new_idea)
        btn_save.pack(anchor='e')

        self.refresh_ideas()

    def refresh_ideas(self):
        self.idea_listbox.delete(0, tk.END)
        self.current_ideas = prototype_logger.list_ideas()
        for idea in self.current_ideas:
            self.idea_listbox.insert(tk.END, idea['title'])

    def on_idea_select(self, event):
        selection = self.idea_listbox.curselection()
        if not selection:
            return

        idx = selection[0]
        idea = self.current_ideas[idx]

        # Populate fields (read-only mode essentially, but editable if they want to copy-paste)
        self.entry_title.delete(0, tk.END)
        self.entry_title.insert(0, idea['title'])
        self.text_desc.delete(1.0, tk.END)
        self.text_desc.insert(tk.END, idea['description'])

    def save_new_idea(self):
        title = self.entry_title.get().strip()
        desc = self.text_desc.get("1.0", tk.END).strip()

        if not title:
            messagebox.showerror("Error", "Title is required!")
            return

        prototype_logger.save_idea(title, desc)
        messagebox.showinfo("Success", "Idea saved!")
        self.refresh_ideas()

        # Clear form
        self.entry_title.delete(0, tk.END)
        self.text_desc.delete(1.0, tk.END)

    def delete_selected_idea(self):
        selection = self.idea_listbox.curselection()
        if not selection:
            return

        idx = selection[0]
        confirm = messagebox.askyesno("Confirm", "Are you sure you want to delete this idea?")
        if confirm:
            prototype_logger.delete_idea(idx)
            self.refresh_ideas()

    def create_calculator_tab(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Cost Calculator")

        frame = ttk.Frame(tab, padding=20)
        frame.pack(fill='both', expand=True)

        # Inputs
        ttk.Label(frame, text="Weight (g):").grid(row=0, column=0, sticky='w', pady=5)
        self.calc_weight = ttk.Entry(frame)
        self.calc_weight.grid(row=0, column=1, pady=5)

        ttk.Label(frame, text="Cost per kg ($):").grid(row=1, column=0, sticky='w', pady=5)
        self.calc_cost_kg = ttk.Entry(frame)
        self.calc_cost_kg.grid(row=1, column=1, pady=5)

        # Electricity (Optional)
        ttk.Label(frame, text="Print Time (hours):").grid(row=2, column=0, sticky='w', pady=5)
        self.calc_hours = ttk.Entry(frame)
        self.calc_hours.grid(row=2, column=1, pady=5)

        ttk.Label(frame, text="Power (Watts):").grid(row=3, column=0, sticky='w', pady=5)
        self.calc_watts = ttk.Entry(frame)
        self.calc_watts.insert(0, "150") # Default
        self.calc_watts.grid(row=3, column=1, pady=5)

        ttk.Label(frame, text="Elec Cost ($/kWh):").grid(row=4, column=0, sticky='w', pady=5)
        self.calc_kwh = ttk.Entry(frame)
        self.calc_kwh.insert(0, "0.12") # Default
        self.calc_kwh.grid(row=4, column=1, pady=5)

        # Calculate Button
        btn_calc = ttk.Button(frame, text="Calculate", command=self.perform_calculation)
        btn_calc.grid(row=5, column=0, columnspan=2, pady=20)

        # Results
        self.lbl_result = ttk.Label(frame, text="Total Cost: $0.00", font=('Arial', 14, 'bold'))
        self.lbl_result.grid(row=6, column=0, columnspan=2)

    def perform_calculation(self):
        try:
            w = float(self.calc_weight.get())
            c_kg = float(self.calc_cost_kg.get())

            # Optional electricity
            h_str = self.calc_hours.get()
            if h_str:
                h = float(h_str)
                watts = float(self.calc_watts.get())
                kwh = float(self.calc_kwh.get())
                total = calculator.calculate_total_cost(w, c_kg, h, watts, kwh)
            else:
                total = calculator.calculate_cost(w, c_kg)

            self.lbl_result.config(text=f"Total Cost: ${total:.2f}")

        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers.")

    def create_basics_tab(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="CAD Basics")

        # Sub-tabs for Tools vs Shortcuts
        sub_notebook = ttk.Notebook(tab)
        sub_notebook.pack(fill='both', expand=True, padx=10, pady=10)

        # Tools Tab
        tab_tools = ttk.Frame(sub_notebook)
        sub_notebook.add(tab_tools, text="Common Tools")

        self.tools_text = tk.Text(tab_tools, wrap='word', padx=10, pady=10)
        self.tools_text.pack(fill='both', expand=True)

        tools_content = ""
        for tool in cad_basics.list_tools():
            tools_content += f"{tool}:\n   {cad_basics.get_tool_explanation(tool)}\n\n"

        self.tools_text.insert(tk.END, tools_content)
        self.tools_text.config(state='disabled')

        # Shortcuts Tab
        tab_shortcuts = ttk.Frame(sub_notebook)
        sub_notebook.add(tab_shortcuts, text="Keyboard Shortcuts")

        self.shortcuts_text = tk.Text(tab_shortcuts, wrap='word', padx=10, pady=10)
        self.shortcuts_text.pack(fill='both', expand=True)

        sc_content = ""
        for sw in cad_basics.list_software():
            sc_content += f"=== {sw} ===\n"
            shortcuts = cad_basics.get_shortcuts_for_software(sw)
            for key, action in shortcuts.items():
                sc_content += f"  {key}: {action}\n"
            sc_content += "\n"

        self.shortcuts_text.insert(tk.END, sc_content)
        self.shortcuts_text.config(state='disabled')

if __name__ == "__main__":
    app = CADAssistantApp()
    app.mainloop()
