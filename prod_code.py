###############################
##MUST CHANGE THIS VARIABLE##

########################################################################################
##  small format = sf    large format = wf    engraving = en    uv printing = uv    ####
##  envelope = env       dyesub = ds          vinyl = vin       digital = dig       ####
##  inventory = inven    outsourced = out                                           ####
########################################################################################

type = 'sf' ##<-- change this##

##########################
#####OTHER VARIABLES######
size_R = float(env['snap']['layout']['what_kind_d_you_like3565']['fin_width'])
size_L = float(env['snap']['layout']['what_kind_d_you_like3565']['fin_height'])
size = str(size_L) + str("x") + str(size_R)
paper = lookup('paper')
ink = lookup('ink')
bleed = lookup('does_your_ave_bleeds3135')
fin1 = lookup('finishing_ns_per_set2764')
fin2 = lookup('finishing__per_sheet2969')
fin3 = lookup('finishing_s_per_sqft2878')
bind = lookup('binding_covers')
misc = lookup('misc_options')

###############
##PAPER ARRAY##
doorhanger = ['2054','2107']
sticker = ['2171','2165','2167','2169','2170','2171','2173','2174','2175']
sf_plain = ['2004','2005','2008','2009','2014','2015','2016','2017','2018','2019','2020','2023','2024','2025','2026','2028','2029','2032','2033','2034','2036','2037','2038','2045','2046','2048','2049','2050','2051','2052','2055','2056','2057','2058','2059','2060','2062','2105','2414']
wf_plain = ['2300','2301','2302','2303','2304']
poly = ['2070','2071']
tabs = ['2108','2111']
wf_spec = ['2127','2128','2129','2130','2133','2400','2401','2402','2403','2404','2405','2406','2407','2408','2409','2410','2411','2412','2413']
NCR = ['2141','2142','2144','2145']
stamp = ['4100','4101','4102','4104','4105','4106','4108','4109','4110','4112','4113','4114','4116','4117','4118','4120','4121','4122','4124','4125','4126','4128','4129','4130','4132','4133','4134','4136','4137','4138','4140','4141','4142']
vinyl = ['4701','4702','4703','4704','4705','4706','4707','4708','4709','4710','4711','4712','4713','4714','4715']
htv = ['4750','4751','4752','4753','4754','4755','4756']
bindings = ['_516_comb_binding_sf','_38_comb_binding_sf','_58_comb_binding_sf','_14_comb_binding_sf','_34_comb_binding_sf','_1_comb_binding_sf','_1_12_combbinding_sf2021','_2_comb_binding_sf','_8mm_blackil_bind_sf2297','_8mm_whiteil_bind_sf2333','_10mm_blacil_bind_sf2338','_11mm_whitil_bind_sf2375','_12mm_whitil_bind_sf2376','_13mm_whitil_bind_sf2377','_14mm_whitil_bind_sf2378','_14mm_blacil_bind_sf2342','_18mm_blacil_bind_sf2346','_22mm_blacil_bind_sf2341','small_fastbinding_sf2682','medium_fasbinding_sf2786','large_fastbinding_sf2668','insert_int_binder_sf3195','insert_int_binder_sf3098','insert_int_binder_sf3339','insert_int_binder_sf3099','insert_int_binder_sf3100','insert_int_binder_sf3101','insert_int_binder_sf3102','chicago_screw_sf']
digital = ['4147','4149','4150']

