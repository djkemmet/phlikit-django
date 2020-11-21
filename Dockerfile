FROM python:alpine3.7
WORKDIR /phlikit
COPY . /app
run pip3 install django
EXPOSE 8080
ENTRYPOINT [ "python" ]
CMD [ "app.py"  ]
