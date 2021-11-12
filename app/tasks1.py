from celery import Celery
from settings import config as conf

app = Celery( broker= conf.get("broker"))

@app.task(
    bind=True,
    max_retry=5,
    
)
def ola_mundo(ctx):    
    return 'olá mundo...'

if __name__ == '__main__':
    print(ola_mundo())

