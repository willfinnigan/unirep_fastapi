FROM continuumio/miniconda3

RUN conda install scikit-learn
RUN pip install fastapi uvicorn python-multipart requests jax-unirep

EXPOSE 8081

COPY ./main.py main.py

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8081"]