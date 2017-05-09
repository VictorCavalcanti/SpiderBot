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
body_1.SetName('Spibot-LEG-4/lower_limb-1')
body_1.SetPos(chrono.ChVectorD(0.0767518309848005,0.158072913136618,0.189672424609489))
body_1.SetRot(chrono.ChQuaternionD(4.59715612550483e-13,-2.00534039767992e-15,0.999999970353798,0.000243500313603757))
body_1.SetMass(0.173763895224452)
body_1.SetInertiaXX(chrono.ChVectorD(0.000660134295478084,8.75830083245302e-06,0.00066065385403829))
body_1.SetInertiaXY(chrono.ChVectorD(7.08403843378737e-11,-6.70198789063151e-12,-3.12821476539226e-07))
body_1.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(4.14273289964873e-09,-0.0143933772184335,3.59893950746433e-07),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_1_1_shape = chrono.ChObjShapeFile() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_1_1_shape.SetColor(chrono.ChColor(0.898039215686275,0.917647058823529,0.929411764705882)) 
body_1_1_shape.SetFading(0.75) 
body_1_1_level = chrono.ChAssetLevel() 
body_1_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_1_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_1_1_level.GetAssets().push_back(body_1_1_shape) 
body_1.GetAssets().push_back(body_1_1_level) 

# Auxiliary marker (coordinate system feature)
marker_1_1 =chrono.ChMarker()
marker_1_1.SetName('LowerLimbCenterRef')
body_1.AddMarker(marker_1_1)
marker_1_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(0.0767518309848005,0.158072913136618,0.189672424609489),chrono.ChQuaternionD(-0.000172180723295276,0.707106760223519,-0.707106760223516,-0.000172180722645179)))

# Auxiliary marker (coordinate system feature)
marker_1_2 =chrono.ChMarker()
marker_1_2.SetName('LL-UL-Ref')
body_1.AddMarker(marker_1_2)
marker_1_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(0.0767518309848001,0.258072901278138,0.189721124670766),chrono.ChQuaternionD(-0.000172180723295276,0.707106760223519,-0.707106760223516,-0.000172180722645179)))

# Collision shapes 
body_1.GetCollisionModel().ClearModel()
body_1.GetCollisionModel().AddSphere(0.01, chrono.ChVectorD(3.46944695195361E-17,-0.1,0))
body_1.GetCollisionModel().BuildModel()
body_1.SetCollide(True)

exported_items.append(body_1)



# Rigid body part
body_2= chrono.ChBodyAuxRef()
body_2.SetName('Spibot-LEG-4/upper_limb-1')
body_2.SetPos(chrono.ChVectorD(0.0767518309848918,0.257531497332188,0.0897225902734927))
body_2.SetRot(chrono.ChQuaternionD(0.501351682816853,0.498644653171685,0.501351682816393,0.498644653172146))
body_2.SetMass(0.0769386604687246)
body_2.SetInertiaXX(chrono.ChVectorD(1.21361246296042e-05,0.000291222022970345,0.000279898353184369))
body_2.SetInertiaXY(chrono.ChVectorD(-1.51104850236057e-06,-1.20058215311761e-05,-6.50009440709708e-08))
body_2.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-0.00433891891647106,-0.0160004109829567,3.48337905591851e-19),chrono.ChQuaternionD(1,0,0,0)))

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
marker_2_1.SetName('UL-LL-Ref')
body_2.AddMarker(marker_2_1)
marker_2_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(0.0767518309847998,0.258072901277412,0.189721124671593),chrono.ChQuaternionD(0.707104190339522,-0.00191415901864596,0.707104190338872,-0.00191415901864504)))

# Auxiliary marker (coordinate system feature)
marker_2_2 =chrono.ChMarker()
marker_2_2.SetName('UL-LB-Ref')
body_2.AddMarker(marker_2_2)
marker_2_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(0.0767518309849838,0.256990093386964,-0.0102759441246079),chrono.ChQuaternionD(0.707104190339522,-0.00191415901864596,0.707104190338872,-0.00191415901864504)))

exported_items.append(body_2)



# Rigid body part
body_3= chrono.ChBodyAuxRef()
body_3.SetName('Spibot-LEG-4/Actuator_rod-1')
body_3.SetPos(chrono.ChVectorD(0.0768018309848877,0.211601875975492,0.0946134633178994))
body_3.SetRot(chrono.ChQuaternionD(0.999426563775094,-0.0338606500337523,-4.59521137990638e-13,-1.36219211425019e-14))
body_3.SetMass(0.00140945245841084)
body_3.SetInertiaXX(chrono.ChVectorD(2.33089158373325e-06,2.31640927196729e-06,3.41108000182889e-08))
body_3.SetInertiaXY(chrono.ChVectorD(1.43555569035984e-19,-2.11676351807725e-18,1.55542426052224e-07))
body_3.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-1.65060230227876e-19,-2.34447212110501e-18,0.0545976735175364),chrono.ChQuaternionD(1,0,0,0)))

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
marker_3_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(0.0768018309848366,0.215366713159027,0.150110910340096),chrono.ChQuaternionD(4.59521137990638E-13,1.36219211425019E-14,0.999426563775094,-0.0338606500337523)))

# Auxiliary marker (coordinate system feature)
marker_3_2 =chrono.ChMarker()
marker_3_2.SetName('LL-Act-Shaft')
body_3.AddMarker(marker_3_2)
marker_3_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(0.0768018309847999,0.218074011807861,0.190019186850439),chrono.ChQuaternionD(4.59521137990638E-13,1.36219211425019E-14,0.999426563775094,-0.0338606500337523)))

exported_items.append(body_3)



# Rigid body part
body_4= chrono.ChBodyAuxRef()
body_4.SetName('Spibot-LEG-4/Actuator_body-1')
body_4.SetPos(chrono.ChVectorD(0.0768018309271289,0.212039036824046,0.101057649619788))
body_4.SetRot(chrono.ChQuaternionD(1.35941496417016e-14,-4.59659995494634e-13,0.0338606500334549,0.999426563775104))
body_4.SetMass(0.00204159144576871)
body_4.SetInertiaXX(chrono.ChVectorD(8.08481090947278e-07,7.98194720293902e-07,8.93139775008301e-08))
body_4.SetInertiaXY(chrono.ChVectorD(4.49091554619882e-20,6.62816863313579e-19,-4.8311398298662e-08))
body_4.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-4.17192939730159e-18,5.58956732701871e-20,-0.0175577824053523),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_4_1_shape = chrono.ChObjShapeFile() 
body_4_1_shape.SetFilename(shapes_dir +'body_4_1.obj') 
body_4_1_shape.SetColor(chrono.ChColor(0.752941176470588,0.752941176470588,0.752941176470588)) 
body_4_1_shape.SetFading(0.75) 
body_4_1_level = chrono.ChAssetLevel() 
body_4_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_4_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_4_1_level.GetAssets().push_back(body_4_1_shape) 
body_4.GetAssets().push_back(body_4_1_level) 

# Auxiliary marker (coordinate system feature)
marker_4_1 =chrono.ChMarker()
marker_4_1.SetName('LL-Act-Base')
body_4.AddMarker(marker_4_1)
marker_4_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(0.0768018309271748,0.208654913513033,0.0511723039818569),chrono.ChQuaternionD(1.35941496417016E-14,-4.59659995494634E-13,0.0338606500334549,0.999426563775104)))

# Auxiliary marker (coordinate system feature)
marker_4_2 =chrono.ChMarker()
marker_4_2.SetName('UL-Act-Base')
body_4.AddMarker(marker_4_2)
marker_4_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(0.0768018309271656,0.209331738175236,0.0611493731094431),chrono.ChQuaternionD(1.35941496417016E-14,-4.59659995494634E-13,0.0338606500334549,0.999426563775104)))

exported_items.append(body_4)



# Rigid body part
body_5= chrono.ChBodyAuxRef()
body_5.SetName('Spibot-LEG-4/Actuator_rod-2')
body_5.SetPos(chrono.ChVectorD(0.0766518309849933,0.220949314256782,-0.0206285165274802))
body_5.SetRot(chrono.ChQuaternionD(3.79955302904412e-14,-4.58467790060022e-13,0.0869387495364259,0.996213658724394))
body_5.SetMass(0.00140945245841084)
body_5.SetInertiaXX(chrono.ChVectorD(2.33089158373325e-06,2.25784768904727e-06,9.26723829383097e-08))
body_5.SetInertiaXY(chrono.ChVectorD(3.67533642032845e-19,2.09106485183369e-18,-3.929618283261e-07))
body_5.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-1.65060230227876e-19,-2.34447212110501e-18,0.0545976735175364),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_3_1_shape = chrono.ChObjShapeFile() 
body_3_1_shape.SetFilename(shapes_dir +'body_3_1.obj') 
body_3_1_level = chrono.ChAssetLevel() 
body_3_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_3_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_3_1_level.GetAssets().push_back(body_3_1_shape) 
body_5.GetAssets().push_back(body_3_1_level) 

# Auxiliary marker (coordinate system feature)
marker_5_1 =chrono.ChMarker()
marker_5_1.SetName('UL-Act-Shaft')
body_5.AddMarker(marker_5_1)
marker_5_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(0.0766518309849428,0.23058462889265,0.0341556174610008),chrono.ChQuaternionD(0.0869387495364259,0.996213658724394,-3.79955302904412E-14,4.58467790060022E-13)))

# Auxiliary marker (coordinate system feature)
marker_5_2 =chrono.ChMarker()
marker_5_2.SetName('LL-Act-Shaft')
body_5.AddMarker(marker_5_2)
marker_5_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(0.0766518309849066,0.237513394473498,0.0735509497673242),chrono.ChQuaternionD(0.0869387495364259,0.996213658724394,-3.79955302904412E-14,4.58467790060022E-13)))

exported_items.append(body_5)



# Rigid body part
body_6= chrono.ChBodyAuxRef()
body_6.SetName('Spibot-LEG-4/Actuator_body-2')
body_6.SetPos(chrono.ChVectorD(0.076651830984984,0.222702898286502,-0.0106580499599832))
body_6.SetRot(chrono.ChQuaternionD(3.79746344900981e-14,-4.5845385952646e-13,0.0869387495364259,0.996213658724394))
body_6.SetMass(0.00204159144576871)
body_6.SetInertiaXX(chrono.ChVectorD(8.08481090947278e-07,7.80005522469939e-07,1.07503175324792e-07))
body_6.SetInertiaXY(chrono.ChVectorD(1.15078772659052e-19,6.54525487117181e-19,-1.22053743704784e-07))
body_6.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-4.17192939730159e-18,5.58956732701871e-20,-0.0175577824053523),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_4_1_shape = chrono.ChObjShapeFile() 
body_4_1_shape.SetFilename(shapes_dir +'body_4_1.obj') 
body_4_1_shape.SetColor(chrono.ChColor(0.843137254901961,0.843137254901961,0)) 
body_4_1_shape.SetFading(0.75) 
body_4_1_level = chrono.ChAssetLevel() 
body_4_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_4_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_4_1_level.GetAssets().push_back(body_4_1_shape) 
body_6.GetAssets().push_back(body_4_1_level) 

# Auxiliary marker (coordinate system feature)
marker_6_1 =chrono.ChMarker()
marker_6_1.SetName('LL-Act-Base')
body_6.AddMarker(marker_6_1)
marker_6_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(0.0766518309850293,0.214041941310441,-0.0599022153428874),chrono.ChQuaternionD(3.79746344900981E-14,-4.5845385952646E-13,0.0869387495364259,0.996213658724394)))

# Auxiliary marker (coordinate system feature)
marker_6_2 =chrono.ChMarker()
marker_6_2.SetName('UL-Act-Base')
body_6.AddMarker(marker_6_2)
marker_6_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(0.0766518309850202,0.215774132705653,-0.0500533822663066),chrono.ChQuaternionD(3.79746344900981E-14,-4.5845385952646E-13,0.0869387495364259,0.996213658724394)))

exported_items.append(body_6)



# Rigid body part
body_7= chrono.ChBodyAuxRef()
body_7.SetName('Spibot-LEG-4/limb_body_connector-1')
body_7.SetPos(chrono.ChVectorD(0.0666518309850388,0.24666539758002,-0.0702209243689553))
body_7.SetRot(chrono.ChQuaternionD(0.501351682816853,0.498644653171686,0.501351682816393,0.498644653172146))
body_7.SetMass(0.0319301494979552)
body_7.SetInertiaXX(chrono.ChVectorD(2.2110890182935e-06,4.65620459313165e-06,4.83154745183424e-06))
body_7.SetInertiaXY(chrono.ChVectorD(-1.32385342629295e-08,-9.5026827600349e-21,-1.61834070103109e-19))
body_7.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(0.01,0.00875766097763167,0.01),chrono.ChQuaternionD(1,0,0,0)))

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
marker_7_1.SetName('LB-UL-Ref')
body_7.AddMarker(marker_7_1)
marker_7_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(0.0766518309849836,0.256990093386964,-0.0102759441246081),chrono.ChQuaternionD(-0.498644653172146,0.501351682816853,-0.501351682816393,-0.498644653171686)))

# Auxiliary marker (coordinate system feature)
marker_7_2 =chrono.ChMarker()
marker_7_2.SetName('LB-B-Act-1')
body_7.AddMarker(marker_7_2)
marker_7_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(0.0766518309850388,0.25666525101983,-0.0702750647634685),chrono.ChQuaternionD(3.24808166086752E-13,-3.25865121160342E-13,0.709018349357842,0.705190031320552)))

exported_items.append(body_7)



# Rigid body part
body_8= chrono.ChBodyAuxRef()
body_8.SetName('Spibot-LEG-4/limb_body_connector-2')
body_8.SetPos(chrono.ChVectorD(0.0666518309850388,0.205665998476799,-0.0699989487514135))
body_8.SetRot(chrono.ChQuaternionD(0.501351682816852,0.498644653171686,0.501351682816393,0.498644653172147))
body_8.SetMass(0.0319301494979552)
body_8.SetInertiaXX(chrono.ChVectorD(2.2110890182935e-06,4.65620459313165e-06,4.83154745183424e-06))
body_8.SetInertiaXY(chrono.ChVectorD(-1.32385342629263e-08,-9.43694451520729e-21,-1.61614864057939e-19))
body_8.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(0.01,0.00875766097763167,0.01),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_7_1_shape = chrono.ChObjShapeFile() 
body_7_1_shape.SetFilename(shapes_dir +'body_7_1.obj') 
body_7_1_level = chrono.ChAssetLevel() 
body_7_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_7_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_7_1_level.GetAssets().push_back(body_7_1_shape) 
body_8.GetAssets().push_back(body_7_1_level) 

# Auxiliary marker (coordinate system feature)
marker_8_1 =chrono.ChMarker()
marker_8_1.SetName('LB-UL-Ref')
body_8.AddMarker(marker_8_1)
marker_8_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(0.0766518309850204,0.215774132705654,-0.0500533822663066),chrono.ChQuaternionD(-0.498644653172146,0.501351682816853,-0.501351682816392,-0.498644653171686)))

# Auxiliary marker (coordinate system feature)
marker_8_2 =chrono.ChMarker()
marker_8_2.SetName('LB-B-Act-1')
body_8.AddMarker(marker_8_2)
marker_8_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(0.0766518309850388,0.215665851916609,-0.0700530891459267),chrono.ChQuaternionD(3.24915818918322E-13,-3.25933627507704E-13,0.709018349357842,0.705190031320552)))

exported_items.append(body_8)



# Rigid body part
body_9= chrono.ChBodyAuxRef()
body_9.SetName('Spibot-LEG-3/Actuator_body-2')
body_9.SetPos(chrono.ChVectorD(0.0766518309850032,0.221626237847951,-0.209519670473169))
body_9.SetRot(chrono.ChQuaternionD(-0.0815439353092672,0.996669748018007,4.02679175161455e-14,4.58987494772641e-13))
body_9.SetMass(0.00204159144576871)
body_9.SetInertiaXX(chrono.ChVectorD(8.08481090947278e-07,7.82569697144767e-07,1.04939000649965e-07))
body_9.SetInertiaXY(chrono.ChVectorD(1.08221415218692e-19,6.56706144342555e-19,-1.14743748732899e-07))
body_9.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-4.17192939730159e-18,5.58956732701871e-20,-0.0175577824053523),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_4_1_shape = chrono.ChObjShapeFile() 
body_4_1_shape.SetFilename(shapes_dir +'body_4_1.obj') 
body_4_1_shape.SetColor(chrono.ChColor(0.843137254901961,0.843137254901961,0)) 
body_4_1_shape.SetFading(0.75) 
body_4_1_level = chrono.ChAssetLevel() 
body_4_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_4_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_4_1_level.GetAssets().push_back(body_4_1_shape) 
body_9.GetAssets().push_back(body_4_1_level) 

# Auxiliary marker (coordinate system feature)
marker_9_1 =chrono.ChMarker()
marker_9_1.SetName('LL-Act-Base')
body_9.AddMarker(marker_9_1)
marker_9_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(0.0766518309849577,0.213499000502243,-0.160184611811741),chrono.ChQuaternionD(-0.0815439353092672,0.996669748018007,4.02679175161455E-14,4.58987494772641E-13)))

# Auxiliary marker (coordinate system feature)
marker_9_2 =chrono.ChMarker()
marker_9_2.SetName('UL-Act-Base')
body_9.AddMarker(marker_9_2)
marker_9_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(0.0766518309849668,0.215124447971384,-0.170051623544027),chrono.ChQuaternionD(-0.0815439353092672,0.996669748018007,4.02679175161455E-14,4.58987494772641E-13)))

exported_items.append(body_9)



# Rigid body part
body_10= chrono.ChBodyAuxRef()
body_10.SetName('Spibot-LEG-3/Actuator_rod-2')
body_10.SetPos(chrono.ChVectorD(0.0766518309849943,0.21998071603615,-0.199530800742826))
body_10.SetRot(chrono.ChQuaternionD(-0.0815439353092672,0.996669748018007,4.01502232712358e-14,4.59080669045187e-13))
body_10.SetMass(0.00140945245841084)
body_10.SetInertiaXX(chrono.ChVectorD(2.33089158373325e-06,2.26610325530671e-06,8.44168166788694e-08))
body_10.SetInertiaXY(chrono.ChVectorD(3.45707171723462e-19,2.09843321165322e-18,-3.69426712548295e-07))
body_10.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-1.65060230227876e-19,-2.34447212110501e-18,0.0545976735175364),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_3_1_shape = chrono.ChObjShapeFile() 
body_3_1_shape.SetFilename(shapes_dir +'body_3_1.obj') 
body_3_1_level = chrono.ChAssetLevel() 
body_3_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_3_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_3_1_level.GetAssets().push_back(body_3_1_shape) 
body_10.GetAssets().push_back(body_3_1_level) 

# Auxiliary marker (coordinate system feature)
marker_10_1 =chrono.ChMarker()
marker_10_1.SetName('UL-Act-Shaft')
body_10.AddMarker(marker_10_1)
marker_10_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(0.0766518309850448,0.229022267583251,-0.254416053503665),chrono.ChQuaternionD(-4.01502232712358E-14,-4.59080669045187E-13,-0.0815439353092672,0.996669748018007)))

# Auxiliary marker (coordinate system feature)
marker_10_2 =chrono.ChMarker()
marker_10_2.SetName('LL-Act-Shaft')
body_10.AddMarker(marker_10_2)
marker_10_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(0.0766518309850812,0.235524057459818,-0.293884100432807),chrono.ChQuaternionD(-4.01502232712358E-14,-4.59080669045187E-13,-0.0815439353092672,0.996669748018007)))

exported_items.append(body_10)



# Rigid body part
body_11= chrono.ChBodyAuxRef()
body_11.SetName('Spibot-LEG-3/limb_body_connector-2')
body_11.SetPos(chrono.ChVectorD(0.0866518309849486,0.20523287532062,-0.149997776269876))
body_11.SetRot(chrono.ChQuaternionD(-0.498644653171685,0.501351682816853,0.498644653172146,-0.501351682816394))
body_11.SetMass(0.0319301494979552)
body_11.SetInertiaXX(chrono.ChVectorD(2.2110890182935e-06,4.65620459313165e-06,4.83154745183424e-06))
body_11.SetInertiaXY(chrono.ChVectorD(1.32385342629328e-08,1.18231687448505e-20,-1.61501932119795e-19))
body_11.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(0.01,0.00875766097763167,0.01),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_7_1_shape = chrono.ChObjShapeFile() 
body_7_1_shape.SetFilename(shapes_dir +'body_7_1.obj') 
body_7_1_level = chrono.ChAssetLevel() 
body_7_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_7_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_7_1_level.GetAssets().push_back(body_7_1_shape) 
body_11.GetAssets().push_back(body_7_1_level) 

# Auxiliary marker (coordinate system feature)
marker_11_1 =chrono.ChMarker()
marker_11_1.SetName('LB-UL-Ref')
body_11.AddMarker(marker_11_1)
marker_11_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(0.076651830984967,0.215124447971385,-0.170051623544027),chrono.ChQuaternionD(-0.498644653171686,0.501351682816392,0.501351682816854,0.498644653172145)))

# Auxiliary marker (coordinate system feature)
marker_11_2 =chrono.ChMarker()
marker_11_2.SetName('LB-B-Act-1')
body_11.AddMarker(marker_11_2)
marker_11_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(0.0766518309849486,0.21523272876043,-0.150051916664407),chrono.ChQuaternionD(0.705190031320551,-0.709018349357843,-3.26478346370859E-13,-3.24793831728823E-13)))

exported_items.append(body_11)



# Rigid body part
body_12= chrono.ChBodyAuxRef()
body_12.SetName('Spibot-LEG-3/limb_body_connector-1')
body_12.SetPos(chrono.ChVectorD(0.0866518309849486,0.246232274423841,-0.150219751887417))
body_12.SetRot(chrono.ChQuaternionD(-0.498644653171685,0.501351682816853,0.498644653172147,-0.501351682816393))
body_12.SetMass(0.0319301494979552)
body_12.SetInertiaXX(chrono.ChVectorD(2.2110890182935e-06,4.65620459313165e-06,4.83154745183423e-06))
body_12.SetInertiaXY(chrono.ChVectorD(1.32385342629299e-08,1.17474968675379e-20,-1.61462630740868e-19))
body_12.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(0.01,0.00875766097763167,0.01),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_7_1_shape = chrono.ChObjShapeFile() 
body_7_1_shape.SetFilename(shapes_dir +'body_7_1.obj') 
body_7_1_level = chrono.ChAssetLevel() 
body_7_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_7_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_7_1_level.GetAssets().push_back(body_7_1_shape) 
body_12.GetAssets().push_back(body_7_1_level) 

# Auxiliary marker (coordinate system feature)
marker_12_1 =chrono.ChMarker()
marker_12_1.SetName('LB-UL-Ref')
body_12.AddMarker(marker_12_1)
marker_12_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(0.0766518309850038,0.255907285496517,-0.210273012920809),chrono.ChQuaternionD(-0.498644653171686,0.501351682816392,0.501351682816854,0.498644653172146)))

# Auxiliary marker (coordinate system feature)
marker_12_2 =chrono.ChMarker()
marker_12_2.SetName('LB-B-Act-1')
body_12.AddMarker(marker_12_2)
marker_12_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(0.0766518309849486,0.256232127863651,-0.150273892281949),chrono.ChQuaternionD(0.705190031320552,-0.709018349357842,-3.26389843043606E-13,-3.24725379514077E-13)))

exported_items.append(body_12)



# Rigid body part
body_13= chrono.ChBodyAuxRef()
body_13.SetName('Spibot-LEG-3/Actuator_body-1')
body_13.SetPos(chrono.ChVectorD(0.0765018309851054,0.209744177360601,-0.321113877014873))
body_13.SetRot(chrono.ChQuaternionD(-0.0283573753951083,0.999597848767544,1.5685722540752e-14,4.6042739959198e-13))
body_13.SetMass(0.00204159144576871)
body_13.SetInertiaXX(chrono.ChVectorD(8.08481090947278e-07,7.99172677507276e-07,8.83360202874553e-08))
body_13.SetInertiaXY(chrono.ChVectorD(3.77643801582259e-20,6.64410961950231e-19,-4.04941942681146e-08))
body_13.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-4.17192939730159e-18,5.58956732701871e-20,-0.0175577824053523),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_4_1_shape = chrono.ChObjShapeFile() 
body_4_1_shape.SetFilename(shapes_dir +'body_4_1.obj') 
body_4_1_shape.SetColor(chrono.ChColor(0.752941176470588,0.752941176470588,0.752941176470588)) 
body_4_1_shape.SetFading(0.75) 
body_4_1_level = chrono.ChAssetLevel() 
body_4_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_4_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_4_1_level.GetAssets().push_back(body_4_1_shape) 
body_13.GetAssets().push_back(body_4_1_level) 

# Auxiliary marker (coordinate system feature)
marker_13_1 =chrono.ChMarker()
marker_13_1.SetName('LL-Act-Base')
body_13.AddMarker(marker_13_1)
marker_13_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(0.0765018309850595,0.206909580216436,-0.271194291088803),chrono.ChQuaternionD(-0.0283573753951083,0.999597848767544,1.5685722540752E-14,4.6042739959198E-13)))

# Auxiliary marker (coordinate system feature)
marker_13_2 =chrono.ChMarker()
marker_13_2.SetName('UL-Act-Base')
body_13.AddMarker(marker_13_2)
marker_13_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(0.0765018309850686,0.207476499645269,-0.281178208274017),chrono.ChQuaternionD(-0.0283573753951083,0.999597848767544,1.5685722540752E-14,4.6042739959198E-13)))

exported_items.append(body_13)



# Rigid body part
body_14= chrono.ChBodyAuxRef()
body_14.SetName('Spibot-LEG-3/lower_limb-1')
body_14.SetPos(chrono.ChVectorD(0.0765518309851901,0.154824489464548,-0.410318781778193))
body_14.SetRot(chrono.ChQuaternionD(0.999999970353798,0.000243500313129109,-4.59687856974045e-13,1.87350140959715e-15))
body_14.SetMass(0.173763895224452)
body_14.SetInertiaXX(chrono.ChVectorD(0.000660134295478084,8.75830083245243e-06,0.00066065385403829))
body_14.SetInertiaXY(chrono.ChVectorD(-7.08403841197001e-11,-6.70198781740738e-12,3.1282147592031e-07))
body_14.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(4.14273289964873e-09,-0.0143933772184335,3.59893950746433e-07),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_1_1_shape = chrono.ChObjShapeFile() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_1_1_shape.SetColor(chrono.ChColor(0.898039215686275,0.917647058823529,0.929411764705882)) 
body_1_1_shape.SetFading(0.75) 
body_1_1_level = chrono.ChAssetLevel() 
body_1_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_1_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_1_1_level.GetAssets().push_back(body_1_1_shape) 
body_14.GetAssets().push_back(body_1_1_level) 

# Auxiliary marker (coordinate system feature)
marker_14_1 =chrono.ChMarker()
marker_14_1.SetName('LowerLimbCenterRef')
body_14.AddMarker(marker_14_1)
marker_14_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(0.0765518309851901,0.154824489464548,-0.410318781778193),chrono.ChQuaternionD(0.707106760223519,0.000172180722959689,0.000172180722309552,-0.707106760223516)))

# Auxiliary marker (coordinate system feature)
marker_14_2 =chrono.ChMarker()
marker_14_2.SetName('LL-UL-Ref')
body_14.AddMarker(marker_14_2)
marker_14_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(0.0765518309851898,0.254824477606067,-0.410270081717011),chrono.ChQuaternionD(0.707106760223519,0.000172180722959688,0.000172180722309552,-0.707106760223516)))

# Collision shapes 
body_14.GetCollisionModel().ClearModel()
body_14.GetCollisionModel().AddSphere(0.01, chrono.ChVectorD(3.46944695195361E-17,-0.1,0))
body_14.GetCollisionModel().BuildModel()
body_14.SetCollide(True)

exported_items.append(body_14)



# Rigid body part
body_15= chrono.ChBodyAuxRef()
body_15.SetName('Spibot-LEG-3/Actuator_rod-1')
body_15.SetPos(chrono.ChVectorD(0.0765018309851003,0.209404730142535,-0.315135893163521))
body_15.SetRot(chrono.ChQuaternionD(4.60396506877195e-13,-1.57959131201817e-14,0.999597848767544,0.0283573753951083))
body_15.SetMass(0.00140945245841084)
body_15.SetInertiaXX(chrono.ChVectorD(2.33089158373325e-06,2.31955788374232e-06,3.09621882432615e-08))
body_15.SetInertiaXY(chrono.ChVectorD(1.20545829015392e-19,-2.12253054984026e-18,1.30374309981668e-07))
body_15.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-1.65060230227876e-19,-2.34447212110501e-18,0.0545976735175364),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_3_1_shape = chrono.ChObjShapeFile() 
body_3_1_shape.SetFilename(shapes_dir +'body_3_1.obj') 
body_3_1_level = chrono.ChAssetLevel() 
body_3_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_3_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_3_1_level.GetAssets().push_back(body_3_1_shape) 
body_15.GetAssets().push_back(body_3_1_level) 

# Auxiliary marker (coordinate system feature)
marker_15_1 =chrono.ChMarker()
marker_15_1.SetName('UL-Act-Shaft')
body_15.AddMarker(marker_15_1)
marker_15_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(0.0765018309851515,0.212558219465418,-0.370671432506274),chrono.ChQuaternionD(0.999597848767544,0.0283573753951083,-4.60396506877195E-13,1.57959131201817E-14)))

# Auxiliary marker (coordinate system feature)
marker_15_2 =chrono.ChMarker()
marker_15_2.SetName('LL-Act-Shaft')
body_15.AddMarker(marker_15_2)
marker_15_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(0.0765018309851883,0.21482589718075,-0.41060710124713),chrono.ChQuaternionD(0.999597848767544,0.0283573753951083,-4.60396506877195E-13,1.57959131201817E-14)))

exported_items.append(body_15)



