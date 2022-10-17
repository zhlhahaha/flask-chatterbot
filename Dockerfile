FROM python:3.6

COPY . /app/
WORKDIR /app

RUN pip install -r requirements.txt
RUN BLIS_ARCH="generic" pip install spacy --no-binary blis
RUN pip install spacy
RUN patch -p0 /usr/local/lib/python3.6/site-packages/chatterbot/tagging.py tagging.patch
RUN python -m spacy download en_core_web_sm
