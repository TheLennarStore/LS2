###############################
##MUST CHANGE THIS VARIABLE##

#############################################################################################
##  small format = sf     large format = wf      engraving = en      uv printing = uv    ####
##  envelope = env        dyesub = ds            vinyl = vin         digital = dig       ####
##  inventory = inven     outsourced = out                                               ####
#############################################################################################

type = 'sf' ##<-- change this##

##########################
#####OTHER VARIABLES######
##give the ink item the current value of "Is your project Color or Black & White?"
i =  lookup('is_your_prack__white4030')
env['ink'] = i
paper = lookup('what_kind_d_you_like3565')

##global variables
pc_array = {
  #LETTER
  'ltr':{
    'color':{
      4000:{'desc':'T1.5','pc':'1044','price':0.056},
      2000:{'desc':'T1.4','pc':'1043','price':0.060},
      1000:{'desc':'T1.3','pc':'1042','price':0.070},
      500: {'desc':'T1.2','pc':'1041','price':0.080},
      0:   {'desc':'T1.1','pc':'1040','price':0.120}
    },
    'bw':{
      2000:{'desc':'T2.4','pc':'1075','price':0.060},
      1000:{'desc':'T2.3','pc':'1074','price':0.070},
      500 :{'desc':'T2.2','pc':'1073','price':0.080},
      0:   {'desc':'T2.1','pc':'1072','price':0.120}
    },
    'none':{
      0:   {'desc':'catchall','pc':'','price':0.2}
    }
  },
  #LEGAL
  'lgl':{
    'color':{
      4000:{'desc':'T3.5','pc':'1052','price':0.065},
      2000:{'desc':'T3.4','pc':'1051','price':0.070},
      1000:{'desc':'T3.3','pc':'1050','price':0.080},
      500: {'desc':'T3.2','pc':'1049','price':0.090},
      0:   {'desc':'T3.1','pc':'1048','price':0.130}
    },
    'bw':{
      2000:{'desc':'T4.4','pc':'1075','price':0.010},
      1000:{'desc':'T4.3','pc':'1074','price':0.015},
      500 :{'desc':'T4.2','pc':'1073','price':0.020},
      0:   {'desc':'T4.1','pc':'1072','price':0.030}
    },
    'none':{
      0:   {'desc':'catchall','pc':'','price':0.2}
    }
  },
  #TABLOID
  'tab':{
    'color':{
      4000:{'desc':'T5.5','pc':'1060','price':0.075},
      2000:{'desc':'T5.4','pc':'1059','price':0.080},
      1000:{'desc':'T5.3','pc':'1058','price':0.090},
      500: {'desc':'T5.2','pc':'1057','price':0.100},
      0:   {'desc':'T5.1','pc':'1056','price':0.140}
    },
    'bw':{
      2000:{'desc':'T6.4','pc':'1091','price':0.010},
      1000:{'desc':'T6.3','pc':'1090','price':0.015},
      500 :{'desc':'T6.2','pc':'1089','price':0.020},
      0:   {'desc':'T6.1','pc':'1088','price':0.040}
    },
    'none':{
      0:   {'desc':'catchall','pc':'','price':0.2}
    }
  },
  #12x18 or 13x19
  'ex':{
    'color':{
      4000:{'desc':'T7.5','pc':'1068','price':0.075},
      2000:{'desc':'T7.4','pc':'1067','price':0.080},
      1000:{'desc':'T7.3','pc':'1066','price':0.090},
      500: {'desc':'T7.2','pc':'1065','price':0.100},
      0:   {'desc':'T7.1','pc':'1064','price':0.140}
    },
    'bw':{
      2000:{'desc':'T8.4','pc':'1099','price':0.010},
      1000:{'desc':'T8.3','pc':'1098','price':0.020},
      500 :{'desc':'T8.2','pc':'1097','price':0.030},
      0:   {'desc':'T8.1','pc':'1096','price':0.050}
    },
    'none':{
      0:   {'desc':'catchall','pc':'','price':0.2}
    }
  },
  #WIDE FORMAT
  'wf':{
    'color':{
      2: {'desc':'T9.2','pc':'1031','price':0.350},
      1: {'desc':'T9.1','pc':'1030','price':0.700}
    },
    'bw':{
      2 :{'desc':'T10.2','pc':'1021','price':0.130},
      1: {'desc':'T10.1','pc':'1020','price':0.130}
    },
    'none':{
      0:   {'desc':'catchall','pc':'','price':0.2}
    }
  },
  #UV
  'uv':{
    'color':{
      2: {'desc':'T11.2','pc':'4401','price':0.200},
      1: {'desc':'T11.1','pc':'4400','price':0.100}
    },
    'none':{
      0:   {'desc':'catchall','pc':'','price':0.2}
    }
  },
  #DYE SUB
  'ds':{
    'color':{
      3: {'desc':'T12.3','pc':'4902','price':1.000},
      2: {'desc':'T12.2','pc':'4901','price':0.750},
      1: {'desc':'T12.1','pc':'4900','price':0.500}
    },
    'none':{
      0:   {'desc':'catchall','pc':'','price':0.2}
    }
  },
  #ENVELOPES
  'env':{
    'color':{
      2: {'desc':'T13.2','pc':'4024','price':0.033},
      1: {'desc':'T13.1','pc':'4016','price':0.055}
    },
    'bw':{
      2 :{'desc':'T13.2','pc':'4018','price':0.019},
      1: {'desc':'T13.1','pc':'4017','price':0.030}
    },
    'none':{
      0:   {'desc':'catchall','pc':'','price':0.2}
    }
  }
}

