from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def hello(name=None,message=None):

    if name is None and message is None:
        text = 'Name and message is none'
    elif name is None:
        text = 'Name is none'
    elif message is None:
        text = 'Message is none'
    else:
        text = ['Hello ' + name + '!',
                message]
    return text