# Rigid body part
body_16= chrono.ChBodyAuxRef()
body_16.SetName('Spibot-LEG-3/upper_limb-1')
body_16.SetPos(chrono.ChVectorD(0.0765518309850958,0.255365881551293,-0.31027154731891))
body_16.SetRot(chrono.ChQuaternionD(-0.498644653171685,0.501351682816853,0.498644653172147,-0.501351682816393))
body_16.SetMass(0.0769386604687246)
body_16.SetInertiaXX(chrono.ChVectorD(1.21361246296042e-05,0.000291222022970345,0.000279898353184369))
body_16.SetInertiaXY(chrono.ChVectorD(1.51104850236051e-06,1.20058215311765e-05,-6.50009440709573e-08))
body_16.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-0.00433891891647106,-0.0160004109829567,3.48337905591851e-19),chrono.ChQuaternionD(1,0,0,0)))

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
marker_16_1.SetName('UL-LL-Ref')
body_16.AddMarker(marker_16_1)
marker_16_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(0.0765518309851879,0.254824477606069,-0.410270081717011),chrono.ChQuaternionD(0.707104190338871,-0.00191415901864447,-0.707104190339523,0.00191415901864643)))

# Auxiliary marker (coordinate system feature)
marker_16_2 =chrono.ChMarker()
marker_16_2.SetName('UL-LB-Ref')
body_16.AddMarker(marker_16_2)
marker_16_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(0.0765518309850036,0.255907285496516,-0.210273012920809),chrono.ChQuaternionD(0.707104190338871,-0.00191415901864447,-0.707104190339523,0.00191415901864643)))

exported_items.append(body_16)



# Rigid body part
body_17= chrono.ChBodyAuxRef()
body_17.SetName('Spibot-LEG-2/Actuator_rod-1')
body_17.SetPos(chrono.ChVectorD(-0.0134981653625017,0.20940473093857,-0.315135892023723))
body_17.SetRot(chrono.ChQuaternionD(4.59900548489089e-13,-1.52786498101866e-14,0.999597848778317,0.0283573750153508))
body_17.SetMass(0.00140945245841084)
body_17.SetInertiaXX(chrono.ChVectorD(2.33089158373325e-06,2.31955788394044e-06,3.09621880451393e-08))
body_17.SetInertiaXY(chrono.ChVectorD(1.20376902757946e-19,-2.12039041734084e-18,1.30374308242746e-07))
body_17.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-1.65060230227876e-19,-2.34447212110501e-18,0.0545976735175364),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_3_1_shape = chrono.ChObjShapeFile() 
body_3_1_shape.SetFilename(shapes_dir +'body_3_1.obj') 
body_3_1_level = chrono.ChAssetLevel() 
body_3_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_3_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_3_1_level.GetAssets().push_back(body_3_1_shape) 
body_17.GetAssets().push_back(body_3_1_level) 

# Auxiliary marker (coordinate system feature)
marker_17_1 =chrono.ChMarker()
marker_17_1.SetName('UL-Act-Shaft')
body_17.AddMarker(marker_17_1)
marker_17_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.0134981653624506,0.212558220219256,-0.370671431368872),chrono.ChQuaternionD(0.999597848778317,0.0283573750153508,-4.59900548489089E-13,1.52786498101866E-14)))

# Auxiliary marker (coordinate system feature)
marker_17_2 =chrono.ChMarker()
marker_17_2.SetName('LL-Act-Shaft')
body_17.AddMarker(marker_17_2)
marker_17_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.0134981653624139,0.214825897904244,-0.410607100111451),chrono.ChQuaternionD(0.999597848778317,0.0283573750153508,-4.59900548489089E-13,1.52786498101866E-14)))

exported_items.append(body_17)



# Rigid body part
body_18= chrono.ChBodyAuxRef()
body_18.SetName('Spibot-LEG-2/Actuator_body-1')
body_18.SetPos(chrono.ChVectorD(-0.0134981690148943,0.209744178291282,-0.321113876206431))
body_18.SetRot(chrono.ChQuaternionD(-0.0283573750153507,0.999597848778317,1.56187924002362e-14,4.59858898376022e-13))
body_18.SetMass(0.00204159144576871)
body_18.SetInertiaXX(chrono.ChVectorD(8.08481090947278e-07,7.99172677568813e-07,8.83360202259187e-08))
body_18.SetInertiaXY(chrono.ChVectorD(3.77772239771025e-20,6.63659162324702e-19,-4.04941937280061e-08))
body_18.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-4.17192939730159e-18,5.58956732701871e-20,-0.0175577824053523),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_4_1_shape = chrono.ChObjShapeFile() 
body_4_1_shape.SetFilename(shapes_dir +'body_4_1.obj') 
body_4_1_shape.SetColor(chrono.ChColor(0.752941176470588,0.752941176470588,0.752941176470588)) 
body_4_1_shape.SetFading(0.75) 
body_4_1_level = chrono.ChAssetLevel() 
body_4_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_4_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_4_1_level.GetAssets().push_back(body_4_1_shape) 
body_18.GetAssets().push_back(body_4_1_level) 

# Auxiliary marker (coordinate system feature)
marker_18_1 =chrono.ChMarker()
marker_18_1.SetName('LL-Act-Base')
body_18.AddMarker(marker_18_1)
marker_18_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.0134981690149402,0.206909581185048,-0.271194290278207),chrono.ChQuaternionD(-0.0283573750153507,0.999597848778317,1.56187924002362E-14,4.59858898376022E-13)))

# Auxiliary marker (coordinate system feature)
marker_18_2 =chrono.ChMarker()
marker_18_2.SetName('UL-Act-Base')
body_18.AddMarker(marker_18_2)
marker_18_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.0134981690149311,0.207476500606295,-0.281178207463852),chrono.ChQuaternionD(-0.0283573750153507,0.999597848778317,1.56187924002362E-14,4.59858898376022E-13)))

exported_items.append(body_18)



# Rigid body part
body_19= chrono.ChBodyAuxRef()
body_19.SetName('Spibot-LEG-2/limb_body_connector-1')
body_19.SetPos(chrono.ChVectorD(-0.00334816901505142,0.246232274423842,-0.150219751887316))
body_19.SetRot(chrono.ChQuaternionD(-0.498644653171685,0.501351682816852,0.498644653172147,-0.501351682816394))
body_19.SetMass(0.0319301494979552)
body_19.SetInertiaXX(chrono.ChVectorD(2.2110890182935e-06,4.65620459313165e-06,4.83154745183424e-06))
body_19.SetInertiaXY(chrono.ChVectorD(1.32385342629295e-08,1.31350727244605e-20,-1.62134993374948e-19))
body_19.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(0.01,0.00875766097763167,0.01),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_7_1_shape = chrono.ChObjShapeFile() 
body_7_1_shape.SetFilename(shapes_dir +'body_7_1.obj') 
body_7_1_level = chrono.ChAssetLevel() 
body_7_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_7_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_7_1_level.GetAssets().push_back(body_7_1_shape) 
body_19.GetAssets().push_back(body_7_1_level) 

# Auxiliary marker (coordinate system feature)
marker_19_1 =chrono.ChMarker()
marker_19_1.SetName('LB-UL-Ref')
body_19.AddMarker(marker_19_1)
marker_19_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.0133481690149962,0.255907285496517,-0.210273012920708),chrono.ChQuaternionD(-0.498644653171687,0.501351682816392,0.501351682816854,0.498644653172145)))

# Auxiliary marker (coordinate system feature)
marker_19_2 =chrono.ChMarker()
marker_19_2.SetName('LB-B-Act-1')
body_19.AddMarker(marker_19_2)
marker_19_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.0133481690150514,0.256232127863652,-0.150273892281847),chrono.ChQuaternionD(0.705190031320552,-0.709018349357842,-3.26423880293882E-13,-3.245051289628E-13)))

exported_items.append(body_19)



# Rigid body part
body_20= chrono.ChBodyAuxRef()
body_20.SetName('Spibot-LEG-2/limb_body_connector-2')
body_20.SetPos(chrono.ChVectorD(-0.00334816901505131,0.20523287532062,-0.149997776269774))
body_20.SetRot(chrono.ChQuaternionD(-0.498644653171685,0.501351682816853,0.498644653172147,-0.501351682816394))
body_20.SetMass(0.0319301494979552)
body_20.SetInertiaXX(chrono.ChVectorD(2.2110890182935e-06,4.65620459313165e-06,4.83154745183424e-06))
body_20.SetInertiaXY(chrono.ChVectorD(1.32385342629326e-08,1.32134055263932e-20,-1.62173594299468e-19))
body_20.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(0.01,0.00875766097763167,0.01),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_7_1_shape = chrono.ChObjShapeFile() 
body_7_1_shape.SetFilename(shapes_dir +'body_7_1.obj') 
body_7_1_level = chrono.ChAssetLevel() 
body_7_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_7_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_7_1_level.GetAssets().push_back(body_7_1_shape) 
body_20.GetAssets().push_back(body_7_1_level) 

# Auxiliary marker (coordinate system feature)
marker_20_1 =chrono.ChMarker()
marker_20_1.SetName('LB-UL-Ref')
body_20.AddMarker(marker_20_1)
marker_20_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.0133481690150329,0.215124447971386,-0.170051623543926),chrono.ChQuaternionD(-0.498644653171686,0.501351682816392,0.501351682816854,0.498644653172145)))

# Auxiliary marker (coordinate system feature)
marker_20_2 =chrono.ChMarker()
marker_20_2.SetName('LB-B-Act-1')
body_20.AddMarker(marker_20_2)
marker_20_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.0133481690150513,0.21523272876043,-0.150051916664306),chrono.ChQuaternionD(0.705190031320551,-0.709018349357843,-3.26512438047624E-13,-3.24574007215711E-13)))

exported_items.append(body_20)



# Rigid body part
body_21= chrono.ChBodyAuxRef()
body_21.SetName('Spibot-LEG-2/lower_limb-1')
body_21.SetPos(chrono.ChVectorD(-0.0134481690148116,0.154824489485807,-0.410318781770277))
body_21.SetRot(chrono.ChQuaternionD(0.999999970353792,0.000243500340069838,-4.60118068408844e-13,2.5396352441206e-15))
body_21.SetMass(0.173763895224452)
body_21.SetInertiaXX(chrono.ChVectorD(0.000660134295478084,8.75830083248614e-06,0.000660653854038257))
body_21.SetInertiaXY(chrono.ChVectorD(-7.08403850061876e-11,-6.70198792313265e-12,3.12821511045432e-07))
body_21.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(4.14273289964873e-09,-0.0143933772184335,3.59893950746433e-07),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_1_1_shape = chrono.ChObjShapeFile() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_1_1_shape.SetColor(chrono.ChColor(0.898039215686275,0.917647058823529,0.929411764705882)) 
body_1_1_shape.SetFading(0.75) 
body_1_1_level = chrono.ChAssetLevel() 
body_1_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_1_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_1_1_level.GetAssets().push_back(body_1_1_shape) 
body_21.GetAssets().push_back(body_1_1_level) 

# Auxiliary marker (coordinate system feature)
marker_21_1 =chrono.ChMarker()
marker_21_1.SetName('LowerLimbCenterRef')
body_21.AddMarker(marker_21_1)
marker_21_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.0134481690148116,0.154824489485807,-0.410318781770277),chrono.ChQuaternionD(0.707106760223514,0.000172180742009916,0.000172180741359211,-0.707106760223511)))

# Auxiliary marker (coordinate system feature)
marker_21_2 =chrono.ChMarker()
marker_21_2.SetName('LL-UL-Ref')
body_21.AddMarker(marker_21_2)
marker_21_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.0134481690148121,0.254824477627324,-0.410270081703707),chrono.ChQuaternionD(0.707106760223514,0.000172180742009916,0.000172180741359211,-0.707106760223511)))

# Collision shapes 
body_21.GetCollisionModel().ClearModel()
body_21.GetCollisionModel().AddSphere(0.01, chrono.ChVectorD(3.46944695195361E-17,-0.1,0))
body_21.GetCollisionModel().BuildModel()
body_21.SetCollide(True)

exported_items.append(body_21)



# Rigid body part
body_22= chrono.ChBodyAuxRef()
body_22.SetName('Spibot-LEG-2/upper_limb-1')
body_22.SetPos(chrono.ChVectorD(-0.0134481690149042,0.255365881476422,-0.310271547318403))
body_22.SetRot(chrono.ChQuaternionD(-0.498644652983999,0.501351683003525,0.49864465298446,-0.501351683003066))
body_22.SetMass(0.0769386604687246)
body_22.SetInertiaXX(chrono.ChVectorD(1.21361246318669e-05,0.000291222022968082,0.000279898353184369))
body_22.SetInertiaXY(chrono.ChVectorD(1.51104871131796e-06,1.20058215311278e-05,-6.50009530599927e-08))
body_22.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-0.00433891891647106,-0.0160004109829567,3.48337905591851e-19),chrono.ChQuaternionD(1,0,0,0)))

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
marker_22_1.SetName('UL-LL-Ref')
body_22.AddMarker(marker_22_1)
marker_22_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.0134481690148122,0.254824477456328,-0.410270081716099),chrono.ChQuaternionD(0.707104190338155,-0.00191415928335639,-0.707104190338806,0.0019141592833582)))

# Auxiliary marker (coordinate system feature)
marker_22_2 =chrono.ChMarker()
marker_22_2.SetName('UL-LB-Ref')
body_22.AddMarker(marker_22_2)
marker_22_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.0134481690149962,0.255907285496517,-0.210273012920708),chrono.ChQuaternionD(0.707104190338155,-0.00191415928335639,-0.707104190338806,0.0019141592833582)))

exported_items.append(body_22)



# Rigid body part
body_23= chrono.ChBodyAuxRef()
body_23.SetName('Spibot-LEG-2/Actuator_rod-2')
body_23.SetPos(chrono.ChVectorD(-0.0133481690150116,0.219980719469194,-0.199530794446692))
body_23.SetRot(chrono.ChQuaternionD(-0.0815439351382681,0.996669748031998,4.03382879420433e-14,4.58202292478018e-13))
body_23.SetMass(0.00140945245841084)
body_23.SetInertiaXX(chrono.ChVectorD(2.33089158373325e-06,2.26610325556024e-06,8.44168164253385e-08))
body_23.SetInertiaXY(chrono.ChVectorD(3.45149963935294e-19,2.09464163748155e-18,-3.69426711799669e-07))
body_23.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-1.65060230227876e-19,-2.34447212110501e-18,0.0545976735175364),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_3_1_shape = chrono.ChObjShapeFile() 
body_3_1_shape.SetFilename(shapes_dir +'body_3_1.obj') 
body_3_1_level = chrono.ChAssetLevel() 
body_3_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_3_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_3_1_level.GetAssets().push_back(body_3_1_shape) 
body_23.GetAssets().push_back(body_3_1_level) 

# Auxiliary marker (coordinate system feature)
marker_23_1 =chrono.ChMarker()
marker_23_1.SetName('UL-Act-Shaft')
body_23.AddMarker(marker_23_1)
marker_23_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.0133481690149611,0.229022270997461,-0.254416047210633),chrono.ChQuaternionD(-4.03382879420433E-14,-4.58202292478018E-13,-0.0815439351382681,0.996669748031998)))

# Auxiliary marker (coordinate system feature)
marker_23_2 =chrono.ChMarker()
marker_23_2.SetName('LL-Act-Shaft')
body_23.AddMarker(marker_23_2)
marker_23_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.0133481690149249,0.235524060860485,-0.293884094142006),chrono.ChQuaternionD(-4.03382879420433E-14,-4.58202292478018E-13,-0.0815439351382681,0.996669748031998)))

exported_items.append(body_23)



# Rigid body part
body_24= chrono.ChBodyAuxRef()
body_24.SetName('Spibot-LEG-2/Actuator_body-2')
body_24.SetPos(chrono.ChVectorD(-0.0133481690150018,0.2216262415423,-0.209519665784619))
body_24.SetRot(chrono.ChQuaternionD(-0.081543935138268,0.996669748031998,4.03661362595732e-14,4.58230140795548e-13))
body_24.SetMass(0.00204159144576871)
body_24.SetInertiaXX(chrono.ChVectorD(8.08481090947278e-07,7.82569697223513e-07,1.04939000571219e-07))
body_24.SetInertiaXY(chrono.ChVectorD(1.08071443447886e-19,6.55693431284746e-19,-1.14743748500376e-07))
body_24.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-4.17192939730159e-18,5.58956732701871e-20,-0.0175577824053523),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_4_1_shape = chrono.ChObjShapeFile() 
body_4_1_shape.SetFilename(shapes_dir +'body_4_1.obj') 
body_4_1_shape.SetColor(chrono.ChColor(0.843137254901961,0.843137254901961,0)) 
body_4_1_shape.SetFading(0.75) 
body_4_1_level = chrono.ChAssetLevel() 
body_4_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_4_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_4_1_level.GetAssets().push_back(body_4_1_shape) 
body_24.GetAssets().push_back(body_4_1_level) 

# Auxiliary marker (coordinate system feature)
marker_24_1 =chrono.ChMarker()
marker_24_1.SetName('LL-Act-Base')
body_24.AddMarker(marker_24_1)
marker_24_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.0133481690150471,0.213499004213521,-0.160184607120402),chrono.ChQuaternionD(-0.081543935138268,0.996669748031998,4.03661362595732E-14,4.58230140795548E-13)))

# Auxiliary marker (coordinate system feature)
marker_24_2 =chrono.ChMarker()
marker_24_2.SetName('UL-Act-Base')
body_24.AddMarker(marker_24_2)
marker_24_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.0133481690150381,0.215124451679277,-0.170051618853246),chrono.ChQuaternionD(-0.081543935138268,0.996669748031998,4.03661362595732E-14,4.58230140795548E-13)))

exported_items.append(body_24)



# Rigid body part
body_25= chrono.ChBodyAuxRef()
body_25.SetName('Spibot-LEG-1/limb_body_connector-1')
body_25.SetPos(chrono.ChVectorD(-0.0933481690150514,0.246232274423842,-0.150219751887214))
body_25.SetRot(chrono.ChQuaternionD(-0.498644653171685,0.501351682816852,0.498644653172147,-0.501351682816393))
body_25.SetMass(0.0319301494979552)
body_25.SetInertiaXX(chrono.ChVectorD(2.2110890182935e-06,4.65620459313164e-06,4.83154745183423e-06))
body_25.SetInertiaXY(chrono.ChVectorD(1.32385342629299e-08,1.30522695294681e-20,-1.61410843813686e-19))
body_25.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(0.01,0.00875766097763167,0.01),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_7_1_shape = chrono.ChObjShapeFile() 
body_7_1_shape.SetFilename(shapes_dir +'body_7_1.obj') 
body_7_1_level = chrono.ChAssetLevel() 
body_7_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_7_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_7_1_level.GetAssets().push_back(body_7_1_shape) 
body_25.GetAssets().push_back(body_7_1_level) 

# Auxiliary marker (coordinate system feature)
marker_25_1 =chrono.ChMarker()
marker_25_1.SetName('LB-UL-Ref')
body_25.AddMarker(marker_25_1)
marker_25_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.103348169014996,0.255907285496518,-0.210273012920606),chrono.ChQuaternionD(-0.498644653171686,0.501351682816392,0.501351682816854,0.498644653172145)))

# Auxiliary marker (coordinate system feature)
marker_25_2 =chrono.ChMarker()
marker_25_2.SetName('LB-B-Act-1')
body_25.AddMarker(marker_25_2)
marker_25_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.103348169015051,0.256232127863652,-0.150273892281746),chrono.ChQuaternionD(0.705190031320552,-0.709018349357842,-3.26447924366294E-13,-3.24430828870974E-13)))

exported_items.append(body_25)



# Rigid body part
body_26= chrono.ChBodyAuxRef()
body_26.SetName('Spibot-LEG-1/Actuator_body-2')
body_26.SetPos(chrono.ChVectorD(-0.103348169014997,0.221626237820866,-0.209519670477429))
body_26.SetRot(chrono.ChQuaternionD(-0.0815439349672634,0.996669748045989,3.99205631785346e-14,4.5827191326541e-13))
body_26.SetMass(0.00204159144576871)
body_26.SetInertiaXX(chrono.ChVectorD(8.08481090947277e-07,7.82569697302263e-07,1.04939000492469e-07))
body_26.SetInertiaXY(chrono.ChVectorD(1.08055751441072e-19,6.55712362917514e-19,-1.14743748267846e-07))
body_26.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-4.17192939730159e-18,5.58956732701871e-20,-0.0175577824053523),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_4_1_shape = chrono.ChObjShapeFile() 
body_4_1_shape.SetFilename(shapes_dir +'body_4_1.obj') 
body_4_1_shape.SetColor(chrono.ChColor(0.843137254901961,0.843137254901961,0)) 
body_4_1_shape.SetFading(0.75) 
body_4_1_level = chrono.ChAssetLevel() 
body_4_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_4_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_4_1_level.GetAssets().push_back(body_4_1_shape) 
body_26.GetAssets().push_back(body_4_1_level) 

# Auxiliary marker (coordinate system feature)
marker_26_1 =chrono.ChMarker()
marker_26_1.SetName('LL-Act-Base')
body_26.AddMarker(marker_26_1)
marker_26_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.103348169015042,0.213499000509016,-0.160184611810423),chrono.ChQuaternionD(-0.0815439349672634,0.996669748045989,3.99205631785346E-14,4.5827191326541E-13)))

# Auxiliary marker (coordinate system feature)
marker_26_2 =chrono.ChMarker()
marker_26_2.SetName('UL-Act-Base')
body_26.AddMarker(marker_26_2)
marker_26_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.103348169015033,0.215124447971386,-0.170051623543824),chrono.ChQuaternionD(-0.0815439349672634,0.996669748045989,3.99205631785346E-14,4.5827191326541E-13)))

exported_items.append(body_26)



# Rigid body part
body_27= chrono.ChBodyAuxRef()
body_27.SetName('Spibot-LEG-1/Actuator_rod-2')
body_27.SetPos(chrono.ChVectorD(-0.103348169015006,0.219980716007717,-0.19953080069616))
body_27.SetRot(chrono.ChQuaternionD(-0.0815439349672634,0.996669748045989,3.98977353456365e-14,4.58377270444487e-13))
body_27.SetMass(0.00140945245841084)
body_27.SetInertiaXX(chrono.ChVectorD(2.33089158373325e-06,2.26610325581378e-06,8.44168161717993e-08))
body_27.SetInertiaXY(chrono.ChVectorD(3.45164364899445e-19,2.09514759750721e-18,-3.69426711051019e-07))
body_27.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-1.65060230227876e-19,-2.34447212110501e-18,0.0545976735175364),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_3_1_shape = chrono.ChObjShapeFile() 
body_3_1_shape.SetFilename(shapes_dir +'body_3_1.obj') 
body_3_1_level = chrono.ChAssetLevel() 
body_3_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_3_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_3_1_level.GetAssets().push_back(body_3_1_shape) 
body_27.GetAssets().push_back(body_3_1_level) 

# Auxiliary marker (coordinate system feature)
marker_27_1 =chrono.ChMarker()
marker_27_1.SetName('UL-Act-Shaft')
body_27.AddMarker(marker_27_1)
marker_27_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.103348169014956,0.229022267517151,-0.254416053463204),chrono.ChQuaternionD(-3.98977353456365E-14,-4.58377270444487E-13,-0.0815439349672634,0.996669748045989)))

# Auxiliary marker (coordinate system feature)
marker_27_2 =chrono.ChMarker()
marker_27_2.SetName('LL-Act-Shaft')
body_27.AddMarker(marker_27_2)
marker_27_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.103348169014919,0.235524057366631,-0.293884100396808),chrono.ChQuaternionD(-3.98977353456365E-14,-4.58377270444487E-13,-0.0815439349672634,0.996669748045989)))

exported_items.append(body_27)



# Rigid body part
body_28= chrono.ChBodyAuxRef()
body_28.SetName('Spibot-LEG-1/Actuator_body-1')
body_28.SetPos(chrono.ChVectorD(-0.103498169014894,0.209744179221956,-0.321113875397993))
body_28.SetRot(chrono.ChQuaternionD(-0.0283573746355862,0.99959784878909,1.54147714359e-14,4.59685384111915e-13))
body_28.SetMass(0.00204159144576871)
body_28.SetInertiaXX(chrono.ChVectorD(8.08481090947278e-07,7.99172677630351e-07,8.83360201643809e-08))
body_28.SetInertiaXY(chrono.ChVectorD(3.76994970059914e-20,6.63330101430141e-19,-4.04941931878879e-08))
body_28.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-4.17192939730159e-18,5.58956732701871e-20,-0.0175577824053523),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_4_1_shape = chrono.ChObjShapeFile() 
body_4_1_shape.SetFilename(shapes_dir +'body_4_1.obj') 
body_4_1_shape.SetColor(chrono.ChColor(0.752941176470588,0.752941176470588,0.752941176470588)) 
body_4_1_shape.SetFading(0.75) 
body_4_1_level = chrono.ChAssetLevel() 
body_4_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_4_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_4_1_level.GetAssets().push_back(body_4_1_shape) 
body_28.GetAssets().push_back(body_4_1_level) 

# Auxiliary marker (coordinate system feature)
marker_28_1 =chrono.ChMarker()
marker_28_1.SetName('LL-Act-Base')
body_28.AddMarker(marker_28_1)
marker_28_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.10349816901494,0.206909582153653,-0.271194289467615),chrono.ChQuaternionD(-0.0283573746355862,0.99959784878909,1.54147714359E-14,4.59685384111915E-13)))

# Auxiliary marker (coordinate system feature)
marker_28_2 =chrono.ChMarker()
marker_28_2.SetName('UL-Act-Base')
body_28.AddMarker(marker_28_2)
marker_28_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.103498169014931,0.207476501567313,-0.28117820665369),chrono.ChQuaternionD(-0.0283573746355862,0.99959784878909,1.54147714359E-14,4.59685384111915E-13)))

exported_items.append(body_28)



# Rigid body part
body_29= chrono.ChBodyAuxRef()
body_29.SetName('Spibot-LEG-1/Actuator_rod-1')
body_29.SetPos(chrono.ChVectorD(-0.103498169014899,0.209404729811477,-0.315135892070162))
body_29.SetRot(chrono.ChQuaternionD(4.59684597036659e-13,-1.54425158495773e-14,0.99959784878909,0.0283573746355862))
body_29.SetMass(0.00140945245841084)
body_29.SetInertiaXX(chrono.ChVectorD(2.33089158373325e-06,2.31955788413856e-06,3.09621878470135e-08))
body_29.SetInertiaXY(chrono.ChVectorD(1.20354419028169e-19,-2.11920590454842e-18,1.30374306503791e-07))
body_29.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-1.65060230227876e-19,-2.34447212110501e-18,0.0545976735175364),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_3_1_shape = chrono.ChObjShapeFile() 
body_3_1_shape.SetFilename(shapes_dir +'body_3_1.obj') 
body_3_1_level = chrono.ChAssetLevel() 
body_3_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_3_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_3_1_level.GetAssets().push_back(body_3_1_shape) 
body_29.GetAssets().push_back(body_3_1_level) 

# Auxiliary marker (coordinate system feature)
marker_29_1 =chrono.ChMarker()
marker_29_1.SetName('UL-Act-Shaft')
body_29.AddMarker(marker_29_1)
marker_29_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.103498169014848,0.212558219049965,-0.370671431417708),chrono.ChQuaternionD(0.99959784878909,0.0283573746355862,-4.59684597036659E-13,1.54425158495773E-14)))

# Auxiliary marker (coordinate system feature)
marker_29_2 =chrono.ChMarker()
marker_29_2.SetName('LL-Act-Shaft')
body_29.AddMarker(marker_29_2)
marker_29_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.103498169014811,0.214825896704608,-0.41060710016201),chrono.ChQuaternionD(0.99959784878909,0.0283573746355862,-4.59684597036659E-13,1.54425158495773E-14)))

exported_items.append(body_29)



# Rigid body part
body_30= chrono.ChBodyAuxRef()
body_30.SetName('Spibot-LEG-1/lower_limb-1')
body_30.SetPos(chrono.ChVectorD(-0.103448169014814,0.154824489507054,-0.410318781762366))
body_30.SetRot(chrono.ChQuaternionD(0.999999970353785,0.000243500366994983,-4.60020295109691e-13,2.5822614170296e-15))
body_30.SetMass(0.173763895224452)
body_30.SetInertiaXX(chrono.ChVectorD(0.000660134295478084,8.75830083251983e-06,0.000660653854038223))
body_30.SetInertiaXY(chrono.ChVectorD(-7.08403850634256e-11,-6.70198773446307e-12,3.12821546150198e-07))
body_30.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(4.14273289964873e-09,-0.0143933772184335,3.59893950746433e-07),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_1_1_shape = chrono.ChObjShapeFile() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_1_1_shape.SetColor(chrono.ChColor(0.898039215686275,0.917647058823529,0.929411764705882)) 
body_1_1_shape.SetFading(0.75) 
body_1_1_level = chrono.ChAssetLevel() 
body_1_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_1_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_1_1_level.GetAssets().push_back(body_1_1_shape) 
body_30.GetAssets().push_back(body_1_1_level) 

# Auxiliary marker (coordinate system feature)
marker_30_1 =chrono.ChMarker()
marker_30_1.SetName('LowerLimbCenterRef')
body_30.AddMarker(marker_30_1)
marker_30_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.103448169014814,0.154824489507054,-0.410318781762366),chrono.ChQuaternionD(0.70710676022351,0.000172180761048849,0.000172180760398282,-0.707106760223506)))

# Auxiliary marker (coordinate system feature)
marker_30_2 =chrono.ChMarker()
marker_30_2.SetName('LL-UL-Ref')
body_30.AddMarker(marker_30_2)
marker_30_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.103448169014814,0.254824477648568,-0.41027008169041),chrono.ChQuaternionD(0.70710676022351,0.000172180761048849,0.000172180760398282,-0.707106760223506)))

# Collision shapes 
body_30.GetCollisionModel().ClearModel()
body_30.GetCollisionModel().AddSphere(0.01, chrono.ChVectorD(3.46944695195361E-17,-0.1,0))
body_30.GetCollisionModel().BuildModel()
body_30.SetCollide(True)

exported_items.append(body_30)



