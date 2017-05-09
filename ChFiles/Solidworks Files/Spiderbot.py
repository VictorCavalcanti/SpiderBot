# Chrono::Engine Python script from SolidWorks 
# Assembly: D:\Documents\ME - Graduate\Research\Projects\Project Chrono\SpiderBot\Solidworks Files\Parts\SpiderBot.SLDASM


import ChronoEngine_python_core as chrono 
import builtins 

shapes_dir = 'Spiderbot_shapes/' 

if hasattr(builtins, 'exported_system_relpath'): 
    shapes_dir = builtins.exported_system_relpath + shapes_dir 

exported_items = [] 

body_0= chrono.ChBodyAuxRef()
body_0.SetName('ground')
body_0.SetBodyFixed(True)
exported_items.append(body_0)

# Rigid body part
body_1= chrono.ChBodyAuxRef()
body_1.SetName('Spibot-LEG-2/Actuator_body-1')
body_1.SetPos(chrono.ChVectorD(-0.0134981735755341,0.209744176176648,-0.321113881458628))
body_1.SetRot(chrono.ChQuaternionD(-0.0283573737426925,0.999597848814421,1.53897167778103e-14,4.59720064649193e-13))
body_1.SetMass(0.00204159144576871)
body_1.SetInertiaXX(chrono.ChVectorD(8.08481090947278e-07,7.99172677775037e-07,8.83360200196947e-08))
body_1.SetInertiaXY(chrono.ChVectorD(3.77521823029834e-20,6.63388779166475e-19,-4.0494191917974e-08))
body_1.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-4.17192939730159e-18,5.58956732701871e-20,-0.0175577824053523),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_1_1_shape = chrono.ChObjShapeFile() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_1_1_shape.SetColor(chrono.ChColor(0.752941176470588,0.752941176470588,0.752941176470588)) 
body_1_1_shape.SetFading(0.75) 
body_1_1_level = chrono.ChAssetLevel() 
body_1_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_1_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_1_1_level.GetAssets().push_back(body_1_1_shape) 
body_1.GetAssets().push_back(body_1_1_level) 

# Auxiliary marker (coordinate system feature)
marker_1_1 =chrono.ChMarker()
marker_1_1.SetName('LL-Act-Base')
body_1.AddMarker(marker_1_1)
marker_1_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.01349817357558,0.206909579197526,-0.271194295523186),chrono.ChQuaternionD(-0.0283573737426925,0.999597848814421,1.53897167778103E-14,4.59720064649193E-13)))

# Auxiliary marker (coordinate system feature)
marker_1_2 =chrono.ChMarker()
marker_1_2.SetName('UL-Act-Base')
body_1.AddMarker(marker_1_2)
marker_1_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.0134981735755708,0.207476498593351,-0.281178212710274),chrono.ChQuaternionD(-0.0283573737426925,0.999597848814421,1.53897167778103E-14,4.59720064649193E-13)))

exported_items.append(body_1)



# Rigid body part
body_2= chrono.ChBodyAuxRef()
body_2.SetName('Spibot-LEG-2/limb_body_connector-1')
body_2.SetPos(chrono.ChVectorD(-0.00344817357569127,0.246232273060171,-0.150219756703369))
body_2.SetRot(chrono.ChQuaternionD(-0.498644653171685,0.501351682816852,0.498644653172147,-0.501351682816394))
body_2.SetMass(0.0319301494979552)
body_2.SetInertiaXX(chrono.ChVectorD(2.2110890182935e-06,4.65620459313165e-06,4.83154745183424e-06))
body_2.SetInertiaXY(chrono.ChVectorD(1.32385342629295e-08,1.31350727244605e-20,-1.62134993374948e-19))
body_2.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(0.01,0.00875766097763167,0.01),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_2_1_shape = chrono.ChObjShapeFile() 
body_2_1_shape.SetFilename(shapes_dir +'body_2_1.obj') 
body_2_1_level = chrono.ChAssetLevel() 
body_2_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_2_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_2_1_level.GetAssets().push_back(body_2_1_shape) 
body_2.GetAssets().push_back(body_2_1_level) 

# Auxiliary marker (coordinate system feature)
marker_2_1 =chrono.ChMarker()
marker_2_1.SetName('LB-UL-Ref')
body_2.AddMarker(marker_2_1)
marker_2_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.013448173575636,0.255907284132847,-0.210273017736761),chrono.ChQuaternionD(-0.498644653171687,0.501351682816392,0.501351682816854,0.498644653172145)))

# Auxiliary marker (coordinate system feature)
marker_2_2 =chrono.ChMarker()
marker_2_2.SetName('LB-B-Act-1')
body_2.AddMarker(marker_2_2)
marker_2_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.0134481735756913,0.256232126499981,-0.1502738970979),chrono.ChQuaternionD(0.705190031320552,-0.709018349357842,-3.26423880293882E-13,-3.245051289628E-13)))

exported_items.append(body_2)



# Rigid body part
body_3= chrono.ChBodyAuxRef()
body_3.SetName('Spibot-LEG-2/upper_limb-1')
body_3.SetPos(chrono.ChVectorD(-0.013448173174563,0.255365880246591,-0.3102715527097))
body_3.SetRot(chrono.ChQuaternionD(-0.498644652983999,0.501351683003525,0.49864465298446,-0.501351683003066))
body_3.SetMass(0.0769386604687246)
body_3.SetInertiaXX(chrono.ChVectorD(1.2136124631867e-05,0.000291222022968082,0.000279898353184369))
body_3.SetInertiaXY(chrono.ChVectorD(1.51104871131798e-06,1.20058215311278e-05,-6.50009530599816e-08))
body_3.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-0.00433891891647107,-0.0160004109829567,2.90281587993209e-19),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_3_1_shape = chrono.ChObjShapeFile() 
body_3_1_shape.SetFilename(shapes_dir +'body_3_1.obj') 
body_3_1_level = chrono.ChAssetLevel() 
body_3_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_3_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_3_1_level.GetAssets().push_back(body_3_1_shape) 
body_3.GetAssets().push_back(body_3_1_level) 

# Auxiliary marker (coordinate system feature)
marker_3_1 =chrono.ChMarker()
marker_3_1.SetName('UL-LL-Ref')
body_3.AddMarker(marker_3_1)
marker_3_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.013448173174471,0.254824476226496,-0.410270087107396),chrono.ChQuaternionD(0.707104190338155,-0.00191415928335635,-0.707104190338806,0.00191415928335825)))

# Auxiliary marker (coordinate system feature)
marker_3_2 =chrono.ChMarker()
marker_3_2.SetName('UL-LB-Ref')
body_3.AddMarker(marker_3_2)
marker_3_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.0134481731746551,0.255907284266685,-0.210273018312005),chrono.ChQuaternionD(0.707104190338155,-0.00191415928335635,-0.707104190338806,0.00191415928335825)))

exported_items.append(body_3)



# Rigid body part
body_4= chrono.ChBodyAuxRef()
body_4.SetName('Spibot-LEG-2/Actuator_body_b-2')
body_4.SetPos(chrono.ChVectorD(-0.013348173317604,0.221626236639373,-0.209519675072253))
body_4.SetRot(chrono.ChQuaternionD(-0.081543935138268,0.996669748031998,4.03452500214258e-14,4.58146595842959e-13))
body_4.SetMass(0.00204159144576871)
body_4.SetInertiaXX(chrono.ChVectorD(8.08481090947278e-07,7.82569697223514e-07,1.04939000571219e-07))
body_4.SetInertiaXY(chrono.ChVectorD(1.0813955768462e-19,6.55561698667547e-19,-1.14743748500376e-07))
body_4.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-4.17826009441434e-18,4.31502965232471e-20,-0.0175577824053523),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_4_1_shape = chrono.ChObjShapeFile() 
body_4_1_shape.SetFilename(shapes_dir +'body_4_1.obj') 
body_4_1_shape.SetColor(chrono.ChColor(0.843137254901961,0.843137254901961,0)) 
body_4_1_shape.SetFading(0) 
body_4_1_level = chrono.ChAssetLevel() 
body_4_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_4_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_4_1_level.GetAssets().push_back(body_4_1_shape) 
body_4.GetAssets().push_back(body_4_1_level) 

# Auxiliary marker (coordinate system feature)
marker_4_1 =chrono.ChMarker()
marker_4_1.SetName('LL-Act-Base')
body_4.AddMarker(marker_4_1)
marker_4_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.0133481733176493,0.213498999310594,-0.160184616408036),chrono.ChQuaternionD(-0.081543935138268,0.996669748031998,4.03452500214258E-14,4.58146595842959E-13)))

# Auxiliary marker (coordinate system feature)
marker_4_2 =chrono.ChMarker()
marker_4_2.SetName('UL-Act-Base')
body_4.AddMarker(marker_4_2)
marker_4_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.0133481733176402,0.21512444677635,-0.170051628140879),chrono.ChQuaternionD(-0.081543935138268,0.996669748031998,4.03452500214258E-14,4.58146595842959E-13)))

exported_items.append(body_4)



# Rigid body part
body_5= chrono.ChBodyAuxRef()
body_5.SetName('Spibot-LEG-2/Actuator_rod-1')
body_5.SetPos(chrono.ChVectorD(-0.0134981699231418,0.209404728839158,-0.315135897275055))
body_5.SetRot(chrono.ChQuaternionD(4.59761714762259e-13,-1.50565158732839e-14,0.999597848814421,0.0283573737426925))
body_5.SetMass(0.00140945245841084)
body_5.SetInertiaXX(chrono.ChVectorD(2.33089158373325e-06,2.31955788460439e-06,3.09621873811846e-08))
body_5.SetInertiaXY(chrono.ChVectorD(1.20503043514503e-19,-2.11968774765387e-18,1.30374302415202e-07))
body_5.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-1.65060230227876e-19,-2.34447212110501e-18,0.0545976735175364),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_5_1_shape = chrono.ChObjShapeFile() 
body_5_1_shape.SetFilename(shapes_dir +'body_5_1.obj') 
body_5_1_level = chrono.ChAssetLevel() 
body_5_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_5_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_5_1_level.GetAssets().push_back(body_5_1_shape) 
body_5.GetAssets().push_back(body_5_1_level) 

# Auxiliary marker (coordinate system feature)
marker_5_1 =chrono.ChMarker()
marker_5_1.SetName('UL-Act-Shaft')
body_5.AddMarker(marker_5_1)
marker_5_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.0134981699230907,0.212558217978432,-0.370671436628234),chrono.ChQuaternionD(0.999597848814421,0.0283573737426925,-4.59761714762259E-13,1.50565158732839E-14)))

# Auxiliary marker (coordinate system feature)
marker_5_2 =chrono.ChMarker()
marker_5_2.SetName('LL-Act-Shaft')
body_5.AddMarker(marker_5_2)
marker_5_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.013498169923054,0.214825895561729,-0.410607105376588),chrono.ChQuaternionD(0.999597848814421,0.0283573737426925,-4.59761714762259E-13,1.50565158732839E-14)))

exported_items.append(body_5)



# Rigid body part
body_6= chrono.ChBodyAuxRef()
body_6.SetName('Spibot-LEG-2/limb_body_connector_b-2')
body_6.SetPos(chrono.ChVectorD(-0.0134144336066082,0.215151516890677,-0.165051702008418))
body_6.SetRot(chrono.ChQuaternionD(-0.498644653171685,0.501351682816853,0.498644653172146,-0.501351682816394))
body_6.SetMass(0.0118048176111825)
body_6.SetInertiaXX(chrono.ChVectorD(8.17149703748216e-07,1.71878703364595e-06,1.78336759057685e-06))
body_6.SetInertiaXY(chrono.ChVectorD(3.54051977885007e-09,3.72601266914357e-21,-5.9895885504249e-20))
body_6.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-1.56699758850283e-18,-0.00621524420249397,8.63806342003782e-06),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_6_1_shape = chrono.ChObjShapeFile() 
body_6_1_shape.SetFilename(shapes_dir +'body_6_1.obj') 
body_6_1_level = chrono.ChAssetLevel() 
body_6_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_6_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_6_1_level.GetAssets().push_back(body_6_1_shape) 
body_6.GetAssets().push_back(body_6_1_level) 

# Auxiliary marker (coordinate system feature)
marker_6_1 =chrono.ChMarker()
marker_6_1.SetName('LB-B-Act-1')
body_6.AddMarker(marker_6_1)
marker_6_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.0134481735756913,0.21523272748246,-0.150051921848703),chrono.ChQuaternionD(0.705190031320551,-0.709018349357843,-3.26246764786397E-13,-3.24485449461969E-13)))

# Auxiliary marker (coordinate system feature)
marker_6_2 =chrono.ChMarker()
marker_6_2.SetName('LB-UL-Ref')
body_6.AddMarker(marker_6_2)
marker_6_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.0134144336066036,0.215124446693415,-0.170051628728323),chrono.ChQuaternionD(-0.498644653171685,0.501351682816853,0.498644653172146,-0.501351682816394)))

exported_items.append(body_6)



# Rigid body part
body_7= chrono.ChBodyAuxRef()
body_7.SetName('Spibot-LEG-2/lower_limb-1')
body_7.SetPos(chrono.ChVectorD(-0.0134481735754519,0.154824488045809,-0.410318805379456))
body_7.SetRot(chrono.ChQuaternionD(0.99999997033137,0.0002435924020288,-4.59520758755722e-13,2.31850409563674e-15))
body_7.SetMass(0.173763895224452)
body_7.SetInertiaXX(chrono.ChVectorD(0.000660134295478084,8.75830094770409e-06,0.000660653853923039))
body_7.SetInertiaXY(chrono.ChVectorD(-7.08403859531171e-11,-6.7019746955525e-12,3.12941540612304e-07))
body_7.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(4.14273289970014e-09,-0.0143933772184335,3.59893950746433e-07),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_7_1_shape = chrono.ChObjShapeFile() 
body_7_1_shape.SetFilename(shapes_dir +'body_7_1.obj') 
body_7_1_shape.SetColor(chrono.ChColor(0.898039215686275,0.917647058823529,0.929411764705882)) 
body_7_1_shape.SetFading(0.75) 
body_7_1_level = chrono.ChAssetLevel() 
body_7_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_7_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_7_1_level.GetAssets().push_back(body_7_1_shape) 
body_7.GetAssets().push_back(body_7_1_level) 

# Auxiliary marker (coordinate system feature)
marker_7_1 =chrono.ChMarker()
marker_7_1.SetName('LowerLimbCenterRef')
body_7.AddMarker(marker_7_1)
marker_7_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.0134481735754519,0.154824488045809,-0.410318805379456),chrono.ChQuaternionD(0.70710676020766,0.000172245839645015,0.000172245838995154,-0.707106760207657)))

# Auxiliary marker (coordinate system feature)
marker_7_2 =chrono.ChMarker()
marker_7_2.SetName('LL-UL-Ref')
body_7.AddMarker(marker_7_2)
marker_7_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.0134481735754524,0.254824476178357,-0.410270086900496),chrono.ChQuaternionD(0.70710676020766,0.000172245839645015,0.000172245838995154,-0.707106760207657)))

# Collision shapes 
body_7.GetCollisionModel().ClearModel()
body_7.GetCollisionModel().AddSphere(0.01, chrono.ChVectorD(3.46944695195361E-17,-0.1,0))
body_7.GetCollisionModel().BuildModel()
body_7.SetCollide(True)

exported_items.append(body_7)



# Rigid body part
body_8= chrono.ChBodyAuxRef()
body_8.SetName('Spibot-LEG-2/Actuator_rod_b-2')
body_8.SetPos(chrono.ChVectorD(-0.0133481733176137,0.219980714826898,-0.199530805316447))
body_8.SetRot(chrono.ChQuaternionD(-0.0815439351382682,0.996669748031998,4.01433497193341e-14,4.58104823366664e-13))
body_8.SetMass(0.00122087835937912)
body_8.SetInertiaXX(chrono.ChVectorD(7.21325661454779e-07,6.99059605707624e-07,4.17530544958075e-08))
body_8.SetInertiaXY(chrono.ChVectorD(1.04418984540569e-19,6.33464541481515e-19,-1.11302244677677e-07))
body_8.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-2.22314235000441e-19,1.10781155047926e-18,0.0317642663115355),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_8_1_shape = chrono.ChObjShapeFile() 
body_8_1_shape.SetFilename(shapes_dir +'body_8_1.obj') 
body_8_1_level = chrono.ChAssetLevel() 
body_8_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_8_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_8_1_level.GetAssets().push_back(body_8_1_shape) 
body_8.GetAssets().push_back(body_8_1_level) 

# Auxiliary marker (coordinate system feature)
marker_8_1 =chrono.ChMarker()
marker_8_1.SetName('UL-Act-Shaft')
body_8.AddMarker(marker_8_1)
marker_8_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.0133481733175633,0.229022266355166,-0.254416058080388),chrono.ChQuaternionD(-4.01433497193341E-14,-4.58104823366664E-13,-0.0815439351382682,0.996669748031998)))

# Auxiliary marker (coordinate system feature)
marker_8_2 =chrono.ChMarker()
marker_8_2.SetName('LL-Act-Shaft')
body_8.AddMarker(marker_8_2)
marker_8_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.013348173317527,0.235524056218189,-0.293884105011761),chrono.ChQuaternionD(-4.01433497193341E-14,-4.58104823366664E-13,-0.0815439351382682,0.996669748031998)))

exported_items.append(body_8)



# Rigid body part
body_9= chrono.ChBodyAuxRef()
body_9.SetName('Spibot-LEG-4/upper_limb-1')
body_9.SetPos(chrono.ChVectorD(0.076551817386744,0.257531495362178,0.0897225962001834))
body_9.SetRot(chrono.ChQuaternionD(0.501351681728308,0.498644654266139,0.501351681727849,0.4986446542666))
body_9.SetMass(0.0769386604687246)
body_9.SetInertiaXX(chrono.ChVectorD(1.21361246164097e-05,0.000291222022983539,0.000279898353184369))
body_9.SetInertiaXY(chrono.ChVectorD(-1.51104728386778e-06,-1.20058215314599e-05,-6.50008916533907e-08))
body_9.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-0.00433891891647107,-0.0160004109829567,2.90281587993209e-19),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_3_1_shape = chrono.ChObjShapeFile() 
body_3_1_shape.SetFilename(shapes_dir +'body_3_1.obj') 
body_3_1_level = chrono.ChAssetLevel() 
body_3_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_3_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_3_1_level.GetAssets().push_back(body_3_1_shape) 
body_9.GetAssets().push_back(body_3_1_level) 

# Auxiliary marker (coordinate system feature)
marker_9_1 =chrono.ChMarker()
marker_9_1.SetName('UL-LL-Ref')
body_9.AddMarker(marker_9_1)
marker_9_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(0.0765518173866519,0.258072898870807,0.189721130600648),chrono.ChQuaternionD(0.707104190343701,-0.00191415747503272,0.70710419034305,-0.00191415747503188)))

# Auxiliary marker (coordinate system feature)
marker_9_2 =chrono.ChMarker()
marker_9_2.SetName('UL-LB-Ref')
body_9.AddMarker(marker_9_2)
marker_9_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(0.0765518173868361,0.256990091853549,-0.010275938200281),chrono.ChQuaternionD(0.707104190343701,-0.00191415747503272,0.70710419034305,-0.00191415747503188)))

exported_items.append(body_9)



# Rigid body part
body_10= chrono.ChBodyAuxRef()
body_10.SetName('Spibot-LEG-4/Actuator_rod_b-2')
body_10.SetPos(chrono.ChVectorD(0.0764518176436045,0.2209493128239,-0.0206285113106875))
body_10.SetRot(chrono.ChQuaternionD(3.80233913542453e-14,-4.58147387748093e-13,0.0869387485397259,0.996213658811375))
body_10.SetMass(0.00122087835937912)
body_10.SetInertiaXX(chrono.ChVectorD(7.21325661454779e-07,6.96572338599981e-07,4.42403216034504e-08))
body_10.SetInertiaXY(chrono.ChVectorD(1.11169507882327e-19,6.3208704670633e-19,-1.18392990236298e-07))
body_10.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-2.22314235000441e-19,1.10781155047926e-18,0.0317642663115355),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_8_1_shape = chrono.ChObjShapeFile() 
body_8_1_shape.SetFilename(shapes_dir +'body_8_1.obj') 
body_8_1_level = chrono.ChAssetLevel() 
body_8_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_8_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_8_1_level.GetAssets().push_back(body_8_1_shape) 
body_10.GetAssets().push_back(body_8_1_level) 

# Auxiliary marker (coordinate system feature)
marker_10_1 =chrono.ChMarker()
marker_10_1.SetName('UL-Act-Shaft')
body_10.AddMarker(marker_10_1)
marker_10_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(0.0764518176435541,0.230584627350146,0.0341556226970735),chrono.ChQuaternionD(0.0869387485397259,0.996213658811375,-3.80177397651193E-14,4.58145077782547E-13)))

# Auxiliary marker (coordinate system feature)
marker_10_2 =chrono.ChMarker()
marker_10_2.SetName('LL-Act-Shaft')
body_10.AddMarker(marker_10_2)
marker_10_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(0.0764518176435179,0.237513392852165,0.0735509550172612),chrono.ChQuaternionD(0.0869387485397259,0.996213658811375,-3.80233913542453E-14,4.58147387748093E-13)))

exported_items.append(body_10)



# Rigid body part
body_11= chrono.ChBodyAuxRef()
body_11.SetName('Spibot-LEG-4/Actuator_body_b-2')
body_11.SetPos(chrono.ChVectorD(0.0764518176435959,0.222702896833669,-0.0106580447396816))
body_11.SetRot(chrono.ChQuaternionD(3.80249788701464e-14,-4.58228029233157e-13,0.0869387485397259,0.996213658811375))
body_11.SetMass(0.00204159144576871)
body_11.SetInertiaXX(chrono.ChVectorD(8.08481090947278e-07,7.80005522958393e-07,1.07503174836339e-07))
body_11.SetInertiaXY(chrono.ChVectorD(1.15024945544434e-19,6.54163902908454e-19,-1.22053742359123e-07))
body_11.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-4.17826009441434e-18,4.31502965232471e-20,-0.0175577824053523),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_4_1_shape = chrono.ChObjShapeFile() 
body_4_1_shape.SetFilename(shapes_dir +'body_4_1.obj') 
body_4_1_shape.SetColor(chrono.ChColor(0.843137254901961,0.843137254901961,0)) 
body_4_1_shape.SetFading(0) 
body_4_1_level = chrono.ChAssetLevel() 
body_4_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_4_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_4_1_level.GetAssets().push_back(body_4_1_shape) 
body_11.GetAssets().push_back(body_4_1_level) 

# Auxiliary marker (coordinate system feature)
marker_11_1 =chrono.ChMarker()
marker_11_1.SetName('LL-Act-Base')
body_11.AddMarker(marker_11_1)
marker_11_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(0.0764518176436412,0.214041939956145,-0.0599022101399162),chrono.ChQuaternionD(3.80249788701464E-14,-4.58228029233157E-13,0.0869387485397259,0.996213658811375)))

# Auxiliary marker (coordinate system feature)
marker_11_2 =chrono.ChMarker()
marker_11_2.SetName('UL-Act-Base')
body_11.AddMarker(marker_11_2)
marker_11_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(0.0764518176436321,0.21577413133165,-0.0500533770598693),chrono.ChQuaternionD(3.80249788701464E-14,-4.58228029233157E-13,0.0869387485397259,0.996213658811375)))

exported_items.append(body_11)



# Rigid body part
body_12= chrono.ChBodyAuxRef()
body_12.SetName('Spibot-LEG-4/lower_limb-1')
body_12.SetPos(chrono.ChVectorD(0.076551815571355,0.15807291015964,0.189672421706701))
body_12.SetRot(chrono.ChQuaternionD(4.5959071246098e-13,-1.93595145660255e-15,0.999999970344074,0.000243540244961039))
body_12.SetMass(0.173763895224452)
body_12.SetInertiaXX(chrono.ChVectorD(0.000660134295478084,8.75830088242273e-06,0.00066065385398832))
body_12.SetInertiaXY(chrono.ChVectorD(7.08403847637235e-11,-6.70198212327745e-12,-3.1287353868923e-07))
body_12.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(4.14273289970014e-09,-0.0143933772184335,3.59893950746433e-07),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_7_1_shape = chrono.ChObjShapeFile() 
body_7_1_shape.SetFilename(shapes_dir +'body_7_1.obj') 
body_7_1_shape.SetColor(chrono.ChColor(0.898039215686275,0.917647058823529,0.929411764705882)) 
body_7_1_shape.SetFading(0.75) 
body_7_1_level = chrono.ChAssetLevel() 
body_7_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_7_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_7_1_level.GetAssets().push_back(body_7_1_shape) 
body_12.GetAssets().push_back(body_7_1_level) 

# Auxiliary marker (coordinate system feature)
marker_12_1 =chrono.ChMarker()
marker_12_1.SetName('LowerLimbCenterRef')
body_12.AddMarker(marker_12_1)
marker_12_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(0.076551815571355,0.15807291015964,0.189672421706701),chrono.ChQuaternionD(-0.000172208959028748,0.707106760216643,-0.70710676021664,-0.000172208958378799)))

# Auxiliary marker (coordinate system feature)
marker_12_2 =chrono.ChMarker()
marker_12_2.SetName('LL-UL-Ref')
body_12.AddMarker(marker_12_2)
marker_12_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(0.0765518155713546,0.25807289829727,0.189721129754248),chrono.ChQuaternionD(-0.000172208959028748,0.707106760216643,-0.70710676021664,-0.000172208958378799)))

# Collision shapes 
body_12.GetCollisionModel().ClearModel()
body_12.GetCollisionModel().AddSphere(0.01, chrono.ChVectorD(3.46944695195361E-17,-0.1,0))
body_12.GetCollisionModel().BuildModel()
body_12.SetCollide(True)

exported_items.append(body_12)



# Rigid body part
body_13= chrono.ChBodyAuxRef()
body_13.SetName('Spibot-LEG-4/Actuator_body-1')
body_13.SetPos(chrono.ChVectorD(0.076601817386734,0.212039035007263,0.101057655255187))
body_13.SetRot(chrono.ChQuaternionD(1.35802638905979e-14,-4.59423937714032e-13,0.0338606485052858,0.999426563826878))
body_13.SetMass(0.00204159144576871)
body_13.SetInertiaXX(chrono.ChVectorD(8.08481090947278e-07,7.98194720589383e-07,8.93139772053487e-08))
body_13.SetInertiaXY(chrono.ChVectorD(4.48668619957873e-20,6.62451066185714e-19,-4.83113961308396e-08))
body_13.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-4.17192939730159e-18,5.58956732701871e-20,-0.0175577824053523),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_1_1_shape = chrono.ChObjShapeFile() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_1_1_shape.SetColor(chrono.ChColor(0.752941176470588,0.752941176470588,0.752941176470588)) 
body_1_1_shape.SetFading(0.75) 
body_1_1_level = chrono.ChAssetLevel() 
body_1_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_1_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_1_1_level.GetAssets().push_back(body_1_1_shape) 
body_13.GetAssets().push_back(body_1_1_level) 

# Auxiliary marker (coordinate system feature)
marker_13_1 =chrono.ChMarker()
marker_13_1.SetName('LL-Act-Base')
body_13.AddMarker(marker_13_1)
marker_13_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(0.0766018173867799,0.208654911848804,0.0511723096069069),chrono.ChQuaternionD(1.35802638905979E-14,-4.59423937714032E-13,0.0338606485052858,0.999426563826878)))

# Auxiliary marker (coordinate system feature)
marker_13_2 =chrono.ChMarker()
marker_13_2.SetName('UL-Act-Base')
body_13.AddMarker(marker_13_2)
marker_13_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(0.0766018173867707,0.209331736480495,0.0611493787365629),chrono.ChQuaternionD(1.35802638905979E-14,-4.59423937714032E-13,0.0338606485052858,0.999426563826878)))

exported_items.append(body_13)



# Rigid body part
body_14= chrono.ChBodyAuxRef()
body_14.SetName('Spibot-LEG-4/Actuator_rod-1')
body_14.SetPos(chrono.ChVectorD(0.0766018173867374,0.21160187415052,0.0946134688525606))
body_14.SetRot(chrono.ChQuaternionD(0.999426563826878,-0.0338606485052858,-4.59410051963633e-13,-1.37052356441924e-14))
body_14.SetMass(0.00140945245841084)
body_14.SetInertiaXX(chrono.ChVectorD(2.33089158373325e-06,2.3164092729188e-06,3.41107990667777e-08))
body_14.SetInertiaXY(chrono.ChVectorD(1.43428421589602e-19,-2.11641247009043e-18,1.55542419071387e-07))
body_14.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-1.65060230227876e-19,-2.34447212110501e-18,0.0545976735175364),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_5_1_shape = chrono.ChObjShapeFile() 
body_5_1_shape.SetFilename(shapes_dir +'body_5_1.obj') 
body_5_1_level = chrono.ChAssetLevel() 
body_5_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_5_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_5_1_level.GetAssets().push_back(body_5_1_shape) 
body_14.GetAssets().push_back(body_5_1_level) 

# Auxiliary marker (coordinate system feature)
marker_14_1 =chrono.ChMarker()
marker_14_1.SetName('UL-Act-Shaft')
body_14.AddMarker(marker_14_1)
marker_14_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(0.0766018173866864,0.215366711164305,0.150110915886272),chrono.ChQuaternionD(4.59410051963633E-13,1.37052356441924E-14,0.999426563826878,-0.0338606485052858)))

# Auxiliary marker (coordinate system feature)
marker_14_2 =chrono.ChMarker()
marker_14_2.SetName('LL-Act-Shaft')
body_14.AddMarker(marker_14_2)
marker_14_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(0.0766018173866497,0.218074009691072,0.190019192404896),chrono.ChQuaternionD(4.59410051963633E-13,1.37052356441924E-14,0.999426563826878,-0.0338606485052858)))

exported_items.append(body_14)



# Rigid body part
body_15= chrono.ChBodyAuxRef()
body_15.SetName('Spibot-LEG-4/limb_body_connector_b-2')
body_15.SetPos(chrono.ChVectorD(0.0765180741340384,0.215747061798726,-0.0550533036406316))
body_15.SetRot(chrono.ChQuaternionD(0.501351682816852,0.498644653171686,0.501351682816393,0.498644653172147))
body_15.SetMass(0.0118048176111825)
body_15.SetInertiaXX(chrono.ChVectorD(8.17149703748215e-07,1.71878703364595e-06,1.78336759057685e-06))
body_15.SetInertiaXY(chrono.ChVectorD(-3.54051977884762e-09,-2.42696189821606e-21,-5.95282906074747e-20))
body_15.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-1.56699758850283e-18,-0.00621524420249397,8.63806342003782e-06),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_6_1_shape = chrono.ChObjShapeFile() 
body_6_1_shape.SetFilename(shapes_dir +'body_6_1.obj') 
body_6_1_level = chrono.ChAssetLevel() 
body_6_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_6_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_6_1_level.GetAssets().push_back(body_6_1_shape) 
body_15.GetAssets().push_back(body_6_1_level) 

