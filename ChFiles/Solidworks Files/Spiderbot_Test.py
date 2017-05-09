# Chrono::Engine Python script from SolidWorks 
# Assembly: D:\Documents\ME - Graduate\Research\Projects\Project Chrono\SpiderBot\Solidworks Files\Parts\SpiderBot-Test.SLDASM


import ChronoEngine_python_core as chrono 
import builtins 

shapes_dir = 'Spiderbot_Test_shapes/' 

if hasattr(builtins, 'exported_system_relpath'): 
    shapes_dir = builtins.exported_system_relpath + shapes_dir 

exported_items = [] 

body_0= chrono.ChBodyAuxRef()
body_0.SetName('ground')
body_0.SetBodyFixed(True)
exported_items.append(body_0)

# Rigid body part
body_1= chrono.ChBodyAuxRef()
body_1.SetName('Spibot-LEG-1/limb_body_connector-1')
body_1.SetPos(chrono.ChVectorD(-0.0934481735756908,0.24623227300669,-0.150219766581464))
body_1.SetRot(chrono.ChQuaternionD(-0.498644653171685,0.501351682816852,0.498644653172147,-0.501351682816393))
body_1.SetMass(0.0319301494979552)
body_1.SetInertiaXX(chrono.ChVectorD(2.2110890182935e-06,4.65620459313164e-06,4.83154745183423e-06))
body_1.SetInertiaXY(chrono.ChVectorD(1.32385342629299e-08,1.30522695294681e-20,-1.61410843813686e-19))
body_1.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(0.01,0.00875766097763167,0.01),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_1_1_shape = chrono.ChObjShapeFile() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_1_1_level = chrono.ChAssetLevel() 
body_1_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_1_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_1_1_level.GetAssets().push_back(body_1_1_shape) 
body_1.GetAssets().push_back(body_1_1_level) 

# Auxiliary marker (coordinate system feature)
marker_1_1 =chrono.ChMarker()
marker_1_1.SetName('LB-UL-Ref')
body_1.AddMarker(marker_1_1)
marker_1_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.103448173575636,0.255907284079365,-0.210273027614856),chrono.ChQuaternionD(-0.498644653171686,0.501351682816392,0.501351682816854,0.498644653172145)))

# Auxiliary marker (coordinate system feature)
marker_1_2 =chrono.ChMarker()
marker_1_2.SetName('LB-B-Act-1')
body_1.AddMarker(marker_1_2)
marker_1_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.103448173575691,0.2562321264465,-0.150273906975996),chrono.ChQuaternionD(0.705190031320552,-0.709018349357842,-3.26447924366294E-13,-3.24430828870974E-13)))

exported_items.append(body_1)



# Rigid body part
body_2= chrono.ChBodyAuxRef()
body_2.SetName('Spibot-LEG-1/Actuator_body_b-2')
body_2.SetPos(chrono.ChVectorD(-0.103348173575636,0.221626237070786,-0.209519685061788))
body_2.SetRot(chrono.ChQuaternionD(-0.0815439433899001,0.996669747356879,3.99692977618465e-14,4.58007354565552e-13))
body_2.SetMass(0.00204159144576871)
body_2.SetInertiaXX(chrono.ChVectorD(8.08481090947277e-07,7.82569693423566e-07,1.04939004371166e-07))
body_2.SetInertiaXY(chrono.ChVectorD(1.07997029789078e-19,6.55274082118834e-19,-1.14743759720862e-07))
body_2.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-4.17826009441434e-18,4.31502965232471e-20,-0.0175577824053523),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_2_1_shape = chrono.ChObjShapeFile() 
body_2_1_shape.SetFilename(shapes_dir +'body_2_1.obj') 
body_2_1_shape.SetColor(chrono.ChColor(0.843137254901961,0.843137254901961,0)) 
body_2_1_shape.SetFading(0) 
body_2_1_level = chrono.ChAssetLevel() 
body_2_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_2_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_2_1_level.GetAssets().push_back(body_2_1_shape) 
body_2.GetAssets().push_back(body_2_1_level) 

# Auxiliary marker (coordinate system feature)
marker_2_1 =chrono.ChMarker()
marker_2_1.SetName('LL-Act-Base')
body_2.AddMarker(marker_2_1)
marker_2_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.103348173575681,0.213498998925096,-0.160184626532146),chrono.ChQuaternionD(-0.0815439433899001,0.996669747356879,3.99692977618465E-14,4.58007354565552E-13)))

# Auxiliary marker (coordinate system feature)
marker_2_2 =chrono.ChMarker()
marker_2_2.SetName('UL-Act-Base')
body_2.AddMarker(marker_2_2)
marker_2_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.103348173575672,0.215124446554234,-0.170051638238074),chrono.ChQuaternionD(-0.0815439433899001,0.996669747356879,3.99692977618465E-14,4.58007354565552E-13)))

exported_items.append(body_2)



# Rigid body part
body_3= chrono.ChBodyAuxRef()
body_3.SetName('Spibot-LEG-1/Actuator_rod_b-2')
body_3.SetPos(chrono.ChVectorD(-0.103348173575645,0.219980715290835,-0.199530816534697))
body_3.SetRot(chrono.ChQuaternionD(-0.0815439433899001,0.996669747356879,4.00086435661759e-14,4.5820110640621e-13))
body_3.SetMass(0.00122087835937912)
body_3.SetInertiaXX(chrono.ChVectorD(7.21325661454779e-07,6.99059602021648e-07,4.17530581817835e-08))
body_3.SetInertiaXY(chrono.ChVectorD(1.04387774740752e-19,6.33546995276293e-19,-1.11302255561627e-07))
body_3.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-2.22314235000441e-19,1.10781155047926e-18,0.0317642663115355),chrono.ChQuaternionD(1,0,0,0)))

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
marker_3_1.SetName('UL-Act-Shaft')
body_3.AddMarker(marker_3_1)
marker_3_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.103348173575595,0.229022267727915,-0.254416069148925),chrono.ChQuaternionD(-4.00086435661759E-14,-4.5820110640621E-13,-0.0815439433899001,0.996669747356879)))

