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
#LTR
pc1040 = 0.12
pc1041 = 0.08
pc1042 = 0.07
pc1043 = 0.06
pc1044 = 0.056
pc1072 = 0.03
pc1073 = 0.02
pc1074 = 0.015
pc1075 = 0.01
ltr_pc_array = {
  'color':{
    4000:{'desc':'T5.4.1','pc':'1044','price':0.056},
    2000:{'desc':'T4.4.1','pc':'1043','price':0.06},
    1000:{'desc':'T3.4.1','pc':'1042','price':0.07},
    500: {'desc':'T2.4.1','pc':'1041','price':0.08},
    0:   {'desc':'T1.4.1','pc':'1040','price':0.12}
  },
  'bw':{
    2000:{'desc':'T4.4.1','pc':'1075','price':0.06},
    1000:{'desc':'T3.4.1','pc':'1074','price':0.07},
    500 :{'desc':'T2.4.1','pc':'1073','price':0.08},
    0:   {'desc':'T1.4.1','pc':'1072','price':0.12}
  }
}

#LGL
pc1048 = 0.13
pc1049 = 0.09
pc1050 = 0.08
pc1051 = 0.07
pc1052 = 0.065
pc1080 = 0.03
pc1081 = 0.02
pc1082 = 0.015
pc1083 = 0.01

#TAB
pc1056 = 0.14
pc1057 = 0.10
pc1058 = 0.09
pc1059 = 0.08
pc1060 = 0.075
pc1088 = 0.04
pc1089 = 0.02
pc1090 = 0.015
pc1091 = 0.01

#LDG
pc1064 = 0.14
pc1065 = 0.10
pc1066 = 0.09
pc1067 = 0.08
pc1068 = 0.075
pc1096 = 0.05
pc1097 = 0.03
pc1098 = 0.02
pc1099 = 0.01

#Wide Format
pc1030 = 0.70
pc1031 = 0.35
pc1020 = 0.13
pc1021 = 0.13

#UV
pc4400 = 0.10
pc4401 = 0.20

#DyeSub
pc4900 = 1.00
pc4901 = 0.75
pc4902 = 0.50

#Envelopes
pc4017 = 0.03
pc4018 = 0.02
pc4016 = 0.06
pc4024 = 0.03

sides = lookup('ink')
pages = float(pretty(lookup('num_pages')))
# modulus (%) is used to find if there's a blank page in the file by finding out if it's an odd number of pages), and to remove that from the click count
if sides == "4/4":
  if pages%2 != 0:
    clicks = float(press_sheets()*2-qty)
    cb = "color"
  else:
    clicks = float(press_sheets()*2)
    cb = "color"
elif sides == "1/1":
  if pages%2 != 0:
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

num_pages = float(pretty(lookup('num_pages')))

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
 

##########################
## Small Format OPTIONS ##       
if type == 'sf':
  if xp == 8.5 and yp == 11 or xp == 11 and yp == 8.5:  
    descript = ltr_pc_array[cb][active_teir]['desc']
    prod = ltr_pc_array[cb][active_teir]['pc']
    cost = ltr_pc_array[cb][active_teir]['price']

    desc = str('Color - 8.5x11 ') + str(clicks) + str(descript) + str(' PC:') + prod
    price = clicks * cost
      
  elif xp == 8.5 and yp == 14 or xp == 14 and yp == 8.5:  
    if clicks >= 4000:
      price = clicks * pc1052
      desc = str('Color - 8.5x14 ') + str(clicks) + str(' clicks T5.3.1')
    elif clicks >= 2000:
      price = clicks * pc1051
      desc = str('Color - 8.5x14 ') + str(clicks) + str(' clicks T4.3.1')    
    elif clicks >= 1000:
      price = clicks * pc1050
      desc = str('Color - 8.5x14 ') + str(clicks) + str(' clicks T3.3.1')
    elif clicks >= 500:
      price = clicks * pc1049 
      desc = str('Color - 8.5x14 ') + str(clicks) + str(' clicks T2.3.1')
    else:
      price = clicks * pc1048
      desc = str('Color - 8.5x14 ') + str(clicks) + str(' clicks T1.3.1')
  elif xp == 11 and yp == 17 or xp == 17 and yp == 11: 
    if clicks >= 4000:
      price = clicks * pc1060
      desc = str('Color - 11x17 ') + str(clicks) + str(' clicks T5.2.1')
    elif clicks >= 2000:
      price = clicks * pc1059
      desc = str('Color - 11x17 ') + str(clicks) + str(' clicks T4.2.1')    
    elif clicks >= 1000:
      price = clicks * pc1058
      desc = str('Color - 11x17 ') + str(clicks) + str(' clicks T3.2.1')
    elif clicks >= 500:
      price = clicks * pc1057 
      desc = str('Color - 11x17 ') + str(clicks) + str(' clicks T2.2.1')
    else:
      price = clicks * pc1056
      desc = str('Color - 11x17 ') + str(clicks) + str(' clicks T1.2.1')
  elif xp == 12 and yp == 18 or xp == 18 and yp == 12 or xp == 13 and yp == 19 or xp == 19 and yp == 13: 
    if clicks >= 4000:
      price = clicks * pc1068
      desc = str('Color - 12x18 ') + str(clicks) + str(' clicks T5.1.1')   
    elif clicks >= 2000:
      price = clicks * pc1067 
      desc = str('Color - 12x18 ') + str(clicks) + str(' clicks T4.1.1')
    elif clicks >= 1000:
      price = clicks * pc1066 
      desc = str('Color - 12x18 ') + str(clicks) + str(' clicks T3.1.1')
    elif clicks >= 500:
      price = clicks * pc1065
      desc = str('Color - 12x18 ') + str(clicks) + str(' clicks T2.1.1')
    else:
      price = clicks * pc1064
      desc = str('Color - 12x18 ') + str(clicks) + str(' clicks T1.1.1')
  elif xp > 13 and yp > 19 or xp > 19 and yp > 13:
    if qty > 1:
      sqft = ((px * py) / 144) * num_pages
      first_set = sqft * pc1030
      consec_set = ((qty - 1) * sqft) * pc1031
      price = first_set + consec_set
      desc = str('Color - WF ') + str(sqft) + str(' sqft T0.1.2 > 1 set')
    elif qty == 1:
      sqft = ((px * py) / 144) * num_pages
      price = sqft * pc1030
      desc = str('Color - WF ') + str(sqft) + str(' sqft T0.1.2 == 1 set')
