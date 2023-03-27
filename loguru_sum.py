from loguru import logger

logger.add("file_{time}.log")

def sum(a,b):
    c = a+b
    logger.debug("a =="+str(a)+"; b=="+str(b)+"; sum=="+str(c))
    return c
    

sum(4,6)

