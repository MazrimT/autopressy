import logging

def make_logger():

    logging.basicConfig(
        format='%(asctime)s - %(message)s',
        filename='autopressy.log', 
        filemode='w',
        datefmt='%Y-%m-%d %H:%M:%S',
        level=logging.INFO,
        encoding='utf-8'
    )
    logger = logging.getLogger('autopressy')
    
    

    # bash logger/printer
    sh = logging.StreamHandler()
    sh.setLevel(logging.DEBUG)
    formatter = logging.Formatter(fmt='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    sh.setFormatter(formatter)
    logger.addHandler(sh)

    return logger