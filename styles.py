import streamlit as st

def apply_custom_styles():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&display=swap');

        .main {
            padding: 2rem;
            background-color: #121212;
            font-family: 'Roboto', sans-serif;
        }

        .stButton>button {
            background-color: #9C27B0;
            color: white;
            border: none;
            padding: 0.75rem 1.5rem;
            border-radius: 8px;
            font-weight: 500;
            letter-spacing: 0.5px;
            transition: all 0.3s ease;
            box-shadow: 0 2px 4px rgba(156, 39, 176, 0.2);
        }

        .stButton>button:hover {
            background-color: #7B1FA2;
            transform: translateY(-2px);
            box-shadow: 0 4px 8px rgba(156, 39, 176, 0.3);
        }

        .stButton>button:active {
            transform: translateY(0);
        }

        .stat-card {
            background-color: #1E1E1E;
            color: white;
            padding: 1.5rem;
            border-radius: 12px;
            margin: 0.75rem 0;
            border: 1px solid rgba(156, 39, 176, 0.1);
            transition: all 0.3s ease;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            position: relative;
            overflow: hidden;
        }

        .stat-card:hover {
            transform: translateY(-4px);
            border-color: rgba(156, 39, 176, 0.3);
            box-shadow: 0 8px 12px rgba(0, 0, 0, 0.2);
        }

        .stat-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 4px;
            background: linear-gradient(90deg, #9C27B0, #E91E63);
            opacity: 0;
            transition: opacity 0.3s ease;
        }

        .stat-card:hover::before {
            opacity: 1;
        }

        .badge-card {
            text-align: center;
            background: linear-gradient(145deg, #1E1E1E, #2D2D2D);
            border-radius: 16px;
            padding: 2rem;
            position: relative;
            overflow: hidden;
        }

        .badge-icon {
            font-size: 3rem;
            margin: 1rem 0;
            display: inline-block;
            animation: float 3s ease-in-out infinite;
        }

        @keyframes float {
            0% { transform: translateY(0px); }
            50% { transform: translateY(-10px); }
            100% { transform: translateY(0px); }
        }

        .progress-bar {
            height: 8px;
            border-radius: 4px;
            background: linear-gradient(90deg, #9C27B0, #E91E63);
            transition: width 0.5s ease;
        }

        .achievement-progress {
            background-color: #2D2D2D;
            border-radius: 8px;
            padding: 1rem;
            margin: 0.5rem 0;
            transition: all 0.3s ease;
        }

        .achievement-progress:hover {
            background-color: #363636;
        }

        /* Improved Typography */
        h1, h2, h3, h4, h5, h6 {
            font-family: 'Roboto', sans-serif;
            font-weight: 700;
            letter-spacing: -0.5px;
            margin-bottom: 1rem;
        }

        /* Tab styling */
        .stTabs [data-baseweb="tab-list"] {
            gap: 8px;
            background-color: #1E1E1E;
            padding: 0.5rem;
            border-radius: 12px;
        }

        .stTabs [data-baseweb="tab"] {
            padding: 0.75rem 1.5rem;
            border-radius: 8px;
            transition: all 0.2s ease;
        }

        .stTabs [data-baseweb="tab"]:hover {
            background-color: rgba(156, 39, 176, 0.1);
        }

        .stTabs [aria-selected="true"] {
            background-color: #9C27B0 !important;
        }

        /* Loading animation */
        @keyframes pulse {
            0% { opacity: 1; }
            50% { opacity: 0.5; }
            100% { opacity: 1; }
        }

        .loading {
            animation: pulse 1.5s ease-in-out infinite;
        }

        /* Custom scrollbar */
        ::-webkit-scrollbar {
            width: 8px;
            height: 8px;
        }

        ::-webkit-scrollbar-track {
            background: #1E1E1E;
        }

        ::-webkit-scrollbar-thumb {
            background: #9C27B0;
            border-radius: 4px;
        }

        ::-webkit-scrollbar-thumb:hover {
            background: #7B1FA2;
        }
        </style>
    """, unsafe_allow_html=True)

def create_stat_card(title, value):
    st.markdown(f"""
        <div class="stat-card">
            <h3 style="color: #9C27B0; margin-bottom: 0.5rem;">{title}</h3>
            <p style="font-size: 1.75rem; font-weight: 700; margin: 0.5rem 0;">{value}</p>
        </div>
    """, unsafe_allow_html=True)

def create_badge_card(title, icon, description):
    st.markdown(f"""
        <div class="badge-card">
            <h3 style="color: #9C27B0; margin-bottom: 0.5rem;">{title}</h3>
            <div class="badge-icon">{icon}</div>
            <p style="font-size: 0.9rem; opacity: 0.8;"><em>{description}</em></p>
        </div>
    """, unsafe_allow_html=True)

def create_progress_bar(label, current, maximum, icon="🎯"):
    percentage = min(current / maximum * 100, 100)
    st.markdown(f"""
        <div class="achievement-progress">
            <div style="display: flex; align-items: center; margin-bottom: 0.5rem;">
                <span style="font-size: 1.25rem; margin-right: 0.5rem;">{icon}</span>
                <span style="font-weight: 500;">{label}</span>
            </div>
            <div style="background-color: #363636; border-radius: 4px; height: 8px; overflow: hidden;">
                <div class="progress-bar" style="width: {percentage}%;"></div>
            </div>
            <div style="text-align: right; font-size: 0.9rem; opacity: 0.8; margin-top: 0.25rem;">
                {current}/{maximum}
            </div>
        </div>
    """, unsafe_allow_html=True)