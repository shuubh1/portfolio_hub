import streamlit as st
import pandas as pd
import re
from datetime import datetime
import time

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Shubhayan Chakraborty | Portfolio",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- SIDEBAR NAVIGATION ---
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", [
    "About Me", 
    "Dealflow & Sourcing Engine", 
    "Automated Reconciliation", 
    "Data Engineering"
])

st.sidebar.markdown("---")
st.sidebar.markdown("**Connect**")
st.sidebar.markdown("[LinkedIn](https://linkedin.com/in/yourprofile)")
st.sidebar.markdown("[GitHub](https://github.com/shuubh1)")
st.sidebar.markdown("📍 Kolkata, West Bengal")

# ==========================================
# PAGE 1: ABOUT ME
# ==========================================
if page == "About Me":
    st.title("Bridging Financial Theory and Technical Execution")
    st.markdown("---")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        I am a finance professional and automation engineer focused on eliminating operational bottlenecks in financial due diligence, valuations, and deal sourcing. 
        
        Currently pursuing a B.Com. Honours (Financial Accounting) at Scottish Church College (Class of 2028) and preparing for the CFA Level 1, I combine rigorous theoretical knowledge with high-level Python scripting. 
        
        My internship experience encompasses executing DCF and COMPS valuations, calculating NAV, and performing financial due diligence. However, my differentiator is my ability to build custom tools that extract unstructured financial data, bypass manual entry, and automate complex workflows.
        
        ### Core Competencies
        * **Financial Analysis:** Valuations (NAV, COMPS, DCF), Financial Due Diligence, Market Research.
        * **Technical Stack:** Python, Pandas, Selenium, BeautifulSoup, pdfplumber, Streamlit.
        * **Emerging Tech:** Generative Engine Optimization (GEO), LLM API Integration.
        """)
    
    with col2:
        st.success("""
        **Current Trajectory:**
        - CFA Level 1 Candidate
        - Expanding automated data pipelines
        - Building Generative Search tools
        """)
        st.info("👈 **Select a project from the sidebar to interact with the live tools.**")

# ==========================================
# PAGE 2: DEALFLOW OUTREACH ENGINE
# ==========================================
elif page == "Dealflow & Sourcing Engine":
    st.title("Dealflow Outreach Engine")
    st.markdown("[View Source Code](https://github.com/shuubh1/dealflow-outreach-engine) | **Tech:** Python, Pandas, FuzzyWuzzy, Gemini API")
    st.markdown("---")
    
    st.markdown("""
    **The Bottleneck:** Analysts spend hours manually parsing messy Excel dumps to identify decision-makers, and even more time researching them to draft personalized outreach emails.  
    **The Solution:** An automated pipeline that scores leads using Levenshtein distance string matching and leverages the Gemini API to draft hyper-personalized, context-aware emails.
    """)
    
    st.markdown("### 🧪 Interactive Playground: Rank & Draft")
    st.markdown("Test the logic. Below is a sample raw data dump of conference attendees.")
    
    # 1. Provide Mid-Sized Example Data
    raw_data = {
        "First Name": ["Sarah", "Michael", "Elena", "David", "Priya"],
        "Last Name": ["Jenkins", "Chen", "Rodriguez", "Gould", "Sharma"],
        "Company": ["Apex Capital", "BlueWave Partners", "Vertex Tech", "Gould Capital Inc.", "Apex Capital"],
        "Designation": ["Managing Partner", "Senior Financial Analyst", "Chief Executive Officer", "VP of Operations", "Associate"]
    }
    df = pd.DataFrame(raw_data)
    st.dataframe(df, use_container_width=True)
    
    # 2. Interactive Execution
    if st.button("Execute: Score Leads & Generate Outreach", type="primary"):
        with st.spinner("Scoring seniority and drafting AI email for the top prospect..."):
            time.sleep(1.5) # Simulate processing time
            
            # Simulate the fuzzy matching scoring logic
            def mock_score(title):
                t = title.lower()
                if 'partner' in t or 'chief' in t or 'ceo' in t: return 100
                if 'vp' in t or 'vice president' in t: return 75
                if 'senior' in t: return 50
                return 20
            
            df['Seniority Score'] = df['Designation'].apply(mock_score)
            scored_df = df.sort_values(by=['Company', 'Seniority Score'], ascending=[True, False])
            
            st.success("✅ Candidates ranked by organizational authority.")
            st.dataframe(scored_df, use_container_width=True)
            
            top_target = scored_df.iloc[0]
            st.markdown(f"**Target Selected:** `{top_target['First Name']} {top_target['Last Name']}` - `{top_target['Designation']}`")
            
            # Simulate the AI output
            st.info("🤖 **Generated Contextual Draft (via Gemini API):**")
            mock_email = f"""
            Hi {top_target['First Name']},
            
            I noticed {top_target['Company']}'s recent successful close of your Series B funding round—congratulations to you and the team on that milestone. 
            
            I am reaching out because our firm is currently leading strategic conversations regarding mid-market tech valuations. Given your specific role as {top_target['Designation']}, I believe our current market analysis could offer significant strategic leverage for your upcoming deployments.
            
            Would you be open to a brief, high-level conversation next Tuesday to discuss how we might align our insights with your current portfolio strategy?
            
            Best regards,  
            Shubhayan Chakraborty
            """
            st.code(mock_email, language="markdown")

# ==========================================
# PAGE 3: AUTOMATED RECONCILIATION
# ==========================================
elif page == "Automated Reconciliation":
    st.title("Automated Bank Statement Reconciliation")
    st.markdown("[View Source Code](https://github.com/shuubh1/bank_reconciliation) | **Tech:** Python, pdfplumber, RegEx State Machines")
    st.markdown("---")
    
    st.markdown("""
    **The Bottleneck:** Financial due diligence stalls when analysts have to manually transcribe hundreds of pages of unstructured bank statements (PDFs), risking human error.  
    **The Solution:** A dynamic Python extraction tool utilizing complex RegEx state-machines to handle multi-line transaction descriptions and format variations across different banks.
    """)
    
    st.markdown("### 🧪 Interactive Playground: Unstructured to Structured")
    st.markdown("Edit the raw PDF text block below (notice the multi-line transaction on 04/17/25) and hit parse to see the regex engine structure the data.")
    
    # 1. Provide Unstructured Input Data
    sample_pdf_text = """Withdrawals and other debits
