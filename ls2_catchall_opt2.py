#######################
##setup and variables##
conflicts = {}

size_R = float(env['snap']['layout']['what_kind_d_you_like3565']['fin_width'])
size_L = float(env['snap']['layout']['what_kind_d_you_like3565']['fin_height'])
size = str(size_L) + str("x") + str(size_R)
alt_size = str(size_R) + str("x") + str(size_L)
pageDNA_size = lookup('what_is_thur_project3488')
bleeds = lookup('does_your_ave_bleeds3135')
ink = lookup("is_your_prack__white4030")

###########################
####BEGIN THE FILTERING####

##initial load to not show paper options or finishing options until the ink option is selected.
if(ink == '0/0'):
  init_limits = []
  allow_init = '== 0/0'
  filter_init = ''

  ##conflict save for initialization of page
  init_limits.append(str('is_your_prack__white4030 ') + str(allow_init) + str(' allow ') + str(filter_init))
  conflicts['packaging'] = init_limits
  conflicts['misc_options'] = init_limits
  conflicts['binding_covers'] = init_limits
  conflicts['finishing_ns_per_set2764'] = init_limits
  conflicts['finishing__per_sheet2969'] = init_limits
  conflicts['finishing_s_per_sqft2878'] = init_limits
  conflicts['what_kind_d_you_like3565'] = init_limits
  conflicts['setups'] = init_limits

  descript = str("no ink")
else: 
  #######################
  ##setup and variables##
  paper_limit = []

  ##PAPER CATALOG
  ltr_paper = '2015 2017 2022 2023 2054 2059 2107 2108 2111 2165 2167 2169 2170'
  lgl_paper = '2018 2024 2141 2142'
  tab_paper = '2004 2005 2014 2016 2020 2021 2028 2033 2034 2045 2055 2057 2058 2062 2144 2145 2171'
  exc_paper = '2008 2009 2019 2025 2026 2032 2036 2037 2046 2050 2051 2052 2060 2070 2071 2414'
  exc_plus_paper = '2029 2038 2048 2049 2056 2105'
  wide_f_paperA = '2300'
  wide_f_paperB = '2127 2129 2130 2301 2400 2401 2403 2405 2407'
  wide_f_paperC = '2127 2129 2130 2301 2303 2400 2401 2403 2405 2407'
  wide_f_paperD = '2127 2129 2130 2301 2405 2407'
  wide_f_paperE = '2302'
  wide_f_paperF = '2127 2129 2130 2303 2400 2401 2403 2405 2407'
  envelop = '4019 4020 4021 4022 4023 4025 4028 4029 4030 4031 4032 4034 4035'
  vinyl = '4701 4702 4703 4704 4705 4706 4707 4708 4709 4710 4711 4712 4713 4714 4715 4750 4751 4752 4753 4754 4755 4756 4953 4954'
  dye_sub = '4800 4850 4851 4852 4853 4854 4855 4856 4857 4858 4859 4860 4861 4862 4863 4864 4865 4866 4867 4868'
  uv = '4250 4301 4302 4303 4305 4306 4307 4309 4310 4313 4316 4350 4500 4501 4503 4869 4870'
  stamp = '4100 4104 4108 4112 4116 4120 4124 4128 4132 4136 4140'
  apparel = '4921 4922 4923 4924 4925 4926'
  misc = '4950 4951 4953 4954 4927'

###########################
####PAPER OPTIONS LIMIT####

