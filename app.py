import streamlit as st
from PIL import Image

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
    "Financial Operations (Reconciliation)", 
    "Data Engineering (Scrapers)",
    "AIEO & Generative Prototypes"
])

st.sidebar.markdown("---")
st.sidebar.markdown("**Connect**")
st.sidebar.markdown("[LinkedIn](https://www.linkedin.com/in/shubhayan-chakraborty-67034228a/)")
st.sidebar.markdown("[GitHub](https://github.com/shuubh1)")
st.sidebar.markdown("📍 Kolkata, West Bengal")

# --- ABOUT ME ---
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
        * **Emerging Tech:** AI Engine Optimization (AIEO), Generative Engine Optimization (GEO), LLM Integration via API.
        """)
    
    with col2:
        # Placeholder for a professional headshot
        # st.info("📸 **Add your headshot here**\n\nSave an image as `profile.jpg` in your folder and uncomment the code below.")
        image = Image.open('profile.jpg')
        st.image(image, use_column_width=True)
        
        st.success("""
        **Current Trajectory:**
        - CFA Level 1 Candidate
        - Expanding automated data pipelines
        - Building Generative Search tools
        """)

# --- DEALFLOW OUTREACH ENGINE ---
elif page == "Dealflow & Sourcing Engine":
    st.title("Dealflow Outreach Engine")
    st.markdown("[View Repository](https://github.com/shuubh1/dealflow-outreach-engine) | **Tech:** Python, Pandas, FuzzyWuzzy, Gemini API")
    st.markdown("---")
    
    st.markdown("""
    ### The Bottleneck
    In private equity and advisory, analysts spend countless hours manually parsing massive Excel dumps to identify key decision-makers, and even more time researching them to draft personalized, non-generic outreach emails.

    ### The Solution
    An automated, two-part pipeline that scores leads and generates hyper-personalized outreach.
    
    1. **The Screener:** Programmatically ranks candidates based on custom seniority hierarchies using Levenshtein distance string matching (`FuzzyWuzzy`), generating an audit-trail Excel sheet with dynamic formulas linking back to source data.
    2. **The Drafter:** A backend engine that leverages the Gemini API and live web search to autonomously research selected candidates and draft contextual, peer-to-peer outreach emails referencing recent company milestones.
    """)
    
    # st.info("📸 **Visual Placeholder:** Take a screenshot of the clean Excel output with the generated draft emails and uncomment the code below.")
    st.image("dealflow_screenshot.png", caption="Automated output showing scored candidates and AI-generated drafts.")

# --- FINANCIAL OPERATIONS (RECONCILIATION) ---
elif page == "Financial Operations (Reconciliation)":
    st.title("Automated Bank Statement Reconciliation")
    st.markdown("[View Repository](https://github.com/shuubh1/bank_reconciliation) | **Tech:** Python, pdfplumber, Camelot, Regex")
    st.markdown("---")
    
    st.markdown("""
    ### The Bottleneck
    Financial due diligence often stalls when processing raw, unstructured bank statements (PDFs). Manual transcription risks human error and wastes hours of high-value analyst time.

    ### The Solution
    A dynamic extraction tool capable of parsing multiple complex bank statement formats (e.g., Bank of America, TD Business). 
    
    * Utilizes `pdfplumber` and complex RegEx state-machines for fluid, multi-line text extraction.
    * Leverages `camelot` for strict table-stream extraction on highly formatted pages.
    * Outputs sanitized, standardized pandas DataFrames ready for immediate ingestion into valuation models and cash flow analysis.
    """)
    
    # st.info("📸 **Visual Placeholder:** Show a side-by-side screenshot of a messy BoA PDF and the clean Pandas/Excel DataFrame output.")
    st.image("reconciliation_screenshot.png", caption="Unstructured PDF to structured DataFrame.")

# --- DATA ENGINEERING (SCRAPERS) ---
elif page == "Data Engineering (Scrapers)":
    st.title("Data Engineering & Web Scraping")
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Reonomy Commercial Real Estate Scraper")
        st.markdown("[View Repository](https://github.com/shuubh1/reonomy_scraper)")
        st.markdown("""
        Built a Selenium-based automation tool to handle dynamic authentication flows and extract proprietary commercial real estate data. 
        Demonstrates the ability to handle complex DOM structures, explicit waits, and secure environment variable credential management.
        """)
        # st.info("📸 **Visual Placeholder:** Screenshot of the Reonomy terminal output.")
        st.image("reonomy_ss.png")

    with col2:
        st.markdown("### InformaConnect Attendee Extractor")
        st.markdown("[View Repository](https://github.com/shuubh1/informaconnect_scraper)")
        st.markdown("""
        Engineered a scraper that bypasses standard authentication blocks by hooking into live, pre-authenticated browser debugging sessions. 
        Scrolls, parses hidden React/Chakra UI modals, and aggregates targeted investor profiles into structured Excel sheets.
        """)
        # st.info("📸 **Visual Placeholder:** Screenshot of the scraped attendee Excel file.")
        st.image("informa_ss.png")

# --- AIEO & GENERATIVE PROTOTYPES ---
elif page == "AIEO & Generative Prototypes":
    st.title("Generative Engine Optimization (GEO) Prototypes")
    st.markdown("---")
    
    st.markdown("""
    ### "Rick and MortAI" - Experimenting with AI Visibility
    [View Repo 1](https://github.com/shuubh1/RickAndMortai) | [View Repo 2](https://github.com/shuubh1/Rick-and-MortAI-Science-Exhibition)

    As search behavior shifts from traditional indexing to Large Language Model synthesis, positioning data to be effectively retrieved by AI (AIEO/GEO) is becoming a critical skill. 

    These projects serve as prototypes and sandboxes for testing how LLMs ingest, process, and retrieve highly specific thematic data. By experimenting with retrieval augmented generation (RAG) concepts and prompt structures, I am actively building intuition for the future of search and automated data retrieval architectures.
    """)
    
    # st.info("📸 **Visual Placeholder:** Add a screenshot of the prototype interface or a terminal output of the AI responding.")
    st.image("ai_prototype_ss.png")