# Auxiliary marker (coordinate system feature)
marker_3_2 =chrono.ChMarker()
marker_3_2.SetName('LL-Act-Shaft')
body_3.AddMarker(marker_3_2)
marker_3_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.103348173575558,0.235524058244466,-0.293884115972639),chrono.ChQuaternionD(-4.00086435661759E-14,-4.5820110640621E-13,-0.0815439433899001,0.996669747356879)))

exported_items.append(body_3)



# Rigid body part
body_4= chrono.ChBodyAuxRef()
body_4.SetName('Spibot-LEG-1/limb_body_connector_b-2')
body_4.SetPos(chrono.ChVectorD(-0.103414433606608,0.215151516751495,-0.165051711518169))
body_4.SetRot(chrono.ChQuaternionD(-0.498644653171685,0.501351682816853,0.498644653172147,-0.501351682816394))
body_4.SetMass(0.0118048176111825)
body_4.SetInertiaXX(chrono.ChVectorD(8.17149703748216e-07,1.71878703364595e-06,1.78336759057685e-06))
body_4.SetInertiaXY(chrono.ChVectorD(3.54051977884999e-09,3.96652494596064e-21,-5.94585782936986e-20))
body_4.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-1.56699758850283e-18,-0.00621524420249397,8.63806342003782e-06),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_4_1_shape = chrono.ChObjShapeFile() 
body_4_1_shape.SetFilename(shapes_dir +'body_4_1.obj') 
body_4_1_level = chrono.ChAssetLevel() 
body_4_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_4_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_4_1_level.GetAssets().push_back(body_4_1_shape) 
body_4.GetAssets().push_back(body_4_1_level) 

# Auxiliary marker (coordinate system feature)
marker_4_1 =chrono.ChMarker()
marker_4_1.SetName('LB-B-Act-1')
body_4.AddMarker(marker_4_1)
marker_4_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.103448173575691,0.215232727343279,-0.150051931358454),chrono.ChQuaternionD(0.705190031320551,-0.709018349357843,-3.26526428701587E-13,-3.24430616356632E-13)))

# Auxiliary marker (coordinate system feature)
marker_4_2 =chrono.ChMarker()
marker_4_2.SetName('LB-UL-Ref')
body_4.AddMarker(marker_4_2)
marker_4_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.103414433606603,0.215124446554234,-0.170051638238074),chrono.ChQuaternionD(-0.498644653171685,0.501351682816853,0.498644653172147,-0.501351682816394)))

exported_items.append(body_4)



# Rigid body part
body_5= chrono.ChBodyAuxRef()
body_5.SetName('Spibot-LEG-1/Actuator_rod-1')
body_5.SetPos(chrono.ChVectorD(-0.103498173575539,0.209404732177373,-0.315135898980292))
body_5.SetRot(chrono.ChQuaternionD(4.59293026625088e-13,-1.55424838793458e-14,0.999597848206953,0.0283573951559304))
body_5.SetMass(0.00140945245841084)
body_5.SetInertiaXX(chrono.ChVectorD(2.33089158373325e-06,2.31955787343295e-06,3.09621985526252e-08))
body_5.SetInertiaXY(chrono.ChVectorD(1.2025371975028e-19,-2.11741557648667e-18,1.30374400467121e-07))
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
marker_5_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.103498173575488,0.212558223695995,-0.370671438198364),chrono.ChQuaternionD(0.999597848206953,0.0283573951559304,-4.59293026625088E-13,1.55424838793458E-14)))

# Auxiliary marker (coordinate system feature)
marker_5_2 =chrono.ChMarker()
marker_5_2.SetName('LL-Act-Shaft')
body_5.AddMarker(marker_5_2)
marker_5_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.103498173575451,0.214825902990285,-0.410607106849561),chrono.ChQuaternionD(0.999597848206953,0.0283573951559304,-4.59293026625088E-13,1.55424838793458E-14)))

exported_items.append(body_5)



# Rigid body part
body_6= chrono.ChBodyAuxRef()
body_6.SetName('Spibot-LEG-1/Actuator_body-1')
body_6.SetPos(chrono.ChVectorD(-0.103498173575534,0.209744180686373,-0.321113897171299))
body_6.SetRot(chrono.ChQuaternionD(-0.0283573951559303,0.999597848206953,1.5474696996844e-14,4.59350483141974e-13))
body_6.SetMass(0.00204159144576871)
body_6.SetInertiaXX(chrono.ChVectorD(8.08481090947278e-07,7.99172674305193e-07,8.83360234895384e-08))
body_6.SetInertiaXY(chrono.ChVectorD(3.76732126578673e-20,6.62849574029888e-19,-4.04942223728502e-08))
body_6.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-4.17192939730159e-18,5.58956732701871e-20,-0.0175577824053523),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_6_1_shape = chrono.ChObjShapeFile() 
body_6_1_shape.SetFilename(shapes_dir +'body_6_1.obj') 
body_6_1_shape.SetColor(chrono.ChColor(0.752941176470588,0.752941176470588,0.752941176470588)) 
body_6_1_shape.SetFading(0.75) 
body_6_1_level = chrono.ChAssetLevel() 
body_6_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_6_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_6_1_level.GetAssets().push_back(body_6_1_shape) 
body_6.GetAssets().push_back(body_6_1_level) 

