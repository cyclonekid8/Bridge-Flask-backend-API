# 1 
FROM python:3.7

# 2
COPY requirements.txt
RUN pip install -r requirements.txt

# 3
COPY . /app
# Expose port 5000
EXPOSE 5000
#4
ENV PORT 5000
WORKDIR /app

# 5
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 app:app