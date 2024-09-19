import logging

name = input("Enter your name: ")

logging.basicConfig(filename="fileopen.log",
                    format='%(asctime)s %(message)s',
                    filemode='a')

logger = logging.getLogger()

logger.setLevel(logging.DEBUG)

logger.info(f"File open by {name}")