# Auxiliary marker (coordinate system feature)
marker_6_1 =chrono.ChMarker()
marker_6_1.SetName('LL-Act-Base')
body_6.AddMarker(marker_6_1)
marker_6_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.103498173575579,0.206909581568511,-0.271194311357302),chrono.ChQuaternionD(-0.0283573951559303,0.999597848206953,1.5474696996844E-14,4.59350483141974E-13)))

# Auxiliary marker (coordinate system feature)
marker_6_2 =chrono.ChMarker()
marker_6_2.SetName('UL-Act-Base')
body_6.AddMarker(marker_6_2)
marker_6_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.10349817357557,0.207476501392083,-0.281178228520101),chrono.ChQuaternionD(-0.0283573951559303,0.999597848206953,1.5474696996844E-14,4.59350483141974E-13)))

exported_items.append(body_6)



# Rigid body part
body_7= chrono.ChBodyAuxRef()
body_7.SetName('Spibot-LEG-1/upper_limb-1')
body_7.SetPos(chrono.ChVectorD(-0.103448173575543,0.255365883672166,-0.310271562032112))
body_7.SetRot(chrono.ChQuaternionD(-0.498644662040788,0.501351673995638,0.498644662041249,-0.501351673995179))
body_7.SetMass(0.0769386604687246)
body_7.SetInertiaXX(chrono.ChVectorD(1.21361245226805e-05,0.000291222023077268,0.000279898353184369))
body_7.SetInertiaXY(chrono.ChVectorD(1.51103862808834e-06,1.20058215334762e-05,-6.50005192959008e-08))
body_7.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-0.00433891891647107,-0.0160004109829567,2.90281587993209e-19),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_7_1_shape = chrono.ChObjShapeFile() 
body_7_1_shape.SetFilename(shapes_dir +'body_7_1.obj') 
body_7_1_level = chrono.ChAssetLevel() 
body_7_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_7_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_7_1_level.GetAssets().push_back(body_7_1_shape) 
body_7.GetAssets().push_back(body_7_1_level) 

# Auxiliary marker (coordinate system feature)
marker_7_1 =chrono.ChMarker()
marker_7_1.SetName('UL-LL-Ref')
body_7.AddMarker(marker_7_1)
marker_7_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.103448173575451,0.254824483264966,-0.410270096449368),chrono.ChQuaternionD(0.707104190372734,-0.0019141465097016,-0.707104190373384,0.00191414650970319)))

# Auxiliary marker (coordinate system feature)
marker_7_2 =chrono.ChMarker()
marker_7_2.SetName('UL-LB-Ref')
body_7.AddMarker(marker_7_2)
marker_7_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.103448173575635,0.255907284079365,-0.210273027614856),chrono.ChQuaternionD(0.707104190372734,-0.0019141465097016,-0.707104190373384,0.00191414650970319)))

exported_items.append(body_7)



# Rigid body part
body_8= chrono.ChBodyAuxRef()
body_8.SetName('Spibot-LEG-1/lower_limb-1')
body_8.SetPos(chrono.ChVectorD(-0.103448173575451,0.154824495110536,-0.410318769991421))
body_8.SetRot(chrono.ChQuaternionD(0.999999970386077,0.000243367717472511,-4.59409655919735e-13,2.65144072669563e-15))
body_8.SetMass(0.173763895224452)
body_8.SetInertiaXX(chrono.ChVectorD(0.000660134295478084,8.7583006665832e-06,0.000660653854204159))
body_8.SetInertiaXY(chrono.ChVectorD(-7.08403833753521e-11,-6.70200652894143e-12,3.1264859887736e-07))
body_8.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(4.14273289970014e-09,-0.0143933772184335,3.59893950746433e-07),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_8_1_shape = chrono.ChObjShapeFile() 
body_8_1_shape.SetFilename(shapes_dir +'body_8_1.obj') 
body_8_1_shape.SetColor(chrono.ChColor(0.898039215686275,0.917647058823529,0.929411764705882)) 
body_8_1_shape.SetFading(0.75) 
body_8_1_level = chrono.ChAssetLevel() 
body_8_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_8_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_8_1_level.GetAssets().push_back(body_8_1_shape) 
body_8.GetAssets().push_back(body_8_1_level) 

# Auxiliary marker (coordinate system feature)
marker_8_1 =chrono.ChMarker()
marker_8_1.SetName('LowerLimbCenterRef')
body_8.AddMarker(marker_8_1)
marker_8_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.103448173575451,0.154824495110536,-0.410318769991421),chrono.ChQuaternionD(0.707106760246343,0.000172086963671556,0.000172086963021853,-0.707106760246339)))

# Auxiliary marker (coordinate system feature)
marker_8_2 =chrono.ChMarker()
marker_8_2.SetName('LL-UL-Ref')
body_8.AddMarker(marker_8_2)
marker_8_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.103448173575452,0.254824483264966,-0.410270096449368),chrono.ChQuaternionD(0.707106760246343,0.000172086963671556,0.000172086963021853,-0.70710676024634)))

# Collision shapes 
body_8.GetCollisionModel().ClearModel()
body_8.GetCollisionModel().AddSphere(0.01, chrono.ChVectorD(3.46944695195361E-17,-0.1,0))
body_8.GetCollisionModel().BuildModel()
body_8.SetCollide(True)

exported_items.append(body_8)



