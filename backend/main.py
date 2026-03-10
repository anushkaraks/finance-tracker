from parser import parse_bank_statement

def summarize(df):
    """
    Prints a basic summary of the transactions.
    """
    total_credits = df[df['amount'] > 0]['amount'].sum()
    total_debits = df[df['amount'] < 0]['amount'].sum()
    net = total_credits + total_debits

    print("=" * 40)
    print("       FINANCE TRACKER SUMMARY")
    print("=" * 40)
    print(f"Total Transactions : {len(df)}")
    print(f"Total Money In     : ₹{total_credits:,.2f}")
    print(f"Total Money Out    : ₹{total_debits:,.2f}")
    print(f"Net Balance Change : ₹{net:,.2f}")
    print("=" * 40)

if __name__ == "__main__":
    filepath = "../sample_data/sample_statement.csv"
    
    print("Loading bank statement...")
    df = parse_bank_statement(filepath)
    
    summarize(df)