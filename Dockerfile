FROM python:3.6-alpine
COPY . /build
WORKDIR /build
RUN pip install -r requirements.txt
ENTRYPOINT ["/build/update-windows-release-json.py"]
