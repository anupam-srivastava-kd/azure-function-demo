// Import the necessary libraries.
import logging
import azure.functions as func

// Define the function.
def hello_world(req: func.HttpRequest) -> func.HttpResponse:
    // Get the request body.
    body = req.get_body()

    // Print the request body.
    logging.info(body)

    // Print "Hello, world!"
    return func.HttpResponse(
        body="Hello, world!",
        status_code=200,
    )
