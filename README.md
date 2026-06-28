# 🧾 FinSight

A **Streamlit-based web application** for analyzing personal or business financial transactions. This app allows users to upload CSV bank transaction data, automatically categorize expenses using customizable keywords, and visualize their finances with interactive charts.

---

## 🚀 Features

- 📁 **CSV Upload:** Upload and parse your bank transactions in CSV format.
- 🏷️ **Automatic Categorization:** Transactions are automatically categorized based on keywords.
- 🛠️ **Editable Categories:** Add, edit, and assign categories directly from the dashboard.
- 📊 **Expense Visualization:** View categorized expenses in tabular and pie chart formats.
- 💰 **Debits & Credits Tabs:** Separate views for expenses (debits) and payments/income (credits).
- 🌍 **Global & Multi-Currency Support:** Dynamically filter and view transactions by currency (e.g. NGN, USD).
- 🔐 **Persistent State:** Category mappings are saved in a local JSON file.

---

## ⚙️ How It Works

1. **Upload your CSV**: You start by uploading your bank statement in a CSV format. The app automatically detects the `Currency` column.
2. **Filter by Currency**: If your statement has multiple currencies (like NGN and USD), a sidebar will appear to let you filter the transactions.
3. **Auto-Categorization**: The app scans the `Details` column of each transaction against a local `categories.json` file. For instance, if it spots "UBER" or "BOLT", it automatically assigns it to "Transportation".
4. **Review & Edit**: You can review these auto-assigned categories in an interactive table. If a transaction falls into "Uncategorized", you can manually assign a category right in the table and click **Apply Changes**. The app remembers your choice for next time!
5. **Visualize**: Once everything is categorized, it generates a beautiful summary table and pie chart so you can see exactly where your money went.

---

## 📦 Installation

1. **Clone the Repository**

```bash
git clone https://github.com/asileayuba/financeapp.git
cd financeapp
```

2. **Install Required Packages:** Make sure you have Python 3.7+ installed and then install dependencies:

```bash
pip install -r requirements.txt
```

2. **Run the App**

```bash
streamlit run main.py
```

## 📁 Project Structure
```bash
finsight/
├── main.py               # Main Streamlit application
├── categories.json      # Stores category-keyword mappings
├── requirements.txt     # List of required packages
└── README.md            # Project documentation
```


---
## 🙌 Contributing

Contributions are welcome!
Feel free to fork the project and submit a pull request. For major changes, please open an issue first to discuss your ideas.

