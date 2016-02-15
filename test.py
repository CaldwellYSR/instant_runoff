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
    
def appropriate_votes():
    cnt = 0.0
    for name, votes in vote_dict.iteritems():
        if name != "options":
            for index, val in enumerate(votes):
                if val == str(round_num):
                    cnt += 1
                    results[vote_dict["options"][index]] += 1

def check_results(results, vote_dict, round_num=0):
    winner = get_max(results, round_num)
    print "Winner: " + winner
    cut = get_min(results, round_num)
    print "Loser: " + cut
    """
    winner = get_max(res)
    cut = get_min(res)
    
    if res[winner] > cnt / 2.0:
        print "Winner: " + winner
    else:
        # Delete lowest and reappropriate results
        print "No Winner Yet!"
        round_num += 1
        del res[cut]
        vote_dict['options'].remove(cut)
        print vote_dict
        appropriate_votes(res, round_num, vote_dict)
    print winner
    print res
    """

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

    print results
    check_results(results, vote_dict)

    """
    results = {}
    for option in vote_dict["options"]:
        results[option] = 0

    round_num = 1
    cnt = 0.0
    for name, votes in vote_dict.iteritems():
        if name != "options":
            for index, val in enumerate(votes):
                if val == '1':
                    cnt += 1
                    results[vote_dict["options"][index]] += 1

    print results
    check_results(results, cnt, round_num, vote_dict)
    """

if __name__ == "__main__":
    main()
