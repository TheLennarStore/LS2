#############
##VARIABLES##
ink = lookup('is_your_prack__white4030')
up = env['snap']['layout']['what_kind_d_you_like3565']['up']
press_sheets = press_sheets()
size_R = float(env['snap']['layout']['what_kind_d_you_like3565']['fin_width'])
size_L = float(env['snap']['layout']['what_kind_d_you_like3565']['fin_height'])
size = str(size_R) + str("x") + str(size_L)
alt_size = str(size_L) + str("x") + str(size_R)
paper = lookup('what_kind_d_you_like3565')
to_display = ''

#################################
##Finishing PC key=>value array##

##FIN1
pc_array_fin1 = {"no_shrink_wrapping":"No Shrink Wrap", "corner_staple_sf":"_3096", "saddle_sti_staple_sf2508":"_3097", "_516_comb_binding_sf":"_3069", "_38_comb_binding_sf":"_3068", "_58_comb_binding_sf":"_3070", "_14_comb_binding_sf":"_3065", "_34_comb_binding_sf":"_3067", "_1_comb_binding_sf":"_3062", "_1_12_combbinding_sf2021":"_3063", "_2_comb_binding_sf":"_3066", "_8mm_blackil_bind_sf2297":"_3162", "_8mm_whiteil_bind_sf2333":"_3170", "_10mm_blacil_bind_sf2338":"_3163", "_11mm_whitil_bind_sf2375":"_3167", "_12mm_whitil_bind_sf2376":"_3171", "_13mm_whitil_bind_sf2377":"_3169", "_14mm_whitil_bind_sf2378":"_3168", "_14mm_blacil_bind_sf2342":"_3164", "_18mm_blacil_bind_sf2346":"_3165", "_22mm_blacil_bind_sf2341":"_3166", "small_fastbinding_sf2682":"_3077", "medium_fasbinding_sf2786":"_3075", "large_fastbinding_sf2668":"_3079", "insert_int_binder_sf3195":"_3033", "insert_int_binder_sf3098":"_3029", "insert_int_binder_sf3339":"_3031", "insert_int_binder_sf3099":"_3035", "insert_int_binder_sf3100":"_3037", "insert_int_binder_sf3101":"_3038", "insert_int_binder_sf3102":"_3039", "binder_clier_clip_sf3010":"_3117_3118_3119_3115", "chicago_screw_sf":"_4081_4082_4083_4084_4085_4086_4087", "staple__leve_flat_wf2317":"_3100", "staple_roler_band_wf2996":"_3100_3116", "chicago_scve_flat_wf3029":"_4081_4082_4083_4084_4085_4086_4087", "chicago_scer_band_wf3708":"_4081_4082_4083_4084_4085_4086_4087_3116", "magnet_back_uv":"_4072", "pin_back_uv":"_4073"}

##FIN2
pc_array_fin2 = {"machine_cut_sf":"_3124", "cut_to_blecorners_uv3307":"_3123_4079", "cut_to_bleed_sf":"_3125", "cut_to_blee__fold_sf2978":"_3125_3095", "cut_to_bled__fold_sf2299":"_3125_3088", "hand_cut_sf":"_3123", "machine_fold_only_sf":"_3088", "hand_fold_only_sf":"_3087", "fold_and_ivelopes_sf3581":"_3089", "score__fold_only_sf":"_3095", "perforation_sf":"_3122", "round_corners_sf":"_4079", "cut_to_bleed_wf":"_3123", "hand_cut_wf":"_3123", "round_corners_uv":"_4079", "cut_to_bleed_uv":"_3123", "bend_plastic_uv":"_4308"}

##FIN3
pc_array_fin3 = {"lamination_all":"_4014", "white_ink_uv":"_4401", "clear_ink_uv":"_4401", "laminationamcore_all3686":"_4014_4009", "laminationrboard_all3903":"_QUOTE", "mounting_only_all":"_4009", "contour_cut_graphtec":"_4700"}

##Bind
pc_array_bind = {"clear_ltr_k_ltr_back3261":"_3058_3059", "clear_ltr__ltr_cover3413":"_3058", "clear_ltr__cardstock3854":"_3058_2034", "printed_lt_cardstock4690":"_1056_2028", "clear_lgl_k_lgl_back3223":"_3060_3061", "clear_lgl_r_lgl_back3233":"_3060", "clear_11x111x17_back3229":"_3055_3056", "chipboard_back":"_3110"}