# Rigid body part
body_9= chrono.ChBodyAuxRef()
body_9.SetName('Body-2')
body_9.SetPos(chrono.ChVectorD(-0.0134481779660203,0.23594898852646,-0.110163495529889))
body_9.SetRot(chrono.ChQuaternionD(0.0019141591236923,0.707104229144446,-0.00191415891359841,-0.707104151533946))
body_9.SetMass(0.341410951377452)
body_9.SetInertiaXX(chrono.ChVectorD(0.000241317387799145,0.00125554646880151,0.00103704927238703))
body_9.SetInertiaXY(chrono.ChVectorD(5.49131770190389e-06,-8.73381196775929e-11,6.02717032743408e-13))
body_9.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-2.0412340707415e-18,0,1.64121582559538e-17),chrono.ChQuaternionD(1,0,0,0)))
body_9.SetBodyFixed(True)

# Visualization shape 
body_9_1_shape = chrono.ChObjShapeFile() 
body_9_1_shape.SetFilename(shapes_dir +'body_9_1.obj') 
body_9_1_shape.SetColor(chrono.ChColor(0.792156862745098,0.819607843137255,0.933333333333333)) 
body_9_1_shape.SetFading(0) 
body_9_1_level = chrono.ChAssetLevel() 
body_9_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_9_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_9_1_level.GetAssets().push_back(body_9_1_shape) 
body_9.GetAssets().push_back(body_9_1_level) 

# Auxiliary marker (coordinate system feature)
marker_9_1 =chrono.ChMarker()
marker_9_1.SetName('BM-4')
body_9.AddMarker(marker_9_1)
marker_9_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(0.0765518176436502,0.236165550158031,-0.0701640718925539),chrono.ChQuaternionD(0.501351710330357,0.498644680537091,0.498644625806739,-0.501351655302887)))

# Auxiliary marker (coordinate system feature)
marker_9_2 =chrono.ChMarker()
marker_9_2.SetName('BM-3')
body_9.AddMarker(marker_9_2)
marker_9_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(0.0765518264243082,0.235732427001851,-0.150162899411034),chrono.ChQuaternionD(0.501351710330357,0.498644680537091,0.498644625806739,-0.501351655302887)))

# Auxiliary marker (coordinate system feature)
marker_9_3 =chrono.ChMarker()
marker_9_3.SetName('BM-5')
body_9.AddMarker(marker_9_3)
marker_9_3.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.0134481823563493,0.236165550104549,-0.0701640817706494),chrono.ChQuaternionD(0.501351710330357,0.498644680537091,0.498644625806739,-0.501351655302887)))

# Auxiliary marker (coordinate system feature)
marker_9_4 =chrono.ChMarker()
marker_9_4.SetName('BM-2')
body_9.AddMarker(marker_9_4)
marker_9_4.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.0134481735756912,0.23573242694837,-0.150162909289129),chrono.ChQuaternionD(0.501351710330357,0.498644680537091,0.498644625806739,-0.501351655302887)))

# Auxiliary marker (coordinate system feature)
marker_9_5 =chrono.ChMarker()
marker_9_5.SetName('BM-6')
body_9.AddMarker(marker_9_5)
marker_9_5.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.103448182356349,0.236165550051068,-0.0701640916487449),chrono.ChQuaternionD(0.501351710330357,0.498644680537091,0.498644625806739,-0.501351655302887)))

# Auxiliary marker (coordinate system feature)
marker_9_6 =chrono.ChMarker()
marker_9_6.SetName('BM-1')
body_9.AddMarker(marker_9_6)
marker_9_6.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.103448173575691,0.235732426894889,-0.150162919167225),chrono.ChQuaternionD(0.501351710330357,0.498644680537091,0.498644625806739,-0.501351655302887)))

exported_items.append(body_9)




# Mate constraint: Distance1 [MateDistanceDim] type:5 align:1 flip:False
#   Entity 0: C::E name: body_4 , SW name: Spibot-LEG-1/limb_body_connector_b-2 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_9 , SW name: Body-2 ,  SW ref.type:2 (2)

link_1 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(-0.113414433606621,0.225232580783089,-0.150106071752986)
cB = chrono.ChVectorD(-0.0134481779660203,0.22594913508665,-0.110109355135367)
dA = chrono.ChVectorD(-4.71844785465692e-16,0.999985343981005,-0.00541403945223995)
dB = chrono.ChVectorD(-1.13959586670642e-15,-0.999985343981005,0.00541403945223878)
link_1.Initialize(body_4,body_9,False,cA,cB,dB)
link_1.SetDistance(-0.0005)
link_1.SetName("Distance1")
exported_items.append(link_1)

link_2 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.113414433606621,0.225232580783089,-0.150106071752986)
dA = chrono.ChVectorD(-4.71844785465692e-16,0.999985343981005,-0.00541403945223995)
cB = chrono.ChVectorD(-0.0134481779660203,0.22594913508665,-0.110109355135367)
dB = chrono.ChVectorD(-1.13959586670642e-15,-0.999985343981005,0.00541403945223878)
link_2.SetFlipped(True)
link_2.Initialize(body_4,body_9,False,cA,cB,dA,dB)
link_2.SetName("Distance1")
exported_items.append(link_2)


# Mate constraint: Concentric1 [MateConcentric] type:1 align:1 flip:False
#   Entity 0: C::E name: body_9 , SW name: Body-2 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_4 , SW name: Spibot-LEG-1/limb_body_connector_b-2 ,  SW ref.type:2 (2)

