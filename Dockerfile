FROM python:latest
RUN pip install plotly
RUN pip install dash
RUN pip install pandas

RUN git clone https://github.com/giovannorachmat/dkatalis-take-home-test-bi-analyst.git
RUN cd /dkatalis-take-home-test-bi-analyst/
CMD [ "bash", "./task_1.pdf" ]
CMD [ "bash", "./task_3.pdf" ]
