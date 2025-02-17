import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt

# KALKULATOR UTANG
class DebtCalculator:
    def __init__(self, principal, annual_interest_rate, periods):
        self.principal = principal 
        self.annual_interest_rate = annual_interest_rate / 100
        self.periods = periods  
        self.monthly_interest_rate = self.annual_interest_rate / 12  

    def calculate_monthly_installment(self):
        r = self.monthly_interest_rate
        n = self.periods
        P = self.principal
        
        A = (P * r * (1 + r)**n) / ((1 + r)**n - 1)
        return A

    def calculate_total_payment(self):
        return self.calculate_monthly_installment() * self.periods

    def calculate_total_interest(self):
        return self.calculate_total_payment() - self.principal

    def calculate_remaining_balance(self, paid_periods):
        r = self.monthly_interest_rate
        n = self.periods
        t = paid_periods
        P = self.principal
        
        remaining_balance = P * ((1 + r)**n - (1 + r)**t) / ((1 + r)**n - 1)
        return remaining_balance

# Fungsi untuk menampilkan hasil kalkulator utang
def show_debt_results():
    try:
        principal = float(entry_principal.get())
        interest_rate = float(entry_interest.get())
        periods = int(entry_periods.get())

        calculator = DebtCalculator(principal, interest_rate, periods)
        monthly_installment = calculator.calculate_monthly_installment()
        total_payment = calculator.calculate_total_payment()
        total_interest = calculator.calculate_total_interest()
        remaining_balance = calculator.calculate_remaining_balance(12)

        result_text = (
            f"Angsuran Bulanan: Rp {monthly_installment:,.2f}\n"
            f"Total Pembayaran: Rp {total_payment:,.2f}\n"
            f"Total Bunga: Rp {total_interest:,.2f}\n"
            f"Sisa Utang setelah 12 bulan: Rp {remaining_balance:,.2f}"
        )
        messagebox.showinfo("Hasil Kalkulasi Utang", result_text)
    except ValueError:
        messagebox.showerror("Input Error", "Masukkan angka yang valid!")

# Fungsi untuk kalkulator tabungan
def show_savings_results():
    try:
        income = float(entry_income.get())
        expenses = float(entry_expenses.get())
        annual_interest_rate = float(entry_savings_interest.get())
        years = int(entry_years.get())
        initial_savings = float(entry_initial_savings.get() or 0)

        monthly_savings = income - expenses
        if monthly_savings <= 0:
            messagebox.showerror("Error", "Pengeluaran lebih besar dari penghasilan!")
            return

        monthly_interest_rate = annual_interest_rate / 100 / 12
        total_months = years * 12
        savings_progress = []
        current_savings = initial_savings

        for _ in range(total_months):
            current_savings = current_savings * (1 + monthly_interest_rate) + monthly_savings
            savings_progress.append(current_savings)

        result_text = f"Total tabungan setelah {years} tahun: Rp {current_savings:,.2f}"
        messagebox.showinfo("Hasil Kalkulasi Tabungan", result_text)

        # graph
        plt.figure(figsize=(10, 6))
        plt.plot(range(1, total_months + 1), savings_progress, label="Perkembangan Tabungan")
        
        num_labels = 10  # banyak label yang ingin ditampilkan
        step = max(1, total_months // num_labels)  # interval label
        for i in range(0, total_months, step):
            plt.text(i + 1, savings_progress[i], f"Rp{savings_progress[i]:,.0f}", fontsize=8, ha='right')
        
        plt.title("Grafik Perkembangan Tabungan")
        plt.xlabel("Bulan")
        plt.ylabel("Total Tabungan (Rp)")
        plt.grid(True)
        plt.legend()
        plt.tight_layout()
        plt.show()

    except ValueError:
        messagebox.showerror("Input Error", "Masukkan angka yang valid!")

# GUI dengan Tkinter
root = tk.Tk()
root.title("Kalkulator Utang & Tabungan")
root.geometry("1000x500")

# Input untuk kalkulator utang
tk.Label(root, text="Kalkulator Utang").pack()
tk.Label(root, text="Jumlah Utang (Rp)").pack()
entry_principal = tk.Entry(root)
entry_principal.pack()
tk.Label(root, text="Bunga Tahunan (%)").pack()
entry_interest = tk.Entry(root)
entry_interest.pack()
tk.Label(root, text="Lama Cicilan (bulan)").pack()
entry_periods = tk.Entry(root)
entry_periods.pack()
tk.Button(root, text="Hitung Utang", command=show_debt_results).pack(pady=5)

# Input untuk kalkulator tabungan
tk.Label(root, text="Kalkulator Tabungan").pack()
tk.Label(root, text="Penghasilan Bulanan (Rp)").pack()
entry_income = tk.Entry(root)
entry_income.pack()
tk.Label(root, text="Pengeluaran Bulanan (Rp)").pack()
entry_expenses = tk.Entry(root)
entry_expenses.pack()
tk.Label(root, text="Bunga Tabungan Tahunan (%)").pack()
entry_savings_interest = tk.Entry(root)
entry_savings_interest.pack()
tk.Label(root, text="Durasi Menabung (tahun)").pack()
entry_years = tk.Entry(root)
entry_years.pack()
tk.Label(root, text="Tabungan Awal (opsional)").pack()
entry_initial_savings = tk.Entry(root)
entry_initial_savings.pack()
tk.Button(root, text="Hitung Tabungan", command=show_savings_results).pack(pady=5)

root.mainloop()