# Auxiliary marker (coordinate system feature)
marker_15_1 =chrono.ChMarker()
marker_15_1.SetName('LB-B-Act-1')
body_15.AddMarker(marker_15_1)
marker_15_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(0.0765518141031215,0.215665851206943,-0.0700530838003467),chrono.ChQuaternionD(3.24935392160425E-13,-3.25933627507704E-13,0.709018349357842,0.705190031320552)))

# Auxiliary marker (coordinate system feature)
marker_15_2 =chrono.ChMarker()
marker_15_2.SetName('LB-UL-Ref')
body_15.AddMarker(marker_15_2)
marker_15_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(0.0765180741340338,0.215774131995988,-0.0500533769207266),chrono.ChQuaternionD(0.501351682816852,0.498644653171686,0.501351682816393,0.498644653172147)))

exported_items.append(body_15)



# Rigid body part
body_16= chrono.ChBodyAuxRef()
body_16.SetName('Spibot-LEG-4/limb_body_connector-1')
body_16.SetPos(chrono.ChVectorD(0.0665518176436503,0.246665396269831,-0.0702209193068116))
body_16.SetRot(chrono.ChQuaternionD(0.501351682816853,0.498644653171686,0.501351682816393,0.498644653172146))
body_16.SetMass(0.0319301494979552)
body_16.SetInertiaXX(chrono.ChVectorD(2.2110890182935e-06,4.65620459313165e-06,4.83154745183424e-06))
body_16.SetInertiaXY(chrono.ChVectorD(-1.32385342629295e-08,-9.5026827600349e-21,-1.61834070103109e-19))
body_16.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(0.01,0.00875766097763167,0.01),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_2_1_shape = chrono.ChObjShapeFile() 
body_2_1_shape.SetFilename(shapes_dir +'body_2_1.obj') 
body_2_1_level = chrono.ChAssetLevel() 
body_2_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_2_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_2_1_level.GetAssets().push_back(body_2_1_shape) 
body_16.GetAssets().push_back(body_2_1_level) 

# Auxiliary marker (coordinate system feature)
marker_16_1 =chrono.ChMarker()
marker_16_1.SetName('LB-UL-Ref')
body_16.AddMarker(marker_16_1)
marker_16_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(0.0765518176435951,0.256990092076775,-0.0102759390624645),chrono.ChQuaternionD(-0.498644653172146,0.501351682816853,-0.501351682816393,-0.498644653171686)))

# Auxiliary marker (coordinate system feature)
marker_16_2 =chrono.ChMarker()
marker_16_2.SetName('LB-B-Act-1')
body_16.AddMarker(marker_16_2)
marker_16_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(0.0765518176436503,0.256665249709641,-0.0702750597013248),chrono.ChQuaternionD(3.24808166086752E-13,-3.25865121160342E-13,0.709018349357842,0.705190031320552)))

exported_items.append(body_16)



# Rigid body part
body_17= chrono.ChBodyAuxRef()
body_17.SetName('Spibot-LEG-3/Actuator_rod-1')
body_17.SetPos(chrono.ChVectorD(0.0765018347301764,0.209404730850348,-0.315135888072107))
body_17.SetRot(chrono.ChQuaternionD(4.59969965356137e-13,-1.58964598210974e-14,0.999597848752379,0.0283573759296457))
body_17.SetMass(0.00140945245841084)
body_17.SetInertiaXX(chrono.ChVectorD(2.33089158373325e-06,2.31955788346344e-06,3.09621885221335e-08))
body_17.SetInertiaXY(chrono.ChVectorD(1.20579701266173e-19,-2.12041063784404e-18,1.30374312429332e-07))
body_17.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-1.65060230227876e-19,-2.34447212110501e-18,0.0545976735175364),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_5_1_shape = chrono.ChObjShapeFile() 
body_5_1_shape.SetFilename(shapes_dir +'body_5_1.obj') 
body_5_1_level = chrono.ChAssetLevel() 
body_5_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_5_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_5_1_level.GetAssets().push_back(body_5_1_shape) 
body_17.GetAssets().push_back(body_5_1_level) 

# Auxiliary marker (coordinate system feature)
marker_17_1 =chrono.ChMarker()
marker_17_1.SetName('UL-Act-Shaft')
body_17.AddMarker(marker_17_1)
marker_17_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(0.0765018347302275,0.212558220232626,-0.370671427411488),chrono.ChQuaternionD(0.999597848752379,0.0283573759296457,-4.59969965356137E-13,1.58964598210974E-14)))

# Auxiliary marker (coordinate system feature)
marker_17_2 =chrono.ChMarker()
marker_17_2.SetName('LL-Act-Shaft')
body_17.AddMarker(marker_17_2)
marker_17_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(0.0765018347302642,0.214825897990669,-0.410607096149918),chrono.ChQuaternionD(0.999597848752379,0.0283573759296457,-4.59969965356137E-13,1.58964598210974E-14)))

exported_items.append(body_17)



# Rigid body part
body_18= chrono.ChBodyAuxRef()
body_18.SetName('Spibot-LEG-3/limb_body_connector_b-2')
body_18.SetPos(chrono.ChVectorD(0.0765855443445832,0.215151512943282,-0.165051699190019))
body_18.SetRot(chrono.ChQuaternionD(-0.498644653171685,0.501351682816853,0.498644653172146,-0.501351682816394))
body_18.SetMass(0.0118048176111825)
body_18.SetInertiaXX(chrono.ChVectorD(8.17149703748215e-07,1.71878703364595e-06,1.78336759057685e-06))
body_18.SetInertiaXY(chrono.ChVectorD(3.54051977885004e-09,3.67074152283566e-21,-5.94431575686403e-20))
body_18.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-1.56699758850283e-18,-0.00621524420249397,8.63806342003782e-06),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_6_1_shape = chrono.ChObjShapeFile() 
body_6_1_shape.SetFilename(shapes_dir +'body_6_1.obj') 
body_6_1_level = chrono.ChAssetLevel() 
body_6_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_6_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_6_1_level.GetAssets().push_back(body_6_1_shape) 
body_18.GetAssets().push_back(body_6_1_level) 

# Auxiliary marker (coordinate system feature)
marker_18_1 =chrono.ChMarker()
marker_18_1.SetName('LB-B-Act-1')
body_18.AddMarker(marker_18_1)
marker_18_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(0.0765518043755001,0.215232723535066,-0.150051919030304),chrono.ChQuaternionD(0.705190031320551,-0.709018349357843,-3.26340060598146E-13,-3.24460560203928E-13)))

# Auxiliary marker (coordinate system feature)
marker_18_2 =chrono.ChMarker()
marker_18_2.SetName('LB-UL-Ref')
body_18.AddMarker(marker_18_2)
marker_18_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(0.0765855443445878,0.215124442746021,-0.170051625909924),chrono.ChQuaternionD(-0.498644653171685,0.501351682816853,0.498644653172146,-0.501351682816394)))

exported_items.append(body_18)



# Rigid body part
body_19= chrono.ChBodyAuxRef()
body_19.SetName('Spibot-LEG-3/Actuator_body-1')
body_19.SetPos(chrono.ChVectorD(0.0765018264244652,0.209744178470893,-0.321113870197228))
body_19.SetRot(chrono.ChQuaternionD(-0.0283573759296457,0.999597848752379,1.57368010543352e-14,4.60053265582274e-13))
body_19.SetMass(0.00204159144576871)
body_19.SetInertiaXX(chrono.ChVectorD(8.08481090947277e-07,7.99172677420659e-07,8.83360203740728e-08))
body_19.SetInertiaXY(chrono.ChVectorD(3.77990693772796e-20,6.63850735163815e-19,-4.04941950283579e-08))
body_19.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-4.17192939730159e-18,5.58956732701871e-20,-0.0175577824053523),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_1_1_shape = chrono.ChObjShapeFile() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_1_1_shape.SetColor(chrono.ChColor(0.752941176470588,0.752941176470588,0.752941176470588)) 
body_1_1_shape.SetFading(0.75) 
body_1_1_level = chrono.ChAssetLevel() 
body_1_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_1_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_1_1_level.GetAssets().push_back(body_1_1_shape) 
body_19.GetAssets().push_back(body_1_1_level) 

# Auxiliary marker (coordinate system feature)
marker_19_1 =chrono.ChMarker()
marker_19_1.SetName('LL-Act-Base')
body_19.AddMarker(marker_19_1)
marker_19_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(0.0765018264244193,0.206909581273339,-0.27119428427419),chrono.ChQuaternionD(-0.0283573759296457,0.999597848752379,1.57368010543352E-14,4.60053265582274E-13)))

# Auxiliary marker (coordinate system feature)
marker_19_2 =chrono.ChMarker()
marker_19_2.SetName('UL-Act-Base')
body_19.AddMarker(marker_19_2)
marker_19_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(0.0765018264244285,0.20747650071285,-0.281178201458797),chrono.ChQuaternionD(-0.0283573759296457,0.999597848752379,1.57368010543352E-14,4.60053265582274E-13)))

exported_items.append(body_19)



# Rigid body part
body_20= chrono.ChBodyAuxRef()
body_20.SetName('Spibot-LEG-3/Actuator_rod_b-2')
body_20.SetPos(chrono.ChVectorD(0.0766518264243531,0.219980714751991,-0.19953079563761))
body_20.SetRot(chrono.ChQuaternionD(-0.0815439352761142,0.99666974802072,4.03169574456196e-14,4.58565757739071e-13))
body_20.SetMass(0.00122087835937912)
body_20.SetInertiaXX(chrono.ChVectorD(7.21325661454779e-07,6.99059605646048e-07,4.17530545573828e-08))
body_20.SetInertiaXY(chrono.ChVectorD(1.04478078930547e-19,6.34081812753951e-19,-1.11302244859497e-07))
body_20.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-2.22314235000441e-19,1.10781155047926e-18,0.0317642663115355),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_8_1_shape = chrono.ChObjShapeFile() 
body_8_1_shape.SetFilename(shapes_dir +'body_8_1.obj') 
body_8_1_level = chrono.ChAssetLevel() 
body_8_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_8_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_8_1_level.GetAssets().push_back(body_8_1_shape) 
body_20.GetAssets().push_back(body_8_1_level) 

# Auxiliary marker (coordinate system feature)
marker_20_1 =chrono.ChMarker()
marker_20_1.SetName('UL-Act-Shaft')
body_20.AddMarker(marker_20_1)
marker_20_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(0.0766518264244036,0.229022266295441,-0.25441604839905),chrono.ChQuaternionD(-4.03169574456196E-14,-4.58565757739071E-13,-0.0815439352761142,0.99666974802072)))

# Auxiliary marker (coordinate system feature)
marker_20_2 =chrono.ChMarker()
marker_20_2.SetName('LL-Act-Shaft')
body_20.AddMarker(marker_20_2)
marker_20_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(0.0766518264244399,0.235524056169382,-0.293884095328625),chrono.ChQuaternionD(-4.03169574456196E-14,-4.58565757739071E-13,-0.0815439352761142,0.99666974802072)))

exported_items.append(body_20)



# Rigid body part
body_21= chrono.ChBodyAuxRef()
body_21.SetName('Spibot-LEG-3/Actuator_body_b-2')
body_21.SetPos(chrono.ChVectorD(0.0766518264243626,0.221626236563128,-0.209519665368063))
body_21.SetRot(chrono.ChQuaternionD(-0.0815439352761142,0.99666974802072,4.03870224981776e-14,4.58327609912089e-13))
body_21.SetMass(0.00204159144576871)
body_21.SetInertiaXX(chrono.ChVectorD(8.08481090947278e-07,7.82569697160034e-07,1.04939000634698e-07))
body_21.SetInertiaXY(chrono.ChVectorD(1.08069663204581e-19,6.55769437035526e-19,-1.14743748687818e-07))
body_21.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-4.17826009441434e-18,4.31502965232471e-20,-0.0175577824053523),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_4_1_shape = chrono.ChObjShapeFile() 
body_4_1_shape.SetFilename(shapes_dir +'body_4_1.obj') 
body_4_1_shape.SetColor(chrono.ChColor(0.843137254901961,0.843137254901961,0)) 
body_4_1_shape.SetFading(0) 
body_4_1_level = chrono.ChAssetLevel() 
body_4_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_4_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_4_1_level.GetAssets().push_back(body_4_1_shape) 
body_21.GetAssets().push_back(body_4_1_level) 

# Auxiliary marker (coordinate system feature)
marker_21_1 =chrono.ChMarker()
marker_21_1.SetName('LL-Act-Base')
body_21.AddMarker(marker_21_1)
marker_21_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(0.0766518264243173,0.213498999220701,-0.160184606706094),chrono.ChQuaternionD(-0.0815439352761142,0.99666974802072,4.03870224981776E-14,4.58327609912089E-13)))

# Auxiliary marker (coordinate system feature)
marker_21_2 =chrono.ChMarker()
marker_21_2.SetName('UL-Act-Base')
body_21.AddMarker(marker_21_2)
marker_21_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(0.0766518264243264,0.215124446689187,-0.170051618438488),chrono.ChQuaternionD(-0.0815439352761142,0.99666974802072,4.03870224981776E-14,4.58327609912089E-13)))

exported_items.append(body_21)



# Rigid body part
body_22= chrono.ChBodyAuxRef()
body_22.SetName('Spibot-LEG-3/limb_body_connector-1')
body_22.SetPos(chrono.ChVectorD(0.0865518264243083,0.246232273113652,-0.150219746825273))
body_22.SetRot(chrono.ChQuaternionD(-0.498644653171685,0.501351682816853,0.498644653172147,-0.501351682816393))
body_22.SetMass(0.0319301494979552)
body_22.SetInertiaXX(chrono.ChVectorD(2.2110890182935e-06,4.65620459313165e-06,4.83154745183423e-06))
body_22.SetInertiaXY(chrono.ChVectorD(1.32385342629299e-08,1.17474968675379e-20,-1.61462630740868e-19))
body_22.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(0.01,0.00875766097763167,0.01),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_2_1_shape = chrono.ChObjShapeFile() 
body_2_1_shape.SetFilename(shapes_dir +'body_2_1.obj') 
body_2_1_level = chrono.ChAssetLevel() 
body_2_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_2_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_2_1_level.GetAssets().push_back(body_2_1_shape) 
body_22.GetAssets().push_back(body_2_1_level) 

# Auxiliary marker (coordinate system feature)
marker_22_1 =chrono.ChMarker()
marker_22_1.SetName('LB-UL-Ref')
body_22.AddMarker(marker_22_1)
marker_22_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(0.0765518264243635,0.255907284186328,-0.210273007858665),chrono.ChQuaternionD(-0.498644653171686,0.501351682816392,0.501351682816854,0.498644653172146)))

# Auxiliary marker (coordinate system feature)
marker_22_2 =chrono.ChMarker()
marker_22_2.SetName('LB-B-Act-1')
body_22.AddMarker(marker_22_2)
marker_22_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(0.0765518264243083,0.256232126553462,-0.150273887219805),chrono.ChQuaternionD(0.705190031320552,-0.709018349357842,-3.26389843043606E-13,-3.24725379514077E-13)))

exported_items.append(body_22)



# Rigid body part
body_23= chrono.ChBodyAuxRef()
body_23.SetName('Spibot-LEG-3/lower_limb-1')
body_23.SetPos(chrono.ChVectorD(0.0765518264245476,0.154824485424998,-0.410318768120438))
body_23.SetRot(chrono.ChQuaternionD(0.999999970364508,0.000243456324874239,-4.597981762951e-13,2.88749842132001e-15))
body_23.SetMass(0.173763895224452)
body_23.SetInertiaXX(chrono.ChVectorD(0.000660134295478084,8.75830077741559e-06,0.000660653854093327))
body_23.SetInertiaXY(chrono.ChVectorD(-7.08403848703976e-11,-6.70199397442499e-12,3.12764124423156e-07))
body_23.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(4.14273289970014e-09,-0.0143933772184335,3.59893950746433e-07),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_7_1_shape = chrono.ChObjShapeFile() 
body_7_1_shape.SetFilename(shapes_dir +'body_7_1.obj') 
body_7_1_shape.SetColor(chrono.ChColor(0.898039215686275,0.917647058823529,0.929411764705882)) 
body_7_1_shape.SetFading(0.75) 
body_7_1_level = chrono.ChAssetLevel() 
body_7_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_7_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_7_1_level.GetAssets().push_back(body_7_1_shape) 
body_23.GetAssets().push_back(body_7_1_level) 

# Auxiliary marker (coordinate system feature)
marker_23_1 =chrono.ChMarker()
marker_23_1.SetName('LowerLimbCenterRef')
body_23.AddMarker(marker_23_1)
marker_23_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(0.0765518264245476,0.154824485424998,-0.410318768120438),chrono.ChQuaternionD(0.707106760231093,0.000172149618566456,0.000172149617916203,-0.707106760231088)))

# Auxiliary marker (coordinate system feature)
marker_23_2 =chrono.ChMarker()
marker_23_2.SetName('LL-UL-Ref')
body_23.AddMarker(marker_23_2)
marker_23_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(0.076551826424547,0.254824473570801,-0.410270076856906),chrono.ChQuaternionD(0.707106760231093,0.000172149618566456,0.000172149617916203,-0.707106760231089)))

# Collision shapes 
body_23.GetCollisionModel().ClearModel()
body_23.GetCollisionModel().AddSphere(0.01, chrono.ChVectorD(3.46944695195361E-17,-0.1,0))
body_23.GetCollisionModel().BuildModel()
body_23.SetCollide(True)

exported_items.append(body_23)



# Rigid body part
body_24= chrono.ChBodyAuxRef()
body_24.SetName('Spibot-LEG-3/upper_limb-1')
body_24.SetPos(chrono.ChVectorD(0.0765518266812141,0.255365880367523,-0.310271542536265))
body_24.SetRot(chrono.ChQuaternionD(-0.498644653135296,0.501351682853045,0.498644653135758,-0.501351682852586))
body_24.SetMass(0.0769386604687246)
body_24.SetInertiaXX(chrono.ChVectorD(1.2136124630043e-05,0.000291222022969906,0.000279898353184369))
body_24.SetInertiaXY(chrono.ChVectorD(1.51104854287323e-06,1.20058215311671e-05,-6.5000945813771e-08))
body_24.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-0.00433891891647107,-0.0160004109829567,2.90281587993209e-19),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_3_1_shape = chrono.ChObjShapeFile() 
body_3_1_shape.SetFilename(shapes_dir +'body_3_1.obj') 
body_3_1_level = chrono.ChAssetLevel() 
body_3_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_3_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_3_1_level.GetAssets().push_back(body_3_1_shape) 
body_24.GetAssets().push_back(body_3_1_level) 

# Auxiliary marker (coordinate system feature)
marker_24_1 =chrono.ChMarker()
marker_24_1.SetName('UL-LL-Ref')
body_24.AddMarker(marker_24_1)
marker_24_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(0.0765518266813061,0.254824476407783,-0.410270076934287),chrono.ChQuaternionD(0.707104190338733,-0.0019141590699668,-0.707104190339384,0.00191415906996888)))

# Auxiliary marker (coordinate system feature)
marker_24_2 =chrono.ChMarker()
marker_24_2.SetName('UL-LB-Ref')
body_24.AddMarker(marker_24_2)
marker_24_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(0.076551826681122,0.255907284327263,-0.210273008138243),chrono.ChQuaternionD(0.707104190338733,-0.0019141590699668,-0.707104190339384,0.00191415906996888)))

exported_items.append(body_24)



# Rigid body part
body_25= chrono.ChBodyAuxRef()
body_25.SetName('Spibot-LEG-6/limb_body_connector-1')
body_25.SetPos(chrono.ChVectorD(-0.113448182356349,0.246665396162869,-0.0702209390630026))
body_25.SetRot(chrono.ChQuaternionD(0.501351682816853,0.498644653171685,0.501351682816393,0.498644653172147))
body_25.SetMass(0.0319301494979552)
body_25.SetInertiaXX(chrono.ChVectorD(2.2110890182935e-06,4.65620459313165e-06,4.83154745183424e-06))
body_25.SetInertiaXY(chrono.ChVectorD(-1.32385342629298e-08,-1.13823654339839e-20,-1.61441326557281e-19))
body_25.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(0.01,0.00875766097763167,0.01),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_2_1_shape = chrono.ChObjShapeFile() 
body_2_1_shape.SetFilename(shapes_dir +'body_2_1.obj') 
body_2_1_level = chrono.ChAssetLevel() 
body_2_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_2_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_2_1_level.GetAssets().push_back(body_2_1_shape) 
body_25.GetAssets().push_back(body_2_1_level) 

# Auxiliary marker (coordinate system feature)
marker_25_1 =chrono.ChMarker()
marker_25_1.SetName('LB-UL-Ref')
body_25.AddMarker(marker_25_1)
marker_25_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.103448182356404,0.256990091969813,-0.0102759588186555),chrono.ChQuaternionD(-0.498644653172146,0.501351682816854,-0.501351682816392,-0.498644653171686)))

# Auxiliary marker (coordinate system feature)
marker_25_2 =chrono.ChMarker()
marker_25_2.SetName('LB-B-Act-1')
body_25.AddMarker(marker_25_2)
marker_25_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.103448182356349,0.256665249602679,-0.0702750794575158),chrono.ChQuaternionD(3.24735431634622E-13,-3.26301552230695E-13,0.709018349357842,0.705190031320552)))

exported_items.append(body_25)



# Rigid body part
body_26= chrono.ChBodyAuxRef()
body_26.SetName('Spibot-LEG-6/limb_body_connector_b-2')
body_26.SetPos(chrono.ChVectorD(-0.103481925881979,0.215747058291975,-0.0550533340876927))
body_26.SetRot(chrono.ChQuaternionD(0.501351682816852,0.498644653171686,0.501351682816393,0.498644653172147))
body_26.SetMass(0.0118048176111825)
body_26.SetInertiaXX(chrono.ChVectorD(8.17149703748216e-07,1.71878703364595e-06,1.78336759057685e-06))
body_26.SetInertiaXY(chrono.ChVectorD(-3.54051977884751e-09,-3.26945521019206e-21,-5.94596082364856e-20))
body_26.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-1.56699758850283e-18,-0.00621524420249397,8.63806342003782e-06),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_6_1_shape = chrono.ChObjShapeFile() 
body_6_1_shape.SetFilename(shapes_dir +'body_6_1.obj') 
body_6_1_level = chrono.ChAssetLevel() 
body_6_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_6_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_6_1_level.GetAssets().push_back(body_6_1_shape) 
body_26.GetAssets().push_back(body_6_1_level) 

# Auxiliary marker (coordinate system feature)
marker_26_1 =chrono.ChMarker()
marker_26_1.SetName('LB-B-Act-1')
body_26.AddMarker(marker_26_1)
marker_26_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.103448185912896,0.215665847700192,-0.0700531142474077),chrono.ChQuaternionD(3.24706019073181E-13,-3.26291659495905E-13,0.709018349357842,0.705190031320552)))

# Auxiliary marker (coordinate system feature)
marker_26_2 =chrono.ChMarker()
marker_26_2.SetName('LB-UL-Ref')
body_26.AddMarker(marker_26_2)
marker_26_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.103481925881984,0.215774128489236,-0.0500534073677877),chrono.ChQuaternionD(0.501351682816852,0.498644653171686,0.501351682816393,0.498644653172147)))

exported_items.append(body_26)



# Rigid body part
body_27= chrono.ChBodyAuxRef()
body_27.SetName('Spibot-LEG-6/Actuator_rod-1')
body_27.SetPos(chrono.ChVectorD(-0.103398182355707,0.211601877040437,0.0946134466340741))
body_27.SetRot(chrono.ChQuaternionD(0.999426563490189,-0.0338606584429772,-4.59235673051836e-13,-1.37537967842477e-14))
body_27.SetMass(0.00140945245841084)
body_27.SetInertiaXX(chrono.ChVectorD(2.33089158373325e-06,2.31640926673232e-06,3.41108052532564e-08))
body_27.SetInertiaXY(chrono.ChVectorD(1.43493967231331e-19,-2.11545415786653e-18,1.5554246445897e-07))
body_27.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-1.65060230227876e-19,-2.34447212110501e-18,0.0545976735175364),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_5_1_shape = chrono.ChObjShapeFile() 
body_5_1_shape.SetFilename(shapes_dir +'body_5_1.obj') 
body_5_1_level = chrono.ChAssetLevel() 
body_5_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_5_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_5_1_level.GetAssets().push_back(body_5_1_shape) 
body_27.GetAssets().push_back(body_5_1_level) 

# Auxiliary marker (coordinate system feature)
marker_27_1 =chrono.ChMarker()
marker_27_1.SetName('UL-Act-Shaft')
body_27.AddMarker(marker_27_1)
marker_27_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.103398182355758,0.215366715157888,0.150110893592915),chrono.ChQuaternionD(4.59235673051836E-13,1.37537967842477E-14,0.999426563490189,-0.0338606584429772)))

# Auxiliary marker (coordinate system feature)
marker_27_2 =chrono.ChMarker()
marker_27_2.SetName('LL-Act-Shaft')
body_27.AddMarker(marker_27_2)
marker_27_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.103398182355795,0.218074014478303,0.1900191700577),chrono.ChQuaternionD(4.59235673051836E-13,1.37537967842477E-14,0.999426563490189,-0.0338606584429772)))

exported_items.append(body_27)



# Rigid body part
body_28= chrono.ChBodyAuxRef()
body_28.SetName('Spibot-LEG-6/Actuator_body_b-2')
body_28.SetPos(chrono.ChVectorD(-0.103548182356404,0.222702897091505,-0.0106580660028762))
body_28.SetRot(chrono.ChQuaternionD(3.74370820212826e-14,-4.58195751320792e-13,0.0869387537805039,0.996213658354016))
body_28.SetMass(0.00204159144576871)
body_28.SetInertiaXX(chrono.ChVectorD(8.08481090947278e-07,7.80005520390042e-07,1.0750317740469e-07))
body_28.SetInertiaXY(chrono.ChVectorD(1.14996065086708e-19,6.54046824547719e-19,-1.22053749434785e-07))
body_28.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-4.17826009441434e-18,4.31502965232471e-20,-0.0175577824053523),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_4_1_shape = chrono.ChObjShapeFile() 
body_4_1_shape.SetFilename(shapes_dir +'body_4_1.obj') 
body_4_1_shape.SetColor(chrono.ChColor(0.843137254901961,0.843137254901961,0)) 
body_4_1_shape.SetFading(0) 
body_4_1_level = chrono.ChAssetLevel() 
body_4_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_4_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_4_1_level.GetAssets().push_back(body_4_1_shape) 
body_28.GetAssets().push_back(body_4_1_level) 

# Auxiliary marker (coordinate system feature)
marker_28_1 =chrono.ChMarker()
marker_28_1.SetName('LL-Act-Base')
body_28.AddMarker(marker_28_1)
marker_28_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.103548182356358,0.214041939695863,-0.0599022313119855),chrono.ChQuaternionD(3.74370820212826E-14,-4.58195751320792E-13,0.0869387537805039,0.996213658354016)))

# Auxiliary marker (coordinate system feature)
marker_28_2 =chrono.ChMarker()
marker_28_2.SetName('UL-Act-Base')
body_28.AddMarker(marker_28_2)
marker_28_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.103548182356367,0.215774131174992,-0.0500533982501636),chrono.ChQuaternionD(3.74370820212826E-14,-4.58195751320792E-13,0.0869387537805039,0.996213658354016)))

exported_items.append(body_28)



# Rigid body part
body_29= chrono.ChBodyAuxRef()
body_29.SetName('Spibot-LEG-6/Actuator_body-1')
body_29.SetPos(chrono.ChVectorD(-0.103398182356575,0.212039038025579,0.101057633027705))
body_29.SetRot(chrono.ChQuaternionD(1.35476289817152e-14,-4.5929820103644e-13,0.0338606584429773,0.999426563490189))
body_29.SetMass(0.00204159144576871)
body_29.SetInertiaXX(chrono.ChVectorD(8.08481090947278e-07,7.98194718667866e-07,8.93139791268659e-08))
body_29.SetInertiaXY(chrono.ChVectorD(4.4896577600038e-20,6.62238738167934e-19,-4.83114102281997e-08))
body_29.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-4.17192939730159e-18,5.58956732701871e-20,-0.0175577824053523),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_1_1_shape = chrono.ChObjShapeFile() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_1_1_shape.SetColor(chrono.ChColor(0.752941176470588,0.752941176470588,0.752941176470588)) 
body_1_1_shape.SetFading(0.75) 
body_1_1_level = chrono.ChAssetLevel() 
body_1_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_1_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_1_1_level.GetAssets().push_back(body_1_1_shape) 
body_29.GetAssets().push_back(body_1_1_level) 

# Auxiliary marker (coordinate system feature)
marker_29_1 =chrono.ChMarker()
marker_29_1.SetName('LL-Act-Base')
body_29.AddMarker(marker_29_1)
marker_29_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.103398182356529,0.208654913875061,0.0511722874467238),chrono.ChQuaternionD(1.35476289817152E-14,-4.5929820103644E-13,0.0338606584429773,0.999426563490189)))

# Auxiliary marker (coordinate system feature)
marker_29_2 =chrono.ChMarker()
marker_29_2.SetName('UL-Act-Base')
body_29.AddMarker(marker_29_2)
marker_29_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.103398182356538,0.209331738705165,0.06114935656292),chrono.ChQuaternionD(1.35476289817152E-14,-4.5929820103644E-13,0.0338606584429773,0.999426563490189)))

exported_items.append(body_29)



# Rigid body part
body_30= chrono.ChBodyAuxRef()
body_30.SetName('Spibot-LEG-6/lower_limb-1')
body_30.SetPos(chrono.ChVectorD(-0.103448184428644,0.15807291555938,0.189672412571112))
body_30.SetRot(chrono.ChQuaternionD(4.59714967050504e-13,-2.65154831127407e-15,0.999999970368455,0.000243440113756959))
body_30.SetMass(0.173763895224452)
body_30.SetInertiaXX(chrono.ChVectorD(0.000660134295478084,8.75830075713525e-06,0.000660653854113607))
body_30.SetInertiaXY(chrono.ChVectorD(7.08403843457549e-11,-6.70199627146262e-12,-3.12742988511991e-07))
body_30.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(4.14273289970014e-09,-0.0143933772184335,3.59893950746433e-07),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_7_1_shape = chrono.ChObjShapeFile() 
body_7_1_shape.SetFilename(shapes_dir +'body_7_1.obj') 
body_7_1_shape.SetColor(chrono.ChColor(0.898039215686275,0.917647058823529,0.929411764705882)) 
body_7_1_shape.SetFading(0.75) 
body_7_1_level = chrono.ChAssetLevel() 
body_7_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_7_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_7_1_level.GetAssets().push_back(body_7_1_shape) 
body_30.GetAssets().push_back(body_7_1_level) 

