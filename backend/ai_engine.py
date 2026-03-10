import os
import json
from groq import Groq
from dotenv import load_dotenv

# Load your .env file so we can access the API key
load_dotenv()

# Initialize the Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def categorize_transactions(df):
    """
    Takes a DataFrame of transactions and returns
    AI-generated categories for each one.
    """
    # Build a simple text list of transactions to send to the AI
    transaction_list = ""
    for _, row in df.iterrows():
        transaction_list += f"- {row['description']}: {row['amount']}\n"

    system_prompt = """
You are a personal finance assistant. 
Your job is to categorize bank transactions.

Use ONLY these categories:
- Food & Dining
- Transport
- Entertainment
- Shopping
- Bills & Utilities
- Income
- Health & Fitness
- Transfers & Withdrawals
- Other

Respond ONLY with a valid JSON object.
No explanation, no extra text, just JSON.

Format:
{
  "categories": [
    {"description": "SWIGGY ORDER", "category": "Food & Dining"},
    {"description": "SALARY CREDIT", "category": "Income"}
  ]
}
"""

    user_prompt = f"""
Categorize these transactions:

{transaction_list}

Remember: respond ONLY with the JSON object.
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0
    )

    # Extract the text response
    raw_response = response.choices[0].message.content

    # Parse the JSON response
    result = json.loads(raw_response)

    # Add categories back to your DataFrame
    category_map = {
        item['description']: item['category']
        for item in result['categories']
    }

    df['category'] = df['description'].map(category_map).fillna('Other')

    return df


if __name__ == "__main__":
    import sys
    sys.path.append('.')
    from parser import parse_bank_statement

    df = parse_bank_statement("../sample_data/sample_statement.csv")

    print("Sending transactions to AI...")
    df = categorize_transactions(df)

    print("\nCategorization complete!")
    print(df[['date', 'description', 'amount', 'amount', 'category']])
