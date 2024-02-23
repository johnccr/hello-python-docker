FROM python:3.13.0a4

RUN mkdir /app
ADD ./app /app/
RUN pip install -r /app/requirements.txt
EXPOSE 80

RUN mkdir /html
ADD ./html /html/
EXPOSE 8080

WORKDIR /
ADD startup.sh /
RUN chmod +x /startup.sh
CMD ["bash", "startup.sh"]