###########
##IF BLEEDS
###########
  if bleeds == 'yes':
    if size_L < 8.75 and size_R < 11.25:
      ##if smaller than 8.75x11.25 is selected, allow user to select from 12x18 paper options
      filter_list = exc_paper
      descript = str("bleed + less than 8.75x11.25")
    elif size_L < 11.25 and size_R < 8.75:
      ##if smaller than 11.25x8.75 is selected, allow user to select from 12x18 paper options
      filter_list = exc_paper
      descript = str("bleed + less than 11.25x8.75")
    elif size_L == 8.75 and size_R == 11.25:
      ##if 8.75x11.25 (EXACTLY) is selected, allow user to select from 12x18 paper options
      filter_list = exc_paper
      descript = str("bleed + exact 8.75x11.25")
    elif size_L == 11.25 and size_R == 8.75:
      ##if 11.25x8.75 (EXACTLY) is selected, allow user to select from 12x18 paper options
      filter_list = exc_paper
      descript = str("bleed + exact 11.25x8.75")
    elif size_L == 8.75 and size_R == 14.25:
      ##if 8.75x14.25 (EXACTLY) is selected, allow user to select from 11x17 paper options
      filter_list = tab_paper + str(" ") + exc_paper
      descript = str("bleed + exact 8.75x14.25")
    elif size_L == 14.25 and size_R == 8.75:
      ##if 14.25x8.75 (EXACTLY) is selected, allow user to select from 11x17 paper options
      filter_list = tab_paper + str(" ") + exc_paper
      descript = str("bleed + exact 14.25x8.75")
    elif size_L <= 11.25 and size_R <= 17.25:
      ##if 11.25x17.25 or smaller is selected, allow user to select from 12x18 paper options
      filter_list = exc_paper + str(" ") + exc_plus_paper
      descript = str("bleed + less than 11x17")
    elif size_L <= 17.25 and size_R <= 11.25:
      ##if 17.25x11.25 or smaller is selected, allow user to select from 12x18 paper options
      filter_list = exc_paper + str(" ") + exc_plus_paper
      descript = str("bleed + less than 17x11")
    elif size_L <= 13.00 and size_R <= 19.00:
      ##if 13x19 or smaller is selected, allow user to select from 13x19 paper options
      filter_list = exc_plus_paper
      descript = str("bleed + less than 12x18")
    elif size_L <= 19.00 and size_R <= 13.00:
      ##if 19x13 or smaller is selected, allow user to select from 13x19 paper options
      filter_list = exc_plus_paper
      descript = str("bleed + less than 19x13")
    elif size_L <= 15.00 and size_R <= 21.00:
      ##if 15x21 or smaller is selected, allow user to select from 15x21 paper options
      filter_list = wide_f_paperA
      descript = str("bleed + less than 15x21")
    elif size_L <= 21.00 and size_R <= 15.00:
      ##if 15x21 or smaller is selected, allow user to select from 15x21 paper options
      filter_list = wide_f_paperA
      descript = str("bleed + less than 21x15")
    elif size_L <= 18.00 and size_R <= 24.00:
      ##if 18x24 or smaller is selected, allow user to select from 18x24 paper options
      filter_list = wide_f_paperB
      descript = str("bleed + less than 18x24")
    elif size_L <= 24.00 and size_R <= 18.00:
      ##if 18x24 or smaller is selected, allow user to select from 18x24 paper options
      filter_list = wide_f_paperB
      descript = str("bleed + less than 24x18")
    elif size_L <= 24.00 and size_R <= 36.00:
      ##if 24x36 or smaller is selected, allow user to select from 24x36 paper options
      filter_list = wide_f_paperC
      descript = str("bleed + less than 24x36")
    elif size_L <= 36.00 and size_R <= 24.00:
      ##if 24x36 or smaller is selected, allow user to select from 24x36 paper options
      filter_list = wide_f_paperC
      descript = str("bleed + less than 36x24")
    elif size_L <= 24.00 and size_R <= 42.00:
      ##if 24x42 or smaller is selected, allow user to select from 24x42 paper options
      filter_list = wide_f_paperD
      descript = str("bleed + less than 24x42")
    elif size_L <= 42.00 and size_R <= 24.00:
      ##if 24x42 or smaller is selected, allow user to select from 24x42 paper options
      filter_list = wide_f_paperD
      descript = str("bleed + less than 42x24")
    elif size_L <= 30.00 and size_R <= 42.00:
      ##if 30x42 or smaller is selected, allow user to select from 30x42 paper options
      filter_list = wide_f_paperE
      descript = str("bleed + less than 30x42")
    elif size_L <= 42.00 and size_R <= 30.00:
      ##if 30x42 or smaller is selected, allow user to select from 30x42 paper options
      filter_list = wide_f_paperE
      descript = str("bleed + less than 42x30")
    elif size_L <= 36.00 and size_R <= 48.00:
      ##if 36x48 or smaller is selected, allow user to select from 36x48 paper options
      filter_list = wide_f_paperF
      descript = str("bleed + less than 36x48")
    elif size_L <= 48.00 and size_R <= 36.00:
      ##if 36x48 or smaller is selected, allow user to select from 36x48 paper options
      filter_list = wide_f_paperF
      descript = str("bleed + less than 48x36")
    else:
      ##catch all - shouldnt ever trigger
      filter_list = ''
      descript = str("CATCHALL WITH BLEEDS")