link_3 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.103448173575691,0.245732280334699,-0.150217059561747)
dA = chrono.ChVectorD(-1.13959586670642e-15,-0.999985343981005,0.00541403945223878)
cB = chrono.ChVectorD(-0.103448173575691,0.205232873903469,-0.149997790963932)
dB = chrono.ChVectorD(-4.71844785465692e-16,0.999985343981005,-0.00541403945223995)
link_3.SetFlipped(True)
link_3.Initialize(body_9,body_4,False,cA,cB,dA,dB)
link_3.SetName("Concentric1")
exported_items.append(link_3)

link_4 = chrono.ChLinkMateGeneric()
link_4.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.103448173575691,0.245732280334699,-0.150217059561747)
cB = chrono.ChVectorD(-0.103448173575691,0.205232873903469,-0.149997790963932)
dA = chrono.ChVectorD(-1.13959586670642e-15,-0.999985343981005,0.00541403945223878)
dB = chrono.ChVectorD(-4.71844785465692e-16,0.999985343981005,-0.00541403945223995)
link_4.Initialize(body_9,body_4,False,cA,cB,dA,dB)
link_4.SetName("Concentric1")
exported_items.append(link_4)


# Mate constraint: Distance8 [MateDistanceDim] type:5 align:1 flip:False
#   Entity 0: C::E name: body_1 , SW name: Spibot-LEG-1/limb_body_connector-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_9 , SW name: Body-2 ,  SW ref.type:2 (2)

link_5 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(-0.113448173575691,0.24623227300669,-0.150219766581483)
cB = chrono.ChVectorD(-0.0134481779660202,0.24594884196627,-0.110217635924412)
dA = chrono.ChVectorD(3.60822483003176e-16,-0.999985343981005,0.00541403945223878)
dB = chrono.ChVectorD(1.13959586670642e-15,0.999985343981005,-0.00541403945223878)
link_5.Initialize(body_1,body_9,False,cA,cB,dB)
link_5.SetDistance(-0.000499999999999743)
link_5.SetName("Distance8")
exported_items.append(link_5)

link_6 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.113448173575691,0.24623227300669,-0.150219766581483)
dA = chrono.ChVectorD(3.60822483003176e-16,-0.999985343981005,0.00541403945223878)
cB = chrono.ChVectorD(-0.0134481779660202,0.24594884196627,-0.110217635924412)
dB = chrono.ChVectorD(1.13959586670642e-15,0.999985343981005,-0.00541403945223878)
link_6.SetFlipped(True)
link_6.Initialize(body_1,body_9,False,cA,cB,dA,dB)
link_6.SetName("Distance8")
exported_items.append(link_6)


# Mate constraint: Concentric3 [MateConcentric] type:1 align:1 flip:False
#   Entity 0: C::E name: body_7 , SW name: Spibot-LEG-1/upper_limb-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_8 , SW name: Spibot-LEG-1/lower_limb-1 ,  SW ref.type:2 (2)

link_1 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.105898173575451,0.254824483264966,-0.41027009644937)
dA = chrono.ChVectorD(1,4.66293670342566e-15,9.19930798204405e-13)
cB = chrono.ChVectorD(-0.0934481735754518,0.254824483264966,-0.410270096449359)
dB = chrono.ChVectorD(-1,-5.21804821573824e-15,-9.1882057517978e-13)
link_1.SetFlipped(True)
link_1.Initialize(body_7,body_8,False,cA,cB,dA,dB)
link_1.SetName("Concentric3")
exported_items.append(link_1)

link_2 = chrono.ChLinkMateGeneric()
link_2.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.105898173575451,0.254824483264966,-0.41027009644937)
cB = chrono.ChVectorD(-0.0934481735754518,0.254824483264966,-0.410270096449359)
dA = chrono.ChVectorD(1,4.66293670342566e-15,9.19930798204405e-13)
dB = chrono.ChVectorD(-1,-5.21804821573824e-15,-9.1882057517978e-13)
link_2.Initialize(body_7,body_8,False,cA,cB,dA,dB)
link_2.SetName("Concentric3")
exported_items.append(link_2)


# Mate constraint: Concentric4 [MateConcentric] type:1 align:1 flip:False
#   Entity 0: C::E name: body_8 , SW name: Spibot-LEG-1/lower_limb-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_5 , SW name: Spibot-LEG-1/Actuator_rod-1 ,  SW ref.type:2 (2)

link_3 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.0934481735754513,0.214825902990285,-0.410607106849552)
dA = chrono.ChVectorD(-1,-5.21804821573824e-15,-9.1882057517978e-13)
cB = chrono.ChVectorD(-0.105898173575451,0.214825902990285,-0.410607106849563)
dB = chrono.ChVectorD(1,5.02375918642883e-15,9.19098130935936e-13)
link_3.SetFlipped(True)
link_3.Initialize(body_8,body_5,False,cA,cB,dA,dB)
link_3.SetName("Concentric4")
exported_items.append(link_3)

link_4 = chrono.ChLinkMateGeneric()
link_4.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.0934481735754513,0.214825902990285,-0.410607106849552)
cB = chrono.ChVectorD(-0.105898173575451,0.214825902990285,-0.410607106849563)
dA = chrono.ChVectorD(-1,-5.21804821573824e-15,-9.1882057517978e-13)
dB = chrono.ChVectorD(1,5.02375918642883e-15,9.19098130935936e-13)
link_4.Initialize(body_8,body_5,False,cA,cB,dA,dB)
link_4.SetName("Concentric4")
exported_items.append(link_4)


# Mate constraint: Concentric6 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_5 , SW name: Spibot-LEG-1/Actuator_rod-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_6 , SW name: Spibot-LEG-1/Actuator_body-1 ,  SW ref.type:2 (2)

