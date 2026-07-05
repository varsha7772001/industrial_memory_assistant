import streamlit as st

def load_css():
    st.markdown("""
<style>

/* Hide Streamlit */

#MainMenu{
    visibility:hidden;
}

footer{
    visibility:hidden;
}

/* Background */

.stApp{

background:linear-gradient(
135deg,
#0b1220 0%,
#121c2b 35%,
#1c2638 100%
);

color:white;

}

/* Hero */

.hero{

padding:25px;

border-radius:20px;

background:rgba(255,255,255,.06);

backdrop-filter:blur(15px);

border:1px solid rgba(255,255,255,.08);

margin-bottom:20px;

}

/* Cards */

.metric-card{

background:rgba(255,255,255,.05);

padding:20px;

border-radius:16px;

border:1px solid rgba(255,255,255,.08);

transition:.3s;

box-shadow:0 8px 30px rgba(0,0,0,.25);

}

.metric-card:hover{

transform:translateY(-5px);

border:1px solid #3B82F6;

}

/* Report */

.report{

background:#182131;

padding:20px;

border-radius:16px;

border-left:5px solid #22c55e;

}

/* Memory */

.memory{

background:#1d2939;

padding:20px;

border-radius:16px;

border-left:5px solid #3B82F6;

}

/* Buttons */

.stButton>button{

width:100%;

height:55px;

border-radius:12px;

background:#2563eb;

color:white;

font-weight:bold;

font-size:17px;

border:none;

transition:.3s;

}

.stButton>button:hover{

background:#1d4ed8;

transform:scale(1.02);

}

/* Text area */

textarea{

border-radius:12px !important;

background:#111827 !important;

color:white !important;

}

/* Sidebar */

section[data-testid="stSidebar"]{

background:#111827;

}

/* Status */

.status{

padding:10px;

background:#0f172a;

border-radius:12px;

margin-bottom:10px;

}

/* Scroll */

::-webkit-scrollbar{

width:8px;

}

::-webkit-scrollbar-thumb{

background:#2563eb;

border-radius:10px;

}

</style>
""",unsafe_allow_html=True)
    
    