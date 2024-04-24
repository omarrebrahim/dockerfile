FROM  python    
WORKDIR /project
COPY . /docker
RUN pip install nltk
RUN pip install pandas
RUN pip install numpy

CMD [ "python3","code.py" ]
