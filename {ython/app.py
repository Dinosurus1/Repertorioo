import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

class AgendaApp:
    def init(self, root):
        self.root = root
        self.appointments = []
        self.current_appointment = None


        self.root.title("Agenda Personal")
        self.root.geometry("400x600")


        self.top_frame = ttk.Frame(self.root)
        self.top_frame.pack(pady=10)


        self.title_label = ttk.Label(self.top_frame, text="Título:")
        self.title_label.grid(row=0, column=0, padx=5)
        self.title_entry = ttk.Entry(self.top_frame)
        self.title_entry.grid(row=0, column=1, padx=5)

        self.date_label = ttk.Label(self.top_frame, text="Fecha:")
        self.date_label.grid(row=1, column=0, padx=5)
        self.date_entry = ttk.Entry(self.top_frame)
        self.date_entry.grid(row=1, column=1, padx=5)

        self.time_label = ttk.Label(self.top_frame, text="Hora:")
        self.time_label.grid(row=2, column=0, padx=5)
        self.time_entry = ttk.Entry(self.top_frame)
        self.time_entry.grid(row=2, column=1, padx=5)


        self.button_frame = ttk.Frame(self.root)
        self.button_frame.pack(pady=10)

        self.add_button = ttk.Button(self.button_frame, text="Agregar", command=self.add_appointment)
        self.add_button.grid(row=0, column=0, padx=5)

        self.edit_button = ttk.Button(self.button_frame, text="Editar", command=self.edit_appointment)
        self.edit_button.grid(row=0, column=1, padx=5)

        self.delete_button = ttk.Button(self.button_frame, text="Eliminar", command=self.delete_appointment)
        self.delete_button.grid(row=0, column=2, padx=5)


        self.appointments_listbox = tk.Listbox(self.root)
        self.appointments_listbox.pack(pady=10, fill=tk.BOTH, expand=True)
        self.appointments_listbox.bind("<<ListboxSelect>>", self.select_appointment)

    def add_appointment(self):
        title = self.title_entry.get()
        date_str = self.date_entry.get()
        time_str = self.time_entry.get()

        try:
            datetime.strptime(date_str, "%d/%m/%Y")
            datetime.strptime(time_str, "%H:%M")

            new_id = len(self.appointments) + 1
            appointment = {
                "id": new_id,
                "title": title,
                "date": date_str,
                "time": time_str
            }
            self.appointments.append(appointment)
            self.update_listbox()
            messagebox.showinfo("Exito", "Cita agregada correctamente.")
        except ValueError:
            messagebox.showerror("Error", "Fecha o hora no válida.")

    def edit_appointment(self):
        if not self.current_appointment:
            messagebox.showerror("Error", "Seleccione una cita para editar.")
            return

        title = self.title_entry.get()
        date_str = self.date_entry.get()
        time_str = self.time_entry.get()

        try:
            datetime.strptime(date_str, "%d/%m/%Y")
            datetime.strptime(time_str, "%H:%M")

            index = next(i for i, a in enumerate(self.appointments) if a["id"] == self.current_appointment["id"])
            self.appointments[index] = {
                "id": self.appointments[index]["id"],
                "title": title,
                "date": date_str,
                "time": time_str
            }
            self.update_listbox()
            messagebox.showinfo("Exito", "Cita actualizada correctamente.")
        except ValueError:
            messagebox.showerror("Error", "Fecha o hora no válida.")

    def delete_appointment(self):
        if not self.current_appointment:
            messagebox.showerror("Error", "Seleccione una cita para eliminar.")
            return

        index = next(i for i, a in enumerate(self.appointments) if a["id"] == self.current_appointment["id"])
        del self.appointments[index]
        self.update_listbox()
        messagebox.showinfo("Exito", "Cita eliminada correctamente.")

    def select_appointment(self, event):
        widget = event.widget
        index = int(widget.curselection()[0])
        self.current_appointment = self.appointments[index]


        self.title_entry.delete(0, tk.END)
        self.title_entry.insert(0, self.current_appointment["title"])

        self.date_entry.delete(0, tk.END)
        self.date_entry.insert(0, self.current_appointment["date"])

        self.time_entry.delete(0, tk.END)
        self.time_entry.insert(0, self.current_appointment["time"])

    def update_listbox(self):
        self.appointments_listbox.delete(0, tk.END)
        for appointment in self.appointments:
            date_str = f"{appointment['date']} {appointment['time']}"
            display_text = f"[{appointment['id']}]{appointment['title']} ({date_str})"
            self.appointments_listbox.insert(tk.END, display_text)

if __name__ == "main":
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()