# Rigid body part
body_31= chrono.ChBodyAuxRef()
body_31.SetName('Spibot-LEG-1/upper_limb-1')
body_31.SetPos(chrono.ChVectorD(-0.103448169014904,0.25536588140155,-0.310271547317897))
body_31.SetRot(chrono.ChQuaternionD(-0.498644652796309,0.501351683190202,0.498644652796771,-0.501351683189743))
body_31.SetMass(0.0769386604687246)
body_31.SetInertiaXX(chrono.ChVectorD(1.21361246341297e-05,0.000291222022965819,0.000279898353184369))
body_31.SetInertiaXY(chrono.ChVectorD(1.51104892027932e-06,1.2005821531079e-05,-6.50009620491592e-08))
body_31.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-0.00433891891647106,-0.0160004109829567,3.48337905591851e-19),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_2_1_shape = chrono.ChObjShapeFile() 
body_2_1_shape.SetFilename(shapes_dir +'body_2_1.obj') 
body_2_1_level = chrono.ChAssetLevel() 
body_2_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_2_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_2_1_level.GetAssets().push_back(body_2_1_shape) 
body_31.GetAssets().push_back(body_2_1_level) 

# Auxiliary marker (coordinate system feature)
marker_31_1 =chrono.ChMarker()
marker_31_1.SetName('UL-LL-Ref')
body_31.AddMarker(marker_31_1)
marker_31_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.103448169014812,0.254824477306583,-0.410270081715187),chrono.ChQuaternionD(0.707104190337438,-0.00191415954807328,-0.707104190338089,0.00191415954807488)))

# Auxiliary marker (coordinate system feature)
marker_31_2 =chrono.ChMarker()
marker_31_2.SetName('UL-LB-Ref')
body_31.AddMarker(marker_31_2)
marker_31_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.103448169014996,0.255907285496518,-0.210273012920607),chrono.ChQuaternionD(0.707104190337438,-0.00191415954807328,-0.707104190338089,0.00191415954807488)))

exported_items.append(body_31)



# Rigid body part
body_32= chrono.ChBodyAuxRef()
body_32.SetName('Spibot-LEG-1/limb_body_connector-2')
body_32.SetPos(chrono.ChVectorD(-0.0933481690150513,0.205232875320621,-0.149997776269673))
body_32.SetRot(chrono.ChQuaternionD(-0.498644653171685,0.501351682816853,0.498644653172146,-0.501351682816394))
body_32.SetMass(0.0319301494979552)
body_32.SetInertiaXX(chrono.ChVectorD(2.2110890182935e-06,4.65620459313165e-06,4.83154745183423e-06))
body_32.SetInertiaXY(chrono.ChVectorD(1.3238534262933e-08,1.33975070053376e-20,-1.61638181524187e-19))
body_32.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(0.01,0.00875766097763167,0.01),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_7_1_shape = chrono.ChObjShapeFile() 
body_7_1_shape.SetFilename(shapes_dir +'body_7_1.obj') 
body_7_1_level = chrono.ChAssetLevel() 
body_7_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_7_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_7_1_level.GetAssets().push_back(body_7_1_shape) 
body_32.GetAssets().push_back(body_7_1_level) 

# Auxiliary marker (coordinate system feature)
marker_32_1 =chrono.ChMarker()
marker_32_1.SetName('LB-UL-Ref')
body_32.AddMarker(marker_32_1)
marker_32_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.103348169015033,0.215124447971386,-0.170051623543824),chrono.ChQuaternionD(-0.498644653171686,0.501351682816392,0.501351682816854,0.498644653172145)))

# Auxiliary marker (coordinate system feature)
marker_32_2 =chrono.ChMarker()
marker_32_2.SetName('LB-B-Act-1')
body_32.AddMarker(marker_32_2)
marker_32_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.103348169015051,0.215232728760431,-0.150051916664204),chrono.ChQuaternionD(0.705190031320551,-0.709018349357843,-3.26512438047624E-13,-3.24564167465295E-13)))

exported_items.append(body_32)



# Rigid body part
body_33= chrono.ChBodyAuxRef()
body_33.SetName('Body-2')
body_33.SetPos(chrono.ChVectorD(-0.0133481690150063,0.235948989890131,-0.110163490713836))
body_33.SetRot(chrono.ChQuaternionD(-0.00191415901864387,-0.707104190338798,0.00191415901864684,0.707104190339595))
body_33.SetMass(0.341410951377452)
body_33.SetInertiaXX(chrono.ChVectorD(0.000241317387799136,0.00125554646880151,0.00103704927238704))
body_33.SetInertiaXY(chrono.ChVectorD(5.49131770190392e-06,8.96797680322172e-16,-6.44299869772712e-18))
body_33.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-1.67538677735044e-18,3.02853719694585e-22,1.57207324416603e-17),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_33_1_shape = chrono.ChObjShapeFile() 
body_33_1_shape.SetFilename(shapes_dir +'body_33_1.obj') 
body_33_1_shape.SetColor(chrono.ChColor(0.792156862745098,0.819607843137255,0.933333333333333)) 
body_33_1_shape.SetFading(0.75) 
body_33_1_level = chrono.ChAssetLevel() 
body_33_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_33_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_33_1_level.GetAssets().push_back(body_33_1_shape) 
body_33.GetAssets().push_back(body_33_1_level) 

# Auxiliary marker (coordinate system feature)
marker_33_1 =chrono.ChMarker()
marker_33_1.SetName('BM-4')
body_33.AddMarker(marker_33_1)
marker_33_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(0.0766518309850387,0.236165551468219,-0.0701640769546976),chrono.ChQuaternionD(0.50135168281634,0.498644653171635,0.498644653172197,-0.501351682816906)))

# Auxiliary marker (coordinate system feature)
marker_33_2 =chrono.ChMarker()
marker_33_2.SetName('BM-3')
body_33.AddMarker(marker_33_2)
marker_33_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(0.0766518309849486,0.23573242831204,-0.150162904473178),chrono.ChQuaternionD(0.50135168281634,0.498644653171635,0.498644653172197,-0.501351682816906)))

# Auxiliary marker (coordinate system feature)
marker_33_3 =chrono.ChMarker()
marker_33_3.SetName('BM-5')
body_33.AddMarker(marker_33_3)
marker_33_3.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.0133481690149612,0.23616555146822,-0.0701640769545961),chrono.ChQuaternionD(0.50135168281634,0.498644653171635,0.498644653172197,-0.501351682816906)))

# Auxiliary marker (coordinate system feature)
marker_33_4 =chrono.ChMarker()
marker_33_4.SetName('BM-2')
body_33.AddMarker(marker_33_4)
marker_33_4.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.0133481690150514,0.235732428312041,-0.150162904473077),chrono.ChQuaternionD(0.50135168281634,0.498644653171635,0.498644653172197,-0.501351682816906)))

# Auxiliary marker (coordinate system feature)
marker_33_5 =chrono.ChMarker()
marker_33_5.SetName('BM-6')
body_33.AddMarker(marker_33_5)
marker_33_5.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.103348169014961,0.236165551468221,-0.0701640769544947),chrono.ChQuaternionD(0.50135168281634,0.498644653171635,0.498644653172197,-0.501351682816906)))

# Auxiliary marker (coordinate system feature)
marker_33_6 =chrono.ChMarker()
marker_33_6.SetName('BM-1')
body_33.AddMarker(marker_33_6)
marker_33_6.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.103348169015051,0.235732428312042,-0.150162904472975),chrono.ChQuaternionD(0.50135168281634,0.498644653171635,0.498644653172197,-0.501351682816906)))

exported_items.append(body_33)



# Rigid body part
body_34= chrono.ChBodyAuxRef()
body_34.SetName('Spibot-LEG-6/upper_limb-1')
body_34.SetPos(chrono.ChVectorD(-0.103248169190155,0.257531497384281,0.0897225903656261))
body_34.SetRot(chrono.ChQuaternionD(0.501351682816854,0.498644653171684,0.501351682816393,0.498644653172147))
body_34.SetMass(0.0769386604687246)
body_34.SetInertiaXX(chrono.ChVectorD(1.21361246296042e-05,0.000291222022970345,0.000279898353184369))
body_34.SetInertiaXY(chrono.ChVectorD(-1.51104850236071e-06,-1.20058215311765e-05,-6.50009440708966e-08))
body_34.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-0.00433891891647106,-0.0160004109829567,3.48337905591851e-19),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_2_1_shape = chrono.ChObjShapeFile() 
body_2_1_shape.SetFilename(shapes_dir +'body_2_1.obj') 
body_2_1_level = chrono.ChAssetLevel() 
body_2_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_2_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_2_1_level.GetAssets().push_back(body_2_1_shape) 
body_34.GetAssets().push_back(body_2_1_level) 

# Auxiliary marker (coordinate system feature)
marker_34_1 =chrono.ChMarker()
marker_34_1.SetName('UL-LL-Ref')
body_34.AddMarker(marker_34_1)
marker_34_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.103248169190248,0.258072901329505,0.189721124763727),chrono.ChQuaternionD(0.707104190339524,-0.00191415901864669,0.70710419033887,-0.00191415901864481)))

# Auxiliary marker (coordinate system feature)
marker_34_2 =chrono.ChMarker()
marker_34_2.SetName('UL-LB-Ref')
body_34.AddMarker(marker_34_2)
marker_34_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.103248169190063,0.256990093439057,-0.0102759440324745),chrono.ChQuaternionD(0.707104190339524,-0.00191415901864669,0.70710419033887,-0.00191415901864481)))

exported_items.append(body_34)



# Rigid body part
body_35= chrono.ChBodyAuxRef()
body_35.SetName('Spibot-LEG-6/lower_limb-1')
body_35.SetPos(chrono.ChVectorD(-0.103248169013917,0.158072913135899,0.189672424609948))
body_35.SetRot(chrono.ChQuaternionD(4.59715612550484e-13,-1.82492915082982e-15,0.999999970353798,0.000243500315199938))
body_35.SetMass(0.173763895224452)
body_35.SetInertiaXX(chrono.ChVectorD(0.000660134295478084,8.75830083245502e-06,0.000660653854038287))
body_35.SetInertiaXY(chrono.ChVectorD(7.08403840471675e-11,-6.70198789040288e-12,-3.12821478620277e-07))
body_35.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(4.14273289964873e-09,-0.0143933772184335,3.59893950746433e-07),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_1_1_shape = chrono.ChObjShapeFile() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_1_1_shape.SetColor(chrono.ChColor(0.898039215686275,0.917647058823529,0.929411764705882)) 
body_1_1_shape.SetFading(0.75) 
body_1_1_level = chrono.ChAssetLevel() 
body_1_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_1_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_1_1_level.GetAssets().push_back(body_1_1_shape) 
body_35.GetAssets().push_back(body_1_1_level) 

# Auxiliary marker (coordinate system feature)
marker_35_1 =chrono.ChMarker()
marker_35_1.SetName('LowerLimbCenterRef')
body_35.AddMarker(marker_35_1)
marker_35_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.103248169013917,0.158072913135899,0.189672424609948),chrono.ChQuaternionD(-0.000172180724423967,0.707106760223518,-0.707106760223516,-0.000172180723773831)))

# Auxiliary marker (coordinate system feature)
marker_35_2 =chrono.ChMarker()
marker_35_2.SetName('LL-UL-Ref')
body_35.AddMarker(marker_35_2)
marker_35_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.103248169013917,0.258072901277418,0.189721124671544),chrono.ChQuaternionD(-0.000172180724423967,0.707106760223518,-0.707106760223516,-0.000172180723773831)))

# Collision shapes 
body_35.GetCollisionModel().ClearModel()
body_35.GetCollisionModel().AddSphere(0.01, chrono.ChVectorD(3.46944695195361E-17,-0.1,0))
body_35.GetCollisionModel().BuildModel()
body_35.SetCollide(True)

exported_items.append(body_35)



# Rigid body part
body_36= chrono.ChBodyAuxRef()
body_36.SetName('Spibot-LEG-6/Actuator_rod-1')
body_36.SetPos(chrono.ChVectorD(-0.103198169015112,0.211601876279734,0.0946134655816056))
body_36.SetRot(chrono.ChQuaternionD(0.999426563775093,-0.0338606500337887,-4.59706307558301e-13,-1.37975095509466e-14))
body_36.SetMass(0.00140945245841084)
body_36.SetInertiaXX(chrono.ChVectorD(2.33089158373325e-06,2.31640927196727e-06,3.41108000183115e-08))
body_36.SetInertiaXY(chrono.ChVectorD(1.4364152150586e-19,-2.11762655812541e-18,1.5554242605239e-07))
body_36.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-1.65060230227876e-19,-2.34447212110501e-18,0.0545976735175364),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_3_1_shape = chrono.ChObjShapeFile() 
body_3_1_shape.SetFilename(shapes_dir +'body_3_1.obj') 
body_3_1_level = chrono.ChAssetLevel() 
body_3_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_3_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_3_1_level.GetAssets().push_back(body_3_1_shape) 
body_36.GetAssets().push_back(body_3_1_level) 

# Auxiliary marker (coordinate system feature)
marker_36_1 =chrono.ChMarker()
marker_36_1.SetName('UL-Act-Shaft')
body_36.AddMarker(marker_36_1)
marker_36_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.103198169015163,0.215366713463273,0.150110912603802),chrono.ChQuaternionD(4.59706307558301E-13,1.37975095509466E-14,0.999426563775093,-0.0338606500337886)))

# Auxiliary marker (coordinate system feature)
marker_36_2 =chrono.ChMarker()
marker_36_2.SetName('LL-Act-Shaft')
body_36.AddMarker(marker_36_2)
marker_36_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.1031981690152,0.21807401211211,0.190019189114145),chrono.ChQuaternionD(4.59706307558301E-13,1.37975095509466E-14,0.999426563775093,-0.0338606500337887)))

exported_items.append(body_36)



# Rigid body part
body_37= chrono.ChBodyAuxRef()
body_37.SetName('Spibot-LEG-6/Actuator_body-1')
body_37.SetPos(chrono.ChVectorD(-0.103198169015118,0.212039036970017,0.10105764923853))
body_37.SetRot(chrono.ChQuaternionD(1.36625705404606e-14,-4.59821965305716e-13,0.0338606500337886,0.999426563775093))
body_37.SetMass(0.00204159144576871)
body_37.SetInertiaXX(chrono.ChVectorD(8.08481090947278e-07,7.98194720293837e-07,8.93139775008946e-08))
body_37.SetInertiaXY(chrono.ChVectorD(4.49494971688182e-20,6.62998870242982e-19,-4.83113982991354e-08))
body_37.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-4.17192939730159e-18,5.58956732701871e-20,-0.0175577824053523),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_4_1_shape = chrono.ChObjShapeFile() 
body_4_1_shape.SetFilename(shapes_dir +'body_4_1.obj') 
body_4_1_shape.SetColor(chrono.ChColor(0.752941176470588,0.752941176470588,0.752941176470588)) 
body_4_1_shape.SetFading(0.75) 
body_4_1_level = chrono.ChAssetLevel() 
body_4_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_4_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_4_1_level.GetAssets().push_back(body_4_1_shape) 
body_37.GetAssets().push_back(body_4_1_level) 

# Auxiliary marker (coordinate system feature)
marker_37_1 =chrono.ChMarker()
marker_37_1.SetName('LL-Act-Base')
body_37.AddMarker(marker_37_1)
marker_37_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.103198169015072,0.208654913658971,0.0511723036006011),chrono.ChQuaternionD(1.36625705404606E-14,-4.59821965305716E-13,0.0338606500337886,0.999426563775093)))

# Auxiliary marker (coordinate system feature)
marker_37_2 =chrono.ChMarker()
marker_37_2.SetName('UL-Act-Base')
body_37.AddMarker(marker_37_2)
marker_37_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.103198169015082,0.20933173832118,0.0611493727281869),chrono.ChQuaternionD(1.36625705404606E-14,-4.59821965305716E-13,0.0338606500337886,0.999426563775093)))

exported_items.append(body_37)



# Rigid body part
body_38= chrono.ChBodyAuxRef()
body_38.SetName('Spibot-LEG-6/Actuator_rod-2')
body_38.SetPos(chrono.ChVectorD(-0.103348169190054,0.220949314308874,-0.0206285164353502))
body_38.SetRot(chrono.ChQuaternionD(3.75671286703526e-14,-4.6080334255511e-13,0.0869387495364262,0.996213658724394))
body_38.SetMass(0.00140945245841084)
body_38.SetInertiaXX(chrono.ChVectorD(2.33089158373325e-06,2.25784768904727e-06,9.26723829383103e-08))
body_38.SetInertiaXY(chrono.ChVectorD(3.69566069578839e-19,2.10138594976458e-18,-3.92961828326101e-07))
body_38.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-1.65060230227876e-19,-2.34447212110501e-18,0.0545976735175364),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_3_1_shape = chrono.ChObjShapeFile() 
body_3_1_shape.SetFilename(shapes_dir +'body_3_1.obj') 
body_3_1_level = chrono.ChAssetLevel() 
body_3_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_3_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_3_1_level.GetAssets().push_back(body_3_1_shape) 
body_38.GetAssets().push_back(body_3_1_level) 

# Auxiliary marker (coordinate system feature)
marker_38_1 =chrono.ChMarker()
marker_38_1.SetName('UL-Act-Shaft')
body_38.AddMarker(marker_38_1)
marker_38_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.103348169190105,0.230584628944741,0.0341556175531307),chrono.ChQuaternionD(0.0869387495364262,0.996213658724394,-3.75671286703526E-14,4.6080334255511E-13)))

# Auxiliary marker (coordinate system feature)
marker_38_2 =chrono.ChMarker()
marker_38_2.SetName('LL-Act-Shaft')
body_38.AddMarker(marker_38_2)
marker_38_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.103348169190141,0.23751339452559,0.0735509498594541),chrono.ChQuaternionD(0.0869387495364262,0.996213658724394,-3.75671286703526E-14,4.6080334255511E-13)))

exported_items.append(body_38)



# Rigid body part
body_39= chrono.ChBodyAuxRef()
body_39.SetName('Spibot-LEG-6/Actuator_body-2')
body_39.SetPos(chrono.ChVectorD(-0.103348169190063,0.222702898338594,-0.0106580498678531))
body_39.SetRot(chrono.ChQuaternionD(3.75190668083946e-14,-4.60891120075786e-13,0.0869387495364263,0.996213658724394))
body_39.SetMass(0.00204159144576871)
body_39.SetInertiaXX(chrono.ChVectorD(8.08481090947278e-07,7.80005522469939e-07,1.07503175324792e-07))
body_39.SetInertiaXY(chrono.ChVectorD(1.15667852278902e-19,6.57878835175641e-19,-1.22053743704785e-07))
body_39.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-4.17192939730159e-18,5.58956732701871e-20,-0.0175577824053523),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_4_1_shape = chrono.ChObjShapeFile() 
body_4_1_shape.SetFilename(shapes_dir +'body_4_1.obj') 
body_4_1_shape.SetColor(chrono.ChColor(0.843137254901961,0.843137254901961,0)) 
body_4_1_shape.SetFading(0.75) 
body_4_1_level = chrono.ChAssetLevel() 
body_4_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_4_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_4_1_level.GetAssets().push_back(body_4_1_shape) 
body_39.GetAssets().push_back(body_4_1_level) 

# Auxiliary marker (coordinate system feature)
marker_39_1 =chrono.ChMarker()
marker_39_1.SetName('LL-Act-Base')
body_39.AddMarker(marker_39_1)
marker_39_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.103348169190018,0.214041941362533,-0.0599022152507574),chrono.ChQuaternionD(3.75190668083946E-14,-4.60891120075786E-13,0.0869387495364263,0.996213658724394)))

# Auxiliary marker (coordinate system feature)
marker_39_2 =chrono.ChMarker()
marker_39_2.SetName('UL-Act-Base')
body_39.AddMarker(marker_39_2)
marker_39_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.103348169190027,0.215774132757745,-0.0500533821741765),chrono.ChQuaternionD(3.75190668083946E-14,-4.60891120075786E-13,0.0869387495364263,0.996213658724394)))

exported_items.append(body_39)



# Rigid body part
body_40= chrono.ChBodyAuxRef()
body_40.SetName('Spibot-LEG-6/limb_body_connector-1')
body_40.SetPos(chrono.ChVectorD(-0.113348169014961,0.246665397580021,-0.0702209243687524))
body_40.SetRot(chrono.ChQuaternionD(0.501351682816853,0.498644653171685,0.501351682816393,0.498644653172147))
body_40.SetMass(0.0319301494979552)
body_40.SetInertiaXX(chrono.ChVectorD(2.2110890182935e-06,4.65620459313165e-06,4.83154745183424e-06))
body_40.SetInertiaXY(chrono.ChVectorD(-1.32385342629298e-08,-1.13823654339839e-20,-1.61441326557281e-19))
body_40.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(0.01,0.00875766097763167,0.01),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_7_1_shape = chrono.ChObjShapeFile() 
body_7_1_shape.SetFilename(shapes_dir +'body_7_1.obj') 
body_7_1_level = chrono.ChAssetLevel() 
body_7_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_7_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_7_1_level.GetAssets().push_back(body_7_1_shape) 
body_40.GetAssets().push_back(body_7_1_level) 

# Auxiliary marker (coordinate system feature)
marker_40_1 =chrono.ChMarker()
marker_40_1.SetName('LB-UL-Ref')
body_40.AddMarker(marker_40_1)
marker_40_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.103348169015016,0.256990093386966,-0.0102759441244052),chrono.ChQuaternionD(-0.498644653172146,0.501351682816854,-0.501351682816392,-0.498644653171686)))

# Auxiliary marker (coordinate system feature)
marker_40_2 =chrono.ChMarker()
marker_40_2.SetName('LB-B-Act-1')
body_40.AddMarker(marker_40_2)
marker_40_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.103348169014961,0.256665251019831,-0.0702750647632656),chrono.ChQuaternionD(3.24735431634622E-13,-3.26301552230695E-13,0.709018349357842,0.705190031320552)))

exported_items.append(body_40)



# Rigid body part
body_41= chrono.ChBodyAuxRef()
body_41.SetName('Spibot-LEG-6/limb_body_connector-2')
body_41.SetPos(chrono.ChVectorD(-0.113348169014961,0.2056659984768,-0.0699989487512106))
body_41.SetRot(chrono.ChQuaternionD(0.501351682816852,0.498644653171685,0.501351682816393,0.498644653172147))
body_41.SetMass(0.0319301494979552)
body_41.SetInertiaXX(chrono.ChVectorD(2.2110890182935e-06,4.65620459313165e-06,4.83154745183423e-06))
body_41.SetInertiaXY(chrono.ChVectorD(-1.32385342629268e-08,-1.09796217358603e-20,-1.62198376871761e-19))
body_41.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(0.01,0.00875766097763167,0.01),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_7_1_shape = chrono.ChObjShapeFile() 
body_7_1_shape.SetFilename(shapes_dir +'body_7_1.obj') 
body_7_1_level = chrono.ChAssetLevel() 
body_7_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_7_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_7_1_level.GetAssets().push_back(body_7_1_shape) 
body_41.GetAssets().push_back(body_7_1_level) 

# Auxiliary marker (coordinate system feature)
marker_41_1 =chrono.ChMarker()
marker_41_1.SetName('LB-UL-Ref')
body_41.AddMarker(marker_41_1)
marker_41_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.10334816901498,0.215774132705655,-0.0500533822661037),chrono.ChQuaternionD(-0.498644653172146,0.501351682816853,-0.501351682816392,-0.498644653171686)))

# Auxiliary marker (coordinate system feature)
marker_41_2 =chrono.ChMarker()
marker_41_2.SetName('LB-B-Act-1')
body_41.AddMarker(marker_41_2)
marker_41_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.103348169014961,0.21566585191661,-0.0700530891457238),chrono.ChQuaternionD(3.24769019602545E-13,-3.26422958560292E-13,0.709018349357842,0.705190031320552)))

exported_items.append(body_41)



# Rigid body part
body_42= chrono.ChBodyAuxRef()
body_42.SetName('Spibot-LEG-5/upper_limb-1')
body_42.SetPos(chrono.ChVectorD(-0.0132481690151081,0.257531497332189,0.0897225902735941))
body_42.SetRot(chrono.ChQuaternionD(0.501351682816853,0.498644653171685,0.501351682816393,0.498644653172146))
body_42.SetMass(0.0769386604687246)
body_42.SetInertiaXX(chrono.ChVectorD(1.21361246296042e-05,0.000291222022970345,0.000279898353184369))
body_42.SetInertiaXY(chrono.ChVectorD(-1.51104850236052e-06,-1.20058215311763e-05,-6.50009440709756e-08))
body_42.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-0.00433891891647106,-0.0160004109829567,3.48337905591851e-19),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_2_1_shape = chrono.ChObjShapeFile() 
body_2_1_shape.SetFilename(shapes_dir +'body_2_1.obj') 
body_2_1_level = chrono.ChAssetLevel() 
body_2_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_2_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_2_1_level.GetAssets().push_back(body_2_1_shape) 
body_42.GetAssets().push_back(body_2_1_level) 

# Auxiliary marker (coordinate system feature)
marker_42_1 =chrono.ChMarker()
marker_42_1.SetName('UL-LL-Ref')
body_42.AddMarker(marker_42_1)
marker_42_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.0132481690152,0.258072901277413,0.189721124671695),chrono.ChQuaternionD(0.707104190339522,-0.00191415901864609,0.707104190338872,-0.00191415901864478)))

# Auxiliary marker (coordinate system feature)
marker_42_2 =chrono.ChMarker()
marker_42_2.SetName('UL-LB-Ref')
body_42.AddMarker(marker_42_2)
marker_42_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.0132481690150161,0.256990093386965,-0.0102759441245066),chrono.ChQuaternionD(0.707104190339522,-0.00191415901864609,0.707104190338872,-0.00191415901864478)))

exported_items.append(body_42)



# Rigid body part
body_43= chrono.ChBodyAuxRef()
body_43.SetName('Spibot-LEG-5/lower_limb-1')
body_43.SetPos(chrono.ChVectorD(-0.0132481691478485,0.158072913123956,0.189672446182903))
body_43.SetRot(chrono.ChQuaternionD(4.590767747328e-13,-1.88809272059868e-15,0.999999970380055,0.000243392459438312))
body_43.SetMass(0.173763895224452)
body_43.SetInertiaXX(chrono.ChVectorD(0.000660134295478084,8.75830069752696e-06,0.000660653854173216))
body_43.SetInertiaXY(chrono.ChVectorD(7.08403827130595e-11,-6.70200302430357e-12,-3.12680857233297e-07))
body_43.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(4.14273289964873e-09,-0.0143933772184335,3.59893950746433e-07),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_1_1_shape = chrono.ChObjShapeFile() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_1_1_shape.SetColor(chrono.ChColor(0.898039215686275,0.917647058823529,0.929411764705882)) 
body_1_1_shape.SetFading(0.75) 
body_1_1_level = chrono.ChAssetLevel() 
body_1_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_1_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_1_1_level.GetAssets().push_back(body_1_1_shape) 
body_43.GetAssets().push_back(body_1_1_level) 

# Auxiliary marker (coordinate system feature)
marker_43_1 =chrono.ChMarker()
marker_43_1.SetName('LowerLimbCenterRef')
body_43.AddMarker(marker_43_1)
marker_43_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.0132481691478485,0.158072913123956,0.189672446182903),chrono.ChQuaternionD(-0.000172104458883119,0.707106760242085,-0.707106760242082,-0.000172104458233886)))

# Auxiliary marker (coordinate system feature)
marker_43_2 =chrono.ChMarker()
marker_43_2.SetName('LL-UL-Ref')
body_43.AddMarker(marker_43_2)
marker_43_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.0132481691478489,0.258072901275978,0.189721124673348),chrono.ChQuaternionD(-0.000172104458883119,0.707106760242085,-0.707106760242082,-0.000172104458233886)))

# Collision shapes 
body_43.GetCollisionModel().ClearModel()
body_43.GetCollisionModel().AddSphere(0.01, chrono.ChVectorD(3.46944695195361E-17,-0.1,0))
body_43.GetCollisionModel().BuildModel()
body_43.SetCollide(True)

exported_items.append(body_43)



# Rigid body part
body_44= chrono.ChBodyAuxRef()
body_44.SetName('Spibot-LEG-5/Actuator_rod-1')
body_44.SetPos(chrono.ChVectorD(-0.0131981607365096,0.211601875754943,0.0946134639558315))
body_44.SetRot(chrono.ChQuaternionD(0.999426563838333,-0.033860648167188,-4.59701652716751e-13,-1.38232645224287e-14))
body_44.SetMass(0.00140945245841084)
body_44.SetInertiaXX(chrono.ChVectorD(2.33089158373325e-06,2.31640927312927e-06,3.41107988563028e-08))
body_44.SetInertiaXY(chrono.ChVectorD(1.43494112252346e-19,-2.11759629763203e-18,1.55542417527221e-07))
body_44.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-1.65060230227876e-19,-2.34447212110501e-18,0.0545976735175364),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_3_1_shape = chrono.ChObjShapeFile() 
body_3_1_shape.SetFilename(shapes_dir +'body_3_1.obj') 
body_3_1_level = chrono.ChAssetLevel() 
body_3_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_3_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_3_1_level.GetAssets().push_back(body_3_1_shape) 
body_44.GetAssets().push_back(body_3_1_level) 

# Auxiliary marker (coordinate system feature)
marker_44_1 =chrono.ChMarker()
marker_44_1.SetName('UL-Act-Shaft')
body_44.AddMarker(marker_44_1)
marker_44_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.0131981607365607,0.21536671273118,0.15011091099209),chrono.ChQuaternionD(4.59701652716751E-13,1.38232645224287E-14,0.999426563838333,-0.033860648167188)))

# Auxiliary marker (coordinate system feature)
marker_44_2 =chrono.ChMarker()
marker_44_2.SetName('LL-Act-Shaft')
body_44.AddMarker(marker_44_2)
marker_44_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.0131981607365974,0.218074011230946,0.190019187512546),chrono.ChQuaternionD(4.59701652716751E-13,1.38232645224287E-14,0.999426563838333,-0.033860648167188)))

exported_items.append(body_44)



