from abc import ABC, abstractmethod


class customer:
    def __init__(self, customer_id, customer_name, age, email, phone_number, income, credit_score):
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.age = age
        self.email = email
        self.phone_number = phone_number
        self.income = income
        self.credit_score = credit_score

    def check_eligibility(self):
        if self.age < 21 or self.credit_score < 650 or self.income < 25000:
            return False
        return True

    def display_customer(self):
        print("\nCustomer Details")
        print("--------------------")
        print("Customer ID  :", self.customer_id)
        print("Customer Name:", self.customer_name)
        print("Email        :", self.email)
        print("Phone Number :", self.phone_number)
        print("Age          :", self.age)
        print("Income       :", self.income)
        print("Credit Score :", self.credit_score)


class Loan(ABC):

    def __init__(self, loan_id, customer, loan_amount, interest_rate, tenure):
        self.loan_id = loan_id
        self.customer = customer
        self.__loan_amount = loan_amount
        self.interest_rate = interest_rate
        self.tenure = tenure
        self.__balance = loan_amount
        self.__total_paid = 0
        self.repayment_history = []
        self.status = "Applied"

    @abstractmethod
    def calculate_emi(self):
        pass

    def check_loan_eligibility(self):

        if not self.customer.check_eligibility():
            self.status = "Rejected"
            return False

        return True

    def sanction_loan(self):

        if self.status == "Rejected":
            print("Loan application was Rejected")
            return

        if not self.check_loan_eligibility():
            print("Customer is not eligible for the loan")
            return

        self.status = "Sanctioned"
        print("\nLoan Sanctioned Successfully")

    def repay(self, amount):

        if self.status != "Sanctioned":
            print("Repayment is not allowed")
            print("Loan Status:", self.status)
            return

        if amount <= 0:
            print("Invalid repayment amount")
            return

        if amount > self.__balance:
            print("Repayment amount is greater than outstanding balance")
            return

        self.__balance -= amount
        self.__total_paid += amount

        self.repayment_history.append(amount)

        print("\nRepayment Successful")
        print("Amount Paid         :", amount)
        print("Outstanding Balance :", self.__balance)

        if self.__balance == 0:
            self.status = "Closed"
            print("Loan Closed Successfully")

    def get_balance(self):
        return self.__balance

    def get_loan_amount(self):
        return self.__loan_amount

    def get_total_paid(self):
        return self.__total_paid

    def display_statement(self):

        print("\n")
        print("=" * 40)
        print("LOAN STATEMENT")
        print("=" * 40)

        print("Loan ID             :", self.loan_id)
        print("Customer Name       :", self.customer.customer_name)
        print("Loan Amount         :", self.__loan_amount)
        print("Interest Rate       :", self.interest_rate)
        print("Tenure              :", self.tenure)
        print("Total Paid          :", self.__total_paid)
        print("Outstanding Balance :", self.__balance)
        print("Loan Status         :", self.status)

        print("\nRepayment History")

        if not self.repayment_history:
            print("No repayment made")

        else:
            for i in range(len(self.repayment_history)):
                print(f"Payment {i + 1} : {self.repayment_history[i]}")

        print("=" * 40)

    def __str__(self):

        return (
            f"Loan ID: {self.loan_id}, "
            f"Customer: {self.customer.customer_name}, "
            f"Loan Amount: {self.__loan_amount}, "
            f"Outstanding: {self.__balance}, "
            f"Status: {self.status}"
        )


class HomeLoan(Loan):

    def calculate_emi(self):

        principal = self.get_loan_amount()
        monthly_rate = self.interest_rate / (12 * 100)
        months = self.tenure * 12

        emi = (
            principal
            * monthly_rate
            * (1 + monthly_rate) ** months
            / ((1 + monthly_rate) ** months - 1)
        )

        return round(emi, 2)


class PersonalLoan(Loan):

    def calculate_emi(self):

        principal = self.get_loan_amount()
        monthly_rate = self.interest_rate / (12 * 100)
        months = self.tenure * 12

        emi = (
            principal
            * monthly_rate
            * (1 + monthly_rate) ** months
            / ((1 + monthly_rate) ** months - 1)
        )

        return round(emi, 2)


class CarLoan(Loan):

    def calculate_emi(self):

        principal = self.get_loan_amount()
        monthly_rate = self.interest_rate / (12 * 100)
        months = self.tenure * 12

        emi = (
            principal
            * monthly_rate
            * (1 + monthly_rate) ** months
            / ((1 + monthly_rate) ** months - 1)
        )

        return round(emi, 2)


# ---------------- CUSTOMER 1 ----------------

reena = customer(
    1,
    'reena',
    22,
    'reena@gmail.com',
    87654376543,
    25000,
    750
)

reena.display_customer()
print("Loan Eligibility:", reena.check_eligibility())


# ---------------- CUSTOMER 2 ----------------

kowsar = customer(
    2,
    'kowsar',
    24,
    'kowsar@gmail.com',
    7654376543,
    25000,
    550
)

kowsar.display_customer()
print("Loan Eligibility:", kowsar.check_eligibility())


# ---------------- HOME LOAN ----------------

home_loan = HomeLoan(
    "HL1001",
    reena,
    500000,
    8.5,
    10
)


print("\nLoan Application")
print("----------------")

print(home_loan)


# ---------------- ELIGIBILITY ----------------

print("\nChecking Loan Eligibility")

if home_loan.check_loan_eligibility():

    print("Customer is eligible")

    home_loan.sanction_loan()

    print("\nEMI")
    print("Monthly EMI:", home_loan.calculate_emi())

    print("\nRepayments")

    home_loan.repay(100000)
    home_loan.repay(150000)
    home_loan.repay(250000)

else:

    print("Customer is not eligible")


# ---------------- FINAL DETAILS ----------------

print("\nFinal Loan Details")

print(home_loan)

home_loan.display_statement()