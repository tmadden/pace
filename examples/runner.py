from DonJulioNoir import DJRSD, DJRSDfmln
from voting_fmln import voting_fmln
import numpy as np
import logging
import pace
import pprint
import multiprocessing

logging.basicConfig(level=logging.INFO)

#shortcuts:
a0203 = ['A0203']
#there are three others close to A0203: 0201, 0204, and [farthest] 0207
a0203train = ['A0203']
a68 = ['A6802']
b35 = ['B3501']
a31 = ['A3101']

a24 = ['A0204']
a24t = ['A0203', 'A0204']

b4403 = ['B4403']
b4403t = ['B4402', 'B4403']

b5802 = ['B5802']
b5802t = ['B5801', 'B5802']


#wrapper function for pace.evaluate call:
def worker(rseed, return_dict):
    scores = pace.evaluate(
        #DJRSD,
        #lambda: voting_fmln(5, 4, encoding_style='one_hot'),
        lambda: DJRSDfmln(5, 4, encoding_style='one_hot'),
        selected_lengths=[9, 10],
        #selected_lengths=[10],
        selected_alleles=b5802t,
        test_alleles=b5802,
        test_lengths=[10],
        dataset=pace.data.load_dataset(95),
        nbr_train=10,
        nbr_test=1000,
        random_seed=rseed * 3)
    return_dict[rseed] = scores


#choose the set of random seeds
rseeds = range(24)

manager = multiprocessing.Manager()
return_dict = manager.dict()
jobs = []

#run jobs in parallel
for rs in rseeds:
    p = multiprocessing.Process(target=worker, args=(rs, return_dict))
    jobs.append(p)
    p.start()

#wait for all runs to finish:
for proc in jobs:
    proc.join()

ppv_values = []
for r in return_dict.keys():
    s = return_dict[r]
    ppv_values.append(s['overall']['ppv'])
    print(s['overall']['ppv'])

mean_ppv = np.mean(ppv_values)
std_ppv = np.std(ppv_values)

print("Mean ppv is {:.2f}".format(mean_ppv))
print('Stdev of ppv is {:.3f}'.format(std_ppv))