# Rigid body part
body_45= chrono.ChBodyAuxRef()
body_45.SetName('Spibot-LEG-5/Actuator_body-1')
body_45.SetPos(chrono.ChVectorD(-0.0131981690151185,0.212039036840165,0.101057649020741))
body_45.SetRot(chrono.ChQuaternionD(1.37191213944345e-14,-4.59201765702379e-13,0.033860648167188,0.999426563838333))
body_45.SetMass(0.00204159144576871)
body_45.SetInertiaXX(chrono.ChVectorD(8.08481090947277e-07,7.98194720654757e-07,8.93139771399754e-08))
body_45.SetInertiaXY(chrono.ChVectorD(4.48719035553361e-20,6.62145204958683e-19,-4.83113956512225e-08))
body_45.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-4.17192939730159e-18,5.58956732701871e-20,-0.0175577824053523),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_4_1_shape = chrono.ChObjShapeFile() 
body_4_1_shape.SetFilename(shapes_dir +'body_4_1.obj') 
body_4_1_shape.SetColor(chrono.ChColor(0.752941176470588,0.752941176470588,0.752941176470588)) 
body_4_1_shape.SetFading(0.75) 
body_4_1_level = chrono.ChAssetLevel() 
body_4_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_4_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_4_1_level.GetAssets().push_back(body_4_1_shape) 
body_45.GetAssets().push_back(body_4_1_level) 

# Auxiliary marker (coordinate system feature)
marker_45_1 =chrono.ChMarker()
marker_45_1.SetName('LL-Act-Base')
body_45.AddMarker(marker_45_1)
marker_45_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.0131981690150727,0.208654913715458,0.0511723033701708),chrono.ChQuaternionD(1.37191213944345E-14,-4.59201765702379E-13,0.033860648167188,0.999426563838333)))

# Auxiliary marker (coordinate system feature)
marker_45_2 =chrono.ChMarker()
marker_45_2.SetName('UL-Act-Base')
body_45.AddMarker(marker_45_2)
marker_45_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.0131981690150818,0.2093317383404,0.0611493725002847),chrono.ChQuaternionD(1.37191213944345E-14,-4.59201765702379E-13,0.033860648167188,0.999426563838333)))

exported_items.append(body_45)



# Rigid body part
body_46= chrono.ChBodyAuxRef()
body_46.SetName('Spibot-LEG-5/Actuator_rod-2')
body_46.SetPos(chrono.ChVectorD(-0.0133481690150064,0.220949314256783,-0.0206285165273787))
body_46.SetRot(chrono.ChQuaternionD(3.77447806863246e-14,-4.58328484724402e-13,0.0869387495364262,0.996213658724394))
body_46.SetMass(0.00140945245841084)
body_46.SetInertiaXX(chrono.ChVectorD(2.33089158373325e-06,2.25784768904727e-06,9.26723829383103e-08))
body_46.SetInertiaXY(chrono.ChVectorD(3.67515463583406e-19,2.09035364207169e-18,-3.92961828326101e-07))
body_46.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-1.65060230227876e-19,-2.34447212110501e-18,0.0545976735175364),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_3_1_shape = chrono.ChObjShapeFile() 
body_3_1_shape.SetFilename(shapes_dir +'body_3_1.obj') 
body_3_1_level = chrono.ChAssetLevel() 
body_3_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_3_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_3_1_level.GetAssets().push_back(body_3_1_shape) 
body_46.GetAssets().push_back(body_3_1_level) 

# Auxiliary marker (coordinate system feature)
marker_46_1 =chrono.ChMarker()
marker_46_1.SetName('UL-Act-Shaft')
body_46.AddMarker(marker_46_1)
marker_46_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.0133481690150568,0.23058462889265,0.0341556174611023),chrono.ChQuaternionD(0.0869387495364262,0.996213658724394,-3.77447806863246E-14,4.58328484724402E-13)))

# Auxiliary marker (coordinate system feature)
marker_46_2 =chrono.ChMarker()
marker_46_2.SetName('LL-Act-Shaft')
body_46.AddMarker(marker_46_2)
marker_46_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.0133481690150931,0.237513394473499,0.0735509497674257),chrono.ChQuaternionD(0.0869387495364262,0.996213658724394,-3.77447806863246E-14,4.58328484724402E-13)))

exported_items.append(body_46)



# Rigid body part
body_47= chrono.ChBodyAuxRef()
body_47.SetName('Spibot-LEG-5/Actuator_body-2')
body_47.SetPos(chrono.ChVectorD(-0.0133481690150158,0.222702898286503,-0.0106580499598816))
body_47.SetRot(chrono.ChQuaternionD(3.77587112198866e-14,-4.5838420685865e-13,0.0869387495364262,0.996213658724394))
body_47.SetMass(0.00204159144576871)
body_47.SetInertiaXX(chrono.ChVectorD(8.08481090947278e-07,7.80005522469939e-07,1.07503175324793e-07))
body_47.SetInertiaXY(chrono.ChVectorD(1.15052507041657e-19,6.54491206368089e-19,-1.22053743704785e-07))
body_47.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-4.17192939730159e-18,5.58956732701871e-20,-0.0175577824053523),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_4_1_shape = chrono.ChObjShapeFile() 
body_4_1_shape.SetFilename(shapes_dir +'body_4_1.obj') 
body_4_1_shape.SetColor(chrono.ChColor(0.843137254901961,0.843137254901961,0)) 
body_4_1_shape.SetFading(0.75) 
body_4_1_level = chrono.ChAssetLevel() 
body_4_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_4_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_4_1_level.GetAssets().push_back(body_4_1_shape) 
body_47.GetAssets().push_back(body_4_1_level) 

# Auxiliary marker (coordinate system feature)
marker_47_1 =chrono.ChMarker()
marker_47_1.SetName('LL-Act-Base')
body_47.AddMarker(marker_47_1)
marker_47_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.0133481690149704,0.214041941310442,-0.0599022153427859),chrono.ChQuaternionD(3.77587112198866E-14,-4.5838420685865E-13,0.0869387495364262,0.996213658724394)))

# Auxiliary marker (coordinate system feature)
marker_47_2 =chrono.ChMarker()
marker_47_2.SetName('UL-Act-Base')
body_47.AddMarker(marker_47_2)
marker_47_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.0133481690149795,0.215774132705654,-0.0500533822662051),chrono.ChQuaternionD(3.77587112198866E-14,-4.5838420685865E-13,0.0869387495364262,0.996213658724394)))

exported_items.append(body_47)



# Rigid body part
body_48= chrono.ChBodyAuxRef()
body_48.SetName('Spibot-LEG-5/limb_body_connector-1')
body_48.SetPos(chrono.ChVectorD(-0.0233481690149612,0.246665397580021,-0.0702209243688538))
body_48.SetRot(chrono.ChQuaternionD(0.501351682816853,0.498644653171685,0.501351682816393,0.498644653172146))
body_48.SetMass(0.0319301494979552)
body_48.SetInertiaXX(chrono.ChVectorD(2.2110890182935e-06,4.65620459313164e-06,4.83154745183423e-06))
body_48.SetInertiaXY(chrono.ChVectorD(-1.32385342629295e-08,-9.70070315805874e-21,-1.61316073557728e-19))
body_48.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(0.01,0.00875766097763167,0.01),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_7_1_shape = chrono.ChObjShapeFile() 
body_7_1_shape.SetFilename(shapes_dir +'body_7_1.obj') 
body_7_1_shape.SetColor(chrono.ChColor(0.898039215686275,0.917647058823529,0.929411764705882)) 
body_7_1_shape.SetFading(0.75) 
body_7_1_level = chrono.ChAssetLevel() 
body_7_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_7_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_7_1_level.GetAssets().push_back(body_7_1_shape) 
body_48.GetAssets().push_back(body_7_1_level) 

# Auxiliary marker (coordinate system feature)
marker_48_1 =chrono.ChMarker()
marker_48_1.SetName('LB-UL-Ref')
body_48.AddMarker(marker_48_1)
marker_48_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.0133481690150164,0.256990093386965,-0.0102759441245067),chrono.ChQuaternionD(-0.498644653172146,0.501351682816853,-0.501351682816393,-0.498644653171686)))

# Auxiliary marker (coordinate system feature)
marker_48_2 =chrono.ChMarker()
marker_48_2.SetName('LB-B-Act-1')
body_48.AddMarker(marker_48_2)
marker_48_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.0133481690149612,0.256665251019831,-0.070275064763367),chrono.ChQuaternionD(3.24726867114467E-13,-3.2584031269656E-13,0.709018349357842,0.705190031320552)))

exported_items.append(body_48)



# Rigid body part
body_49= chrono.ChBodyAuxRef()
body_49.SetName('Spibot-LEG-5/limb_body_connector-2')
body_49.SetPos(chrono.ChVectorD(-0.0233481690149612,0.205665998476799,-0.069998948751312))
body_49.SetRot(chrono.ChQuaternionD(0.501351682816852,0.498644653171686,0.501351682816393,0.498644653172147))
body_49.SetMass(0.0319301494979552)
body_49.SetInertiaXX(chrono.ChVectorD(2.2110890182935e-06,4.65620459313165e-06,4.83154745183424e-06))
body_49.SetInertiaXY(chrono.ChVectorD(-1.32385342629263e-08,-9.85639019887959e-21,-1.61842806649233e-19))
body_49.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(0.01,0.00875766097763167,0.01),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_7_1_shape = chrono.ChObjShapeFile() 
body_7_1_shape.SetFilename(shapes_dir +'body_7_1.obj') 
body_7_1_level = chrono.ChAssetLevel() 
body_7_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_7_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_7_1_level.GetAssets().push_back(body_7_1_shape) 
body_49.GetAssets().push_back(body_7_1_level) 

# Auxiliary marker (coordinate system feature)
marker_49_1 =chrono.ChMarker()
marker_49_1.SetName('LB-UL-Ref')
body_49.AddMarker(marker_49_1)
marker_49_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.0133481690149796,0.215774132705654,-0.0500533822662051),chrono.ChQuaternionD(-0.498644653172146,0.501351682816853,-0.501351682816392,-0.498644653171687)))

# Auxiliary marker (coordinate system feature)
marker_49_2 =chrono.ChMarker()
marker_49_2.SetName('LB-B-Act-1')
body_49.AddMarker(marker_49_2)
marker_49_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.0133481690149612,0.215665851916609,-0.0700530891458252),chrono.ChQuaternionD(3.24788592844649E-13,-3.25914054265601E-13,0.709018349357842,0.705190031320552)))

exported_items.append(body_49)




# Mate constraint: Distance1 [MateDistanceDim] type:5 align:1 flip:False
#   Entity 0: C::E name: body_32 , SW name: Spibot-LEG-1/limb_body_connector-2 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_33 , SW name: Body-2 ,  SW ref.type:2 (2)

link_1 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(-0.113348169015051,0.225232582200241,-0.150106057058736)
cB = chrono.ChVectorD(-0.0133481690150063,0.225949136450321,-0.110109350319314)
dA = chrono.ChVectorD(-3.60822483003176e-16,0.999985343981005,-0.00541403945224001)
dB = chrono.ChVectorD(-1.13959586666279e-15,-0.999985343981005,0.00541403945223878)
link_1.Initialize(body_32,body_33,False,cA,cB,dB)
link_1.SetDistance(-0.0005)
link_1.SetName("Distance1")
exported_items.append(link_1)

link_2 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.113348169015051,0.225232582200241,-0.150106057058736)
dA = chrono.ChVectorD(-3.60822483003176e-16,0.999985343981005,-0.00541403945224001)
cB = chrono.ChVectorD(-0.0133481690150063,0.225949136450321,-0.110109350319314)
dB = chrono.ChVectorD(-1.13959586666279e-15,-0.999985343981005,0.00541403945223878)
link_2.SetFlipped(True)
link_2.Initialize(body_32,body_33,False,cA,cB,dA,dB)
link_2.SetName("Distance1")
exported_items.append(link_2)


# Mate constraint: Distance2 [MateDistanceDim] type:5 align:1 flip:False
#   Entity 0: C::E name: body_20 , SW name: Spibot-LEG-2/limb_body_connector-2 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_33 , SW name: Body-2 ,  SW ref.type:2 (2)

link_3 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(-0.0233481690150513,0.22523258220024,-0.150106057058837)
cB = chrono.ChVectorD(-0.0133481690150063,0.225949136450321,-0.110109350319314)
dA = chrono.ChVectorD(-3.60822483003176e-16,0.999985343981005,-0.00541403945223984)
dB = chrono.ChVectorD(-1.13959586666279e-15,-0.999985343981005,0.00541403945223878)
link_3.Initialize(body_20,body_33,False,cA,cB,dB)
link_3.SetDistance(-0.0005)
link_3.SetName("Distance2")
exported_items.append(link_3)

link_4 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.0233481690150513,0.22523258220024,-0.150106057058837)
dA = chrono.ChVectorD(-3.60822483003176e-16,0.999985343981005,-0.00541403945223984)
cB = chrono.ChVectorD(-0.0133481690150063,0.225949136450321,-0.110109350319314)
dB = chrono.ChVectorD(-1.13959586666279e-15,-0.999985343981005,0.00541403945223878)
link_4.SetFlipped(True)
link_4.Initialize(body_20,body_33,False,cA,cB,dA,dB)
link_4.SetName("Distance2")
exported_items.append(link_4)


# Mate constraint: Distance6 [MateDistanceDim] type:5 align:1 flip:False
#   Entity 0: C::E name: body_11 , SW name: Spibot-LEG-3/limb_body_connector-2 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_33 , SW name: Body-2 ,  SW ref.type:2 (2)

link_5 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(0.0666518309849486,0.22523258220024,-0.150106057058939)
cB = chrono.ChVectorD(-0.0133481690150063,0.225949136450321,-0.110109350319314)
dA = chrono.ChVectorD(1.11022302462516e-16,0.999985343981005,-0.00541403945224001)
dB = chrono.ChVectorD(-1.13959586666279e-15,-0.999985343981005,0.00541403945223878)
link_5.Initialize(body_11,body_33,False,cA,cB,dB)
link_5.SetDistance(-0.0005)
link_5.SetName("Distance6")
exported_items.append(link_5)

link_6 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.0666518309849486,0.22523258220024,-0.150106057058939)
dA = chrono.ChVectorD(1.11022302462516e-16,0.999985343981005,-0.00541403945224001)
cB = chrono.ChVectorD(-0.0133481690150063,0.225949136450321,-0.110109350319314)
dB = chrono.ChVectorD(-1.13959586666279e-15,-0.999985343981005,0.00541403945223878)
link_6.SetFlipped(True)
link_6.Initialize(body_11,body_33,False,cA,cB,dA,dB)
link_6.SetName("Distance6")
exported_items.append(link_6)


# Mate constraint: Distance5 [MateDistanceDim] type:5 align:1 flip:False
#   Entity 0: C::E name: body_8 , SW name: Spibot-LEG-4/limb_body_connector-2 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_33 , SW name: Body-2 ,  SW ref.type:2 (2)

link_7 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(0.0866518309850388,0.225665705356419,-0.0701072295404398)
cB = chrono.ChVectorD(-0.0133481690150063,0.225949136450321,-0.110109350319314)
dA = chrono.ChVectorD(1.0547118733939e-15,0.999985343981005,-0.0054140394522374)
dB = chrono.ChVectorD(-1.13959586666279e-15,-0.999985343981005,0.00541403945223878)
link_7.Initialize(body_8,body_33,False,cA,cB,dB)
link_7.SetDistance(-0.0005)
link_7.SetName("Distance5")
exported_items.append(link_7)

link_8 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.0866518309850388,0.225665705356419,-0.0701072295404398)
dA = chrono.ChVectorD(1.0547118733939e-15,0.999985343981005,-0.0054140394522374)
cB = chrono.ChVectorD(-0.0133481690150063,0.225949136450321,-0.110109350319314)
dB = chrono.ChVectorD(-1.13959586666279e-15,-0.999985343981005,0.00541403945223878)
link_8.SetFlipped(True)
link_8.Initialize(body_8,body_33,False,cA,cB,dA,dB)
link_8.SetName("Distance5")
exported_items.append(link_8)


# Mate constraint: Distance4 [MateDistanceDim] type:5 align:1 flip:False
#   Entity 0: C::E name: body_49 , SW name: Spibot-LEG-5/limb_body_connector-2 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_33 , SW name: Body-2 ,  SW ref.type:2 (2)

link_9 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(-0.00334816901496116,0.225665705356419,-0.0701072295403383)
cB = chrono.ChVectorD(-0.0133481690150063,0.225949136450321,-0.110109350319314)
dA = chrono.ChVectorD(9.15933995315754e-16,0.999985343981005,-0.00541403945223742)
dB = chrono.ChVectorD(-1.13959586666279e-15,-0.999985343981005,0.00541403945223878)
link_9.Initialize(body_49,body_33,False,cA,cB,dB)
link_9.SetDistance(-0.0005)
link_9.SetName("Distance4")
exported_items.append(link_9)

link_10 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.00334816901496116,0.225665705356419,-0.0701072295403383)
dA = chrono.ChVectorD(9.15933995315754e-16,0.999985343981005,-0.00541403945223742)
cB = chrono.ChVectorD(-0.0133481690150063,0.225949136450321,-0.110109350319314)
dB = chrono.ChVectorD(-1.13959586666279e-15,-0.999985343981005,0.00541403945223878)
link_10.SetFlipped(True)
link_10.Initialize(body_49,body_33,False,cA,cB,dA,dB)
link_10.SetName("Distance4")
exported_items.append(link_10)


# Mate constraint: Distance7 [MateDistanceDim] type:5 align:1 flip:False
#   Entity 0: C::E name: body_41 , SW name: Spibot-LEG-6/limb_body_connector-2 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_33 , SW name: Body-2 ,  SW ref.type:2 (2)

link_11 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(-0.0933481690149612,0.22566570535642,-0.0701072295402369)
cB = chrono.ChVectorD(-0.0133481690150063,0.225949136450321,-0.110109350319314)
dA = chrono.ChVectorD(3.05311331771918e-16,0.999985343981005,-0.00541403945223756)
dB = chrono.ChVectorD(-1.13959586666279e-15,-0.999985343981005,0.00541403945223878)
link_11.Initialize(body_41,body_33,False,cA,cB,dB)
link_11.SetDistance(-0.0005)
link_11.SetName("Distance7")
exported_items.append(link_11)

link_12 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.0933481690149612,0.22566570535642,-0.0701072295402369)
dA = chrono.ChVectorD(3.05311331771918e-16,0.999985343981005,-0.00541403945223756)
cB = chrono.ChVectorD(-0.0133481690150063,0.225949136450321,-0.110109350319314)
dB = chrono.ChVectorD(-1.13959586666279e-15,-0.999985343981005,0.00541403945223878)
link_12.SetFlipped(True)
link_12.Initialize(body_41,body_33,False,cA,cB,dA,dB)
link_12.SetName("Distance7")
exported_items.append(link_12)


# Mate constraint: Concentric1 [MateConcentric] type:1 align:1 flip:False
#   Entity 0: C::E name: body_33 , SW name: Body-2 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_32 , SW name: Spibot-LEG-1/limb_body_connector-2 ,  SW ref.type:2 (2)

link_13 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.103348169015051,0.245732281751852,-0.150217044867497)
dA = chrono.ChVectorD(-1.13959586666279e-15,-0.999985343981005,0.00541403945223878)
cB = chrono.ChVectorD(-0.103348169015051,0.205232875320621,-0.149997776269682)
dB = chrono.ChVectorD(-3.60822483003176e-16,0.999985343981005,-0.00541403945224001)
link_13.SetFlipped(True)
link_13.Initialize(body_33,body_32,False,cA,cB,dA,dB)
link_13.SetName("Concentric1")
exported_items.append(link_13)

link_14 = chrono.ChLinkMateGeneric()
link_14.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.103348169015051,0.245732281751852,-0.150217044867497)
cB = chrono.ChVectorD(-0.103348169015051,0.205232875320621,-0.149997776269682)
dA = chrono.ChVectorD(-1.13959586666279e-15,-0.999985343981005,0.00541403945223878)
dB = chrono.ChVectorD(-3.60822483003176e-16,0.999985343981005,-0.00541403945224001)
link_14.Initialize(body_33,body_32,False,cA,cB,dA,dB)
link_14.SetName("Concentric1")
exported_items.append(link_14)


# Mate constraint: Concentric2 [MateConcentric] type:1 align:1 flip:False
#   Entity 0: C::E name: body_33 , SW name: Body-2 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_19 , SW name: Spibot-LEG-2/limb_body_connector-1 ,  SW ref.type:2 (2)

link_15 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.0133481690150514,0.245732281751851,-0.150217044867599)
dA = chrono.ChVectorD(-1.13959586666279e-15,-0.999985343981005,0.00541403945223878)
cB = chrono.ChVectorD(-0.0133481690150514,0.246232274423842,-0.150219751887325)
dB = chrono.ChVectorD(-3.33066907387547e-16,0.999985343981005,-0.00541403945223867)
link_15.SetFlipped(True)
link_15.Initialize(body_33,body_19,False,cA,cB,dA,dB)
link_15.SetName("Concentric2")
exported_items.append(link_15)

link_16 = chrono.ChLinkMateGeneric()
link_16.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.0133481690150514,0.245732281751851,-0.150217044867599)
cB = chrono.ChVectorD(-0.0133481690150514,0.246232274423842,-0.150219751887325)
dA = chrono.ChVectorD(-1.13959586666279e-15,-0.999985343981005,0.00541403945223878)
dB = chrono.ChVectorD(-3.33066907387547e-16,0.999985343981005,-0.00541403945223867)
link_16.Initialize(body_33,body_19,False,cA,cB,dA,dB)
link_16.SetName("Concentric2")
exported_items.append(link_16)


# Mate constraint: Concentric3 [MateConcentric] type:1 align:1 flip:False
#   Entity 0: C::E name: body_33 , SW name: Body-2 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_7 , SW name: Spibot-LEG-4/limb_body_connector-1 ,  SW ref.type:2 (2)

link_17 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.0766518309850387,0.246165404908029,-0.07021821734922)
dA = chrono.ChVectorD(-1.13959586666279e-15,-0.999985343981005,0.00541403945223878)
cB = chrono.ChVectorD(0.0766518309850388,0.24666539758002,-0.0702209243689461)
dB = chrono.ChVectorD(1.02695629777827e-15,0.999985343981005,-0.00541403945223862)
link_17.SetFlipped(True)
link_17.Initialize(body_33,body_7,False,cA,cB,dA,dB)
link_17.SetName("Concentric3")
exported_items.append(link_17)

link_18 = chrono.ChLinkMateGeneric()
link_18.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(0.0766518309850387,0.246165404908029,-0.07021821734922)
cB = chrono.ChVectorD(0.0766518309850388,0.24666539758002,-0.0702209243689461)
dA = chrono.ChVectorD(-1.13959586666279e-15,-0.999985343981005,0.00541403945223878)
dB = chrono.ChVectorD(1.02695629777827e-15,0.999985343981005,-0.00541403945223862)
link_18.Initialize(body_33,body_7,False,cA,cB,dA,dB)
link_18.SetName("Concentric3")
exported_items.append(link_18)


# Mate constraint: Concentric4 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_33 , SW name: Body-2 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_12 , SW name: Spibot-LEG-3/limb_body_connector-1 ,  SW ref.type:1 (1)

link_19 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.0766518309849486,0.24573228175185,-0.1502170448677)
dA = chrono.ChVectorD(-1.13959586666279e-15,-0.999985343981005,0.00541403945223878)
cB = chrono.ChVectorD(0.0766518309849486,0.266231981303461,-0.150328032676471)
dB = chrono.ChVectorD(-1.38777878078145e-16,-0.999985343981005,0.00541403945223881)
link_19.Initialize(body_12,body_33,False,cB,cA,dB,dA)
link_19.SetName("Concentric4")
exported_items.append(link_19)

link_20 = chrono.ChLinkMateGeneric()
link_20.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(0.0766518309849486,0.24573228175185,-0.1502170448677)
cB = chrono.ChVectorD(0.0766518309849486,0.266231981303461,-0.150328032676471)
dA = chrono.ChVectorD(-1.13959586666279e-15,-0.999985343981005,0.00541403945223878)
dB = chrono.ChVectorD(-1.38777878078145e-16,-0.999985343981005,0.00541403945223881)
link_20.Initialize(body_12,body_33,False,cB,cA,dB,dA)
link_20.SetName("Concentric4")
exported_items.append(link_20)


# Mate constraint: Concentric5 [MateConcentric] type:1 align:1 flip:False
#   Entity 0: C::E name: body_33 , SW name: Body-2 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_48 , SW name: Spibot-LEG-5/limb_body_connector-1 ,  SW ref.type:2 (2)

link_21 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.0133481690149612,0.24616540490803,-0.0702182173491185)
dA = chrono.ChVectorD(-1.13959586666279e-15,-0.999985343981005,0.00541403945223878)
cB = chrono.ChVectorD(-0.0133481690149612,0.246665397580021,-0.0702209243688446)
dB = chrono.ChVectorD(9.15933995315754e-16,0.999985343981005,-0.00541403945223865)
link_21.SetFlipped(True)
link_21.Initialize(body_33,body_48,False,cA,cB,dA,dB)
link_21.SetName("Concentric5")
exported_items.append(link_21)

link_22 = chrono.ChLinkMateGeneric()
link_22.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.0133481690149612,0.24616540490803,-0.0702182173491185)
cB = chrono.ChVectorD(-0.0133481690149612,0.246665397580021,-0.0702209243688446)
dA = chrono.ChVectorD(-1.13959586666279e-15,-0.999985343981005,0.00541403945223878)
dB = chrono.ChVectorD(9.15933995315754e-16,0.999985343981005,-0.00541403945223865)
link_22.Initialize(body_33,body_48,False,cA,cB,dA,dB)
link_22.SetName("Concentric5")
exported_items.append(link_22)


# Mate constraint: Concentric6 [MateConcentric] type:1 align:1 flip:False
#   Entity 0: C::E name: body_33 , SW name: Body-2 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_40 , SW name: Spibot-LEG-6/limb_body_connector-1 ,  SW ref.type:2 (2)

link_23 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.103348169014961,0.246165404908031,-0.0702182173490171)
dA = chrono.ChVectorD(-1.13959586666279e-15,-0.999985343981005,0.00541403945223878)
cB = chrono.ChVectorD(-0.103348169014961,0.246665397580021,-0.0702209243687432)
dB = chrono.ChVectorD(2.77555756156289e-16,0.999985343981005,-0.00541403945223876)
link_23.SetFlipped(True)
link_23.Initialize(body_33,body_40,False,cA,cB,dA,dB)
link_23.SetName("Concentric6")
exported_items.append(link_23)

link_24 = chrono.ChLinkMateGeneric()
link_24.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.103348169014961,0.246165404908031,-0.0702182173490171)
cB = chrono.ChVectorD(-0.103348169014961,0.246665397580021,-0.0702209243687432)
dA = chrono.ChVectorD(-1.13959586666279e-15,-0.999985343981005,0.00541403945223878)
dB = chrono.ChVectorD(2.77555756156289e-16,0.999985343981005,-0.00541403945223876)
link_24.Initialize(body_33,body_40,False,cA,cB,dA,dB)
link_24.SetName("Concentric6")
exported_items.append(link_24)


# Mate constraint: Concentric3 [MateConcentric] type:1 align:1 flip:False
#   Entity 0: C::E name: body_2 , SW name: Spibot-LEG-4/upper_limb-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_1 , SW name: Spibot-LEG-4/lower_limb-1 ,  SW ref.type:2 (2)

link_1 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.0792018309847997,0.258072901277412,0.189721124671596)
dA = chrono.ChVectorD(-1,-3.71924713249427e-15,-9.20374887414255e-13)
cB = chrono.ChVectorD(0.0667518309848001,0.258072901278138,0.189721124670757)
dB = chrono.ChVectorD(1,3.58046925441613e-15,9.19431197843323e-13)
link_1.SetFlipped(True)
link_1.Initialize(body_2,body_1,False,cA,cB,dA,dB)
link_1.SetName("Concentric3")
exported_items.append(link_1)

link_2 = chrono.ChLinkMateGeneric()
link_2.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(0.0792018309847997,0.258072901277412,0.189721124671596)
cB = chrono.ChVectorD(0.0667518309848001,0.258072901278138,0.189721124670757)
dA = chrono.ChVectorD(-1,-3.71924713249427e-15,-9.20374887414255e-13)
dB = chrono.ChVectorD(1,3.58046925441613e-15,9.19431197843323e-13)
link_2.Initialize(body_2,body_1,False,cA,cB,dA,dB)
link_2.SetName("Concentric3")
exported_items.append(link_2)


# Mate constraint: Concentric4 [MateConcentric] type:1 align:1 flip:False
#   Entity 0: C::E name: body_1 , SW name: Spibot-LEG-4/lower_limb-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_3 , SW name: Spibot-LEG-4/Actuator_rod-1 ,  SW ref.type:2 (2)

link_3 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.0667518309848001,0.218074011806889,0.190019186856902)
dA = chrono.ChVectorD(1,3.58046925441613e-15,9.19431197843323e-13)
cB = chrono.ChVectorD(0.0792018309847999,0.218074011807861,0.190019186850441)
dB = chrono.ChVectorD(-1,-3.88578058618805e-15,-9.19431197843323e-13)
link_3.SetFlipped(True)
link_3.Initialize(body_1,body_3,False,cA,cB,dA,dB)
link_3.SetName("Concentric4")
exported_items.append(link_3)

link_4 = chrono.ChLinkMateGeneric()
link_4.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(0.0667518309848001,0.218074011806889,0.190019186856902)
cB = chrono.ChVectorD(0.0792018309847999,0.218074011807861,0.190019186850441)
dA = chrono.ChVectorD(1,3.58046925441613e-15,9.19431197843323e-13)
dB = chrono.ChVectorD(-1,-3.88578058618805e-15,-9.19431197843323e-13)
link_4.Initialize(body_1,body_3,False,cA,cB,dA,dB)
link_4.SetName("Concentric4")
exported_items.append(link_4)


# Mate constraint: Concentric6 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_3 , SW name: Spibot-LEG-4/Actuator_rod-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_4 , SW name: Spibot-LEG-4/Actuator_body-1 ,  SW ref.type:2 (2)