##MISC
pc_array_misc = {"_5in_easel_all":"_3130", "_7in_easel_all":"_3131", "_8in_easel_all":"_3133", "_9in_easel_all":"_3132", "_12in_easel_all":"_3129", "grommets_wf":"_3016", "mailing_seals_sf":"_3023", "_12_velcro_dots_all":"_4078", "htv_cut__weed_ds":"_4952"}

##PACK
pc_array_pack = {"no_shrink_wrapping":"None", "any_amount":"Any Amount", "shrink_wraackages_252934":"Pack of 25 PC:5018", "shrink_wraackages_502932":"Pack of 50 PC:5018", "shrink_wraackages_752939":"Pack of 75 PC:5018", "shrink_wrackages_1002976":"Pack of 100 PC:5018", "shrink_wrackages_1252983":"Pack of 125 PC:5018", "shrink_wrackages_1502981":"Pack of 150 PC:5018", "shrink_wrackages_1752988":"Pack of 175 PC:5018", "shrink_wrackages_2002977":"Pack of 200", "shrink_wrackages_2252984":"Pack of 225", "shrink_wrackages_2502982":"Pack of 250", "shrink_wrackages_2752989":"Pack of 275", "shrink_wrackages_3002978":"Pack of 300", "shrink_wrackages_4002979":"Pack of 400", "shrink_wrackages_5002980":"Pack of 500"}

##SETUP
pc_array_setup = {"mounting_setup":"_4053", "general_setup":"_4054", "padding_setup":"_4055", "tab_setup":"_4056", "stamp_setup":"_4064"}

##Build Finishing Options 1
fin1 = lookup('finishing_ns_per_set2764')
if fin1 == 'none' or fin1 == 'other' or fin1 == '':
  fin1_out = ''
else:
  fin1_in = pc_array_fin1[str(fin1)]
  fin1_out = fin1_in

##Build Finishing Options 2
fin2 = lookup('finishing__per_sheet2969')
if fin2 == 'none' or fin2 == 'other' or fin2 == '':
  fin2_out = ''
else:
  fin2_in = pc_array_fin2[str(fin2)]
  fin2_out = fin2_in

##Build Finishing Options 3
fin3 = lookup('finishing_s_per_sqft2878')
if fin3 == 'none' or fin3 == 'other' or fin3 == '':
  fin3_out = ''
else:
  fin3_in = pc_array_fin3[str(fin3)]
  fin3_out = fin3_in

##Build Finishing Options Binding
binding = lookup('binding_covers')
if binding == 'none' or binding == 'other' or binding == '':
  binding_out = ''
else:
  binding_in = pc_array_bind[str(binding)]
  binding_out = binding_in

##Build Finishing Options MISC
misc = lookup('misc_options')
if misc == 'none' or misc == 'other' or misc == '':
  misc_out = ''
else:
  misc_in = pc_array_misc[str(misc)]
  misc_out = misc_in

##Build Finishing Options Pack
pack = lookup('packaging')
if pack == 'none' or pack == '':
  pack_out = ''
else:
  pack_in = pc_array_pack[str(pack)]
  pack_out = 'Pack:(' + pack_in + ')'

##Build Finishing Options SETUP
setup = lookup('setups')
if setup == 'none' or setup =='':
  setup_out = ''
else:
  setup_in = pc_array_setup[str(setup)]
  setup_out = 'Setup:(' + setup_in + ')'

##########################
##Build 1st part of DESC##
oneSideBuild = str('Print ') + str(press_sheets) + str(' sheets, ') + str(alt_size) + str(' ') + str(up) + str('up, 1-sided, on ') + str(paper) + str('. Then, finish ')
twoSideBuild = str('Print ') + str(press_sheets) + str(' sheets, ') + str(alt_size) + str(' ') + str(up) + str('up, 2-sided, on ') + str(paper) + str('. Then, finish ')

if size <= '13x19' or alt_size <= '19x13':
  if ink == '4/0' or ink == '1/0':
    to_display = oneSideBuild
  elif ink == '4/4' or ink == '1/1':
    to_display = twoSideBuild
elif size > '13x19' or alt_size > '13x19':
  to_display = oneSideBuild

#############################
##Build second part of DESC##
fin_to_display = str('(') + str(fin1_out) + str(fin2_out) + str(fin3_out) + str(binding_out) + str(misc_out) + str(') ') + str(setup_out) + str(" ") + str(pack_out)

########################
##Concat parts of DESC##
to_display_comp = to_display + fin_to_display

###########
##DISPLAY##
env['finishing'] = to_display_comp