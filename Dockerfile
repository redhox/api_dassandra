FROM python:3.10-slim

WORKDIR /app

COPY requierement.txt ./

RUN pip install -r requierement.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]