link_5 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.103498173575538,0.209440164666346,-0.315759893802967)
dA = chrono.ChVectorD(-9.17599329852692e-13,-0.0566919823572446,0.998391716279941)
cB = chrono.ChVectorD(-0.103498173575506,0.211444940157091,-0.351065648659697)
dB = chrono.ChVectorD(-9.17543818701461e-13,-0.0566919823572445,0.998391716279941)
link_5.Initialize(body_5,body_6,False,cA,cB,dA,dB)
link_5.SetName("Concentric6")
exported_items.append(link_5)

link_6 = chrono.ChLinkMateGeneric()
link_6.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.103498173575538,0.209440164666346,-0.315759893802967)
cB = chrono.ChVectorD(-0.103498173575506,0.211444940157091,-0.351065648659697)
dA = chrono.ChVectorD(-9.17599329852692e-13,-0.0566919823572446,0.998391716279941)
dB = chrono.ChVectorD(-9.17543818701461e-13,-0.0566919823572445,0.998391716279941)
link_6.Initialize(body_5,body_6,False,cA,cB,dA,dB)
link_6.SetName("Concentric6")
exported_items.append(link_6)


# Mate constraint: Concentric11 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_3 , SW name: Spibot-LEG-1/Actuator_rod_b-2 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_2 , SW name: Spibot-LEG-1/Actuator_body_b-2 ,  SW ref.type:2 (2)

link_7 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.103348173575645,0.220082305767656,-0.200147504766318)
dA = chrono.ChVectorD(-9.06774655362597e-13,-0.162544762913791,0.986701170592849)
cB = chrono.ChVectorD(-0.103348173575618,0.224877132329061,-0.229253708473645)
dB = chrono.ChVectorD(-9.06441588455209e-13,-0.162544762913791,0.986701170592849)
link_7.Initialize(body_3,body_2,False,cA,cB,dA,dB)
link_7.SetName("Concentric11")
exported_items.append(link_7)

link_8 = chrono.ChLinkMateGeneric()
link_8.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.103348173575645,0.220082305767656,-0.200147504766318)
cB = chrono.ChVectorD(-0.103348173575618,0.224877132329061,-0.229253708473645)
dA = chrono.ChVectorD(-9.06774655362597e-13,-0.162544762913791,0.986701170592849)
dB = chrono.ChVectorD(-9.06441588455209e-13,-0.162544762913791,0.986701170592849)
link_8.Initialize(body_3,body_2,False,cA,cB,dA,dB)
link_8.SetName("Concentric11")
exported_items.append(link_8)


# Mate constraint: Concentric12 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_7 , SW name: Spibot-LEG-1/upper_limb-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_1 , SW name: Spibot-LEG-1/limb_body_connector-1 ,  SW ref.type:2 (2)

link_9 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.105898173575635,0.255907284079365,-0.210273027614858)
dA = chrono.ChVectorD(1,4.66293670342566e-15,9.19930798204405e-13)
cB = chrono.ChVectorD(-0.113448173575636,0.255907284079365,-0.210273027614865)
dB = chrono.ChVectorD(1,5.13478148889135e-15,9.20485909716717e-13)
link_9.Initialize(body_7,body_1,False,cA,cB,dA,dB)
link_9.SetName("Concentric12")
exported_items.append(link_9)

link_10 = chrono.ChLinkMateGeneric()
link_10.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.105898173575635,0.255907284079365,-0.210273027614858)
cB = chrono.ChVectorD(-0.113448173575636,0.255907284079365,-0.210273027614865)
dA = chrono.ChVectorD(1,4.66293670342566e-15,9.19930798204405e-13)
dB = chrono.ChVectorD(1,5.13478148889135e-15,9.20485909716717e-13)
link_10.Initialize(body_7,body_1,False,cA,cB,dA,dB)
link_10.SetName("Concentric12")
exported_items.append(link_10)


# Mate constraint: Concentric13 [MateConcentric] type:1 align:1 flip:False
#   Entity 0: C::E name: body_2 , SW name: Spibot-LEG-1/Actuator_body_b-2 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_4 , SW name: Spibot-LEG-1/limb_body_connector_b-2 ,  SW ref.type:2 (2)

link_11 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.110948173575672,0.215124446554234,-0.170051638238081)
dA = chrono.ChVectorD(1,4.96824803519758e-15,9.19486708994555e-13)
cB = chrono.ChVectorD(-0.093414433606603,0.215124446554234,-0.170051638238065)
dB = chrono.ChVectorD(-1,-5.16253706450698e-15,-9.20541420867949e-13)
link_11.SetFlipped(True)
link_11.Initialize(body_2,body_4,False,cA,cB,dA,dB)
link_11.SetName("Concentric13")
exported_items.append(link_11)

link_12 = chrono.ChLinkMateGeneric()
link_12.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.110948173575672,0.215124446554234,-0.170051638238081)
cB = chrono.ChVectorD(-0.093414433606603,0.215124446554234,-0.170051638238065)
dA = chrono.ChVectorD(1,4.96824803519758e-15,9.19486708994555e-13)
dB = chrono.ChVectorD(-1,-5.16253706450698e-15,-9.20541420867949e-13)
link_12.Initialize(body_2,body_4,False,cA,cB,dA,dB)
link_12.SetName("Concentric13")
exported_items.append(link_12)


# Mate constraint: Concentric17 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_1 , SW name: Spibot-LEG-1/limb_body_connector-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_4 , SW name: Spibot-LEG-1/limb_body_connector_b-2 ,  SW ref.type:2 (2)