elif cb == "bw":
  if xp == 8.5 and yp == 11 or xp == 11 and yp == 8.5:  
    if clicks >= 4000:
      price = clicks * pc1075
      desc = str('BW - 8.5x11 ') + str(clicks) + str(' clicks T5.4.2')
    elif clicks >= 2000:
      price = clicks * pc1075
      desc = str('BW- 8.5x11 ') + str(clicks) + str(' clicks T4.4.2')    
    elif clicks >= 1000:
      price = clicks * pc1074
      desc = str('BW - 8.5x11 ') + str(clicks) + str(' clicks T3.4.2')
    elif clicks >= 500:
      price = clicks * pc1073
      desc = str('BW - 8.5x11 ') + str(clicks) + str(' clicks T2.4.2')
    else:
      price = clicks * pc1072
      desc = str('BW - 8.5x11 ') + str(clicks) + str(' clicks T1.4.2')
  elif xp == 8.5 and yp == 14 or xp == 14 and yp == 8.5:  
    if clicks >= 4000:
      price = clicks * pc1083
      desc = str('BW - 8.5x14 ') + str(clicks) + str(' clicks T5.3.2')
    elif clicks >= 2000:
      price = clicks * pc1083
      desc = str('BW - 8.5x14 ') + str(clicks) + str(' clicks T4.3.2')    
    elif clicks >= 1000:
      price = clicks * pc1082
      desc = str('BW - 8.5x14 ') + str(clicks) + str(' clicks T3.3.2')
    elif clicks >= 500:
      price = clicks * pc1081
      desc = str('BW - 8.5x14 ') + str(clicks) + str(' clicks T2.3.2')
    else:
      price = clicks * pc1080
      desc = str('BW - 8.5x14 ') + str(clicks) + str(' clicks T1.3.2')
  elif xp == 11 and yp == 17 or xp == 17 and yp == 11: 
    if clicks >= 4000:
      price = clicks * pc1091
      desc = str('BW - 11x17 ') + str(clicks) + str(' clicks T5.2.2')
    elif clicks >= 2000:
      price = clicks * pc1091
      desc = str('BW - 11x17 ') + str(clicks) + str(' clicks T4.2.2')
    elif clicks >= 1000:
      price = clicks * pc1090
      desc = str('BW - 11x17 ') + str(clicks) + str(' clicks T3.2.2')
    elif clicks >= 500:
      price = clicks * pc1089
      desc = str('BW - 11x17 ') + str(clicks) + str(' clicks T2.2.2')
    else:
      price = clicks * pc1088
      desc = str('BW - 11x17 ') + str(clicks) + str(' clicks T1.2.2')
  elif xp == 12 and yp == 18 or xp == 18 and yp == 12 or xp == 13 and yp == 19 or xp == 19 and yp == 13: 
    if clicks >= 4000:
      price = clicks * pc1099
      desc = str('BW - 12x18 ') + str(clicks) + str(' clicks T5.1.2')   
    elif clicks >= 2000:
      price = clicks * pc1099
      desc = str('BW - 12x18 ') + str(clicks) + str(' clicks T4.1.2')
    elif clicks >= 1000:
      price = clicks * pc1098
      desc = str('BW - 12x18 ') + str(clicks) + str(' clicks T3.1.2')
    elif clicks >= 500:
      price = clicks * pc1097
      desc = str('BW - 12x18 ') + str(clicks) + str(' clicks T2.1.2')
    else:
      price = clicks * pc1096
      desc = str('BW - 12x18 ') + str(clicks) + str(' clicks T1.1.2')
  elif xp > 13 and yp > 19 or xp > 19 and yp > 13:
    if qty > 1:
      sqft = ((px * py) / 144) * num_pages
      first_set = sqft * pc1020
      consec_set = ((qty - 1) * sqft) * pc1021
      price = first_set + consec_set
      desc = str('BW - WF ') + str(sqft) + str(' sqft T0.1.2 > 1 set')
    elif qty == 1:
      sqft = ((px * py) / 144) * num_pages
      price = sqft * pc1020
      desc = str('BW - WF ') + str(sqft) + str(' sqft T0.1.2 == 1 set')
