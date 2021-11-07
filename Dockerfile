
# 1 
FROM python:3.7

# 2
COPY requirements.txt /
RUN pip install -r requirements.txt

# Expose port 5000
EXPOSE 8080
#3
ENV PORT 8080
WORKDIR /

# 4
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 app:app
