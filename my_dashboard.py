"""
WHY/DESIGN:

This dashboard follows the standard Streamlit layout pattern used in professional
data apps: a wide page configuration, a sidebar for user-driven filters, a metrics
row for quick insights, and tabbed content for organized navigation.

The sidebar provides interactive controls (month, year, region, price ranges, and
budget) that directly influence the main dashboard calculations. This keeps the
interface clean while allowing users to adjust inputs without cluttering the page.

The metrics row uses st.columns() and st.metric() to surface key trip statistics
at a glance. Delta values are included to show change relative to a baseline,
which mirrors real-world KPI dashboards.

Tabs separate the content into logical sections: an Overview tab for visual
summaries, a Details tab for traveler-specific information, and a Raw Data tab
for backend-style records. This structure ensures the dashboard remains readable
and scalable as more features are added.

An expander is included to provide optional explanatory text without interrupting
the main layout. This supports clarity while maintaining a clean visual design.

All data is intentionally hardcoded to focus on layout, component usage, and
dashboard structure rather than external data sources, aligning with the project
requirements.
"""




import streamlit as st
import random
from datetime import datetime
import pandas as pd


# This runs on EVERY re-run — so the timestamp changes each time
st.write(f"Script ran at: **{datetime.now().strftime('%H:%M:%S')}**")

# --- Page Config (MUST be first Streamlit command) ---
st.set_page_config(
    page_title="Travel Dashboard",
    page_icon="🛫📊",
    layout="wide"  # Use full browser width
)

#sidebar controls 
with st.sidebar:
    st.title(" Dashboard Filters")

month = st.sidebar.selectbox(
    "Select Travel Month",
    ["January", "February", "March", "April", "May", "June",
     "July", "August", "September", "October", "November", "December"]
)

year = st.sidebar.selectbox(
    "Select Travel Year",
    list(range(2024, 2031))
)

region = st.sidebar.selectbox(
    "Select Travel Region",
    ["North America", "Europe", "Asia", "South America", "Africa", "Oceania" ]
)

flight_price = st.sidebar.multiselect(
    "Flight Price Range",
    ["$150-$350", "$350-$550", "$550-$750", "$750-$999", "$10,000"],
    default=["$350-$550"]
)

resort_price = st.sidebar.multiselect(
    "Resort Price Range",
    ["$150-$350", "$350-$550", "$550-$750", "$750-$999", "$10,000"],
    default=["$350-$550"]
)

user_budget = st.sidebar.slider(
    "Total Trip Budget",
    min_value=500,
    max_value=10000,
    value=3000,
    step=100
)


show_details = st.checkbox("Show detailed view", value=True)

st.divider()
st.caption(f"Viewing: {month} | {year} | {region}")

#main dashboard page
st.title("Trips Overview Dashboard")
st.write(f"Showing stats for travel during {month} - {year} - {region} ")


price_map = {
    "$150-$350": 250,
    "$350-$550": 450,
    "$550-$750": 650,
    "$750-$999": 875,
    "$10,000": 10000
}



total_flight_cost = sum(price_map[p] for p in flight_price) if flight_price else 0
total_resort_cost = sum(price_map[p] for p in resort_price) if resort_price else 0
total_trip_cost = total_flight_cost + total_resort_cost
previous_total_trip_cost = 1800  # baseline or last month

budget_utilization = (total_trip_cost / user_budget) * 100
budget_utilization_display = f"{budget_utilization:.1f}%"
previous_utilization = 72.5  # example baseline
delta_utilization = budget_utilization - previous_utilization
delta_display = f"{delta_utilization:.1f}%"

cost_data = pd.DataFrame({
    "Category": ["Flight Cost", "Resort Cost", "Total Trip Cost"],
    "Amount": [total_flight_cost, total_resort_cost, total_trip_cost]
})



#---metrics row----
col1, col2, col3, col4= st.columns(4)

with col1:
    st.metric(
    "Total Trip Cost",
    f"${total_trip_cost:,.0f}",
    delta=f"${total_trip_cost - previous_total_trip_cost:,.0f}"
)


with col2:
    st.metric("Total Flight Cost", f"${total_flight_cost:,.0f}")

with col3:
      st.metric("Total Resort Cost", f"${total_resort_cost:,.0f}")

with col4:
    st.metric(
        "Budget Utilization",
        budget_utilization_display,
        delta_display
    )

st.divider()


# --- Tabbed Content ---
tab_overview, tab_details, tab_raw = st.tabs(
    ["📈 Overview", "🔍 Details", "🗑️ Raw Data"]
)

with tab_overview:
    st.subheader("Trip Cost Breakdown")
    st.bar_chart(cost_data.set_index("Category"))

    with st.expander("💡 How to read this chart"):
            st.write("""
    This chart shows a breakdown of your trip costs based on the selections in the sidebar.
    Each bar represents one part of the total cost: flights, resort stay, and the combined
    total trip cost. Taller bars indicate higher expenses. Use this visualization to quickly
    compare which part of your trip contributes most to your overall spending and how your
    choices affect the total cost.
    """)

with tab_details:
    st.subheader("Traveler details")

    if show_details:
        travelers = [
            {"name": "Alex Johnson", "completed": 4, "upcoming": 2},
            {"name": "Maria Lopez", "completed": 7, "upcoming": 1},
            {"name": "Jordan Smith", "completed": 2, "upcoming": 3},
            {"name": "Taylor Brown", "completed": 5, "upcoming": 0},
            {"name": "Casey Nguyen", "completed": 3, "upcoming": 2},
            {"name": "Riley Thompson", "completed": 6, "upcoming": 1},
        ]

        st.write("### Travelers Overview")
        for t in travelers:
            st.write(
                f"- **{t['name']}** — Completed Trips: {t['completed']} | Upcoming Trips: {t['upcoming']}"
            )

    else:
        st.write("Detailed traveler information is hidden. Enable 'Show detailed view' in the sidebar to see it.")

with tab_raw:
     st.subheader("Raw Traveler Data")

     raw_travelers_df = pd.DataFrame([
        ["Alex Johnson", ["North America", "Europe"], 4, 2],
        ["Maria Lopez", ["Asia", "South America", "Europe"], 7, 1],
        ["Jordan Smith", ["Africa"], 2, 3],
        ["Taylor Brown", ["Oceania", "North America"], 5, 0],
        ["Casey Nguyen", ["Europe", "Asia"], 3, 2],
        ["Riley Thompson", ["South America", "Africa", "Asia"], 6, 1],
    ], columns=["Traveler", "Regions Traveled", "Completed Trips", "Upcoming Trips"])

     st.dataframe(raw_travelers_df)