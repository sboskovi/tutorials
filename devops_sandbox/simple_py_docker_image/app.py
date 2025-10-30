import sys
import time
import logging

logger = logging.getLogger("main_logger")
logger.setLevel(logging.INFO)
handler = logging.StreamHandler(stream=sys.stdout)
logger.addHandler(handler)


def main():
    logger.debug("Started application")
    seconds_count = 0

    while True:
        logger.info("Running for %s seconds", seconds_count)
        seconds_count = seconds_count + 1
        time.sleep(1)


if __name__ == "__main__":
    main()

