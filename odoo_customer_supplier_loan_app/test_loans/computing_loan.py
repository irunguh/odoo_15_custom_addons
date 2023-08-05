
# Caluclate loan payment per period
def pmt(rate, nper, pv, fv=0, type=0, freq=12):
    """
    Calculate the fixed periodic payment required to pay off a loan or investment based on a constant interest rate and a fixed loan term.

    Args:
        rate (float): The interest rate for the loan period.
        nper (int): The total number of payment periods for the loan.
        pv (float): The present value or principal amount of the loan.
        fv (float, optional): The future value or a cash balance you want to attain after the last payment is made. Defaults to 0.
        type (int, optional): The number 0 or 1 to indicate when payments are due, with 0 meaning at the end of the period and 1 meaning at the beginning of the period. Defaults to 0.
        freq (int, optional): The number of times per year the interest rate is compounded. Defaults to 12.

    Returns:
        float: The fixed periodic payment required to pay off the loan or investment.
    """
    if freq == 1:
        rate /= freq
        nper *= freq
    else:
        rate /= freq
        nper *= freq
        fv *= (1 + rate) ** (1 / freq)
    if rate == 0:
        return -(fv + pv) / nper
    else:
        pmt_value = (rate * (fv + pv * (1 + rate) ** nper)) / ((1 + rate) ** nper - 1)
        if type == 1:
            pmt_value /= (1 + rate)
        return -pmt_value

if __name__ == '__main__':
    rate = 0.18
    nper = 12
    pv = 300000
    fv = 0
    type = 0
    freq = 6  # annual compounding

    monthly_payment = pmt(rate, nper, pv, fv, type, freq)
    print("Debug::: Monlthy payment for a loan")
    print(monthly_payment)
