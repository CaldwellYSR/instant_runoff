#!/usr/bin/python

import csv, sys

class Instant_Runoff:
    def __init__(self, f):
        reader = csv.reader(f)
        self.vote_dict = dict((rows[0],[rows[1], rows[2], rows[3], rows[4], rows[5]]) for rows in reader)
        self.results = {}
        for name, votes in self.vote_dict.iteritems():
            if name != "Votes":
                for index, val in enumerate(votes):
                    try:
                        self.results[val][index] =  0
                    except KeyError:
                        self.results[val] = {index: 0}

        for name, votes in self.vote_dict.iteritems():
            if name != "Votes":
                for index, val in enumerate(votes):
                    self.results[val][index] +=  1 

        self.cnt = len(self.vote_dict)
        self.check_results()
 

    def get_max(self, round_num):
        tmp = None
        for option, votes in self.results.iteritems():
            if tmp == None:
                tmp = option
                winner = option
            else:
                try:
                    if votes[round_num] > self.results[tmp][round_num]:
                        winner = option
                except KeyError:
                    pass

        return winner

    def get_min(self, round_num):
        tmp = None
        for option, votes in self.results.iteritems():
            if tmp == None:
                tmp = option
                loser = option
            else:
                try:
                    if votes[round_num] < self.results[tmp][round_num]:
                        loser = option
                except KeyError:
                    loser = option

        return loser
    
    def appropriate_votes(self, loser, round_num):
        delete = None
        for name, votes in self.vote_dict.iteritems():
            if name != "Votes":
                if self.vote_dict[name][round_num] == loser:
                    self.results[self.vote_dict[name][1]][0] += 1
                    delete = name

        if delete != None:
            del self.vote_dict[delete]

        self.check_results(round_num)
    
    def check_results(self, round_num=0):
        winner = self.get_max(round_num)
        loser = self.get_min(round_num)

        if self.results[winner][0] > self.cnt / 2.0:
            print "Winner: " + winner
        else:
            print "No winner found yet, deleting " + loser
            del self.results[loser]
            self.appropriate_votes(loser, round_num)

def main():
    with open(sys.argv[1], mode='r') as infile:
        ir = Instant_Runoff(infile)
 
    
if __name__ == "__main__":
    main()
