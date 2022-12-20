import re

def identify_apex_from_filename(filename):

    """ 
    Function for extracting the APEX number from the APEX datafile name.
    In the future it would be good to standardize these names so this is less
    difficult. 
    """

    remove_before_apex = re.findall('APEX.*|Apex.*|apex.*', filename)[0]
    strip_apex = remove_before_apex[4:8].lstrip('0')
    apex_number = re.findall('\d*', strip_apex)[0]

    print('APEX NUMBER: {}'.format(apex_number))

    return('APEX ' + apex_number)



# test cases
identify_apex_from_filename('Apex4_cc__amqc_DQC_000001_2022126_003.dat')

identify_apex_from_filename('APEX004-CC_AMQC_DQC_000001_2022286_001.dat')

identify_apex_from_filename('APEX5_cc_PMQC_DQC_000001_2022136_001.dat')

identify_apex_from_filename('APEX010-CC_PMQC_DQC_000001_2022291_003.dat')

identify_apex_from_filename('APEX013-CC_AMQC_DQC_000001_2022294_003.dat')

identify_apex_from_filename('APEX13_CC_PMQC_DQC_000001_2022129_001.dat')

identify_apex_from_filename('APEX019-LEB-20220803_IVS2-PM_DQC_000001_2022216_002.dat')

identify_apex_from_filename('APEX014-CampRobinson-1_IVS_DQC_000001_2022308_006.dat')

identify_apex_from_filename('20220511_APEX11_BAFS_IVS3_DQC_000001_2022132_003.dat')