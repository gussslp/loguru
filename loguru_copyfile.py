from loguru import logger
import shutil
logger.add("file_{time}.log")
file = "file"
path = "path"
def copy(file):
    start = file
    target = "%s\\ %s " % (path,file)

    shutil.copyfile(start, target)
    logger.debug("start == %s; target == %s;" % (start ,target))

copy(file)
