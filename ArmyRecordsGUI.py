import tkinter as tk
from tkinter import messagebox
from ArmyRecords import ArmyRecords
from CalculateBMI import CalculateBMI

class ArmyRecordsGUI:
    def __init__(self, master):
        # Initializes the GUI window
        self.master = master
        self.master.title("Army Records GUI")
        self.army_records = ArmyRecords()
        self.create_widgets()

    def create_widgets(self):
        # Creates labels, entry fields, buttons, and text windows for the GUI
        tk.Label(self.master, text="Rank:").grid(row=0, column=0)
        tk.Label(self.master, text="Last Name:").grid(row=1, column=0)
        tk.Label(self.master, text="First Name:").grid(row=2, column=0)
        tk.Label(self.master, text="Age:").grid(row=3, column=0)
        tk.Label(self.master, text="Height (in):").grid(row=4, column=0)
        tk.Label(self.master, text="Weight (lb):").grid(row=5, column=0)
        tk.Label(self.master, text="ETS (YYYYMMDD):").grid(row=6, column=0)

        self.rank_entry = tk.Entry(self.master)
        self.rank_entry.grid(row=0, column=1)
        self.last_name_entry = tk.Entry(self.master)
        self.last_name_entry.grid(row=1, column=1)
        self.first_name_entry = tk.Entry(self.master)
        self.first_name_entry.grid(row=2, column=1)
        self.age_entry = tk.Entry(self.master)
        self.age_entry.grid(row=3, column=1)
        self.height_entry = tk.Entry(self.master)
        self.height_entry.grid(row=4, column=1)
        self.weight_entry = tk.Entry(self.master)
        self.weight_entry.grid(row=5, column=1)
        self.ets_entry = tk.Entry(self.master)
        self.ets_entry.grid(row=6, column=1)

        tk.Button(self.master, text="Add Record", command=self.add_record).grid(row=7, column=0, columnspan=2)
        tk.Button(self.master, text="Print by Last Name (Quick Sort)", command=self.print_by_last_name).grid(row=8, column=0, columnspan=2)
        tk.Button(self.master, text="Print by ETS (Priority Queue)", command=self.print_by_ets).grid(row=9, column=0, columnspan=2)
        tk.Button(self.master, text="Clear Entries", command=self.clear_entries).grid(row=10, column=0, columnspan=2)

        self.text_widget = tk.Text(self.master, height=10, width=50)
        self.text_widget.grid(row=11, column=0, columnspan=2)

    def add_record(self):
        # Gets entry fields
        rank = self.rank_entry.get()
        last_name = self.last_name_entry.get()
        first_name = self.first_name_entry.get()
        age_str = self.age_entry.get()
        height_str = self.height_entry.get()
        weight_str = self.weight_entry.get()
        ets = self.ets_entry.get()

        try:
            age = int(age_str)
            height = int(height_str)
            weight = int(weight_str)

            # Validate age, height, and weight
            if not all(val > 0 for val in (age, height, weight)):
                raise ValueError("Age, height, and weight must be positive integers.")

            bmi = CalculateBMI.calculate_bmi(weight, height)

            self.army_records.add_record(rank, last_name, first_name, age, height, weight, ets)
            self.rank_entry.delete(0, tk.END)
            self.last_name_entry.delete(0, tk.END)
            self.first_name_entry.delete(0, tk.END)
            self.age_entry.delete(0, tk.END)
            self.height_entry.delete(0, tk.END)
            self.weight_entry.delete(0, tk.END)
            self.ets_entry.delete(0, tk.END)

        # Detailed error message for invalid input.
        except ValueError as e:
            messagebox.showerror("Error", f"Invalid input: {str(e)} Please enter valid positive integers for age, height, and weight.")

    # Print by last name using quick sort
    def print_by_last_name(self):
        self.update_records_display()
        self.army_records.print_records_by_last_name()

    # Print by ETS using Priority Queue
    def print_by_ets(self):
        self.update_records_display()
        self.army_records.print_records_by_ets()

    # Clears the text widget and updates it with latest records
    def update_records_display(self):
        self.text_widget.delete(1.0, tk.END)
        records = self.army_records.get_records()
        for record in records:
            self.text_widget.insert(tk.END, f"Rank: {record['Rank']}, Last Name: {record['Last Name']}, "
                                            f"First Name: {record['First Name']}, Age: {record['Age']}, "
                                            f"Height: {record['Height']}, Weight: {record['Weight']}, "
                                            f"ETS: {record['ETS'].strftime('%Y%m%d')}, BMI: {record['BMI']:.2f}\n")

    # Clears all entry fields
    def clear_entries(self):
        self.rank_entry.delete(0, tk.END)
        self.last_name_entry.delete(0, tk.END)
        self.first_name_entry.delete(0, tk.END)
        self.age_entry.delete(0, tk.END)
        self.height_entry.delete(0, tk.END)
        self.weight_entry.delete(0, tk.END)
        self.ets_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ArmyRecordsGUI(root)
    root.mainloop()
