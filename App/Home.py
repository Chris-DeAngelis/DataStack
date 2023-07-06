import streamlit as st
#from snowflake.sqlalchemy import URL
#from sqlalchemy import create_engine
import requests
import pandas as pd

if "shared" not in st.session_state:
   st.session_state["shared"] = True

st.set_page_config(
    page_title="Evaluate My Data Stack With Spaulding Ridge",
    page_icon=":bar_chart:", #"👋",
    #initial_sidebar_state="expanded",
    menu_items={
        #'Get Help': 'http://google.com'#'chris.deangelis@elkay.com'#,
        #'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# Built by Chris DeAngelis, CFA | cdeangelis@spauldingridge.com"
    }
)

# Load config
#config, instructions, readme = load_config(
#    "config_streamlit.toml", "config_instructions.toml", "config_readme.toml"
#)
#display_links(readme["links"]["repo"], readme["links"]["article"])

st.write("# Evaluate Your Current Data Stack and Compare Alternatives")#:bar_chart::rocket:")
st.markdown(
        """
        ### Select products you use today across the major 
        1. Data Ingestion
        2. Data Storage & Transformation
        3. Data Catalog & Governance
        4. Data Analytics & Publication        
        """
)
#st.title('Data Ingestion')
a = with st.expander("Data Ingestion", expanded=True):
    st.multiselect(
             "Choose Business Verticals", ['A','B','C'], ['B']
    )

b = with st.expander("Data Storage & Transformation", expanded=True):
    st.multiselect(
             "Choose Business Verticals", ['A','B','C'], ['B']
    )

c = with st.expander("Data Catalog & bGovernance", expanded=True):
    st.multiselect(
             "Choose Business Verticals", ['A','B','C'], ['C']
    )

d = with st.expander("Data Analytics & Publication ", expanded=True):
    st.multiselect(
             "Choose Business Verticals", ['A','B','C'], ['B']
    )


#zews_query = st.secrets.credentials.zews_query
#@st.cache_resource(ttl=43200) # Update every 10 minutes = 600
# def connect_snowflake():  
#     '''
#     Function to connect to Snowflake. Returns a connected database object that can be queried.
#     '''
#     engine = create_engine(URL(
#             user=st.secrets.credentials.user,
#             password=st.secrets.credentials.password,
#             account=st.secrets.credentials.account,
#             warehouse=st.secrets.credentials.warehouse,
#             database=st.secrets.credentials.database,
#             schema=st.secrets.credentials.schema
#     ))
#     #cs = ctx.cursor()
#     connection = engine.connect()
#     return connection, engine

# @st.cache_data(ttl=43200) # Update every 10 minutes = 600
# def run_query(query=zews_query):
#     '''
#     Function to run query against Snowflake. This function connects to database, runs query, closes connection, and returns query results in a dataframe.
#     '''  
#     try:
#     	connection, engine = connect_snowflake()
#         #connection.execute(zews_query)
#     	df = pd.read_sql_query(zews_query, engine)
#     finally:
#     	connection.close()
#     	engine.dispose()
#     return df

# # Execute queries for ZEWS Invoices and Macroeconomic Data
# # Caching ZEWS data from Snowflake
# df = run_query(query=zews_query)
# st.write(df.head())
# if 'zews_sales' not in st.session_state:
#     st.session_state['zews_sales'] = df

# Caching Macroeconomic data from Snowflake
#@st.cache_data
#run_query(query=macroeconomics_query)

# KPI boxes
# to = todf[(todf['Hospital Attended']==hosp) & (todf['Metric']== 'Total Outstanding')]   
# ch = todf[(todf['Hospital Attended']==hosp) & (todf['Metric']== 'Current Handover Average Mins')]   
# hl = todf[(todf['Hospital Attended']==hosp) & (todf['Metric']== 'Hours Lost to Handovers Over 15 Mins')

#m1.write('')
#m2.metric(label ='Total Outstanding Handovers',value = int(to['Value']), delta = str(int(to['Previous']))+' Compared to 1 hour ago', delta_color = 'inverse')
#m3.metric(label ='Current Handover Average',value = str(int(ch['Value']))+" Mins", delta = str(int(ch['Previous']))+' Compared to 1 hour ago', delta_color = 'inverse')
#m4.metric(label = 'Time Lost today (Above 15 mins)',value = str(int(hl['Value']))+" Hours", delta = str(int(hl['Previous']))+' Compared to yesterday')
#m1.write('')

# Using object notation
#Add_selectbox = st.sidebar.selectbox(
#    "Contact Me",
#    ("Email", "LinkedIn", "Github Profile")
#)

# Load logo
def add_logo():
    st.markdown(
        """
        <style>
            [data-testid="stSidebarNav"] {
                background-image: url(https://avatars.githubusercontent.com/u/12800772?v=4);
                background-repeat: no-repeat;
                padding-top: 120px;
                background-position: 20px 20px;
                background-size: 200px 200px;
            }
            [data-testid="stSidebarNav"]::before {
                content: "";
                margin-left: 20px;
                margin-top: 20px;
                font-size: 15px;
                position: relative;
                top: 150px;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )
add_logo()