if type == 'sf':
    if paper in sticker:
        ##any sticker
        desc = '409 - stickers ' + size
        set_sku('409')

    if paper in poly:
        ##poly paper
        desc = '202 - poly paper ' + size
        set_sku('202')

    if paper in NCR:
        ##ncr paper
        desc = '307 - ncr ' + size
        set_sku('307')

    if paper in tabs:
        #tabs
        desc = '309 - tabs ' + size
        set_sku('309')

    if paper in doorhanger:
        if ink == '4/0' or ink == '1/0':
            ##1-sided doorhanger
            desc = '203 - 1sided doorhanger ' + size
            set_sku('203')
        elif ink == '4/4' or ink == '1/1':
            ##2-sided doorhanger
            desc = '204 - 2sided doorhanger ' + size
            set_sku('204')
        else:
            ##fail 8
            desc = 'fail 8 ' + size
            set_sku('200')

    if size_L <= 3.9 and size_R <= 3.4:
        if ink == '4/0' or ink == '1/0':
            ##1-sided biz card - HOR
            desc = '216 - 1sided biz cards - hor ' + size
            set_sku('216')
        elif ink == '4/4' or ink == '1/1':
            ##2-sided biz card - HOR
            desc = '210 - 2sided biz cards - hor ' + size
            set_sku('210')
        else:
            ##fail 1
            desc = 'fail 1 ' + size
            set_sku('200')

    elif size_L <= 3.4 and size_R <= 4.9:
        if ink == '4/0' or ink == '1/0':
            ##1-sided biz card - VERT
            desc = '217 - 1sided biz cards - vert ' + size
            set_sku('217')
        elif ink == '4/4' or ink == '1/1':
            ##2-sided biz card - VERT
            desc = '211 - 1sided biz cards - vert ' + size
            set_sku('211')
        else:
            ##fail 3
            desc = 'fail 3 ' + size
            set_sku('200')

    elif fin2 == 'machine_cut_sf':
        if ink == '4/0' or ink == '1/0':
            if bleed == 'no':
                ##1-sided flyer no bleeds
                desc = '300 - 1sided flyer no bleeds ' + size
                set_sku('300')
            elif bleed == 'yes':
                ##1-sided flyer WITH bleeds
                desc = '301 - 1sided flyer with bleeds ' + size
                set_sku('301')
            else:
                ##fail 5
                desc = 'fail 5 ' + size
                set_sku('200')
        elif ink == '4/4' or ink == '1/1':
            if bleed == 'no':
                ##2-sided flyer no bleeds
                desc = '302 - 2sided flyer no bleeds ' + size
                set_sku('302')
            elif bleed == 'yes':
                ##2-sided flyer WITH bleeds
                desc = '303 - 2sided flyer with bleeds ' + size
                set_sku('303')
            else:
                ##fail 6
                desc = 'fail 6 ' + size
                set_sku('200')

    elif paper in sf_plain: 
        if bind == 'chipboard_back':
            #notepad
            desc = '305 - notepads ' + size
            set_sku('305') 
        elif fin1 in bindings:
            #bound report
            desc = '405 - bound report ' + size
            set_sku('405')
        elif fin1 == 'corner_staple_sf':
            if ink == '4/0' or ink == '1/0':
                if bleed == 'no':
                    #1-sided multipage brochure no bleeds
                    desc = '104 - 1sided multipage brochure no bleeds ' + size
                    set_sku('104')
                elif bleed == 'yes':
                    #1-sided multipage brochure WITH bleeds
                    desc = '105 - 1sided multipage brochure with bleeds ' + size
                    set_sku('105')
            elif ink == '4/4' or ink == '1/1':
                if bleed == 'no':
                    #2-sided multipage brochure no bleeds
                    desc = '108 - 2sided multipage brochure no bleeds ' + size
                    set_sku('108')
                elif bleed == 'yes':
                    #2-sided multipage brochure WITH bleeds
                    desc = '109 - 2sided multipage brochure with bleeds ' + size
                    set_sku('109')

        elif fin1 == 'saddle_sti_staple_sf2508':
            if ink == '4/0' or ink == '1/0':
                #1-sided saddle stitched brohcure
                desc = '112 - 1sided saddle brochure ' + size
                set_sku('112')
            elif ink == '4/4' or ink == '1/1':
                #2-sided saddle stitched brohcure
                desc = '113 - 2sided saddle brochure ' + size
                set_sku('113')

        elif fin3 == 'laminationamcore_all3686' or fin3 == 'laminationrboard_all3903' or fin3 == 'mounting_only_all':
            #small format display
            desc = '605 - display ' + size
            set_sku('605')

        elif fin2 == 'cut_to_bled__fold_sf2299':
            #tri-fold brochure
            desc = '102 - trifold brochure ' + size
            set_sku('102')

        elif fin2 == 'fold_and_ivelopes_sf3581':
            #fold & insert into envelope
            desc = '501 - fold and insert ' + size
            set_sku('501')

        elif fin2 == 'cut_to_blee__fold_sf2978' or fin2 == 'score__fold_only_sf':
            if ink == '4/0' or ink == '1/0':
                ##1-sided foldover
                desc = '206 - 1sided foldover ' + size
                set_sku('206')
            elif ink == '4/4' or ink == '1/1':
                ##2-sided foldover
                desc = '207 - 2sided foldover ' + size
                set_sku('207')

        elif fin1 == 'none' and fin2 == 'none' and fin3 == 'none' and bind == 'none' and misc == 'none':
            ##All NONE SF
            desc = '200 - catch all 1 SF PLAIN ' + size
            set_sku('200') 
              
        else:
            ##catch all SF PLAIN
            desc = '200 - catch all 2 SF PLAIN ' + size
            set_sku('200')   

