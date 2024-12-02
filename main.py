#! /usr/bin/env python

import logging, logging.config, coloredlogs

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Refer to
#   1. https://stackoverflow.com/a/7507842/1677041
#   2. https://stackoverflow.com/a/49400680/1677041
#   3. https://docs.python.org/2/library/logging.config.html
#		4. https://gist.github.com/bootandy/5546891
LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'standard': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
        'colored': {
            '()': 'coloredlogs.ColoredFormatter',
            'format': "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            'datefmt': '%H:%M:%S',
        }
    },
    'handlers': {
        'default': {
            'level': 'DEBUG' if __debug__ else 'INFO',
            'formatter': 'standard',
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stdout',  # Default is stderr
        },
        'console': {
            'level': 'DEBUG' if __debug__ else 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'colored',
            'stream': 'ext://sys.stdout'
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'formatter': 'standard',
            'filename': 'logs/main.log',
            'backupCount': 10,
            'when': 'midnight',
            'interval': 1,
        }
    },
    'loggers': {
        '': {  # root logger
            'handlers': ['console', 'file'],
            'level': 'DEBUG',
            'propagate': False
        },
        '__main__': {  # if __name__ == '__main__'
            'handlers': ['console', 'file'],
            'level': 'DEBUG',
            'propagate': False
        }
    }
}

logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger(__name__)



def main():
    logger.info("Initializing Chrome WebDriver...")

    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")  # Recommended for headless
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

    try:
        # Use WebDriver Manager instead of hardcoded path for better compatibility
        driver_path = ChromeDriverManager().install()
        logger.info(f"ChromeDriver path: {driver_path}")

        service = Service(executable_path=driver_path)
        driver = webdriver.Chrome(service=service, options=chrome_options)
        logger.info("Chrome WebDriver initialized successfully")

        # Open x.com timeline
        driver.get("https://x.com")

        # Wait for the page to load
        driver.implicitly_wait(10)  # seconds

        # You can add more interactions here if needed

    except Exception as e:
        logger.error(f"Failed to initialize Chrome WebDriver: {str(e)}")
        raise
    finally:
        if 'driver' in locals():
            driver.quit()
            logger.info("Chrome WebDriver closed")

if __name__ == "__main__":
    main()
