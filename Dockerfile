FROM continuumio/miniconda3

RUN conda install scikit-learn
RUN pip install fastapi uvicorn python-multipart requests jax-unirep

EXPOSE 80

COPY ./main.py main.py

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
