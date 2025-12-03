import math

# Constants
BRUTUS_INITIAL_DEPOSIT = 1
PORTIA_INITIAL_DEPOSIT = 100_000
BRUTUS_INTEREST_RATE = 5   # percent
PORTIA_INTEREST_RATE = 4   # percent

def find_crossover_year(b_init, p_init, b_rate, p_rate):
    """
    Returns the year when Brutus's account overtakes Portia's account,
    or None if it never happens.
    """
    b_growth = 1 + b_rate / 100
    p_growth = 1 + p_rate / 100

    # If Brutus's rate is not higher, he'll never catch up
    if b_growth <= p_growth:
        return None

    # Solve: b_init * (b_growth)^y >= p_init * (p_growth)^y
    ratio = b_growth / p_growth
    target = p_init / b_init

    y = math.log(target) / math.log(ratio)
    return math.ceil(y)  # first integer year at which Brutus catches up

# --- Run it ---
year = find_crossover_year(
    BRUTUS_INITIAL_DEPOSIT,
    PORTIA_INITIAL_DEPOSIT,
    BRUTUS_INTEREST_RATE,
    PORTIA_INTEREST_RATE
)

if year:
    print(f"Brutus overtakes Portia in year {year}.")
else:
    print("Brutus will never catch up.")
