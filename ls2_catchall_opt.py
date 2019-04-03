#######################
##setup and variables##
conflicts = {}

size_L = float(env['snap']['layout']['what_kind_d_you_like3565']['fin_width'])
size_R = float(env['snap']['layout']['what_kind_d_you_like3565']['fin_height'])
size = str(size_L) + str("x") + str(size_R)
alt_size = str(size_R) + str("x") + str(size_L)
bleeds = lookup('does_your_ave_bleeds3135')
ink = lookup("is_your_prack__white4030")
finishing_options_1 = lookup('finishing_options_1')
finishing_options_2 = lookup('finishing_options_2')
finishing_options_3 = lookup('finishing_options_3')
pgs = int(lookup('how_many_pr_document3785'))
desc_1 = ''
desc_2 = ''
desc_3 = ''
desc_bind = ''
desc_misc = ''
desc_pack = ''

##PAPER CATALOG
ltr_paper = str('2015 2017 2022 2023 2047 2053 2054 2107 2059')
lgl_paper = str('2018 2024')
tab_paper = str('2004 2005 2014 2016 2020 2021 2028 2033 2034 2045 2055 2057 2062 2144 2145 2058 2035')
exc_paper = str('2008 2009 2019 2025 2026 2032 2036 2037 2046 2050 2051 2052 2061 2070 2071 2414')
exc_plus_paper = str('2029 2049 2060 2105 2056 2038 2048')
wide_f_paper = str('2127 2128 2129 2130 2300 2301 2302 2303 2304 2400 2401 2402 2403 2404 2405 2406 2407 2408 2409 2410 2411 2412')

init_limits=[]
fin1_limits=[]
fin2_limits=[]
fin3_limits=[]
bind_limit=[]
misc_limit=[]
pack_limit=[]
paper_limit =[]

###########################
####BEGIN THE FILTERING####

##initial load to not show paper options or finishing options until the ink option is selected.
if(ink == '0/0'):
  allow_init = '== 0/0'
  filter_init = ''

  ##conflict save for initialization of page
  init_limits.append(str('is_your_prack__white4030 ') + str(allow_init) + str(' allow ') + str(filter_init))
  conflicts['packaging'] = init_limits
  conflicts['misc_options'] = init_limits
  conflicts['binding_covers'] = init_limits
  conflicts['finishing_options_3'] = init_limits
  conflicts['finishing_options_2'] = init_limits
  conflicts['finishing_options_1'] = init_limits
  conflicts['what_kind_d_you_like3565'] = init_limits

  ##final output for line description and conflict save
  desc = str('(Size) ') + str(size) + str(" or ") + str(alt_size)
  save['*conflicts'] = conflicts

