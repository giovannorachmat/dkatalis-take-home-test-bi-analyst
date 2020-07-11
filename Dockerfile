FROM python:latest
RUN pip install plotly
RUN pip install dash
RUN pip install pandas

RUN git clone https://github.com/giovannorachmat/dkatalis-take-home-test-bi-analyst.git
RUN cd /dkatalis-take-home-test-bi-analyst/
CMD [ "bash", "./dkatalis-take-home-test-bi-analyst/task_1.pdf" ]
CMD [ "bash", "./dkatalis-take-home-test-bi-analyst/task_3.pdf" ]
CMD [ "python", "./dkatalis-take-home-test-bi-analyst/task_2.py" ]
