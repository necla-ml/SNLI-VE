'''
SNLI-VE Parser
This file provide a sample code for parsing SNLI-VE dataset

Author: Ning Xie, xie.25@wright.edu

# Copyright (C) 2018 NEC Laboratories America, Inc. ("NECLA"). 
# All rights reserved.
#
# This source code is licensed under the license found in the LICENSE file in
# the root directory of this source tree. An additional grant of patent rights
# can be found in the PATENTS file in the same directory.
'''

import os
import jsonlines


def parser(SNLI_VE_root, SNLI_VE_files, choice):
    '''
    This is a sample function to parse SNLI-VE dataset

    :param SNLI_VE_root: root of SNLI-VE dataset
    :param SNLI_VE_files: filenames of each data split of SNLI-VE
    :param choice: data split choice, train/dev/test
    '''
    filename = os.path.join(SNLI_VE_root, SNLI_VE_files[choice])
    with jsonlines.open(filename) as jsonl_file:
        for line in jsonl_file:
            # #######################################################################
            # ############ Items used in our Visual Entailment (VE) Task ############
            # #######################################################################

            # => Flikr30kID can be used to find corresponding Flickr30k image premise
            Flikr30kID = str(line['Flikr30kID'])
            # =>  gold_label is the label assigned by the majority label in annotator_labels (at least 3 out of 5),
            # If such a consensus is not reached, the gold label is marked as "-",
            # which are already filtered out from our SNLI-VE dataset
            gold_label = str(line['gold_label'])
            # => hypothesis is the text hypothesis
            hypothesis = str(line['sentence2'])


            # #######################################################################
            # ######## Extra information for Possible Extensions of VE Task #########
            # #######################################################################

            # => hypothesis_binary_parse is the original hypothesis_binary_parse from SNLI dataset
            hypothesis_binary_parse = str(line['sentence2_binary_parse'])
            # => hypothesis_parse is the original hypothesis_parse from SNLI dataset
            hypothesis_parse = str(line['sentence2_parse'])
            # =>  annotator_labels is a list of annotations for current (premise, hypothesis) pair
            annotator_labels = [str(item) for item in line['annotator_labels']]
            # =>  captionID is the original image caption ID from SNLI dataset
            captionID = str(line['captionID'])
            # =>  pairID is the original (premise, hypothesis) pair ID from SNLI dataset
            pairID = str(line['pairID'])
            # => premise is the original text premise, which is not used in our VE task
            premise = str(line['sentence1'])
            # => premise_binary_parse is the original premise_binary_parse from SNLI dataset
            premise_binary_parse = str(line['sentence1_binary_parse'])
            # => premise_parse is the original premise_parse from SNLI dataset
            premise_parse = str(line['sentence1_parse'])






if __name__ == '__main__':

    # SNLI-VE paths
    SNLI_VE_root = './'
    SNLI_VE_files = {'dev': 'snli_ve_dev.jsonl',
                     'test': 'snli_ve_test.jsonl',
                     'train': 'snli_ve_train.jsonl'}
    choice = 'dev'

    parser(SNLI_VE_root, SNLI_VE_files, choice)