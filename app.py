
import streamlit as st
import pandas as pd

st.title("CommunityConnect")
st.write("Find community resources based on your needs.")

resources = pd.DataFrame({
    "Organization": [
        "Community Food Program",
        "Employment Support Center",
        "Housing Assistance Program"
    ],
    "Category": [
        "Food",
        "Employment",
        "Housing"
    ],
    "Description": [
        "Helps families access food assistance.",
        "Provides job search and career support.",
        "Provides information about housing assistance."
    ]
})

keywords = {
    "Food": ["food", "hungry", "groceries", "eat", "meals"],
    "Housing": ["housing", "rent", "homeless", "shelter", "apartment"],
    "Employment": ["job", "work", "unemployed", "career", "employment"]
}

question = st.text_input("What do you need help with?")

if question:
    matched_categories = []

    for category, words in keywords.items():
        if any(word in question.lower().split() for word in words):
            matched_categories.append(category)

    matches = resources[
        resources["Category"].isin(matched_categories)
    ]

    if not matches.empty:
        st.success("Here are some resources that may help:")
        st.dataframe(matches, hide_index=True)
    else:
        st.warning("No matching resources found.")

st.caption("Demo only: resource organizations are fictional.")
