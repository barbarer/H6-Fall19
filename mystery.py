# SI 206
# HW6 - Regular Expressions
# Name: 
# Who did you work with:　

import re
import os

def read_file(filename):
    """ Return a list of the lines in the file with the passed filename """
    
    # Open the file and get the file object
    source_dir = os.path.dirname(__file__) #<-- directory name
    full_path = os.path.join(source_dir, filename)
    infile = open(full_path,'r')
    
    # Read the lines from the file object into a list
    lines = infile.readlines()
    
    # Close the file object
    infile.close()
    
    # return the list of lines
    return lines

            
def find_IPs(filename):
    """ Return a list of valid IP addresses from the text file. 
    
        filename -- the name of the file to read from
        return -- the list of valid IP addresses found in the file
    """
    pass

    # initialize a list of IP addresses to an empty list

    # read the lines from the file into a list

    # define the regular expression

    # loop through the list of lines from the file

        # get the list of items that match the regular expression from the current line

        # add the list of items that matched to the list of dates found so far

    # return the list of dates


def find_zipcodes(filename):
    """ Return a list of valid zip codes in the text file with the given filename """
    pass


def find_dates(filename):
    """ Return a list of dates in the text file with the given filename """
    pass


def find_domains(filename):
    """ Return a list of domains in the text file with the given filename """
    pass


## Extra credit
def count_word(filename, word):
    """ Return the number of times a given word or its plural (add s) appears in the file 
    
        fileName -- the name of the file to read from
        word -- the word to look for
        return -- a count of the number of times the word or its plural appears in the file 
    """
    pass
        

## Do not modify the code below
## This function is for grading and debugging purposes
## statistics function reports your score based on the number of matches you got correct. 
def statistics(list1, list2):
    #print("Function output: ",list1)
    #print("Actual output: ", list2)
    matches = set(list2).intersection(set(list1)) 
    score = (len(matches)/len(list2))*15
    if len(matches)==len(list2):
        # no mismatches
        print("You found all the matches! Woohooo! Your score is: ", int(score))
    else:
        print("Looks like you missed some matches. Your score is:", int(score))
        print("You missed:", list(set(list2) - matches))

if __name__ == "__main__":
    filename = "The_Adventures_of_Sherlock_Holmes.txt"
    
    print("--------------------------------------------")
    #Report the accuracy of find_IP_address function
    print("1. Testing find_IPs function")
    statistics(find_IPs(filename), [
        '255.255.255.255',
        '192.168.3.1',
        '83.24.43.5',
        '192.183.6.254', 
        '127.0.0.1'
    ])

    print("--------------------------------------------")
    #Report the accuracy of find_zipcodes function
    print("2. Testing find_zipcodes function")
    statistics(find_zipcodes(filename), [
        '48105',
        '14325',
        '23451',
        '41123-2314',
        '63923-1323'
    ])

    print("--------------------------------------------")
    #Report the accuracy of find_dates function
    print("3. Testing find_dates function")
    statistics(find_dates(filename), [
        '12/29/02',
        '9/13/2020',
        '12-3-98',
        '12/09/20',
        '10-9-1899',
        '3.18.80',
        '10/31/16',
        '10-13-2021',
        '12.1.2018',
        '3.6.1991',
        '3/2/11',
        '5-16-1929',
        '3.4.91'])

    print("--------------------------------------------")
    # Report the accuracy of find_domains function
    print("4. Testing find_domains function")
    statistics(find_domains(filename), [
        'umsi.info',
        'google.com',
        'microsoft.co.jp',
        'e94d.org',
        'greatearth.earth'
    ])

    print("--------------------------------------------")
    print("Extra: Testing count_word function")
    count = count_word(filename,"lip")
    if count == 30:
        print("You made count_word correctly!      Your score is:   3")
    else:
        print("Count word for shoud return 28 and it returned: " + str(count))
    
    print("--------------------------------------------")
    
    




