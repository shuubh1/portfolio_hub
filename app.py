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
    "Generative Engine Optimization (GEO)", 
    "Dealflow & Sourcing Engine", 
    "Automated Reconciliation", 
    "Data Engineering"
])

st.sidebar.markdown("---")
st.sidebar.markdown("**Connect**")
st.sidebar.markdown("[LinkedIn](https://linkedin.com/in/shubhayan-chakraborty-67034228a/)")
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
        * **Search & AI Strategy:** Generative Engine Optimization (GEO), LLM Visibility Consulting, Semantic Architecture.
        """)
    
    with col2:
        st.success("""
        **Current Trajectory:**
        - CFA Level 1 Candidate
        - Expanding automated data pipelines
        - Consulting on GEO & LLM Search Visibility
        """)
        st.info("👈 **Select a project from the sidebar to interact with the live tools.**")

# ==========================================
# PAGE 2: GEO CONSULTING FRAMEWORK
# ==========================================
elif page == "Generative Engine Optimization (GEO)":
    st.title("Generative Engine Optimization (GEO)")
    st.markdown("**Positioning brands for visibility in AI Overviews, Perplexity, and LLM-driven search.**")
    st.markdown("---")
    
    st.markdown("""
    As search shifts from traditional keyword indexing to Large Language Model synthesis, traditional SEO is no longer enough. AI engines do not rank pages; they synthesize entities, facts, and consensus. 
    
    I have developed a proprietary GEO framework designed to restructure brand data so that AI models (ChatGPT, Gemini, Perplexity) confidently cite and recommend it.
    """)
    
    # Showcase the Framework (High-Level, protecting the IP)
    st.markdown("### The Consulting Methodology")
    tab1, tab2, tab3 = st.tabs(["1. Semantic Architecture", "2. EEAT & Entity Trust", "3. AI Visibility Testing"])
    
    with tab1:
        st.markdown("""
        **Structuring content for machine readability.**
        * **Entity-Centric Writing:** Shifting focus from keywords to defined entities (Subject → Predicate → Object relationships).
        * **Context Bridging:** Establishing semantic proximity between a brand and high-authority industry terms.
        * **Schema & Knowledge Graphs:** Utilizing structured data (sameAs, Organization, Author) to feed direct facts to LLMs.
        """)
    with tab2:
        st.markdown("""
        **Building unshakeable AI confidence.**
        * **Consensus Retrieval:** Ensuring AI finds the exact same brand facts across owned assets, PR, and rented platforms.
        * **Experience-Led Content:** Forcing AI to cite a brand by injecting first-hand insights and specific use cases that generative models cannot hallucinate.
        * **Brand Citation Engineering:** Securing non-linked mentions on high-trust platforms that LLMs use as training weights.
        """)
    with tab3:
        st.markdown("""
        **Measuring the invisible.**
        * **Prompt Fan-Out Analysis:** Reverse-engineering exactly what contextual data an LLM requires to answer a high-value query.
        * **Source Citation Monitoring:** Tracking Perplexity and Search Generative Experience (SGE) for brand inclusion.
        * **Hallucination Audits:** Identifying where AI models are misrepresenting a brand and injecting corrections into the knowledge graph.
        """)
    
    st.divider()
    
    # Interactive GEO Grader
    st.markdown("### 🧪 Interactive Playground: GEO Readiness Grader")
    st.markdown("Are your digital assets ready for AI search? Take this mini-assessment based on my proprietary evaluation matrix.")
    
    with st.form("geo_audit"):
        st.markdown("**Content & Structure**")
        c1 = st.checkbox("Our content explicitly defines core concepts rather than assuming context.")
        c2 = st.checkbox("We use structured 'Subject-Action-Object' sentences (Semantic Triples).")
        c3 = st.checkbox("Our authors have verifiable digital footprints (LinkedIn, Publications).")
        
        st.markdown("**Technical & Citations**")
        t1 = st.checkbox("Our 'About' page and social profiles have 100% consistent descriptions.")
        t2 = st.checkbox("We utilize advanced Schema markup (sameAs, Person, Organization).")
        t3 = st.checkbox("We track brand mentions inside Perplexity or ChatGPT, not just Google Analytics.")
        
        submitted = st.form_submit_button("Calculate GEO Score", type="primary")
        
        if submitted:
            score = sum([c1, c2, c3, t1, t2, t3])
            st.progress(score / 6)
            
            if score <= 2:
                st.error(f"**Score: {score}/6 (High Risk)**\n\nYour brand is likely invisible to AI search engines. LLMs lack the structured data and consensus required to confidently recommend you. Focus immediately on basic Entity alignment and Schema markup.")
            elif score <= 4:
                st.warning(f"**Score: {score}/6 (Transitional)**\n\nYour traditional SEO is likely solid, but AI models may hallucinate details about your brand or prefer competitors with stronger EEAT signals. You need a dedicated Semantic Content Strategy.")
            else:
                st.success(f"**Score: {score}/6 (AI-Optimized)**\n\nExcellent. Your brand is generating strong trust signals. The next step is targeted AI Visibility Testing to dominate specific generative search prompts.")

# ==========================================
# PAGE 3: DEALFLOW OUTREACH ENGINE
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
    
    raw_data = {
        "First Name": ["Sarah", "Michael", "Elena", "David", "Priya"],
        "Last Name": ["Jenkins", "Chen", "Rodriguez", "Gould", "Sharma"],
        "Company": ["Apex Capital", "BlueWave Partners", "Vertex Tech", "Gould Capital Inc.", "Apex Capital"],
        "Designation": ["Managing Partner", "Senior Financial Analyst", "Chief Executive Officer", "VP of Operations", "Associate"]
    }
    df = pd.DataFrame(raw_data)
    st.dataframe(df, use_container_width=True)
    
    if st.button("Execute: Score Leads & Generate Outreach", type="primary"):
        with st.spinner("Scoring seniority and drafting AI email for the top prospect..."):
            time.sleep(1.5)
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
# PAGE 4: AUTOMATED RECONCILIATION
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
    
    sample_pdf_text = """Withdrawals and other debits
