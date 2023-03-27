import uvicorn

from web.app import create_app


app = create_app

if __name__ == '__main__':
    """
    Runs the algolia connector locally
    """
    # uvicorn.run("application:app", host="0.0.0.0", port=8777, log_level="debug")
    uvicorn.run("application:app", host="0.0.0.0", port=9001, log_level="debug")
