from wsgiref.simple_server import make_server
import logging
import falcon as falcon
import config

logging.basicConfig(format=config.LOGGING_FORMAT, level=config.LOGGING_LEVEL, datefmt='%Y-%m-%d %H:%M:%S')


# Import resources
from Resources.user_access import UserAccessResource

# Initialize app
app = falcon.API()

# Add routes
app.add_route("/access/{user_token}", UserAccessResource())

# Run server in debug mode
if __name__ == "__main__":
    with make_server("0.0.0.0", config.PORT, app) as httpd:
        logging.info(f"Using falcon {falcon.version.__version__}")
        logging.info(f"Serving on port http://localhost:{config.PORT}")

        # Serve until process is killed
        httpd.serve_forever()

    logging.info("API Server has been closed")