FROM postgres:alpine
COPY tables.sql /docker-entrypoint-initdb.d/
ADD tables.sql /docker-entrypoint-initdb.d
RUN chmod a+r /docker-entrypoint-initdb.d/*
EXPOSE 5432