link_5 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.0768018309848872,0.21164417751688,0.0952370301383735)
dA = chrono.ChVectorD(9.17599329852692e-13,-0.0676824662208482,-0.997706912758584)
cB = chrono.ChVectorD(0.0768018309271015,0.214069510810654,0.130988857002547)
dB = chrono.ChVectorD(9.17932396760079e-13,-0.0676824662202545,-0.997706912758624)
link_5.Initialize(body_3,body_4,False,cA,cB,dA,dB)
link_5.SetName("Concentric6")
exported_items.append(link_5)

link_6 = chrono.ChLinkMateGeneric()
link_6.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(0.0768018309848872,0.21164417751688,0.0952370301383735)
cB = chrono.ChVectorD(0.0768018309271015,0.214069510810654,0.130988857002547)
dA = chrono.ChVectorD(9.17599329852692e-13,-0.0676824662208482,-0.997706912758584)
dB = chrono.ChVectorD(9.17932396760079e-13,-0.0676824662202545,-0.997706912758624)
link_6.Initialize(body_3,body_4,False,cA,cB,dA,dB)
link_6.SetName("Concentric6")
exported_items.append(link_6)


# Mate constraint: Concentric11 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_5 , SW name: Spibot-LEG-4/Actuator_rod-2 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_6 , SW name: Spibot-LEG-4/Actuator_body-2 ,  SW ref.type:2 (2)

link_7 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.0766518309849927,0.221057576218983,-0.0200129644601939)
dA = chrono.ChVectorD(9.06885677665059e-13,-0.173219139521213,-0.984883307658085)
cB = chrono.ChVectorD(0.0766518309849659,0.226167281076926,0.00903961619317856)
dB = chrono.ChVectorD(9.06885677665059e-13,-0.173219139521213,-0.984883307658085)
link_7.Initialize(body_5,body_6,False,cA,cB,dA,dB)
link_7.SetName("Concentric11")
exported_items.append(link_7)

link_8 = chrono.ChLinkMateGeneric()
link_8.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(0.0766518309849927,0.221057576218983,-0.0200129644601939)
cB = chrono.ChVectorD(0.0766518309849659,0.226167281076926,0.00903961619317856)
dA = chrono.ChVectorD(9.06885677665059e-13,-0.173219139521213,-0.984883307658085)
dB = chrono.ChVectorD(9.06885677665059e-13,-0.173219139521213,-0.984883307658085)
link_8.Initialize(body_5,body_6,False,cA,cB,dA,dB)
link_8.SetName("Concentric11")
exported_items.append(link_8)


# Mate constraint: Concentric12 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_2 , SW name: Spibot-LEG-4/upper_limb-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_7 , SW name: Spibot-LEG-4/limb_body_connector-1 ,  SW ref.type:2 (2)

link_9 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.0792018309849838,0.256990093386964,-0.0102759441246057)
dA = chrono.ChVectorD(-1,-3.71924713249427e-15,-9.20374887414255e-13)
cB = chrono.ChVectorD(0.0866518309849836,0.256990093386964,-0.0102759441245989)
dB = chrono.ChVectorD(-1,-3.91353616180368e-15,-9.2015284280933e-13)
link_9.Initialize(body_2,body_7,False,cA,cB,dA,dB)
link_9.SetName("Concentric12")
exported_items.append(link_9)

link_10 = chrono.ChLinkMateGeneric()
link_10.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(0.0792018309849838,0.256990093386964,-0.0102759441246057)
cB = chrono.ChVectorD(0.0866518309849836,0.256990093386964,-0.0102759441245989)
dA = chrono.ChVectorD(-1,-3.71924713249427e-15,-9.20374887414255e-13)
dB = chrono.ChVectorD(-1,-3.91353616180368e-15,-9.2015284280933e-13)
link_10.Initialize(body_2,body_7,False,cA,cB,dA,dB)
link_10.SetName("Concentric12")
exported_items.append(link_10)


# Mate constraint: Concentric13 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_6 , SW name: Spibot-LEG-4/Actuator_body-2 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_8 , SW name: Spibot-LEG-4/limb_body_connector-2 ,  SW ref.type:2 (2)

link_11 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.0842518309850203,0.215774132705653,-0.0500533822662996)
dA = chrono.ChVectorD(-1,-3.99680288865056e-15,-9.20041820506867e-13)
cB = chrono.ChVectorD(0.0866518309850204,0.215774132705654,-0.0500533822662974)
dB = chrono.ChVectorD(-1,-3.88578058618805e-15,-9.20430398565486e-13)
link_11.Initialize(body_6,body_8,False,cA,cB,dA,dB)
link_11.SetName("Concentric13")
exported_items.append(link_11)

link_12 = chrono.ChLinkMateGeneric()
link_12.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(0.0842518309850203,0.215774132705653,-0.0500533822662996)
cB = chrono.ChVectorD(0.0866518309850204,0.215774132705654,-0.0500533822662974)
dA = chrono.ChVectorD(-1,-3.99680288865056e-15,-9.20041820506867e-13)
dB = chrono.ChVectorD(-1,-3.88578058618805e-15,-9.20430398565486e-13)
link_12.Initialize(body_6,body_8,False,cA,cB,dA,dB)
link_12.SetName("Concentric13")
exported_items.append(link_12)


# Mate constraint: Concentric17 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_7 , SW name: Spibot-LEG-4/limb_body_connector-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_8 , SW name: Spibot-LEG-4/limb_body_connector-2 ,  SW ref.type:2 (2)

link_13 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.0766518309850388,0.24666539758002,-0.0702209243689461)
dA = chrono.ChVectorD(9.99200722162641e-16,0.999985343981005,-0.00541403945223859)
cB = chrono.ChVectorD(0.0766518309850388,0.205665998476799,-0.0699989487514043)
dB = chrono.ChVectorD(1.02695629777827e-15,0.999985343981005,-0.00541403945223742)
link_13.Initialize(body_7,body_8,False,cA,cB,dA,dB)
link_13.SetName("Concentric17")
exported_items.append(link_13)

link_14 = chrono.ChLinkMateGeneric()
link_14.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(0.0766518309850388,0.24666539758002,-0.0702209243689461)
cB = chrono.ChVectorD(0.0766518309850388,0.205665998476799,-0.0699989487514043)
dA = chrono.ChVectorD(9.99200722162641e-16,0.999985343981005,-0.00541403945223859)
dB = chrono.ChVectorD(1.02695629777827e-15,0.999985343981005,-0.00541403945223742)
link_14.Initialize(body_7,body_8,False,cA,cB,dA,dB)
link_14.SetName("Concentric17")
exported_items.append(link_14)


# Mate constraint: Parallel14 [MateParallel] type:3 align:0 flip:False
#   Entity 0: C::E name: body_2 , SW name: Spibot-LEG-4/upper_limb-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_3 , SW name: Spibot-LEG-4/Actuator_rod-1 ,  SW ref.type:2 (2)

link_15 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.0792018309848919,0.257531497332188,0.0897225902734949)
dA = chrono.ChVectorD(1,3.71924713249427e-15,9.20374887414255e-13)
cB = chrono.ChVectorD(0.0792018309847999,0.218074011807861,0.190019186850441)
dB = chrono.ChVectorD(1,3.88578058618805e-15,9.19431197843323e-13)
link_15.Initialize(body_2,body_3,False,cA,cB,dA,dB)
link_15.SetName("Parallel14")
exported_items.append(link_15)


# Mate constraint: Parallel15 [MateParallel] type:3 align:0 flip:False
#   Entity 0: C::E name: body_2 , SW name: Spibot-LEG-4/upper_limb-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_5 , SW name: Spibot-LEG-4/Actuator_rod-2 ,  SW ref.type:2 (2)

link_16 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.0743018309849274,0.208654913539206,0.0511723040885544)
dA = chrono.ChVectorD(1,3.71924713249427e-15,9.20374887414255e-13)
cB = chrono.ChVectorD(0.079051830984943,0.23058462889265,0.034155617461003)
dB = chrono.ChVectorD(1,3.96904731303493e-15,9.20041820506867e-13)
link_16.Initialize(body_2,body_5,False,cA,cB,dA,dB)
link_16.SetName("Parallel15")
exported_items.append(link_16)


# Mate constraint: Distance10 [MateDistanceDim] type:5 align:1 flip:False
#   Entity 0: C::E name: body_2 , SW name: Spibot-LEG-4/upper_limb-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_1 , SW name: Spibot-LEG-4/lower_limb-1 ,  SW ref.type:2 (2)

link_17 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(0.0792018309848919,0.257531497332188,0.0897225902734949)
cB = chrono.ChVectorD(0.0792518309847909,0.268068030086162,0.199725993491048)
dA = chrono.ChVectorD(1,3.71924713249427e-15,9.20374887414255e-13)
dB = chrono.ChVectorD(-1,-3.85802501057242e-15,-9.19320175540861e-13)
link_17.Initialize(body_2,body_1,False,cA,cB,dB)
link_17.SetDistance(0)
link_17.SetName("Distance10")
exported_items.append(link_17)

link_18 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.0792018309848919,0.257531497332188,0.0897225902734949)
dA = chrono.ChVectorD(1,3.71924713249427e-15,9.20374887414255e-13)
cB = chrono.ChVectorD(0.0792518309847909,0.268068030086162,0.199725993491048)
dB = chrono.ChVectorD(-1,-3.85802501057242e-15,-9.19320175540861e-13)
link_18.SetFlipped(True)
link_18.Initialize(body_2,body_1,False,cA,cB,dA,dB)
link_18.SetName("Distance10")
exported_items.append(link_18)


# Mate constraint: Distance11 [MateDistanceDim] type:5 align:1 flip:False
#   Entity 0: C::E name: body_3 , SW name: Spibot-LEG-4/Actuator_rod-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_1 , SW name: Spibot-LEG-4/lower_limb-1 ,  SW ref.type:2 (2)

link_19 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(0.0792018309847999,0.218074011807861,0.190019186850441)
cB = chrono.ChVectorD(0.0792518309847909,0.268068030086162,0.199725993491048)
dA = chrono.ChVectorD(1,3.88578058618805e-15,9.19431197843323e-13)
dB = chrono.ChVectorD(-1,-3.85802501057242e-15,-9.19320175540861e-13)
link_19.Initialize(body_3,body_1,False,cA,cB,dB)
link_19.SetDistance(0)
link_19.SetName("Distance11")
exported_items.append(link_19)

link_20 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.0792018309847999,0.218074011807861,0.190019186850441)
dA = chrono.ChVectorD(1,3.88578058618805e-15,9.19431197843323e-13)
cB = chrono.ChVectorD(0.0792518309847909,0.268068030086162,0.199725993491048)
dB = chrono.ChVectorD(-1,-3.85802501057242e-15,-9.19320175540861e-13)
link_20.SetFlipped(True)
link_20.Initialize(body_3,body_1,False,cA,cB,dA,dB)
link_20.SetName("Distance11")
exported_items.append(link_20)


# Mate constraint: Distance12 [MateDistanceDim] type:5 align:1 flip:True
#   Entity 0: C::E name: body_2 , SW name: Spibot-LEG-4/upper_limb-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_7 , SW name: Spibot-LEG-4/limb_body_connector-1 ,  SW ref.type:2 (2)

link_21 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(0.0792018309848919,0.257531497332188,0.0897225902734949)
cB = chrono.ChVectorD(0.0791518309849744,0.247044380341677,-0.000221950290273443)
dA = chrono.ChVectorD(1,3.71924713249427e-15,9.20374887414255e-13)
dB = chrono.ChVectorD(-1,-3.88578058618805e-15,-9.19930798204405e-13)
link_21.Initialize(body_2,body_7,False,cA,cB,dB)
link_21.SetDistance(0)
link_21.SetName("Distance12")
exported_items.append(link_21)

link_22 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.0792018309848919,0.257531497332188,0.0897225902734949)
dA = chrono.ChVectorD(1,3.71924713249427e-15,9.20374887414255e-13)
cB = chrono.ChVectorD(0.0791518309849744,0.247044380341677,-0.000221950290273443)
dB = chrono.ChVectorD(-1,-3.88578058618805e-15,-9.19930798204405e-13)
link_22.SetFlipped(True)
link_22.Initialize(body_2,body_7,False,cA,cB,dA,dB)
link_22.SetName("Distance12")
exported_items.append(link_22)


# Mate constraint: Distance13 [MateDistanceDim] type:5 align:1 flip:True
#   Entity 0: C::E name: body_6 , SW name: Spibot-LEG-4/Actuator_body-2 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_2 , SW name: Spibot-LEG-4/upper_limb-1 ,  SW ref.type:2 (2)

link_23 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(0.0742518309850203,0.215774132705653,-0.0500533822663088)
cB = chrono.ChVectorD(0.0743018309849274,0.208654913539206,0.0511723040885544)
dA = chrono.ChVectorD(-1,-3.99680288865056e-15,-9.20041820506867e-13)
dB = chrono.ChVectorD(1,3.71924713249427e-15,9.20374887414255e-13)
link_23.Initialize(body_6,body_2,False,cA,cB,dB)
link_23.SetDistance(0)
link_23.SetName("Distance13")
exported_items.append(link_23)

link_24 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.0742518309850203,0.215774132705653,-0.0500533822663088)
dA = chrono.ChVectorD(-1,-3.99680288865056e-15,-9.20041820506867e-13)
cB = chrono.ChVectorD(0.0743018309849274,0.208654913539206,0.0511723040885544)
dB = chrono.ChVectorD(1,3.71924713249427e-15,9.20374887414255e-13)
link_24.SetFlipped(True)
link_24.Initialize(body_6,body_2,False,cA,cB,dA,dB)
link_24.SetName("Distance13")
exported_items.append(link_24)


# Mate constraint: Distance14 [MateDistanceDim] type:5 align:1 flip:False
#   Entity 0: C::E name: body_8 , SW name: Spibot-LEG-4/limb_body_connector-2 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_7 , SW name: Spibot-LEG-4/limb_body_connector-1 ,  SW ref.type:2 (2)

link_25 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(0.0866518309850388,0.225665705356419,-0.0701072295404399)
cB = chrono.ChVectorD(0.0866518309850388,0.24666539758002,-0.0702209243689368)
dA = chrono.ChVectorD(1.02695629777827e-15,0.999985343981005,-0.00541403945223742)
dB = chrono.ChVectorD(-9.99200722162641e-16,-0.999985343981005,0.00541403945223859)
link_25.Initialize(body_8,body_7,False,cA,cB,dB)
link_25.SetDistance(0)
link_25.SetName("Distance14")
exported_items.append(link_25)

link_26 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.0866518309850388,0.225665705356419,-0.0701072295404399)
dA = chrono.ChVectorD(1.02695629777827e-15,0.999985343981005,-0.00541403945223742)
cB = chrono.ChVectorD(0.0866518309850388,0.24666539758002,-0.0702209243689368)
dB = chrono.ChVectorD(-9.99200722162641e-16,-0.999985343981005,0.00541403945223859)
link_26.SetFlipped(True)
link_26.Initialize(body_8,body_7,False,cA,cB,dA,dB)
link_26.SetName("Distance14")
exported_items.append(link_26)


# Mate constraint: Concentric21 [MateConcentric] type:1 align:1 flip:False
#   Entity 0: C::E name: body_2 , SW name: Spibot-LEG-4/upper_limb-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_4 , SW name: Spibot-LEG-4/Actuator_body-1 ,  SW ref.type:2 (2)

link_27 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.0718018309849275,0.208654913539206,0.051172304088552)
dA = chrono.ChVectorD(1,3.71924713249427e-15,9.20374887414255e-13)
cB = chrono.ChVectorD(0.0844018309271748,0.208654913513033,0.051172303981864)
dB = chrono.ChVectorD(-1,-3.94129173741931e-15,-9.19653242448248e-13)
link_27.SetFlipped(True)
link_27.Initialize(body_2,body_4,False,cA,cB,dA,dB)
link_27.SetName("Concentric21")
exported_items.append(link_27)

link_28 = chrono.ChLinkMateGeneric()
link_28.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(0.0718018309849275,0.208654913539206,0.051172304088552)
cB = chrono.ChVectorD(0.0844018309271748,0.208654913513033,0.051172303981864)
dA = chrono.ChVectorD(1,3.71924713249427e-15,9.20374887414255e-13)
dB = chrono.ChVectorD(-1,-3.94129173741931e-15,-9.19653242448248e-13)
link_28.Initialize(body_2,body_4,False,cA,cB,dA,dB)
link_28.SetName("Concentric21")
exported_items.append(link_28)


# Mate constraint: Concentric22 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_2 , SW name: Spibot-LEG-4/upper_limb-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_5 , SW name: Spibot-LEG-4/Actuator_rod-2 ,  SW ref.type:2 (2)

link_29 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.0718018309849431,0.23058462889265,0.0341556174609964)
dA = chrono.ChVectorD(1,3.71924713249427e-15,9.20374887414255e-13)
cB = chrono.ChVectorD(0.0690518309849428,0.23058462889265,0.0341556174609938)
dB = chrono.ChVectorD(1,3.96904731303493e-15,9.20041820506867e-13)
link_29.Initialize(body_2,body_5,False,cA,cB,dA,dB)
link_29.SetName("Concentric22")
exported_items.append(link_29)

link_30 = chrono.ChLinkMateGeneric()
link_30.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(0.0718018309849431,0.23058462889265,0.0341556174609964)
cB = chrono.ChVectorD(0.0690518309849428,0.23058462889265,0.0341556174609938)
dA = chrono.ChVectorD(1,3.71924713249427e-15,9.20374887414255e-13)
dB = chrono.ChVectorD(1,3.96904731303493e-15,9.20041820506867e-13)
link_30.Initialize(body_2,body_5,False,cA,cB,dA,dB)
link_30.SetName("Concentric22")
exported_items.append(link_30)


# Mate constraint: Concentric3 [MateConcentric] type:1 align:1 flip:False
#   Entity 0: C::E name: body_16 , SW name: Spibot-LEG-3/upper_limb-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_14 , SW name: Spibot-LEG-3/lower_limb-1 ,  SW ref.type:2 (2)

link_1 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.074101830985188,0.254824477606069,-0.410270081717013)
dA = chrono.ChVectorD(1,5.24580379135386e-15,9.21707155043805e-13)
cB = chrono.ChVectorD(0.0865518309851897,0.254824477606067,-0.410270081717001)
dB = chrono.ChVectorD(-1,-3.66373598126302e-15,-9.19375686692092e-13)
link_1.SetFlipped(True)
link_1.Initialize(body_16,body_14,False,cA,cB,dA,dB)
link_1.SetName("Concentric3")
exported_items.append(link_1)

link_2 = chrono.ChLinkMateGeneric()
link_2.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(0.074101830985188,0.254824477606069,-0.410270081717013)
cB = chrono.ChVectorD(0.0865518309851897,0.254824477606067,-0.410270081717001)
dA = chrono.ChVectorD(1,5.24580379135386e-15,9.21707155043805e-13)
dB = chrono.ChVectorD(-1,-3.66373598126302e-15,-9.19375686692092e-13)
link_2.Initialize(body_16,body_14,False,cA,cB,dA,dB)
link_2.SetName("Concentric3")
exported_items.append(link_2)


# Mate constraint: Concentric4 [MateConcentric] type:1 align:1 flip:False
#   Entity 0: C::E name: body_14 , SW name: Spibot-LEG-3/lower_limb-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_15 , SW name: Spibot-LEG-3/Actuator_rod-1 ,  SW ref.type:2 (2)

link_3 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.0865518309851901,0.214825897420759,-0.410607102724471)
dA = chrono.ChVectorD(-1,-3.66373598126302e-15,-9.19375686692092e-13)
cB = chrono.ChVectorD(0.0741018309851883,0.21482589718075,-0.410607101247132)
dB = chrono.ChVectorD(1,5.49560397189452e-15,9.21374088136417e-13)
link_3.SetFlipped(True)
link_3.Initialize(body_14,body_15,False,cA,cB,dA,dB)
link_3.SetName("Concentric4")
exported_items.append(link_3)

link_4 = chrono.ChLinkMateGeneric()
link_4.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(0.0865518309851901,0.214825897420759,-0.410607102724471)
cB = chrono.ChVectorD(0.0741018309851883,0.21482589718075,-0.410607101247132)
dA = chrono.ChVectorD(-1,-3.66373598126302e-15,-9.19375686692092e-13)
dB = chrono.ChVectorD(1,5.49560397189452e-15,9.21374088136417e-13)
link_4.Initialize(body_14,body_15,False,cA,cB,dA,dB)
link_4.SetName("Concentric4")
exported_items.append(link_4)


# Mate constraint: Concentric6 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_15 , SW name: Spibot-LEG-3/Actuator_rod-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_13 , SW name: Spibot-LEG-3/Actuator_body-1 ,  SW ref.type:2 (2)

link_5 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.076501830985101,0.209440162606837,-0.315759887987597)
dA = chrono.ChVectorD(-9.19597731297017e-13,-0.0566919428832879,0.998391718521402)
cB = chrono.ChVectorD(0.0765018309851331,0.211444935647099,-0.351065628570515)
dB = chrono.ChVectorD(-9.19542220145786e-13,-0.0566919428832879,0.998391718521402)
link_5.Initialize(body_15,body_13,False,cA,cB,dA,dB)
link_5.SetName("Concentric6")
exported_items.append(link_5)

link_6 = chrono.ChLinkMateGeneric()
link_6.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(0.076501830985101,0.209440162606837,-0.315759887987597)
cB = chrono.ChVectorD(0.0765018309851331,0.211444935647099,-0.351065628570515)
dA = chrono.ChVectorD(-9.19597731297017e-13,-0.0566919428832879,0.998391718521402)
dB = chrono.ChVectorD(-9.19542220145786e-13,-0.0566919428832879,0.998391718521402)
link_6.Initialize(body_15,body_13,False,cA,cB,dA,dB)
link_6.SetName("Concentric6")
exported_items.append(link_6)


# Mate constraint: Concentric11 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_10 , SW name: Spibot-LEG-3/Actuator_rod-2 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_9 , SW name: Spibot-LEG-3/Actuator_body-2 ,  SW ref.type:2 (2)

link_7 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.076651830984995,0.220082306502972,-0.200147488976094)
dA = chrono.ChVectorD(-9.08495501050766e-13,-0.162544746914168,0.986701173228556)
cB = chrono.ChVectorD(0.0766518309850214,0.224877132786234,-0.22925369393774)
dB = chrono.ChVectorD(-9.08328967597072e-13,-0.162544746914168,0.986701173228556)
link_7.Initialize(body_10,body_9,False,cA,cB,dA,dB)
link_7.SetName("Concentric11")
exported_items.append(link_7)

link_8 = chrono.ChLinkMateGeneric()
link_8.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(0.076651830984995,0.220082306502972,-0.200147488976094)
cB = chrono.ChVectorD(0.0766518309850214,0.224877132786234,-0.22925369393774)
dA = chrono.ChVectorD(-9.08495501050766e-13,-0.162544746914168,0.986701173228556)
dB = chrono.ChVectorD(-9.08328967597072e-13,-0.162544746914168,0.986701173228556)
link_8.Initialize(body_10,body_9,False,cA,cB,dA,dB)
link_8.SetName("Concentric11")
exported_items.append(link_8)


# Mate constraint: Concentric12 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_16 , SW name: Spibot-LEG-3/upper_limb-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_12 , SW name: Spibot-LEG-3/limb_body_connector-1 ,  SW ref.type:2 (2)

link_9 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.0741018309850036,0.255907285496516,-0.210273012920812)
dA = chrono.ChVectorD(1,5.24580379135386e-15,9.21707155043805e-13)
cB = chrono.ChVectorD(0.0666518309850038,0.255907285496517,-0.210273012920818)
dB = chrono.ChVectorD(1,4.77395900588817e-15,9.20874487775336e-13)
link_9.Initialize(body_16,body_12,False,cA,cB,dA,dB)
link_9.SetName("Concentric12")
exported_items.append(link_9)

link_10 = chrono.ChLinkMateGeneric()
link_10.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(0.0741018309850036,0.255907285496516,-0.210273012920812)
cB = chrono.ChVectorD(0.0666518309850038,0.255907285496517,-0.210273012920818)
dA = chrono.ChVectorD(1,5.24580379135386e-15,9.21707155043805e-13)
dB = chrono.ChVectorD(1,4.77395900588817e-15,9.20874487775336e-13)
link_10.Initialize(body_16,body_12,False,cA,cB,dA,dB)
link_10.SetName("Concentric12")
exported_items.append(link_10)


# Mate constraint: Concentric13 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_9 , SW name: Spibot-LEG-3/Actuator_body-2 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_11 , SW name: Spibot-LEG-3/limb_body_connector-2 ,  SW ref.type:2 (2)

link_11 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.0690518309849669,0.215124447971384,-0.170051623544034)
dA = chrono.ChVectorD(1,5.41233724504764e-15,9.2148511043888e-13)
cB = chrono.ChVectorD(0.0666518309849669,0.215124447971385,-0.170051623544036)
dB = chrono.ChVectorD(1,4.82947015711943e-15,9.2104102122903e-13)
link_11.Initialize(body_9,body_11,False,cA,cB,dA,dB)
link_11.SetName("Concentric13")
exported_items.append(link_11)

link_12 = chrono.ChLinkMateGeneric()
link_12.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(0.0690518309849669,0.215124447971384,-0.170051623544034)
cB = chrono.ChVectorD(0.0666518309849669,0.215124447971385,-0.170051623544036)
dA = chrono.ChVectorD(1,5.41233724504764e-15,9.2148511043888e-13)
dB = chrono.ChVectorD(1,4.82947015711943e-15,9.2104102122903e-13)
link_12.Initialize(body_9,body_11,False,cA,cB,dA,dB)
link_12.SetName("Concentric13")
exported_items.append(link_12)


# Mate constraint: Concentric17 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_12 , SW name: Spibot-LEG-3/limb_body_connector-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_11 , SW name: Spibot-LEG-3/limb_body_connector-2 ,  SW ref.type:2 (2)

link_13 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.0766518309849485,0.246232274423841,-0.150219751887427)
dA = chrono.ChVectorD(1.66533453693773e-16,0.999985343981005,-0.00541403945223884)
cB = chrono.ChVectorD(0.0766518309849485,0.20523287532062,-0.149997776269885)
dB = chrono.ChVectorD(1.38777878078145e-16,0.999985343981005,-0.00541403945224)
link_13.Initialize(body_12,body_11,False,cA,cB,dA,dB)
link_13.SetName("Concentric17")
exported_items.append(link_13)

link_14 = chrono.ChLinkMateGeneric()
link_14.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(0.0766518309849485,0.246232274423841,-0.150219751887427)
cB = chrono.ChVectorD(0.0766518309849485,0.20523287532062,-0.149997776269885)
dA = chrono.ChVectorD(1.66533453693773e-16,0.999985343981005,-0.00541403945223884)
dB = chrono.ChVectorD(1.38777878078145e-16,0.999985343981005,-0.00541403945224)
link_14.Initialize(body_12,body_11,False,cA,cB,dA,dB)
link_14.SetName("Concentric17")
exported_items.append(link_14)


# Mate constraint: Parallel14 [MateParallel] type:3 align:0 flip:False
#   Entity 0: C::E name: body_16 , SW name: Spibot-LEG-3/upper_limb-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_15 , SW name: Spibot-LEG-3/Actuator_rod-1 ,  SW ref.type:2 (2)

link_15 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.0741018309850957,0.255365881551293,-0.310271547318912)
dA = chrono.ChVectorD(-1,-5.24580379135386e-15,-9.21707155043805e-13)
cB = chrono.ChVectorD(0.0741018309851883,0.21482589718075,-0.410607101247132)
dB = chrono.ChVectorD(-1,-5.49560397189452e-15,-9.21374088136417e-13)
link_15.Initialize(body_16,body_15,False,cA,cB,dA,dB)
link_15.SetName("Parallel14")
exported_items.append(link_15)


# Mate constraint: Parallel15 [MateParallel] type:3 align:0 flip:False
#   Entity 0: C::E name: body_16 , SW name: Spibot-LEG-3/upper_limb-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_10 , SW name: Spibot-LEG-3/Actuator_rod-2 ,  SW ref.type:2 (2)

link_16 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.07900183098506,0.206909582504679,-0.271194289342969)
dA = chrono.ChVectorD(-1,-5.24580379135386e-15,-9.21707155043805e-13)
cB = chrono.ChVectorD(0.0742518309850447,0.229022267583251,-0.254416053503667)
dB = chrono.ChVectorD(-1,-5.16253706450698e-15,-9.21651643892574e-13)
link_16.Initialize(body_16,body_10,False,cA,cB,dA,dB)
link_16.SetName("Parallel15")
exported_items.append(link_16)


# Mate constraint: Distance10 [MateDistanceDim] type:5 align:1 flip:False
#   Entity 0: C::E name: body_16 , SW name: Spibot-LEG-3/upper_limb-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_14 , SW name: Spibot-LEG-3/lower_limb-1 ,  SW ref.type:2 (2)

link_17 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(0.0741018309850957,0.255365881551293,-0.310271547318912)
cB = chrono.ChVectorD(0.0740518309851989,0.264829346426337,-0.420265210525047)
dA = chrono.ChVectorD(-1,-5.24580379135386e-15,-9.21707155043805e-13)
dB = chrono.ChVectorD(1,3.44169137633799e-15,9.19320175540861e-13)
link_17.Initialize(body_16,body_14,False,cA,cB,dB)
link_17.SetDistance(0)
link_17.SetName("Distance10")
exported_items.append(link_17)

link_18 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.0741018309850957,0.255365881551293,-0.310271547318912)
dA = chrono.ChVectorD(-1,-5.24580379135386e-15,-9.21707155043805e-13)
cB = chrono.ChVectorD(0.0740518309851989,0.264829346426337,-0.420265210525047)
dB = chrono.ChVectorD(1,3.44169137633799e-15,9.19320175540861e-13)
link_18.SetFlipped(True)
link_18.Initialize(body_16,body_14,False,cA,cB,dA,dB)
link_18.SetName("Distance10")
exported_items.append(link_18)


# Mate constraint: Distance11 [MateDistanceDim] type:5 align:1 flip:False
#   Entity 0: C::E name: body_15 , SW name: Spibot-LEG-3/Actuator_rod-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_14 , SW name: Spibot-LEG-3/lower_limb-1 ,  SW ref.type:2 (2)

