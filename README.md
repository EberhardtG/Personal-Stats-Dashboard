
# 🛫 Travel Dashboard  
A Streamlit‑powered personal stats dashboard for exploring travel costs, budget utilization, and traveler activity. Built as part of a layout‑focused assignment to practice professional dashboard structure using Streamlit components such as sidebars, metrics, tabs, expanders, and charts.

---

## 📌 Overview  
This dashboard provides an interactive way to explore trip costs based on user‑selected filters such as travel month, year, region, flight price range, resort price range, and total budget. It includes a metrics row for quick insights, a cost breakdown chart, traveler details, and raw backend‑style data.

The project emphasizes **layout and structure**, not external data sources — all data is intentionally hardcoded.

---

## 🎯 Features  
### **Sidebar Controls**
- Travel month selector  
- Travel year selector  
- Region selector  
- Flight price range multiselect  
- Resort price range multiselect  
- Budget slider  
- “Show detailed view” checkbox to toggle traveler details  

### **Metrics Row**
Displays key trip statistics:
- Total Trip Cost  
- Total Flight Cost  
- Total Resort Cost  
- Budget Utilization (with delta comparison)  

### **Tabbed Layout**
- **📈 Overview**  
  - Bar chart of trip cost breakdown  
  - Expander explaining how to interpret the chart  

- **🔍 Details**  
  - Traveler list with completed and upcoming trips  
  - Conditionally displayed based on sidebar checkbox  

- **🗑️ Raw Data**  
  - Table of travelers, regions visited, and trip counts  
  - Represents backend‑style raw records  

### **Professional Layout Elements**
- Wide page configuration  
- Clean section dividers  
- Hardcoded data for simplicity  
- Organized and readable structure  

---

## 🧩 Tech Stack
- **Python 3.x**  
- **Streamlit**  
- **Pandas**  

---

## 🚀 Getting Started

### **1. Clone the repository**
```bash
git clone https://github.com/your-username/travel-dashboard.git
cd travel-dashboard
```

### **2. Install dependencies**
```bash
pip install -r requirements.txt
```

### **3. Run the app**
```bash
streamlit run my_dashboard.py
```

---

## 📁 Project Structure
```
my_dashboard.py        # Main Streamlit application
requirements.txt       # Python dependencies
README.md              # Project documentation
```

---

## 🧠 Design Notes
This project follows a standard Streamlit dashboard pattern used in professional data applications:

- **Sidebar for user input**  
- **Metrics row for KPIs**  
- **Tabs for organized content**  
- **Expander for optional explanations**  
- **Charts + tables for visual and raw data**  

The goal is to demonstrate clean layout, component usage, and dashboard structure — not API integration or dynamic data fetching.

---

## 📄 License  
This project is open‑source and available under the MIT License.

---