if type == 'wf':
    if paper in wf_plain:
        if ink == '4/0':
            if fin3 == 'laminationamcore_all3686' or fin3 == 'laminationrboard_all3903' or fin3 == 'mounting_only_all':
                ##display
                desc = '605 - display color ' + size
                set_sku('605')
            else:
                ##color construction plans
                desc = '601 - color construction plans ' + size
                set_sku('601')
        elif ink == '1/0':
            if fin3 == 'laminationamcore_all3686' or fin3 == 'laminationrboard_all3903' or fin3 == 'mounting_only_all':
                ##display
                desc = '605 - display BW ' + size
                set_sku('605')
            else:
                ##BW contruction plans
                desc = '600 - bw construction plans ' + size
                set_sku('600')
    elif paper in wf_spec:
        if fin3 == 'laminationamcore_all3686' or fin3 == 'laminationrboard_all3903' or fin3 == 'mounting_only_all':
            ##display
            desc = '605 - display ' + size
            set_sku('605')
        else:
            ##BW contruction plans
            desc = '608 - Poster ' + size
            set_sku('608')
    else:
        ##catch all WF
        desc = '200 - catch all WF ' + size
        set_sku('200') 

if type == 'en':
    if fin1 == 'magnet_back_uv' or fin1 == 'pin_back_uv':
        ##name badges
        desc = '510 - name badge ' + size
        set_sku('510') 
    else:
        ##engraving
        desc = '511 - engraving ' + size
        set_sku('511') 

if type == 'dig':
    if paper in digital:
        ##usbs
        desc = '506 - USB ' + size
        set_sku('506')
    else:
        ##scanning
        desc = '315 - scanning ' + size
        set_sku('315')

if type == 'uv':
    ##UV printing
    desc = '509 - UV printing ' + size
    set_sku('509')

if type == 'env':
    ##envelopes
    desc = '500 - envelopes ' + size
    set_sku('500')

if type == 'vin':
    if paper in vinyl:
        ##vinyl
        desc = '512 - vinyl ' + size
        set_sku('512')
    elif paper in htv:
        ##htv
        desc = '606 - apparel ' + size
        set_sku('606') 
    else:
        ##catch all VIN
        desc = '200 - catch all VIN ' + size
        set_sku('200')  

if type == 'inven':
    ##inventory item
    desc = '415 - inventory ' + size
    set_sku('415')

if type == 'ds':
    ##dye sub
    desc = '550 - dye sublimation ' + size
    set_sku('550')

if type == 'out':
    ##outsourced
    desc = '713 - outsourced ' + size
    set_sku('713')