link_19 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(0.0741018309851883,0.21482589718075,-0.410607101247132)
cB = chrono.ChVectorD(0.0740518309851989,0.264829346426337,-0.420265210525047)
dA = chrono.ChVectorD(-1,-5.49560397189452e-15,-9.21374088136417e-13)
dB = chrono.ChVectorD(1,3.44169137633799e-15,9.19320175540861e-13)
link_19.Initialize(body_15,body_14,False,cA,cB,dB)
link_19.SetDistance(0)
link_19.SetName("Distance11")
exported_items.append(link_19)

link_20 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.0741018309851883,0.21482589718075,-0.410607101247132)
dA = chrono.ChVectorD(-1,-5.49560397189452e-15,-9.21374088136417e-13)
cB = chrono.ChVectorD(0.0740518309851989,0.264829346426337,-0.420265210525047)
dB = chrono.ChVectorD(1,3.44169137633799e-15,9.19320175540861e-13)
link_20.SetFlipped(True)
link_20.Initialize(body_15,body_14,False,cA,cB,dA,dB)
link_20.SetName("Distance11")
exported_items.append(link_20)


# Mate constraint: Distance12 [MateDistanceDim] type:5 align:1 flip:True
#   Entity 0: C::E name: body_16 , SW name: Spibot-LEG-3/upper_limb-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_12 , SW name: Spibot-LEG-3/limb_body_connector-1 ,  SW ref.type:2 (2)

link_21 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(0.0741018309850957,0.255365881551293,-0.310271547318912)
cB = chrono.ChVectorD(0.074151830985013,0.245853291662184,-0.220218725966099)
dA = chrono.ChVectorD(-1,-5.24580379135386e-15,-9.21707155043805e-13)
dB = chrono.ChVectorD(1,4.8017145815038e-15,9.20652443170411e-13)
link_21.Initialize(body_16,body_12,False,cA,cB,dB)
link_21.SetDistance(0)
link_21.SetName("Distance12")
exported_items.append(link_21)

link_22 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.0741018309850957,0.255365881551293,-0.310271547318912)
dA = chrono.ChVectorD(-1,-5.24580379135386e-15,-9.21707155043805e-13)
cB = chrono.ChVectorD(0.074151830985013,0.245853291662184,-0.220218725966099)
dB = chrono.ChVectorD(1,4.8017145815038e-15,9.20652443170411e-13)
link_22.SetFlipped(True)
link_22.Initialize(body_16,body_12,False,cA,cB,dA,dB)
link_22.SetName("Distance12")
exported_items.append(link_22)


# Mate constraint: Distance13 [MateDistanceDim] type:5 align:1 flip:True
#   Entity 0: C::E name: body_9 , SW name: Spibot-LEG-3/Actuator_body-2 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_16 , SW name: Spibot-LEG-3/upper_limb-1 ,  SW ref.type:2 (2)

link_23 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(0.0790518309849669,0.215124447971384,-0.170051623544024)
cB = chrono.ChVectorD(0.07900183098506,0.206909582504679,-0.271194289342969)
dA = chrono.ChVectorD(1,5.41233724504764e-15,9.2148511043888e-13)
dB = chrono.ChVectorD(-1,-5.24580379135386e-15,-9.21707155043805e-13)
link_23.Initialize(body_9,body_16,False,cA,cB,dB)
link_23.SetDistance(0)
link_23.SetName("Distance13")
exported_items.append(link_23)

link_24 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.0790518309849669,0.215124447971384,-0.170051623544024)
dA = chrono.ChVectorD(1,5.41233724504764e-15,9.2148511043888e-13)
cB = chrono.ChVectorD(0.07900183098506,0.206909582504679,-0.271194289342969)
dB = chrono.ChVectorD(-1,-5.24580379135386e-15,-9.21707155043805e-13)
link_24.SetFlipped(True)
link_24.Initialize(body_9,body_16,False,cA,cB,dA,dB)
link_24.SetName("Distance13")
exported_items.append(link_24)


# Mate constraint: Distance14 [MateDistanceDim] type:5 align:1 flip:False
#   Entity 0: C::E name: body_11 , SW name: Spibot-LEG-3/limb_body_connector-2 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_12 , SW name: Spibot-LEG-3/limb_body_connector-1 ,  SW ref.type:2 (2)

link_25 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(0.0666518309849485,0.22523258220024,-0.150106057058939)
cB = chrono.ChVectorD(0.0666518309849485,0.246232274423841,-0.150219751887436)
dA = chrono.ChVectorD(1.38777878078145e-16,0.999985343981005,-0.00541403945224)
dB = chrono.ChVectorD(-1.66533453693773e-16,-0.999985343981005,0.00541403945223884)
link_25.Initialize(body_11,body_12,False,cA,cB,dB)
link_25.SetDistance(0)
link_25.SetName("Distance14")
exported_items.append(link_25)

link_26 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.0666518309849485,0.22523258220024,-0.150106057058939)
dA = chrono.ChVectorD(1.38777878078145e-16,0.999985343981005,-0.00541403945224)
cB = chrono.ChVectorD(0.0666518309849485,0.246232274423841,-0.150219751887436)
dB = chrono.ChVectorD(-1.66533453693773e-16,-0.999985343981005,0.00541403945223884)
link_26.SetFlipped(True)
link_26.Initialize(body_11,body_12,False,cA,cB,dA,dB)
link_26.SetName("Distance14")
exported_items.append(link_26)


# Mate constraint: Concentric21 [MateConcentric] type:1 align:1 flip:False
#   Entity 0: C::E name: body_16 , SW name: Spibot-LEG-3/upper_limb-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_13 , SW name: Spibot-LEG-3/Actuator_body-1 ,  SW ref.type:2 (2)

link_27 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.08150183098506,0.206909582504679,-0.271194289342967)
dA = chrono.ChVectorD(-1,-5.24580379135386e-15,-9.21707155043805e-13)
cB = chrono.ChVectorD(0.0689018309850595,0.206909580216436,-0.27119429108881)
dB = chrono.ChVectorD(1,5.24580379135386e-15,9.2148511043888e-13)
link_27.SetFlipped(True)
link_27.Initialize(body_16,body_13,False,cA,cB,dA,dB)
link_27.SetName("Concentric21")
exported_items.append(link_27)

link_28 = chrono.ChLinkMateGeneric()
link_28.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(0.08150183098506,0.206909582504679,-0.271194289342967)
cB = chrono.ChVectorD(0.0689018309850595,0.206909580216436,-0.27119429108881)
dA = chrono.ChVectorD(-1,-5.24580379135386e-15,-9.21707155043805e-13)
dB = chrono.ChVectorD(1,5.24580379135386e-15,9.2148511043888e-13)
link_28.Initialize(body_16,body_13,False,cA,cB,dA,dB)
link_28.SetName("Concentric21")
exported_items.append(link_28)


# Mate constraint: Concentric22 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_16 , SW name: Spibot-LEG-3/upper_limb-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_10 , SW name: Spibot-LEG-3/Actuator_rod-2 ,  SW ref.type:2 (2)

link_29 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.0815018309850444,0.229022267583251,-0.254416053503661)
dA = chrono.ChVectorD(-1,-5.24580379135386e-15,-9.21707155043805e-13)
cB = chrono.ChVectorD(0.084251830985045,0.229022267583251,-0.254416053503658)
dB = chrono.ChVectorD(-1,-5.16253706450698e-15,-9.21651643892574e-13)
link_29.Initialize(body_16,body_10,False,cA,cB,dA,dB)
link_29.SetName("Concentric22")
exported_items.append(link_29)

link_30 = chrono.ChLinkMateGeneric()
link_30.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(0.0815018309850444,0.229022267583251,-0.254416053503661)
cB = chrono.ChVectorD(0.084251830985045,0.229022267583251,-0.254416053503658)
dA = chrono.ChVectorD(-1,-5.24580379135386e-15,-9.21707155043805e-13)
dB = chrono.ChVectorD(-1,-5.16253706450698e-15,-9.21651643892574e-13)
link_30.Initialize(body_16,body_10,False,cA,cB,dA,dB)
link_30.SetName("Concentric22")
exported_items.append(link_30)


# Mate constraint: Concentric3 [MateConcentric] type:1 align:1 flip:False
#   Entity 0: C::E name: body_22 , SW name: Spibot-LEG-2/upper_limb-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_21 , SW name: Spibot-LEG-2/lower_limb-1 ,  SW ref.type:2 (2)

link_1 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.0158981690148121,0.254824477456328,-0.410270081716101)
dA = chrono.ChVectorD(1,4.9960036108132e-15,9.20430398565486e-13)
cB = chrono.ChVectorD(-0.00344816901481204,0.254824477627324,-0.410270081703698)
dB = chrono.ChVectorD(-1,-4.96824803519758e-15,-9.20097331658098e-13)
link_1.SetFlipped(True)
link_1.Initialize(body_22,body_21,False,cA,cB,dA,dB)
link_1.SetName("Concentric3")
exported_items.append(link_1)

link_2 = chrono.ChLinkMateGeneric()
link_2.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.0158981690148121,0.254824477456328,-0.410270081716101)
cB = chrono.ChVectorD(-0.00344816901481204,0.254824477627324,-0.410270081703698)
dA = chrono.ChVectorD(1,4.9960036108132e-15,9.20430398565486e-13)
dB = chrono.ChVectorD(-1,-4.96824803519758e-15,-9.20097331658098e-13)
link_2.Initialize(body_22,body_21,False,cA,cB,dA,dB)
link_2.SetName("Concentric3")
exported_items.append(link_2)


# Mate constraint: Concentric4 [MateConcentric] type:1 align:1 flip:False
#   Entity 0: C::E name: body_21 , SW name: Spibot-LEG-2/lower_limb-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_17 , SW name: Spibot-LEG-2/Actuator_rod-1 ,  SW ref.type:2 (2)

link_3 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.0034481690148116,0.214825897442034,-0.410607102713322)
dA = chrono.ChVectorD(-1,-4.96824803519758e-15,-9.20097331658098e-13)
cB = chrono.ChVectorD(-0.0158981653624138,0.214825897904244,-0.410607100111453)
dB = chrono.ChVectorD(1,4.46864767411626e-15,9.20208353960561e-13)
link_3.SetFlipped(True)
link_3.Initialize(body_21,body_17,False,cA,cB,dA,dB)
link_3.SetName("Concentric4")
exported_items.append(link_3)

link_4 = chrono.ChLinkMateGeneric()
link_4.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.0034481690148116,0.214825897442034,-0.410607102713322)
cB = chrono.ChVectorD(-0.0158981653624138,0.214825897904244,-0.410607100111453)
dA = chrono.ChVectorD(-1,-4.96824803519758e-15,-9.20097331658098e-13)
dB = chrono.ChVectorD(1,4.46864767411626e-15,9.20208353960561e-13)
link_4.Initialize(body_21,body_17,False,cA,cB,dA,dB)
link_4.SetName("Concentric4")
exported_items.append(link_4)


# Mate constraint: Concentric6 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_17 , SW name: Spibot-LEG-2/Actuator_rod-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_18 , SW name: Spibot-LEG-2/Actuator_body-1 ,  SW ref.type:2 (2)

link_5 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.013498165362501,0.209440163402398,-0.315759886847826)
dA = chrono.ChVectorD(-9.18654041726086e-13,-0.0566919421246893,0.998391718564478)
cB = chrono.ChVectorD(-0.0134981690148668,0.211444936555023,-0.351065627763365)
dB = chrono.ChVectorD(-9.18543019423623e-13,-0.0566919421246891,0.998391718564478)
link_5.Initialize(body_17,body_18,False,cA,cB,dA,dB)
link_5.SetName("Concentric6")
exported_items.append(link_5)

link_6 = chrono.ChLinkMateGeneric()
link_6.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.013498165362501,0.209440163402398,-0.315759886847826)
cB = chrono.ChVectorD(-0.0134981690148668,0.211444936555023,-0.351065627763365)
dA = chrono.ChVectorD(-9.18654041726086e-13,-0.0566919421246893,0.998391718564478)
dB = chrono.ChVectorD(-9.18543019423623e-13,-0.0566919421246891,0.998391718564478)
link_6.Initialize(body_17,body_18,False,cA,cB,dA,dB)
link_6.SetName("Concentric6")
exported_items.append(link_6)


# Mate constraint: Concentric11 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_23 , SW name: Spibot-LEG-2/Actuator_rod-2 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_24 , SW name: Spibot-LEG-2/Actuator_body-2 ,  SW ref.type:2 (2)

link_7 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.013348169015011,0.220082309935804,-0.200147482679995)
dA = chrono.ChVectorD(-9.06830166513828e-13,-0.16254474657559,0.986701173284332)
cB = chrono.ChVectorD(-0.0133481690149837,0.224877136473812,-0.229253689250305)
dB = chrono.ChVectorD(-9.06885677665059e-13,-0.16254474657559,0.986701173284332)
link_7.Initialize(body_23,body_24,False,cA,cB,dA,dB)
link_7.SetName("Concentric11")
exported_items.append(link_7)

link_8 = chrono.ChLinkMateGeneric()
link_8.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.013348169015011,0.220082309935804,-0.200147482679995)
cB = chrono.ChVectorD(-0.0133481690149837,0.224877136473812,-0.229253689250305)
dA = chrono.ChVectorD(-9.06830166513828e-13,-0.16254474657559,0.986701173284332)
dB = chrono.ChVectorD(-9.06885677665059e-13,-0.16254474657559,0.986701173284332)
link_8.Initialize(body_23,body_24,False,cA,cB,dA,dB)
link_8.SetName("Concentric11")
exported_items.append(link_8)


# Mate constraint: Concentric12 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_22 , SW name: Spibot-LEG-2/upper_limb-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_19 , SW name: Spibot-LEG-2/limb_body_connector-1 ,  SW ref.type:2 (2)

link_9 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.0158981690149963,0.255907285496517,-0.21027301292071)
dA = chrono.ChVectorD(1,4.9960036108132e-15,9.20430398565486e-13)
cB = chrono.ChVectorD(-0.0233481690149961,0.255907285496517,-0.210273012920717)
dB = chrono.ChVectorD(1,5.24580379135386e-15,9.20430398565486e-13)
link_9.Initialize(body_22,body_19,False,cA,cB,dA,dB)
link_9.SetName("Concentric12")
exported_items.append(link_9)

link_10 = chrono.ChLinkMateGeneric()
link_10.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.0158981690149963,0.255907285496517,-0.21027301292071)
cB = chrono.ChVectorD(-0.0233481690149961,0.255907285496517,-0.210273012920717)
dA = chrono.ChVectorD(1,4.9960036108132e-15,9.20430398565486e-13)
dB = chrono.ChVectorD(1,5.24580379135386e-15,9.20430398565486e-13)
link_10.Initialize(body_22,body_19,False,cA,cB,dA,dB)
link_10.SetName("Concentric12")
exported_items.append(link_10)


# Mate constraint: Concentric13 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_24 , SW name: Spibot-LEG-2/Actuator_body-2 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_20 , SW name: Spibot-LEG-2/limb_body_connector-2 ,  SW ref.type:2 (2)

link_11 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.020948169015038,0.215124451679277,-0.170051618853253)
dA = chrono.ChVectorD(1,5.74540415243519e-15,9.19986309355636e-13)
cB = chrono.ChVectorD(-0.023348169015033,0.215124447971385,-0.170051623543935)
dB = chrono.ChVectorD(1,5.27355936696949e-15,9.20652443170411e-13)
link_11.Initialize(body_24,body_20,False,cA,cB,dA,dB)
link_11.SetName("Concentric13")
exported_items.append(link_11)

link_12 = chrono.ChLinkMateGeneric()
link_12.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.020948169015038,0.215124451679277,-0.170051618853253)
cB = chrono.ChVectorD(-0.023348169015033,0.215124447971385,-0.170051623543935)
dA = chrono.ChVectorD(1,5.74540415243519e-15,9.19986309355636e-13)
dB = chrono.ChVectorD(1,5.27355936696949e-15,9.20652443170411e-13)
link_12.Initialize(body_24,body_20,False,cA,cB,dA,dB)
link_12.SetName("Concentric13")
exported_items.append(link_12)


# Mate constraint: Concentric17 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_19 , SW name: Spibot-LEG-2/limb_body_connector-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_20 , SW name: Spibot-LEG-2/limb_body_connector-2 ,  SW ref.type:2 (2)

link_13 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.0133481690150514,0.246232274423842,-0.150219751887325)
dA = chrono.ChVectorD(-3.05311331771918e-16,0.999985343981006,-0.00541403945223862)
cB = chrono.ChVectorD(-0.0133481690150513,0.20523287532062,-0.149997776269783)
dB = chrono.ChVectorD(-3.33066907387547e-16,0.999985343981006,-0.00541403945223984)
link_13.Initialize(body_19,body_20,False,cA,cB,dA,dB)
link_13.SetName("Concentric17")
exported_items.append(link_13)

link_14 = chrono.ChLinkMateGeneric()
link_14.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.0133481690150514,0.246232274423842,-0.150219751887325)
cB = chrono.ChVectorD(-0.0133481690150513,0.20523287532062,-0.149997776269783)
dA = chrono.ChVectorD(-3.05311331771918e-16,0.999985343981006,-0.00541403945223862)
dB = chrono.ChVectorD(-3.33066907387547e-16,0.999985343981006,-0.00541403945223984)
link_14.Initialize(body_19,body_20,False,cA,cB,dA,dB)
link_14.SetName("Concentric17")
exported_items.append(link_14)


# Mate constraint: Parallel14 [MateParallel] type:3 align:0 flip:False
#   Entity 0: C::E name: body_22 , SW name: Spibot-LEG-2/upper_limb-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_17 , SW name: Spibot-LEG-2/Actuator_rod-1 ,  SW ref.type:2 (2)

link_15 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.0158981690149043,0.255365881476422,-0.310271547318406)
dA = chrono.ChVectorD(-1,-4.9960036108132e-15,-9.20430398565486e-13)
cB = chrono.ChVectorD(-0.0158981653624138,0.214825897904244,-0.410607100111453)
dB = chrono.ChVectorD(-1,-4.46864767411626e-15,-9.20208353960561e-13)
link_15.Initialize(body_22,body_17,False,cA,cB,dA,dB)
link_15.SetName("Parallel14")
exported_items.append(link_15)


# Mate constraint: Parallel15 [MateParallel] type:3 align:0 flip:False
#   Entity 0: C::E name: body_22 , SW name: Spibot-LEG-2/upper_limb-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_23 , SW name: Spibot-LEG-2/Actuator_rod-2 ,  SW ref.type:2 (2)

link_16 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.01099816901494,0.206909582459067,-0.271194289306182)
dA = chrono.ChVectorD(-1,-4.9960036108132e-15,-9.20430398565486e-13)
cB = chrono.ChVectorD(-0.0157481690149611,0.229022270997461,-0.254416047210635)
dB = chrono.ChVectorD(-1,-5.6621374255883e-15,-9.19875287053173e-13)
link_16.Initialize(body_22,body_23,False,cA,cB,dA,dB)
link_16.SetName("Parallel15")
exported_items.append(link_16)


# Mate constraint: Distance10 [MateDistanceDim] type:5 align:1 flip:False
#   Entity 0: C::E name: body_22 , SW name: Spibot-LEG-2/upper_limb-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_21 , SW name: Spibot-LEG-2/lower_limb-1 ,  SW ref.type:2 (2)

link_17 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(-0.0158981690149043,0.255365881476422,-0.310271547318406)
cB = chrono.ChVectorD(-0.0159481690148029,0.264829346448133,-0.420265210511204)
dA = chrono.ChVectorD(-1,-4.9960036108132e-15,-9.20430398565486e-13)
dB = chrono.ChVectorD(1,4.74620343027254e-15,9.20097331658098e-13)
link_17.Initialize(body_22,body_21,False,cA,cB,dB)
link_17.SetDistance(0)
link_17.SetName("Distance10")
exported_items.append(link_17)

link_18 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.0158981690149043,0.255365881476422,-0.310271547318406)
dA = chrono.ChVectorD(-1,-4.9960036108132e-15,-9.20430398565486e-13)
cB = chrono.ChVectorD(-0.0159481690148029,0.264829346448133,-0.420265210511204)
dB = chrono.ChVectorD(1,4.74620343027254e-15,9.20097331658098e-13)
link_18.SetFlipped(True)
link_18.Initialize(body_22,body_21,False,cA,cB,dA,dB)
link_18.SetName("Distance10")
exported_items.append(link_18)


# Mate constraint: Distance11 [MateDistanceDim] type:5 align:1 flip:False
#   Entity 0: C::E name: body_17 , SW name: Spibot-LEG-2/Actuator_rod-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_21 , SW name: Spibot-LEG-2/lower_limb-1 ,  SW ref.type:2 (2)

link_19 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(-0.0158981653624138,0.214825897904244,-0.410607100111453)
cB = chrono.ChVectorD(-0.0159481690148029,0.264829346448133,-0.420265210511204)
dA = chrono.ChVectorD(-1,-4.46864767411626e-15,-9.20208353960561e-13)
dB = chrono.ChVectorD(1,4.74620343027254e-15,9.20097331658098e-13)
link_19.Initialize(body_17,body_21,False,cA,cB,dB)
link_19.SetDistance(0)
link_19.SetName("Distance11")
exported_items.append(link_19)

link_20 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.0158981653624138,0.214825897904244,-0.410607100111453)
dA = chrono.ChVectorD(-1,-4.46864767411626e-15,-9.20208353960561e-13)
cB = chrono.ChVectorD(-0.0159481690148029,0.264829346448133,-0.420265210511204)
dB = chrono.ChVectorD(1,4.74620343027254e-15,9.20097331658098e-13)
link_20.SetFlipped(True)
link_20.Initialize(body_17,body_21,False,cA,cB,dA,dB)
link_20.SetName("Distance11")
exported_items.append(link_20)


# Mate constraint: Distance12 [MateDistanceDim] type:5 align:1 flip:True
#   Entity 0: C::E name: body_22 , SW name: Spibot-LEG-2/upper_limb-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_19 , SW name: Spibot-LEG-2/limb_body_connector-1 ,  SW ref.type:2 (2)

link_21 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(-0.0158981690149043,0.255365881476422,-0.310271547318406)
cB = chrono.ChVectorD(-0.015848169014987,0.245853291662185,-0.220218725965998)
dA = chrono.ChVectorD(-1,-4.9960036108132e-15,-9.20430398565486e-13)
dB = chrono.ChVectorD(1,5.27355936696949e-15,9.2015284280933e-13)
link_21.Initialize(body_22,body_19,False,cA,cB,dB)
link_21.SetDistance(0)
link_21.SetName("Distance12")
exported_items.append(link_21)

link_22 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.0158981690149043,0.255365881476422,-0.310271547318406)
dA = chrono.ChVectorD(-1,-4.9960036108132e-15,-9.20430398565486e-13)
cB = chrono.ChVectorD(-0.015848169014987,0.245853291662185,-0.220218725965998)
dB = chrono.ChVectorD(1,5.27355936696949e-15,9.2015284280933e-13)
link_22.SetFlipped(True)
link_22.Initialize(body_22,body_19,False,cA,cB,dA,dB)
link_22.SetName("Distance12")
exported_items.append(link_22)


# Mate constraint: Distance13 [MateDistanceDim] type:5 align:1 flip:True
#   Entity 0: C::E name: body_24 , SW name: Spibot-LEG-2/Actuator_body-2 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_22 , SW name: Spibot-LEG-2/upper_limb-1 ,  SW ref.type:2 (2)

link_23 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(-0.0109481690150381,0.215124451679277,-0.170051618853243)
cB = chrono.ChVectorD(-0.01099816901494,0.206909582459067,-0.271194289306182)
dA = chrono.ChVectorD(1,5.74540415243519e-15,9.19986309355636e-13)
dB = chrono.ChVectorD(-1,-4.9960036108132e-15,-9.20430398565486e-13)
link_23.Initialize(body_24,body_22,False,cA,cB,dB)
link_23.SetDistance(0)
link_23.SetName("Distance13")
exported_items.append(link_23)

link_24 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.0109481690150381,0.215124451679277,-0.170051618853243)
dA = chrono.ChVectorD(1,5.74540415243519e-15,9.19986309355636e-13)
cB = chrono.ChVectorD(-0.01099816901494,0.206909582459067,-0.271194289306182)
dB = chrono.ChVectorD(-1,-4.9960036108132e-15,-9.20430398565486e-13)
link_24.SetFlipped(True)
link_24.Initialize(body_24,body_22,False,cA,cB,dA,dB)
link_24.SetName("Distance13")
exported_items.append(link_24)


# Mate constraint: Distance14 [MateDistanceDim] type:5 align:1 flip:False
#   Entity 0: C::E name: body_20 , SW name: Spibot-LEG-2/limb_body_connector-2 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_19 , SW name: Spibot-LEG-2/limb_body_connector-1 ,  SW ref.type:2 (2)

link_25 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(-0.0233481690150513,0.22523258220024,-0.150106057058837)
cB = chrono.ChVectorD(-0.0233481690150514,0.246232274423841,-0.150219751887334)
dA = chrono.ChVectorD(-3.33066907387547e-16,0.999985343981006,-0.00541403945223984)
dB = chrono.ChVectorD(3.05311331771918e-16,-0.999985343981006,0.00541403945223862)
link_25.Initialize(body_20,body_19,False,cA,cB,dB)
link_25.SetDistance(0)
link_25.SetName("Distance14")
exported_items.append(link_25)

link_26 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.0233481690150513,0.22523258220024,-0.150106057058837)
dA = chrono.ChVectorD(-3.33066907387547e-16,0.999985343981006,-0.00541403945223984)
cB = chrono.ChVectorD(-0.0233481690150514,0.246232274423841,-0.150219751887334)
dB = chrono.ChVectorD(3.05311331771918e-16,-0.999985343981006,0.00541403945223862)
link_26.SetFlipped(True)
link_26.Initialize(body_20,body_19,False,cA,cB,dA,dB)
link_26.SetName("Distance14")
exported_items.append(link_26)


# Mate constraint: Concentric21 [MateConcentric] type:1 align:1 flip:False
#   Entity 0: C::E name: body_22 , SW name: Spibot-LEG-2/upper_limb-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_18 , SW name: Spibot-LEG-2/Actuator_body-1 ,  SW ref.type:2 (2)

link_27 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.00849816901493994,0.206909582459067,-0.27119428930618)
dA = chrono.ChVectorD(-1,-4.9960036108132e-15,-9.20430398565486e-13)
cB = chrono.ChVectorD(-0.0210981690149402,0.206909581185048,-0.271194290278214)
dB = chrono.ChVectorD(1,5.10702591327572e-15,9.2015284280933e-13)
link_27.SetFlipped(True)
link_27.Initialize(body_22,body_18,False,cA,cB,dA,dB)
link_27.SetName("Concentric21")
exported_items.append(link_27)

link_28 = chrono.ChLinkMateGeneric()
link_28.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.00849816901493994,0.206909582459067,-0.27119428930618)
cB = chrono.ChVectorD(-0.0210981690149402,0.206909581185048,-0.271194290278214)
dA = chrono.ChVectorD(-1,-4.9960036108132e-15,-9.20430398565486e-13)
dB = chrono.ChVectorD(1,5.10702591327572e-15,9.2015284280933e-13)
link_28.Initialize(body_22,body_18,False,cA,cB,dA,dB)
link_28.SetName("Concentric21")
exported_items.append(link_28)


# Mate constraint: Concentric22 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_22 , SW name: Spibot-LEG-2/upper_limb-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_23 , SW name: Spibot-LEG-2/Actuator_rod-2 ,  SW ref.type:2 (2)

link_29 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.00849816901495559,0.229022267550202,-0.25441605348343)
dA = chrono.ChVectorD(-1,-4.9960036108132e-15,-9.20430398565486e-13)
cB = chrono.ChVectorD(-0.00574816901496122,0.229022270997461,-0.254416047210626)
dB = chrono.ChVectorD(-1,-5.6621374255883e-15,-9.19875287053173e-13)
link_29.Initialize(body_22,body_23,False,cA,cB,dA,dB)
link_29.SetName("Concentric22")
exported_items.append(link_29)

link_30 = chrono.ChLinkMateGeneric()
link_30.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.00849816901495559,0.229022267550202,-0.25441605348343)
cB = chrono.ChVectorD(-0.00574816901496122,0.229022270997461,-0.254416047210626)
dA = chrono.ChVectorD(-1,-4.9960036108132e-15,-9.20430398565486e-13)
dB = chrono.ChVectorD(-1,-5.6621374255883e-15,-9.19875287053173e-13)
link_30.Initialize(body_22,body_23,False,cA,cB,dA,dB)
link_30.SetName("Concentric22")
exported_items.append(link_30)


# Mate constraint: Concentric3 [MateConcentric] type:1 align:1 flip:False
#   Entity 0: C::E name: body_31 , SW name: Spibot-LEG-1/upper_limb-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_30 , SW name: Spibot-LEG-1/lower_limb-1 ,  SW ref.type:2 (2)

link_1 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.105898169014812,0.254824477306583,-0.410270081715189)
dA = chrono.ChVectorD(1,4.66293670342566e-15,9.19986309355636e-13)
cB = chrono.ChVectorD(-0.0934481690148142,0.254824477648568,-0.410270081690401)
dB = chrono.ChVectorD(-1,-5.05151476204446e-15,-9.20041820506867e-13)
link_1.SetFlipped(True)
link_1.Initialize(body_31,body_30,False,cA,cB,dA,dB)
link_1.SetName("Concentric3")
exported_items.append(link_1)

link_2 = chrono.ChLinkMateGeneric()
link_2.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.105898169014812,0.254824477306583,-0.410270081715189)
cB = chrono.ChVectorD(-0.0934481690148142,0.254824477648568,-0.410270081690401)
dA = chrono.ChVectorD(1,4.66293670342566e-15,9.19986309355636e-13)
dB = chrono.ChVectorD(-1,-5.05151476204446e-15,-9.20041820506867e-13)
link_2.Initialize(body_31,body_30,False,cA,cB,dA,dB)
link_2.SetName("Concentric3")
exported_items.append(link_2)


# Mate constraint: Concentric4 [MateConcentric] type:1 align:1 flip:False
#   Entity 0: C::E name: body_30 , SW name: Spibot-LEG-1/lower_limb-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_29 , SW name: Spibot-LEG-1/Actuator_rod-1 ,  SW ref.type:2 (2)

