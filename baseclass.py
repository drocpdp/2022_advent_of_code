
class BaseClass:
    '''
    def get_data(self, day_str):
        fp = open('./data/{}.txt'.format(day_str), 'r')
        measures = [l.strip() for l in fp.readlines()]
        fp.close()           
        return measures
    '''

    def get_data(self, day_str):
        return (line for line in open('./data/{}.txt'.format(day_str)))