elif cb == "none":
  price = 0
  desc = str('none ')

#########################
## Wide Format OPTIONS ##       
elif type == "wf":
  if cb == "color":
    if qty > 1:
      sqft = ((px * py) / 144) * num_pages
      first_set = sqft * pc1030
      consec_set = ((qty - 1) * sqft) * pc1031
      price = first_set + consec_set
      desc = str('Color - WF ') + str(sqft) + str(' sqft T0.1.2 > 1 set')
    elif qty == 1:
      sqft = ((px * py) / 144) * num_pages
      price = sqft * pc1030
      desc = str('Color - WF ') + str(sqft) + str(' sqft T0.1.2 == 1 set')
  elif cb == "bw":
    if qty > 1:
      sqft = ((px * py) / 144) * num_pages
      first_set = sqft * pc1020
      consec_set = ((qty - 1) * sqft) * pc1021
      price = first_set + consec_set
      desc = str('BW - WF ') + str(sqft) + str(' sqft T0.1.2 > 1 set')
    elif qty == 1:
      sqft = ((px * py) / 144) * num_pages
      price = sqft * pc1020
      desc = str('BW - WF ') + str(sqft) + str(' sqft T0.1.2 == 1 set')
  elif cb == "none":
    price = 0
    desc = str('none ')

################
## UV OPTIONS ##    
elif type == "uv":
  if cb == "color" or cb == 'bw':
    if int(paper) >= 4200 and int(paper) <= 4225:
      if qty > 1:
        sqin = ((px * py) * num_pages)*qty
        price = qty * -0.50
        desc = str('UV BADGE ') + str(sqin) + str(' sqin ') + str(' &qty > ') + str(qty) + str(' ') + str(paper)
      else:
        sqin = ((px * py) * num_pages)*qty
        price = 0
        desc = str('UV BADGE ') + str(sqin) + str(' sqin ') + str(' &qty = ') + str(qty) + str(' ') + str(paper)
    else:
      sqin = ((px * py) * num_pages)*qty
      price = sqin * pc4400
      desc = str('UV ') + str(sqin) + str(' sqin ') + str(' ') + str(paper)
  elif cb == "none":
    price = 0
    desc = str('none ')

######################
## Envelope OPTIONS ##       
elif type == "env":
  if cb == "color":
    if qty > 500:
      price = qty * pc4024
      desc = str('Color Envelopes ') + str(qty) + str(' greater than 500')
    else:
      price = qty * pc4016
      desc = str('Color Envelopes ') + str(qty) + str(' less than 500')
  elif cb == "bw":
    if qty > 500:
      price = qty * pc4018
      desc = str('BW Envelopes ') + str(qty) + str(' greater than 500')
    else:
      price = qty * pc4017
      desc = str('BW Envelopes ') + str(qty) + str(' less than 500')
  elif cb == "none":
    price = 0
    desc = str('none ')

####################
## DyeSub OPTIONS ##       
elif type == "ds":
  if cb == "color" or cb == "bw":
    sqft = (((px * py) / 144) * num_pages)*qty
    if sqft < 72:
      price = sqft * pc4900
      desc = str('DyeSub ') + str(sqft) + str(' sqft 1-72sqft')
    elif sqft < 144:
      price = sqft * pc4901
      desc = str('DyeSub ') + str(sqft) + str(' sqft 73-144sqft')
    elif sqft < 216:
      price = sqft * pc4902
      desc = str('DyeSub ') + str(sqft) + str(' sqft 145-216sqft')
  elif cb == "none":
    price = 0
    desc = str('none ')

