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
    future_savings_calculator()
