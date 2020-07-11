RUN git clone https://github.com/giovannorachmat/dkatalis-take-home-test-bi-analyst.git
RUN cd /dkatalis-take-home-test-bi-analyst/
RUN open ~/task_1.pdf
RUN open ~/task_3.pdf

FROM python:alpine
RUN python task_2.py
