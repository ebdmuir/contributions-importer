FROM python:3

WORKDIR /usr/src/app

RUN git clone https://github.com/miromannino/Contributions-Importer-For-Github.git .
RUN pip3 install gitpython pathlib

COPY ./run.py ./

CMD [ "ls" ]