# Auxiliary marker (coordinate system feature)
marker_30_1 =chrono.ChMarker()
marker_30_1.SetName('LowerLimbCenterRef')
body_30.AddMarker(marker_30_1)
marker_30_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.103448184428644,0.15807291555938,0.189672412571112),chrono.ChQuaternionD(-0.000172138155575438,0.707106760233883,-0.707106760233879,-0.000172138154925303)))

# Auxiliary marker (coordinate system feature)
marker_30_2 =chrono.ChMarker()
marker_30_2.SetName('LL-UL-Ref')
body_30.AddMarker(marker_30_2)
marker_30_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.103448184428644,0.258072903706762,0.189721100592421),chrono.ChQuaternionD(-0.000172138155575438,0.707106760233883,-0.707106760233879,-0.000172138154925303)))

# Collision shapes 
body_30.GetCollisionModel().ClearModel()
body_30.GetCollisionModel().AddSphere(0.01, chrono.ChVectorD(3.46944695195361E-17,-0.1,0))
body_30.GetCollisionModel().BuildModel()
body_30.SetCollide(True)

exported_items.append(body_30)



# Rigid body part
body_31= chrono.ChBodyAuxRef()
body_31.SetName('Spibot-LEG-6/Actuator_rod_b-2')
body_31.SetPos(chrono.ChVectorD(-0.103548182356395,0.220949312976833,-0.0206285325554318))
body_31.SetRot(chrono.ChQuaternionD(3.74870658293642e-14,-4.58244901693398e-13,0.086938753780504,0.996213658354016))
body_31.SetMass(0.00122087835937912)
body_31.SetInertiaXX(chrono.ChVectorD(7.21325661454779e-07,6.96572336108662e-07,4.4240324094769e-08))
body_31.SetInertiaXY(chrono.ChVectorD(1.1125257259355e-19,6.32184603451995e-19,-1.1839299709974e-07))
body_31.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-2.22314235000441e-19,1.10781155047926e-18,0.0317642663115355),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_8_1_shape = chrono.ChObjShapeFile() 
body_8_1_shape.SetFilename(shapes_dir +'body_8_1.obj') 
body_8_1_level = chrono.ChAssetLevel() 
body_8_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_8_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_8_1_level.GetAssets().push_back(body_8_1_shape) 
body_31.GetAssets().push_back(body_8_1_level) 

# Auxiliary marker (coordinate system feature)
marker_31_1 =chrono.ChMarker()
marker_31_1.SetName('UL-Act-Shaft')
body_31.AddMarker(marker_31_1)
marker_31_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.103548182356446,0.230584628079484,0.0341556013509523),chrono.ChQuaternionD(0.086938753780504,0.996213658354016,-3.74870658293642E-14,4.58244901693398E-13)))

# Auxiliary marker (coordinate system feature)
marker_31_2 =chrono.ChMarker()
marker_31_2.SetName('LL-Act-Shaft')
body_31.AddMarker(marker_31_2)
marker_31_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.103548182356482,0.237513393995997,0.0735509335982397),chrono.ChQuaternionD(0.086938753780504,0.996213658354016,-3.74870658293642E-14,4.58244901693398E-13)))

exported_items.append(body_31)



# Rigid body part
body_32= chrono.ChBodyAuxRef()
body_32.SetName('Spibot-LEG-6/upper_limb-1')
body_32.SetPos(chrono.ChVectorD(-0.103448182613256,0.25753149835563,0.0897225723562364))
body_32.SetRot(chrono.ChQuaternionD(0.501351687452017,0.498644648511358,0.501351687451557,0.498644648511819))
body_32.SetMass(0.0769386604687246)
body_32.SetInertiaXX(chrono.ChVectorD(1.21361246857883e-05,0.00029122202291416,0.000279898353184369))
body_32.SetInertiaXY(chrono.ChVectorD(-1.51105369086067e-06,-1.20058215299679e-05,-6.50011672718248e-08))
body_32.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-0.00433891891647107,-0.0160004109829567,2.90281587993209e-19),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_3_1_shape = chrono.ChObjShapeFile() 
body_3_1_shape.SetFilename(shapes_dir +'body_3_1.obj') 
body_3_1_level = chrono.ChAssetLevel() 
body_3_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_3_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_3_1_level.GetAssets().push_back(body_3_1_shape) 
body_32.GetAssets().push_back(body_3_1_level) 

# Auxiliary marker (coordinate system feature)
marker_32_1 =chrono.ChMarker()
marker_32_1.SetName('UL-LL-Ref')
body_32.AddMarker(marker_32_1)
marker_32_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.103448182613348,0.258072904159931,0.189721106744272),chrono.ChQuaternionD(0.707104190321729,-0.00191416559155128,0.707104190321079,-0.00191416559154961)))

# Auxiliary marker (coordinate system feature)
marker_32_2 =chrono.ChMarker()
marker_32_2.SetName('UL-LB-Ref')
body_32.AddMarker(marker_32_2)
marker_32_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.103448182613164,0.256990092551328,-0.0102759620317989),chrono.ChQuaternionD(0.707104190321729,-0.00191416559155128,0.707104190321079,-0.00191416559154961)))

exported_items.append(body_32)



# Rigid body part
body_33= chrono.ChBodyAuxRef()
body_33.SetName('Spibot-LEG-1/limb_body_connector-1')
body_33.SetPos(chrono.ChVectorD(-0.0934481735756908,0.24623227300669,-0.150219766581464))
body_33.SetRot(chrono.ChQuaternionD(-0.498644653171685,0.501351682816852,0.498644653172147,-0.501351682816393))
body_33.SetMass(0.0319301494979552)
body_33.SetInertiaXX(chrono.ChVectorD(2.2110890182935e-06,4.65620459313164e-06,4.83154745183423e-06))
body_33.SetInertiaXY(chrono.ChVectorD(1.32385342629299e-08,1.30522695294681e-20,-1.61410843813686e-19))
body_33.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(0.01,0.00875766097763167,0.01),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_2_1_shape = chrono.ChObjShapeFile() 
body_2_1_shape.SetFilename(shapes_dir +'body_2_1.obj') 
body_2_1_level = chrono.ChAssetLevel() 
body_2_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_2_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_2_1_level.GetAssets().push_back(body_2_1_shape) 
body_33.GetAssets().push_back(body_2_1_level) 

# Auxiliary marker (coordinate system feature)
marker_33_1 =chrono.ChMarker()
marker_33_1.SetName('LB-UL-Ref')
body_33.AddMarker(marker_33_1)
marker_33_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.103448173575636,0.255907284079365,-0.210273027614856),chrono.ChQuaternionD(-0.498644653171686,0.501351682816392,0.501351682816854,0.498644653172145)))

# Auxiliary marker (coordinate system feature)
marker_33_2 =chrono.ChMarker()
marker_33_2.SetName('LB-B-Act-1')
body_33.AddMarker(marker_33_2)
marker_33_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.103448173575691,0.2562321264465,-0.150273906975996),chrono.ChQuaternionD(0.705190031320552,-0.709018349357842,-3.26447924366294E-13,-3.24430828870974E-13)))

exported_items.append(body_33)



# Rigid body part
body_34= chrono.ChBodyAuxRef()
body_34.SetName('Spibot-LEG-1/Actuator_body_b-2')
body_34.SetPos(chrono.ChVectorD(-0.103348167296681,0.221626241869362,-0.209519686071544))
body_34.SetRot(chrono.ChQuaternionD(-0.0815439433899001,0.996669747356879,3.99692977618465e-14,4.58007354565552e-13))
body_34.SetMass(0.00204159144576871)
body_34.SetInertiaXX(chrono.ChVectorD(8.08481090947277e-07,7.82569693423566e-07,1.04939004371166e-07))
body_34.SetInertiaXY(chrono.ChVectorD(1.07997029789078e-19,6.55274082118834e-19,-1.14743759720862e-07))
body_34.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-4.17826009441434e-18,4.31502965232471e-20,-0.0175577824053523),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_4_1_shape = chrono.ChObjShapeFile() 
body_4_1_shape.SetFilename(shapes_dir +'body_4_1.obj') 
body_4_1_shape.SetColor(chrono.ChColor(0.843137254901961,0.843137254901961,0)) 
body_4_1_shape.SetFading(0) 
body_4_1_level = chrono.ChAssetLevel() 
body_4_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_4_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_4_1_level.GetAssets().push_back(body_4_1_shape) 
body_34.GetAssets().push_back(body_4_1_level) 

# Auxiliary marker (coordinate system feature)
marker_34_1 =chrono.ChMarker()
marker_34_1.SetName('LL-Act-Base')
body_34.AddMarker(marker_34_1)
marker_34_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.103348167296726,0.213499003723672,-0.160184627541901),chrono.ChQuaternionD(-0.0815439433899001,0.996669747356879,3.99692977618465E-14,4.58007354565552E-13)))

# Auxiliary marker (coordinate system feature)
marker_34_2 =chrono.ChMarker()
marker_34_2.SetName('UL-Act-Base')
body_34.AddMarker(marker_34_2)
marker_34_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.103348167296717,0.21512445135281,-0.17005163924783),chrono.ChQuaternionD(-0.0815439433899001,0.996669747356879,3.99692977618465E-14,4.58007354565552E-13)))

exported_items.append(body_34)



# Rigid body part
body_35= chrono.ChBodyAuxRef()
body_35.SetName('Spibot-LEG-1/Actuator_rod_b-2')
body_35.SetPos(chrono.ChVectorD(-0.103348167296694,0.219980719887384,-0.199530816318089))
body_35.SetRot(chrono.ChQuaternionD(-0.0815439433899001,0.996669747356879,4.00086435661759e-14,4.5820110640621e-13))
body_35.SetMass(0.00122087835937912)
body_35.SetInertiaXX(chrono.ChVectorD(7.21325661454779e-07,6.99059602021648e-07,4.17530581817835e-08))
body_35.SetInertiaXY(chrono.ChVectorD(1.04387774740752e-19,6.33546995276293e-19,-1.11302255561627e-07))
body_35.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-2.22314235000441e-19,1.10781155047926e-18,0.0317642663115355),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_8_1_shape = chrono.ChObjShapeFile() 
body_8_1_shape.SetFilename(shapes_dir +'body_8_1.obj') 
body_8_1_level = chrono.ChAssetLevel() 
body_8_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_8_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_8_1_level.GetAssets().push_back(body_8_1_shape) 
body_35.GetAssets().push_back(body_8_1_level) 

# Auxiliary marker (coordinate system feature)
marker_35_1 =chrono.ChMarker()
marker_35_1.SetName('UL-Act-Shaft')
body_35.AddMarker(marker_35_1)
marker_35_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.103348167296643,0.229022272324464,-0.254416068932317),chrono.ChQuaternionD(-4.00086435661759E-14,-4.5820110640621E-13,-0.0815439433899001,0.996669747356879)))

# Auxiliary marker (coordinate system feature)
marker_35_2 =chrono.ChMarker()
marker_35_2.SetName('LL-Act-Shaft')
body_35.AddMarker(marker_35_2)
marker_35_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.103348167296607,0.235524062841016,-0.293884115756031),chrono.ChQuaternionD(-4.00086435661759E-14,-4.5820110640621E-13,-0.0815439433899001,0.996669747356879)))

exported_items.append(body_35)



# Rigid body part
body_36= chrono.ChBodyAuxRef()
body_36.SetName('Spibot-LEG-1/limb_body_connector_b-2')
body_36.SetPos(chrono.ChVectorD(-0.103414437047852,0.215151515845392,-0.165051718476699))
body_36.SetRot(chrono.ChQuaternionD(-0.498644653171685,0.501351682816853,0.498644653172147,-0.501351682816394))
body_36.SetMass(0.0118048176111825)
body_36.SetInertiaXX(chrono.ChVectorD(8.17149703748216e-07,1.71878703364595e-06,1.78336759057685e-06))
body_36.SetInertiaXY(chrono.ChVectorD(3.54051977885002e-09,3.93970701234162e-21,-5.94584800245345e-20))
body_36.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-1.56699758850283e-18,-0.00621524420249397,8.63806342003782e-06),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_6_1_shape = chrono.ChObjShapeFile() 
body_6_1_shape.SetFilename(shapes_dir +'body_6_1.obj') 
body_6_1_level = chrono.ChAssetLevel() 
body_6_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_6_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_6_1_level.GetAssets().push_back(body_6_1_shape) 
body_36.GetAssets().push_back(body_6_1_level) 

# Auxiliary marker (coordinate system feature)
marker_36_1 =chrono.ChMarker()
marker_36_1.SetName('LB-B-Act-1')
body_36.AddMarker(marker_36_1)
marker_36_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.103448177016935,0.215232726437176,-0.150051938316983),chrono.ChQuaternionD(0.705190031320551,-0.709018349357843,-3.26516642223968E-13,-3.24440455962837E-13)))

# Auxiliary marker (coordinate system feature)
marker_36_2 =chrono.ChMarker()
marker_36_2.SetName('LB-UL-Ref')
body_36.AddMarker(marker_36_2)
marker_36_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.103414437047848,0.215124445648131,-0.170051645196604),chrono.ChQuaternionD(-0.498644653171685,0.501351682816853,0.498644653172147,-0.501351682816394)))

exported_items.append(body_36)



# Rigid body part
body_37= chrono.ChBodyAuxRef()
body_37.SetName('Spibot-LEG-1/Actuator_rod-1')
body_37.SetPos(chrono.ChVectorD(-0.103498173575539,0.209404729436652,-0.3151359173087))
body_37.SetRot(chrono.ChQuaternionD(4.59470164214356e-13,-1.55146671252317e-14,0.999597848284551,0.0283573924205892))
body_37.SetMass(0.00140945245841084)
body_37.SetInertiaXX(chrono.ChVectorD(2.33089158373325e-06,2.31955787486e-06,3.09621971255775e-08))
body_37.SetInertiaXY(chrono.ChVectorD(1.20252382984888e-19,-2.11827496661401e-18,1.30374387941904e-07))
body_37.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-1.65060230227876e-19,-2.34447212110501e-18,0.0545976735175364),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_5_1_shape = chrono.ChObjShapeFile() 
body_5_1_shape.SetFilename(shapes_dir +'body_5_1.obj') 
body_5_1_level = chrono.ChAssetLevel() 
body_5_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_5_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_5_1_level.GetAssets().push_back(body_5_1_shape) 
body_37.GetAssets().push_back(body_5_1_level) 

# Auxiliary marker (coordinate system feature)
marker_37_1 =chrono.ChMarker()
marker_37_1.SetName('UL-Act-Shaft')
body_37.AddMarker(marker_37_1)
marker_37_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.103498173575488,0.212558220651334,-0.37067145654403),chrono.ChQuaternionD(0.999597848284551,0.0283573924205892,-4.59460280225348E-13,1.55194606633515E-14)))

# Auxiliary marker (coordinate system feature)
marker_37_2 =chrono.ChMarker()
marker_37_2.SetName('LL-Act-Shaft')
body_37.AddMarker(marker_37_2)
marker_37_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.103498173575451,0.214825899727061,-0.410607125207639),chrono.ChQuaternionD(0.999597848284551,0.0283573924205892,-4.59470164214356E-13,1.55146671252317E-14)))

exported_items.append(body_37)



# Rigid body part
body_38= chrono.ChBodyAuxRef()
body_38.SetName('Spibot-LEG-1/Actuator_body-1')
body_38.SetPos(chrono.ChVectorD(-0.103498173575533,0.209744178928954,-0.321113898319204))
body_38.SetRot(chrono.ChQuaternionD(-0.0283573924205892,0.999597848284551,1.54370144981112e-14,4.59490385866261e-13))
body_38.SetMass(0.00204159144576871)
body_38.SetInertiaXX(chrono.ChVectorD(8.08481090947278e-07,7.99172674748434e-07,8.83360230462981e-08))
body_38.SetInertiaXY(chrono.ChVectorD(3.76839941475015e-20,6.63049803451057e-19,-4.04942184825242e-08))
body_38.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-4.17192939730159e-18,5.58956732701871e-20,-0.0175577824053523),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_1_1_shape = chrono.ChObjShapeFile() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_1_1_shape.SetColor(chrono.ChColor(0.752941176470588,0.752941176470588,0.752941176470588)) 
body_1_1_shape.SetFading(0.75) 
body_1_1_level = chrono.ChAssetLevel() 
body_1_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_1_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_1_1_level.GetAssets().push_back(body_1_1_shape) 
body_38.GetAssets().push_back(body_1_1_level) 

# Auxiliary marker (coordinate system feature)
marker_38_1 =chrono.ChMarker()
marker_38_1.SetName('LL-Act-Base')
body_38.AddMarker(marker_38_1)
marker_38_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.103498173575579,0.206909580084296,-0.271194312489693),chrono.ChQuaternionD(-0.0283573924205892,0.999597848284551,1.54370144981112E-14,4.59490385866261E-13)))

# Auxiliary marker (coordinate system feature)
marker_38_2 =chrono.ChMarker()
marker_38_2.SetName('UL-Act-Base')
body_38.AddMarker(marker_38_2)
marker_38_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.10349817357557,0.207476499853228,-0.281178229655595),chrono.ChQuaternionD(-0.0283573924205892,0.999597848284551,1.54370144981112E-14,4.59490385866261E-13)))

exported_items.append(body_38)



# Rigid body part
body_39= chrono.ChBodyAuxRef()
body_39.SetName('Spibot-LEG-1/upper_limb-1')
body_39.SetPos(chrono.ChVectorD(-0.103448173575543,0.255365880907447,-0.310271568450641))
body_39.SetRot(chrono.ChQuaternionD(-0.498644662040788,0.501351673995638,0.498644662041249,-0.501351673995179))
body_39.SetMass(0.0769386604687246)
body_39.SetInertiaXX(chrono.ChVectorD(1.21361245226805e-05,0.000291222023077268,0.000279898353184369))
body_39.SetInertiaXY(chrono.ChVectorD(1.51103862808834e-06,1.20058215334762e-05,-6.50005192959008e-08))
body_39.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-0.00433891891647107,-0.0160004109829567,2.90281587993209e-19),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_3_1_shape = chrono.ChObjShapeFile() 
body_3_1_shape.SetFilename(shapes_dir +'body_3_1.obj') 
body_3_1_level = chrono.ChAssetLevel() 
body_3_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_3_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_3_1_level.GetAssets().push_back(body_3_1_shape) 
body_39.GetAssets().push_back(body_3_1_level) 

# Auxiliary marker (coordinate system feature)
marker_39_1 =chrono.ChMarker()
marker_39_1.SetName('UL-LL-Ref')
body_39.AddMarker(marker_39_1)
marker_39_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.103448173575451,0.254824480500248,-0.410270102867897),chrono.ChQuaternionD(0.707104190372734,-0.00191414650970159,-0.707104190373384,0.00191414650970317)))

# Auxiliary marker (coordinate system feature)
marker_39_2 =chrono.ChMarker()
marker_39_2.SetName('UL-LB-Ref')
body_39.AddMarker(marker_39_2)
marker_39_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.103448173575635,0.255907281314647,-0.210273034033385),chrono.ChQuaternionD(0.707104190372734,-0.00191414650970159,-0.707104190373384,0.00191414650970317)))

exported_items.append(body_39)



# Rigid body part
body_40= chrono.ChBodyAuxRef()
body_40.SetName('Spibot-LEG-1/lower_limb-1')
body_40.SetPos(chrono.ChVectorD(-0.103448173575451,0.154824495213514,-0.410318810301462))
body_40.SetRot(chrono.ChQuaternionD(0.999999970337902,0.000243565586627068,-4.59548423128594e-13,2.69319879340228e-15))
body_40.SetMass(0.173763895224452)
body_40.SetInertiaXX(chrono.ChVectorD(0.000660134295478084,8.75830091413935e-06,0.000660653853956603))
body_40.SetInertiaXY(chrono.ChVectorD(-7.08403860818266e-11,-6.70197849451626e-12,3.12906578928985e-07))
body_40.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(4.14273289970014e-09,-0.0143933772184335,3.59893950746433e-07),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_7_1_shape = chrono.ChObjShapeFile() 
body_7_1_shape.SetFilename(shapes_dir +'body_7_1.obj') 
body_7_1_shape.SetColor(chrono.ChColor(0.898039215686275,0.917647058823529,0.929411764705882)) 
body_7_1_shape.SetFading(0.75) 
body_7_1_level = chrono.ChAssetLevel() 
body_7_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_7_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_7_1_level.GetAssets().push_back(body_7_1_shape) 
body_40.GetAssets().push_back(body_7_1_level) 

# Auxiliary marker (coordinate system feature)
marker_40_1 =chrono.ChMarker()
marker_40_1.SetName('LowerLimbCenterRef')
body_40.AddMarker(marker_40_1)
marker_40_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.103448173575451,0.154824495213514,-0.410318810301462),chrono.ChQuaternionD(0.707106760212279,0.000172226878292629,0.00017222687764273,-0.707106760212275)))

# Auxiliary marker (coordinate system feature)
marker_40_2 =chrono.ChMarker()
marker_40_2.SetName('LL-UL-Ref')
body_40.AddMarker(marker_40_2)
marker_40_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.103448173575452,0.254824483348675,-0.410270097185582),chrono.ChQuaternionD(0.707106760212279,0.000172226878292629,0.00017222687764273,-0.707106760212275)))

# Collision shapes 
body_40.GetCollisionModel().ClearModel()
body_40.GetCollisionModel().AddSphere(0.01, chrono.ChVectorD(3.46944695195361E-17,-0.1,0))
body_40.GetCollisionModel().BuildModel()
body_40.SetCollide(True)

exported_items.append(body_40)



# Rigid body part
body_41= chrono.ChBodyAuxRef()
body_41.SetName('Body-2')
body_41.SetPos(chrono.ChVectorD(-0.0134481779660203,0.23594898852646,-0.110163495529889))
body_41.SetRot(chrono.ChQuaternionD(0.0019141591236923,0.707104229144446,-0.00191415891359841,-0.707104151533946))
body_41.SetMass(0.341410951377452)
body_41.SetInertiaXX(chrono.ChVectorD(0.000241317387799145,0.00125554646880151,0.00103704927238703))
body_41.SetInertiaXY(chrono.ChVectorD(5.49131770190389e-06,-8.73381196775929e-11,6.02717032743408e-13))
body_41.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-2.0412340707415e-18,0,1.64121582559538e-17),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_41_1_shape = chrono.ChObjShapeFile() 
body_41_1_shape.SetFilename(shapes_dir +'body_41_1.obj') 
body_41_1_shape.SetColor(chrono.ChColor(0.792156862745098,0.819607843137255,0.933333333333333)) 
body_41_1_shape.SetFading(0) 
body_41_1_level = chrono.ChAssetLevel() 
body_41_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_41_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_41_1_level.GetAssets().push_back(body_41_1_shape) 
body_41.GetAssets().push_back(body_41_1_level) 

# Auxiliary marker (coordinate system feature)
marker_41_1 =chrono.ChMarker()
marker_41_1.SetName('BM-4')
body_41.AddMarker(marker_41_1)
marker_41_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(0.0765518176436502,0.236165550158031,-0.0701640718925539),chrono.ChQuaternionD(0.501351710330357,0.498644680537091,0.498644625806739,-0.501351655302887)))

# Auxiliary marker (coordinate system feature)
marker_41_2 =chrono.ChMarker()
marker_41_2.SetName('BM-3')
body_41.AddMarker(marker_41_2)
marker_41_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(0.0765518264243082,0.235732427001851,-0.150162899411034),chrono.ChQuaternionD(0.501351710330357,0.498644680537091,0.498644625806739,-0.501351655302887)))

# Auxiliary marker (coordinate system feature)
marker_41_3 =chrono.ChMarker()
marker_41_3.SetName('BM-5')
body_41.AddMarker(marker_41_3)
marker_41_3.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.0134481823563493,0.236165550104549,-0.0701640817706494),chrono.ChQuaternionD(0.501351710330357,0.498644680537091,0.498644625806739,-0.501351655302887)))

# Auxiliary marker (coordinate system feature)
marker_41_4 =chrono.ChMarker()
marker_41_4.SetName('BM-2')
body_41.AddMarker(marker_41_4)
marker_41_4.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.0134481735756912,0.23573242694837,-0.150162909289129),chrono.ChQuaternionD(0.501351710330357,0.498644680537091,0.498644625806739,-0.501351655302887)))

# Auxiliary marker (coordinate system feature)
marker_41_5 =chrono.ChMarker()
marker_41_5.SetName('BM-6')
body_41.AddMarker(marker_41_5)
marker_41_5.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.103448182356349,0.236165550051068,-0.0701640916487449),chrono.ChQuaternionD(0.501351710330357,0.498644680537091,0.498644625806739,-0.501351655302887)))

# Auxiliary marker (coordinate system feature)
marker_41_6 =chrono.ChMarker()
marker_41_6.SetName('BM-1')
body_41.AddMarker(marker_41_6)
marker_41_6.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.103448173575691,0.235732426894889,-0.150162919167225),chrono.ChQuaternionD(0.501351710330357,0.498644680537091,0.498644625806739,-0.501351655302887)))

exported_items.append(body_41)



# Rigid body part
body_42= chrono.ChBodyAuxRef()
body_42.SetName('Spibot-LEG-5/limb_body_connector_b-2')
body_42.SetPos(chrono.ChVectorD(-0.0134819275359306,0.215747060992745,-0.0550533169583308))
body_42.SetRot(chrono.ChQuaternionD(0.501351682816852,0.498644653171686,0.501351682816393,0.498644653172147))
body_42.SetMass(0.0118048176111825)
body_42.SetInertiaXX(chrono.ChVectorD(8.17149703748215e-07,1.71878703364595e-06,1.78336759057685e-06))
body_42.SetInertiaXY(chrono.ChVectorD(-3.54051977884766e-09,-2.7328999994824e-21,-5.94540579121349e-20))
body_42.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-1.56699758850283e-18,-0.00621524420249397,8.63806342003782e-06),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_6_1_shape = chrono.ChObjShapeFile() 
body_6_1_shape.SetFilename(shapes_dir +'body_6_1.obj') 
body_6_1_level = chrono.ChAssetLevel() 
body_6_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_6_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_6_1_level.GetAssets().push_back(body_6_1_shape) 
body_42.GetAssets().push_back(body_6_1_level) 

# Auxiliary marker (coordinate system feature)
marker_42_1 =chrono.ChMarker()
marker_42_1.SetName('LB-B-Act-1')
body_42.AddMarker(marker_42_1)
marker_42_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.0134481875668475,0.215665850400961,-0.0700530971180458),chrono.ChQuaternionD(3.24883238242028E-13,-3.26076250731119E-13,0.709018349357842,0.705190031320552)))

# Auxiliary marker (coordinate system feature)
marker_42_2 =chrono.ChMarker()
marker_42_2.SetName('LB-UL-Ref')
body_42.AddMarker(marker_42_2)
marker_42_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.0134819275359352,0.215774131190006,-0.0500533902384257),chrono.ChQuaternionD(0.501351682816852,0.498644653171686,0.501351682816393,0.498644653172147)))

exported_items.append(body_42)



# Rigid body part
body_43= chrono.ChBodyAuxRef()
body_43.SetName('Spibot-LEG-5/Actuator_body_b-2')
body_43.SetPos(chrono.ChVectorD(-0.0135481823564043,0.222702898306728,-0.0106580534232886))
body_43.SetRot(chrono.ChQuaternionD(3.77865722956866e-14,-4.58230971094679e-13,0.0869387521574456,0.996213658495659))
body_43.SetMass(0.00204159144576871)
body_43.SetInertiaXX(chrono.ChVectorD(8.08481090947278e-07,7.80005521185455e-07,1.07503176609277e-07))
body_43.SetInertiaXY(chrono.ChVectorD(1.15055982843991e-19,6.54153604093117e-19,-1.22053747243467e-07))
body_43.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-4.17826009441434e-18,4.31502965232471e-20,-0.0175577824053523),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_4_1_shape = chrono.ChObjShapeFile() 
body_4_1_shape.SetFilename(shapes_dir +'body_4_1.obj') 
body_4_1_shape.SetColor(chrono.ChColor(0.843137254901961,0.843137254901961,0)) 
body_4_1_shape.SetFading(0) 
body_4_1_level = chrono.ChAssetLevel() 
body_4_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_4_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_4_1_level.GetAssets().push_back(body_4_1_shape) 
body_43.GetAssets().push_back(body_4_1_level) 

# Auxiliary marker (coordinate system feature)
marker_43_1 =chrono.ChMarker()
marker_43_1.SetName('LL-Act-Base')
body_43.AddMarker(marker_43_1)
marker_43_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.013548182356359,0.214041941071547,-0.0599022187606193),chrono.ChQuaternionD(3.77865722956866E-14,-4.58230971094679E-13,0.0869387521574456,0.996213658495659)))

# Auxiliary marker (coordinate system feature)
marker_43_2 =chrono.ChMarker()
marker_43_2.SetName('UL-Act-Base')
body_43.AddMarker(marker_43_2)
marker_43_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.0135481823563681,0.215774132518583,-0.0500533856931531),chrono.ChQuaternionD(3.77865722956866E-14,-4.58230971094679E-13,0.0869387521574456,0.996213658495659)))

exported_items.append(body_43)



# Rigid body part
body_44= chrono.ChBodyAuxRef()
body_44.SetName('Spibot-LEG-5/Actuator_rod_b-2')
body_44.SetPos(chrono.ChVectorD(-0.013548182356395,0.220949314224544,-0.0206285199815577))
body_44.SetRot(chrono.ChQuaternionD(3.77105201060524e-14,-4.57976861128442e-13,0.0869387521574456,0.996213658495659))
body_44.SetMass(0.00122087835937912)
body_44.SetInertiaXX(chrono.ChVectorD(7.21325661454779e-07,6.96572336880219e-07,4.42403233232126e-08))
body_44.SetInertiaXY(chrono.ChVectorD(1.11104035670118e-19,6.31813710805792e-19,-1.18392994974145e-07))
body_44.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-2.22314235000441e-19,1.10781155047926e-18,0.0317642663115355),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_8_1_shape = chrono.ChObjShapeFile() 
body_8_1_shape.SetFilename(shapes_dir +'body_8_1.obj') 
body_8_1_level = chrono.ChAssetLevel() 
body_8_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_8_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_8_1_level.GetAssets().push_back(body_8_1_shape) 
body_44.GetAssets().push_back(body_8_1_level) 

