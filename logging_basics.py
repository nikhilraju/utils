import logging
logger = logging.getLogger('lists-cleanup')
logger.setLevel(logging.INFO)
sh = logging.StreamHandler()
sh.setFormatter(logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
logger.addHandler(sh)
foo = 'hello'
logger.info('Logging something: %s',foo)
