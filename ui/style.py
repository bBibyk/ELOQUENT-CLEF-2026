import streamlit as st

def apply_clean_theme():
    """Injecte du CSS personnalisé pour affiner le layout. Les couleurs sont gérées dans .streamlit/config.toml."""
    st.markdown("""
        <style>
        /* Import Inter Font */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap');

        /* Force Inter font on all text */
        html, body, [class*="css"] {
            font-family: 'Inter', sans-serif !important;
        }

        /* Streamlit Header (must be visible for sidebar toggle) */
        header {
            background-color: transparent !important;
        }
        
        /* The button that opens the sidebar when collapsed */
        [data-testid="collapsedControl"] {
            display: flex;
            align-items: center;
            background-color: #FFFFFF !important;
            border: 1px solid #E5E7EB !important;
            border-radius: 6px !important;
            padding: 4px 10px !important;
            box-shadow: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
            margin-top: 10px;
            margin-left: 10px;
            z-index: 1000;
        }
        
        /* Add text 'Config' next to the expand icon */
        [data-testid="collapsedControl"]::after {
            content: "Configuration";
            font-family: 'Inter', sans-serif;
            font-size: 0.85rem;
            font-weight: 500;
            color: #374151;
            margin-left: 8px;
        }

        /* Hide Streamlit Footer and extra top padding */
        footer {visibility: hidden;}
        .stApp > header {
            height: 0px !important; /* Prevents header from taking up blank space when expanded */
        }
        .stButton > button {
            border-radius: 6px !important;
            font-weight: 500 !important;
            transition: all 0.2s ease;
            box-shadow: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
        }
        .stButton > button:hover {
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
            transform: translateY(-1px);
            background-color: #374151 !important; /* Lighter dark for hover */
            color: #FFFFFF !important;
            border-color: #374151 !important;
        }

        /* Clean Expanders */
        [data-testid="stExpander"] {
            border: 1px solid #E5E7EB !important;
            border-radius: 8px !important;
            box-shadow: 0 1px 2px 0 rgba(0, 0, 0, 0.05) !important;
            margin-bottom: 0.75rem;
            background-color: transparent !important;
        }
        [data-testid="stExpander"] details summary {
            font-weight: 500 !important;
            border-bottom: none !important;
            padding: 10px 15px !important;
        }

        /* Sidebar minimalist */
        [data-testid="stSidebar"] {
            background-color: #FFFFFF !important;
            border-right: 1px solid #E5E7EB !important;
        }
        [data-testid="stSidebarUserContent"] {
            padding-top: 1.5rem !important;
        }
        /* Clean Metrics Cards */
        [data-testid="stMetric"] {
            background-color: #FFFFFF;
            border: 1px solid #E5E7EB;
            border-radius: 8px;
            padding: 1.5rem;
            box-shadow: 0 1px 3px rgba(0,0,0,0.05);
        }
        [data-testid="stMetricLabel"] {
            color: #6B7280 !important;
            font-weight: 500 !important;
            font-size: 0.875rem !important;
        }
        [data-testid="stMetricValue"] {
            font-size: 1.875rem !important;
            font-weight: 600 !important;
            margin-top: 0.25rem;
        }

        /* Tabs clean lines */
        .stTabs [data-baseweb="tab-list"] {
            gap: 2rem;
            border-bottom: 1px solid #E5E7EB;
            background-color: transparent !important;
            padding-bottom: 0;
            margin-bottom: 1.5rem;
        }
        .stTabs [data-baseweb="tab"] {
            padding-bottom: 0.75rem;
            padding-top: 0.75rem;
            border: none !important;
            background-color: transparent !important;
            font-weight: 500;
        }
        .stTabs [aria-selected="true"] {
            border-bottom: 2px solid #111827 !important;
            color: #111827 !important;
        }

        /* Alert and info boxes */
        .stAlert {
            border-radius: 6px !important;
            border: 1px solid #E5E7EB !important;
            box-shadow: 0 1px 2px 0 rgba(0, 0, 0, 0.02);
        }
        
        /* Select and inputs */
        .stSelectbox div[data-baseweb="select"] {
            border-radius: 6px !important;
            border: 1px solid #D1D5DB !important;
            background-color: #FFFFFF !important;
        }
        .stMultiSelect div[data-baseweb="select"] {
            border-radius: 6px !important;
            border: 1px solid #D1D5DB !important;
            background-color: #FFFFFF !important;
            color: #111827 !important;
        }
        .stSlider [data-baseweb="slider"] {
            margin-top: 10px !important;
        }
        
        hr {
            margin: 2rem 0 !important;
            border-color: #E5E7EB !important;
        }
        </style>
    """, unsafe_allow_html=True)
