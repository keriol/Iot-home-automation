from fastapi import FastAPI

app = FastAPI()


def alexa_response(text: str):
    return {
        "version": "1.0",
        "response": {
            "outputSpeech": {
                "type": "PlainText",
                "text": text,
            },
            "shouldEndSession": True,
        },
    }


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/alexa/example")
def alexa_example():
    return alexa_response("Example response from Home Assistant bridge.")
