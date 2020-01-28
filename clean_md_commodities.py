import pandas as pd
import numpy as np
import sys
np.set_printoptions(threshold=sys.maxsize)

# read in both excel files into pandas dataframes
md_files = pd.read_excel('G:\\datasets\\mining_district\\mining_district_files_12202019.xlsx')
commodities = pd.read_excel('G:\\datasets\\mining_district\\nv_commodities.xlsx')

# take a look at unique values in the mining district files commodities list
comm_list = md_files.commodity.str.cat(sep="; ")
comm_list_arr = comm_list.split("; ")
comm_list_arr = np.unique(comm_list_arr, axis=0)

# identify values that are in the mining district file spreadsheet but NOT in the commodities master list

#first, change lists to sets and make them all lower case for comparison
lower_md_comm = {item.lower() for item in comm_list_arr}
lower_gen_comm = {item.lower() for item in commodities.name}

#find out what values are in the mining district files that do overlap with the commodities master list, and which ones don't
not_in = lower_md_comm.difference(lower_gen_comm)
intersection = lower_md_comm.intersection(lower_gen_comm)

df=pd.DataFrame(md_files)
df.replace(to_replace ='BAIRITE', value ="BARYTE") 

df=pd.DataFrame(lower_gen_comm)
df.replace(to_replace = 'molybdenium', value= 'molybdenum')
df.replace(to_replace= 'vanandinite', value='vanadinite')
df.replace(to_replace= 'soduim', value='sodium')
df.replace(to_replace='lead tungston', value='lead tungsten')
df.replace(to_replace='leaseable', value='leasable')
df.replace(to_replace='wallastonite', value='wollastonite')
df.replace(to_replace='neodynium', value='neodymium')
df.replace(to_replace='copper tungston', value='copper tungsten')
df.replace(to_replace='kuroko base metal deposit', value='kuroko deposit')
df.replace(to_replace='uraniforous', value='uraniferous')
df.replace(to_replace='sodium sufate', value='sodium sulfate')

df=pd.DataFrame(lower_md_comm)
df.replace(to_replace='platimun', value='platinum')
df.replace(to_replace='tunsten', value='tungsten')
df.replace(to_replace='silca sand',value='silica sand')
df.replace(to_replace='murcury', value='mercury')
df.replace(to_replace='glod', value='gold')
df.replace(to_replace='hornsilver', value='horn silver')
df.replace(to_replace='magnesiuim', value= 'magnesium')
df.replace(to_replace='varicite', value='variscite')
df.replace(to_replace='fluorspar;barite', value='fluorspar; barite')
df.replace(to_replace='fledspar', value='feldspar')
df.replace(to_replace='bitumens', value='bituminous minerals')
df.replace(to_replace='fluroite', value= 'fluorite')
df.replace(to_replace='lead-sillver', value= 'lead-silver')
df.replace(to_replace='hgold', value='gold')
df.replace(to_replace='cpper', value='copper')
df.replace(to_replace='artimony', value='antimony')
df.replace(to_replace='coppper', value='copper')
df.replace(to_replace='molybdeum', value='molybdneum')
df.replace(to_replace='flourite', value='fluorite')
df.replace(to_replace='sheelite', value='scheelite')
df.replace(to_replace='chlorargyite', value='chlorargyrite')
df.replace(to_replace='malacite', value='malachite')
df.replace(to_replace='mangansese', value='manganese')
df.replace(to_replace='vanandinite', value='vanadinite')
df.replace(to_replace='soduim nitrate', value='sodium nitrate')
df.replace(to_replace='flurotie', value='fluorite')
df.replace(to_replace='tungston', value='tunsten')
df.replace(to_replace='wolastonite', value='wollastonite')
df.replace(to_replace='mangnaese', value='manganese')
df.replace(to_replace='molybdemum', value='molybdenum')
df.replace(to_replace='silver;copper', value='silver; copper')
df.replace(to_replace='wulphur', value='sulphur')
df.replace(to_replace='cerrusite', value='cerrussite')
df.replace(to_replace='zince', value= 'zinc')
df.replace(to_replace='ainc', value='zinc')
df.replace(to_replace='paladium', value='palladium')
df.replace(to_replace='salines', value= 'saline minerals')
df.replace(to_replace='cpidote', value= 'epidote')
df.replace(to_replace='batite', value='barite')
df.replace(to_replace='ceragyrite', value='cerargyrite')
df.replace(to_replace='liemstone', value='limestone')
df.replace(to_replace='ismium', value='osmium')
df.replace(to_replace='pumacite', value='pumicite')
df.replace(to_replace='cuo', value= 'copper oxide')
df.replace(to_replace='siler', value='silver')
df.replace(to_replace='rungsten', value='tungsten')
df.replace(to_replace='goldl', value='gold')
df.replace(to_replace='phospherous', value='phosphorous')
df.replace(to_replace='marganese', value='manganese')
df.replace(to_replace='wollastorite', value='wollastonite')
df.replace(to_replace='molybdenyum', value='molybdenum')
df.replace(to_replace='goled', value='gold')
