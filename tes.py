# pip install pyinstaller
# pip install matplotlib as plt
 
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
        monthly_installment = self.calculate_monthly_installment()
        return monthly_installment * self.periods

    def calculate_total_interest(self):
        total_payment = self.calculate_total_payment()
        return total_payment - self.principal

    def calculate_remaining_balance(self, paid_periods):
        r = self.monthly_interest_rate
        n = self.periods
        t = paid_periods
        P = self.principal
        
        remaining_balance = P * ((1 + r)**n - (1 + r)**t) / ((1 + r)**n - 1)
        return remaining_balance

    def calculate_interest_for_period(self, remaining_balance):
        return remaining_balance * self.monthly_interest_rate

# KALKULATOR TABUNGAN
import matplotlib.pyplot as plt

def future_savings_calculator():
    print("Savings Calculator")
    
    income = float(input("Penghasilan bulanan (Rp): "))
    expenses = float(input("Pengeluaran bulanan (Rp): "))
    annual_interest_rate = float(input("Bunga tahunan (%): "))
    years = int(input("Durasi menabung (tahun): "))
    initial_savings = float(input("Tabungan awal (Rp, opsional, default 0): ") or 0)

    monthly_savings = income - expenses
    if monthly_savings <= 0:
        print("Pengeluaran lebih besar atau sama dengan penghasilan. Tidak ada tabungan yang bisa dihitung.")
        return

    monthly_interest_rate = annual_interest_rate / 100 / 12
    total_months = years * 12

    # savings simulation development
    savings_progress = []
    current_savings = initial_savings

    for month in range(1, total_months + 1):
        current_savings = current_savings * (1 + monthly_interest_rate) + monthly_savings
        savings_progress.append(current_savings)

    print(f"\nTotal tabungan di akhir {years} tahun: Rp{current_savings:,.2f}")

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

if __name__ == "__main__":
    principal = int(input("Utang: "))  
    annual_interest_rate = int(input("annual interest rate: "))
    periods = int(input("angusran: "))

    calculator = DebtCalculator(principal, annual_interest_rate, periods)

    monthly_installment = calculator.calculate_monthly_installment()
    print(f"Angsuran Bulanan: Rp {monthly_installment:,.2f}")

    total_payment = calculator.calculate_total_payment()
    print(f"Total Pembayaran: Rp {total_payment:,.2f}")

    total_interest = calculator.calculate_total_interest()
    print(f"Total Bunga yang Dibayar: Rp {total_interest:,.2f}")

    paid_periods = 12  
    remaining_balance = calculator.calculate_remaining_balance(paid_periods)
    print(f"Sisa Utang setelah {paid_periods} bulan: Rp {remaining_balance:,.2f}")

    interest_for_period = calculator.calculate_interest_for_period(remaining_balance)
    print(f"Bunga untuk bulan berikutnya: Rp {interest_for_period:,.2f}")

    # KALKULATOR TABUNGAN
    future_savings_calculator()








