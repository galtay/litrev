import logging
import os
import tarfile
import wget


logger = logging.getLogger(__name__)


logging.basicConfig(level=logging.INFO)
BASE_DATA_PATH = "../data/srlconll05"
os.makedirs(BASE_DATA_PATH, exist_ok=True)

# get all data related to CoNLL 2004/2005 evaluations
wget_path = "http://www.lsi.upc.edu/~srlconll"

fnames = [
    "srlconll-1.1.tgz",
    "conll05st-release.tar.gz",
    "conll05st-tests.tar.gz",
]

for fname in fnames:
    local_target = os.path.join(BASE_DATA_PATH, fname)
    logger.info("checking local_target: {}".format(local_target))
    if not os.path.isfile(local_target):
        wget_target = os.path.join(wget_path, fname)
        logger.info("downloading wget_target: {}".format(wget_target))
        wget.download(wget_target, out=local_target)
        logger.info("extracting downloaded file: {}".format(local_target))
        tf = tarfile.open(local_target)
        tf.extractall(path=BASE_DATA_PATH)
    else:
        logger.info("local_target exists")