# Auxiliary marker (coordinate system feature)
marker_44_1 =chrono.ChMarker()
marker_44_1.SetName('UL-Act-Shaft')
body_44.AddMarker(marker_44_1)
marker_44_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.0135481823564454,0.230584629148684,0.0341556139562226),chrono.ChQuaternionD(0.0869387521574456,0.996213658495659,-3.77105201060524E-14,4.57976861128442E-13)))

# Auxiliary marker (coordinate system feature)
marker_44_2 =chrono.ChMarker()
marker_44_2.SetName('LL-Act-Shaft')
body_44.AddMarker(marker_44_2)
marker_44_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.0135481823564816,0.237513394936829,0.0735509462260871),chrono.ChQuaternionD(0.0869387521574456,0.996213658495659,-3.77105201060524E-14,4.57976861128442E-13)))

exported_items.append(body_44)



# Rigid body part
body_45= chrono.ChBodyAuxRef()
body_45.SetName('Spibot-LEG-5/Actuator_rod-1')
body_45.SetPos(chrono.ChVectorD(-0.0133981826132578,0.211601876906579,0.0946134659969513))
body_45.SetRot(chrono.ChQuaternionD(0.999426563631346,-0.0338606542766029,-4.59562795307937e-13,-1.37885501492864e-14))
body_45.SetMass(0.00140945245841084)
body_45.SetInertiaXX(chrono.ChVectorD(2.33089158373325e-06,2.316409269326e-06,3.41108026595768e-08))
body_45.SetInertiaXY(chrono.ChVectorD(1.43558566714024e-19,-2.11707345036726e-18,1.55542445430238e-07))
body_45.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-1.65060230227876e-19,-2.34447212110501e-18,0.0545976735175364),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_5_1_shape = chrono.ChObjShapeFile() 
body_5_1_shape.SetFilename(shapes_dir +'body_5_1.obj') 
body_5_1_level = chrono.ChAssetLevel() 
body_5_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_5_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_5_1_level.GetAssets().push_back(body_5_1_shape) 
body_45.GetAssets().push_back(body_5_1_level) 

# Auxiliary marker (coordinate system feature)
marker_45_1 =chrono.ChMarker()
marker_45_1.SetName('UL-Act-Shaft')
body_45.AddMarker(marker_45_1)
marker_45_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.0133981826133088,0.215366714561319,0.150110912987182),chrono.ChQuaternionD(4.59562795307937E-13,1.37885501492864E-14,0.999426563631346,-0.0338606542766029)))

# Auxiliary marker (coordinate system feature)
marker_45_2 =chrono.ChMarker()
marker_45_2.SetName('LL-Act-Shaft')
body_45.AddMarker(marker_45_2)
marker_45_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.0133981826133455,0.218074013548997,0.190019189474539),chrono.ChQuaternionD(4.59562795307937E-13,1.37885501492864E-14,0.999426563631346,-0.0338606542766029)))

exported_items.append(body_45)



# Rigid body part
body_46= chrono.ChBodyAuxRef()
body_46.SetName('Spibot-LEG-5/Actuator_body-1')
body_46.SetPos(chrono.ChVectorD(-0.0133981826132656,0.212039037254823,0.101057643801614))
body_46.SetRot(chrono.ChQuaternionD(1.37052356468738e-14,-4.58993479541451e-13,0.0338606542766029,0.999426563631346))
body_46.SetMass(0.00204159144576871)
body_46.SetInertiaXX(chrono.ChVectorD(8.08481090947277e-07,7.98194719473462e-07,8.93139783212703e-08))
body_46.SetInertiaXY(chrono.ChVectorD(4.482960887846e-20,6.618691672995e-19,-4.83114043178854e-08))
body_46.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-4.17192939730159e-18,5.58956732701871e-20,-0.0175577824053523),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_1_1_shape = chrono.ChObjShapeFile() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_1_1_shape.SetColor(chrono.ChColor(0.752941176470588,0.752941176470588,0.752941176470588)) 
body_1_1_shape.SetFading(0.75) 
body_1_1_level = chrono.ChAssetLevel() 
body_1_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_1_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_1_1_level.GetAssets().push_back(body_1_1_shape) 
body_46.GetAssets().push_back(body_1_1_level) 

# Auxiliary marker (coordinate system feature)
marker_46_1 =chrono.ChMarker()
marker_46_1.SetName('LL-Act-Base')
body_46.AddMarker(marker_46_1)
marker_46_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.0133981826132198,0.208654913520226,0.0511722981924178),chrono.ChQuaternionD(1.37052356468738E-14,-4.58993479541451E-13,0.0338606542766029,0.999426563631346)))

# Auxiliary marker (coordinate system feature)
marker_46_2 =chrono.ChMarker()
marker_46_2.SetName('UL-Act-Base')
body_46.AddMarker(marker_46_2)
marker_46_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.013398182613229,0.209331738267145,0.061149367314257),chrono.ChQuaternionD(1.37052356468738E-14,-4.58993479541451E-13,0.0338606542766029,0.999426563631346)))

exported_items.append(body_46)



# Rigid body part
body_47= chrono.ChBodyAuxRef()
body_47.SetName('Spibot-LEG-5/lower_limb-1')
body_47.SetPos(chrono.ChVectorD(-0.0134481826835879,0.15807291414518,0.189672437832875))
body_47.SetRot(chrono.ChQuaternionD(4.59951534939898e-13,-2.37310178543652e-15,0.999999970376219,0.000243408217159078))
body_47.SetMass(0.173763895224452)
body_47.SetInertiaXX(chrono.ChVectorD(0.000660134295478084,8.75830071723615e-06,0.000660653854153506))
body_47.SetInertiaXY(chrono.ChVectorD(7.0840383591321e-11,-6.70200090202855e-12,-3.12701402010124e-07))
body_47.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(4.14273289970014e-09,-0.0143933772184335,3.59893950746433e-07),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_7_1_shape = chrono.ChObjShapeFile() 
body_7_1_shape.SetFilename(shapes_dir +'body_7_1.obj') 
body_7_1_shape.SetColor(chrono.ChColor(0.898039215686275,0.917647058823529,0.929411764705882)) 
body_7_1_shape.SetFading(0.75) 
body_7_1_level = chrono.ChAssetLevel() 
body_7_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_7_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_7_1_level.GetAssets().push_back(body_7_1_shape) 
body_47.GetAssets().push_back(body_7_1_level) 

# Auxiliary marker (coordinate system feature)
marker_47_1 =chrono.ChMarker()
marker_47_1.SetName('LowerLimbCenterRef')
body_47.AddMarker(marker_47_1)
marker_47_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.0134481826835879,0.15807291414518,0.189672437832875),chrono.ChQuaternionD(-0.000172115601274907,0.707106760239373,-0.70710676023937,-0.000172115600624457)))

# Auxiliary marker (coordinate system feature)
marker_47_2 =chrono.ChMarker()
marker_47_2.SetName('LL-UL-Ref')
body_47.AddMarker(marker_47_2)
marker_47_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.0134481826835884,0.258072902295668,0.189721119474865),chrono.ChQuaternionD(-0.000172115601274907,0.707106760239373,-0.70710676023937,-0.000172115600624457)))

# Collision shapes 
body_47.GetCollisionModel().ClearModel()
body_47.GetCollisionModel().AddSphere(0.01, chrono.ChVectorD(3.46944695195361E-17,-0.1,0))
body_47.GetCollisionModel().BuildModel()
body_47.SetCollide(True)

exported_items.append(body_47)



# Rigid body part
body_48= chrono.ChBodyAuxRef()
body_48.SetName('Spibot-LEG-5/upper_limb-1')
body_48.SetPos(chrono.ChVectorD(-0.0134481826132556,0.257531497797575,0.0897225841115481))
body_48.SetRot(chrono.ChQuaternionD(0.501351685679396,0.498644650293601,0.501351685678937,0.498644650294062))
body_48.SetMass(0.0769386604687246)
body_48.SetInertiaXX(chrono.ChVectorD(1.21361246643019e-05,0.000291222022935647,0.000279898353184369))
body_48.SetInertiaXY(chrono.ChVectorD(-1.51105170662873e-06,-1.200582153043e-05,-6.50010819133807e-08))
body_48.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-0.00433891891647107,-0.0160004109829567,2.90281587993209e-19),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_3_1_shape = chrono.ChObjShapeFile() 
body_3_1_shape.SetFilename(shapes_dir +'body_3_1.obj') 
body_3_1_level = chrono.ChAssetLevel() 
body_3_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_3_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_3_1_level.GetAssets().push_back(body_3_1_shape) 
body_48.GetAssets().push_back(body_3_1_level) 

# Auxiliary marker (coordinate system feature)
marker_48_1 =chrono.ChMarker()
marker_48_1.SetName('UL-LL-Ref')
body_48.AddMarker(marker_48_1)
marker_48_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.0134481826133477,0.258072902890912,0.189721118503433),chrono.ChQuaternionD(0.707104190328534,-0.00191416307788289,0.707104190327883,-0.0019141630778815)))

# Auxiliary marker (coordinate system feature)
marker_48_2 =chrono.ChMarker()
marker_48_2.SetName('UL-LB-Ref')
body_48.AddMarker(marker_48_2)
marker_48_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.0134481826131636,0.256990092704239,-0.0102759502803365),chrono.ChQuaternionD(0.707104190328534,-0.00191416307788289,0.707104190327883,-0.0019141630778815)))

exported_items.append(body_48)



# Rigid body part
body_49= chrono.ChBodyAuxRef()
body_49.SetName('Spibot-LEG-5/limb_body_connector-1')
body_49.SetPos(chrono.ChVectorD(-0.0234481823563493,0.24666539621635,-0.0702209291849071))
body_49.SetRot(chrono.ChQuaternionD(0.501351682816853,0.498644653171685,0.501351682816393,0.498644653172146))
body_49.SetMass(0.0319301494979552)
body_49.SetInertiaXX(chrono.ChVectorD(2.2110890182935e-06,4.65620459313164e-06,4.83154745183423e-06))
body_49.SetInertiaXY(chrono.ChVectorD(-1.32385342629295e-08,-9.70070315805874e-21,-1.61316073557728e-19))
body_49.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(0.01,0.00875766097763167,0.01),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_2_1_shape = chrono.ChObjShapeFile() 
body_2_1_shape.SetFilename(shapes_dir +'body_2_1.obj') 
body_2_1_shape.SetColor(chrono.ChColor(0.898039215686275,0.917647058823529,0.929411764705882)) 
body_2_1_shape.SetFading(0.75) 
body_2_1_level = chrono.ChAssetLevel() 
body_2_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_2_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_2_1_level.GetAssets().push_back(body_2_1_shape) 
body_49.GetAssets().push_back(body_2_1_level) 

# Auxiliary marker (coordinate system feature)
marker_49_1 =chrono.ChMarker()
marker_49_1.SetName('LB-UL-Ref')
body_49.AddMarker(marker_49_1)
marker_49_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.0134481823564045,0.256990092023294,-0.01027594894056),chrono.ChQuaternionD(-0.498644653172146,0.501351682816853,-0.501351682816393,-0.498644653171686)))

# Auxiliary marker (coordinate system feature)
marker_49_2 =chrono.ChMarker()
marker_49_2.SetName('LB-B-Act-1')
body_49.AddMarker(marker_49_2)
marker_49_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.0134481823563493,0.25666524965616,-0.0702750695794203),chrono.ChQuaternionD(3.24726867114467E-13,-3.2584031269656E-13,0.709018349357842,0.705190031320552)))

exported_items.append(body_49)




# Mate constraint: Distance1 [MateDistanceDim] type:5 align:1 flip:False
#   Entity 0: C::E name: body_36 , SW name: Spibot-LEG-1/limb_body_connector_b-2 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_41 , SW name: Body-2 ,  SW ref.type:2 (2)

link_1 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(-0.113414437047866,0.225232579876986,-0.150106078711515)
cB = chrono.ChVectorD(-0.0134481779660203,0.22594913508665,-0.110109355135367)
dA = chrono.ChVectorD(-4.44089209850063e-16,0.999985343981005,-0.00541403945223998)
dB = chrono.ChVectorD(-1.13959586670642e-15,-0.999985343981005,0.00541403945223878)
link_1.Initialize(body_36,body_41,False,cA,cB,dB)
link_1.SetDistance(-0.0005)
link_1.SetName("Distance1")
exported_items.append(link_1)

link_2 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.113414437047866,0.225232579876986,-0.150106078711515)
dA = chrono.ChVectorD(-4.44089209850063e-16,0.999985343981005,-0.00541403945223998)
cB = chrono.ChVectorD(-0.0134481779660203,0.22594913508665,-0.110109355135367)
dB = chrono.ChVectorD(-1.13959586670642e-15,-0.999985343981005,0.00541403945223878)
link_2.SetFlipped(True)
link_2.Initialize(body_36,body_41,False,cA,cB,dA,dB)
link_2.SetName("Distance1")
exported_items.append(link_2)


# Mate constraint: Distance2 [MateDistanceDim] type:5 align:1 flip:False
#   Entity 0: C::E name: body_6 , SW name: Spibot-LEG-2/limb_body_connector_b-2 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_41 , SW name: Body-2 ,  SW ref.type:2 (2)

link_3 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(-0.023414433606622,0.22523258092227,-0.150106062243234)
cB = chrono.ChVectorD(-0.0134481779660203,0.22594913508665,-0.110109355135367)
dA = chrono.ChVectorD(-1.66533453693773e-16,0.999985343981005,-0.00541403945224009)
dB = chrono.ChVectorD(-1.13959586670642e-15,-0.999985343981005,0.00541403945223878)
link_3.Initialize(body_6,body_41,False,cA,cB,dB)
link_3.SetDistance(-0.0005)
link_3.SetName("Distance2")
exported_items.append(link_3)

link_4 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.023414433606622,0.22523258092227,-0.150106062243234)
dA = chrono.ChVectorD(-1.66533453693773e-16,0.999985343981005,-0.00541403945224009)
cB = chrono.ChVectorD(-0.0134481779660203,0.22594913508665,-0.110109355135367)
dB = chrono.ChVectorD(-1.13959586670642e-15,-0.999985343981005,0.00541403945223878)
link_4.SetFlipped(True)
link_4.Initialize(body_6,body_41,False,cA,cB,dA,dB)
link_4.SetName("Distance2")
exported_items.append(link_4)


# Mate constraint: Distance6 [MateDistanceDim] type:5 align:1 flip:False
#   Entity 0: C::E name: body_18 , SW name: Spibot-LEG-3/limb_body_connector_b-2 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_41 , SW name: Body-2 ,  SW ref.type:2 (2)

link_5 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(0.0665855443445694,0.225232576974876,-0.150106059424835)
cB = chrono.ChVectorD(-0.0134481779660203,0.22594913508665,-0.110109355135367)
dA = chrono.ChVectorD(-1.66533453693774e-16,0.999985343981005,-0.00541403945224001)
dB = chrono.ChVectorD(-1.13959586670642e-15,-0.999985343981005,0.00541403945223878)
link_5.Initialize(body_18,body_41,False,cA,cB,dB)
link_5.SetDistance(-0.0005)
link_5.SetName("Distance6")
exported_items.append(link_5)

link_6 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.0665855443445694,0.225232576974876,-0.150106059424835)
dA = chrono.ChVectorD(-1.66533453693774e-16,0.999985343981005,-0.00541403945224001)
cB = chrono.ChVectorD(-0.0134481779660203,0.22594913508665,-0.110109355135367)
dB = chrono.ChVectorD(-1.13959586670642e-15,-0.999985343981005,0.00541403945223878)
link_6.SetFlipped(True)
link_6.Initialize(body_18,body_41,False,cA,cB,dA,dB)
link_6.SetName("Distance6")
exported_items.append(link_6)


# Mate constraint: Distance5 [MateDistanceDim] type:5 align:1 flip:False
#   Entity 0: C::E name: body_15 , SW name: Spibot-LEG-4/limb_body_connector_b-2 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_41 , SW name: Body-2 ,  SW ref.type:2 (2)

link_7 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(0.0865180741340523,0.225665704646753,-0.0701072241948599)
cB = chrono.ChVectorD(-0.0134481779660203,0.22594913508665,-0.110109355135367)
dA = chrono.ChVectorD(1.11022302462516e-15,0.999985343981005,-0.00541403945223737)
dB = chrono.ChVectorD(-1.13959586670642e-15,-0.999985343981005,0.00541403945223878)
link_7.Initialize(body_15,body_41,False,cA,cB,dB)
link_7.SetDistance(-0.0005)
link_7.SetName("Distance5")
exported_items.append(link_7)

link_8 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.0865180741340523,0.225665704646753,-0.0701072241948599)
dA = chrono.ChVectorD(1.11022302462516e-15,0.999985343981005,-0.00541403945223737)
cB = chrono.ChVectorD(-0.0134481779660203,0.22594913508665,-0.110109355135367)
dB = chrono.ChVectorD(-1.13959586670642e-15,-0.999985343981005,0.00541403945223878)
link_8.SetFlipped(True)
link_8.Initialize(body_15,body_41,False,cA,cB,dA,dB)
link_8.SetName("Distance5")
exported_items.append(link_8)


# Mate constraint: Distance4 [MateDistanceDim] type:5 align:1 flip:False
#   Entity 0: C::E name: body_42 , SW name: Spibot-LEG-5/limb_body_connector_b-2 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_41 , SW name: Body-2 ,  SW ref.type:2 (2)

link_9 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(-0.00348192753591677,0.225665703840772,-0.070107237512559)
cB = chrono.ChVectorD(-0.0134481779660203,0.22594913508665,-0.110109355135367)
dA = chrono.ChVectorD(8.04911692853239e-16,0.999985343981005,-0.00541403945223737)
dB = chrono.ChVectorD(-1.13959586670642e-15,-0.999985343981005,0.00541403945223878)
link_9.Initialize(body_42,body_41,False,cA,cB,dB)
link_9.SetDistance(-0.0005)
link_9.SetName("Distance4")
exported_items.append(link_9)

link_10 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.00348192753591677,0.225665703840772,-0.070107237512559)
dA = chrono.ChVectorD(8.04911692853239e-16,0.999985343981005,-0.00541403945223737)
cB = chrono.ChVectorD(-0.0134481779660203,0.22594913508665,-0.110109355135367)
dB = chrono.ChVectorD(-1.13959586670642e-15,-0.999985343981005,0.00541403945223878)
link_10.SetFlipped(True)
link_10.Initialize(body_42,body_41,False,cA,cB,dA,dB)
link_10.SetName("Distance4")
exported_items.append(link_10)


# Mate constraint: Distance7 [MateDistanceDim] type:5 align:1 flip:False
#   Entity 0: C::E name: body_26 , SW name: Spibot-LEG-6/limb_body_connector_b-2 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_41 , SW name: Body-2 ,  SW ref.type:2 (2)

link_11 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(-0.0934819258819656,0.225665701140002,-0.0701072546419209)
cB = chrono.ChVectorD(-0.0134481779660203,0.22594913508665,-0.110109355135367)
dA = chrono.ChVectorD(2.4980018054066e-16,0.999985343981005,-0.0054140394522372)
dB = chrono.ChVectorD(-1.13959586670642e-15,-0.999985343981005,0.00541403945223878)
link_11.Initialize(body_26,body_41,False,cA,cB,dB)
link_11.SetDistance(-0.0005)
link_11.SetName("Distance7")
exported_items.append(link_11)

link_12 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.0934819258819656,0.225665701140002,-0.0701072546419209)
dA = chrono.ChVectorD(2.4980018054066e-16,0.999985343981005,-0.0054140394522372)
cB = chrono.ChVectorD(-0.0134481779660203,0.22594913508665,-0.110109355135367)
dB = chrono.ChVectorD(-1.13959586670642e-15,-0.999985343981005,0.00541403945223878)
link_12.SetFlipped(True)
link_12.Initialize(body_26,body_41,False,cA,cB,dA,dB)
link_12.SetName("Distance7")
exported_items.append(link_12)


# Mate constraint: Concentric1 [MateConcentric] type:1 align:1 flip:False
#   Entity 0: C::E name: body_41 , SW name: Body-2 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_36 , SW name: Spibot-LEG-1/limb_body_connector_b-2 ,  SW ref.type:2 (2)

link_13 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.103448173575691,0.245732280334699,-0.150217059561747)
dA = chrono.ChVectorD(-1.13959586670642e-15,-0.999985343981005,0.00541403945223878)
cB = chrono.ChVectorD(-0.103448177016935,0.205232872997366,-0.149997797922461)
dB = chrono.ChVectorD(-4.44089209850063e-16,0.999985343981005,-0.00541403945223998)
link_13.SetFlipped(True)
link_13.Initialize(body_41,body_36,False,cA,cB,dA,dB)
link_13.SetName("Concentric1")
exported_items.append(link_13)

link_14 = chrono.ChLinkMateGeneric()
link_14.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.103448173575691,0.245732280334699,-0.150217059561747)
cB = chrono.ChVectorD(-0.103448177016935,0.205232872997366,-0.149997797922461)
dA = chrono.ChVectorD(-1.13959586670642e-15,-0.999985343981005,0.00541403945223878)
dB = chrono.ChVectorD(-4.44089209850063e-16,0.999985343981005,-0.00541403945223998)
link_14.Initialize(body_41,body_36,False,cA,cB,dA,dB)
link_14.SetName("Concentric1")
exported_items.append(link_14)


# Mate constraint: Concentric2 [MateConcentric] type:1 align:1 flip:False
#   Entity 0: C::E name: body_41 , SW name: Body-2 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_2 , SW name: Spibot-LEG-2/limb_body_connector-1 ,  SW ref.type:2 (2)

link_15 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.0134481735756912,0.24573228038818,-0.150217049683652)
dA = chrono.ChVectorD(-1.13959586670642e-15,-0.999985343981005,0.00541403945223878)
cB = chrono.ChVectorD(-0.0134481735756913,0.246232273060171,-0.150219756703378)
dB = chrono.ChVectorD(-3.33066907387547e-16,0.999985343981005,-0.00541403945223867)
link_15.SetFlipped(True)
link_15.Initialize(body_41,body_2,False,cA,cB,dA,dB)
link_15.SetName("Concentric2")
exported_items.append(link_15)

link_16 = chrono.ChLinkMateGeneric()
link_16.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.0134481735756912,0.24573228038818,-0.150217049683652)
cB = chrono.ChVectorD(-0.0134481735756913,0.246232273060171,-0.150219756703378)
dA = chrono.ChVectorD(-1.13959586670642e-15,-0.999985343981005,0.00541403945223878)
dB = chrono.ChVectorD(-3.33066907387547e-16,0.999985343981005,-0.00541403945223867)
link_16.Initialize(body_41,body_2,False,cA,cB,dA,dB)
link_16.SetName("Concentric2")
exported_items.append(link_16)


# Mate constraint: Concentric3 [MateConcentric] type:1 align:1 flip:False
#   Entity 0: C::E name: body_41 , SW name: Body-2 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_16 , SW name: Spibot-LEG-4/limb_body_connector-1 ,  SW ref.type:2 (2)

link_17 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.0765518176436502,0.246165403597841,-0.0702182122870763)
dA = chrono.ChVectorD(-1.13959586670642e-15,-0.999985343981005,0.00541403945223878)
cB = chrono.ChVectorD(0.0765518176436503,0.246665396269831,-0.0702209193068024)
dB = chrono.ChVectorD(1.02695629777827e-15,0.999985343981005,-0.00541403945223862)
link_17.SetFlipped(True)
link_17.Initialize(body_41,body_16,False,cA,cB,dA,dB)
link_17.SetName("Concentric3")
exported_items.append(link_17)

link_18 = chrono.ChLinkMateGeneric()
link_18.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(0.0765518176436502,0.246165403597841,-0.0702182122870763)
cB = chrono.ChVectorD(0.0765518176436503,0.246665396269831,-0.0702209193068024)
dA = chrono.ChVectorD(-1.13959586670642e-15,-0.999985343981005,0.00541403945223878)
dB = chrono.ChVectorD(1.02695629777827e-15,0.999985343981005,-0.00541403945223862)
link_18.Initialize(body_41,body_16,False,cA,cB,dA,dB)
link_18.SetName("Concentric3")
exported_items.append(link_18)


# Mate constraint: Concentric4 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_41 , SW name: Body-2 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_22 , SW name: Spibot-LEG-3/limb_body_connector-1 ,  SW ref.type:1 (1)

link_19 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.0765518264243082,0.245732280441662,-0.150217039805556)
dA = chrono.ChVectorD(-1.13959586670642e-15,-0.999985343981005,0.00541403945223878)
cB = chrono.ChVectorD(0.0765518264243083,0.266231979993272,-0.150328027614327)
dB = chrono.ChVectorD(-1.38777878078145e-16,-0.999985343981005,0.00541403945223881)
link_19.Initialize(body_22,body_41,False,cB,cA,dB,dA)
link_19.SetName("Concentric4")
exported_items.append(link_19)

link_20 = chrono.ChLinkMateGeneric()
link_20.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(0.0765518264243082,0.245732280441662,-0.150217039805556)
cB = chrono.ChVectorD(0.0765518264243083,0.266231979993272,-0.150328027614327)
dA = chrono.ChVectorD(-1.13959586670642e-15,-0.999985343981005,0.00541403945223878)
dB = chrono.ChVectorD(-1.38777878078145e-16,-0.999985343981005,0.00541403945223881)
link_20.Initialize(body_22,body_41,False,cB,cA,dB,dA)
link_20.SetName("Concentric4")
exported_items.append(link_20)


# Mate constraint: Concentric5 [MateConcentric] type:1 align:1 flip:False
#   Entity 0: C::E name: body_41 , SW name: Body-2 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_49 , SW name: Spibot-LEG-5/limb_body_connector-1 ,  SW ref.type:2 (2)

link_21 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.0134481823563493,0.24616540354436,-0.0702182221651718)
dA = chrono.ChVectorD(-1.13959586670642e-15,-0.999985343981005,0.00541403945223878)
cB = chrono.ChVectorD(-0.0134481823563493,0.24666539621635,-0.0702209291848979)
dB = chrono.ChVectorD(9.15933995315754e-16,0.999985343981005,-0.00541403945223865)
link_21.SetFlipped(True)
link_21.Initialize(body_41,body_49,False,cA,cB,dA,dB)
link_21.SetName("Concentric5")
exported_items.append(link_21)

link_22 = chrono.ChLinkMateGeneric()
link_22.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.0134481823563493,0.24616540354436,-0.0702182221651718)
cB = chrono.ChVectorD(-0.0134481823563493,0.24666539621635,-0.0702209291848979)
dA = chrono.ChVectorD(-1.13959586670642e-15,-0.999985343981005,0.00541403945223878)
dB = chrono.ChVectorD(9.15933995315754e-16,0.999985343981005,-0.00541403945223865)
link_22.Initialize(body_41,body_49,False,cA,cB,dA,dB)
link_22.SetName("Concentric5")
exported_items.append(link_22)


# Mate constraint: Concentric6 [MateConcentric] type:1 align:1 flip:False
#   Entity 0: C::E name: body_41 , SW name: Body-2 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_25 , SW name: Spibot-LEG-6/limb_body_connector-1 ,  SW ref.type:2 (2)

link_23 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.103448182356349,0.246165403490878,-0.0702182320432673)
dA = chrono.ChVectorD(-1.13959586670642e-15,-0.999985343981005,0.00541403945223878)
cB = chrono.ChVectorD(-0.103448182356349,0.246665396162869,-0.0702209390629934)
dB = chrono.ChVectorD(2.77555756156289e-16,0.999985343981005,-0.00541403945223876)
link_23.SetFlipped(True)
link_23.Initialize(body_41,body_25,False,cA,cB,dA,dB)
link_23.SetName("Concentric6")
exported_items.append(link_23)

link_24 = chrono.ChLinkMateGeneric()
link_24.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.103448182356349,0.246165403490878,-0.0702182320432673)
cB = chrono.ChVectorD(-0.103448182356349,0.246665396162869,-0.0702209390629934)
dA = chrono.ChVectorD(-1.13959586670642e-15,-0.999985343981005,0.00541403945223878)
dB = chrono.ChVectorD(2.77555756156289e-16,0.999985343981005,-0.00541403945223876)
link_24.Initialize(body_41,body_25,False,cA,cB,dA,dB)
link_24.SetName("Concentric6")
exported_items.append(link_24)


# Mate constraint: Distance8 [MateDistanceDim] type:5 align:1 flip:False
#   Entity 0: C::E name: body_33 , SW name: Spibot-LEG-1/limb_body_connector-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_41 , SW name: Body-2 ,  SW ref.type:2 (2)

link_25 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(-0.113448173575691,0.24623227300669,-0.150219766581483)
cB = chrono.ChVectorD(-0.0134481779660202,0.24594884196627,-0.110217635924412)
dA = chrono.ChVectorD(3.60822483003176e-16,-0.999985343981005,0.00541403945223878)
dB = chrono.ChVectorD(1.13959586670642e-15,0.999985343981005,-0.00541403945223878)
link_25.Initialize(body_33,body_41,False,cA,cB,dB)
link_25.SetDistance(-0.000499999999999743)
link_25.SetName("Distance8")
exported_items.append(link_25)

link_26 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.113448173575691,0.24623227300669,-0.150219766581483)
dA = chrono.ChVectorD(3.60822483003176e-16,-0.999985343981005,0.00541403945223878)
cB = chrono.ChVectorD(-0.0134481779660202,0.24594884196627,-0.110217635924412)
dB = chrono.ChVectorD(1.13959586670642e-15,0.999985343981005,-0.00541403945223878)
link_26.SetFlipped(True)
link_26.Initialize(body_33,body_41,False,cA,cB,dA,dB)
link_26.SetName("Distance8")
exported_items.append(link_26)


# Mate constraint: Distance9 [MateDistanceDim] type:5 align:1 flip:False
#   Entity 0: C::E name: body_2 , SW name: Spibot-LEG-2/limb_body_connector-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_41 , SW name: Body-2 ,  SW ref.type:2 (2)

link_27 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(-0.0234481735756913,0.246232273060171,-0.150219756703387)
cB = chrono.ChVectorD(-0.0134481779660202,0.24594884196627,-0.110217635924412)
dA = chrono.ChVectorD(3.33066907387547e-16,-0.999985343981005,0.00541403945223867)
dB = chrono.ChVectorD(1.13959586670642e-15,0.999985343981005,-0.00541403945223878)
link_27.Initialize(body_2,body_41,False,cA,cB,dB)
link_27.SetDistance(-0.000499999999999993)
link_27.SetName("Distance9")
exported_items.append(link_27)

