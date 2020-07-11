FROM python:latest
ADD task_2.py /
RUN pip install plotly
RUN pip install dash
RUN pip install pandas
CMD [ "python", "./task_2.py" ]

RUN git clone https://github.com/giovannorachmat/dkatalis-take-home-test-bi-analyst.git
RUN cd dkatalis-take-home-test-bi-analyst
ADD task_1.pdf /
ADD task_3.pdf /
CMD ["open","task_1.pdf","task_3.pdf"]