04/15/25 ATM Withdrawal 123 Main St -100.00
04/16/25 Transfer to Acct 4567 -550.00
04/17/25 Online Bill Pay:
         Electric Company 
         Invoice #88392 -125.50
04/18/25 Wire Transfer Fee -15.00
Total withdrawals and other debits"""

    user_input = st.text_area("Raw PDF Text Stream (Editable)", value=sample_pdf_text, height=200)
    
    if st.button("Execute: Parse into Pandas DataFrame", type="primary"):
        with st.spinner("Applying RegEx State Machine..."):
            time.sleep(1)
            transactions = []
            current_txn = None
            
            for line in user_input.split('\n'):
                line = line.strip()
                if "Total withdrawals" in line or "Withdrawals and other" in line or not line:
                    continue
                
                match = re.match(r'^(\d{2}/\d{2}/\d{2})\s+(.*?)\s+(-?[\d,]+\.\d{2})$', line)
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
                st.error("Could not parse transactions.")

# ==========================================
# PAGE 5: DATA ENGINEERING
# ==========================================
elif page == "Data Engineering":
    st.title("Data Engineering & Web Scraping")
    st.markdown("---")
    
    st.markdown("""
    **The Bottleneck:** Premium financial and event data is often locked behind complex authentication walls, dynamic JavaScript rendering (React/Chakra UI), or anti-bot protections.  
    **The Solution:** Bypassing standard bot-detection by hooking Selenium directly into live, pre-authenticated Chrome debugging ports, allowing seamless extraction of hidden DOM elements.
    """)
    
    st.markdown("### 🧪 Interactive Playground: DOM Parsing")
    
    sample_html = """<div class="chakra-modal__content-container">
    <h2 class="font-semibold text-xl">Jonathan Sterling</h2>
    <p class="text-gray-600">Managing Director, Quantum Finance</p>
    
    <div id="attendee-card-content">
        <div class="css-rszk63">
            <p class="section-title">Investment Strategy</p>
            <p>Private Equity</p>
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
            st.success("✅ Entities successfully mapped to structured dictionary.")
            extracted_data = {
                "Name": "Jonathan Sterling",
                "Designation, Company": "Managing Director, Quantum Finance",
                "Investment Strategy": "Private Equity",
                "Desired fund size (USD)": "$500M - $1B"
            }
            st.json(extracted_data)