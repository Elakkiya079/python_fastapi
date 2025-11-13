from fastapi import FASTAPI

app =fastapi()

@app.get('/users')
def get_users():
    return 'Hi welcome to Python-FAST API'