# --- Import required libraries ---
import streamlit as st 
import pandas as pd 
import plotly.express as px 
import json
import os
import time

# --- Configure the Streamlit page ---
st.set_page_config(page_title="Finance App", page_icon="🧾", layout="wide")

# --- JSON file to store category-keyword mappings ---
category_file = "categories.json"

# --- Load or initialize categories in session state ---
if "categories" not in st.session_state:
    if os.path.exists(category_file):
        with open(category_file, "r") as f:
            st.session_state.categories = json.load(f)
    else:
        # Start with an "Uncategorized" default
        st.session_state.categories = {
            "Uncategorized": [],
        }

# --- Save categories to the JSON file ---
def save_categories():
    with open(category_file, "w") as f:
        json.dump(st.session_state.categories, f, indent=2)

# --- Assign a category to each transaction based on keywords ---
def categorize_transactions(df):
    df["Category"] = "Uncategorized"  # Default category

    for category, keywords in st.session_state.categories.items():
        # Skip empty or default categories
        if category == "Uncategorized" or not keywords:
            continue

        # Normalize keywords for comparison
        lowered_keywords = [keyword.lower().strip() for keyword in keywords]

        for idx, row in df.iterrows():
            details = row["Details"].lower().strip()
            # Assign category if any keyword matches the transaction detail
            if any(keyword in details for keyword in lowered_keywords):
                df.at[idx, "Category"] = category

    return df

# --- Load uploaded transaction file and format it ---
def load_transactions(file):
    try:
        df = pd.read_csv(file)
        df.columns = [col.strip() for col in df.columns]  # Clean column names
        df["Amount"] = df["Amount"].astype(str).str.replace(",", "").astype(float)  # Remove commas from Amount
        df["Date"] = pd.to_datetime(df["Date"], format="%d %b %Y")  # Parse date

        return categorize_transactions(df)
    except Exception as e:
        st.error(f"Error processing file: {str(e)}")
        return None

# --- Add a new keyword to a category if it doesn't already exist ---
def add_keyword_to_category(category, keyword):
    keyword = keyword.strip()
    if keyword and keyword not in st.session_state.categories[category]:
        st.session_state.categories[category].append(keyword)
        save_categories()
        return True
    return False

# --- Main app interface ---
def main():
    st.title("Finance Dashboard 🧾")

    # --- Upload CSV transaction file ---
    uploaded_file = st.file_uploader("Upload your transaction CSV file", type=["csv"])

    if uploaded_file is not None:
        df = load_transactions(uploaded_file)

        if df is not None:
            # Split data into debits (expenses) and credits (payments)
            debits_df = df[df["Debit/Credit"].str.lower() == "debit"].copy()
            credits_df = df[df["Debit/Credit"].str.lower() == "credit"].copy()

            # Store debits for editing later
            st.session_state.debits_df = debits_df.copy()

            # --- Tabs for Expenses and Credits ---
            tab1, tab2 = st.tabs(["Expenses (Debits)", "Payments (Credits)"])

            with tab1:
                # --- Add a new category section ---
                new_category = st.text_input("New Category Name")
                add_button = st.button("Add Category")

                if add_button and new_category:
                    if new_category not in st.session_state.categories:
                        st.session_state.categories[new_category] = []
                        save_categories()
                        st.success(f"Category '{new_category}' added!")
                        st.rerun()  # Refresh app to include new category in select box

                # --- Expense Data Editor ---
                st.subheader("Your Expenses")
                edited_df = st.data_editor(
                    st.session_state.debits_df[["Date", "Details", "Amount", "Category"]],
                    column_config={
                        "Date": st.column_config.DateColumn("Date", format="DD/MM/YY"),
                        "Amount": st.column_config.NumberColumn("Amount", format="%.2f NGN"),
                        "Category": st.column_config.SelectboxColumn(
                            "Category",
                            options=list(st.session_state.categories.keys())
                        )
                    },
                    hide_index=True,
                    use_container_width=True,
                    key="category_editor"
                )

                # --- Apply changes from editor ---
                save_button = st.button("Apply Changes", type="primary")
                if save_button:
                    for idx, row in edited_df.iterrows():
                        new_category = row["Category"]
                        # Skip if no change
                        if new_category == st.session_state.debits_df.at[idx, "Category"]:
                            continue
                        details = row["Details"]
                        st.session_state.debits_df.at[idx, "Category"] = new_category
                        added = add_keyword_to_category(new_category, details)
                        if added:
                            st.toast(f"Added '{details}' to '{new_category}'")

                    # Save changes and show success temporarily
                    save_categories()
                    success_msg = st.empty()
                    success_msg.success("Changes applied successfully!")
                    time.sleep(3)
                    success_msg.empty()

                # --- Show summary of categorized expenses ---
                st.subheader("Expense Summary")
                category_totals = st.session_state.debits_df.groupby("Category")["Amount"].sum().reset_index()
                category_totals = category_totals.sort_values("Amount", ascending=False)

                # Display as a dataframe
                st.dataframe(
                    category_totals,
                    column_config={
                        "Amount": st.column_config.NumberColumn("Amount", format="%.2f NGN")
                    },
                    use_container_width=True,
                    hide_index=True
                )

                # Display as a pie chart
                fig = px.pie(
                    category_totals,
                    values="Amount",
                    names="Category",
                    title="Expenses by Category"
                )
                st.plotly_chart(fig, use_container_width=True)

            with tab2:
                # --- Display credit transactions ---
                st.subheader("Your Credits / Payments")
                st.dataframe(
                    credits_df,
                    use_container_width=True,
                    hide_index=True
                )

# --- Run the app ---
main()