link_13 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.103448173575691,0.24623227300669,-0.150219766581473)
dA = chrono.ChVectorD(-3.05311331771918e-16,0.999985343981005,-0.00541403945223881)
cB = chrono.ChVectorD(-0.103448173575691,0.205232873903469,-0.149997790963932)
dB = chrono.ChVectorD(-4.9960036108132e-16,0.999985343981005,-0.00541403945223995)
link_13.Initialize(body_1,body_4,False,cA,cB,dA,dB)
link_13.SetName("Concentric17")
exported_items.append(link_13)

link_14 = chrono.ChLinkMateGeneric()
link_14.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.103448173575691,0.24623227300669,-0.150219766581473)
cB = chrono.ChVectorD(-0.103448173575691,0.205232873903469,-0.149997790963932)
dA = chrono.ChVectorD(-3.05311331771918e-16,0.999985343981005,-0.00541403945223881)
dB = chrono.ChVectorD(-4.9960036108132e-16,0.999985343981005,-0.00541403945223995)
link_14.Initialize(body_1,body_4,False,cA,cB,dA,dB)
link_14.SetName("Concentric17")
exported_items.append(link_14)


# Mate constraint: Parallel14 [MateParallel] type:3 align:0 flip:False
#   Entity 0: C::E name: body_7 , SW name: Spibot-LEG-1/upper_limb-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_5 , SW name: Spibot-LEG-1/Actuator_rod-1 ,  SW ref.type:2 (2)

link_15 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.105898173575544,0.255365883672166,-0.310271562032114)
dA = chrono.ChVectorD(-1,-4.66293670342566e-15,-9.19930798204405e-13)
cB = chrono.ChVectorD(-0.105898173575451,0.214825902990285,-0.410607106849563)
dB = chrono.ChVectorD(-1,-5.02375918642883e-15,-9.19098130935936e-13)
link_15.Initialize(body_7,body_5,False,cA,cB,dA,dB)
link_15.SetName("Parallel14")
exported_items.append(link_15)


# Mate constraint: Parallel15 [MateParallel] type:3 align:0 flip:False
#   Entity 0: C::E name: body_7 , SW name: Spibot-LEG-1/upper_limb-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_3 , SW name: Spibot-LEG-1/Actuator_rod_b-2 ,  SW ref.type:2 (2)

link_16 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.100998173575579,0.206909583242969,-0.271194305770592)
dA = chrono.ChVectorD(-1,-4.66293670342566e-15,-9.19930798204405e-13)
cB = chrono.ChVectorD(-0.105748173575595,0.229022267727915,-0.254416069148927)
dB = chrono.ChVectorD(-1,-5.02375918642883e-15,-9.19875287053173e-13)
link_16.Initialize(body_7,body_3,False,cA,cB,dA,dB)
link_16.SetName("Parallel15")
exported_items.append(link_16)


# Mate constraint: Distance10 [MateDistanceDim] type:5 align:1 flip:False
#   Entity 0: C::E name: body_7 , SW name: Spibot-LEG-1/upper_limb-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_8 , SW name: Spibot-LEG-1/lower_limb-1 ,  SW ref.type:2 (2)

link_17 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(-0.105898173575544,0.255365883672166,-0.310271562032114)
cB = chrono.ChVectorD(-0.105948173575443,0.264829349434615,-0.420265227910608)
dA = chrono.ChVectorD(-1,-4.66293670342566e-15,-9.19930798204405e-13)
dB = chrono.ChVectorD(1,4.9960036108132e-15,9.1882057517978e-13)
link_17.Initialize(body_7,body_8,False,cA,cB,dB)
link_17.SetDistance(0)
link_17.SetName("Distance10")
exported_items.append(link_17)

link_18 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.105898173575544,0.255365883672166,-0.310271562032114)
dA = chrono.ChVectorD(-1,-4.66293670342566e-15,-9.19930798204405e-13)
cB = chrono.ChVectorD(-0.105948173575443,0.264829349434615,-0.420265227910608)
dB = chrono.ChVectorD(1,4.9960036108132e-15,9.1882057517978e-13)
link_18.SetFlipped(True)
link_18.Initialize(body_7,body_8,False,cA,cB,dA,dB)
link_18.SetName("Distance10")
exported_items.append(link_18)


# Mate constraint: Distance11 [MateDistanceDim] type:5 align:1 flip:False
#   Entity 0: C::E name: body_5 , SW name: Spibot-LEG-1/Actuator_rod-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_8 , SW name: Spibot-LEG-1/lower_limb-1 ,  SW ref.type:2 (2)

link_19 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(-0.105898173575451,0.214825902990285,-0.410607106849563)
cB = chrono.ChVectorD(-0.105948173575443,0.264829349434615,-0.420265227910608)
dA = chrono.ChVectorD(-1,-5.02375918642883e-15,-9.19098130935936e-13)
dB = chrono.ChVectorD(1,4.9960036108132e-15,9.1882057517978e-13)
link_19.Initialize(body_5,body_8,False,cA,cB,dB)
link_19.SetDistance(0)
link_19.SetName("Distance11")
exported_items.append(link_19)

link_20 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.105898173575451,0.214825902990285,-0.410607106849563)
dA = chrono.ChVectorD(-1,-5.02375918642883e-15,-9.19098130935936e-13)
cB = chrono.ChVectorD(-0.105948173575443,0.264829349434615,-0.420265227910608)
dB = chrono.ChVectorD(1,4.9960036108132e-15,9.1882057517978e-13)
link_20.SetFlipped(True)
link_20.Initialize(body_5,body_8,False,cA,cB,dA,dB)
link_20.SetName("Distance11")
exported_items.append(link_20)