link_3 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.0934481690148138,0.214825897463296,-0.410607102702179)
dA = chrono.ChVectorD(-1,-5.05151476204446e-15,-9.20041820506867e-13)
cB = chrono.ChVectorD(-0.105898169014812,0.214825896704608,-0.410607100162012)
dB = chrono.ChVectorD(1,4.8017145815038e-15,9.19875287053173e-13)
link_3.SetFlipped(True)
link_3.Initialize(body_30,body_29,False,cA,cB,dA,dB)
link_3.SetName("Concentric4")
exported_items.append(link_3)

link_4 = chrono.ChLinkMateGeneric()
link_4.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.0934481690148138,0.214825897463296,-0.410607102702179)
cB = chrono.ChVectorD(-0.105898169014812,0.214825896704608,-0.410607100162012)
dA = chrono.ChVectorD(-1,-5.05151476204446e-15,-9.20041820506867e-13)
dB = chrono.ChVectorD(1,4.8017145815038e-15,9.19875287053173e-13)
link_4.Initialize(body_30,body_29,False,cA,cB,dA,dB)
link_4.SetName("Concentric4")
exported_items.append(link_4)


# Mate constraint: Concentric6 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_29 , SW name: Spibot-LEG-1/Actuator_rod-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_28 , SW name: Spibot-LEG-1/Actuator_body-1 ,  SW ref.type:2 (2)

link_5 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.103498169014899,0.209440162274831,-0.315759886894292)
dA = chrono.ChVectorD(-9.18265463667467e-13,-0.0566919413660766,0.998391718607554)
cB = chrono.ChVectorD(-0.103498169014866,0.211444937462939,-0.351065626956219)
dB = chrono.ChVectorD(-9.18209952516236e-13,-0.0566919413660766,0.998391718607554)
link_5.Initialize(body_29,body_28,False,cA,cB,dA,dB)
link_5.SetName("Concentric6")
exported_items.append(link_5)

link_6 = chrono.ChLinkMateGeneric()
link_6.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.103498169014899,0.209440162274831,-0.315759886894292)
cB = chrono.ChVectorD(-0.103498169014866,0.211444937462939,-0.351065626956219)
dA = chrono.ChVectorD(-9.18265463667467e-13,-0.0566919413660766,0.998391718607554)
dB = chrono.ChVectorD(-9.18209952516236e-13,-0.0566919413660766,0.998391718607554)
link_6.Initialize(body_29,body_28,False,cA,cB,dA,dB)
link_6.SetName("Concentric6")
exported_items.append(link_6)


# Mate constraint: Concentric11 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_27 , SW name: Spibot-LEG-1/Actuator_rod-2 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_26 , SW name: Spibot-LEG-1/Actuator_body-2 ,  SW ref.type:2 (2)

link_7 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.103348169015006,0.220082306474116,-0.200147488929498)
dA = chrono.ChVectorD(-9.07274255723678e-13,-0.162544746237002,0.986701173340109)
cB = chrono.ChVectorD(-0.103348169014979,0.224877132745606,-0.229253693944231)
dB = chrono.ChVectorD(-9.07052211118753e-13,-0.162544746237002,0.986701173340109)
link_7.Initialize(body_27,body_26,False,cA,cB,dA,dB)
link_7.SetName("Concentric11")
exported_items.append(link_7)

link_8 = chrono.ChLinkMateGeneric()
link_8.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.103348169015006,0.220082306474116,-0.200147488929498)
cB = chrono.ChVectorD(-0.103348169014979,0.224877132745606,-0.229253693944231)
dA = chrono.ChVectorD(-9.07274255723678e-13,-0.162544746237002,0.986701173340109)
dB = chrono.ChVectorD(-9.07052211118753e-13,-0.162544746237002,0.986701173340109)
link_8.Initialize(body_27,body_26,False,cA,cB,dA,dB)
link_8.SetName("Concentric11")
exported_items.append(link_8)


# Mate constraint: Concentric12 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_31 , SW name: Spibot-LEG-1/upper_limb-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_25 , SW name: Spibot-LEG-1/limb_body_connector-1 ,  SW ref.type:2 (2)

link_9 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.105898169014996,0.255907285496518,-0.210273012920609)
dA = chrono.ChVectorD(1,4.66293670342566e-15,9.19986309355636e-13)
cB = chrono.ChVectorD(-0.113348169014996,0.255907285496518,-0.210273012920615)
dB = chrono.ChVectorD(1,5.13478148889135e-15,9.20485909716717e-13)
link_9.Initialize(body_31,body_25,False,cA,cB,dA,dB)
link_9.SetName("Concentric12")
exported_items.append(link_9)

link_10 = chrono.ChLinkMateGeneric()
link_10.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.105898169014996,0.255907285496518,-0.210273012920609)
cB = chrono.ChVectorD(-0.113348169014996,0.255907285496518,-0.210273012920615)
dA = chrono.ChVectorD(1,4.66293670342566e-15,9.19986309355636e-13)
dB = chrono.ChVectorD(1,5.13478148889135e-15,9.20485909716717e-13)
link_10.Initialize(body_31,body_25,False,cA,cB,dA,dB)
link_10.SetName("Concentric12")
exported_items.append(link_10)


# Mate constraint: Concentric13 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_26 , SW name: Spibot-LEG-1/Actuator_body-2 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_32 , SW name: Spibot-LEG-1/limb_body_connector-2 ,  SW ref.type:2 (2)

link_11 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.110948169015033,0.215124447971386,-0.170051623543831)
dA = chrono.ChVectorD(1,4.82947015711943e-15,9.19930798204405e-13)
cB = chrono.ChVectorD(-0.113348169015033,0.215124447971386,-0.170051623543833)
dB = chrono.ChVectorD(1,5.19029264012261e-15,9.20652443170411e-13)
link_11.Initialize(body_26,body_32,False,cA,cB,dA,dB)
link_11.SetName("Concentric13")
exported_items.append(link_11)

link_12 = chrono.ChLinkMateGeneric()
link_12.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.110948169015033,0.215124447971386,-0.170051623543831)
cB = chrono.ChVectorD(-0.113348169015033,0.215124447971386,-0.170051623543833)
dA = chrono.ChVectorD(1,4.82947015711943e-15,9.19930798204405e-13)
dB = chrono.ChVectorD(1,5.19029264012261e-15,9.20652443170411e-13)
link_12.Initialize(body_26,body_32,False,cA,cB,dA,dB)
link_12.SetName("Concentric13")
exported_items.append(link_12)


# Mate constraint: Concentric17 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_25 , SW name: Spibot-LEG-1/limb_body_connector-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_32 , SW name: Spibot-LEG-1/limb_body_connector-2 ,  SW ref.type:2 (2)

link_13 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.103348169015051,0.246232274423842,-0.150219751887224)
dA = chrono.ChVectorD(-3.05311331771918e-16,0.999985343981005,-0.00541403945223881)
cB = chrono.ChVectorD(-0.103348169015051,0.205232875320621,-0.149997776269682)
dB = chrono.ChVectorD(-3.33066907387547e-16,0.999985343981005,-0.00541403945224)
link_13.Initialize(body_25,body_32,False,cA,cB,dA,dB)
link_13.SetName("Concentric17")
exported_items.append(link_13)

link_14 = chrono.ChLinkMateGeneric()
link_14.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.103348169015051,0.246232274423842,-0.150219751887224)
cB = chrono.ChVectorD(-0.103348169015051,0.205232875320621,-0.149997776269682)
dA = chrono.ChVectorD(-3.05311331771918e-16,0.999985343981005,-0.00541403945223881)
dB = chrono.ChVectorD(-3.33066907387547e-16,0.999985343981005,-0.00541403945224)
link_14.Initialize(body_25,body_32,False,cA,cB,dA,dB)
link_14.SetName("Concentric17")
exported_items.append(link_14)


# Mate constraint: Parallel14 [MateParallel] type:3 align:0 flip:False
#   Entity 0: C::E name: body_31 , SW name: Spibot-LEG-1/upper_limb-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_29 , SW name: Spibot-LEG-1/Actuator_rod-1 ,  SW ref.type:2 (2)

link_15 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.105898169014904,0.25536588140155,-0.310271547317899)
dA = chrono.ChVectorD(-1,-4.66293670342566e-15,-9.19986309355636e-13)
cB = chrono.ChVectorD(-0.105898169014812,0.214825896704608,-0.410607100162012)
dB = chrono.ChVectorD(-1,-4.8017145815038e-15,-9.19875287053173e-13)
link_15.Initialize(body_31,body_29,False,cA,cB,dA,dB)
link_15.SetName("Parallel14")
exported_items.append(link_15)


# Mate constraint: Parallel15 [MateParallel] type:3 align:0 flip:False
#   Entity 0: C::E name: body_31 , SW name: Spibot-LEG-1/upper_limb-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_27 , SW name: Spibot-LEG-1/Actuator_rod-2 ,  SW ref.type:2 (2)

link_16 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.10099816901494,0.206909582413454,-0.271194289269395)
dA = chrono.ChVectorD(-1,-4.66293670342566e-15,-9.19986309355636e-13)
cB = chrono.ChVectorD(-0.105748169014956,0.229022267517151,-0.254416053463206)
dB = chrono.ChVectorD(-1,-4.8017145815038e-15,-9.20208353960561e-13)
link_16.Initialize(body_31,body_27,False,cA,cB,dA,dB)
link_16.SetName("Parallel15")
exported_items.append(link_16)


# Mate constraint: Distance10 [MateDistanceDim] type:5 align:1 flip:False
#   Entity 0: C::E name: body_31 , SW name: Spibot-LEG-1/upper_limb-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_30 , SW name: Spibot-LEG-1/lower_limb-1 ,  SW ref.type:2 (2)

link_17 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(-0.105898169014904,0.25536588140155,-0.310271547317899)
cB = chrono.ChVectorD(-0.105948169014805,0.264829346469915,-0.420265210497368)
dA = chrono.ChVectorD(-1,-4.66293670342566e-15,-9.19986309355636e-13)
dB = chrono.ChVectorD(1,4.82947015711943e-15,9.19986309355636e-13)
link_17.Initialize(body_31,body_30,False,cA,cB,dB)
link_17.SetDistance(0)
link_17.SetName("Distance10")
exported_items.append(link_17)

link_18 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.105898169014904,0.25536588140155,-0.310271547317899)
dA = chrono.ChVectorD(-1,-4.66293670342566e-15,-9.19986309355636e-13)
cB = chrono.ChVectorD(-0.105948169014805,0.264829346469915,-0.420265210497368)
dB = chrono.ChVectorD(1,4.82947015711943e-15,9.19986309355636e-13)
link_18.SetFlipped(True)
link_18.Initialize(body_31,body_30,False,cA,cB,dA,dB)
link_18.SetName("Distance10")
exported_items.append(link_18)


# Mate constraint: Distance11 [MateDistanceDim] type:5 align:1 flip:False
#   Entity 0: C::E name: body_29 , SW name: Spibot-LEG-1/Actuator_rod-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_30 , SW name: Spibot-LEG-1/lower_limb-1 ,  SW ref.type:2 (2)

link_19 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(-0.105898169014812,0.214825896704608,-0.410607100162012)
cB = chrono.ChVectorD(-0.105948169014805,0.264829346469915,-0.420265210497368)
dA = chrono.ChVectorD(-1,-4.8017145815038e-15,-9.19875287053173e-13)
dB = chrono.ChVectorD(1,4.82947015711943e-15,9.19986309355636e-13)
link_19.Initialize(body_29,body_30,False,cA,cB,dB)
link_19.SetDistance(0)
link_19.SetName("Distance11")
exported_items.append(link_19)

link_20 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.105898169014812,0.214825896704608,-0.410607100162012)
dA = chrono.ChVectorD(-1,-4.8017145815038e-15,-9.19875287053173e-13)
cB = chrono.ChVectorD(-0.105948169014805,0.264829346469915,-0.420265210497368)
dB = chrono.ChVectorD(1,4.82947015711943e-15,9.19986309355636e-13)
link_20.SetFlipped(True)
link_20.Initialize(body_29,body_30,False,cA,cB,dA,dB)
link_20.SetName("Distance11")
exported_items.append(link_20)


# Mate constraint: Distance12 [MateDistanceDim] type:5 align:1 flip:True
#   Entity 0: C::E name: body_31 , SW name: Spibot-LEG-1/upper_limb-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_25 , SW name: Spibot-LEG-1/limb_body_connector-1 ,  SW ref.type:2 (2)

link_21 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(-0.105898169014904,0.25536588140155,-0.310271547317899)
cB = chrono.ChVectorD(-0.105848169014987,0.245853291662185,-0.220218725965896)
dA = chrono.ChVectorD(-1,-4.66293670342566e-15,-9.19986309355636e-13)
dB = chrono.ChVectorD(1,5.16253706450698e-15,9.2015284280933e-13)
link_21.Initialize(body_31,body_25,False,cA,cB,dB)
link_21.SetDistance(0)
link_21.SetName("Distance12")
exported_items.append(link_21)

link_22 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.105898169014904,0.25536588140155,-0.310271547317899)
dA = chrono.ChVectorD(-1,-4.66293670342566e-15,-9.19986309355636e-13)
cB = chrono.ChVectorD(-0.105848169014987,0.245853291662185,-0.220218725965896)
dB = chrono.ChVectorD(1,5.16253706450698e-15,9.2015284280933e-13)
link_22.SetFlipped(True)
link_22.Initialize(body_31,body_25,False,cA,cB,dA,dB)
link_22.SetName("Distance12")
exported_items.append(link_22)


# Mate constraint: Distance13 [MateDistanceDim] type:5 align:1 flip:True
#   Entity 0: C::E name: body_26 , SW name: Spibot-LEG-1/Actuator_body-2 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_31 , SW name: Spibot-LEG-1/upper_limb-1 ,  SW ref.type:2 (2)

link_23 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(-0.100948169015033,0.215124447971386,-0.170051623543822)
cB = chrono.ChVectorD(-0.10099816901494,0.206909582413454,-0.271194289269395)
dA = chrono.ChVectorD(1,4.82947015711943e-15,9.19930798204405e-13)
dB = chrono.ChVectorD(-1,-4.66293670342566e-15,-9.19986309355636e-13)
link_23.Initialize(body_26,body_31,False,cA,cB,dB)
link_23.SetDistance(0)
link_23.SetName("Distance13")
exported_items.append(link_23)

link_24 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.100948169015033,0.215124447971386,-0.170051623543822)
dA = chrono.ChVectorD(1,4.82947015711943e-15,9.19930798204405e-13)
cB = chrono.ChVectorD(-0.10099816901494,0.206909582413454,-0.271194289269395)
dB = chrono.ChVectorD(-1,-4.66293670342566e-15,-9.19986309355636e-13)
link_24.SetFlipped(True)
link_24.Initialize(body_26,body_31,False,cA,cB,dA,dB)
link_24.SetName("Distance13")
exported_items.append(link_24)


# Mate constraint: Distance14 [MateDistanceDim] type:5 align:1 flip:False
#   Entity 0: C::E name: body_32 , SW name: Spibot-LEG-1/limb_body_connector-2 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_25 , SW name: Spibot-LEG-1/limb_body_connector-1 ,  SW ref.type:2 (2)

link_25 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(-0.113348169015051,0.225232582200241,-0.150106057058736)
cB = chrono.ChVectorD(-0.113348169015051,0.246232274423842,-0.150219751887233)
dA = chrono.ChVectorD(-3.33066907387547e-16,0.999985343981005,-0.00541403945224)
dB = chrono.ChVectorD(3.05311331771918e-16,-0.999985343981005,0.00541403945223881)
link_25.Initialize(body_32,body_25,False,cA,cB,dB)
link_25.SetDistance(0)
link_25.SetName("Distance14")
exported_items.append(link_25)

link_26 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.113348169015051,0.225232582200241,-0.150106057058736)
dA = chrono.ChVectorD(-3.33066907387547e-16,0.999985343981005,-0.00541403945224)
cB = chrono.ChVectorD(-0.113348169015051,0.246232274423842,-0.150219751887233)
dB = chrono.ChVectorD(3.05311331771918e-16,-0.999985343981005,0.00541403945223881)
link_26.SetFlipped(True)
link_26.Initialize(body_32,body_25,False,cA,cB,dA,dB)
link_26.SetName("Distance14")
exported_items.append(link_26)


# Mate constraint: Concentric21 [MateConcentric] type:1 align:1 flip:False
#   Entity 0: C::E name: body_31 , SW name: Spibot-LEG-1/upper_limb-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_28 , SW name: Spibot-LEG-1/Actuator_body-1 ,  SW ref.type:2 (2)

link_27 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.0984981690149396,0.206909582413454,-0.271194289269393)
dA = chrono.ChVectorD(-1,-4.66293670342566e-15,-9.19986309355636e-13)
cB = chrono.ChVectorD(-0.11109816901494,0.206909582153652,-0.271194289467622)
dB = chrono.ChVectorD(1,4.74620343027254e-15,9.19875287053173e-13)
link_27.SetFlipped(True)
link_27.Initialize(body_31,body_28,False,cA,cB,dA,dB)
link_27.SetName("Concentric21")
exported_items.append(link_27)

link_28 = chrono.ChLinkMateGeneric()
link_28.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.0984981690149396,0.206909582413454,-0.271194289269393)
cB = chrono.ChVectorD(-0.11109816901494,0.206909582153652,-0.271194289467622)
dA = chrono.ChVectorD(-1,-4.66293670342566e-15,-9.19986309355636e-13)
dB = chrono.ChVectorD(1,4.74620343027254e-15,9.19875287053173e-13)
link_28.Initialize(body_31,body_28,False,cA,cB,dA,dB)
link_28.SetName("Concentric21")
exported_items.append(link_28)


# Mate constraint: Concentric22 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_31 , SW name: Spibot-LEG-1/upper_limb-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_27 , SW name: Spibot-LEG-1/Actuator_rod-2 ,  SW ref.type:2 (2)

link_29 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.0984981690149551,0.22902226751715,-0.2544160534632)
dA = chrono.ChVectorD(-1,-4.66293670342566e-15,-9.19986309355636e-13)
cB = chrono.ChVectorD(-0.0957481690149558,0.229022267517151,-0.254416053463197)
dB = chrono.ChVectorD(-1,-4.8017145815038e-15,-9.20208353960561e-13)
link_29.Initialize(body_31,body_27,False,cA,cB,dA,dB)
link_29.SetName("Concentric22")
exported_items.append(link_29)

link_30 = chrono.ChLinkMateGeneric()
link_30.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.0984981690149551,0.22902226751715,-0.2544160534632)
cB = chrono.ChVectorD(-0.0957481690149558,0.229022267517151,-0.254416053463197)
dA = chrono.ChVectorD(-1,-4.66293670342566e-15,-9.19986309355636e-13)
dB = chrono.ChVectorD(-1,-4.8017145815038e-15,-9.20208353960561e-13)
link_30.Initialize(body_31,body_27,False,cA,cB,dA,dB)
link_30.SetName("Concentric22")
exported_items.append(link_30)


# Mate constraint: Concentric3 [MateConcentric] type:1 align:1 flip:False
#   Entity 0: C::E name: body_34 , SW name: Spibot-LEG-6/upper_limb-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_35 , SW name: Spibot-LEG-6/lower_limb-1 ,  SW ref.type:2 (2)

link_1 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.100798169190248,0.258072901329505,0.189721124763729)
dA = chrono.ChVectorD(-1,-5.21804821573824e-15,-9.24760268361524e-13)
cB = chrono.ChVectorD(-0.113248169013917,0.258072901277418,0.189721124671535)
dB = chrono.ChVectorD(1,3.3584246494911e-15,9.19320175540861e-13)
link_1.SetFlipped(True)
link_1.Initialize(body_34,body_35,False,cA,cB,dA,dB)
link_1.SetName("Concentric3")
exported_items.append(link_1)

link_2 = chrono.ChLinkMateGeneric()
link_2.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.100798169190248,0.258072901329505,0.189721124763729)
cB = chrono.ChVectorD(-0.113248169013917,0.258072901277418,0.189721124671535)
dA = chrono.ChVectorD(-1,-5.21804821573824e-15,-9.24760268361524e-13)
dB = chrono.ChVectorD(1,3.3584246494911e-15,9.19320175540861e-13)
link_2.Initialize(body_34,body_35,False,cA,cB,dA,dB)
link_2.SetName("Concentric3")
exported_items.append(link_2)


# Mate constraint: Concentric4 [MateConcentric] type:1 align:1 flip:False
#   Entity 0: C::E name: body_35 , SW name: Spibot-LEG-6/lower_limb-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_36 , SW name: Spibot-LEG-6/Actuator_rod-1 ,  SW ref.type:2 (2)

link_3 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.113248169013917,0.218074011806168,0.190019186857552)
dA = chrono.ChVectorD(1,3.3584246494911e-15,9.19320175540861e-13)
cB = chrono.ChVectorD(-0.1007981690152,0.21807401211211,0.190019189114147)
dB = chrono.ChVectorD(-1,-3.52495810318487e-15,-9.19875287053173e-13)
link_3.SetFlipped(True)
link_3.Initialize(body_35,body_36,False,cA,cB,dA,dB)
link_3.SetName("Concentric4")
exported_items.append(link_3)

link_4 = chrono.ChLinkMateGeneric()
link_4.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.113248169013917,0.218074011806168,0.190019186857552)
cB = chrono.ChVectorD(-0.1007981690152,0.21807401211211,0.190019189114147)
dA = chrono.ChVectorD(1,3.3584246494911e-15,9.19320175540861e-13)
dB = chrono.ChVectorD(-1,-3.52495810318487e-15,-9.19875287053173e-13)
link_4.Initialize(body_35,body_36,False,cA,cB,dA,dB)
link_4.SetName("Concentric4")
exported_items.append(link_4)


# Mate constraint: Concentric6 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_36 , SW name: Spibot-LEG-6/Actuator_rod-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_37 , SW name: Spibot-LEG-6/Actuator_body-1 ,  SW ref.type:2 (2)

link_5 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.103198169015113,0.211644177821122,0.0952370324020798)
dA = chrono.ChVectorD(9.17932396760079e-13,-0.0676824662209207,-0.997706912758579)
cB = chrono.ChVectorD(-0.103198169015146,0.214069510956644,0.130988856621287)
dB = chrono.ChVectorD(9.18376485969929e-13,-0.0676824662209207,-0.997706912758579)
link_5.Initialize(body_36,body_37,False,cA,cB,dA,dB)
link_5.SetName("Concentric6")
exported_items.append(link_5)

link_6 = chrono.ChLinkMateGeneric()
link_6.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.103198169015113,0.211644177821122,0.0952370324020798)
cB = chrono.ChVectorD(-0.103198169015146,0.214069510956644,0.130988856621287)
dA = chrono.ChVectorD(9.17932396760079e-13,-0.0676824662209207,-0.997706912758579)
dB = chrono.ChVectorD(9.18376485969929e-13,-0.0676824662209207,-0.997706912758579)
link_6.Initialize(body_36,body_37,False,cA,cB,dA,dB)
link_6.SetName("Concentric6")
exported_items.append(link_6)


# Mate constraint: Concentric11 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_38 , SW name: Spibot-LEG-6/Actuator_rod-2 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_39 , SW name: Spibot-LEG-6/Actuator_body-2 ,  SW ref.type:2 (2)

link_7 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.103348169190055,0.221057576271075,-0.0200129643680639)
dA = chrono.ChVectorD(9.11881681275872e-13,-0.173219139521214,-0.984883307658085)
cB = chrono.ChVectorD(-0.103348169190081,0.226167281129018,0.00903961628530853)
dB = chrono.ChVectorD(9.11881681275872e-13,-0.173219139521214,-0.984883307658085)
link_7.Initialize(body_38,body_39,False,cA,cB,dA,dB)
link_7.SetName("Concentric11")
exported_items.append(link_7)

link_8 = chrono.ChLinkMateGeneric()
link_8.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.103348169190055,0.221057576271075,-0.0200129643680639)
cB = chrono.ChVectorD(-0.103348169190081,0.226167281129018,0.00903961628530853)
dA = chrono.ChVectorD(9.11881681275872e-13,-0.173219139521214,-0.984883307658085)
dB = chrono.ChVectorD(9.11881681275872e-13,-0.173219139521214,-0.984883307658085)
link_8.Initialize(body_38,body_39,False,cA,cB,dA,dB)
link_8.SetName("Concentric11")
exported_items.append(link_8)


# Mate constraint: Concentric12 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_34 , SW name: Spibot-LEG-6/upper_limb-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_40 , SW name: Spibot-LEG-6/limb_body_connector-1 ,  SW ref.type:2 (2)

link_9 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.100798169190063,0.256990093439057,-0.0102759440324723)
dA = chrono.ChVectorD(-1,-5.21804821573824e-15,-9.24760268361524e-13)
cB = chrono.ChVectorD(-0.0933481690150165,0.256990093386966,-0.0102759441243961)
dB = chrono.ChVectorD(-1,-4.8017145815038e-15,-9.20541420867949e-13)
link_9.Initialize(body_34,body_40,False,cA,cB,dA,dB)
link_9.SetName("Concentric12")
exported_items.append(link_9)

link_10 = chrono.ChLinkMateGeneric()
link_10.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.100798169190063,0.256990093439057,-0.0102759440324723)
cB = chrono.ChVectorD(-0.0933481690150165,0.256990093386966,-0.0102759441243961)
dA = chrono.ChVectorD(-1,-5.21804821573824e-15,-9.24760268361524e-13)
dB = chrono.ChVectorD(-1,-4.8017145815038e-15,-9.20541420867949e-13)
link_10.Initialize(body_34,body_40,False,cA,cB,dA,dB)
link_10.SetName("Concentric12")
exported_items.append(link_10)


# Mate constraint: Concentric13 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_39 , SW name: Spibot-LEG-6/Actuator_body-2 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_41 , SW name: Spibot-LEG-6/limb_body_connector-2 ,  SW ref.type:2 (2)

link_11 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.0957481691900267,0.215774132757745,-0.0500533821741695)
dA = chrono.ChVectorD(-1,-5.35682609381638e-15,-9.24815779512755e-13)
cB = chrono.ChVectorD(-0.0933481690149797,0.215774132705655,-0.0500533822660945)
dB = chrono.ChVectorD(-1,-4.82947015711943e-15,-9.20763465472874e-13)
link_11.Initialize(body_39,body_41,False,cA,cB,dA,dB)
link_11.SetName("Concentric13")
exported_items.append(link_11)

link_12 = chrono.ChLinkMateGeneric()
link_12.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.0957481691900267,0.215774132757745,-0.0500533821741695)
cB = chrono.ChVectorD(-0.0933481690149797,0.215774132705655,-0.0500533822660945)
dA = chrono.ChVectorD(-1,-5.35682609381638e-15,-9.24815779512755e-13)
dB = chrono.ChVectorD(-1,-4.82947015711943e-15,-9.20763465472874e-13)
link_12.Initialize(body_39,body_41,False,cA,cB,dA,dB)
link_12.SetName("Concentric13")
exported_items.append(link_12)


# Mate constraint: Concentric17 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_40 , SW name: Spibot-LEG-6/limb_body_connector-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_41 , SW name: Spibot-LEG-6/limb_body_connector-2 ,  SW ref.type:2 (2)

link_13 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.103348169014961,0.246665397580021,-0.0702209243687432)
dA = chrono.ChVectorD(2.4980018054066e-16,0.999985343981005,-0.00541403945223873)
cB = chrono.ChVectorD(-0.103348169014961,0.2056659984768,-0.0699989487512014)
dB = chrono.ChVectorD(2.77555756156289e-16,0.999985343981005,-0.00541403945223753)
link_13.Initialize(body_40,body_41,False,cA,cB,dA,dB)
link_13.SetName("Concentric17")
exported_items.append(link_13)

link_14 = chrono.ChLinkMateGeneric()
link_14.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.103348169014961,0.246665397580021,-0.0702209243687432)
cB = chrono.ChVectorD(-0.103348169014961,0.2056659984768,-0.0699989487512014)
dA = chrono.ChVectorD(2.4980018054066e-16,0.999985343981005,-0.00541403945223873)
dB = chrono.ChVectorD(2.77555756156289e-16,0.999985343981005,-0.00541403945223753)
link_14.Initialize(body_40,body_41,False,cA,cB,dA,dB)
link_14.SetName("Concentric17")
exported_items.append(link_14)


# Mate constraint: Parallel14 [MateParallel] type:3 align:0 flip:False
#   Entity 0: C::E name: body_34 , SW name: Spibot-LEG-6/upper_limb-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_36 , SW name: Spibot-LEG-6/Actuator_rod-1 ,  SW ref.type:2 (2)

link_15 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.100798169190155,0.257531497384281,0.0897225903656284)
dA = chrono.ChVectorD(1,5.21804821573824e-15,9.24760268361524e-13)
cB = chrono.ChVectorD(-0.1007981690152,0.21807401211211,0.190019189114147)
dB = chrono.ChVectorD(1,3.52495810318487e-15,9.19875287053173e-13)
link_15.Initialize(body_34,body_36,False,cA,cB,dA,dB)
link_15.SetName("Parallel14")
exported_items.append(link_15)


# Mate constraint: Parallel15 [MateParallel] type:3 align:0 flip:False
#   Entity 0: C::E name: body_34 , SW name: Spibot-LEG-6/upper_limb-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_38 , SW name: Spibot-LEG-6/Actuator_rod-2 ,  SW ref.type:2 (2)

link_16 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.105698169190119,0.208654913591299,0.0511723041806879)
dA = chrono.ChVectorD(1,5.21804821573824e-15,9.24760268361524e-13)
cB = chrono.ChVectorD(-0.100948169190105,0.230584628944741,0.034155617553133)
dB = chrono.ChVectorD(1,5.24580379135386e-15,9.24649246059062e-13)
link_16.Initialize(body_34,body_38,False,cA,cB,dA,dB)
link_16.SetName("Parallel15")
exported_items.append(link_16)


# Mate constraint: Distance10 [MateDistanceDim] type:5 align:1 flip:False
#   Entity 0: C::E name: body_34 , SW name: Spibot-LEG-6/upper_limb-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_35 , SW name: Spibot-LEG-6/lower_limb-1 ,  SW ref.type:2 (2)

