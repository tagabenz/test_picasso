FROM python:latest

    COPY requirements.txt cmd.sh ./

    RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt
    
    WORKDIR /app
    COPY my_app .
    
    # CMD ["./manage.py", "runserver", "0.0.0.0:8000"]
    ENTRYPOINT ["../cmd.sh"]
