import streamlit as st
from datetime import datetime, date

st.title("⏳ Advanced Age Calculator App")

dob = st.date_input("Select your Date of Birth")

if st.button("Calculate Exact Age"):
    now = datetime.now()
    dob_datetime = datetime.combine(dob, datetime.min.time())

    # Difference
    diff = now - dob_datetime

    # Years, months, days calculation
    years = now.year - dob.year
    months = now.month - dob.month
    days = now.day - dob.day

    if days < 0:
        months -= 1
        days += 30
    if months < 0:
        years -= 1
        months += 12

    # Convert total seconds
    total_seconds = diff.total_seconds()
    total_minutes = total_seconds / 60
    total_hours = total_minutes / 60

    st.success(f"🎉 **Your Age:** {years} Years, {months} Months, {days} Days")

    st.info(f"""
### ⏱ Age Till This Second:
- **Total Days:** {diff.days:,}
- **Total Hours:** {int(total_hours):,}
- **Total Minutes:** {int(total_minutes):,}
- **Total Seconds:** {int(total_seconds):,}
    """)
