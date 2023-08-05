
from numpy_financial import pmt


def compute_monthly_payments_and_interest_and_principal(loan_amount, interest_rate, loan_term_months):
    """
    Compute the monthly payment, interest payments, and principal payments for each month of a loan based on the
    given loan amount, interest rate, and loan term in months.

    Args:
    loan_amount (float): The loan amount in dollars.
    interest_rate (float): The interest rate as a percentage per year.
    loan_term_months (int): The loan term in months.

    Returns:
    tuple: A tuple containing three lists:
           - monthly_payments: The monthly payments in dollars.
           - monthly_interest_payments: The interest payments for each month in dollars.
           - monthly_principal_payments: The principal payments for each month in dollars.
    """
    # Convert the interest rate from percentage to decimal and monthly interest rate.
    r = interest_rate / 100 / 12

    # Compute the monthly payment using the pmt function from numpy_financial.
    p = pmt(rate=r, nper=loan_term_months, pv=-loan_amount, when='begin')

    # Initialize the remaining loan balance to the original loan amount.
    remaining_loan_balance = loan_amount

    # Initialize empty lists for the monthly payments, interest payments, and principal payments.
    monthly_payments = []
    monthly_interest_payments = []
    monthly_principal_payments = []

    # Compute the monthly payments, interest payments, and principal payments for each month of the loan.
    for i in range(loan_term_months):
        # Compute the interest payment for this month.
        interest_payment = remaining_loan_balance * r
        # Compute the principal payment for this month.
        principal_payment = p - interest_payment

        # Update the remaining loan balance.
        remaining_loan_balance -= principal_payment

        # Append the monthly payment, interest payment, and principal payment to their respective lists.
        monthly_payments.append(p)
        monthly_interest_payments.append(interest_payment)
        monthly_principal_payments.append(principal_payment)

    return monthly_payments, monthly_interest_payments, monthly_principal_payments


if __name__ == '__main__':
    loan_amount = 100000
    interest_rate = 18
    loan_term_months = 12

    monthly_payments, monthly_interest_payments, monthly_principal_payments = compute_monthly_payments_and_interest_and_principal(
        loan_amount, interest_rate, loan_term_months)

    # Print the monthly payments, interest payments, and principal payments for each month.
    for i in range(loan_term_months):
        print(
            f"Month {i + 1}: Payment = {monthly_payments[i]:.2f}, Interest = {monthly_interest_payments[i]:.2f}, Principal = {monthly_principal_payments[i]:.2f}")
