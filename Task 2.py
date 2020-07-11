import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
pio.renderers.default='notebook'

import pandas as pd

df_raw = pd.read_csv('/Users/giovannorachmat/Git (Personal)/dkatalis-take-home-test-bi-analyst/datasets/luxury_loan_portfolio.csv')

# Removing unnecessary columns
df_parse = df_raw.drop(columns=[
    '10 yr treasury index date funded',
    'firstname',
    'middlename',
    'lastname',
    'social',
    'phone',
    'ADDRESS 1',
    'ADDRESS 2',
    'ZIP CODE',
    'TOTAL UNITS',
    'LAND SQUARE FEET',
    'GROSS SQUARE FEET',
    'TAX CLASS AT TIME OF SALE',
    'BUILDING CLASS CATEGORY'
])

# Renaming columns for standardization
df_pure = df_parse.rename(columns={
    'TAX CLASS AT PRESENT':'tax_class',
    'BUILDING CLASS AT PRESENT':'building_class_at_present',
    'CITY':'city',
    'STATE':'state',
    'payments':'payment_amount',
    'purpose':'asset_type',
    'duration years':'duration_years',
    'duration months':'duration_months',
    'interest rate percent':'interest_rate_percent',
    'interest rate':'interest_rate',
    'total past payments':'total_past_payments',
    'loan balance':'loan_balance',
    'property value':'property_value',
    'employment length':'employment_length'
})

df_pure['asset_type']=df_pure['asset_type'].astype('category')
df_pure['tax_class']=df_pure['tax_class'].astype('category')
df_pure['building_class_at_present']=df_pure['building_class_at_present'].astype('category')
df_pure['city']=df_pure['city'].astype('category')
df_pure['state']=df_pure['state'].astype('category')
df_pure['funded_date']=df_pure['funded_date'].astype('datetime64[ns]')

# Get total number of funded amount per asset_type
q1_df = df_pure.groupby(['tax_class','asset_type'])[['funded_amount']].agg('sum').reset_index() # Resetting index to make the funded_amount column name unchanged

q1_df

q1_px = px.bar(q1_df, x="asset_type", y="funded_amount",
 color="tax_class",
 labels={"funded_amount":"Total Funded Amount","asset_type":"Type of Asset","tax_class":"Tax Class"},
 title="Total Funded Amount per Purpose"
)

q1_px.show()
