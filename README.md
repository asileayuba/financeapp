# 🧾 Spendify

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
spendify/
├── main.py               # Main Streamlit application
├── categories.json      # Stores category-keyword mappings
├── requirements.txt     # List of required packages
└── README.md            # Project documentation
```


---
## 🙌 Contributing

Contributions are welcome!
Feel free to fork the project and submit a pull request. For major changes, please open an issue first to discuss your ideas.

