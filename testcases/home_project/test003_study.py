import logging
import os
import pytest

path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
log_path = path + "/logs/test.log"
logger = logging.getLogger(log_path)
#
logger.info("logging information")

if __name__ == '__main__':
    print(log_path)
    logging.debug("debug...")
    logging.info("info...")
    logging.warning("warning...")
    logging.error("error...")
    logging.critical("critical...")
    pytest.main()
