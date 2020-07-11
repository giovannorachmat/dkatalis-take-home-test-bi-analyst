FROM python:latest
RUN pip install plotly
RUN pip install dash
RUN pip install pandas
COPY . /app
ENTRYPOINT ["python","app/task_2.py","luxury_loan_portfolio.csv"]