link_28 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.0234481735756913,0.246232273060171,-0.150219756703387)
dA = chrono.ChVectorD(3.33066907387547e-16,-0.999985343981005,0.00541403945223867)
cB = chrono.ChVectorD(-0.0134481779660202,0.24594884196627,-0.110217635924412)
dB = chrono.ChVectorD(1.13959586670642e-15,0.999985343981005,-0.00541403945223878)
link_28.SetFlipped(True)
link_28.Initialize(body_2,body_41,False,cA,cB,dA,dB)
link_28.SetName("Distance9")
exported_items.append(link_28)


# Mate constraint: Distance10 [MateDistanceDim] type:5 align:1 flip:False
#   Entity 0: C::E name: body_22 , SW name: Spibot-LEG-3/limb_body_connector-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_41 , SW name: Body-2 ,  SW ref.type:2 (2)

link_29 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(0.0665518264243083,0.246232273113652,-0.150219746825292)
cB = chrono.ChVectorD(-0.0134481779660202,0.24594884196627,-0.110217635924412)
dA = chrono.ChVectorD(-1.38777878078145e-16,-0.999985343981005,0.00541403945223881)
dB = chrono.ChVectorD(1.13959586670642e-15,0.999985343981005,-0.00541403945223878)
link_29.Initialize(body_22,body_41,False,cA,cB,dB)
link_29.SetDistance(-0.0005)
link_29.SetName("Distance10")
exported_items.append(link_29)

link_30 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.0665518264243083,0.246232273113652,-0.150219746825292)
dA = chrono.ChVectorD(-1.38777878078145e-16,-0.999985343981005,0.00541403945223881)
cB = chrono.ChVectorD(-0.0134481779660202,0.24594884196627,-0.110217635924412)
dB = chrono.ChVectorD(1.13959586670642e-15,0.999985343981005,-0.00541403945223878)
link_30.SetFlipped(True)
link_30.Initialize(body_22,body_41,False,cA,cB,dA,dB)
link_30.SetName("Distance10")
exported_items.append(link_30)


# Mate constraint: Distance11 [MateDistanceDim] type:5 align:1 flip:False
#   Entity 0: C::E name: body_16 , SW name: Spibot-LEG-4/limb_body_connector-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_41 , SW name: Body-2 ,  SW ref.type:2 (2)

link_31 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(0.0865518176436503,0.246665396269831,-0.0702209193067932)
cB = chrono.ChVectorD(-0.0134481779660202,0.24594884196627,-0.110217635924412)
dA = chrono.ChVectorD(-1.02695629777827e-15,-0.999985343981005,0.00541403945223862)
dB = chrono.ChVectorD(1.13959586670642e-15,0.999985343981005,-0.00541403945223878)
link_31.Initialize(body_16,body_41,False,cA,cB,dB)
link_31.SetDistance(-0.0005)
link_31.SetName("Distance11")
exported_items.append(link_31)

link_32 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.0865518176436503,0.246665396269831,-0.0702209193067932)
dA = chrono.ChVectorD(-1.02695629777827e-15,-0.999985343981005,0.00541403945223862)
cB = chrono.ChVectorD(-0.0134481779660202,0.24594884196627,-0.110217635924412)
dB = chrono.ChVectorD(1.13959586670642e-15,0.999985343981005,-0.00541403945223878)
link_32.SetFlipped(True)
link_32.Initialize(body_16,body_41,False,cA,cB,dA,dB)
link_32.SetName("Distance11")
exported_items.append(link_32)


# Mate constraint: Distance12 [MateDistanceDim] type:5 align:1 flip:False
#   Entity 0: C::E name: body_49 , SW name: Spibot-LEG-5/limb_body_connector-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_41 , SW name: Body-2 ,  SW ref.type:2 (2)

link_33 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(-0.00344818235634927,0.24666539621635,-0.0702209291848887)
cB = chrono.ChVectorD(-0.0134481779660202,0.24594884196627,-0.110217635924412)
dA = chrono.ChVectorD(-9.15933995315754e-16,-0.999985343981005,0.00541403945223865)
dB = chrono.ChVectorD(1.13959586670642e-15,0.999985343981005,-0.00541403945223878)
link_33.Initialize(body_49,body_41,False,cA,cB,dB)
link_33.SetDistance(-0.0005)
link_33.SetName("Distance12")
exported_items.append(link_33)

link_34 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.00344818235634927,0.24666539621635,-0.0702209291848887)
dA = chrono.ChVectorD(-9.15933995315754e-16,-0.999985343981005,0.00541403945223865)
cB = chrono.ChVectorD(-0.0134481779660202,0.24594884196627,-0.110217635924412)
dB = chrono.ChVectorD(1.13959586670642e-15,0.999985343981005,-0.00541403945223878)
link_34.SetFlipped(True)
link_34.Initialize(body_49,body_41,False,cA,cB,dA,dB)
link_34.SetName("Distance12")
exported_items.append(link_34)


# Mate constraint: Distance13 [MateDistanceDim] type:5 align:1 flip:False
#   Entity 0: C::E name: body_25 , SW name: Spibot-LEG-6/limb_body_connector-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_41 , SW name: Body-2 ,  SW ref.type:2 (2)

link_35 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(-0.0934481823563487,0.246665396162869,-0.0702209390629842)
cB = chrono.ChVectorD(-0.0134481779660202,0.24594884196627,-0.110217635924412)
dA = chrono.ChVectorD(-2.77555756156289e-16,-0.999985343981005,0.00541403945223876)
dB = chrono.ChVectorD(1.13959586670642e-15,0.999985343981005,-0.00541403945223878)
link_35.Initialize(body_25,body_41,False,cA,cB,dB)
link_35.SetDistance(-0.0005)
link_35.SetName("Distance13")
exported_items.append(link_35)

link_36 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.0934481823563487,0.246665396162869,-0.0702209390629842)
dA = chrono.ChVectorD(-2.77555756156289e-16,-0.999985343981005,0.00541403945223876)
cB = chrono.ChVectorD(-0.0134481779660202,0.24594884196627,-0.110217635924412)
dB = chrono.ChVectorD(1.13959586670642e-15,0.999985343981005,-0.00541403945223878)
link_36.SetFlipped(True)
link_36.Initialize(body_25,body_41,False,cA,cB,dA,dB)
link_36.SetName("Distance13")
exported_items.append(link_36)


# Mate constraint: Concentric3 [MateConcentric] type:1 align:1 flip:False
#   Entity 0: C::E name: body_3 , SW name: Spibot-LEG-2/upper_limb-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_7 , SW name: Spibot-LEG-2/lower_limb-1 ,  SW ref.type:2 (2)

link_1 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.015898173174471,0.254824476226496,-0.410270087107398)
dA = chrono.ChVectorD(1,4.94049245958195e-15,9.2015284280933e-13)
cB = chrono.ChVectorD(-0.00344817357545235,0.254824476178357,-0.410270086900487)
dB = chrono.ChVectorD(-1,-4.52415882534751e-15,-9.19098130935936e-13)
link_1.SetFlipped(True)
link_1.Initialize(body_3,body_7,False,cA,cB,dA,dB)
link_1.SetName("Concentric3")
exported_items.append(link_1)

link_2 = chrono.ChLinkMateGeneric()
link_2.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.015898173174471,0.254824476226496,-0.410270087107398)
cB = chrono.ChVectorD(-0.00344817357545235,0.254824476178357,-0.410270086900487)
dA = chrono.ChVectorD(1,4.94049245958195e-15,9.2015284280933e-13)
dB = chrono.ChVectorD(-1,-4.52415882534751e-15,-9.19098130935936e-13)
link_2.Initialize(body_3,body_7,False,cA,cB,dA,dB)
link_2.SetName("Concentric3")
exported_items.append(link_2)


# Mate constraint: Concentric4 [MateConcentric] type:1 align:1 flip:False
#   Entity 0: C::E name: body_7 , SW name: Spibot-LEG-2/lower_limb-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_5 , SW name: Spibot-LEG-2/Actuator_rod-1 ,  SW ref.type:2 (2)

link_3 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.00344817357545191,0.214825896055122,-0.410607115274806)
dA = chrono.ChVectorD(-1,-4.52415882534751e-15,-9.19098130935936e-13)
cB = chrono.ChVectorD(-0.0158981699230539,0.214825895561729,-0.41060710537659)
dB = chrono.ChVectorD(1,4.05231403988182e-15,9.19930798204405e-13)
link_3.SetFlipped(True)
link_3.Initialize(body_7,body_5,False,cA,cB,dA,dB)
link_3.SetName("Concentric4")
exported_items.append(link_3)

link_4 = chrono.ChLinkMateGeneric()
link_4.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.00344817357545191,0.214825896055122,-0.410607115274806)
cB = chrono.ChVectorD(-0.0158981699230539,0.214825895561729,-0.41060710537659)
dA = chrono.ChVectorD(-1,-4.52415882534751e-15,-9.19098130935936e-13)
dB = chrono.ChVectorD(1,4.05231403988182e-15,9.19930798204405e-13)
link_4.Initialize(body_7,body_5,False,cA,cB,dA,dB)
link_4.SetName("Concentric4")
exported_items.append(link_4)


# Mate constraint: Concentric6 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_5 , SW name: Spibot-LEG-2/Actuator_rod-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_1 , SW name: Spibot-LEG-2/Actuator_body-1 ,  SW ref.type:2 (2)

link_5 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.0134981699231411,0.209440161301397,-0.315759892099248)
dA = chrono.ChVectorD(-9.18431997121161e-13,-0.0566919395824439,0.998391718708835)
cB = chrono.ChVectorD(-0.0134981735755066,0.211444934364122,-0.351065633019892)
dB = chrono.ChVectorD(-9.18320974818698e-13,-0.0566919395824439,0.998391718708835)
link_5.Initialize(body_5,body_1,False,cA,cB,dA,dB)
link_5.SetName("Concentric6")
exported_items.append(link_5)

link_6 = chrono.ChLinkMateGeneric()
link_6.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.0134981699231411,0.209440161301397,-0.315759892099248)
cB = chrono.ChVectorD(-0.0134981735755066,0.211444934364122,-0.351065633019892)
dA = chrono.ChVectorD(-9.18431997121161e-13,-0.0566919395824439,0.998391718708835)
dB = chrono.ChVectorD(-9.18320974818698e-13,-0.0566919395824439,0.998391718708835)
link_6.Initialize(body_5,body_1,False,cA,cB,dA,dB)
link_6.SetName("Concentric6")
exported_items.append(link_6)


# Mate constraint: Concentric11 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_8 , SW name: Spibot-LEG-2/Actuator_rod_b-2 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_4 , SW name: Spibot-LEG-2/Actuator_body_b-2 ,  SW ref.type:2 (2)

link_7 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.0133481733176131,0.220082305293508,-0.20014749354975)
dA = chrono.ChVectorD(-9.06663633060134e-13,-0.162544746575591,0.986701173284332)
cB = chrono.ChVectorD(-0.0133481733175858,0.224877131570885,-0.229253698537939)
dB = chrono.ChVectorD(-9.06719144211365e-13,-0.16254474657559,0.986701173284332)
link_7.Initialize(body_8,body_4,False,cA,cB,dA,dB)
link_7.SetName("Concentric11")
exported_items.append(link_7)

link_8 = chrono.ChLinkMateGeneric()
link_8.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.0133481733176131,0.220082305293508,-0.20014749354975)
cB = chrono.ChVectorD(-0.0133481733175858,0.224877131570885,-0.229253698537939)
dA = chrono.ChVectorD(-9.06663633060134e-13,-0.162544746575591,0.986701173284332)
dB = chrono.ChVectorD(-9.06719144211365e-13,-0.16254474657559,0.986701173284332)
link_8.Initialize(body_8,body_4,False,cA,cB,dA,dB)
link_8.SetName("Concentric11")
exported_items.append(link_8)


# Mate constraint: Concentric12 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_3 , SW name: Spibot-LEG-2/upper_limb-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_2 , SW name: Spibot-LEG-2/limb_body_connector-1 ,  SW ref.type:2 (2)

link_9 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.015898173174655,0.255907284266685,-0.210273018312007)
dA = chrono.ChVectorD(1,4.94049245958195e-15,9.2015284280933e-13)
cB = chrono.ChVectorD(-0.023448173575636,0.255907284132847,-0.21027301773677)
dB = chrono.ChVectorD(1,5.24580379135386e-15,9.20430398565486e-13)
link_9.Initialize(body_3,body_2,False,cA,cB,dA,dB)
link_9.SetName("Concentric12")
exported_items.append(link_9)

link_10 = chrono.ChLinkMateGeneric()
link_10.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.015898173174655,0.255907284266685,-0.210273018312007)
cB = chrono.ChVectorD(-0.023448173575636,0.255907284132847,-0.21027301773677)
dA = chrono.ChVectorD(1,4.94049245958195e-15,9.2015284280933e-13)
dB = chrono.ChVectorD(1,5.24580379135386e-15,9.20430398565486e-13)
link_10.Initialize(body_3,body_2,False,cA,cB,dA,dB)
link_10.SetName("Concentric12")
exported_items.append(link_10)


# Mate constraint: Concentric13 [MateConcentric] type:1 align:1 flip:False
#   Entity 0: C::E name: body_4 , SW name: Spibot-LEG-2/Actuator_body_b-2 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_6 , SW name: Spibot-LEG-2/limb_body_connector_b-2 ,  SW ref.type:2 (2)

link_11 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.0209481733176402,0.21512444677635,-0.170051628140886)
dA = chrono.ChVectorD(1,5.63438184997267e-15,9.19764264750711e-13)
cB = chrono.ChVectorD(-0.00341443360660354,0.215124446693415,-0.170051628728314)
dB = chrono.ChVectorD(-1,-5.07927033766009e-15,-9.20097331658098e-13)
link_11.SetFlipped(True)
link_11.Initialize(body_4,body_6,False,cA,cB,dA,dB)
link_11.SetName("Concentric13")
exported_items.append(link_11)

link_12 = chrono.ChLinkMateGeneric()
link_12.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.0209481733176402,0.21512444677635,-0.170051628140886)
cB = chrono.ChVectorD(-0.00341443360660354,0.215124446693415,-0.170051628728314)
dA = chrono.ChVectorD(1,5.63438184997267e-15,9.19764264750711e-13)
dB = chrono.ChVectorD(-1,-5.07927033766009e-15,-9.20097331658098e-13)
link_12.Initialize(body_4,body_6,False,cA,cB,dA,dB)
link_12.SetName("Concentric13")
exported_items.append(link_12)


# Mate constraint: Concentric17 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_2 , SW name: Spibot-LEG-2/limb_body_connector-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_6 , SW name: Spibot-LEG-2/limb_body_connector_b-2 ,  SW ref.type:2 (2)

link_13 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.0134481735756913,0.246232273060171,-0.150219756703378)
dA = chrono.ChVectorD(-3.05311331771918e-16,0.999985343981006,-0.00541403945223862)
cB = chrono.ChVectorD(-0.0134481735756913,0.20523287404265,-0.14999778145418)
dB = chrono.ChVectorD(-1.66533453693773e-16,0.999985343981005,-0.00541403945224009)
link_13.Initialize(body_2,body_6,False,cA,cB,dA,dB)
link_13.SetName("Concentric17")
exported_items.append(link_13)

link_14 = chrono.ChLinkMateGeneric()
link_14.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.0134481735756913,0.246232273060171,-0.150219756703378)
cB = chrono.ChVectorD(-0.0134481735756913,0.20523287404265,-0.14999778145418)
dA = chrono.ChVectorD(-3.05311331771918e-16,0.999985343981006,-0.00541403945223862)
dB = chrono.ChVectorD(-1.66533453693773e-16,0.999985343981005,-0.00541403945224009)
link_14.Initialize(body_2,body_6,False,cA,cB,dA,dB)
link_14.SetName("Concentric17")
exported_items.append(link_14)


# Mate constraint: Parallel14 [MateParallel] type:3 align:0 flip:False
#   Entity 0: C::E name: body_3 , SW name: Spibot-LEG-2/upper_limb-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_5 , SW name: Spibot-LEG-2/Actuator_rod-1 ,  SW ref.type:2 (2)

link_15 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.0158981731745631,0.255365880246591,-0.310271552709703)
dA = chrono.ChVectorD(-1,-4.94049245958195e-15,-9.2015284280933e-13)
cB = chrono.ChVectorD(-0.0158981699230539,0.214825895561729,-0.41060710537659)
dB = chrono.ChVectorD(-1,-4.05231403988182e-15,-9.19930798204405e-13)
link_15.Initialize(body_3,body_5,False,cA,cB,dA,dB)
link_15.SetName("Parallel14")
exported_items.append(link_15)


# Mate constraint: Parallel15 [MateParallel] type:3 align:0 flip:False
#   Entity 0: C::E name: body_3 , SW name: Spibot-LEG-2/upper_limb-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_8 , SW name: Spibot-LEG-2/Actuator_rod_b-2 ,  SW ref.type:2 (2)

link_16 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.0109981731745987,0.206909581229235,-0.271194294697479)
dA = chrono.ChVectorD(-1,-4.94049245958195e-15,-9.2015284280933e-13)
cB = chrono.ChVectorD(-0.0157481733175633,0.229022266355166,-0.25441605808039)
dB = chrono.ChVectorD(-1,-5.27355936696949e-15,-9.19653242448248e-13)
link_16.Initialize(body_3,body_8,False,cA,cB,dA,dB)
link_16.SetName("Parallel15")
exported_items.append(link_16)


# Mate constraint: Distance10 [MateDistanceDim] type:5 align:1 flip:False
#   Entity 0: C::E name: body_3 , SW name: Spibot-LEG-2/upper_limb-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_7 , SW name: Spibot-LEG-2/lower_limb-1 ,  SW ref.type:2 (2)

link_17 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(-0.0158981731745631,0.255365880246591,-0.310271552709703)
cB = chrono.ChVectorD(-0.0159481735754432,0.264829346839508,-0.420265213865857)
dA = chrono.ChVectorD(-1,-4.94049245958195e-15,-9.2015284280933e-13)
dB = chrono.ChVectorD(1,4.30211422042248e-15,9.19042619784705e-13)
link_17.Initialize(body_3,body_7,False,cA,cB,dB)
link_17.SetDistance(0)
link_17.SetName("Distance10")
exported_items.append(link_17)

link_18 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.0158981731745631,0.255365880246591,-0.310271552709703)
dA = chrono.ChVectorD(-1,-4.94049245958195e-15,-9.2015284280933e-13)
cB = chrono.ChVectorD(-0.0159481735754432,0.264829346839508,-0.420265213865857)
dB = chrono.ChVectorD(1,4.30211422042248e-15,9.19042619784705e-13)
link_18.SetFlipped(True)
link_18.Initialize(body_3,body_7,False,cA,cB,dA,dB)
link_18.SetName("Distance10")
exported_items.append(link_18)


# Mate constraint: Distance11 [MateDistanceDim] type:5 align:1 flip:False
#   Entity 0: C::E name: body_5 , SW name: Spibot-LEG-2/Actuator_rod-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_7 , SW name: Spibot-LEG-2/lower_limb-1 ,  SW ref.type:2 (2)

link_19 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(-0.0158981699230539,0.214825895561729,-0.41060710537659)
cB = chrono.ChVectorD(-0.0159481735754432,0.264829346839508,-0.420265213865857)
dA = chrono.ChVectorD(-1,-4.05231403988182e-15,-9.19930798204405e-13)
dB = chrono.ChVectorD(1,4.30211422042248e-15,9.19042619784705e-13)
link_19.Initialize(body_5,body_7,False,cA,cB,dB)
link_19.SetDistance(0)
link_19.SetName("Distance11")
exported_items.append(link_19)

link_20 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.0158981699230539,0.214825895561729,-0.41060710537659)
dA = chrono.ChVectorD(-1,-4.05231403988182e-15,-9.19930798204405e-13)
cB = chrono.ChVectorD(-0.0159481735754432,0.264829346839508,-0.420265213865857)
dB = chrono.ChVectorD(1,4.30211422042248e-15,9.19042619784705e-13)
link_20.SetFlipped(True)
link_20.Initialize(body_5,body_7,False,cA,cB,dA,dB)
link_20.SetName("Distance11")
exported_items.append(link_20)


# Mate constraint: Distance12 [MateDistanceDim] type:5 align:1 flip:False
#   Entity 0: C::E name: body_3 , SW name: Spibot-LEG-2/upper_limb-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_2 , SW name: Spibot-LEG-2/limb_body_connector-1 ,  SW ref.type:2 (2)

link_21 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(-0.0158981731745631,0.255365880246591,-0.310271552709703)
cB = chrono.ChVectorD(-0.0159481735756268,0.245853290298514,-0.220218730782051)
dA = chrono.ChVectorD(-1,-4.94049245958195e-15,-9.2015284280933e-13)
dB = chrono.ChVectorD(1,5.27355936696949e-15,9.2015284280933e-13)
link_21.Initialize(body_3,body_2,False,cA,cB,dB)
link_21.SetDistance(0)
link_21.SetName("Distance12")
exported_items.append(link_21)

link_22 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.0158981731745631,0.255365880246591,-0.310271552709703)
dA = chrono.ChVectorD(-1,-4.94049245958195e-15,-9.2015284280933e-13)
cB = chrono.ChVectorD(-0.0159481735756268,0.245853290298514,-0.220218730782051)
dB = chrono.ChVectorD(1,5.27355936696949e-15,9.2015284280933e-13)
link_22.SetFlipped(True)
link_22.Initialize(body_3,body_2,False,cA,cB,dA,dB)
link_22.SetName("Distance12")
exported_items.append(link_22)


# Mate constraint: Distance13 [MateDistanceDim] type:5 align:1 flip:True
#   Entity 0: C::E name: body_4 , SW name: Spibot-LEG-2/Actuator_body_b-2 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_3 , SW name: Spibot-LEG-2/upper_limb-1 ,  SW ref.type:2 (2)

link_23 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(-0.0109481733176402,0.21512444677635,-0.170051628140877)
cB = chrono.ChVectorD(-0.0109981731745987,0.206909581229235,-0.271194294697479)
dA = chrono.ChVectorD(1,5.63438184997267e-15,9.19764264750711e-13)
dB = chrono.ChVectorD(-1,-4.94049245958195e-15,-9.2015284280933e-13)
link_23.Initialize(body_4,body_3,False,cA,cB,dB)
link_23.SetDistance(0)
link_23.SetName("Distance13")
exported_items.append(link_23)

link_24 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.0109481733176402,0.21512444677635,-0.170051628140877)
dA = chrono.ChVectorD(1,5.63438184997267e-15,9.19764264750711e-13)
cB = chrono.ChVectorD(-0.0109981731745987,0.206909581229235,-0.271194294697479)
dB = chrono.ChVectorD(-1,-4.94049245958195e-15,-9.2015284280933e-13)
link_24.SetFlipped(True)
link_24.Initialize(body_4,body_3,False,cA,cB,dA,dB)
link_24.SetName("Distance13")
exported_items.append(link_24)


# Mate constraint: Concentric21 [MateConcentric] type:1 align:1 flip:False
#   Entity 0: C::E name: body_3 , SW name: Spibot-LEG-2/upper_limb-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_1 , SW name: Spibot-LEG-2/Actuator_body-1 ,  SW ref.type:2 (2)

link_25 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.00849817317459878,0.206909581229235,-0.271194294697477)
dA = chrono.ChVectorD(-1,-4.94049245958195e-15,-9.2015284280933e-13)
cB = chrono.ChVectorD(-0.02109817357558,0.206909579197526,-0.271194295523193)
dB = chrono.ChVectorD(1,4.66293670342566e-15,9.19930798204405e-13)
link_25.SetFlipped(True)
link_25.Initialize(body_3,body_1,False,cA,cB,dA,dB)
link_25.SetName("Concentric21")
exported_items.append(link_25)

link_26 = chrono.ChLinkMateGeneric()
link_26.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.00849817317459878,0.206909581229235,-0.271194294697477)
cB = chrono.ChVectorD(-0.02109817357558,0.206909579197526,-0.271194295523193)
dA = chrono.ChVectorD(-1,-4.94049245958195e-15,-9.2015284280933e-13)
dB = chrono.ChVectorD(1,4.66293670342566e-15,9.19930798204405e-13)
link_26.Initialize(body_3,body_1,False,cA,cB,dA,dB)
link_26.SetName("Concentric21")
exported_items.append(link_26)


# Mate constraint: Concentric22 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_3 , SW name: Spibot-LEG-2/upper_limb-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_8 , SW name: Spibot-LEG-2/Actuator_rod_b-2 ,  SW ref.type:2 (2)

link_27 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.00849817317461432,0.22902226632037,-0.254416058874727)
dA = chrono.ChVectorD(-1,-4.94049245958195e-15,-9.2015284280933e-13)
cB = chrono.ChVectorD(-0.0109481733175634,0.229022266355166,-0.254416058080386)
dB = chrono.ChVectorD(-1,-5.27355936696949e-15,-9.19653242448248e-13)
link_27.Initialize(body_3,body_8,False,cA,cB,dA,dB)
link_27.SetName("Concentric22")
exported_items.append(link_27)

link_28 = chrono.ChLinkMateGeneric()
link_28.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.00849817317461432,0.22902226632037,-0.254416058874727)
cB = chrono.ChVectorD(-0.0109481733175634,0.229022266355166,-0.254416058080386)
dA = chrono.ChVectorD(-1,-4.94049245958195e-15,-9.2015284280933e-13)
dB = chrono.ChVectorD(-1,-5.27355936696949e-15,-9.19653242448248e-13)
link_28.Initialize(body_3,body_8,False,cA,cB,dA,dB)
link_28.SetName("Concentric22")
exported_items.append(link_28)


# Mate constraint: Concentric3 [MateConcentric] type:1 align:1 flip:False
#   Entity 0: C::E name: body_9 , SW name: Spibot-LEG-4/upper_limb-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_12 , SW name: Spibot-LEG-4/lower_limb-1 ,  SW ref.type:2 (2)

link_1 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.0790018173866519,0.258072898870807,0.18972113060065)
dA = chrono.ChVectorD(-1,-3.63598040564739e-15,-9.2059693201918e-13)
cB = chrono.ChVectorD(0.0665518155713546,0.25807289829727,0.189721129754239)
dB = chrono.ChVectorD(1,3.52495810318487e-15,9.19153642087167e-13)
link_1.SetFlipped(True)
link_1.Initialize(body_9,body_12,False,cA,cB,dA,dB)
link_1.SetName("Concentric3")
exported_items.append(link_1)

link_2 = chrono.ChLinkMateGeneric()
link_2.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(0.0790018173866519,0.258072898870807,0.18972113060065)
cB = chrono.ChVectorD(0.0665518155713546,0.25807289829727,0.189721129754239)
dA = chrono.ChVectorD(-1,-3.63598040564739e-15,-9.2059693201918e-13)
dB = chrono.ChVectorD(1,3.52495810318487e-15,9.19153642087167e-13)
link_2.Initialize(body_9,body_12,False,cA,cB,dA,dB)
link_2.SetName("Concentric3")
exported_items.append(link_2)


# Mate constraint: Concentric4 [MateConcentric] type:1 align:1 flip:False
#   Entity 0: C::E name: body_12 , SW name: Spibot-LEG-4/lower_limb-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_14 , SW name: Spibot-LEG-4/Actuator_rod-1 ,  SW ref.type:2 (2)

link_3 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.0665518155713545,0.218074008802217,0.190019188745964)
dA = chrono.ChVectorD(1,3.52495810318487e-15,9.19153642087167e-13)
cB = chrono.ChVectorD(0.0790018173866497,0.218074009691072,0.190019192404899)
dB = chrono.ChVectorD(-1,-3.69149155687865e-15,-9.19153642087167e-13)
link_3.SetFlipped(True)
link_3.Initialize(body_12,body_14,False,cA,cB,dA,dB)
link_3.SetName("Concentric4")
exported_items.append(link_3)

link_4 = chrono.ChLinkMateGeneric()
link_4.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(0.0665518155713545,0.218074008802217,0.190019188745964)
cB = chrono.ChVectorD(0.0790018173866497,0.218074009691072,0.190019192404899)
dA = chrono.ChVectorD(1,3.52495810318487e-15,9.19153642087167e-13)
dB = chrono.ChVectorD(-1,-3.69149155687865e-15,-9.19153642087167e-13)
link_4.Initialize(body_12,body_14,False,cA,cB,dA,dB)
link_4.SetName("Concentric4")
exported_items.append(link_4)


# Mate constraint: Concentric6 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_14 , SW name: Spibot-LEG-4/Actuator_rod-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_13 , SW name: Spibot-LEG-4/Actuator_body-1 ,  SW ref.type:2 (2)

link_5 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.0766018173867368,0.21164417569,0.0952370356731641)
dA = chrono.ChVectorD(9.17432796398998e-13,-0.0676824631691751,-0.997706912965603)
cB = chrono.ChVectorD(0.0766018173867066,0.214069508902338,0.130988862644155)
dB = chrono.ChVectorD(9.17432796398998e-13,-0.0676824631691751,-0.997706912965603)
link_5.Initialize(body_14,body_13,False,cA,cB,dA,dB)
link_5.SetName("Concentric6")
exported_items.append(link_5)

link_6 = chrono.ChLinkMateGeneric()
link_6.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(0.0766018173867368,0.21164417569,0.0952370356731641)
cB = chrono.ChVectorD(0.0766018173867066,0.214069508902338,0.130988862644155)
dA = chrono.ChVectorD(9.17432796398998e-13,-0.0676824631691751,-0.997706912965603)
dB = chrono.ChVectorD(9.17432796398998e-13,-0.0676824631691751,-0.997706912965603)
link_6.Initialize(body_14,body_13,False,cA,cB,dA,dB)
link_6.SetName("Concentric6")
exported_items.append(link_6)


# Mate constraint: Concentric11 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_10 , SW name: Spibot-LEG-4/Actuator_rod_b-2 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_11 , SW name: Spibot-LEG-4/Actuator_body_b-2 ,  SW ref.type:2 (2)

link_7 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.0764518176436041,0.221057574784869,-0.0200129592431845)
dA = chrono.ChVectorD(9.06275055001515e-13,-0.173219137550485,-0.984883308004693)
cB = chrono.ChVectorD(0.0764518176435777,0.226167279584679,0.00903962142041226)
dB = chrono.ChVectorD(9.06663633060134e-13,-0.173219137550485,-0.984883308004693)
link_7.Initialize(body_10,body_11,False,cA,cB,dA,dB)
link_7.SetName("Concentric11")
exported_items.append(link_7)

