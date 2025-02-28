import tkinter as tk
from tkinter import ttk
import pygame as pg
pg.init()

translations = {
    "en": {"Language": "Language","Enter amount:": "Enter amount:", "From:": "From:", "To:": "To:", "Convert": "Convert", "Invalid input": "Invalid input", "Converted:": "Converted:"},
    "de": {"Language":"Sprache","Enter amount:": "Betrag eingeben:", "From:": "Von:", "To:": "Nach:", "Convert": "Umrechnen", "Invalid input": "Ungültige Eingabe", "Converted:": "Umgewandelt:"},
    "it": {"Language":"Lingua","Enter amount:": "Inserisci l'importo:", "From:": "Da:", "To:": "A:", "Convert": "Convertire", "Invalid input": "Input non valido", "Converted:": "Convertito:"}
}

class CurrencyConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Currency Converter")
        self.root.geometry("300x300")

        self.rates = {"USD": 1, "Euro": 0.96, "Yen": 150.55, "ITL": 1847.12, "GBP": 0.79}
        self.language = "en" 

        self.lang_label = tk.Label(root, text="Language")
        self.lang_label.pack()
        self.lang_select = ttk.Combobox(root, values=["en", "de", "it"], state="readonly")
        self.lang_select.pack()
        self.lang_select.set("en")
        self.lang_select.bind("<<ComboboxSelected>>", self.update_language)
        
        self.label = tk.Label(root, text=translations[self.language]["Enter amount:"])
        self.label.pack(pady=5)
        
        self.entry = tk.Entry(root)
        self.entry.pack(pady=5)
        
        self.from_label = tk.Label(root, text=translations[self.language]["From:"])
        self.from_label.pack(pady=5)
        
        self.from_currency = ttk.Combobox(root, values=list(self.rates.keys()),state="readonly")
        self.from_currency.pack(pady=5)
        
        self.to_label = tk.Label(root, text=translations[self.language]["To:"])
        self.to_label.pack(pady=5)
        
        self.to_currency = ttk.Combobox(root, values=list(self.rates.keys()), state="readonly")
        self.to_currency.pack(pady=5)
        
        self.button = tk.Button(root, text=translations[self.language]["Convert"], command=self.on_click)
        self.button.pack(pady=10)
        
        self.result_label = tk.Label(root, text="")
        self.result_label.pack(pady=5)
    
    def update_language(self, event):
        self.language = self.lang_select.get()
        self.lang_label.config(text=translations[self.language]["Language"])
        self.label.config(text=translations[self.language]["Enter amount:"])
        self.from_label.config(text=translations[self.language]["From:"])
        self.to_label.config(text=translations[self.language]["To:"])
        self.button.config(text=translations[self.language]["Convert"])
    
    def on_click(self):
        try:
            fart = pg.mixer.Sound(r"D:\1_HTL\3aHEL\3a_FSST_Labor\6_GitHubTeil2\sfx\fart.mp3")
            amount = float(self.entry.get())
            from_curr = self.from_currency.get()
            to_curr = self.to_currency.get()
            result = self.convert_currency(amount, from_curr, to_curr)
            fart.play()
            self.result_label.config(text=f"{translations[self.language]["Converted:"]} {result:.2f} {to_curr}")
        except ValueError:
            buzzer = pg.mixer.Sound(r"D:\1_HTL\3aHEL\3a_FSST_Labor\6_GitHubTeil2\sfx\buzzer.mp3")
            self.result_label.config(text=translations[self.language]["Invalid input"])
            buzzer.play()

    
    def convert_currency(self, amount, currency_from, currency_to):
        if currency_from in self.rates and currency_to in self.rates:
            amount_in_usd = amount / self.rates[currency_from]  
            return amount_in_usd * self.rates[currency_to]  
        return amount

if __name__ == "__main__":
    root = tk.Tk()
    app = CurrencyConverter(root)
    root.mainloop()