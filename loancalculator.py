from tkinter import *
font_family = "Helvetica 15 bold"
green = "#135029"
red = "#B03737"
blue = "#1F2B8F"
white = "#FAFAFA"


class LoanCalculator:
    def __init__(self):
        csa = Tk()
        csa.title("Loan Calculator")
        csa.configure(background=green)

        Label(csa, font=font_family, bg=green,
              text="Annual Interest Rate").grid(row=1, column=1, sticky=W)
        Label(csa, font=font_family, bg=green,
              text="Number of Years").grid(row=2, column=1, sticky=W)
        Label(csa, font=font_family, bg=green,
              text="Loan Amount").grid(row=3, column=1, sticky=W)
        Label(csa, font=font_family, bg=green,
              text="Monthly Payment").grid(row=4, column=1, sticky=W)
        Label(csa, font=font_family, bg=green,
              text="Total Payment").grid(row=5, column=1, sticky=W)

        self.annualInterestRateVar = StringVar()
        Entry(csa, textvariable=self.annualInterestRateVar,
              justify=RIGHT).grid(row=1, column=2)

        self.numberofYearsVar = StringVar()
        Entry(csa, textvariable=self.numberofYearsVar,
              justify=RIGHT).grid(row=2, column=2)

        self.loanAmountVar = StringVar()
        Entry(csa, textvariable=self.loanAmountVar,
              justify=RIGHT).grid(row=3, column=2)

        self.monthlyPaymentVar = StringVar()
        lbl_monthly_payment = Label(csa, font=font_family, bg=green,
                                    textvariable=self.monthlyPaymentVar).grid(row=4, column=2, sticky=E)

        self.totalPaymentVar = StringVar()
        lbl_total_payment = Label(csa, font=font_family, bg=green,
                                  textvariable=self.totalPaymentVar).grid(row=5, column=2, sticky=E)

        bt_compute_payment = Button(csa, text="Compute Payment", bg=red, fg=white,
                                    font=font_family, command=self.computePayment).grid(row=6, column=2, sticky=E)
        bt_clear = Button(csa, text="Clear", bg=blue, fg=white, font=font_family,
                          command=self.delete_all).grid(row=6, column=8, padx=20, pady=20, sticky=E)

        csa.mainloop()

    def computePayment(self):
        monthlyPayment = self.getMonthlyPayment(
            float(self.loanAmountVar.get()),
            float(self.annualInterestRateVar.get()) / 1200,
            int(self.numberofYearsVar.get()))

        self.monthlyPaymentVar.set(format(monthlyPayment, "10.2f"))
        totalPayment = float(self.monthlyPaymentVar.get()) * 12 \
            * int(self.numberofYearsVar.get())

        self.totalPaymentVar.set(format(totalPayment, "10.2f"))

    def getMonthlyPayment(self, loanAmount, monthlyInterestRate, numberofYears):
        monthlyPayment = loanAmount * monthlyInterestRate / \
            (1-1/(1 + monthlyInterestRate) ** (numberofYears * 12))
        return monthlyPayment

    def delete_all(self):
        self.monthlyPaymentVar.set("")
        self.loanAmountVar.set("")
        self.annualInterestRateVar.set("")
        self.numberofYearsVar.set("")
        self.totalPaymentVar.set("")


LoanCalculator()