clicks = 0
cost = 0
descript = ''
sides = lookup('ink')
num_pages = float(pretty(lookup('num_pages')))
# modulus (%) is used to find if there's a blank page in the file by finding out if it's an odd number of pages), and to remove that from the click count
if sides == "4/4":
  if num_pages%2 != 0:
    clicks = float(press_sheets()*2-qty)
    cb = "color"
  else:
    clicks = float(press_sheets()*2)
    cb = "color"
elif sides == "1/1":
  if num_pages%2 != 0:
    clicks = float(press_sheets()*2-qty)
    cb = "bw"
  else:
    clicks = float(press_sheets()*2)
    cb = "bw"
elif sides == "4/0":
  clicks = float(press_sheets())
  cb = "color"
elif sides == "1/0":
  clicks = float(press_sheets())
  cb = "bw"
elif sides == '0/0':
  clicks = float(press_sheets())
  cb = "none"

paper_size_x = env['snap']['paper']['what_kind_d_you_like3565']['width_inches']
paper_size_y = env['snap']['paper']['what_kind_d_you_like3565']['height_inches']
xp = paper_size_x
yp = paper_size_y

print_size =  lookup('size')
px = size_left(print_size)
py = size_right(print_size)

##########################
## Small Format OPTIONS ##       
if type == 'sf':
  ##Find pricing teir for arrays
  if cb == 'color':
    if clicks >= 4000:
      active_teir = 4000
    elif clicks >= 2000:
      active_teir = 2000
    elif clicks >= 1000:
      active_teir = 1000
    elif clicks >= 500:
      active_teir = 500
    else:
      active_teir = 0
  elif cb == 'bw':
    if clicks >= 2000:
      active_teir = 2000
    elif clicks >= 1000:
      active_teir = 1000
    elif clicks >= 500:
      active_teir = 500
    else:
      active_teir = 0
  elif cb == 'none':
    active_teir = 0

  ##BUILD COST AND DESCRIPTION    
  if xp == 8.5 and yp == 11 or xp == 11 and yp == 8.5:  
    descript = pc_array['ltr'][cb][active_teir]['desc']
    prod =     pc_array['ltr'][cb][active_teir]['pc']
    cost =     pc_array['ltr'][cb][active_teir]['price']
  elif xp == 8.5 and yp == 14 or xp == 14 and yp == 8.5:  
    descript = pc_array['lgl'][cb][active_teir]['desc']
    prod =     pc_array['lgl'][cb][active_teir]['pc']
    cost =     pc_array['lgl'][cb][active_teir]['price']
  elif xp == 11 and yp == 17 or xp == 17 and yp == 11: 
    descript = pc_array['tab'][cb][active_teir]['desc']
    prod =     pc_array['tab'][cb][active_teir]['pc']
    cost =     pc_array['tab'][cb][active_teir]['price']
  elif xp == 12 and yp == 18 or xp == 18 and yp == 12 or xp == 13 and yp == 19 or xp == 19 and yp == 13: 
    descript = pc_array['ex'][cb][active_teir]['desc']
    prod =     pc_array['ex'][cb][active_teir]['pc']
    cost =     pc_array['ex'][cb][active_teir]['price']
  elif xp > 13 and yp > 19 or xp > 19 and yp > 13:
      if qty > 1:
        sqft = ((px * py) / 144) * num_pages
        first_set = sqft * pc_array[type][cb][1]['price']
        consec_set = ((qty - 1) * sqft) * pc_array[type][cb][2]['price']
        cost = first_set + consec_set
        prod = pc_array[type][cb][2]['pc']
        descript = pc_array[type][cb][2]['desc'] + str(' sqft:' + sqft)
      elif qty == 1:
        sqft = ((px * py) / 144) * num_pages
        cost = sqft * pc_array[type][cb][1]['price']
        prod = pc_array[type][cb][1]['pc']
        descript = pc_array[type][cb][1]['desc'] + str(' sqft:' + sqft)
  else:
    cost = 0
    prod = '999'
    descript = "n/a"

