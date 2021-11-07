
# 1 
FROM python:3.7

# 2

RUN pip install -r requirements.txt

# Expose port 5000
EXPOSE 5000
#3
ENV PORT 5000
WORKDIR /

# 4
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 app:app
