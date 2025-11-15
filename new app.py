import streamlit as st

st.set_page_config(page_title="India News → IT / Education / Market / Govt", layout="wide")

st.title("📰 Latest India News — IT, Education, Stock Market & Government")

# News items as a list of dicts
news = [
    {
        "title": "US Bill Could Disrupt India’s Outsourcing Model",
        "sector": "IT",
        "summary": "A U.S. bill (HIRE Act) proposes 25% tax on outsourcing payments, threatening Indian IT outsourcing.",
        "link": "https://www.ft.com/content/5e9cdd4b-08dc-412a-bb61-f55dea372641"
    },
    {
        "title": "India Approves $2.7B Plan for Electronics Components",
        "sector": "IT / Manufacturing",
        "summary": "Cabinet green-lit a ₹229 billion PLI scheme to boost domestic electronics manufacturing.",
        "link": "https://www.reuters.com/world/india/indian-cabinet-approves-27-billion-plan-boost-electronics-components-2025-03-28/"
    },
    {
        "title": "Tuhin Kanta Pandey Named New SEBI Chief",
        "sector": "Stock Market / Regulator",
        "summary": "The government appointed Tuhin Kanta Pandey as SEBI chairman for 3 years.",
        "link": "https://www.livemint.com/market/stock-market-news/tuhin-kanta-pandey-appointed-new-sebi-chairperson-for-3-year-term-finance-secy-to-succeed-madhabi-puri-buch-11740679999741.html"
    },
    {
        "title": "Medical Education Expansion Announced in Budget 2025",
        "sector": "Education / Government",
        "summary": "10,000 new medical seats to be added, long-term plan for 75k more over 5 years.",
        "link": "https://economictimes.indiatimes.com/markets/stocks/news/niit-other-education-stocks-rally-up-to-5-as-fm-announces-medical-education-expansion-in-budget-2025/articleshow/117820542.cms"
    },
    {
        "title": "US Visa Curbs May Shift High-Value Work to India GCCs",
        "sector": "Service Sector / Politics",
        "summary": "Potential shift of AI/cybersecurity work to India as U.S. tightens H-1B visa rules.",
        "link": "https://www.reuters.com/world/india/trump-visa-curbs-push-us-firms-consider-shifting-more-work-india-2025-09-30/"
    },
]

# Display in two columns
col1, col2 = st.columns(2)
for i, item in enumerate(news):
    with col1 if i % 2 == 0 else col2:
        st.subheader(f"{item['title']}  [{item['sector']}]")
        st.write(item["summary"])
        st.markdown(f"[Read more]({item['link']})")

