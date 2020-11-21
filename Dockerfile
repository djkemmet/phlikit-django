FROM python:alpine3.7
COPY . /app
WORKDIR /app
run pip3 install flask flask_restful flask_jwt
EXPOSE 8080
ENTRYPOINT [ "python" ]
CMD [ "app.py"  ]
