#!/usr/bin/python

import csv, sys

def get_max(res, round_num):
    tmp = None
    for option, votes in res.iteritems():
        if tmp == None:
            tmp = option
            winner = option
        else:
            try:
                if votes[round_num] > res[tmp][round_num]:
                    winner = option
            except KeyError:
                pass

    return winner

def get_min(res, round_num):
    tmp = None
    for option, votes in res.iteritems():
        if tmp == None:
            tmp = option
            loser = option
        else:
            try:
                if votes[round_num] < res[tmp][round_num]:
                    loser = option
            except KeyError:
                loser = option

    return loser
    
def appropriate_votes(results, loser, vote_dict, round_num, cnt):
    delete = None
    for name, votes in vote_dict.iteritems():
        if name != "Votes":
            if vote_dict[name][round_num] == loser:
                print "Found at " + name
                results[vote_dict[name][round_num + 1]][0] += 1
                delete = name

    if delete != None:
        del vote_dict[delete]
    """
    cnt = 0.0
    for name, votes in vote_dict.iteritems():
        if name != "options":
            for index, val in enumerate(votes):
                if val == str(round_num):
                    cnt += 1
                    results[vote_dict["options"][index]] += 1
    """

def check_results(results, vote_dict, cnt, round_num=0):
    winner = get_max(results, round_num)
    loser = get_min(results, round_num)

    if results[winner][round_num] > cnt / 2.0:
        print "Winner: " + winner
    else:
        print "No winner found yet, deleting " + loser
        print results
        # Cut the loser and reappropriate their votes incriment round number
        del results[loser]
        appropriate_votes(results, loser, vote_dict, round_num, cnt)
        round_num += 1
        check_results(results, vote_dict, cnt, round_num)

def main():
    with open(sys.argv[1], mode='r') as infile:
        reader = csv.reader(infile)
        vote_dict = dict((rows[0],[rows[1], rows[2], rows[3], rows[4], rows[5]]) for rows in reader)

    results = {}
    for name, votes in vote_dict.iteritems():
        if name != "Votes":
            for index, val in enumerate(votes):
                try:
                    results[val][index] =  0
                except KeyError:
                    results[val] = {index: 0}

    for name, votes in vote_dict.iteritems():
        if name != "Votes":
            for index, val in enumerate(votes):
                results[val][index] +=  1 

    cnt = len(vote_dict)
    check_results(results, vote_dict, cnt)

if __name__ == "__main__":
    main()