# Mate constraint: Distance12 [MateDistanceDim] type:5 align:1 flip:False
#   Entity 0: C::E name: body_7 , SW name: Spibot-LEG-1/upper_limb-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_1 , SW name: Spibot-LEG-1/limb_body_connector-1 ,  SW ref.type:2 (2)

link_21 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(-0.105898173575544,0.255365883672166,-0.310271562032114)
cB = chrono.ChVectorD(-0.105948173575626,0.245853290245033,-0.220218740660146)
dA = chrono.ChVectorD(-1,-4.66293670342566e-15,-9.19930798204405e-13)
dB = chrono.ChVectorD(1,5.16253706450698e-15,9.2015284280933e-13)
link_21.Initialize(body_7,body_1,False,cA,cB,dB)
link_21.SetDistance(0)
link_21.SetName("Distance12")
exported_items.append(link_21)

link_22 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.105898173575544,0.255365883672166,-0.310271562032114)
dA = chrono.ChVectorD(-1,-4.66293670342566e-15,-9.19930798204405e-13)
cB = chrono.ChVectorD(-0.105948173575626,0.245853290245033,-0.220218740660146)
dB = chrono.ChVectorD(1,5.16253706450698e-15,9.2015284280933e-13)
link_22.SetFlipped(True)
link_22.Initialize(body_7,body_1,False,cA,cB,dA,dB)
link_22.SetName("Distance12")
exported_items.append(link_22)


# Mate constraint: Distance13 [MateDistanceDim] type:5 align:1 flip:True
#   Entity 0: C::E name: body_2 , SW name: Spibot-LEG-1/Actuator_body_b-2 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_7 , SW name: Spibot-LEG-1/upper_limb-1 ,  SW ref.type:2 (2)

link_23 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(-0.100948173575672,0.215124446554234,-0.170051638238072)
cB = chrono.ChVectorD(-0.100998173575579,0.206909583242969,-0.271194305770592)
dA = chrono.ChVectorD(1,4.96824803519758e-15,9.19486708994555e-13)
dB = chrono.ChVectorD(-1,-4.66293670342566e-15,-9.19930798204405e-13)
link_23.Initialize(body_2,body_7,False,cA,cB,dB)
link_23.SetDistance(0)
link_23.SetName("Distance13")
exported_items.append(link_23)

link_24 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.100948173575672,0.215124446554234,-0.170051638238072)
dA = chrono.ChVectorD(1,4.96824803519758e-15,9.19486708994555e-13)
cB = chrono.ChVectorD(-0.100998173575579,0.206909583242969,-0.271194305770592)
dB = chrono.ChVectorD(-1,-4.66293670342566e-15,-9.19930798204405e-13)
link_24.SetFlipped(True)
link_24.Initialize(body_2,body_7,False,cA,cB,dA,dB)
link_24.SetName("Distance13")
exported_items.append(link_24)


# Mate constraint: Concentric21 [MateConcentric] type:1 align:1 flip:False
#   Entity 0: C::E name: body_7 , SW name: Spibot-LEG-1/upper_limb-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_6 , SW name: Spibot-LEG-1/Actuator_body-1 ,  SW ref.type:2 (2)

link_25 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.0984981735755792,0.206909583242969,-0.27119430577059)
dA = chrono.ChVectorD(-1,-4.66293670342566e-15,-9.19930798204405e-13)
cB = chrono.ChVectorD(-0.11109817357558,0.206909581568511,-0.271194311357309)
dB = chrono.ChVectorD(1,4.94049245958195e-15,9.19209153238398e-13)
link_25.SetFlipped(True)
link_25.Initialize(body_7,body_6,False,cA,cB,dA,dB)
link_25.SetName("Concentric21")
exported_items.append(link_25)

link_26 = chrono.ChLinkMateGeneric()
link_26.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.0984981735755792,0.206909583242969,-0.27119430577059)
cB = chrono.ChVectorD(-0.11109817357558,0.206909581568511,-0.271194311357309)
dA = chrono.ChVectorD(-1,-4.66293670342566e-15,-9.19930798204405e-13)
dB = chrono.ChVectorD(1,4.94049245958195e-15,9.19209153238398e-13)
link_26.Initialize(body_7,body_6,False,cA,cB,dA,dB)
link_26.SetName("Concentric21")
exported_items.append(link_26)


# Mate constraint: Concentric22 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_7 , SW name: Spibot-LEG-1/upper_limb-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_3 , SW name: Spibot-LEG-1/Actuator_rod_b-2 ,  SW ref.type:2 (2)

link_27 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.0984981735755948,0.229022267727915,-0.25441606914892)
dA = chrono.ChVectorD(-1,-4.66293670342566e-15,-9.19930798204405e-13)
cB = chrono.ChVectorD(-0.100948173575595,0.229022267727915,-0.254416069148922)
dB = chrono.ChVectorD(-1,-5.02375918642883e-15,-9.19875287053173e-13)
link_27.Initialize(body_7,body_3,False,cA,cB,dA,dB)
link_27.SetName("Concentric22")
exported_items.append(link_27)

link_28 = chrono.ChLinkMateGeneric()
link_28.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.0984981735755948,0.229022267727915,-0.25441606914892)
cB = chrono.ChVectorD(-0.100948173575595,0.229022267727915,-0.254416069148922)
dA = chrono.ChVectorD(-1,-4.66293670342566e-15,-9.19930798204405e-13)
dB = chrono.ChVectorD(-1,-5.02375918642883e-15,-9.19875287053173e-13)
link_28.Initialize(body_7,body_3,False,cA,cB,dA,dB)
link_28.SetName("Concentric22")
exported_items.append(link_28)

