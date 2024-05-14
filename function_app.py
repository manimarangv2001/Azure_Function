import azure.functions as func
import logging
from Azure_OpenAI import configure_openai


app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="http_trigger")
def http_trigger(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    question = req.params.get('question')
    if not question:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            question = req_body.get('question')

    if question:
        answer=configure_openai.openAIFunction(question)
        return func.HttpResponse(str(answer))
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a question in the query string or in the request body for a personalized response.",
             status_code=200
        )