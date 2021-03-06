"""
Module of handy functions.
"""

# do imports first, available to all functions in the module
import os, sys, shutil
from datetime import timedelta
from datetime import datetime

# define one or more variables, available to all functions in the module,
# even without passing it directly
my_secret_number = 47

def make_dir(dirname, clean=False):
    """
    Make a directory if it does not exist.
    Use clean=True to clobber the existing directory.
    """
    if clean == True:
        shutil.rmtree(dirname, ignore_errors=True)
        os.mkdir(dirname)
    else:
        try:
            os.mkdir(dirname)
        except OSError:
            pass # assume OSError was raised because directory already exists
            
def choose_item(indir, tag='', exclude_tag='', itext='** Choose item from list **'):
    """
    Choose an item from a directory listing.  You have to supply the directory to look in.
    Use './' to look in the current directory.  Use the optional keyword arguments
    tag and exclude tag to refine the list, and itext to modify the user prompt.
    """
    print('\n%s\n' % (itext))
    ilist_raw = os.listdir(indir)
    ilist_raw.sort()
    if len(tag) == 0:
        # exclude hidden files
        ilist = [item for item in ilist_raw if item[0] != '.']
    else:
        # include only items with "tag" in their name
        ilist = [item for item in ilist_raw if tag in item]
        
    if len(exclude_tag) == 0:
        pass
    else:
        ilist = [item for item in ilist if exclude_tag not in item]
    
    Nitem = len(ilist)
    idict = dict(zip(range(Nitem), ilist))
    for ii in range(Nitem):
        print(str(ii) + ': ' + ilist[ii])
    my_choice = input('-- Input number -- (return=0)')
    if len(my_choice)==0:
        my_choice = 0
    my_item = idict[int(my_choice)]
    return my_item
    
def square_my_number():
    """
    Test of using a value defined outside of the function.
    """
    xx = my_secret_number**2
    return xx


# edited from code found on the interwebs
def datenum_to_datetime(datenum):
    """
    Convert Matlab datenum into Python datetime.
    :param datenum: Date in datenum format, e.g. 737586.3347222221
    :return:        Python datetime object, converted by 366 days 
    """
    # day = integer of datenum (no decimal) - 366
    DD=datetime.fromordinal(int(datenum))
    DD = DD - timedelta(days=366)
    # calculate hour, min, sec from the fraction of a day in datenum:
    HH = datenum % 1 * 24
    MM = HH % 1 * 60
    SS = MM % 1 * 60
    FF = SS % 1 * 1000

    HH = timedelta(hours=int(HH))
    MM = timedelta(minutes=int(MM))
    SS = timedelta(seconds=int(SS))
    FF = timedelta(milliseconds=int(round(FF)))
    
    return DD + HH + MM + SS + FF