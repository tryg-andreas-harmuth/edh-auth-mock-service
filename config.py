import logging

PORT = 8000

# Mock db for token access
ACCESS_MOCK_DB = {'050096c6e3a64489ff0ea3d1bcd4fb2a': [1, 2, 3],
                  '41c922284c9d6ff9ad61558be4a1a032': [1, 2],
                  '5fcdf50a544533d49db92df9ba48763b': [1, 2, 3],
                  '7038f2d2dc5b8ac40030e1ad964d127d': [1, 2],
                  '750d18490f63d62106ae2425e04b4774': [1],
                  'ab940507be5d3ae696db5f843f60c657': [1, 2],
                  'bad504c5a0ffc429ac58c4f0eb020838': [1, 2],
                  'bfd03a03d56dff9e801bf4b3fd48c2ed': [1, 2, 3],
                  'c2492641e83f56761142b72510609d14': [1],
                  'e79b5c5102d18d793415d8746428b469': [1, 2, 3]}


LOGGING_FORMAT = '[%(levelname)s] [%(asctime)s] %(message)s'
LOGGING_LEVEL = logging.DEBUG