link_8 = chrono.ChLinkMateGeneric()
link_8.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(0.0764518176436041,0.221057574784869,-0.0200129592431845)
cB = chrono.ChVectorD(0.0764518176435777,0.226167279584679,0.00903962142041226)
dA = chrono.ChVectorD(9.06275055001515e-13,-0.173219137550485,-0.984883308004693)
dB = chrono.ChVectorD(9.06663633060134e-13,-0.173219137550485,-0.984883308004693)
link_8.Initialize(body_10,body_11,False,cA,cB,dA,dB)
link_8.SetName("Concentric11")
exported_items.append(link_8)


# Mate constraint: Concentric12 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_9 , SW name: Spibot-LEG-4/upper_limb-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_16 , SW name: Spibot-LEG-4/limb_body_connector-1 ,  SW ref.type:2 (2)

link_9 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.079001817386836,0.256990091853549,-0.0102759382002788)
dA = chrono.ChVectorD(-1,-3.63598040564739e-15,-9.2059693201918e-13)
cB = chrono.ChVectorD(0.0865518176435951,0.256990092076775,-0.0102759390624553)
dB = chrono.ChVectorD(-1,-3.91353616180368e-15,-9.2015284280933e-13)
link_9.Initialize(body_9,body_16,False,cA,cB,dA,dB)
link_9.SetName("Concentric12")
exported_items.append(link_9)

link_10 = chrono.ChLinkMateGeneric()
link_10.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(0.079001817386836,0.256990091853549,-0.0102759382002788)
cB = chrono.ChVectorD(0.0865518176435951,0.256990092076775,-0.0102759390624553)
dA = chrono.ChVectorD(-1,-3.63598040564739e-15,-9.2059693201918e-13)
dB = chrono.ChVectorD(-1,-3.91353616180368e-15,-9.2015284280933e-13)
link_10.Initialize(body_9,body_16,False,cA,cB,dA,dB)
link_10.SetName("Concentric12")
exported_items.append(link_10)


# Mate constraint: Concentric13 [MateConcentric] type:1 align:1 flip:False
#   Entity 0: C::E name: body_11 , SW name: Spibot-LEG-4/Actuator_body_b-2 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_15 , SW name: Spibot-LEG-4/limb_body_connector_b-2 ,  SW ref.type:2 (2)

link_11 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.0840518176436321,0.21577413133165,-0.0500533770598623)
dA = chrono.ChVectorD(-1,-3.88578058618805e-15,-9.19653242448248e-13)
cB = chrono.ChVectorD(0.066518074134034,0.215774131995988,-0.0500533769207358)
dB = chrono.ChVectorD(1,3.88578058618805e-15,9.20430398565486e-13)
link_11.SetFlipped(True)
link_11.Initialize(body_11,body_15,False,cA,cB,dA,dB)
link_11.SetName("Concentric13")
exported_items.append(link_11)

link_12 = chrono.ChLinkMateGeneric()
link_12.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(0.0840518176436321,0.21577413133165,-0.0500533770598623)
cB = chrono.ChVectorD(0.066518074134034,0.215774131995988,-0.0500533769207358)
dA = chrono.ChVectorD(-1,-3.88578058618805e-15,-9.19653242448248e-13)
dB = chrono.ChVectorD(1,3.88578058618805e-15,9.20430398565486e-13)
link_12.Initialize(body_11,body_15,False,cA,cB,dA,dB)
link_12.SetName("Concentric13")
exported_items.append(link_12)


# Mate constraint: Concentric17 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_16 , SW name: Spibot-LEG-4/limb_body_connector-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_15 , SW name: Spibot-LEG-4/limb_body_connector_b-2 ,  SW ref.type:2 (2)

link_13 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.0765518176436503,0.246665396269831,-0.0702209193068024)
dA = chrono.ChVectorD(9.99200722162641e-16,0.999985343981005,-0.00541403945223859)
cB = chrono.ChVectorD(0.0765518141031217,0.205665997767133,-0.0699989434058243)
dB = chrono.ChVectorD(1.11022302462516e-15,0.999985343981005,-0.00541403945223737)
link_13.Initialize(body_16,body_15,False,cA,cB,dA,dB)
link_13.SetName("Concentric17")
exported_items.append(link_13)

link_14 = chrono.ChLinkMateGeneric()
link_14.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(0.0765518176436503,0.246665396269831,-0.0702209193068024)
cB = chrono.ChVectorD(0.0765518141031217,0.205665997767133,-0.0699989434058243)
dA = chrono.ChVectorD(9.99200722162641e-16,0.999985343981005,-0.00541403945223859)
dB = chrono.ChVectorD(1.11022302462516e-15,0.999985343981005,-0.00541403945223737)
link_14.Initialize(body_16,body_15,False,cA,cB,dA,dB)
link_14.SetName("Concentric17")
exported_items.append(link_14)


# Mate constraint: Parallel14 [MateParallel] type:3 align:0 flip:False
#   Entity 0: C::E name: body_9 , SW name: Spibot-LEG-4/upper_limb-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_14 , SW name: Spibot-LEG-4/Actuator_rod-1 ,  SW ref.type:2 (2)

link_15 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.0790018173867441,0.257531495362178,0.0897225962001856)
dA = chrono.ChVectorD(1,3.63598040564739e-15,9.2059693201918e-13)
cB = chrono.ChVectorD(0.0790018173866497,0.218074009691072,0.190019192404899)
dB = chrono.ChVectorD(1,3.69149155687865e-15,9.19153642087167e-13)
link_15.Initialize(body_9,body_14,False,cA,cB,dA,dB)
link_15.SetName("Parallel14")
exported_items.append(link_15)


# Mate constraint: Parallel15 [MateParallel] type:3 align:0 flip:False
#   Entity 0: C::E name: body_9 , SW name: Spibot-LEG-4/upper_limb-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_10 , SW name: Spibot-LEG-4/Actuator_rod_b-2 ,  SW ref.type:2 (2)

link_16 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.0741018173867797,0.208654911737508,0.0511723098018492)
dA = chrono.ChVectorD(1,3.63598040564739e-15,9.2059693201918e-13)
cB = chrono.ChVectorD(0.0788518176435542,0.230584627350146,0.0341556226970758)
dB = chrono.ChVectorD(1,3.91353616180368e-15,9.19486708994555e-13)
link_16.Initialize(body_9,body_10,False,cA,cB,dA,dB)
link_16.SetName("Parallel15")
exported_items.append(link_16)


# Mate constraint: Distance10 [MateDistanceDim] type:5 align:1 flip:False
#   Entity 0: C::E name: body_9 , SW name: Spibot-LEG-4/upper_limb-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_12 , SW name: Spibot-LEG-4/lower_limb-1 ,  SW ref.type:2 (2)

link_17 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(0.0790018173867441,0.257531495362178,0.0897225962001856)
cB = chrono.ChVectorD(0.0790518155713453,0.268068026306278,0.199725999372768)
dA = chrono.ChVectorD(1,3.63598040564739e-15,9.2059693201918e-13)
dB = chrono.ChVectorD(-1,-3.7470027081099e-15,-9.19153642087167e-13)
link_17.Initialize(body_9,body_12,False,cA,cB,dB)
link_17.SetDistance(0)
link_17.SetName("Distance10")
exported_items.append(link_17)

link_18 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.0790018173867441,0.257531495362178,0.0897225962001856)
dA = chrono.ChVectorD(1,3.63598040564739e-15,9.2059693201918e-13)
cB = chrono.ChVectorD(0.0790518155713453,0.268068026306278,0.199725999372768)
dB = chrono.ChVectorD(-1,-3.7470027081099e-15,-9.19153642087167e-13)
link_18.SetFlipped(True)
link_18.Initialize(body_9,body_12,False,cA,cB,dA,dB)
link_18.SetName("Distance10")
exported_items.append(link_18)


# Mate constraint: Distance11 [MateDistanceDim] type:5 align:1 flip:False
#   Entity 0: C::E name: body_14 , SW name: Spibot-LEG-4/Actuator_rod-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_12 , SW name: Spibot-LEG-4/lower_limb-1 ,  SW ref.type:2 (2)

link_19 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(0.0790018173866497,0.218074009691072,0.190019192404899)
cB = chrono.ChVectorD(0.0790518155713453,0.268068026306278,0.199725999372768)
dA = chrono.ChVectorD(1,3.69149155687865e-15,9.19153642087167e-13)
dB = chrono.ChVectorD(-1,-3.7470027081099e-15,-9.19153642087167e-13)
link_19.Initialize(body_14,body_12,False,cA,cB,dB)
link_19.SetDistance(0)
link_19.SetName("Distance11")
exported_items.append(link_19)

link_20 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.0790018173866497,0.218074009691072,0.190019192404899)
dA = chrono.ChVectorD(1,3.69149155687865e-15,9.19153642087167e-13)
cB = chrono.ChVectorD(0.0790518155713453,0.268068026306278,0.199725999372768)
dB = chrono.ChVectorD(-1,-3.7470027081099e-15,-9.19153642087167e-13)
link_20.SetFlipped(True)
link_20.Initialize(body_14,body_12,False,cA,cB,dA,dB)
link_20.SetName("Distance11")
exported_items.append(link_20)


# Mate constraint: Distance12 [MateDistanceDim] type:5 align:1 flip:False
#   Entity 0: C::E name: body_9 , SW name: Spibot-LEG-4/upper_limb-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_16 , SW name: Spibot-LEG-4/limb_body_connector-1 ,  SW ref.type:2 (2)

link_21 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(0.0790018173867441,0.257531495362178,0.0897225962001856)
cB = chrono.ChVectorD(0.0790518176435858,0.247044379031488,-0.000221945228129794)
dA = chrono.ChVectorD(1,3.63598040564739e-15,9.2059693201918e-13)
dB = chrono.ChVectorD(-1,-3.88578058618805e-15,-9.19930798204405e-13)
link_21.Initialize(body_9,body_16,False,cA,cB,dB)
link_21.SetDistance(0)
link_21.SetName("Distance12")
exported_items.append(link_21)

link_22 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.0790018173867441,0.257531495362178,0.0897225962001856)
dA = chrono.ChVectorD(1,3.63598040564739e-15,9.2059693201918e-13)
cB = chrono.ChVectorD(0.0790518176435858,0.247044379031488,-0.000221945228129794)
dB = chrono.ChVectorD(-1,-3.88578058618805e-15,-9.19930798204405e-13)
link_22.SetFlipped(True)
link_22.Initialize(body_9,body_16,False,cA,cB,dA,dB)
link_22.SetName("Distance12")
exported_items.append(link_22)


# Mate constraint: Distance13 [MateDistanceDim] type:5 align:1 flip:True
#   Entity 0: C::E name: body_11 , SW name: Spibot-LEG-4/Actuator_body_b-2 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_9 , SW name: Spibot-LEG-4/upper_limb-1 ,  SW ref.type:2 (2)

link_23 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(0.0740518176436319,0.21577413133165,-0.0500533770598716)
cB = chrono.ChVectorD(0.0741018173867797,0.208654911737508,0.0511723098018492)
dA = chrono.ChVectorD(-1,-3.88578058618805e-15,-9.19653242448248e-13)
dB = chrono.ChVectorD(1,3.63598040564739e-15,9.2059693201918e-13)
link_23.Initialize(body_11,body_9,False,cA,cB,dB)
link_23.SetDistance(0)
link_23.SetName("Distance13")
exported_items.append(link_23)

link_24 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.0740518176436319,0.21577413133165,-0.0500533770598716)
dA = chrono.ChVectorD(-1,-3.88578058618805e-15,-9.19653242448248e-13)
cB = chrono.ChVectorD(0.0741018173867797,0.208654911737508,0.0511723098018492)
dB = chrono.ChVectorD(1,3.63598040564739e-15,9.2059693201918e-13)
link_24.SetFlipped(True)
link_24.Initialize(body_11,body_9,False,cA,cB,dA,dB)
link_24.SetName("Distance13")
exported_items.append(link_24)


# Mate constraint: Concentric21 [MateConcentric] type:1 align:1 flip:False
#   Entity 0: C::E name: body_9 , SW name: Spibot-LEG-4/upper_limb-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_13 , SW name: Spibot-LEG-4/Actuator_body-1 ,  SW ref.type:2 (2)

link_25 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.0716018173867797,0.208654911737508,0.0511723098018469)
dA = chrono.ChVectorD(1,3.63598040564739e-15,9.2059693201918e-13)
cB = chrono.ChVectorD(0.0842018173867799,0.208654911848804,0.0511723096069139)
dB = chrono.ChVectorD(-1,-3.94129173741931e-15,-9.19209153238398e-13)
link_25.SetFlipped(True)
link_25.Initialize(body_9,body_13,False,cA,cB,dA,dB)
link_25.SetName("Concentric21")
exported_items.append(link_25)

link_26 = chrono.ChLinkMateGeneric()
link_26.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(0.0716018173867797,0.208654911737508,0.0511723098018469)
cB = chrono.ChVectorD(0.0842018173867799,0.208654911848804,0.0511723096069139)
dA = chrono.ChVectorD(1,3.63598040564739e-15,9.2059693201918e-13)
dB = chrono.ChVectorD(-1,-3.94129173741931e-15,-9.19209153238398e-13)
link_26.Initialize(body_9,body_13,False,cA,cB,dA,dB)
link_26.SetName("Concentric21")
exported_items.append(link_26)


# Mate constraint: Concentric22 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_9 , SW name: Spibot-LEG-4/upper_limb-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_10 , SW name: Spibot-LEG-4/Actuator_rod_b-2 ,  SW ref.type:2 (2)

link_27 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.0716018173867953,0.230584627165246,0.0341556232700366)
dA = chrono.ChVectorD(1,3.63598040564739e-15,9.2059693201918e-13)
cB = chrono.ChVectorD(0.0740518176435542,0.230584627350146,0.0341556226970713)
dB = chrono.ChVectorD(1,3.91353616180368e-15,9.19486708994555e-13)
link_27.Initialize(body_9,body_10,False,cA,cB,dA,dB)
link_27.SetName("Concentric22")
exported_items.append(link_27)

link_28 = chrono.ChLinkMateGeneric()
link_28.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(0.0716018173867953,0.230584627165246,0.0341556232700366)
cB = chrono.ChVectorD(0.0740518176435542,0.230584627350146,0.0341556226970713)
dA = chrono.ChVectorD(1,3.63598040564739e-15,9.2059693201918e-13)
dB = chrono.ChVectorD(1,3.91353616180368e-15,9.19486708994555e-13)
link_28.Initialize(body_9,body_10,False,cA,cB,dA,dB)
link_28.SetName("Concentric22")
exported_items.append(link_28)


# Mate constraint: Concentric3 [MateConcentric] type:1 align:1 flip:False
#   Entity 0: C::E name: body_24 , SW name: Spibot-LEG-3/upper_limb-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_23 , SW name: Spibot-LEG-3/lower_limb-1 ,  SW ref.type:2 (2)

link_1 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.0741018266813062,0.254824476407783,-0.410270076934289)
dA = chrono.ChVectorD(1,5.41233724504764e-15,9.20541420867949e-13)
cB = chrono.ChVectorD(0.086551826424547,0.254824473570801,-0.410270076856897)
dB = chrono.ChVectorD(-1,-5.68989300120393e-15,-9.19597731297017e-13)
link_1.SetFlipped(True)
link_1.Initialize(body_24,body_23,False,cA,cB,dA,dB)
link_1.SetName("Concentric3")
exported_items.append(link_1)

link_2 = chrono.ChLinkMateGeneric()
link_2.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(0.0741018266813062,0.254824476407783,-0.410270076934289)
cB = chrono.ChVectorD(0.086551826424547,0.254824473570801,-0.410270076856897)
dA = chrono.ChVectorD(1,5.41233724504764e-15,9.20541420867949e-13)
dB = chrono.ChVectorD(-1,-5.68989300120393e-15,-9.19597731297017e-13)
link_2.Initialize(body_24,body_23,False,cA,cB,dA,dB)
link_2.SetName("Concentric3")
exported_items.append(link_2)


# Mate constraint: Concentric4 [MateConcentric] type:1 align:1 flip:False
#   Entity 0: C::E name: body_23 , SW name: Spibot-LEG-3/lower_limb-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_17 , SW name: Spibot-LEG-3/Actuator_rod-1 ,  SW ref.type:2 (2)

link_3 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.0865518264245474,0.214825893355843,-0.410607094345431)
dA = chrono.ChVectorD(-1,-5.68989300120393e-15,-9.19597731297017e-13)
cB = chrono.ChVectorD(0.0741018347302641,0.214825897990669,-0.410607096149921)
dB = chrono.ChVectorD(1,5.6621374255883e-15,9.20541420867949e-13)
link_3.SetFlipped(True)
link_3.Initialize(body_23,body_17,False,cA,cB,dA,dB)
link_3.SetName("Concentric4")
exported_items.append(link_3)

link_4 = chrono.ChLinkMateGeneric()
link_4.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(0.0865518264245474,0.214825893355843,-0.410607094345431)
cB = chrono.ChVectorD(0.0741018347302641,0.214825897990669,-0.410607096149921)
dA = chrono.ChVectorD(-1,-5.68989300120393e-15,-9.19597731297017e-13)
dB = chrono.ChVectorD(1,5.6621374255883e-15,9.20541420867949e-13)
link_4.Initialize(body_23,body_17,False,cA,cB,dA,dB)
link_4.SetName("Concentric4")
exported_items.append(link_4)


# Mate constraint: Concentric6 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_17 , SW name: Spibot-LEG-3/Actuator_rod-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_19 , SW name: Spibot-LEG-3/Actuator_body-1 ,  SW ref.type:2 (2)

link_5 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.0765018347301768,0.209440163315317,-0.315759882896145)
dA = chrono.ChVectorD(-9.18598530574855e-13,-0.0566919439510727,0.99839171846077)
cB = chrono.ChVectorD(0.0765018264244928,0.211444936789425,-0.351065621751051)
dB = chrono.ChVectorD(-9.1882057517978e-13,-0.0566919439510727,0.99839171846077)
link_5.Initialize(body_17,body_19,False,cA,cB,dA,dB)
link_5.SetName("Concentric6")
exported_items.append(link_5)

link_6 = chrono.ChLinkMateGeneric()
link_6.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(0.0765018347301768,0.209440163315317,-0.315759882896145)
cB = chrono.ChVectorD(0.0765018264244928,0.211444936789425,-0.351065621751051)
dA = chrono.ChVectorD(-9.18598530574855e-13,-0.0566919439510727,0.99839171846077)
dB = chrono.ChVectorD(-9.1882057517978e-13,-0.0566919439510727,0.99839171846077)
link_6.Initialize(body_17,body_19,False,cA,cB,dA,dB)
link_6.SetName("Concentric6")
exported_items.append(link_6)


# Mate constraint: Concentric11 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_20 , SW name: Spibot-LEG-3/Actuator_rod_b-2 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_21 , SW name: Spibot-LEG-3/Actuator_body_b-2 ,  SW ref.type:2 (2)

link_7 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.0766518264243538,0.220082305218772,-0.200147483870885)
dA = chrono.ChVectorD(-9.07329766874909e-13,-0.162544746848525,0.98670117323937)
cB = chrono.ChVectorD(0.0766518264243807,0.224877131500098,-0.22925368883285)
dB = chrono.ChVectorD(-9.06996699967522e-13,-0.162544746848525,0.98670117323937)
link_7.Initialize(body_20,body_21,False,cA,cB,dA,dB)
link_7.SetName("Concentric11")
exported_items.append(link_7)

link_8 = chrono.ChLinkMateGeneric()
link_8.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(0.0766518264243538,0.220082305218772,-0.200147483870885)
cB = chrono.ChVectorD(0.0766518264243807,0.224877131500098,-0.22925368883285)
dA = chrono.ChVectorD(-9.07329766874909e-13,-0.162544746848525,0.98670117323937)
dB = chrono.ChVectorD(-9.06996699967522e-13,-0.162544746848525,0.98670117323937)
link_8.Initialize(body_20,body_21,False,cA,cB,dA,dB)
link_8.SetName("Concentric11")
exported_items.append(link_8)


# Mate constraint: Concentric12 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_24 , SW name: Spibot-LEG-3/upper_limb-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_22 , SW name: Spibot-LEG-3/limb_body_connector-1 ,  SW ref.type:2 (2)

link_9 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.0741018266811221,0.255907284327263,-0.210273008138245)
dA = chrono.ChVectorD(1,5.41233724504764e-15,9.20541420867949e-13)
cB = chrono.ChVectorD(0.0665518264243635,0.255907284186328,-0.210273007858674)
dB = chrono.ChVectorD(1,4.77395900588817e-15,9.20874487775336e-13)
link_9.Initialize(body_24,body_22,False,cA,cB,dA,dB)
link_9.SetName("Concentric12")
exported_items.append(link_9)

link_10 = chrono.ChLinkMateGeneric()
link_10.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(0.0741018266811221,0.255907284327263,-0.210273008138245)
cB = chrono.ChVectorD(0.0665518264243635,0.255907284186328,-0.210273007858674)
dA = chrono.ChVectorD(1,5.41233724504764e-15,9.20541420867949e-13)
dB = chrono.ChVectorD(1,4.77395900588817e-15,9.20874487775336e-13)
link_10.Initialize(body_24,body_22,False,cA,cB,dA,dB)
link_10.SetName("Concentric12")
exported_items.append(link_10)


# Mate constraint: Concentric13 [MateConcentric] type:1 align:1 flip:False
#   Entity 0: C::E name: body_21 , SW name: Spibot-LEG-3/Actuator_body_b-2 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_18 , SW name: Spibot-LEG-3/limb_body_connector_b-2 ,  SW ref.type:2 (2)

link_11 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.0690518264243264,0.215124446689187,-0.170051618438495)
dA = chrono.ChVectorD(1,5.77315972805081e-15,9.20263865111792e-13)
cB = chrono.ChVectorD(0.0865855443445879,0.215124442746021,-0.170051625909914)
dB = chrono.ChVectorD(-1,-5.07927033766009e-15,-9.20430398565486e-13)
link_11.SetFlipped(True)
link_11.Initialize(body_21,body_18,False,cA,cB,dA,dB)
link_11.SetName("Concentric13")
exported_items.append(link_11)

link_12 = chrono.ChLinkMateGeneric()
link_12.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(0.0690518264243264,0.215124446689187,-0.170051618438495)
cB = chrono.ChVectorD(0.0865855443445879,0.215124442746021,-0.170051625909914)
dA = chrono.ChVectorD(1,5.77315972805081e-15,9.20263865111792e-13)
dB = chrono.ChVectorD(-1,-5.07927033766009e-15,-9.20430398565486e-13)
link_12.Initialize(body_21,body_18,False,cA,cB,dA,dB)
link_12.SetName("Concentric13")
exported_items.append(link_12)


# Mate constraint: Concentric17 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_22 , SW name: Spibot-LEG-3/limb_body_connector-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_18 , SW name: Spibot-LEG-3/limb_body_connector_b-2 ,  SW ref.type:2 (2)

link_13 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.0765518264243082,0.246232273113652,-0.150219746825282)
dA = chrono.ChVectorD(1.66533453693773e-16,0.999985343981005,-0.00541403945223884)
cB = chrono.ChVectorD(0.0765518043755,0.205232870095256,-0.149997778635781)
dB = chrono.ChVectorD(-1.66533453693773e-16,0.999985343981005,-0.00541403945224)
link_13.Initialize(body_22,body_18,False,cA,cB,dA,dB)
link_13.SetName("Concentric17")
exported_items.append(link_13)

link_14 = chrono.ChLinkMateGeneric()
link_14.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(0.0765518264243082,0.246232273113652,-0.150219746825282)
cB = chrono.ChVectorD(0.0765518043755,0.205232870095256,-0.149997778635781)
dA = chrono.ChVectorD(1.66533453693773e-16,0.999985343981005,-0.00541403945223884)
dB = chrono.ChVectorD(-1.66533453693773e-16,0.999985343981005,-0.00541403945224)
link_14.Initialize(body_22,body_18,False,cA,cB,dA,dB)
link_14.SetName("Concentric17")
exported_items.append(link_14)


# Mate constraint: Parallel14 [MateParallel] type:3 align:0 flip:False
#   Entity 0: C::E name: body_24 , SW name: Spibot-LEG-3/upper_limb-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_17 , SW name: Spibot-LEG-3/Actuator_rod-1 ,  SW ref.type:2 (2)

link_15 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.0741018266812141,0.255365880367523,-0.310271542536267)
dA = chrono.ChVectorD(-1,-5.41233724504764e-15,-9.20541420867949e-13)
cB = chrono.ChVectorD(0.0741018347302641,0.214825897990669,-0.410607096149921)
dB = chrono.ChVectorD(-1,-5.6621374255883e-15,-9.20541420867949e-13)
link_15.Initialize(body_24,body_17,False,cA,cB,dA,dB)
link_15.SetName("Parallel14")
exported_items.append(link_15)


# Mate constraint: Parallel15 [MateParallel] type:3 align:0 flip:False
#   Entity 0: C::E name: body_24 , SW name: Spibot-LEG-3/upper_limb-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_20 , SW name: Spibot-LEG-3/Actuator_rod_b-2 ,  SW ref.type:2 (2)

link_16 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.0790018266811785,0.206909581326583,-0.27119428455329)
dA = chrono.ChVectorD(-1,-5.41233724504764e-15,-9.20541420867949e-13)
cB = chrono.ChVectorD(0.0742518264244035,0.22902226629544,-0.254416048399053)
dB = chrono.ChVectorD(-1,-5.60662627435704e-15,-9.2059693201918e-13)
link_16.Initialize(body_24,body_20,False,cA,cB,dA,dB)
link_16.SetName("Parallel15")
exported_items.append(link_16)


# Mate constraint: Distance10 [MateDistanceDim] type:5 align:1 flip:False
#   Entity 0: C::E name: body_24 , SW name: Spibot-LEG-3/upper_limb-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_23 , SW name: Spibot-LEG-3/lower_limb-1 ,  SW ref.type:2 (2)

link_17 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(0.0741018266812141,0.255365880367523,-0.310271542536267)
cB = chrono.ChVectorD(0.074051826424556,0.264829341511735,-0.420265206545136)
dA = chrono.ChVectorD(-1,-5.41233724504764e-15,-9.20541420867949e-13)
dB = chrono.ChVectorD(1,5.44009282066327e-15,9.19542220145786e-13)
link_17.Initialize(body_24,body_23,False,cA,cB,dB)
link_17.SetDistance(0)
link_17.SetName("Distance10")
exported_items.append(link_17)

link_18 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.0741018266812141,0.255365880367523,-0.310271542536267)
dA = chrono.ChVectorD(-1,-5.41233724504764e-15,-9.20541420867949e-13)
cB = chrono.ChVectorD(0.074051826424556,0.264829341511735,-0.420265206545136)
dB = chrono.ChVectorD(1,5.44009282066327e-15,9.19542220145786e-13)
link_18.SetFlipped(True)
link_18.Initialize(body_24,body_23,False,cA,cB,dA,dB)
link_18.SetName("Distance10")
exported_items.append(link_18)


# Mate constraint: Distance11 [MateDistanceDim] type:5 align:1 flip:False
#   Entity 0: C::E name: body_17 , SW name: Spibot-LEG-3/Actuator_rod-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_23 , SW name: Spibot-LEG-3/lower_limb-1 ,  SW ref.type:2 (2)

link_19 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(0.0741018347302641,0.214825897990669,-0.410607096149921)
cB = chrono.ChVectorD(0.074051826424556,0.264829341511735,-0.420265206545136)
dA = chrono.ChVectorD(-1,-5.6621374255883e-15,-9.20541420867949e-13)
dB = chrono.ChVectorD(1,5.44009282066327e-15,9.19542220145786e-13)
link_19.Initialize(body_17,body_23,False,cA,cB,dB)
link_19.SetDistance(0)
link_19.SetName("Distance11")
exported_items.append(link_19)

link_20 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.0741018347302641,0.214825897990669,-0.410607096149921)
dA = chrono.ChVectorD(-1,-5.6621374255883e-15,-9.20541420867949e-13)
cB = chrono.ChVectorD(0.074051826424556,0.264829341511735,-0.420265206545136)
dB = chrono.ChVectorD(1,5.44009282066327e-15,9.19542220145786e-13)
link_20.SetFlipped(True)
link_20.Initialize(body_17,body_23,False,cA,cB,dA,dB)
link_20.SetName("Distance11")
exported_items.append(link_20)


# Mate constraint: Distance12 [MateDistanceDim] type:5 align:1 flip:False
#   Entity 0: C::E name: body_24 , SW name: Spibot-LEG-3/upper_limb-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_22 , SW name: Spibot-LEG-3/limb_body_connector-1 ,  SW ref.type:2 (2)

link_21 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(0.0741018266812141,0.255365880367523,-0.310271542536267)
cB = chrono.ChVectorD(0.0740518264243727,0.245853290351995,-0.220218720903955)
dA = chrono.ChVectorD(-1,-5.41233724504764e-15,-9.20541420867949e-13)
dB = chrono.ChVectorD(1,4.8017145815038e-15,9.20652443170411e-13)
link_21.Initialize(body_24,body_22,False,cA,cB,dB)
link_21.SetDistance(0)
link_21.SetName("Distance12")
exported_items.append(link_21)

link_22 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.0741018266812141,0.255365880367523,-0.310271542536267)
dA = chrono.ChVectorD(-1,-5.41233724504764e-15,-9.20541420867949e-13)
cB = chrono.ChVectorD(0.0740518264243727,0.245853290351995,-0.220218720903955)
dB = chrono.ChVectorD(1,4.8017145815038e-15,9.20652443170411e-13)
link_22.SetFlipped(True)
link_22.Initialize(body_24,body_22,False,cA,cB,dA,dB)
link_22.SetName("Distance12")
exported_items.append(link_22)


# Mate constraint: Distance13 [MateDistanceDim] type:5 align:1 flip:True
#   Entity 0: C::E name: body_21 , SW name: Spibot-LEG-3/Actuator_body_b-2 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_24 , SW name: Spibot-LEG-3/upper_limb-1 ,  SW ref.type:2 (2)

link_23 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(0.0790518264243264,0.215124446689187,-0.170051618438486)
cB = chrono.ChVectorD(0.0790018266811785,0.206909581326583,-0.27119428455329)
dA = chrono.ChVectorD(1,5.77315972805081e-15,9.20263865111792e-13)
dB = chrono.ChVectorD(-1,-5.41233724504764e-15,-9.20541420867949e-13)
link_23.Initialize(body_21,body_24,False,cA,cB,dB)
link_23.SetDistance(0)
link_23.SetName("Distance13")
exported_items.append(link_23)