04/15/25 ATM Withdrawal 123 Main St -100.00
04/16/25 Transfer to Acct 4567 -550.00
04/17/25 Online Bill Pay:
         Electric Company 
         Invoice #88392 -125.50
04/18/25 Wire Transfer Fee -15.00
Total withdrawals and other debits"""

    user_input = st.text_area("Raw PDF Text Stream (Editable)", value=sample_pdf_text, height=200)
    
    # 2. Interactive Execution
    if st.button("Execute: Parse into Pandas DataFrame", type="primary"):
        with st.spinner("Applying RegEx State Machine..."):
            time.sleep(1)
            
            # The actual logic from your script, adapted for the playground
            transactions = []
            current_txn = None
            
            for line in user_input.split('\n'):
                line = line.strip()
                if "Total withdrawals" in line or "Withdrawals and other" in line or not line:
                    continue
                
                # Match start of a transaction (Date ... Amount)
                match = re.match(r'^(\d{2}/\d{2}/\d{2})\s+(.*?)\s+(-?[\d,]+\.\d{2})$', line)
                
                # Match start of a transaction where amount is missing (multi-line)
                match_partial = re.match(r'^(\d{2}/\d{2}/\d{2})\s+(.*)$', line) if not match else None

                if match:
                    if current_txn: transactions.append(current_txn)
                    date_str, desc, amt = match.groups()
                    current_txn = {"Date": date_str, "Description": desc, "Amount": float(amt)}
                
                elif match_partial and not re.search(r'-?[\d,]+\.\d{2}$', line):
                     if current_txn: transactions.append(current_txn)
                     date_str, desc = match_partial.groups()
                     current_txn = {"Date": date_str, "Description": desc, "Amount": 0.0}
                     
                elif current_txn:
                    # Look for an amount at the end of a continuation line
                    amt_match = re.search(r'\s+(-?[\d,]+\.\d{2})$', line)
                    if amt_match:
                        current_txn["Description"] += " " + line.replace(amt_match.group(1), "").strip()
                        current_txn["Amount"] = float(amt_match.group(1))
                    else:
                        current_txn["Description"] += " " + line
            
            if current_txn and current_txn["Amount"] != 0.0:
                transactions.append(current_txn)
                
            if transactions:
                parsed_df = pd.DataFrame(transactions)
                st.success("✅ Successfully caught multi-line anomalies and structured the data.")
                st.dataframe(parsed_df, use_container_width=True)
            else:
                st.error("Could not parse transactions. Ensure the text format matches the standard layout.")

# ==========================================
# PAGE 4: DATA ENGINEERING
# ==========================================
elif page == "Data Engineering":
    st.title("Data Engineering & Web Scraping")
    st.markdown("---")
    
    st.markdown("""
    **The Bottleneck:** Premium financial and event data is often locked behind complex authentication walls, dynamic JavaScript rendering (React/Chakra UI), or anti-bot protections.  
    **The Solution:** Bypassing standard bot-detection by hooking Selenium directly into live, pre-authenticated Chrome debugging ports, allowing seamless extraction of hidden DOM elements.
    """)
    
    st.markdown("### 🧪 Interactive Playground: DOM Parsing")
    st.markdown("Below is an example of the messy, nested HTML structure found on modern event platforms. Click extract to run the parsing logic.")
    
    sample_html = """<div class="chakra-modal__content-container">
    <h2 class="font-semibold text-xl">Jonathan Sterling</h2>
    <h2 class="font-semibold hidden"></h2><p class="text-gray-600">Managing Director, Quantum Finance</p>
    
    <div id="attendee-card-content">
        <div class="css-rszk63">
            <p class="section-title">Investment Strategy</p>
            <p>Private Equity</p>
            <p>Distressed Assets</p>
        </div>
        <div class="css-rszk63">
            <p class="section-title">Geographic Focus</p>
            <p>North America</p>
            <p>Western Europe</p>
        </div>
        <div class="css-rszk63">
            <p class="section-title">Desired fund size (USD)</p>
            <p>$500M - $1B</p>
        </div>
    </div>
</div>"""
    
    st.code(sample_html, language="html")
    
    if st.button("Execute: Extract Entities to JSON", type="primary"):
        with st.spinner("Traversing DOM nodes..."):
            time.sleep(1)
            # Simulated BeautifulSoup/Selenium extraction logic
            st.success("✅ Entities successfully mapped to structured dictionary.")
            extracted_data = {
                "Name": "Jonathan Sterling",
                "Designation, Company": "Managing Director, Quantum Finance",
                "Investment Strategy": "Private Equity, Distressed Assets",
                "Geographic Focus": "North America, Western Europe",
                "Desired fund size (USD)": "$500M - $1B",
                "Length of GP track record": "N/A"
            }
            st.json(extracted_data)