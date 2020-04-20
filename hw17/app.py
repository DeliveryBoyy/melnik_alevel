from datetime import datetime
import traceback

from main import main

if __name__ == "__main__":
    try:
        main()
    # If any Exception occurs, write it's time, type and traceback logs.txt file.
    except Exception as error:
        with open('logs.txt', 'a') as f:
            f.write('{datetime} {exception_type} {traceback}'.format(
                datetime=datetime.now(),
                exception_type=error.__class__.__name__,
                traceback=traceback.format_exc()))