link_24 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.0790518264243264,0.215124446689187,-0.170051618438486)
dA = chrono.ChVectorD(1,5.77315972805081e-15,9.20263865111792e-13)
cB = chrono.ChVectorD(0.0790018266811785,0.206909581326583,-0.27119428455329)
dB = chrono.ChVectorD(-1,-5.41233724504764e-15,-9.20541420867949e-13)
link_24.SetFlipped(True)
link_24.Initialize(body_21,body_24,False,cA,cB,dA,dB)
link_24.SetName("Distance13")
exported_items.append(link_24)


# Mate constraint: Concentric21 [MateConcentric] type:1 align:1 flip:False
#   Entity 0: C::E name: body_24 , SW name: Spibot-LEG-3/upper_limb-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_19 , SW name: Spibot-LEG-3/Actuator_body-1 ,  SW ref.type:2 (2)

link_25 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.0815018266811786,0.206909581326583,-0.271194284553288)
dA = chrono.ChVectorD(-1,-5.41233724504764e-15,-9.20541420867949e-13)
cB = chrono.ChVectorD(0.0689018264244193,0.206909581273339,-0.271194284274197)
dB = chrono.ChVectorD(1,5.32907051820075e-15,9.20652443170411e-13)
link_25.SetFlipped(True)
link_25.Initialize(body_24,body_19,False,cA,cB,dA,dB)
link_25.SetName("Concentric21")
exported_items.append(link_25)

link_26 = chrono.ChLinkMateGeneric()
link_26.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(0.0815018266811786,0.206909581326583,-0.271194284553288)
cB = chrono.ChVectorD(0.0689018264244193,0.206909581273339,-0.271194284274197)
dA = chrono.ChVectorD(-1,-5.41233724504764e-15,-9.20541420867949e-13)
dB = chrono.ChVectorD(1,5.32907051820075e-15,9.20652443170411e-13)
link_26.Initialize(body_24,body_19,False,cA,cB,dA,dB)
link_26.SetName("Concentric21")
exported_items.append(link_26)


# Mate constraint: Concentric22 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_24 , SW name: Spibot-LEG-3/upper_limb-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_20 , SW name: Spibot-LEG-3/Actuator_rod_b-2 ,  SW ref.type:2 (2)

link_27 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.0815018266811628,0.22902226640759,-0.254416048717191)
dA = chrono.ChVectorD(-1,-5.41233724504764e-15,-9.20541420867949e-13)
cB = chrono.ChVectorD(0.0790518264244037,0.22902226629544,-0.254416048399048)
dB = chrono.ChVectorD(-1,-5.60662627435704e-15,-9.2059693201918e-13)
link_27.Initialize(body_24,body_20,False,cA,cB,dA,dB)
link_27.SetName("Concentric22")
exported_items.append(link_27)

link_28 = chrono.ChLinkMateGeneric()
link_28.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(0.0815018266811628,0.22902226640759,-0.254416048717191)
cB = chrono.ChVectorD(0.0790518264244037,0.22902226629544,-0.254416048399048)
dA = chrono.ChVectorD(-1,-5.41233724504764e-15,-9.20541420867949e-13)
dB = chrono.ChVectorD(-1,-5.60662627435704e-15,-9.2059693201918e-13)
link_28.Initialize(body_24,body_20,False,cA,cB,dA,dB)
link_28.SetName("Concentric22")
exported_items.append(link_28)


# Mate constraint: Concentric3 [MateConcentric] type:1 align:1 flip:False
#   Entity 0: C::E name: body_32 , SW name: Spibot-LEG-6/upper_limb-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_30 , SW name: Spibot-LEG-6/lower_limb-1 ,  SW ref.type:2 (2)

link_1 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.100998182613348,0.258072904159931,0.189721106744274)
dA = chrono.ChVectorD(-1,-4.88498130835069e-15,-9.2015284280933e-13)
cB = chrono.ChVectorD(-0.113448184428644,0.258072903706762,0.189721100592412)
dB = chrono.ChVectorD(1,4.96824803519758e-15,9.19431197843323e-13)
link_1.SetFlipped(True)
link_1.Initialize(body_32,body_30,False,cA,cB,dA,dB)
link_1.SetName("Concentric3")
exported_items.append(link_1)

link_2 = chrono.ChLinkMateGeneric()
link_2.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.100998182613348,0.258072904159931,0.189721106744274)
cB = chrono.ChVectorD(-0.113448184428644,0.258072903706762,0.189721100592412)
dA = chrono.ChVectorD(-1,-4.88498130835069e-15,-9.2015284280933e-13)
dB = chrono.ChVectorD(1,4.96824803519758e-15,9.19431197843323e-13)
link_2.Initialize(body_32,body_30,False,cA,cB,dA,dB)
link_2.SetName("Concentric3")
exported_items.append(link_2)


# Mate constraint: Concentric4 [MateConcentric] type:1 align:1 flip:False
#   Entity 0: C::E name: body_30 , SW name: Spibot-LEG-6/lower_limb-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_27 , SW name: Spibot-LEG-6/Actuator_rod-1 ,  SW ref.type:2 (2)

link_3 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.113448184428644,0.2180740142714,0.19001916759441)
dA = chrono.ChVectorD(1,4.96824803519758e-15,9.19431197843323e-13)
cB = chrono.ChVectorD(-0.100998182355795,0.218074014478303,0.190019170057702)
dB = chrono.ChVectorD(-1,-3.60822483003176e-15,-9.18876086331011e-13)
link_3.SetFlipped(True)
link_3.Initialize(body_30,body_27,False,cA,cB,dA,dB)
link_3.SetName("Concentric4")
exported_items.append(link_3)

link_4 = chrono.ChLinkMateGeneric()
link_4.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.113448184428644,0.2180740142714,0.19001916759441)
cB = chrono.ChVectorD(-0.100998182355795,0.218074014478303,0.190019170057702)
dA = chrono.ChVectorD(1,4.96824803519758e-15,9.19431197843323e-13)
dB = chrono.ChVectorD(-1,-3.60822483003176e-15,-9.18876086331011e-13)
link_4.Initialize(body_30,body_27,False,cA,cB,dA,dB)
link_4.SetName("Concentric4")
exported_items.append(link_4)


# Mate constraint: Concentric6 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_27 , SW name: Spibot-LEG-6/Actuator_rod-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_29 , SW name: Spibot-LEG-6/Actuator_body-1 ,  SW ref.type:2 (2)

link_5 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.103398182355708,0.211644178592318,0.0952370134538363)
dA = chrono.ChVectorD(9.16988707189148e-13,-0.0676824830103596,-0.997706911619616)
cB = chrono.ChVectorD(-0.103398182356602,0.21406951251589,0.130988840376293)
dB = chrono.ChVectorD(9.17321774096536e-13,-0.0676824830103596,-0.997706911619616)
link_5.Initialize(body_27,body_29,False,cA,cB,dA,dB)
link_5.SetName("Concentric6")
exported_items.append(link_5)

link_6 = chrono.ChLinkMateGeneric()
link_6.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.103398182355708,0.211644178592318,0.0952370134538363)
cB = chrono.ChVectorD(-0.103398182356602,0.21406951251589,0.130988840376293)
dA = chrono.ChVectorD(9.16988707189148e-13,-0.0676824830103596,-0.997706911619616)
dB = chrono.ChVectorD(9.17321774096536e-13,-0.0676824830103596,-0.997706911619616)
link_6.Initialize(body_27,body_29,False,cA,cB,dA,dB)
link_6.SetName("Concentric6")
exported_items.append(link_6)


# Mate constraint: Concentric11 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_31 , SW name: Spibot-LEG-6/Actuator_rod_b-2 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_28 , SW name: Spibot-LEG-6/Actuator_body_b-2 ,  SW ref.type:2 (2)

link_7 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.103548182356396,0.221057574944278,-0.020012980489068)
dA = chrono.ChVectorD(9.06552610757672e-13,-0.17321914791283,-0.984883306182186)
cB = chrono.ChVectorD(-0.103548182356422,0.226167280049761,0.0090396001207675)
dB = chrono.ChVectorD(9.06663633060134e-13,-0.17321914791283,-0.984883306182186)
link_7.Initialize(body_31,body_28,False,cA,cB,dA,dB)
link_7.SetName("Concentric11")
exported_items.append(link_7)

link_8 = chrono.ChLinkMateGeneric()
link_8.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.103548182356396,0.221057574944278,-0.020012980489068)
cB = chrono.ChVectorD(-0.103548182356422,0.226167280049761,0.0090396001207675)
dA = chrono.ChVectorD(9.06552610757672e-13,-0.17321914791283,-0.984883306182186)
dB = chrono.ChVectorD(9.06663633060134e-13,-0.17321914791283,-0.984883306182186)
link_8.Initialize(body_31,body_28,False,cA,cB,dA,dB)
link_8.SetName("Concentric11")
exported_items.append(link_8)


# Mate constraint: Concentric12 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_32 , SW name: Spibot-LEG-6/upper_limb-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_25 , SW name: Spibot-LEG-6/limb_body_connector-1 ,  SW ref.type:2 (2)

link_9 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.100998182613164,0.256990092551328,-0.0102759620317966)
dA = chrono.ChVectorD(-1,-4.88498130835069e-15,-9.2015284280933e-13)
cB = chrono.ChVectorD(-0.093448182356404,0.256990091969813,-0.0102759588186464)
dB = chrono.ChVectorD(-1,-4.8017145815038e-15,-9.20541420867949e-13)
link_9.Initialize(body_32,body_25,False,cA,cB,dA,dB)
link_9.SetName("Concentric12")
exported_items.append(link_9)

link_10 = chrono.ChLinkMateGeneric()
link_10.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.100998182613164,0.256990092551328,-0.0102759620317966)
cB = chrono.ChVectorD(-0.093448182356404,0.256990091969813,-0.0102759588186464)
dA = chrono.ChVectorD(-1,-4.88498130835069e-15,-9.2015284280933e-13)
dB = chrono.ChVectorD(-1,-4.8017145815038e-15,-9.20541420867949e-13)
link_10.Initialize(body_32,body_25,False,cA,cB,dA,dB)
link_10.SetName("Concentric12")
exported_items.append(link_10)


# Mate constraint: Concentric13 [MateConcentric] type:1 align:1 flip:False
#   Entity 0: C::E name: body_28 , SW name: Spibot-LEG-6/Actuator_body_b-2 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_26 , SW name: Spibot-LEG-6/limb_body_connector_b-2 ,  SW ref.type:2 (2)

link_11 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.0959481823563673,0.215774131174992,-0.0500533982501566)
dA = chrono.ChVectorD(-1,-5.07927033766009e-15,-9.19431197843323e-13)
cB = chrono.ChVectorD(-0.113481925881984,0.215774128489236,-0.0500534073677968)
dB = chrono.ChVectorD(1,4.96824803519758e-15,9.20319376263024e-13)
link_11.SetFlipped(True)
link_11.Initialize(body_28,body_26,False,cA,cB,dA,dB)
link_11.SetName("Concentric13")
exported_items.append(link_11)

link_12 = chrono.ChLinkMateGeneric()
link_12.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.0959481823563673,0.215774131174992,-0.0500533982501566)
cB = chrono.ChVectorD(-0.113481925881984,0.215774128489236,-0.0500534073677968)
dA = chrono.ChVectorD(-1,-5.07927033766009e-15,-9.19431197843323e-13)
dB = chrono.ChVectorD(1,4.96824803519758e-15,9.20319376263024e-13)
link_12.Initialize(body_28,body_26,False,cA,cB,dA,dB)
link_12.SetName("Concentric13")
exported_items.append(link_12)


# Mate constraint: Concentric17 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_25 , SW name: Spibot-LEG-6/limb_body_connector-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_26 , SW name: Spibot-LEG-6/limb_body_connector_b-2 ,  SW ref.type:2 (2)

link_13 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.103448182356349,0.246665396162869,-0.0702209390629935)
dA = chrono.ChVectorD(2.4980018054066e-16,0.999985343981005,-0.00541403945223873)
cB = chrono.ChVectorD(-0.103448185912896,0.205665994260382,-0.0699989738528853)
dB = chrono.ChVectorD(2.22044604925031e-16,0.999985343981005,-0.00541403945223717)
link_13.Initialize(body_25,body_26,False,cA,cB,dA,dB)
link_13.SetName("Concentric17")
exported_items.append(link_13)

link_14 = chrono.ChLinkMateGeneric()
link_14.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.103448182356349,0.246665396162869,-0.0702209390629935)
cB = chrono.ChVectorD(-0.103448185912896,0.205665994260382,-0.0699989738528853)
dA = chrono.ChVectorD(2.4980018054066e-16,0.999985343981005,-0.00541403945223873)
dB = chrono.ChVectorD(2.22044604925031e-16,0.999985343981005,-0.00541403945223717)
link_14.Initialize(body_25,body_26,False,cA,cB,dA,dB)
link_14.SetName("Concentric17")
exported_items.append(link_14)


# Mate constraint: Parallel14 [MateParallel] type:3 align:0 flip:False
#   Entity 0: C::E name: body_32 , SW name: Spibot-LEG-6/upper_limb-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_27 , SW name: Spibot-LEG-6/Actuator_rod-1 ,  SW ref.type:2 (2)

link_15 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.100998182613256,0.25753149835563,0.0897225723562387)
dA = chrono.ChVectorD(1,4.88498130835069e-15,9.2015284280933e-13)
cB = chrono.ChVectorD(-0.100998182355795,0.218074014478303,0.190019170057702)
dB = chrono.ChVectorD(1,3.60822483003176e-15,9.18876086331011e-13)
link_15.Initialize(body_32,body_27,False,cA,cB,dA,dB)
link_15.SetName("Parallel14")
exported_items.append(link_15)


# Mate constraint: Parallel15 [MateParallel] type:3 align:0 flip:False
#   Entity 0: C::E name: body_32 , SW name: Spibot-LEG-6/upper_limb-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_31 , SW name: Spibot-LEG-6/Actuator_rod_b-2 ,  SW ref.type:2 (2)

link_16 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.10589818261322,0.208654913845957,0.0511722870799651)
dA = chrono.ChVectorD(1,4.88498130835069e-15,9.2015284280933e-13)
cB = chrono.ChVectorD(-0.101148182356446,0.230584628079484,0.0341556013509545)
dB = chrono.ChVectorD(1,5.05151476204446e-15,9.19486708994555e-13)
link_16.Initialize(body_32,body_31,False,cA,cB,dA,dB)
link_16.SetName("Parallel15")
exported_items.append(link_16)


# Mate constraint: Distance10 [MateDistanceDim] type:5 align:1 flip:False
#   Entity 0: C::E name: body_32 , SW name: Spibot-LEG-6/upper_limb-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_30 , SW name: Spibot-LEG-6/lower_limb-1 ,  SW ref.type:2 (2)

link_17 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(-0.100998182613256,0.25753149835563,0.0897225723562387)
cB = chrono.ChVectorD(-0.100948184428653,0.268068033719369,0.199725968209292)
dA = chrono.ChVectorD(1,4.88498130835069e-15,9.2015284280933e-13)
dB = chrono.ChVectorD(-1,-5.19029264012261e-15,-9.19431197843323e-13)
link_17.Initialize(body_32,body_30,False,cA,cB,dB)
link_17.SetDistance(0)
link_17.SetName("Distance10")
exported_items.append(link_17)

link_18 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.100998182613256,0.25753149835563,0.0897225723562387)
dA = chrono.ChVectorD(1,4.88498130835069e-15,9.2015284280933e-13)
cB = chrono.ChVectorD(-0.100948184428653,0.268068033719369,0.199725968209292)
dB = chrono.ChVectorD(-1,-5.19029264012261e-15,-9.19431197843323e-13)
link_18.SetFlipped(True)
link_18.Initialize(body_32,body_30,False,cA,cB,dA,dB)
link_18.SetName("Distance10")
exported_items.append(link_18)


# Mate constraint: Distance11 [MateDistanceDim] type:5 align:1 flip:False
#   Entity 0: C::E name: body_27 , SW name: Spibot-LEG-6/Actuator_rod-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_30 , SW name: Spibot-LEG-6/lower_limb-1 ,  SW ref.type:2 (2)

link_19 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(-0.100998182355795,0.218074014478303,0.190019170057702)
cB = chrono.ChVectorD(-0.100948184428653,0.268068033719369,0.199725968209292)
dA = chrono.ChVectorD(1,3.60822483003176e-15,9.18876086331011e-13)
dB = chrono.ChVectorD(-1,-5.19029264012261e-15,-9.19431197843323e-13)
link_19.Initialize(body_27,body_30,False,cA,cB,dB)
link_19.SetDistance(0)
link_19.SetName("Distance11")
exported_items.append(link_19)

link_20 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.100998182355795,0.218074014478303,0.190019170057702)
dA = chrono.ChVectorD(1,3.60822483003176e-15,9.18876086331011e-13)
cB = chrono.ChVectorD(-0.100948184428653,0.268068033719369,0.199725968209292)
dB = chrono.ChVectorD(-1,-5.19029264012261e-15,-9.19431197843323e-13)
link_20.SetFlipped(True)
link_20.Initialize(body_27,body_30,False,cA,cB,dA,dB)
link_20.SetName("Distance11")
exported_items.append(link_20)


# Mate constraint: Distance12 [MateDistanceDim] type:5 align:1 flip:False
#   Entity 0: C::E name: body_32 , SW name: Spibot-LEG-6/upper_limb-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_25 , SW name: Spibot-LEG-6/limb_body_connector-1 ,  SW ref.type:2 (2)

link_21 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(-0.100998182613256,0.25753149835563,0.0897225723562387)
cB = chrono.ChVectorD(-0.100948182356413,0.247044378924526,-0.000221964984320797)
dA = chrono.ChVectorD(1,4.88498130835069e-15,9.2015284280933e-13)
dB = chrono.ChVectorD(-1,-4.8017145815038e-15,-9.20319376263024e-13)
link_21.Initialize(body_32,body_25,False,cA,cB,dB)
link_21.SetDistance(0)
link_21.SetName("Distance12")
exported_items.append(link_21)

link_22 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.100998182613256,0.25753149835563,0.0897225723562387)
dA = chrono.ChVectorD(1,4.88498130835069e-15,9.2015284280933e-13)
cB = chrono.ChVectorD(-0.100948182356413,0.247044378924526,-0.000221964984320797)
dB = chrono.ChVectorD(-1,-4.8017145815038e-15,-9.20319376263024e-13)
link_22.SetFlipped(True)
link_22.Initialize(body_32,body_25,False,cA,cB,dA,dB)
link_22.SetName("Distance12")
exported_items.append(link_22)


# Mate constraint: Distance13 [MateDistanceDim] type:5 align:1 flip:True
#   Entity 0: C::E name: body_28 , SW name: Spibot-LEG-6/Actuator_body_b-2 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_32 , SW name: Spibot-LEG-6/upper_limb-1 ,  SW ref.type:2 (2)

link_23 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(-0.105948182356367,0.215774131174992,-0.0500533982501658)
cB = chrono.ChVectorD(-0.10589818261322,0.208654913845957,0.0511722870799651)
dA = chrono.ChVectorD(-1,-5.07927033766009e-15,-9.19431197843323e-13)
dB = chrono.ChVectorD(1,4.88498130835069e-15,9.2015284280933e-13)
link_23.Initialize(body_28,body_32,False,cA,cB,dB)
link_23.SetDistance(0)
link_23.SetName("Distance13")
exported_items.append(link_23)

link_24 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.105948182356367,0.215774131174992,-0.0500533982501658)
dA = chrono.ChVectorD(-1,-5.07927033766009e-15,-9.19431197843323e-13)
cB = chrono.ChVectorD(-0.10589818261322,0.208654913845957,0.0511722870799651)
dB = chrono.ChVectorD(1,4.88498130835069e-15,9.2015284280933e-13)
link_24.SetFlipped(True)
link_24.Initialize(body_28,body_32,False,cA,cB,dA,dB)
link_24.SetName("Distance13")
exported_items.append(link_24)


# Mate constraint: Concentric21 [MateConcentric] type:1 align:1 flip:False
#   Entity 0: C::E name: body_32 , SW name: Spibot-LEG-6/upper_limb-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_29 , SW name: Spibot-LEG-6/Actuator_body-1 ,  SW ref.type:2 (2)

link_25 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.10839818261322,0.208654913845957,0.0511722870799629)
dA = chrono.ChVectorD(1,4.88498130835069e-15,9.2015284280933e-13)
cB = chrono.ChVectorD(-0.095798182356529,0.208654913875061,0.0511722874467308)
dB = chrono.ChVectorD(-1,-3.99680288865056e-15,-9.19042619784705e-13)
link_25.SetFlipped(True)
link_25.Initialize(body_32,body_29,False,cA,cB,dA,dB)
link_25.SetName("Concentric21")
exported_items.append(link_25)

link_26 = chrono.ChLinkMateGeneric()
link_26.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.10839818261322,0.208654913845957,0.0511722870799629)
cB = chrono.ChVectorD(-0.095798182356529,0.208654913875061,0.0511722874467308)
dA = chrono.ChVectorD(1,4.88498130835069e-15,9.2015284280933e-13)
dB = chrono.ChVectorD(-1,-3.99680288865056e-15,-9.19042619784705e-13)
link_26.Initialize(body_32,body_29,False,cA,cB,dA,dB)
link_26.SetName("Concentric21")
exported_items.append(link_26)


# Mate constraint: Concentric22 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_32 , SW name: Spibot-LEG-6/upper_limb-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_31 , SW name: Spibot-LEG-6/Actuator_rod_b-2 ,  SW ref.type:2 (2)

link_27 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.108398182613204,0.230584628883043,0.0341556000447108)
dA = chrono.ChVectorD(1,4.88498130835069e-15,9.2015284280933e-13)
cB = chrono.ChVectorD(-0.105948182356445,0.230584628079484,0.0341556013509501)
dB = chrono.ChVectorD(1,5.05151476204446e-15,9.19486708994555e-13)
link_27.Initialize(body_32,body_31,False,cA,cB,dA,dB)
link_27.SetName("Concentric22")
exported_items.append(link_27)

link_28 = chrono.ChLinkMateGeneric()
link_28.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.108398182613204,0.230584628883043,0.0341556000447108)
cB = chrono.ChVectorD(-0.105948182356445,0.230584628079484,0.0341556013509501)
dA = chrono.ChVectorD(1,4.88498130835069e-15,9.2015284280933e-13)
dB = chrono.ChVectorD(1,5.05151476204446e-15,9.19486708994555e-13)
link_28.Initialize(body_32,body_31,False,cA,cB,dA,dB)
link_28.SetName("Concentric22")
exported_items.append(link_28)


# Mate constraint: Concentric3 [MateConcentric] type:1 align:1 flip:False
#   Entity 0: C::E name: body_39 , SW name: Spibot-LEG-1/upper_limb-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_40 , SW name: Spibot-LEG-1/lower_limb-1 ,  SW ref.type:2 (2)

link_1 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.105898173575451,0.254824480500248,-0.410270102867899)
dA = chrono.ChVectorD(1,4.66293670342566e-15,9.19930798204405e-13)
cB = chrono.ChVectorD(-0.0934481735754518,0.254824483348675,-0.410270097185573)
dB = chrono.ChVectorD(-1,-5.21804821573824e-15,-9.19153642087167e-13)
link_1.SetFlipped(True)
link_1.Initialize(body_39,body_40,False,cA,cB,dA,dB)
link_1.SetName("Concentric3")
exported_items.append(link_1)

link_2 = chrono.ChLinkMateGeneric()
link_2.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.105898173575451,0.254824480500248,-0.410270102867899)
cB = chrono.ChVectorD(-0.0934481735754518,0.254824483348675,-0.410270097185573)
dA = chrono.ChVectorD(1,4.66293670342566e-15,9.19930798204405e-13)
dB = chrono.ChVectorD(-1,-5.21804821573824e-15,-9.19153642087167e-13)
link_2.Initialize(body_39,body_40,False,cA,cB,dA,dB)
link_2.SetName("Concentric3")
exported_items.append(link_2)


# Mate constraint: Concentric4 [MateConcentric] type:1 align:1 flip:False
#   Entity 0: C::E name: body_40 , SW name: Spibot-LEG-1/lower_limb-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_37 , SW name: Spibot-LEG-1/Actuator_rod-1 ,  SW ref.type:2 (2)

link_3 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.0934481735754513,0.214825903207365,-0.410607123414736)
dA = chrono.ChVectorD(-1,-5.21804821573824e-15,-9.19153642087167e-13)
cB = chrono.ChVectorD(-0.105898173575451,0.214825899727061,-0.410607125207641)
dB = chrono.ChVectorD(1,4.96824803519758e-15,9.19431197843323e-13)
link_3.SetFlipped(True)
link_3.Initialize(body_40,body_37,False,cA,cB,dA,dB)
link_3.SetName("Concentric4")
exported_items.append(link_3)

link_4 = chrono.ChLinkMateGeneric()
link_4.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.0934481735754513,0.214825903207365,-0.410607123414736)
cB = chrono.ChVectorD(-0.105898173575451,0.214825899727061,-0.410607125207641)
dA = chrono.ChVectorD(-1,-5.21804821573824e-15,-9.19153642087167e-13)
dB = chrono.ChVectorD(1,4.96824803519758e-15,9.19431197843323e-13)
link_4.Initialize(body_40,body_37,False,cA,cB,dA,dB)
link_4.SetName("Concentric4")
exported_items.append(link_4)


# Mate constraint: Concentric6 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_37 , SW name: Spibot-LEG-1/Actuator_rod-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_38 , SW name: Spibot-LEG-1/Actuator_body-1 ,  SW ref.type:2 (2)

link_5 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.103498173575538,0.209440161922211,-0.315759912131569)
dA = chrono.ChVectorD(-9.17710352155154e-13,-0.0566919768931632,0.998391716590209)
cB = chrono.ChVectorD(-0.103498173575506,0.211444938235749,-0.35106564981691)
dB = chrono.ChVectorD(-9.17765863306386e-13,-0.0566919768931632,0.998391716590209)
link_5.Initialize(body_37,body_38,False,cA,cB,dA,dB)
link_5.SetName("Concentric6")
exported_items.append(link_5)

link_6 = chrono.ChLinkMateGeneric()
link_6.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.103498173575538,0.209440161922211,-0.315759912131569)
cB = chrono.ChVectorD(-0.103498173575506,0.211444938235749,-0.35106564981691)
dA = chrono.ChVectorD(-9.17710352155154e-13,-0.0566919768931632,0.998391716590209)
dB = chrono.ChVectorD(-9.17765863306386e-13,-0.0566919768931632,0.998391716590209)
link_6.Initialize(body_37,body_38,False,cA,cB,dA,dB)
link_6.SetName("Concentric6")
exported_items.append(link_6)


# Mate constraint: Concentric11 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_35 , SW name: Spibot-LEG-1/Actuator_rod_b-2 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_34 , SW name: Spibot-LEG-1/Actuator_body_b-2 ,  SW ref.type:2 (2)

link_7 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.103348167296693,0.220082310364206,-0.20014750454971)
dA = chrono.ChVectorD(-9.06774655362597e-13,-0.162544762913791,0.986701170592849)
cB = chrono.ChVectorD(-0.103348167296662,0.224877137127638,-0.229253709483401)
dB = chrono.ChVectorD(-9.06441588455209e-13,-0.162544762913791,0.986701170592849)
link_7.Initialize(body_35,body_34,False,cA,cB,dA,dB)
link_7.SetName("Concentric11")
exported_items.append(link_7)

link_8 = chrono.ChLinkMateGeneric()
link_8.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.103348167296693,0.220082310364206,-0.20014750454971)
cB = chrono.ChVectorD(-0.103348167296662,0.224877137127638,-0.229253709483401)
dA = chrono.ChVectorD(-9.06774655362597e-13,-0.162544762913791,0.986701170592849)
dB = chrono.ChVectorD(-9.06441588455209e-13,-0.162544762913791,0.986701170592849)
link_8.Initialize(body_35,body_34,False,cA,cB,dA,dB)
link_8.SetName("Concentric11")
exported_items.append(link_8)


# Mate constraint: Concentric12 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_39 , SW name: Spibot-LEG-1/upper_limb-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_33 , SW name: Spibot-LEG-1/limb_body_connector-1 ,  SW ref.type:2 (2)

link_9 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.105898173575635,0.255907281314647,-0.210273034033387)
dA = chrono.ChVectorD(1,4.66293670342566e-15,9.19930798204405e-13)
cB = chrono.ChVectorD(-0.113448173575636,0.255907284079365,-0.210273027614865)
dB = chrono.ChVectorD(1,5.13478148889135e-15,9.20485909716717e-13)
link_9.Initialize(body_39,body_33,False,cA,cB,dA,dB)
link_9.SetName("Concentric12")
exported_items.append(link_9)

link_10 = chrono.ChLinkMateGeneric()
link_10.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.105898173575635,0.255907281314647,-0.210273034033387)
cB = chrono.ChVectorD(-0.113448173575636,0.255907284079365,-0.210273027614865)
dA = chrono.ChVectorD(1,4.66293670342566e-15,9.19930798204405e-13)
dB = chrono.ChVectorD(1,5.13478148889135e-15,9.20485909716717e-13)
link_10.Initialize(body_39,body_33,False,cA,cB,dA,dB)
link_10.SetName("Concentric12")
exported_items.append(link_10)


# Mate constraint: Concentric13 [MateConcentric] type:1 align:1 flip:False
#   Entity 0: C::E name: body_34 , SW name: Spibot-LEG-1/Actuator_body_b-2 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_36 , SW name: Spibot-LEG-1/limb_body_connector_b-2 ,  SW ref.type:2 (2)

link_11 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.110948167296717,0.21512445135281,-0.170051639247837)
dA = chrono.ChVectorD(1,4.96824803519758e-15,9.19486708994555e-13)
cB = chrono.ChVectorD(-0.0934144370478476,0.215124445648131,-0.170051645196594)
dB = chrono.ChVectorD(-1,-5.16253706450698e-15,-9.20541420867949e-13)
link_11.SetFlipped(True)
link_11.Initialize(body_34,body_36,False,cA,cB,dA,dB)
link_11.SetName("Concentric13")
exported_items.append(link_11)

link_12 = chrono.ChLinkMateGeneric()
link_12.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.110948167296717,0.21512445135281,-0.170051639247837)
cB = chrono.ChVectorD(-0.0934144370478476,0.215124445648131,-0.170051645196594)
dA = chrono.ChVectorD(1,4.96824803519758e-15,9.19486708994555e-13)
dB = chrono.ChVectorD(-1,-5.16253706450698e-15,-9.20541420867949e-13)
link_12.Initialize(body_34,body_36,False,cA,cB,dA,dB)
link_12.SetName("Concentric13")
exported_items.append(link_12)