else: 
  ###########################
  ####PAPER OPTIONS LIMIT####

  ##if the ink option has been selected, then start filter paper and finishing options
  ##if bleeds == "yes"
  if bleeds == 'yes':
    if (size_L < 8.75 and size_R < 11.25) or (size_L < 11.25 and size_R < 8.75):
      ##if smaller than 8.75x11.25 is selected, allow user to select from 12x18 paper options
      allow_sizes = str('size < ') + size + str(' or size < ') + alt_size
      filter_list = exc_paper
    elif (size_L == 8.75 and size_R == 11.25) or (size_L == 11.25 and size_R == 8.75):
      ##if 8.75x11.25 (EXACTLY) is selected, allow user to select from 12x18 paper options
      allow_sizes = str('size == ') + size + str(' or size == ') + alt_size
      filter_list = exc_paper
    elif (size_L == 8.75 and size_R == 14.25) or (size_L == 14.25 and size_R == 8.75):
      ##if 8.75x14.25 (EXACTLY) is selected, allow user to select from 11x17 paper options
      allow_sizes = str('size == ') + size + str(' or size == ') + alt_size
      filter_list = tab_paper + str(" ") + exc_paper
    elif (size_L <= 11.25 and size_R <= 17.25) or (size_L <= 17.25 and size_R <= 11.25):
      ##if 11.25x17.25 or smaller is selected, allow user to select from 12x18 paper options
      allow_sizes = str('size <= ') + size + str(' or size <= ') + alt_size
      filter_list = exc_paper + str(" ") + exc_plus_paper
    elif (size_L <= 12.25 and size_R <= 18.25) or (size_L <= 18.25 and size_R <= 12.25):
      ##if 12.25x18.25 or smaller is selected, allow user to select from 13x19 paper options
      allow_sizes = str('size <= ') + size + str(' or size <= ') + alt_size
      filter_list = exc_plus_paper
    elif (size_L >= 13.0 and size_R >= 19.0) or (size_L >= 19.0 and size_R >= 13.0):
      ##if 13x19 or larger, is selected, allow user to select from wide format and single side only paper options
      allow_sizes = str('size >= ') + size + str(' or size >= ') + alt_size
      filter_list = wide_f_paper
    else:
      #otherwise force quote
      allow_sizes = str('size == ') + size + str(' or size == ') + alt_size
      filter_list = 'quote' 
  elif bleeds == 'no':
    ##if bleeds == "no"
    if (size_L < 8.5 and size_R < 11.0) or (size_L < 11.0 and size_R < 8.5):
      ##if smaller than 8.5x11 is selected, allow user to select from 12x18 paper options
      allow_sizes = str('size < ') + size + str(' or size < ') + alt_size
      filter_list = exc_paper
    elif (size_L == 8.5 and size_R == 11.0) or (size_L == 11.0 and size_R == 8.5):
      ##if 8.5x11 (EXACTLY) is selected, allow user to select from 11x17 paper options
      allow_sizes = str('size == ') + size + str(' or size == ') + alt_size
      filter_list = tab_paper
    elif (size_L == 8.5 and size_R == 14.0) or (size_L == 14.0 and size_R == 8.5):
      ##if 8.5x14 (EXACTLY) is selected, allow user to select from 8.5x14 paper options
      allow_sizes = str('size == ') + size + str(' or size == ') + alt_size
      filter_list = lgl_paper + str(" ") + tab_paper
    elif (size_L <= 11.0 and size_R <= 17.0) or (size_L <= 17.0 and size_R <= 11.0):
      ##if 11x17 or smaller is selected, allow user to select from 11x17 paper options
      allow_sizes = str('size <= ') + size + str(' or size <= ') + alt_size
      filter_list = tab_paper
    elif (size_L <= 12.0 and size_R <= 18.0) or (size_L <= 18.0 and size_R <= 12.0):
      ##if 12x18 or smaller is selected, allow user to select from 12x18 paper options
      allow_sizes = str('size <= ') + size + str(' or size <= ') + alt_size
      filter_list = exc_paper
    elif (size_L <= 13.0 and size_R <= 19.0) or (size_L <= 19.0 and size_R <= 13.0):
      ##if 13x19 or smaller is selected, allow user to select from 13x19 paper options
      allow_sizes = str('size <= ') + size + str(' or size <= ') + alt_size
      filter_list = exc_plus_paper
    elif (size_L <= 13.0 and size_R <= 19.0) or (size_L <= 19.0 and size_R <= 13.0):
      ##if larger than 13x19, allow user to select from wide format and single side only paper options
      allow_sizes = str('size <= ') + size + str(' or size <= ') + alt_size
      filter_list = wide_f_paper
    else:
      #othereise, force quote
      allow_sizes = str('size == ') + size + str(' or size == ') + alt_size
      filter_list = 'quote' 
  else:
    ##if bleeds has an issue, error out
    allow_sizes = str('quote')
    filter_list = 'quote'

  ##final conflict save for paper
  paper_limit.append(allow_sizes + str(' allow ') + filter_list)
  conflicts['what_kind_d_you_like3565'] = paper_limit 

  #####################
  #### FIN1 LIMITS ####
  if (size_L > 13.0 and size_R > 19.0) or (size_L > 19.0 and size_R > 13.0):
    allow_fin1 = str('size > ') + size + str(' or size > ') + alt_size
    filter_fin1 = str('none other')
    desc_1 = '> 13x19'

    ##final conflict save for fin1
    fin1_limits.append(allow_fin1 + str(' allow ') + filter_fin1)
    conflicts['finishing_options_1'] = fin1_limits
  else:
    desc_1 = '< 13x19'

  #####################
  #### FIN2 LIMITS ####
  if (size_L > 13.0 and size_R > 19.0) or (size_L > 19.0 and size_R > 13.0):
    allow_fin2 = str('size > ') + size + str(' or size > ') + alt_size
    filter_fin2 = str('none cut_in_half cut_to_blecore__fold2585')
    desc_2 = '> 13x19'

    ##final conflict save for fin2
    fin2_limits.append(allow_fin2 + str(' allow ') + filter_fin2)
    conflicts['finishing_options_2'] = fin2_limits
  else:
    desc_2 = '< 13x19'

  #####################
  #### FIN3 LIMITS ####
  if finishing_options_1 == 'none':
    allow_fin3 = str('finishing_options_1 == none')
    filter_fin3 = str('none lamination laminationg_foamcore3197 laminationgatorboard3414 mounting_only other')
    desc_3 = 'fin1 == none'
  elif finishing_options_1 != 'none':
    allow_fin3 = str('finishing_options_1 != none')
    filter_fin3 = str('')
    desc_3 = 'fin1 != none'
  else:
    allow_fin3 = str('')
    filter_fin3 = str('')
    desc_3 = 'error'

  ##final conflict save for fin3
  fin3_limits.append(allow_fin3 + str(' allow ') + filter_fin3)
  conflicts['finishing_options_3'] = fin3_limits 

  #######################
  #### BINDING LIMITS ####
  if finishing_options_1 == 'comb_binding':
    allow_bind = str('finishing_options_1 == comb_binding')
    filter_bind = str('none clear_coveblack_back2395 clear_covelear_cover2547 clear_cove_cardstock2988 printed_ca_cardstock3642')
    desc_bind = 'comb'
  elif finishing_options_1 == 'coil_bind':
    allow_bind = str('finishing_options_1 == coil_bind')
    filter_bind = str('none clear_coveblack_back2395 clear_covelear_cover2547 clear_cove_cardstock2988 printed_ca_cardstock3642')
    desc_bind = 'coil'
  elif finishing_options_1 == 'fastback_binding':
    allow_bind = str('finishing_options_1 == fastback_binding')
    filter_bind = str('none clear_coveblack_back2395 clear_covelear_cover2547 clear_cove_cardstock2988 printed_ca_cardstock3642')
    desc_bind = 'fastback'
  else:
    allow_bind = str('finishing_options_1 == ') + finishing_options_1
    filter_bind = ''
    desc_bind = "none"

  ##final conflict save for binding
  bind_limit.append(allow_bind + str(' allow ') + filter_bind)
  conflicts['binding_covers'] = bind_limit

  #####################
  #### MISC LIMITS ####
  if finishing_options_3 == 'laminationg_foamcore3197':
    allow_misc = str('finishing_options_3 == laminationg_foamcore3197')
    filter_misc = str('none _5in_easel _7in_easel _8in_easel _9in_easel _12in_easel other')
    desc_misc = 'lam + foam'
  elif finishing_options_3 == 'mounting_only':
    allow_misc = str('finishing_options_3 == mounting_only')
    filter_misc = str('none _5in_easel _7in_easel _8in_easel _9in_easel _12in_easel other')
    desc_misc = 'foam'
  elif finishing_options_3 == 'laminationgatorboard3414':
    allow_misc = str('finishing_options_3 == laminationgatorboard3414')
    filter_misc = str('none _5in_easel _7in_easel _8in_easel _9in_easel _12in_easel other')
    desc_misc = 'lam + gator'
  elif finishing_options_3 == 'lamination':
    allow_misc = str('finishing_options_3 == lamination')
    filter_misc = str('')
    desc_misc = 'lam'
  elif finishing_options_3 == 'none':
    allow_misc = str('finishing_options_3 == none')
    filter_misc = str('')
    desc_misc = 'none'
  else:
    allow_misc = str('')
    filter_misc = str('')
    desc_misc = "error"

  ##final conflict save for MISC
  misc_limit.append(allow_misc + str(' allow ') + filter_misc)
  conflicts['misc_options'] = misc_limit 

  #####################
  #### PACK LIMITS ####
  if (size_L > 13.0 and size_R > 19.0) or (size_L > 19.0 and size_R > 13.0):
    allow_pack = str('size > ') + size + str(' or size > ') + alt_size
    filter_pack = str('')
    desc_pack = "> 13x19"
  elif (size_L <= 13.0 and size_R <= 19.0) or (size_L <= 19.0 and size_R <= 13.0):
    if pgs <= 4:
      allow_pack = str('size <= ') + size + str(' or size <= ') + alt_size
      filter_pack = str('none any_amount shrink_wraackages_252934 shrink_wraackages_502932 shrink_wraackages_752939 shrink_wraackages_1002976 shrink_wraackages_1252983 shrink_wraackages_1502981 shrink_wraackages_1752988 shrink_wraackages_2002977 shrink_wraackages_2252984 shrink_wraackages_2502982 shrink_wraackages_2752989 shrink_wraackages_3002978 shrink_wraackages_4002979 shrink_wraackages_5002980 other')
      desc_pack = "<= 13x19 & <= 4pgs"
    elif pgs <= 10:
      allow_pack = str('size <= ') + size + str(' or size <= ') + alt_size
      filter_pack = str('none any_amount shrink_wraackages_252934 shrink_wraackages_502932 shrink_wraackages_752939 shrink_wraackages_1002976 shrink_wraackages_1252983 shrink_wraackages_1502981 shrink_wraackages_1752988 shrink_wraackages_2002977 shrink_wraackages_2252984 shrink_wraackages_2502982 other')
      desc_pack = "<= 13x19 & <= 10pgs"
    elif pgs <= 20:
      allow_pack = str('size <= ') + size + str(' or size <= ') + alt_size
      filter_pack = str('none any_amount shrink_wraackages_252934 shrink_wraackages_502932 shrink_wraackages_752939 shrink_wraackages_1002976 shrink_wraackages_1252983 shrink_wraackages_1502981 other')
      desc_pack = "<= 13x19 & <= 20pgs"
    else:
      allow_pack = str('')
      filter_pack = str('')
      desc_pack = "error 1"
  else:
    allow_pack = str('')
    filter_pack = str('')
    desc_pack = "error 2"

  ##final conflict save for PACKING
  pack_limit.append(allow_pack + str(' allow ') + filter_pack)
  conflicts['packaging'] = pack_limit  

##final output for line description and conflict save
desc = str('(Size) ') + str(size) + str(" or ") + str(alt_size) + str(' (fin1) ') + str(desc_1) + str(' (fin2) ') + str(desc_2) + str(' (fin3) ') + str(desc_3) + str(' (bind) ') + str(desc_bind) + str(' (misc) ') + str(desc_misc) + str(' (pack) ') + str(desc_pack)
save['*conflicts'] = conflicts
