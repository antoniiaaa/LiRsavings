# pip install pyinstaller

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