# Mate constraint: Concentric17 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_33 , SW name: Spibot-LEG-1/limb_body_connector-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_36 , SW name: Spibot-LEG-1/limb_body_connector_b-2 ,  SW ref.type:2 (2)

link_13 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.103448173575691,0.24623227300669,-0.150219766581473)
dA = chrono.ChVectorD(-3.05311331771918e-16,0.999985343981005,-0.00541403945223881)
cB = chrono.ChVectorD(-0.103448177016935,0.205232872997366,-0.149997797922461)
dB = chrono.ChVectorD(-4.44089209850063e-16,0.999985343981005,-0.00541403945223998)
link_13.Initialize(body_33,body_36,False,cA,cB,dA,dB)
link_13.SetName("Concentric17")
exported_items.append(link_13)

link_14 = chrono.ChLinkMateGeneric()
link_14.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.103448173575691,0.24623227300669,-0.150219766581473)
cB = chrono.ChVectorD(-0.103448177016935,0.205232872997366,-0.149997797922461)
dA = chrono.ChVectorD(-3.05311331771918e-16,0.999985343981005,-0.00541403945223881)
dB = chrono.ChVectorD(-4.44089209850063e-16,0.999985343981005,-0.00541403945223998)
link_14.Initialize(body_33,body_36,False,cA,cB,dA,dB)
link_14.SetName("Concentric17")
exported_items.append(link_14)


# Mate constraint: Parallel14 [MateParallel] type:3 align:0 flip:False
#   Entity 0: C::E name: body_39 , SW name: Spibot-LEG-1/upper_limb-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_37 , SW name: Spibot-LEG-1/Actuator_rod-1 ,  SW ref.type:2 (2)

link_15 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.105898173575543,0.255365880907447,-0.310271568450643)
dA = chrono.ChVectorD(-1,-4.66293670342566e-15,-9.19930798204405e-13)
cB = chrono.ChVectorD(-0.105898173575451,0.214825899727061,-0.410607125207641)
dB = chrono.ChVectorD(-1,-4.96824803519758e-15,-9.19431197843323e-13)
link_15.Initialize(body_39,body_37,False,cA,cB,dA,dB)
link_15.SetName("Parallel14")
exported_items.append(link_15)


# Mate constraint: Parallel15 [MateParallel] type:3 align:0 flip:False
#   Entity 0: C::E name: body_39 , SW name: Spibot-LEG-1/upper_limb-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_35 , SW name: Spibot-LEG-1/Actuator_rod_b-2 ,  SW ref.type:2 (2)

link_16 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.100998173575579,0.206909580478251,-0.271194312189121)
dA = chrono.ChVectorD(-1,-4.66293670342566e-15,-9.19930798204405e-13)
cB = chrono.ChVectorD(-0.105748167296643,0.229022272324464,-0.254416068932319)
dB = chrono.ChVectorD(-1,-5.02375918642883e-15,-9.19875287053173e-13)
link_16.Initialize(body_39,body_35,False,cA,cB,dA,dB)
link_16.SetName("Parallel15")
exported_items.append(link_16)


# Mate constraint: Distance10 [MateDistanceDim] type:5 align:1 flip:False
#   Entity 0: C::E name: body_39 , SW name: Spibot-LEG-1/upper_limb-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_40 , SW name: Spibot-LEG-1/lower_limb-1 ,  SW ref.type:2 (2)

link_17 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(-0.105898173575543,0.255365880907447,-0.310271568450643)
cB = chrono.ChVectorD(-0.105948173575443,0.264829353473779,-0.420265224687512)
dA = chrono.ChVectorD(-1,-4.66293670342566e-15,-9.19930798204405e-13)
dB = chrono.ChVectorD(1,5.05151476204446e-15,9.19153642087167e-13)
link_17.Initialize(body_39,body_40,False,cA,cB,dB)
link_17.SetDistance(0)
link_17.SetName("Distance10")
exported_items.append(link_17)

link_18 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.105898173575543,0.255365880907447,-0.310271568450643)
dA = chrono.ChVectorD(-1,-4.66293670342566e-15,-9.19930798204405e-13)
cB = chrono.ChVectorD(-0.105948173575443,0.264829353473779,-0.420265224687512)
dB = chrono.ChVectorD(1,5.05151476204446e-15,9.19153642087167e-13)
link_18.SetFlipped(True)
link_18.Initialize(body_39,body_40,False,cA,cB,dA,dB)
link_18.SetName("Distance10")
exported_items.append(link_18)


# Mate constraint: Distance11 [MateDistanceDim] type:5 align:1 flip:False
#   Entity 0: C::E name: body_37 , SW name: Spibot-LEG-1/Actuator_rod-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_40 , SW name: Spibot-LEG-1/lower_limb-1 ,  SW ref.type:2 (2)

link_19 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(-0.105898173575451,0.214825899727061,-0.410607125207641)
cB = chrono.ChVectorD(-0.105948173575443,0.264829353473779,-0.420265224687512)
dA = chrono.ChVectorD(-1,-4.96824803519758e-15,-9.19431197843323e-13)
dB = chrono.ChVectorD(1,5.05151476204446e-15,9.19153642087167e-13)
link_19.Initialize(body_37,body_40,False,cA,cB,dB)
link_19.SetDistance(0)
link_19.SetName("Distance11")
exported_items.append(link_19)

link_20 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.105898173575451,0.214825899727061,-0.410607125207641)
dA = chrono.ChVectorD(-1,-4.96824803519758e-15,-9.19431197843323e-13)
cB = chrono.ChVectorD(-0.105948173575443,0.264829353473779,-0.420265224687512)
dB = chrono.ChVectorD(1,5.05151476204446e-15,9.19153642087167e-13)
link_20.SetFlipped(True)
link_20.Initialize(body_37,body_40,False,cA,cB,dA,dB)
link_20.SetName("Distance11")
exported_items.append(link_20)


# Mate constraint: Distance12 [MateDistanceDim] type:5 align:1 flip:False
#   Entity 0: C::E name: body_39 , SW name: Spibot-LEG-1/upper_limb-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_33 , SW name: Spibot-LEG-1/limb_body_connector-1 ,  SW ref.type:2 (2)

link_21 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(-0.105898173575543,0.255365880907447,-0.310271568450643)
cB = chrono.ChVectorD(-0.105948173575626,0.245853290245033,-0.220218740660146)
dA = chrono.ChVectorD(-1,-4.66293670342566e-15,-9.19930798204405e-13)
dB = chrono.ChVectorD(1,5.16253706450698e-15,9.2015284280933e-13)
link_21.Initialize(body_39,body_33,False,cA,cB,dB)
link_21.SetDistance(0)
link_21.SetName("Distance12")
exported_items.append(link_21)

link_22 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.105898173575543,0.255365880907447,-0.310271568450643)
dA = chrono.ChVectorD(-1,-4.66293670342566e-15,-9.19930798204405e-13)
cB = chrono.ChVectorD(-0.105948173575626,0.245853290245033,-0.220218740660146)
dB = chrono.ChVectorD(1,5.16253706450698e-15,9.2015284280933e-13)
link_22.SetFlipped(True)
link_22.Initialize(body_39,body_33,False,cA,cB,dA,dB)
link_22.SetName("Distance12")
exported_items.append(link_22)


# Mate constraint: Distance13 [MateDistanceDim] type:5 align:1 flip:True
#   Entity 0: C::E name: body_34 , SW name: Spibot-LEG-1/Actuator_body_b-2 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_39 , SW name: Spibot-LEG-1/upper_limb-1 ,  SW ref.type:2 (2)

link_23 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(-0.100948167296717,0.21512445135281,-0.170051639247828)
cB = chrono.ChVectorD(-0.100998173575579,0.206909580478251,-0.271194312189121)
dA = chrono.ChVectorD(1,4.96824803519758e-15,9.19486708994555e-13)
dB = chrono.ChVectorD(-1,-4.66293670342566e-15,-9.19930798204405e-13)
link_23.Initialize(body_34,body_39,False,cA,cB,dB)
link_23.SetDistance(0)
link_23.SetName("Distance13")
exported_items.append(link_23)

link_24 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.100948167296717,0.21512445135281,-0.170051639247828)
dA = chrono.ChVectorD(1,4.96824803519758e-15,9.19486708994555e-13)
cB = chrono.ChVectorD(-0.100998173575579,0.206909580478251,-0.271194312189121)
dB = chrono.ChVectorD(-1,-4.66293670342566e-15,-9.19930798204405e-13)
link_24.SetFlipped(True)
link_24.Initialize(body_34,body_39,False,cA,cB,dA,dB)
link_24.SetName("Distance13")
exported_items.append(link_24)


# Mate constraint: Concentric21 [MateConcentric] type:1 align:1 flip:False
#   Entity 0: C::E name: body_39 , SW name: Spibot-LEG-1/upper_limb-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_38 , SW name: Spibot-LEG-1/Actuator_body-1 ,  SW ref.type:2 (2)

link_25 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.098498173575579,0.206909580478251,-0.271194312189118)
dA = chrono.ChVectorD(-1,-4.66293670342566e-15,-9.19930798204405e-13)
cB = chrono.ChVectorD(-0.111098173575579,0.206909580084296,-0.2711943124897)
dB = chrono.ChVectorD(1,4.82947015711943e-15,9.19486708994555e-13)
link_25.SetFlipped(True)
link_25.Initialize(body_39,body_38,False,cA,cB,dA,dB)
link_25.SetName("Concentric21")
exported_items.append(link_25)

link_26 = chrono.ChLinkMateGeneric()
link_26.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.098498173575579,0.206909580478251,-0.271194312189118)
cB = chrono.ChVectorD(-0.111098173575579,0.206909580084296,-0.2711943124897)
dA = chrono.ChVectorD(-1,-4.66293670342566e-15,-9.19930798204405e-13)
dB = chrono.ChVectorD(1,4.82947015711943e-15,9.19486708994555e-13)
link_26.Initialize(body_39,body_38,False,cA,cB,dA,dB)
link_26.SetName("Concentric21")
exported_items.append(link_26)


# Mate constraint: Concentric22 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_39 , SW name: Spibot-LEG-1/upper_limb-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_35 , SW name: Spibot-LEG-1/Actuator_rod_b-2 ,  SW ref.type:2 (2)

link_27 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.0984981735755948,0.229022264963196,-0.254416075567449)
dA = chrono.ChVectorD(-1,-4.66293670342566e-15,-9.19930798204405e-13)
cB = chrono.ChVectorD(-0.100948167296643,0.229022272324464,-0.254416068932315)
dB = chrono.ChVectorD(-1,-5.02375918642883e-15,-9.19875287053173e-13)
link_27.Initialize(body_39,body_35,False,cA,cB,dA,dB)
link_27.SetName("Concentric22")
exported_items.append(link_27)

link_28 = chrono.ChLinkMateGeneric()
link_28.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.0984981735755948,0.229022264963196,-0.254416075567449)
cB = chrono.ChVectorD(-0.100948167296643,0.229022272324464,-0.254416068932315)
dA = chrono.ChVectorD(-1,-4.66293670342566e-15,-9.19930798204405e-13)
dB = chrono.ChVectorD(-1,-5.02375918642883e-15,-9.19875287053173e-13)
link_28.Initialize(body_39,body_35,False,cA,cB,dA,dB)
link_28.SetName("Concentric22")
exported_items.append(link_28)


# Mate constraint: Concentric3 [MateConcentric] type:1 align:1 flip:False
#   Entity 0: C::E name: body_48 , SW name: Spibot-LEG-5/upper_limb-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_47 , SW name: Spibot-LEG-5/lower_limb-1 ,  SW ref.type:2 (2)

link_1 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.0109981826133477,0.258072902890912,0.189721118503435)
dA = chrono.ChVectorD(-1,-4.46864767411626e-15,-9.2015284280933e-13)
cB = chrono.ChVectorD(-0.0234481826835884,0.258072902295668,0.189721119474856)
dB = chrono.ChVectorD(1,4.35762537165374e-15,9.19819775901942e-13)
link_1.SetFlipped(True)
link_1.Initialize(body_48,body_47,False,cA,cB,dA,dB)
link_1.SetName("Concentric3")
exported_items.append(link_1)

link_2 = chrono.ChLinkMateGeneric()
link_2.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.0109981826133477,0.258072902890912,0.189721118503435)
cB = chrono.ChVectorD(-0.0234481826835884,0.258072902295668,0.189721119474856)
dA = chrono.ChVectorD(-1,-4.46864767411626e-15,-9.2015284280933e-13)
dB = chrono.ChVectorD(1,4.35762537165374e-15,9.19819775901942e-13)
link_2.Initialize(body_48,body_47,False,cA,cB,dA,dB)
link_2.SetName("Concentric3")
exported_items.append(link_2)


# Mate constraint: Concentric4 [MateConcentric] type:1 align:1 flip:False
#   Entity 0: C::E name: body_47 , SW name: Spibot-LEG-5/lower_limb-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_45 , SW name: Spibot-LEG-5/Actuator_rod-1 ,  SW ref.type:2 (2)

link_3 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.0234481826835886,0.218074012879321,0.190019189028512)
dA = chrono.ChVectorD(1,4.35762537165374e-15,9.19819775901942e-13)
cB = chrono.ChVectorD(-0.0109981826133456,0.218074013548997,0.190019189474541)
dB = chrono.ChVectorD(-1,-3.5527136788005e-15,-9.19486708994555e-13)
link_3.SetFlipped(True)
link_3.Initialize(body_47,body_45,False,cA,cB,dA,dB)
link_3.SetName("Concentric4")
exported_items.append(link_3)

link_4 = chrono.ChLinkMateGeneric()
link_4.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.0234481826835886,0.218074012879321,0.190019189028512)
cB = chrono.ChVectorD(-0.0109981826133456,0.218074013548997,0.190019189474541)
dA = chrono.ChVectorD(1,4.35762537165374e-15,9.19819775901942e-13)
dB = chrono.ChVectorD(-1,-3.5527136788005e-15,-9.19486708994555e-13)
link_4.Initialize(body_47,body_45,False,cA,cB,dA,dB)
link_4.SetName("Concentric4")
exported_items.append(link_4)


# Mate constraint: Concentric6 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_45 , SW name: Spibot-LEG-5/Actuator_rod-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_46 , SW name: Spibot-LEG-5/Actuator_body-1 ,  SW ref.type:2 (2)

link_5 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.0133981826132583,0.211644178453262,0.0952370328170663)
dA = chrono.ChVectorD(9.17710352155154e-13,-0.0676824746919485,-0.997706912183921)
cB = chrono.ChVectorD(-0.0133981826132932,0.214069511495581,0.130988851167131)
dB = chrono.ChVectorD(9.16600129130529e-13,-0.0676824746919485,-0.997706912183921)
link_5.Initialize(body_45,body_46,False,cA,cB,dA,dB)
link_5.SetName("Concentric6")
exported_items.append(link_5)

link_6 = chrono.ChLinkMateGeneric()
link_6.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.0133981826132583,0.211644178453262,0.0952370328170663)
cB = chrono.ChVectorD(-0.0133981826132932,0.214069511495581,0.130988851167131)
dA = chrono.ChVectorD(9.17710352155154e-13,-0.0676824746919485,-0.997706912183921)
dB = chrono.ChVectorD(9.16600129130529e-13,-0.0676824746919485,-0.997706912183921)
link_6.Initialize(body_45,body_46,False,cA,cB,dA,dB)
link_6.SetName("Concentric6")
exported_items.append(link_6)


# Mate constraint: Concentric11 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_44 , SW name: Spibot-LEG-5/Actuator_rod_b-2 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_43 , SW name: Spibot-LEG-5/Actuator_body_b-2 ,  SW ref.type:2 (2)

link_7 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.0135481823563957,0.221057576189984,-0.0200129679148411)
dA = chrono.ChVectorD(9.06219543850284e-13,-0.173219144703633,-0.984883306746613)
cB = chrono.ChVectorD(-0.0135481823564225,0.226167281200801,0.00903961271164366)
dB = chrono.ChVectorD(9.06441588455209e-13,-0.173219144703632,-0.984883306746613)
link_7.Initialize(body_44,body_43,False,cA,cB,dA,dB)
link_7.SetName("Concentric11")
exported_items.append(link_7)

link_8 = chrono.ChLinkMateGeneric()
link_8.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.0135481823563957,0.221057576189984,-0.0200129679148411)
cB = chrono.ChVectorD(-0.0135481823564225,0.226167281200801,0.00903961271164366)
dA = chrono.ChVectorD(9.06219543850284e-13,-0.173219144703633,-0.984883306746613)
dB = chrono.ChVectorD(9.06441588455209e-13,-0.173219144703632,-0.984883306746613)
link_8.Initialize(body_44,body_43,False,cA,cB,dA,dB)
link_8.SetName("Concentric11")
exported_items.append(link_8)


# Mate constraint: Concentric12 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_48 , SW name: Spibot-LEG-5/upper_limb-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_49 , SW name: Spibot-LEG-5/limb_body_connector-1 ,  SW ref.type:2 (2)

link_9 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.0109981826131637,0.256990092704239,-0.0102759502803342)
dA = chrono.ChVectorD(-1,-4.46864767411626e-15,-9.2015284280933e-13)
cB = chrono.ChVectorD(-0.00344818235640454,0.256990092023294,-0.0102759489405508)
dB = chrono.ChVectorD(-1,-3.99680288865056e-15,-9.20041820506867e-13)
link_9.Initialize(body_48,body_49,False,cA,cB,dA,dB)
link_9.SetName("Concentric12")
exported_items.append(link_9)

link_10 = chrono.ChLinkMateGeneric()
link_10.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.0109981826131637,0.256990092704239,-0.0102759502803342)
cB = chrono.ChVectorD(-0.00344818235640454,0.256990092023294,-0.0102759489405508)
dA = chrono.ChVectorD(-1,-4.46864767411626e-15,-9.2015284280933e-13)
dB = chrono.ChVectorD(-1,-3.99680288865056e-15,-9.20041820506867e-13)
link_10.Initialize(body_48,body_49,False,cA,cB,dA,dB)
link_10.SetName("Concentric12")
exported_items.append(link_10)


# Mate constraint: Concentric13 [MateConcentric] type:1 align:1 flip:False
#   Entity 0: C::E name: body_43 , SW name: Spibot-LEG-5/Actuator_body_b-2 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_42 , SW name: Spibot-LEG-5/limb_body_connector_b-2 ,  SW ref.type:2 (2)

link_11 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.00594818235636807,0.215774132518583,-0.0500533856931461)
dA = chrono.ChVectorD(-1,-4.413136522885e-15,-9.19542220145786e-13)
cB = chrono.ChVectorD(-0.0234819275359353,0.215774131190006,-0.0500533902384349)
dB = chrono.ChVectorD(1,4.13558076672871e-15,9.2059693201918e-13)
link_11.SetFlipped(True)
link_11.Initialize(body_43,body_42,False,cA,cB,dA,dB)
link_11.SetName("Concentric13")
exported_items.append(link_11)

link_12 = chrono.ChLinkMateGeneric()
link_12.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.00594818235636807,0.215774132518583,-0.0500533856931461)
cB = chrono.ChVectorD(-0.0234819275359353,0.215774131190006,-0.0500533902384349)
dA = chrono.ChVectorD(-1,-4.413136522885e-15,-9.19542220145786e-13)
dB = chrono.ChVectorD(1,4.13558076672871e-15,9.2059693201918e-13)
link_12.Initialize(body_43,body_42,False,cA,cB,dA,dB)
link_12.SetName("Concentric13")
exported_items.append(link_12)


# Mate constraint: Concentric17 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_49 , SW name: Spibot-LEG-5/limb_body_connector-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_42 , SW name: Spibot-LEG-5/limb_body_connector_b-2 ,  SW ref.type:2 (2)

link_13 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.0134481823563493,0.24666539621635,-0.0702209291848979)
dA = chrono.ChVectorD(9.43689570931383e-16,0.999985343981005,-0.00541403945223862)
cB = chrono.ChVectorD(-0.0134481875668475,0.205665996961151,-0.0699989567235234)
dB = chrono.ChVectorD(8.04911692853238e-16,0.999985343981005,-0.00541403945223737)
link_13.Initialize(body_49,body_42,False,cA,cB,dA,dB)
link_13.SetName("Concentric17")
exported_items.append(link_13)

link_14 = chrono.ChLinkMateGeneric()
link_14.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.0134481823563493,0.24666539621635,-0.0702209291848979)
cB = chrono.ChVectorD(-0.0134481875668475,0.205665996961151,-0.0699989567235234)
dA = chrono.ChVectorD(9.43689570931383e-16,0.999985343981005,-0.00541403945223862)
dB = chrono.ChVectorD(8.04911692853238e-16,0.999985343981005,-0.00541403945223737)
link_14.Initialize(body_49,body_42,False,cA,cB,dA,dB)
link_14.SetName("Concentric17")
exported_items.append(link_14)


# Mate constraint: Parallel14 [MateParallel] type:3 align:0 flip:False
#   Entity 0: C::E name: body_48 , SW name: Spibot-LEG-5/upper_limb-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_45 , SW name: Spibot-LEG-5/Actuator_rod-1 ,  SW ref.type:2 (2)

link_15 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.0109981826132557,0.257531497797575,0.0897225841115503)
dA = chrono.ChVectorD(1,4.46864767411626e-15,9.2015284280933e-13)
cB = chrono.ChVectorD(-0.0109981826133456,0.218074013548997,0.190019189474541)
dB = chrono.ChVectorD(1,3.5527136788005e-15,9.19486708994555e-13)
link_15.Initialize(body_48,body_45,False,cA,cB,dA,dB)
link_15.SetName("Parallel14")
exported_items.append(link_15)


# Mate constraint: Parallel15 [MateParallel] type:3 align:0 flip:False
#   Entity 0: C::E name: body_48 , SW name: Spibot-LEG-5/upper_limb-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_44 , SW name: Spibot-LEG-5/Actuator_rod_b-2 ,  SW ref.type:2 (2)

link_16 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.01589818261322,0.208654913561986,0.0511722984877764)
dA = chrono.ChVectorD(1,4.46864767411626e-15,9.2015284280933e-13)
cB = chrono.ChVectorD(-0.0111481823564454,0.230584629148684,0.0341556139562247)
dB = chrono.ChVectorD(1,4.49640324973188e-15,9.19042619784705e-13)
link_16.Initialize(body_48,body_44,False,cA,cB,dA,dB)
link_16.SetName("Parallel15")
exported_items.append(link_16)


# Mate constraint: Distance10 [MateDistanceDim] type:5 align:1 flip:False
#   Entity 0: C::E name: body_48 , SW name: Spibot-LEG-5/upper_limb-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_47 , SW name: Spibot-LEG-5/lower_limb-1 ,  SW ref.type:2 (2)

link_17 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(-0.0109981826132557,0.257531497797575,0.0897225841115503)
cB = chrono.ChVectorD(-0.0109481826835978,0.268068032946518,0.199725986454115)
dA = chrono.ChVectorD(1,4.46864767411626e-15,9.2015284280933e-13)
dB = chrono.ChVectorD(-1,-4.57966997657877e-15,-9.19819775901942e-13)
link_17.Initialize(body_48,body_47,False,cA,cB,dB)
link_17.SetDistance(0)
link_17.SetName("Distance10")
exported_items.append(link_17)

link_18 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.0109981826132557,0.257531497797575,0.0897225841115503)
dA = chrono.ChVectorD(1,4.46864767411626e-15,9.2015284280933e-13)
cB = chrono.ChVectorD(-0.0109481826835978,0.268068032946518,0.199725986454115)
dB = chrono.ChVectorD(-1,-4.57966997657877e-15,-9.19819775901942e-13)
link_18.SetFlipped(True)
link_18.Initialize(body_48,body_47,False,cA,cB,dA,dB)
link_18.SetName("Distance10")
exported_items.append(link_18)


# Mate constraint: Distance11 [MateDistanceDim] type:5 align:1 flip:False
#   Entity 0: C::E name: body_45 , SW name: Spibot-LEG-5/Actuator_rod-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_47 , SW name: Spibot-LEG-5/lower_limb-1 ,  SW ref.type:2 (2)

link_19 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(-0.0109981826133456,0.218074013548997,0.190019189474541)
cB = chrono.ChVectorD(-0.0109481826835978,0.268068032946518,0.199725986454115)
dA = chrono.ChVectorD(1,3.5527136788005e-15,9.19486708994555e-13)
dB = chrono.ChVectorD(-1,-4.57966997657877e-15,-9.19819775901942e-13)
link_19.Initialize(body_45,body_47,False,cA,cB,dB)
link_19.SetDistance(0)
link_19.SetName("Distance11")
exported_items.append(link_19)

link_20 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.0109981826133456,0.218074013548997,0.190019189474541)
dA = chrono.ChVectorD(1,3.5527136788005e-15,9.19486708994555e-13)
cB = chrono.ChVectorD(-0.0109481826835978,0.268068032946518,0.199725986454115)
dB = chrono.ChVectorD(-1,-4.57966997657877e-15,-9.19819775901942e-13)
link_20.SetFlipped(True)
link_20.Initialize(body_45,body_47,False,cA,cB,dA,dB)
link_20.SetName("Distance11")
exported_items.append(link_20)


# Mate constraint: Distance12 [MateDistanceDim] type:5 align:1 flip:False
#   Entity 0: C::E name: body_48 , SW name: Spibot-LEG-5/upper_limb-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_49 , SW name: Spibot-LEG-5/limb_body_connector-1 ,  SW ref.type:2 (2)

link_21 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(-0.0109981826132557,0.257531497797575,0.0897225841115503)
cB = chrono.ChVectorD(-0.0109481823564137,0.247044378978007,-0.000221955106225302)
dA = chrono.ChVectorD(1,4.46864767411626e-15,9.2015284280933e-13)
dB = chrono.ChVectorD(-1,-3.99680288865056e-15,-9.19764264750711e-13)
link_21.Initialize(body_48,body_49,False,cA,cB,dB)
link_21.SetDistance(0)
link_21.SetName("Distance12")
exported_items.append(link_21)

link_22 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.0109981826132557,0.257531497797575,0.0897225841115503)
dA = chrono.ChVectorD(1,4.46864767411626e-15,9.2015284280933e-13)
cB = chrono.ChVectorD(-0.0109481823564137,0.247044378978007,-0.000221955106225302)
dB = chrono.ChVectorD(-1,-3.99680288865056e-15,-9.19764264750711e-13)
link_22.SetFlipped(True)
link_22.Initialize(body_48,body_49,False,cA,cB,dA,dB)
link_22.SetName("Distance12")
exported_items.append(link_22)


# Mate constraint: Distance13 [MateDistanceDim] type:5 align:1 flip:True
#   Entity 0: C::E name: body_43 , SW name: Spibot-LEG-5/Actuator_body_b-2 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_48 , SW name: Spibot-LEG-5/upper_limb-1 ,  SW ref.type:2 (2)

link_23 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(-0.0159481823563682,0.215774132518583,-0.0500533856931553)
cB = chrono.ChVectorD(-0.01589818261322,0.208654913561986,0.0511722984877764)
dA = chrono.ChVectorD(-1,-4.413136522885e-15,-9.19542220145786e-13)
dB = chrono.ChVectorD(1,4.46864767411626e-15,9.2015284280933e-13)
link_23.Initialize(body_43,body_48,False,cA,cB,dB)
link_23.SetDistance(0)
link_23.SetName("Distance13")
exported_items.append(link_23)

link_24 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.0159481823563682,0.215774132518583,-0.0500533856931553)
dA = chrono.ChVectorD(-1,-4.413136522885e-15,-9.19542220145786e-13)
cB = chrono.ChVectorD(-0.01589818261322,0.208654913561986,0.0511722984877764)
dB = chrono.ChVectorD(1,4.46864767411626e-15,9.2015284280933e-13)
link_24.SetFlipped(True)
link_24.Initialize(body_43,body_48,False,cA,cB,dA,dB)
link_24.SetName("Distance13")
exported_items.append(link_24)


# Mate constraint: Concentric21 [MateConcentric] type:1 align:1 flip:False
#   Entity 0: C::E name: body_48 , SW name: Spibot-LEG-5/upper_limb-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_46 , SW name: Spibot-LEG-5/Actuator_body-1 ,  SW ref.type:2 (2)

link_25 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.0183981826132199,0.208654913561986,0.051172298487774)
dA = chrono.ChVectorD(1,4.46864767411626e-15,9.2015284280933e-13)
cB = chrono.ChVectorD(-0.00579818261321985,0.208654913520226,0.0511722981924248)
dB = chrono.ChVectorD(-1,-3.66373598126302e-15,-9.18320974818698e-13)
link_25.SetFlipped(True)
link_25.Initialize(body_48,body_46,False,cA,cB,dA,dB)
link_25.SetName("Concentric21")
exported_items.append(link_25)

link_26 = chrono.ChLinkMateGeneric()
link_26.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.0183981826132199,0.208654913561986,0.051172298487774)
cB = chrono.ChVectorD(-0.00579818261321985,0.208654913520226,0.0511722981924248)
dA = chrono.ChVectorD(1,4.46864767411626e-15,9.2015284280933e-13)
dB = chrono.ChVectorD(-1,-3.66373598126302e-15,-9.18320974818698e-13)
link_26.Initialize(body_48,body_46,False,cA,cB,dA,dB)
link_26.SetName("Concentric21")
exported_items.append(link_26)


# Mate constraint: Concentric22 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_48 , SW name: Spibot-LEG-5/upper_limb-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_44 , SW name: Spibot-LEG-5/Actuator_rod_b-2 ,  SW ref.type:2 (2)

link_27 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.0183981826132045,0.230584628720056,0.0341556116084368)
dA = chrono.ChVectorD(1,4.46864767411626e-15,9.2015284280933e-13)
cB = chrono.ChVectorD(-0.0159481823564454,0.230584629148684,0.0341556139562204)
dB = chrono.ChVectorD(1,4.49640324973188e-15,9.19042619784705e-13)
link_27.Initialize(body_48,body_44,False,cA,cB,dA,dB)
link_27.SetName("Concentric22")
exported_items.append(link_27)

link_28 = chrono.ChLinkMateGeneric()
link_28.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.0183981826132045,0.230584628720056,0.0341556116084368)
cB = chrono.ChVectorD(-0.0159481823564454,0.230584629148684,0.0341556139562204)
dA = chrono.ChVectorD(1,4.46864767411626e-15,9.2015284280933e-13)
dB = chrono.ChVectorD(1,4.49640324973188e-15,9.19042619784705e-13)
link_28.Initialize(body_48,body_44,False,cA,cB,dA,dB)
link_28.SetName("Concentric22")
exported_items.append(link_28)

