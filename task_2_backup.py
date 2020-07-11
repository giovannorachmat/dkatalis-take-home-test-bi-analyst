# === IMPORTING LIBRARIES
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.graph_objects as go

import pandas as pd

# Exporting Data
your_username = '[INSERT YOUR DEFAULT USERNAME HERE]'
git_clone_dir = 'dkatalis-take-home-test-bi-analyst'
df_raw = pd.read_csv('/Users/{}/{}/luxury_loan_portfolio.csv'.format(your_username,git_clone_dir))
app = dash.Dash(__name__)
if __name__ == '__main__':
    app.run_server(debug=True)

# === DATA PREPROCESSING
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

# Change several columns to category type
df_pure['asset_type']=df_pure['asset_type'].astype('category')
df_pure['tax_class']=df_pure['tax_class'].astype('category')
df_pure['building_class_at_present']=df_pure['building_class_at_present'].astype('category')
df_pure['city']=df_pure['city'].astype('category')
df_pure['state']=df_pure['state'].astype('category')
df_pure['funded_date']=df_pure['funded_date'].astype('datetime64[ns]')

# df_pure.info()

# === BUSINESS QUESTIONS
# Q1
q1_df = df_pure.groupby(['tax_class','asset_type'])[['funded_amount']].agg('sum').reset_index() # Resetting index to make the funded_amount column name unchanged

# q1_df

q1_px = px.bar(q1_df, x="asset_type", y="funded_amount",
 color="tax_class",
 labels={"tax_class":"Tax Class","funded_amount":"$ Funded Amount","asset_type":"Type of Asset"},
 title='"Who bought what?" <br> Total Funded Amount per Type of Asset by Tax Class',
)

q1_px.update_yaxes( # the y-axis is in dollars
    tickprefix="$", showgrid=True
)
q1_px.update_layout(
    title={
    'x':0.5,
    'xanchor':'center',
    'yanchor':'top'
    }
)
q1_px.show()

# Q2
q2_df = df_pure.groupby(['tax_class','asset_type'])[['loan_id']].agg('count').reset_index() # Resetting index to make the funded_amount column name unchanged

# q2_df

q2_px = px.bar(q2_df, x="asset_type", y="loan_id",
 color="tax_class",
 labels={"tax_class":"Tax Class","loan_id":"# Funded Loans","asset_type":"Type of Asset"},
 title='"Who bought what?" <br> Total Funded Loans per Type of Asset by Tax Class',
)

q2_px.update_yaxes( # the y-axis is in dollars
    showgrid=True
)
q2_px.update_layout(
    title={
    'x':0.5,
    'xanchor':'center',
    'yanchor':'top'
    }
)
q2_px.show()

# Q3
q3_df_raw = df_pure.groupby(['title'])[['interest_rate_percent']].agg('mean').reset_index()
q3_df_sort = q3_df_raw.sort_values(by=['interest_rate_percent'],ascending=False)
q3_df_sort['title'] = q3_df_sort['title'].str.upper()
q3_df = q3_df_sort.head(10)
# q3_df

q3_px = px.bar(q3_df, x="title", y="interest_rate_percent",
 color="title",
 text='interest_rate_percent',
 labels={"title":"Job Title","interest_rate_percent":"Average Interest Rate"},
 title='"Higher Position = More Debt?" <br> Top 10 Average Interest Rate by Job Title',
)

q3_px.update_yaxes( # the y-axis is in dollars
    ticksuffix="%", showgrid=True
)

q3_px.update_xaxes(title="")

q3_px.update_layout(
    title={
    'x':0.5,
    'xanchor':'center',
    'yanchor':'top'
    },
    showlegend=False
)
q3_px.show()

# Q4
q4_df_raw = df_pure.groupby(['title'])[['loan_balance']].agg('mean').reset_index()
q4_df_sort = q4_df_raw.sort_values(by=['loan_balance'],ascending=False)
q4_df_sort['title'] = q4_df_sort['title'].str.upper()
q4_df = q4_df_sort.head(5)
# q4_df

q4_px = px.bar(q4_df, x="title", y="loan_balance",
 color="title",
 text='loan_balance',
 labels={"title":"Job Title","loan_balance":"Average Loan Balance"},
 title='"Be A Solution Manager They Said" <br> 5 Most Common Job Titles with High Average Loan Balance',
)

q4_px.update_yaxes( # the y-axis is in dollars
    tickprefix="$", showgrid=True
)
q4_px.update_xaxes(title="")

q4_px.update_layout(
    title={
        'x':0.5,
        'xanchor':'center',
        'yanchor':'top'
    },
    showlegend=False
    # legend=dict(
        # font=dict(size=10),
        # xanchor='auto',
        # yanchor='auto',
        # y=0.5,
    # ),
    # uniformtext_minsize=8
)
q4_px.show()
