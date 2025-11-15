"""
This script exposes the FlaskWebProject 'app' object
so Azure App Service can load it using Gunicorn.
This file should NOT use ssl_context or debug server settings.
"""

from FlaskWebProject import app

# Azure uses Gunicorn to run the app, so we only need to expose `app`
# The block below only runs when using local development (python application.py)
if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5555,
        debug=True
    )