###############      
##IF NO BLEEDS
##############
  if bleeds == 'no':
    if size_L < 11.00 and size_R < 8.50:
      ##if smaller than 8.5x11 is selected, allow user to select from 12x18 paper options
      filter_list = exc_paper
      descript = str("less than 11x8.5")
    elif size_L < 8.50 and size_R < 11.00:
      ##if smaller than 8.5x11 is selected, allow user to select from 12x18 paper options
      filter_list = exc_paper
      descript = str("less than 8.5x11")
    elif size_L == 8.50 and size_R == 11.00:
      ##if 8.5x11 (EXACTLY) is selected, allow user to select from 11x17 paper options
      filter_list = tab_paper
      descript = str("exact 8.5x11")
    elif size_L == 11.00 and size_R == 11.00:
      ##if 8.5x11 (EXACTLY) is selected, allow user to select from 11x17 paper options
      filter_list = tab_paper
      descript = str("exact 11x8.5")      
    elif size_L == 8.50 and size_R == 14.00:
      ##if 8.5x14 (EXACTLY) is selected, allow user to select from 8.5x14 paper options
      filter_list = lgl_paper + str(" ") + tab_paper
      descript = str("exact 8.5x14")
    elif size_L == 14.00 and size_R == 8.50:
      ##if 8.5x14 (EXACTLY) is selected, allow user to select from 8.5x14 paper options
      filter_list = lgl_paper + str(" ") + tab_paper
      descript = str("exact 14x8.5")
    elif size_L <= 11.0 and size_R <= 17.0:
      ##if 11x17 or smaller is selected, allow user to select from 11x17 paper options
      filter_list = tab_paper
      descript = str("less than or equal to 11x17")
    elif size_L <= 17.0 and size_R <= 11.0:
      ##if 11x17 or smaller is selected, allow user to select from 11x17 paper options
      filter_list = tab_paper
      descript = str("less than or equal to 17x11")
    elif size_L <= 12.0 and size_R <= 18.0:
      ##if 12x18 or smaller is selected, allow user to select from 12x18 paper options
      filter_list = exc_paper
      descript = str("less than or equal to 12x18")
    elif size_L <= 18.0 and size_R <= 12.0:
      ##if 12x18 or smaller is selected, allow user to select from 12x18 paper options
      filter_list = exc_paper
      descript = str("less than or equal to 18x12")
    elif size_L <= 13.0 and size_R <= 19.0:
      ##if 13x19 or smaller is selected, allow user to select from 13x19 paper options
      filter_list = exc_plus_paper
      descript = str("less than or equal to 13x19")
    elif size_L <= 19.0 and size_R <= 13.0:
      ##if 13x19 or smaller is selected, allow user to select from 13x19 paper options
      filter_list = exc_plus_paper
      descript = str("less than or equal to 19x13")
    elif size_L <= 15.0 and size_R <= 21.0:
      ##if 15x21 or smaller is selected, allow user to select from 15x21 paper options
      filter_list = wide_f_paperA
      descript = str("less than or equal to 15x21")
    elif size_L <= 21.0 and size_R <= 15.0:
      ##if 15x21 or smaller is selected, allow user to select from 15x21 paper options
      filter_list = wide_f_paperA
      descript = str("less than or equal to 21x15")
    elif size_L <= 18.0 and size_R <= 24.0:
      ##if 18x24 or smaller is selected, allow user to select from 18x24 paper options
      filter_list = wide_f_paperB
      descript = str("less than or equal to 18x24")
    elif size_L <= 24.0 and size_R <= 18.0:
      ##if 18x24 or smaller is selected, allow user to select from 18x24 paper options
      filter_list = wide_f_paperB
      descript = str("less than or equal to 24x18")
    elif size_L <= 24.0 and size_R <= 36.0:
      ##if 24x36 or smaller is selected, allow user to select from 24x36 paper options
      filter_list = wide_f_paperC
      descript = str("less than or equal to 24x36")
    elif size_L <= 36.0 and size_R <= 24.0:
      ##if 24x36 or smaller is selected, allow user to select from 24x36 paper options
      filter_list = wide_f_paperC
      descript = str("less than or equal to 36x24")
    elif size_L <= 24.0 and size_R <= 42.0:
      ##if 24x42 or smaller is selected, allow user to select from 24x42 paper options
      filter_list = wide_f_paperD
      descript = str("less than or equal to 24x42")
    elif size_L <= 42.0 and size_R <= 24.0:
      ##if 24x42 or smaller is selected, allow user to select from 24x42 paper options
      filter_list = wide_f_paperD
      descript = str("less than or equal to 42x24")
    elif size_L <= 30.0 and size_R <= 42.0:
      ##if 30x42 or smaller is selected, allow user to select from 30x42 paper options
      filter_list = wide_f_paperE
      descript = str("less than or equal to 30x42")
    elif size_L <= 42.0 and size_R <= 30.0:
      ##if 30x42 or smaller is selected, allow user to select from 30x42 paper options
      filter_list = wide_f_paperE
      descript = str("less than or equal to 42x30")
    elif size_L <= 36.0 and size_R <= 48.0:
      ##if 36x48 or smaller is selected, allow user to select from 36x48 paper options
      filter_list = wide_f_paperF
      descript = str("less than or equal to 36x48")
    elif size_L <= 48.0 and size_R <= 36.0:
      ##if 36x48 or smaller is selected, allow user to select from 36x48 paper options
      filter_list = wide_f_paperF
      descript = str("less than or equal to 48x36")
    else:
      ##catch all - shouldnt ever trigger
      filter_list = ''
      descript = str("CATCHALL")

  allow_sizes = str('what_is_thur_project3488 == ') + pageDNA_size
  paper_limit.append(allow_sizes + str(' allow ') + filter_list)
  conflicts['what_kind_d_you_like3565'] = paper_limit

##final output for line description and conflict save
save['*conflicts'] = conflicts
desc = str('(Size) ') + str(size) + str(" (DESC) ") + descript