link_17 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(-0.100798169190155,0.257531497384281,0.0897225903656284)
cB = chrono.ChVectorD(-0.100748169013927,0.268068030085411,0.199725993491858)
dA = chrono.ChVectorD(1,5.21804821573824e-15,9.24760268361524e-13)
dB = chrono.ChVectorD(-1,-3.58046925441613e-15,-9.19320175540861e-13)
link_17.Initialize(body_34,body_35,False,cA,cB,dB)
link_17.SetDistance(0)
link_17.SetName("Distance10")
exported_items.append(link_17)

link_18 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.100798169190155,0.257531497384281,0.0897225903656284)
dA = chrono.ChVectorD(1,5.21804821573824e-15,9.24760268361524e-13)
cB = chrono.ChVectorD(-0.100748169013927,0.268068030085411,0.199725993491858)
dB = chrono.ChVectorD(-1,-3.58046925441613e-15,-9.19320175540861e-13)
link_18.SetFlipped(True)
link_18.Initialize(body_34,body_35,False,cA,cB,dA,dB)
link_18.SetName("Distance10")
exported_items.append(link_18)


# Mate constraint: Distance11 [MateDistanceDim] type:5 align:1 flip:False
#   Entity 0: C::E name: body_36 , SW name: Spibot-LEG-6/Actuator_rod-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_35 , SW name: Spibot-LEG-6/lower_limb-1 ,  SW ref.type:2 (2)

link_19 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(-0.1007981690152,0.21807401211211,0.190019189114147)
cB = chrono.ChVectorD(-0.100748169013927,0.268068030085411,0.199725993491858)
dA = chrono.ChVectorD(1,3.52495810318487e-15,9.19875287053173e-13)
dB = chrono.ChVectorD(-1,-3.58046925441613e-15,-9.19320175540861e-13)
link_19.Initialize(body_36,body_35,False,cA,cB,dB)
link_19.SetDistance(0)
link_19.SetName("Distance11")
exported_items.append(link_19)

link_20 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.1007981690152,0.21807401211211,0.190019189114147)
dA = chrono.ChVectorD(1,3.52495810318487e-15,9.19875287053173e-13)
cB = chrono.ChVectorD(-0.100748169013927,0.268068030085411,0.199725993491858)
dB = chrono.ChVectorD(-1,-3.58046925441613e-15,-9.19320175540861e-13)
link_20.SetFlipped(True)
link_20.Initialize(body_36,body_35,False,cA,cB,dA,dB)
link_20.SetName("Distance11")
exported_items.append(link_20)


# Mate constraint: Distance12 [MateDistanceDim] type:5 align:1 flip:True
#   Entity 0: C::E name: body_34 , SW name: Spibot-LEG-6/upper_limb-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_40 , SW name: Spibot-LEG-6/limb_body_connector-1 ,  SW ref.type:2 (2)

link_21 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(-0.100798169190155,0.257531497384281,0.0897225903656284)
cB = chrono.ChVectorD(-0.100848169015026,0.247044380341678,-0.000221950290070549)
dA = chrono.ChVectorD(1,5.21804821573824e-15,9.24760268361524e-13)
dB = chrono.ChVectorD(-1,-4.8017145815038e-15,-9.20319376263024e-13)
link_21.Initialize(body_34,body_40,False,cA,cB,dB)
link_21.SetDistance(0)
link_21.SetName("Distance12")
exported_items.append(link_21)

link_22 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.100798169190155,0.257531497384281,0.0897225903656284)
dA = chrono.ChVectorD(1,5.21804821573824e-15,9.24760268361524e-13)
cB = chrono.ChVectorD(-0.100848169015026,0.247044380341678,-0.000221950290070549)
dB = chrono.ChVectorD(-1,-4.8017145815038e-15,-9.20319376263024e-13)
link_22.SetFlipped(True)
link_22.Initialize(body_34,body_40,False,cA,cB,dA,dB)
link_22.SetName("Distance12")
exported_items.append(link_22)


# Mate constraint: Distance13 [MateDistanceDim] type:5 align:1 flip:True
#   Entity 0: C::E name: body_39 , SW name: Spibot-LEG-6/Actuator_body-2 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_34 , SW name: Spibot-LEG-6/upper_limb-1 ,  SW ref.type:2 (2)

link_23 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(-0.105748169190027,0.215774132757745,-0.0500533821741787)
cB = chrono.ChVectorD(-0.105698169190119,0.208654913591299,0.0511723041806879)
dA = chrono.ChVectorD(-1,-5.35682609381638e-15,-9.24815779512755e-13)
dB = chrono.ChVectorD(1,5.21804821573824e-15,9.24760268361524e-13)
link_23.Initialize(body_39,body_34,False,cA,cB,dB)
link_23.SetDistance(0)
link_23.SetName("Distance13")
exported_items.append(link_23)

link_24 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.105748169190027,0.215774132757745,-0.0500533821741787)
dA = chrono.ChVectorD(-1,-5.35682609381638e-15,-9.24815779512755e-13)
cB = chrono.ChVectorD(-0.105698169190119,0.208654913591299,0.0511723041806879)
dB = chrono.ChVectorD(1,5.21804821573824e-15,9.24760268361524e-13)
link_24.SetFlipped(True)
link_24.Initialize(body_39,body_34,False,cA,cB,dA,dB)
link_24.SetName("Distance13")
exported_items.append(link_24)


# Mate constraint: Distance14 [MateDistanceDim] type:5 align:1 flip:False
#   Entity 0: C::E name: body_41 , SW name: Spibot-LEG-6/limb_body_connector-2 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_40 , SW name: Spibot-LEG-6/limb_body_connector-1 ,  SW ref.type:2 (2)

link_25 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(-0.0933481690149612,0.22566570535642,-0.0701072295402369)
cB = chrono.ChVectorD(-0.0933481690149612,0.246665397580021,-0.070220924368734)
dA = chrono.ChVectorD(2.77555756156289e-16,0.999985343981005,-0.00541403945223753)
dB = chrono.ChVectorD(-2.4980018054066e-16,-0.999985343981005,0.00541403945223873)
link_25.Initialize(body_41,body_40,False,cA,cB,dB)
link_25.SetDistance(0)
link_25.SetName("Distance14")
exported_items.append(link_25)

link_26 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.0933481690149612,0.22566570535642,-0.0701072295402369)
dA = chrono.ChVectorD(2.77555756156289e-16,0.999985343981005,-0.00541403945223753)
cB = chrono.ChVectorD(-0.0933481690149612,0.246665397580021,-0.070220924368734)
dB = chrono.ChVectorD(-2.4980018054066e-16,-0.999985343981005,0.00541403945223873)
link_26.SetFlipped(True)
link_26.Initialize(body_41,body_40,False,cA,cB,dA,dB)
link_26.SetName("Distance14")
exported_items.append(link_26)


# Mate constraint: Concentric21 [MateConcentric] type:1 align:1 flip:False
#   Entity 0: C::E name: body_34 , SW name: Spibot-LEG-6/upper_limb-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_37 , SW name: Spibot-LEG-6/Actuator_body-1 ,  SW ref.type:2 (2)

link_27 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.108198169190119,0.208654913591299,0.0511723041806855)
dA = chrono.ChVectorD(1,5.21804821573824e-15,9.24760268361524e-13)
cB = chrono.ChVectorD(-0.0955981690150725,0.208654913658971,0.0511723036006081)
dB = chrono.ChVectorD(-1,-3.85802501057242e-15,-9.20097331658098e-13)
link_27.SetFlipped(True)
link_27.Initialize(body_34,body_37,False,cA,cB,dA,dB)
link_27.SetName("Concentric21")
exported_items.append(link_27)

link_28 = chrono.ChLinkMateGeneric()
link_28.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.108198169190119,0.208654913591299,0.0511723041806855)
cB = chrono.ChVectorD(-0.0955981690150725,0.208654913658971,0.0511723036006081)
dA = chrono.ChVectorD(1,5.21804821573824e-15,9.24760268361524e-13)
dB = chrono.ChVectorD(-1,-3.85802501057242e-15,-9.20097331658098e-13)
link_28.Initialize(body_34,body_37,False,cA,cB,dA,dB)
link_28.SetName("Concentric21")
exported_items.append(link_28)


# Mate constraint: Concentric22 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_34 , SW name: Spibot-LEG-6/upper_limb-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_38 , SW name: Spibot-LEG-6/Actuator_rod-2 ,  SW ref.type:2 (2)

link_29 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.108198169190104,0.230584628944742,0.0341556175531298)
dA = chrono.ChVectorD(1,5.21804821573824e-15,9.24760268361524e-13)
cB = chrono.ChVectorD(-0.110948169190105,0.230584628944741,0.0341556175531238)
dB = chrono.ChVectorD(1,5.24580379135386e-15,9.24649246059062e-13)
link_29.Initialize(body_34,body_38,False,cA,cB,dA,dB)
link_29.SetName("Concentric22")
exported_items.append(link_29)

link_30 = chrono.ChLinkMateGeneric()
link_30.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.108198169190104,0.230584628944742,0.0341556175531298)
cB = chrono.ChVectorD(-0.110948169190105,0.230584628944741,0.0341556175531238)
dA = chrono.ChVectorD(1,5.21804821573824e-15,9.24760268361524e-13)
dB = chrono.ChVectorD(1,5.24580379135386e-15,9.24649246059062e-13)
link_30.Initialize(body_34,body_38,False,cA,cB,dA,dB)
link_30.SetName("Concentric22")
exported_items.append(link_30)


# Mate constraint: Concentric3 [MateConcentric] type:1 align:1 flip:False
#   Entity 0: C::E name: body_42 , SW name: Spibot-LEG-5/upper_limb-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_43 , SW name: Spibot-LEG-5/lower_limb-1 ,  SW ref.type:2 (2)

link_1 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.0107981690152,0.258072901277413,0.189721124671697)
dA = chrono.ChVectorD(-1,-4.32986979603811e-15,-9.19930798204405e-13)
cB = chrono.ChVectorD(-0.0232481691478489,0.258072901275978,0.189721124673339)
dB = chrono.ChVectorD(1,3.49720252756924e-15,9.18209952516236e-13)
link_1.SetFlipped(True)
link_1.Initialize(body_42,body_43,False,cA,cB,dA,dB)
link_1.SetName("Concentric3")
exported_items.append(link_1)

link_2 = chrono.ChLinkMateGeneric()
link_2.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.0107981690152,0.258072901277413,0.189721124671697)
cB = chrono.ChVectorD(-0.0232481691478489,0.258072901275978,0.189721124673339)
dA = chrono.ChVectorD(-1,-4.32986979603811e-15,-9.19930798204405e-13)
dB = chrono.ChVectorD(1,3.49720252756924e-15,9.18209952516236e-13)
link_2.Initialize(body_42,body_43,False,cA,cB,dA,dB)
link_2.SetName("Concentric3")
exported_items.append(link_2)


# Mate constraint: Concentric4 [MateConcentric] type:1 align:1 flip:False
#   Entity 0: C::E name: body_43 , SW name: Spibot-LEG-5/lower_limb-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_44 , SW name: Spibot-LEG-5/Actuator_rod-1 ,  SW ref.type:2 (2)

link_3 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.0232481691478491,0.218074011869024,0.190019195487578)
dA = chrono.ChVectorD(1,3.49720252756924e-15,9.18209952516236e-13)
cB = chrono.ChVectorD(-0.0107981607365973,0.218074011230946,0.190019187512548)
dB = chrono.ChVectorD(-1,-3.46944695195361e-15,-9.19819775901942e-13)
link_3.SetFlipped(True)
link_3.Initialize(body_43,body_44,False,cA,cB,dA,dB)
link_3.SetName("Concentric4")
exported_items.append(link_3)

link_4 = chrono.ChLinkMateGeneric()
link_4.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.0232481691478491,0.218074011869024,0.190019195487578)
cB = chrono.ChVectorD(-0.0107981607365973,0.218074011230946,0.190019187512548)
dA = chrono.ChVectorD(1,3.49720252756924e-15,9.18209952516236e-13)
dB = chrono.ChVectorD(-1,-3.46944695195361e-15,-9.19819775901942e-13)
link_4.Initialize(body_43,body_44,False,cA,cB,dA,dB)
link_4.SetName("Concentric4")
exported_items.append(link_4)


# Mate constraint: Concentric6 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_44 , SW name: Spibot-LEG-5/Actuator_rod-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_45 , SW name: Spibot-LEG-5/Actuator_body-1 ,  SW ref.type:2 (2)

link_5 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.0131981607365101,0.211644177294002,0.0952370307764636)
dA = chrono.ChVectorD(9.17932396760079e-13,-0.0676824624941429,-0.997706913011396)
cB = chrono.ChVectorD(-0.0131981690151459,0.21406951071499,0.130988856411083)
dB = chrono.ChVectorD(9.16988707189148e-13,-0.0676824624941429,-0.997706913011396)
link_5.Initialize(body_44,body_45,False,cA,cB,dA,dB)
link_5.SetName("Concentric6")
exported_items.append(link_5)

link_6 = chrono.ChLinkMateGeneric()
link_6.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.0131981607365101,0.211644177294002,0.0952370307764636)
cB = chrono.ChVectorD(-0.0131981690151459,0.21406951071499,0.130988856411083)
dA = chrono.ChVectorD(9.17932396760079e-13,-0.0676824624941429,-0.997706913011396)
dB = chrono.ChVectorD(9.16988707189148e-13,-0.0676824624941429,-0.997706913011396)
link_6.Initialize(body_44,body_45,False,cA,cB,dA,dB)
link_6.SetName("Concentric6")
exported_items.append(link_6)


# Mate constraint: Concentric11 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_46 , SW name: Spibot-LEG-5/Actuator_rod-2 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_47 , SW name: Spibot-LEG-5/Actuator_body-2 ,  SW ref.type:2 (2)

link_7 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.0133481690150069,0.221057576218984,-0.0200129644600924)
dA = chrono.ChVectorD(9.06663633060134e-13,-0.173219139521214,-0.984883307658085)
cB = chrono.ChVectorD(-0.0133481690150338,0.226167281076927,0.00903961619328006)
dB = chrono.ChVectorD(9.0694118881629e-13,-0.173219139521214,-0.984883307658085)
link_7.Initialize(body_46,body_47,False,cA,cB,dA,dB)
link_7.SetName("Concentric11")
exported_items.append(link_7)

link_8 = chrono.ChLinkMateGeneric()
link_8.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.0133481690150069,0.221057576218984,-0.0200129644600924)
cB = chrono.ChVectorD(-0.0133481690150338,0.226167281076927,0.00903961619328006)
dA = chrono.ChVectorD(9.06663633060134e-13,-0.173219139521214,-0.984883307658085)
dB = chrono.ChVectorD(9.0694118881629e-13,-0.173219139521214,-0.984883307658085)
link_8.Initialize(body_46,body_47,False,cA,cB,dA,dB)
link_8.SetName("Concentric11")
exported_items.append(link_8)


# Mate constraint: Concentric12 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_42 , SW name: Spibot-LEG-5/upper_limb-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_48 , SW name: Spibot-LEG-5/limb_body_connector-1 ,  SW ref.type:2 (2)

link_9 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.0107981690150162,0.256990093386965,-0.0102759441245042)
dA = chrono.ChVectorD(-1,-4.32986979603811e-15,-9.19930798204405e-13)
cB = chrono.ChVectorD(-0.00334816901501644,0.256990093386965,-0.0102759441244975)
dB = chrono.ChVectorD(-1,-3.99680288865056e-15,-9.20041820506867e-13)
link_9.Initialize(body_42,body_48,False,cA,cB,dA,dB)
link_9.SetName("Concentric12")
exported_items.append(link_9)

link_10 = chrono.ChLinkMateGeneric()
link_10.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.0107981690150162,0.256990093386965,-0.0102759441245042)
cB = chrono.ChVectorD(-0.00334816901501644,0.256990093386965,-0.0102759441244975)
dA = chrono.ChVectorD(-1,-4.32986979603811e-15,-9.19930798204405e-13)
dB = chrono.ChVectorD(-1,-3.99680288865056e-15,-9.20041820506867e-13)
link_10.Initialize(body_42,body_48,False,cA,cB,dA,dB)
link_10.SetName("Concentric12")
exported_items.append(link_10)


# Mate constraint: Concentric13 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_47 , SW name: Spibot-LEG-5/Actuator_body-2 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_49 , SW name: Spibot-LEG-5/limb_body_connector-2 ,  SW ref.type:2 (2)

link_11 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.00574816901497943,0.215774132705654,-0.0500533822661981)
dA = chrono.ChVectorD(-1,-4.46864767411626e-15,-9.1970875359948e-13)
cB = chrono.ChVectorD(-0.00334816901497959,0.215774132705654,-0.0500533822661959)
dB = chrono.ChVectorD(-1,-3.99680288865056e-15,-9.20208353960561e-13)
link_11.Initialize(body_47,body_49,False,cA,cB,dA,dB)
link_11.SetName("Concentric13")
exported_items.append(link_11)

link_12 = chrono.ChLinkMateGeneric()
link_12.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.00574816901497943,0.215774132705654,-0.0500533822661981)
cB = chrono.ChVectorD(-0.00334816901497959,0.215774132705654,-0.0500533822661959)
dA = chrono.ChVectorD(-1,-4.46864767411626e-15,-9.1970875359948e-13)
dB = chrono.ChVectorD(-1,-3.99680288865056e-15,-9.20208353960561e-13)
link_12.Initialize(body_47,body_49,False,cA,cB,dA,dB)
link_12.SetName("Concentric13")
exported_items.append(link_12)


# Mate constraint: Concentric17 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_48 , SW name: Spibot-LEG-5/limb_body_connector-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_49 , SW name: Spibot-LEG-5/limb_body_connector-2 ,  SW ref.type:2 (2)

link_13 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.0133481690149612,0.246665397580021,-0.0702209243688446)
dA = chrono.ChVectorD(9.43689570931383e-16,0.999985343981005,-0.00541403945223862)
cB = chrono.ChVectorD(-0.0133481690149612,0.205665998476799,-0.0699989487513028)
dB = chrono.ChVectorD(9.99200722162641e-16,0.999985343981005,-0.00541403945223745)
link_13.Initialize(body_48,body_49,False,cA,cB,dA,dB)
link_13.SetName("Concentric17")
exported_items.append(link_13)

link_14 = chrono.ChLinkMateGeneric()
link_14.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.0133481690149612,0.246665397580021,-0.0702209243688446)
cB = chrono.ChVectorD(-0.0133481690149612,0.205665998476799,-0.0699989487513028)
dA = chrono.ChVectorD(9.43689570931383e-16,0.999985343981005,-0.00541403945223862)
dB = chrono.ChVectorD(9.99200722162641e-16,0.999985343981005,-0.00541403945223745)
link_14.Initialize(body_48,body_49,False,cA,cB,dA,dB)
link_14.SetName("Concentric17")
exported_items.append(link_14)


# Mate constraint: Parallel14 [MateParallel] type:3 align:0 flip:False
#   Entity 0: C::E name: body_42 , SW name: Spibot-LEG-5/upper_limb-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_44 , SW name: Spibot-LEG-5/Actuator_rod-1 ,  SW ref.type:2 (2)

link_15 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.0107981690151081,0.257531497332189,0.0897225902735963)
dA = chrono.ChVectorD(1,4.32986979603811e-15,9.19930798204405e-13)
cB = chrono.ChVectorD(-0.0107981607365973,0.218074011230946,0.190019187512548)
dB = chrono.ChVectorD(1,3.46944695195361e-15,9.19819775901942e-13)
link_15.Initialize(body_42,body_44,False,cA,cB,dA,dB)
link_15.SetName("Parallel14")
exported_items.append(link_15)


# Mate constraint: Parallel15 [MateParallel] type:3 align:0 flip:False
#   Entity 0: C::E name: body_42 , SW name: Spibot-LEG-5/upper_limb-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_46 , SW name: Spibot-LEG-5/Actuator_rod-2 ,  SW ref.type:2 (2)

link_16 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.0156981690150724,0.208654913539207,0.0511723040886558)
dA = chrono.ChVectorD(1,4.32986979603811e-15,9.19930798204405e-13)
cB = chrono.ChVectorD(-0.0109481690150568,0.23058462889265,0.0341556174611044)
dB = chrono.ChVectorD(1,4.46864767411626e-15,9.1970875359948e-13)
link_16.Initialize(body_42,body_46,False,cA,cB,dA,dB)
link_16.SetName("Parallel15")
exported_items.append(link_16)


# Mate constraint: Distance10 [MateDistanceDim] type:5 align:1 flip:False
#   Entity 0: C::E name: body_42 , SW name: Spibot-LEG-5/upper_limb-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_43 , SW name: Spibot-LEG-5/lower_limb-1 ,  SW ref.type:2 (2)

link_17 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(-0.0107981690151081,0.257531497332189,0.0897225902735963)
cB = chrono.ChVectorD(-0.0107481691478583,0.268068032242135,0.199725991337598)
dA = chrono.ChVectorD(1,4.32986979603811e-15,9.19930798204405e-13)
dB = chrono.ChVectorD(-1,-3.66373598126302e-15,-9.18154441365004e-13)
link_17.Initialize(body_42,body_43,False,cA,cB,dB)
link_17.SetDistance(0)
link_17.SetName("Distance10")
exported_items.append(link_17)

link_18 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.0107981690151081,0.257531497332189,0.0897225902735963)
dA = chrono.ChVectorD(1,4.32986979603811e-15,9.19930798204405e-13)
cB = chrono.ChVectorD(-0.0107481691478583,0.268068032242135,0.199725991337598)
dB = chrono.ChVectorD(-1,-3.66373598126302e-15,-9.18154441365004e-13)
link_18.SetFlipped(True)
link_18.Initialize(body_42,body_43,False,cA,cB,dA,dB)
link_18.SetName("Distance10")
exported_items.append(link_18)


# Mate constraint: Distance11 [MateDistanceDim] type:5 align:1 flip:False
#   Entity 0: C::E name: body_44 , SW name: Spibot-LEG-5/Actuator_rod-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_43 , SW name: Spibot-LEG-5/lower_limb-1 ,  SW ref.type:2 (2)

link_19 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(-0.0107981607365973,0.218074011230946,0.190019187512548)
cB = chrono.ChVectorD(-0.0107481691478583,0.268068032242135,0.199725991337598)
dA = chrono.ChVectorD(1,3.46944695195361e-15,9.19819775901942e-13)
dB = chrono.ChVectorD(-1,-3.66373598126302e-15,-9.18154441365004e-13)
link_19.Initialize(body_44,body_43,False,cA,cB,dB)
link_19.SetDistance(0)
link_19.SetName("Distance11")
exported_items.append(link_19)

link_20 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.0107981607365973,0.218074011230946,0.190019187512548)
dA = chrono.ChVectorD(1,3.46944695195361e-15,9.19819775901942e-13)
cB = chrono.ChVectorD(-0.0107481691478583,0.268068032242135,0.199725991337598)
dB = chrono.ChVectorD(-1,-3.66373598126302e-15,-9.18154441365004e-13)
link_20.SetFlipped(True)
link_20.Initialize(body_44,body_43,False,cA,cB,dA,dB)
link_20.SetName("Distance11")
exported_items.append(link_20)


# Mate constraint: Distance12 [MateDistanceDim] type:5 align:1 flip:True
#   Entity 0: C::E name: body_42 , SW name: Spibot-LEG-5/upper_limb-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_48 , SW name: Spibot-LEG-5/limb_body_connector-1 ,  SW ref.type:2 (2)

link_21 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(-0.0107981690151081,0.257531497332189,0.0897225902735963)
cB = chrono.ChVectorD(-0.0108481690150256,0.247044380341677,-0.000221950290171996)
dA = chrono.ChVectorD(1,4.32986979603811e-15,9.19930798204405e-13)
dB = chrono.ChVectorD(-1,-3.99680288865056e-15,-9.19764264750711e-13)
link_21.Initialize(body_42,body_48,False,cA,cB,dB)
link_21.SetDistance(0)
link_21.SetName("Distance12")
exported_items.append(link_21)

link_22 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.0107981690151081,0.257531497332189,0.0897225902735963)
dA = chrono.ChVectorD(1,4.32986979603811e-15,9.19930798204405e-13)
cB = chrono.ChVectorD(-0.0108481690150256,0.247044380341677,-0.000221950290171996)
dB = chrono.ChVectorD(-1,-3.99680288865056e-15,-9.19764264750711e-13)
link_22.SetFlipped(True)
link_22.Initialize(body_42,body_48,False,cA,cB,dA,dB)
link_22.SetName("Distance12")
exported_items.append(link_22)


# Mate constraint: Distance13 [MateDistanceDim] type:5 align:1 flip:True
#   Entity 0: C::E name: body_47 , SW name: Spibot-LEG-5/Actuator_body-2 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_42 , SW name: Spibot-LEG-5/upper_limb-1 ,  SW ref.type:2 (2)

link_23 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(-0.0157481690149793,0.215774132705654,-0.0500533822662073)
cB = chrono.ChVectorD(-0.0156981690150724,0.208654913539207,0.0511723040886558)
dA = chrono.ChVectorD(-1,-4.46864767411626e-15,-9.1970875359948e-13)
dB = chrono.ChVectorD(1,4.32986979603811e-15,9.19930798204405e-13)
link_23.Initialize(body_47,body_42,False,cA,cB,dB)
link_23.SetDistance(0)
link_23.SetName("Distance13")
exported_items.append(link_23)

link_24 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.0157481690149793,0.215774132705654,-0.0500533822662073)
dA = chrono.ChVectorD(-1,-4.46864767411626e-15,-9.1970875359948e-13)
cB = chrono.ChVectorD(-0.0156981690150724,0.208654913539207,0.0511723040886558)
dB = chrono.ChVectorD(1,4.32986979603811e-15,9.19930798204405e-13)
link_24.SetFlipped(True)
link_24.Initialize(body_47,body_42,False,cA,cB,dA,dB)
link_24.SetName("Distance13")
exported_items.append(link_24)


# Mate constraint: Distance14 [MateDistanceDim] type:5 align:1 flip:False
#   Entity 0: C::E name: body_49 , SW name: Spibot-LEG-5/limb_body_connector-2 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_48 , SW name: Spibot-LEG-5/limb_body_connector-1 ,  SW ref.type:2 (2)

link_25 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(-0.00334816901496116,0.22566570535642,-0.0701072295403384)
cB = chrono.ChVectorD(-0.00334816901496116,0.246665397580021,-0.0702209243688353)
dA = chrono.ChVectorD(9.99200722162641e-16,0.999985343981005,-0.00541403945223745)
dB = chrono.ChVectorD(-9.43689570931383e-16,-0.999985343981005,0.00541403945223862)
link_25.Initialize(body_49,body_48,False,cA,cB,dB)
link_25.SetDistance(0)
link_25.SetName("Distance14")
exported_items.append(link_25)

link_26 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.00334816901496116,0.22566570535642,-0.0701072295403384)
dA = chrono.ChVectorD(9.99200722162641e-16,0.999985343981005,-0.00541403945223745)
cB = chrono.ChVectorD(-0.00334816901496116,0.246665397580021,-0.0702209243688353)
dB = chrono.ChVectorD(-9.43689570931383e-16,-0.999985343981005,0.00541403945223862)
link_26.SetFlipped(True)
link_26.Initialize(body_49,body_48,False,cA,cB,dA,dB)
link_26.SetName("Distance14")
exported_items.append(link_26)


# Mate constraint: Concentric21 [MateConcentric] type:1 align:1 flip:False
#   Entity 0: C::E name: body_42 , SW name: Spibot-LEG-5/upper_limb-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_45 , SW name: Spibot-LEG-5/Actuator_body-1 ,  SW ref.type:2 (2)

link_27 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.0181981690150724,0.208654913539207,0.0511723040886534)
dA = chrono.ChVectorD(1,4.32986979603811e-15,9.19930798204405e-13)
cB = chrono.ChVectorD(-0.0055981690150726,0.208654913715458,0.0511723033701778)
dB = chrono.ChVectorD(-1,-3.63598040564739e-15,-9.18876086331011e-13)
link_27.SetFlipped(True)
link_27.Initialize(body_42,body_45,False,cA,cB,dA,dB)
link_27.SetName("Concentric21")
exported_items.append(link_27)

link_28 = chrono.ChLinkMateGeneric()
link_28.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.0181981690150724,0.208654913539207,0.0511723040886534)
cB = chrono.ChVectorD(-0.0055981690150726,0.208654913715458,0.0511723033701778)
dA = chrono.ChVectorD(1,4.32986979603811e-15,9.19930798204405e-13)
dB = chrono.ChVectorD(-1,-3.63598040564739e-15,-9.18876086331011e-13)
link_28.Initialize(body_42,body_45,False,cA,cB,dA,dB)
link_28.SetName("Concentric21")
exported_items.append(link_28)


# Mate constraint: Concentric22 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_42 , SW name: Spibot-LEG-5/upper_limb-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_46 , SW name: Spibot-LEG-5/Actuator_rod-2 ,  SW ref.type:2 (2)

link_29 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.0181981690150569,0.23058462889265,0.0341556174610979)
dA = chrono.ChVectorD(1,4.32986979603811e-15,9.19930798204405e-13)
cB = chrono.ChVectorD(-0.0209481690150569,0.23058462889265,0.0341556174610953)
dB = chrono.ChVectorD(1,4.46864767411626e-15,9.1970875359948e-13)
link_29.Initialize(body_42,body_46,False,cA,cB,dA,dB)
link_29.SetName("Concentric22")
exported_items.append(link_29)

link_30 = chrono.ChLinkMateGeneric()
link_30.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.0181981690150569,0.23058462889265,0.0341556174610979)
cB = chrono.ChVectorD(-0.0209481690150569,0.23058462889265,0.0341556174610953)
dA = chrono.ChVectorD(1,4.32986979603811e-15,9.19930798204405e-13)
dB = chrono.ChVectorD(1,4.46864767411626e-15,9.1970875359948e-13)
link_30.Initialize(body_42,body_46,False,cA,cB,dA,dB)
link_30.SetName("Concentric22")
exported_items.append(link_30)

