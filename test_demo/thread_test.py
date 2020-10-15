import threading
from concurrent import futures

import logging
import time

FORMAT = '%(asctime)-15s\t  %(process)s %(threadName)s %(process)s %(message)s'
logging.basicConfig(level=logging.INFO, format=FORMAT)