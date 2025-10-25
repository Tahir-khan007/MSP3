import os
import multiprocessing


bind = f"0.0.0.0:{os.environ.get('PORT', '8080')}"

workers = int(os.environ.get('GUNICORN_WORKERS', '1'))

worker_class = 'sync'

timeout = int(os.environ.get('GUNICORN_TIMEOUT', '120'))

accesslog = '-'  # Log to stdout
errorlog = '-'   # Log to stderr
loglevel = os.environ.get('LOG_LEVEL', 'info')

# Preload app
# Set to True to load the app before forking workers
preload_app = True

daemon = False
pidfile = None
umask = 0
user = None
group = None
tmp_upload_dir = None

def on_starting(server):
    """Called just before the master process is initialized."""
    print("=" * 60)
    print("Gunicorn is starting...")
    print(f"Workers: {workers}")
    print(f"Preload: {preload_app}")
    print("=" * 60)

def when_ready(server):
    """Called just after the server is started."""
    print("=" * 60)
    print("Gunicorn server is ready. Waiting for requests...")
    print("=" * 60)

def on_exit(server):
    """Called just before exiting Gunicorn."""
    print("=" * 60)
    print("Gunicorn is shutting down...")
    print("=" * 60)
