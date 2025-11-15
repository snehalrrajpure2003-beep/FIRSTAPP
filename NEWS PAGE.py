# app.py
import streamlit as st
from datetime import datetime
st.set_page_config(page_title="NEWS PAGE", layout="wide", page_icon="📰")

# ---- CSS & fonts ----
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&family=Roboto+Slab:wght@400;700&display=swap" rel="stylesheet">
<style>
:root{
  --bg1: linear-gradient(120deg,#0f172a,#0b1220 40%, #07203a);
  --card-bg: rgba(255,255,255,0.03);
  --glass: rgba(255,255,255,0.03);
}
html,body {background: var(--bg1); font-family: 'Inter', sans-serif; color:#e6eef8;}
.stApp {background: transparent;}
.header {
  display:flex; gap:12px; align-items:center;
}
.title {font-family:'Roboto Slab', serif; font-size:28px; font-weight:700;}
.subtitle {color:#c7d2fe; margin-bottom:8px;}
.card {
  background: linear-gradient(180deg, rgba(255,255,255,0.03), rgba(255,255,255,0.02));
  border-radius:14px;
  padding:18px;
  margin-bottom:14px;
  box-shadow: 0 10px 30px rgba(2,6,23,0.6);
  transform-style: preserve-3d;
  transition: transform .35s cubic-bezier(.2,.9,.3,1), box-shadow .35s;
  border: 1px solid rgba(255,255,255,0.04);
}
.card:hover { transform: translateY(-8px) rotateX(2deg); box-shadow: 0 20px 50px rgba(2,6,23,0.8);}
.badge {display:inline-block; padding:6px 10px; border-radius:999px; background: rgba(34,197,94,0.15); color:#bbf7d0; font-weight:600; margin-left:6px; font-size:12px;}
.pointer {font-size:18px; margin-right:8px;}
.link {color:#93c5fd; text-decoration:none; font-weight:600;}
.sector-btn {
  background: linear-gradient(90deg,#0ea5e9,#6366f1);
  color: white; padding:10px 14px; border-radius:10px; border:none; font-weight:700;
}
.footer {color:#9fb3d6; font-size:13px;}
.kpi {font-size:13px; color:#9fb3d6;}
.row {display:flex; gap:16px;}
.big-card {padding:20px; border-radius:16px; background:linear-gradient(180deg, rgba(255,255,255,0.02), rgba(255,255,255,0.01));}
@keyframes floaty {
  0% { transform: translateY(0px); }
  50% { transform: translateY(-6px);}
  100% { transform: translateY(0px);}
}
.lottie { animation: floaty 6s ease-in-out infinite; }
</style>
""", unsafe_allow_html=True)

# ---- App header ----
col1, col2 = st.columns([3,1])
with col1:
    st.markdown("<div class='header'><div class='title'>NEWS PAGE</div></div>", unsafe_allow_html=True)
    st.markdown("<div class='subtitle'>Choose a sector to see latest verified news (India).</div>", unsafe_allow_html=True)
with col2:
    st.markdown("<div style='text-align:right'><small class='kpi'>Updated: {}</small></div>".format(datetime.now().strftime("%d %b %Y, %H:%M:%S")), unsafe_allow_html=True)

# ---- Sector selector ----
sectors = ["IT","Education","Stock Market","Politics","Government"]
selected = st.radio("Select sector", sectors, index=0, horizontal=True)

# ---- News data (hardcoded snapshot of verified sources) ----
# Replace links and texts below with updated fetches when you refresh.
news_data = {
    "IT": [
        {"title":"Infosys announces record ₹18,000 crore share buyback (Nov 2025)",
         "summary":"Infosys set a record buyback — market and investors reacting to the record date and implications.",
         "link":"https://timesofindia.indiatimes.com/business/india-business/infosys-share-buyback-company-set-for-its-biggest-rs-18000-crore-offer-ever-what-to-know-before-nov-14-record-date/articleshow/125279213.cms",
         "source":"Times of India", "verified":True},
        {"title":"India approves $626M projects to boost electronics components",
         "summary":"Government approved projects to strengthen electronics components manufacturing capacity.",
         "link":"https://www.reuters.com/world/india/india-approves-626-million-projects-boost-electronics-components-manufacturing-2025-10-27/",
         "source":"Reuters", "verified":True},
        {"title":"PLI scheme to boost electronics components (₹22,919 Cr)",
         "summary":"PLI incentives aim to deepen local manufacturing of PCBs, camera modules and battery cells.",
         "link":"https://www.reuters.com/world/india/indian-cabinet-approves-27-billion-plan-boost-electronics-components-2025-03-28/",
         "source":"Reuters", "verified":True},
        {"title":"Semiconductor OSAT investment updates",
         "summary":"Reports detail new investments in OSAT and local chip-related manufacturing.",
         "link":"https://www.india-briefing.com/news/setting-up-a-semiconductor-fabrication-plant-in-india-what-foreign-investors-should-know-22009.html",
         "source":"India Briefing", "verified":True},
    ],
    "Education":[
        {"title":"Govt to add 10,000 medical seats next year (75,000 over 5 years)",
         "summary":"Union Budget/Cabinet plans major expansion of MBBS & allied medical seats.",
         "link":"https://www.pib.gov.in/PressReleasePage.aspx?PRID=2172069",
         "source":"PIB / Govt", "verified":True},
        {"title":"NMC approves thousands of new MBBS seats for 2025–26",
         "summary":"National Medical Commission granted approvals for new seats and colleges.",
         "link":"https://www.business-standard.com/india-news/nmc-approves-6850-new-mbbs-seats-2025-26-medical-education-125091601546_1.html",
         "source":"Business Standard", "verified":True},
        {"title":"Education stocks rally after medical-education expansion",
         "summary":"NIIT and other education stocks moved higher after budget announcements.",
         "link":"https://m.economictimes.com/markets/stocks/news/niit-other-education-stocks-rally-up-to-5-as-fm-announces-medical-education-expansion-in-budget-2025/articleshow/117820542.cms",
         "source":"ET Markets", "verified":True},
    ],
    "Stock Market":[
        {"title":"MSCI to add Paytm and 3 other Indian stocks (Nov 2025)",
         "summary":"MSCI announced inclusions which may attract foreign inflows into Indian markets.",
         "link":"https://www.reuters.com/world/india/msci-add-paytm-3-other-indian-stocks-flagship-global-index-2025-11-06/",
         "source":"Reuters", "verified":True},
        {"title":"Sensex / Nifty market live highlights",
         "summary":"Daily market movements and live blog summaries.",
         "link":"https://m.economictimes.com/markets/stocks/live-blog/bse-sensex-today-live-nifty-stock-market-updates-14-november-2025/liveblog/125313978.cms",
         "source":"Economic Times", "verified":True},
        {"title":"Top analyst picks & market calls (Nov 2025)",
         "summary":"Market columns and buy/sell calls from recognised analysts.",
         "link":"https://www.livemint.com/market/stock-market-news/buy-or-sell-sumeet-bagadia-recommends-three-stocks-to-buy-on-monday-17-november-2025-11763172833089.html",
         "source":"Livemint", "verified":True},
    ],
    "Politics":[
        {"title":"Bihar results: NDA leads / seat counts (Nov 14–15, 2025)",
         "summary":"Live coverage: NDA strong lead in Bihar assembly results; national implications.",
         "link":"https://www.ndtv.com/india-news/bihar-assembly-elections-2025-live-updates-nitish-kumar-tejashwi-yadav-mahagathbandhan-bjp-nda-rjd-congress-9632014",
         "source":"NDTV", "verified":True},
        {"title":"Bihar results analysis & headlines",
         "summary":"Hindustan Times live updates and reaction pieces.",
         "link":"https://www.hindustantimes.com/india-news/bihar-election-results-2025-counting-today-who-will-win-bihar-chunav-bjp-nda-mahagathbandhan-election-commission-jdu-eci-101763072897828.html",
         "source":"Hindustan Times", "verified":True},
        {"title":"Regional & international analysis on Bihar & youth politics",
         "summary":"Al Jazeera provides context on Gen-Z and the election landscape.",
         "link":"https://www.aljazeera.com/news/2025/11/13/as-gen-z-rage-across-south-asia-indias-youngest-state-pins-hopes-on-polls",
         "source":"Al Jazeera", "verified":True},
    ],
    "Government":[
        {"title":"Cabinet approves Export Promotion Mission (~₹25,060 Cr)",
         "summary":"Major package to boost exports and MSME support announced by Cabinet (Nov 12, 2025).",
         "link":"https://www.pmindia.gov.in/en/news_updates/cabinet-approves-export-promotion-mission-to-strengthen-indias-export-ecosystem-with-an-outlay-of-rs-25060-crore/",
         "source":"PM India / PIB", "verified":True},
        {"title":"Cabinet okays Credit Guarantee Scheme for Exporters",
         "summary":"New CGSE scheme details and implementation steps (official release).",
         "link":"https://www.newsonair.gov.in/union-cabinet-approves-new-export-credit-guarantee-scheme-launches-%E2%82%B925000-crore-export-promotion-mission/",
         "source":"NewsOnAir", "verified":True},
        {"title":"SEBI: Tuhin Kanta Pandey takes charge as Chairman (Mar 1, 2025)",
         "summary":"Official SEBI release announcing the new Chairperson.",
         "link":"https://www.sebi.gov.in/media-and-notifications/press-releases/mar-2025/shri-tuhin-kanta-pandey-takes-charge-as-chairman-sebi_92392.html",
         "source":"SEBI.gov.in", "verified":True},
    ]
}

# ---- Display cards for selected sector ----
st.markdown("<div class='big-card'><div style='display:flex; justify-content:space-between; align-items:center;'><div><h3 style='margin:0'>{}</h3><div class='kpi'>Latest verified headlines</div></div><div class='lottie'>✨</div></div></div><br>".format(selected), unsafe_allow_html=True)

sector_list = news_data.get(selected, [])
for i, item in enumerate(sector_list):
    st.markdown(f"""
    <div class='card'>
      <div style='display:flex; justify-content:space-between; align-items:flex-start;'>
        <div>
          <div style='font-size:16px; font-weight:700'>{item['title']} <span class='badge'>VERIFIED</span></div>
          <div style='margin-top:6px; color:#bcd4ff'>{item['summary']}</div>
          <div style='margin-top:10px;'><a class='link' href="{item['link']}" target="_blank">Read full article ↗</a> <span style='color:#9fb3d6; margin-left:12px'>Source: {item['source']}</span></div>
        </div>
        <div style='width:120px; text-align:right;'><button class='sector-btn' onclick='window.open("{item['link']}", "_blank")'>Open</button></div>
      </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<div class='footer'>• Sources: Reuters, PIB, NDTV, Times of India, Economic Times, Livemint, SEBI — all free/public reporting. Click 'Read full article' to verify source content.</div>", unsafe_allow_html=True)

# ---- small footer ----
st.markdown("<br><small class='kpi'>Built for Snehal — press a sector. To refresh news, re-run after replacing news_data with latest links.</small>", unsafe_allow_html=True)
