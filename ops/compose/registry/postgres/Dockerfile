FROM postgres@sha256:e38a7fe2234174d0eb69b5467d346e1bb193c09f98adc229fc9df30fe364dd4a

COPY init_db.sh /docker-entrypoint-initdb.d/

RUN chmod +x /docker-entrypoint-initdb.d/init_db.sh

EXPOSE 5432

CMD ["docker-entrypoint.sh", "postgres"]