#########################
## Wide Format OPTIONS ##       
elif type == "wf":
  if qty > 1:
    sqft = ((px * py) / 144) * num_pages
    first_set = sqft * pc_array[type][cb][1]['price']
    consec_set = ((qty - 1) * sqft) * pc_array[type][cb][2]['price']
    cost = first_set + consec_set
    prod = pc_array[type][cb][2]['pc']
    descript = pc_array[type][cb][2]['desc'] + str(' sqft:' + sqft)
  elif qty == 1:
    sqft = ((px * py) / 144) * num_pages
    cost = sqft * pc_array[type][cb][1]['price']
    prod = pc_array[type][cb][1]['pc']
    descript = pc_array[type][cb][1]['desc'] + str(' sqft:' + sqft)
  else:
    cost = 0
    prod = '999'
    descript = "n/a"

################
## UV OPTIONS ##    
elif type == "uv":
  if int(paper) >= 4200 and int(paper) <= 4225:
    if qty > 1:
      sqin = ((px * py) * num_pages)*qty
      cost = qty * -0.50
      prod = pc_array[type][cb][1]['pc']
      descript = pc_array[type][cb][1]['desc'] + str(' sqin:' + sqin)
    else:
      sqin = ((px * py) * num_pages)*qty
      cost = 0
      prod = pc_array[type][cb][1]['pc']
      descript = pc_array[type][cb][1]['desc'] + str(' sqin:' + sqin)
  else:
    sqin = ((px * py) * num_pages)*qty
    cost = sqin * pc_array[type][cb][1]['price']
    prod = pc_array[type][cb][1]['pc']
    descript = pc_array[type][cb][1]['desc'] + str(' sqin:' + sqin)

######################
## Envelope OPTIONS ##       
elif type == "env":
  if qty > 500:
    cost = qty * pc_array[type][cb][2]['price']
    prod = pc_array[type][cb][2]['pc']
    descript = pc_array[type][cb][2]['desc']
  else:
    cost = qty * pc_array[type][cb][1]['price']
    prod = pc_array[type][cb][1]['pc']
    descript = pc_array[type][cb][1]['desc']

####################
## DyeSub OPTIONS ##       
elif type == "ds":
  sqft = (((px * py) / 144) * num_pages)*qty
  if sqft < 216:
    cost = sqft * pc_array[type][cb][1]['price']
    prod = pc_array[type][cb][1]['pc']
    descript = pc_array[type][cb][1]['desc'] + str(" sqft:" + sqft)
  elif sqft < 144:
    cost = sqft * pc_array[type][cb][2]['price']
    prod = pc_array[type][cb][2]['pc']
    descript = pc_array[type][cb][2]['desc'] + str(" sqft:" + sqft)
  elif sqft < 72:
    cost = sqft * pc_array[type][cb][3]['price']
    prod = pc_array[type][cb][3]['pc']
    descript = pc_array[type][cb][3]['desc'] + str(" sqft:" + sqft)
  else:
    cost = 0
    prod = '999'
    descript = str('none ') + str(" sqft:" + sqft)

######################################
##FINAL PRINT OF DESCRIPTION AND PRICE
##THIS WORKS FOR EVERY PRODUCT TYPE ABOVE
desc = descript + str(' ') + prod
price = clicks * cost