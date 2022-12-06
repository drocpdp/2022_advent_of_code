from collections import Counter
from baseclass import BaseClass

class Day6All(BaseClass):

    def __init__(self):
        """ sliding window """
        dt = self.get_data('day6_1')[0]
        print('Part 1:{}'.format(self.get_start_bit(4, dt)))
        print('Part 2:{}'.format(self.get_start_bit(14, dt)))

    def get_start_bit(self, pckt_len: int, packet: str)->int:
        """ 
        Scan packet for substr of len pckt_len unique chars
        Returns end location (0-based) of such packet
        """

        holder = Counter()
        
        for i, ch in enumerate(packet):
            # add 
            holder.update(ch)

            # get 4 initial characters in
            if i < pckt_len:
                continue

            # remove earliest char
            holder.subtract(packet[i-pckt_len])

            # 4 unique chars
            if len(set(holder.elements())) == pckt_len:
                return (i+1)

if __name__=="__main__":
    Day6All()        