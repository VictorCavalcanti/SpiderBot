# Chrono::Engine Python script from SolidWorks 
# Assembly: D:\Documents\ME - Graduate\Research\Projects\Project Chrono\Spibot-actuators\SpiderBot-Simple.SLDASM


import ChronoEngine_PYTHON_core as chrono 
import builtins 

shapes_dir = 'Spider_Simple_shapes/' 

if hasattr(builtins, 'exported_system_relpath'): 
    shapes_dir = builtins.exported_system_relpath + shapes_dir 

exported_items = [] 

body_0= chrono.ChBodyAuxRef()
body_0.SetName('ground')
body_0.SetBodyFixed(True)
exported_items.append(body_0)

# Rigid body part
body_1= chrono.ChBodyAuxRef()
body_1.SetName('body-1')
body_1.SetPos(chrono.ChVectorD(-0.00458541792951962,0.21,-0.099741440782467))
body_1.SetRot(chrono.ChQuaternionD(0.707106781186548,-2.69107324616134e-17,-0.707106781186547,-2.69107324597082e-17))
body_1.SetMass(1.07840956871912)
body_1.SetInertiaXX(chrono.ChVectorD(0.000933401674312344,0.0044888657385094,0.003627358035445))
body_1.SetInertiaXY(chrono.ChVectorD(-7.423711866259e-21,-1.96817286999336e-19,6.63223768432286e-20))
body_1.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(2.56079314774532e-18,0.01,5.05173630965186e-18),chrono.ChQuaternionD(1,0,0,0)))
body_1.SetBodyFixed(True)

# Visualization shape 
body_1_1_shape = chrono.ChObjShapeFile() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_1_1_level = chrono.ChAssetLevel() 
body_1_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_1_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_1_1_level.GetAssets().push_back(body_1_1_shape) 
body_1.GetAssets().push_back(body_1_1_level) 

exported_items.append(body_1)



# Rigid body part
body_2= chrono.ChBodyAuxRef()
body_2.SetName('Spibot-LEG-1/limb_body_connector-1')
body_2.SetPos(chrono.ChVectorD(-0.0845854179295196,0.23095,-0.139741440782467))
body_2.SetRot(chrono.ChQuaternionD(0.5,-0.5,-0.5,0.5))
body_2.SetMass(0.0319301494979552)
body_2.SetInertiaXX(chrono.ChVectorD(2.21101734329624e-06,4.6562762681289e-06,4.83154745183424e-06))
body_2.SetInertiaXY(chrono.ChVectorD(1.38319354916369e-22,2.84567156309358e-22,5.69462935029567e-22))
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
marker_2_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.0945854179295196,0.24095,-0.199741440782467),chrono.ChQuaternionD(0.5,-0.5,-0.5,-0.5)))

# Auxiliary marker (coordinate system feature)
marker_2_2 =chrono.ChMarker()
marker_2_2.SetName('LB-B-Act-1')
body_2.AddMarker(marker_2_2)
marker_2_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.0945854179295196,0.24095,-0.139741440782467),chrono.ChQuaternionD(0.707106781186547,-0.707106781186548,2.94392336003208E-17,1.66822323735151E-16)))

exported_items.append(body_2)



# Rigid body part
body_3= chrono.ChBodyAuxRef()
body_3.SetName('Spibot-LEG-1/limb_body_connector-2')
body_3.SetPos(chrono.ChVectorD(-0.0845854179295196,0.18995,-0.139741440782467))
body_3.SetRot(chrono.ChQuaternionD(0.5,-0.5,-0.5,0.5))
body_3.SetMass(0.0319301494979552)
body_3.SetInertiaXX(chrono.ChVectorD(2.21101734329624e-06,4.6562762681289e-06,4.83154745183424e-06))
body_3.SetInertiaXY(chrono.ChVectorD(3.17944693951835e-21,4.18669536949243e-22,7.89020170383595e-22))
body_3.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(0.01,0.00875766097763167,0.01),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_2_1_shape = chrono.ChObjShapeFile() 
body_2_1_shape.SetFilename(shapes_dir +'body_2_1.obj') 
body_2_1_level = chrono.ChAssetLevel() 
body_2_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_2_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_2_1_level.GetAssets().push_back(body_2_1_shape) 
body_3.GetAssets().push_back(body_2_1_level) 

# Auxiliary marker (coordinate system feature)
marker_3_1 =chrono.ChMarker()
marker_3_1.SetName('LB-UL-Ref')
body_3.AddMarker(marker_3_1)
marker_3_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.0945854179295196,0.19995,-0.159741440782467),chrono.ChQuaternionD(-0.5,0.5,0.5,0.5)))

# Auxiliary marker (coordinate system feature)
marker_3_2 =chrono.ChMarker()
marker_3_2.SetName('LB-B-Act-1')
body_3.AddMarker(marker_3_2)
marker_3_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.0945854179295196,0.19995,-0.139741440782467),chrono.ChQuaternionD(0.707106781186547,-0.707106781186548,-7.85046229341888E-17,8.83177008009624E-17)))

exported_items.append(body_3)



# Rigid body part
body_4= chrono.ChBodyAuxRef()
body_4.SetName('Spibot-LEG-1/Actuator_body-2')
body_4.SetPos(chrono.ChVectorD(-0.094585417929518,0.204766642669051,-0.199450381254339))
body_4.SetRot(chrono.ChQuaternionD(-0.0603178588943548,0.998179220329897,3.4757755734556e-16,-8.48089239923167e-16))
body_4.SetMass(0.00204159144576871)
body_4.SetInertiaXX(chrono.ChVectorD(8.08481090947278e-07,7.91098235373101e-07,9.64104624216311e-08))
body_4.SetInertiaXY(chrono.ChVectorD(-3.84412347570868e-23,-1.43576405177517e-21,-8.55230530863932e-08))
body_4.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-4.17192939730159e-18,5.58956732701871e-20,-0.0175577824053523),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_4_1_shape = chrono.ChObjShapeFile() 
body_4_1_shape.SetFilename(shapes_dir +'body_4_1.obj') 
body_4_1_shape.SetColor(chrono.ChColor(0.843137254901961,0.843137254901961,0)) 
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
marker_4_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.0945854179295179,0.198745839332737,-0.149814205664499),chrono.ChQuaternionD(-0.0603178588943548,0.998179220329897,3.4757755734556E-16,-8.48089239923167E-16)))

# Auxiliary marker (coordinate system feature)
marker_4_2 =chrono.ChMarker()
marker_4_2.SetName('UL-Act-Base')
body_4.AddMarker(marker_4_2)
marker_4_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.094585417929518,0.19995,-0.159741440782467),chrono.ChQuaternionD(-0.0603178588943548,0.998179220329897,3.4757755734556E-16,-8.48089239923167E-16)))

exported_items.append(body_4)



# Rigid body part
body_5= chrono.ChBodyAuxRef()
body_5.SetName('Spibot-LEG-1/Actuator_rod-2')
body_5.SetPos(chrono.ChVectorD(-0.0945854179295178,0.203107166520883,-0.185769474425711))
body_5.SetRot(chrono.ChQuaternionD(-0.0603178588943547,0.998179220329897,1.87691880966603e-16,-1.00102336515521e-15))
body_5.SetMass(0.00140945245841084)
body_5.SetInertiaXX(chrono.ChVectorD(2.33089158373325e-06,2.29356156894321e-06,5.69585030423677e-08))
body_5.SetInertiaXY(chrono.ChVectorD(-4.17686338101602e-22,-4.31767179669572e-21,-2.75348336599542e-07))
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
marker_5_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.0945854179295179,0.209805310232532,-0.240989719769408),chrono.ChQuaternionD(-1.87691880966603E-16,1.00102336515521E-15,-0.0603178588943547,0.998179220329897)))

# Auxiliary marker (coordinate system feature)
marker_5_2 =chrono.ChMarker()
marker_5_2.SetName('LL-Act-Shaft')
body_5.AddMarker(marker_5_2)
marker_5_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.094585417929518,0.214621952901583,-0.28069866024128),chrono.ChQuaternionD(-1.87691880966603E-16,1.00102336515521E-15,-0.0603178588943547,0.998179220329897)))

exported_items.append(body_5)



# Rigid body part
body_6= chrono.ChBodyAuxRef()
body_6.SetName('Spibot-LEG-1/Actuator_rod-1')
body_6.SetPos(chrono.ChVectorD(-0.0947354179295115,0.184057586615268,-0.304124460209043))
body_6.SetRot(chrono.ChQuaternionD(-8.05094616569465e-16,-2.49856949969834e-16,0.999772792275018,-0.0213158116574014))
body_6.SetMass(0.00140945245841084)
body_6.SetInertiaXX(chrono.ChVectorD(2.33089158373325e-06,2.32277653510708e-06,2.77435368784949e-08))
body_6.SetInertiaXY(chrono.ChVectorD(2.53057858261931e-22,3.72668974347668e-21,-9.80862341405306e-08))
body_6.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-1.65060230227876e-19,-2.34447212110501e-18,0.0545976735175364),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_5_1_shape = chrono.ChObjShapeFile() 
body_5_1_shape.SetFilename(shapes_dir +'body_5_1.obj') 
body_5_1_level = chrono.ChAssetLevel() 
body_5_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_5_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_5_1_level.GetAssets().push_back(body_5_1_shape) 
body_6.GetAssets().push_back(body_5_1_level) 

# Auxiliary marker (coordinate system feature)
marker_6_1 =chrono.ChMarker()
marker_6_1.SetName('UL-Act-Shaft')
body_6.AddMarker(marker_6_1)
marker_6_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.0947354179295116,0.181686741365157,-0.359698912233332),chrono.ChQuaternionD(0.999772792275018,-0.0213158116574014,8.05094616569465E-16,2.49856949969834E-16)))

# Auxiliary marker (coordinate system feature)
marker_6_2 =chrono.ChMarker()
marker_6_2.SetName('LL-Act-Shaft')
body_6.AddMarker(marker_6_2)
marker_6_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.0947354179295116,0.17998186388193,-0.399662563127203),chrono.ChQuaternionD(0.999772792275018,-0.0213158116574014,8.05094616569465E-16,2.49856949969834E-16)))

exported_items.append(body_6)



# Rigid body part
body_7= chrono.ChBodyAuxRef()
body_7.SetName('Spibot-LEG-1/Actuator_body-1')
body_7.SetPos(chrono.ChVectorD(-0.0947354179295057,0.184001526377171,-0.305438555683095))
body_7.SetRot(chrono.ChQuaternionD(0.0213158116574013,0.999772792275018,2.01273654142366e-16,-8.46737441564437e-16))
body_7.SetMass(0.00204159144576871)
body_7.SetInertiaXX(chrono.ChVectorD(8.08481090947278e-07,8.00172388981604e-07,8.73363088131279e-08))
body_7.SetInertiaXY(chrono.ChVectorD(2.58062590217614e-23,-1.32021394475151e-21,3.04655343592836e-08))
body_7.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-4.17192939730159e-18,5.58956732701871e-20,-0.0175577824053523),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_4_1_shape = chrono.ChObjShapeFile() 
body_4_1_shape.SetFilename(shapes_dir +'body_4_1.obj') 
body_4_1_shape.SetColor(chrono.ChColor(0.752941176470588,0.752941176470588,0.752941176470588)) 
body_4_1_shape.SetFading(0.75) 
body_4_1_level = chrono.ChAssetLevel() 
body_4_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_4_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_4_1_level.GetAssets().push_back(body_4_1_shape) 
body_7.GetAssets().push_back(body_4_1_level) 

# Auxiliary marker (coordinate system feature)
marker_7_1 =chrono.ChMarker()
marker_7_1.SetName('LL-Act-Base')
body_7.AddMarker(marker_7_1)
marker_7_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.0947354179295056,0.186132623231204,-0.255483992065756),chrono.ChQuaternionD(0.0213158116574013,0.999772792275018,2.01273654142366E-16,-8.46737441564437E-16)))

# Auxiliary marker (coordinate system feature)
marker_7_2 =chrono.ChMarker()
marker_7_2.SetName('UL-Act-Base')
body_7.AddMarker(marker_7_2)
marker_7_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.0947354179295056,0.185706403860397,-0.265474904789224),chrono.ChQuaternionD(0.0213158116574013,0.999772792275018,2.01273654142366E-16,-8.46737441564437E-16)))

exported_items.append(body_7)



# Rigid body part
body_8= chrono.ChBodyAuxRef()
body_8.SetName('Spibot-LEG-1/upper_limb_con-1')
body_8.SetPos(chrono.ChVectorD(-0.0946854179295166,0.23045936829327,-0.299189651658263))
body_8.SetRot(chrono.ChQuaternionD(0.473046954047032,-0.525572620355004,-0.47304695404703,0.525572620355006))
body_8.SetMass(0.0769386604687246)
body_8.SetInertiaXX(chrono.ChVectorD(1.51995576083702e-05,0.000288158589991578,0.000279898353184369))
body_8.SetInertiaXY(chrono.ChVectorD(2.91180286222586e-05,1.19397497028916e-05,-1.25950497953185e-06))
body_8.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-0.00433891891647107,-0.0160004109829567,1.89023205931516e-19),chrono.ChQuaternionD(1,0,0,0)))

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
marker_8_1.SetName('UL-LL-Ref')
body_8.AddMarker(marker_8_1)
marker_8_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.094685417929517,0.21996873658654,-0.398637862534044),chrono.ChQuaternionD(0.706130672885305,-0.0371412548327095,-0.706130672885302,0.0371412548327107)))

# Auxiliary marker (coordinate system feature)
marker_8_2 =chrono.ChMarker()
marker_8_2.SetName('UL-LB-Ref')
body_8.AddMarker(marker_8_2)
marker_8_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.0946854179295162,0.240950000000001,-0.199741440782482),chrono.ChQuaternionD(0.706130672885305,-0.0371412548327095,-0.706130672885302,0.0371412548327107)))

exported_items.append(body_8)



# Rigid body part
body_9= chrono.ChBodyAuxRef()
body_9.SetName('Spibot-LEG-1/lower_limb-1')
body_9.SetPos(chrono.ChVectorD(-0.0946854179295453,0.119984368293296,-0.400405939737063))
body_9.SetRot(chrono.ChQuaternionD(0.999960919969549,0.00884073151117369,4.46157581361844e-16,2.3198709940726e-16))
body_9.SetMass(0.173763895224452)
body_9.SetInertiaXX(chrono.ChVectorD(0.000660134295478084,8.961775238543e-06,0.0006604503796322))
body_9.SetInertiaXY(chrono.ChVectorD(-7.09451431119308e-11,-5.48297891797272e-12,1.15195709973725e-05))
body_9.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(4.14273289964873e-09,-0.0143933772184335,3.59893950746433e-07),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_9_1_shape = chrono.ChObjShapeFile() 
body_9_1_shape.SetFilename(shapes_dir +'body_9_1.obj') 
body_9_1_shape.SetColor(chrono.ChColor(0.898039215686275,0.917647058823529,0.929411764705882)) 
body_9_1_shape.SetFading(0.75) 
body_9_1_level = chrono.ChAssetLevel() 
body_9_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_9_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_9_1_level.GetAssets().push_back(body_9_1_shape) 
body_9.GetAssets().push_back(body_9_1_level) 

# Auxiliary marker (coordinate system feature)
marker_9_1 =chrono.ChMarker()
marker_9_1.SetName('LowerLimbCenterRef')
body_9.AddMarker(marker_9_1)
marker_9_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.0946854179295453,0.119984368293296,-0.400405939737063),chrono.ChQuaternionD(0.707079147432007,0.0062513412022002,0.00625134120220082,-0.707079147432007)))

# Auxiliary marker (coordinate system feature)
marker_9_2 =chrono.ChMarker()
marker_9_2.SetName('LL-UL-Ref')
body_9.AddMarker(marker_9_2)
marker_9_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.0946854179295454,0.219968736586566,-0.39863786253404),chrono.ChQuaternionD(0.707079147432007,0.00625134120220019,0.00625134120220083,-0.707079147432007)))

# Collision shapes 
body_9.GetCollisionModel().ClearModel()
body_9.GetCollisionModel().AddSphere(0.01, chrono.ChVectorD(3.46944695195361E-17,-0.1,0))
body_9.GetCollisionModel().BuildModel()
body_9.SetCollide(True)

exported_items.append(body_9)



# Rigid body part
body_10= chrono.ChBodyAuxRef()
body_10.SetName('Spibot-LEG-4/limb_body_connector-1')
body_10.SetPos(chrono.ChVectorD(0.0754145820704804,0.23005,-0.059741440782467))
body_10.SetRot(chrono.ChQuaternionD(0.5,0.5,0.5,0.5))
body_10.SetMass(0.0319301494979552)
body_10.SetInertiaXX(chrono.ChVectorD(2.21101734329624e-06,4.6562762681289e-06,4.83154745183424e-06))
body_10.SetInertiaXY(chrono.ChVectorD(-1.86684394118378e-22,-1.04999725584544e-22,-5.03356110089508e-22))
body_10.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(0.01,0.00875766097763167,0.01),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_2_1_shape = chrono.ChObjShapeFile() 
body_2_1_shape.SetFilename(shapes_dir +'body_2_1.obj') 
body_2_1_level = chrono.ChAssetLevel() 
body_2_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_2_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_2_1_level.GetAssets().push_back(body_2_1_shape) 
body_10.GetAssets().push_back(body_2_1_level) 

# Auxiliary marker (coordinate system feature)
marker_10_1 =chrono.ChMarker()
marker_10_1.SetName('LB-UL-Ref')
body_10.AddMarker(marker_10_1)
marker_10_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(0.0854145820704804,0.24005,0.000258559217532997),chrono.ChQuaternionD(0.5,-0.5,0.5,0.5)))

# Auxiliary marker (coordinate system feature)
marker_10_2 =chrono.ChMarker()
marker_10_2.SetName('LB-B-Act-1')
body_10.AddMarker(marker_10_2)
marker_10_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(0.0854145820704803,0.24005,-0.059741440782467),chrono.ChQuaternionD(-9.81307786677359E-18,7.85046229341887E-17,0.707106781186547,0.707106781186548)))

exported_items.append(body_10)



# Rigid body part
body_11= chrono.ChBodyAuxRef()
body_11.SetName('Spibot-LEG-4/Actuator_rod-1')
body_11.SetPos(chrono.ChVectorD(0.0855645820704803,0.183604367247803,0.105100348370227))
body_11.SetRot(chrono.ChQuaternionD(0.999817365081353,0.0191111611834704,1.28527557911233e-15,4.33483058043324e-16))
body_11.SetMass(0.00140945245841084)
body_11.SetInertiaXX(chrono.ChVectorD(2.33089158373325e-06,2.32359704642939e-06,2.69230255561874e-08))
body_11.SetInertiaXY(chrono.ChVectorD(2.15260230660863e-22,5.72513084229013e-21,-8.7960988676374e-08))
body_11.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-1.65060230227876e-19,-2.34447212110501e-18,0.0545976735175364),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_5_1_shape = chrono.ChObjShapeFile() 
body_5_1_shape.SetFilename(shapes_dir +'body_5_1.obj') 
body_5_1_level = chrono.ChAssetLevel() 
body_5_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_5_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_5_1_level.GetAssets().push_back(body_5_1_shape) 
body_11.GetAssets().push_back(body_5_1_level) 

# Auxiliary marker (coordinate system feature)
marker_11_1 =chrono.ChMarker()
marker_11_1.SetName('UL-Act-Shaft')
body_11.AddMarker(marker_11_1)
marker_11_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(0.0855645820704805,0.18147863886929,0.160684715811629),chrono.ChQuaternionD(-1.28527557911233E-15,-4.33483058043324E-16,0.999817365081353,0.0191111611834704)))

# Auxiliary marker (coordinate system feature)
marker_11_2 =chrono.ChMarker()
marker_11_2.SetName('LL-Act-Shaft')
body_11.AddMarker(marker_11_2)
marker_11_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(0.0855645820704806,0.179950025203841,0.200655496893087),chrono.ChQuaternionD(-1.28527557911233E-15,-4.33483058043324E-16,0.999817365081353,0.0191111611834704)))

exported_items.append(body_11)



# Rigid body part
body_12= chrono.ChBodyAuxRef()
body_12.SetName('Spibot-LEG-4/Actuator_body-2')
body_12.SetPos(chrono.ChVectorD(0.0854145820735133,0.203944335468757,-4.20014893013215e-05))
body_12.SetRot(chrono.ChQuaternionD(-3.40646309049133e-16,-8.34235858895837e-17,0.0612944436039246,0.99811972788002))
body_12.SetMass(0.00204159144576871)
body_12.SetInertiaXX(chrono.ChVectorD(8.08481090947278e-07,7.90760874880864e-07,9.67478229138678e-08))
body_12.SetInertiaXY(chrono.ChVectorD(8.35251143296348e-23,8.8341315921519e-23,-8.6881753010342e-08))
body_12.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-4.17192939730159e-18,5.58956732701871e-20,-0.0175577824053523),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_4_1_shape = chrono.ChObjShapeFile() 
body_4_1_shape.SetFilename(shapes_dir +'body_4_1.obj') 
body_4_1_shape.SetColor(chrono.ChColor(0.843137254901961,0.843137254901961,0)) 
body_4_1_shape.SetFading(0.75) 
body_4_1_level = chrono.ChAssetLevel() 
body_4_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_4_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_4_1_level.GetAssets().push_back(body_4_1_shape) 
body_12.GetAssets().push_back(body_4_1_level) 

# Auxiliary marker (coordinate system feature)
marker_12_1 =chrono.ChMarker()
marker_12_1.SetName('LL-Act-Base')
body_12.AddMarker(marker_12_1)
marker_12_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(0.0854145820735133,0.197826416131706,-0.0496663006076299),chrono.ChQuaternionD(-3.40646309049133E-16,-8.34235858895837E-17,0.0612944436039246,0.99811972788002)))

# Auxiliary marker (coordinate system feature)
marker_12_2 =chrono.ChMarker()
marker_12_2.SetName('UL-Act-Base')
body_12.AddMarker(marker_12_2)
marker_12_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(0.0854145820735133,0.199049999999116,-0.0397414407839641),chrono.ChQuaternionD(-3.40646309049133E-16,-8.34235858895837E-17,0.0612944436039246,0.99811972788002)))

exported_items.append(body_12)



# Rigid body part
body_13= chrono.ChBodyAuxRef()
body_13.SetName('Spibot-LEG-4/upper_limb_con-1')
body_13.SetPos(chrono.ChVectorD(0.0855145820704805,0.229987547051718,0.099751006371393))
body_13.SetRot(chrono.ChQuaternionD(0.47417704249499,0.524553269335636,0.47417704249499,0.524553269335636))
body_13.SetMass(0.0769386604687246)
body_13.SetInertiaXX(chrono.ChVectorD(1.49539366151159e-05,0.000288404210984833,0.000279898353184369))
body_13.SetInertiaXY(chrono.ChVectorD(2.79419897738629e-05,-1.19450607093279e-05,1.20809784853421e-06))
body_13.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-0.00433891891647107,-0.0160004109829567,1.89023205931516e-19),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_8_1_shape = chrono.ChObjShapeFile() 
body_8_1_shape.SetFilename(shapes_dir +'body_8_1.obj') 
body_8_1_level = chrono.ChAssetLevel() 
body_8_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_8_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_8_1_level.GetAssets().push_back(body_8_1_shape) 
body_13.GetAssets().push_back(body_8_1_level) 

# Auxiliary marker (coordinate system feature)
marker_13_1 =chrono.ChMarker()
marker_13_1.SetName('UL-LL-Ref')
body_13.AddMarker(marker_13_1)
marker_13_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(0.0855145820704805,0.219925094103436,0.199243453525253),chrono.ChQuaternionD(0.706208976071991,0.0356213716096127,0.706208976071991,0.0356213716096131)))

# Auxiliary marker (coordinate system feature)
marker_13_2 =chrono.ChMarker()
marker_13_2.SetName('UL-LB-Ref')
body_13.AddMarker(marker_13_2)
marker_13_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(0.0855145820704805,0.24005,0.000258559217532969),chrono.ChQuaternionD(0.706208976071991,0.0356213716096127,0.706208976071991,0.0356213716096131)))

exported_items.append(body_13)



# Rigid body part
body_14= chrono.ChBodyAuxRef()
body_14.SetName('Spibot-LEG-4/Actuator_rod-2')
body_14.SetPos(chrono.ChVectorD(0.0854145820746712,0.20227696952827,-0.0135665122908671))
body_14.SetRot(chrono.ChQuaternionD(-1.80751102760765e-16,3.33694343558335e-16,0.0612944436039246,0.99811972788002))
body_14.SetMass(0.00140945245841084)
body_14.SetInertiaXX(chrono.ChVectorD(2.33089158373325e-06,2.29247540974964e-06,5.80446622359358e-08))
body_14.SetInertiaXY(chrono.ChVectorD(-3.7222022880386e-22,-1.32403152025681e-21,-2.79722780103322e-07))
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
marker_14_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(0.0854145820746713,0.209083154790739,0.0416405204782734),chrono.ChQuaternionD(0.0612944436039246,0.99811972788002,1.80751102760765E-16,-3.33694343558335E-16)))

# Auxiliary marker (coordinate system feature)
marker_14_2 =chrono.ChMarker()
marker_14_2.SetName('LL-Act-Shaft')
body_14.AddMarker(marker_14_2)
marker_14_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(0.0854145820746713,0.213977490260379,0.0813399597729362),chrono.ChQuaternionD(0.0612944436039246,0.99811972788002,1.80751102760765E-16,-3.33694343558335E-16)))

exported_items.append(body_14)



# Rigid body part
body_15= chrono.ChBodyAuxRef()
body_15.SetName('Spibot-LEG-4/lower_limb-1')
body_15.SetPos(chrono.ChVectorD(0.0855145820704806,0.119962547051718,0.201980091413802))
body_15.SetRot(chrono.ChQuaternionD(-2.77581748010316e-16,-1.38790874005158e-16,0.999906363245374,-0.0136844708121779))
body_15.SetMass(0.173763895224452)
body_15.SetInertiaXX(chrono.ChVectorD(0.000660134295478084,9.24662227508727e-06,0.000660165532595656))
body_15.SetInertiaXY(chrono.ChVectorD(7.06262259215028e-11,-8.67251897642146e-12,1.78379925000873e-05))
body_15.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(4.14273289964873e-09,-0.0143933772184335,3.59893950746433e-07),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_9_1_shape = chrono.ChObjShapeFile() 
body_9_1_shape.SetFilename(shapes_dir +'body_9_1.obj') 
body_9_1_shape.SetColor(chrono.ChColor(0.898039215686275,0.917647058823529,0.929411764705882)) 
body_9_1_shape.SetFading(0.75) 
body_9_1_level = chrono.ChAssetLevel() 
body_9_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_9_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_9_1_level.GetAssets().push_back(body_9_1_shape) 
body_15.GetAssets().push_back(body_9_1_level) 

# Auxiliary marker (coordinate system feature)
marker_15_1 =chrono.ChMarker()
marker_15_1.SetName('LowerLimbCenterRef')
body_15.AddMarker(marker_15_1)
marker_15_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(0.0855145820704806,0.119962547051718,0.201980091413802),chrono.ChQuaternionD(0.00967638210824057,0.707040570002384,-0.707040570002383,0.00967638210824018)))

# Auxiliary marker (coordinate system feature)
marker_15_2 =chrono.ChMarker()
marker_15_2.SetName('LL-UL-Ref')
body_15.AddMarker(marker_15_2)
marker_15_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(0.0855145820704805,0.219925094103436,0.199243453525253),chrono.ChQuaternionD(0.00967638210824057,0.707040570002384,-0.707040570002383,0.00967638210824018)))

# Collision shapes 
body_15.GetCollisionModel().ClearModel()
body_15.GetCollisionModel().AddSphere(0.01, chrono.ChVectorD(3.46944695195361E-17,-0.1,0))
body_15.GetCollisionModel().BuildModel()
body_15.SetCollide(True)

exported_items.append(body_15)



# Rigid body part
body_16= chrono.ChBodyAuxRef()
body_16.SetName('Spibot-LEG-4/Actuator_body-1')
body_16.SetPos(chrono.ChVectorD(0.0855645820704803,0.183562311606805,0.106200035529632))
body_16.SetRot(chrono.ChQuaternionD(-3.97608372421876e-16,2.57445956855298e-16,-0.0191111611834704,0.999817365081353))
body_16.SetMass(0.00204159144576871)
body_16.SetInertiaXX(chrono.ChVectorD(8.08481090947278e-07,8.00427239380347e-07,8.70814584143847e-08))
body_16.SetInertiaXY(chrono.ChVectorD(1.40759754541229e-23,-5.19045138877448e-22,2.73206382758794e-08))
body_16.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-4.17192939730159e-18,5.58956732701871e-20,-0.0175577824053523),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_4_1_shape = chrono.ChObjShapeFile() 
body_4_1_shape.SetFilename(shapes_dir +'body_4_1.obj') 
body_4_1_shape.SetColor(chrono.ChColor(0.752941176470588,0.752941176470588,0.752941176470588)) 
body_4_1_shape.SetFading(0.75) 
body_4_1_level = chrono.ChAssetLevel() 
body_4_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_4_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_4_1_level.GetAssets().push_back(body_4_1_shape) 
body_16.GetAssets().push_back(body_4_1_level) 

# Auxiliary marker (coordinate system feature)
marker_16_1 =chrono.ChMarker()
marker_16_1.SetName('LL-Act-Base')
body_16.AddMarker(marker_16_1)
marker_16_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(0.0855645820704803,0.185473078688615,0.0562365591778096),chrono.ChQuaternionD(-3.97608372421876E-16,2.57445956855298E-16,-0.0191111611834704,0.999817365081353)))

# Auxiliary marker (coordinate system feature)
marker_16_2 =chrono.ChMarker()
marker_16_2.SetName('UL-Act-Base')
body_16.AddMarker(marker_16_2)
marker_16_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(0.0855645820704803,0.185090925272253,0.066229254448174),chrono.ChQuaternionD(-3.97608372421876E-16,2.57445956855298E-16,-0.0191111611834704,0.999817365081353)))

exported_items.append(body_16)



# Rigid body part
body_17= chrono.ChBodyAuxRef()
body_17.SetName('Spibot-LEG-4/limb_body_connector-2')
body_17.SetPos(chrono.ChVectorD(0.0754145820704804,0.18905,-0.0597414407824671))
body_17.SetRot(chrono.ChQuaternionD(0.5,0.5,0.5,0.5))
body_17.SetMass(0.0319301494979552)
body_17.SetInertiaXX(chrono.ChVectorD(2.21101734329624e-06,4.6562762681289e-06,4.83154745183424e-06))
body_17.SetInertiaXY(chrono.ChVectorD(2.72520556243629e-21,4.04689175765736e-23,-5.52003636015249e-22))
body_17.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(0.01,0.00875766097763167,0.01),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_2_1_shape = chrono.ChObjShapeFile() 
body_2_1_shape.SetFilename(shapes_dir +'body_2_1.obj') 
body_2_1_level = chrono.ChAssetLevel() 
body_2_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_2_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_2_1_level.GetAssets().push_back(body_2_1_shape) 
body_17.GetAssets().push_back(body_2_1_level) 

# Auxiliary marker (coordinate system feature)
marker_17_1 =chrono.ChMarker()
marker_17_1.SetName('LB-UL-Ref')
body_17.AddMarker(marker_17_1)
marker_17_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(0.0854145820704803,0.19905,-0.039741440782467),chrono.ChQuaternionD(0.5,-0.5,0.5,0.5)))

# Auxiliary marker (coordinate system feature)
marker_17_2 =chrono.ChMarker()
marker_17_2.SetName('LB-B-Act-1')
body_17.AddMarker(marker_17_2)
marker_17_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(0.0854145820704803,0.19905,-0.059741440782467),chrono.ChQuaternionD(1.07943856534509E-16,0,0.707106781186547,0.707106781186548)))

exported_items.append(body_17)



# Rigid body part
body_18= chrono.ChBodyAuxRef()
body_18.SetName('Spibot-LEG-5/upper_limb_con-1')
body_18.SetPos(chrono.ChVectorD(-0.00448541792952095,0.229987547232601,0.0997510063896872))
body_18.SetRot(chrono.ChQuaternionD(0.474177042971824,0.524553268904596,0.474177042971824,0.524553268904596))
body_18.SetMass(0.0769386604687246)
body_18.SetInertiaXX(chrono.ChVectorD(1.49539365135156e-05,0.000288404211086433,0.000279898353184369))
body_18.SetInertiaXY(chrono.ChVectorD(2.79419892767145e-05,-1.19450607115243e-05,1.2080978268174e-06))
body_18.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-0.00433891891647107,-0.0160004109829567,1.89023205931516e-19),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_8_1_shape = chrono.ChObjShapeFile() 
body_8_1_shape.SetFilename(shapes_dir +'body_8_1.obj') 
body_8_1_level = chrono.ChAssetLevel() 
body_8_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_8_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_8_1_level.GetAssets().push_back(body_8_1_shape) 
body_18.GetAssets().push_back(body_8_1_level) 

# Auxiliary marker (coordinate system feature)
marker_18_1 =chrono.ChMarker()
marker_18_1.SetName('UL-LL-Ref')
body_18.AddMarker(marker_18_1)
marker_18_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.00448541792952092,0.219925094465202,0.199243453561842),chrono.ChQuaternionD(0.706208976104372,0.0356213709676484,0.706208976104372,0.0356213709676488)))

# Auxiliary marker (coordinate system feature)
marker_18_2 =chrono.ChMarker()
marker_18_2.SetName('UL-LB-Ref')
body_18.AddMarker(marker_18_2)
marker_18_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.00448541792952098,0.24005,0.000258559217533094),chrono.ChQuaternionD(0.706208976104372,0.0356213709676484,0.706208976104372,0.0356213709676488)))

exported_items.append(body_18)



# Rigid body part
body_19= chrono.ChBodyAuxRef()
body_19.SetName('Spibot-LEG-5/limb_body_connector-2')
body_19.SetPos(chrono.ChVectorD(-0.0145854179295196,0.18905,-0.059741440782467))
body_19.SetRot(chrono.ChQuaternionD(0.5,0.5,0.5,0.5))
body_19.SetMass(0.0319301494979552)
body_19.SetInertiaXX(chrono.ChVectorD(2.21101734329624e-06,4.6562762681289e-06,4.83154745183424e-06))
body_19.SetInertiaXY(chrono.ChVectorD(3.19379103542352e-21,2.74574891292646e-22,-4.47826290111567e-23))
body_19.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(0.01,0.00875766097763167,0.01),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_2_1_shape = chrono.ChObjShapeFile() 
body_2_1_shape.SetFilename(shapes_dir +'body_2_1.obj') 
body_2_1_level = chrono.ChAssetLevel() 
body_2_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_2_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_2_1_level.GetAssets().push_back(body_2_1_shape) 
body_19.GetAssets().push_back(body_2_1_level) 

# Auxiliary marker (coordinate system feature)
marker_19_1 =chrono.ChMarker()
marker_19_1.SetName('LB-UL-Ref')
body_19.AddMarker(marker_19_1)
marker_19_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.00458541792951962,0.19905,-0.039741440782467),chrono.ChQuaternionD(0.5,-0.5,0.5,0.5)))

# Auxiliary marker (coordinate system feature)
marker_19_2 =chrono.ChMarker()
marker_19_2.SetName('LB-B-Act-1')
body_19.AddMarker(marker_19_2)
marker_19_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.00458541792951962,0.19905,-0.059741440782467),chrono.ChQuaternionD(6.86915450674151E-17,-6.86915450674151E-17,0.707106781186547,0.707106781186548)))

exported_items.append(body_19)



# Rigid body part
body_20= chrono.ChBodyAuxRef()
body_20.SetName('Spibot-LEG-5/Actuator_body-1')
body_20.SetPos(chrono.ChVectorD(-0.00443541792951929,0.183562311730416,0.106200035629691))
body_20.SetRot(chrono.ChQuaternionD(-6.5931533487098e-16,2.49845811109003e-16,-0.0191111609649517,0.99981736508553))
body_20.SetMass(0.00204159144576871)
body_20.SetInertiaXX(chrono.ChVectorD(8.08481090947278e-07,8.00427239404232e-07,8.70814583905e-08))
body_20.SetInertiaXY(chrono.ChVectorD(1.67821557044002e-23,-5.27971414745411e-22,2.73206379640637e-08))
body_20.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-4.17192939730159e-18,5.58956732701871e-20,-0.0175577824053523),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_4_1_shape = chrono.ChObjShapeFile() 
body_4_1_shape.SetFilename(shapes_dir +'body_4_1.obj') 
body_4_1_shape.SetColor(chrono.ChColor(0.752941176470588,0.752941176470588,0.752941176470588)) 
body_4_1_shape.SetFading(0.75) 
body_4_1_level = chrono.ChAssetLevel() 
body_4_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_4_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_4_1_level.GetAssets().push_back(body_4_1_shape) 
body_20.GetAssets().push_back(body_4_1_level) 

# Auxiliary marker (coordinate system feature)
marker_20_1 =chrono.ChMarker()
marker_20_1.SetName('LL-Act-Base')
body_20.AddMarker(marker_20_1)
marker_20_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.00443541792951932,0.185473078790387,0.0562365592770336),chrono.ChQuaternionD(-6.5931533487098E-16,2.49845811109003E-16,-0.0191111609649517,0.99981736508553)))

# Auxiliary marker (coordinate system feature)
marker_20_2 =chrono.ChMarker()
marker_20_2.SetName('UL-Act-Base')
body_20.AddMarker(marker_20_2)
marker_20_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.00443541792951931,0.185090925378393,0.0662292545475651),chrono.ChQuaternionD(-6.5931533487098E-16,2.49845811109003E-16,-0.0191111609649517,0.99981736508553)))

exported_items.append(body_20)



# Rigid body part
body_21= chrono.ChBodyAuxRef()
body_21.SetName('Spibot-LEG-5/limb_body_connector-1')
body_21.SetPos(chrono.ChVectorD(-0.0145854179295196,0.23005,-0.059741440782467))
body_21.SetRot(chrono.ChQuaternionD(0.5,0.5,0.5,0.5))
body_21.SetMass(0.0319301494979552)
body_21.SetInertiaXX(chrono.ChVectorD(2.21101734329624e-06,4.6562762681289e-06,4.83154745183424e-06))
body_21.SetInertiaXY(chrono.ChVectorD(2.81901078868854e-22,6.77381890722014e-23,2.62340153009205e-22))
body_21.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(0.01,0.00875766097763167,0.01),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_2_1_shape = chrono.ChObjShapeFile() 
body_2_1_shape.SetFilename(shapes_dir +'body_2_1.obj') 
body_2_1_level = chrono.ChAssetLevel() 
body_2_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_2_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_2_1_level.GetAssets().push_back(body_2_1_shape) 
body_21.GetAssets().push_back(body_2_1_level) 

# Auxiliary marker (coordinate system feature)
marker_21_1 =chrono.ChMarker()
marker_21_1.SetName('LB-UL-Ref')
body_21.AddMarker(marker_21_1)
marker_21_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.00458541792951961,0.24005,0.000258559217533011),chrono.ChQuaternionD(0.5,-0.5,0.5,0.5)))

# Auxiliary marker (coordinate system feature)
marker_21_2 =chrono.ChMarker()
marker_21_2.SetName('LB-B-Act-1')
body_21.AddMarker(marker_21_2)
marker_21_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.00458541792951962,0.24005,-0.059741440782467),chrono.ChQuaternionD(-3.92523114670944E-17,-9.81307786677359E-18,0.707106781186547,0.707106781186548)))

exported_items.append(body_21)



# Rigid body part
body_22= chrono.ChBodyAuxRef()
body_22.SetName('Spibot-LEG-5/Actuator_body-2')
body_22.SetPos(chrono.ChVectorD(-0.0045854179295195,0.203944335502457,-4.20014918497691e-05))
body_22.SetRot(chrono.ChQuaternionD(-7.49692727233603e-16,-1.82307019644277e-17,0.0612944440164548,0.998119727854687))
body_22.SetMass(0.00204159144576871)
body_22.SetInertiaXX(chrono.ChVectorD(8.08481090947278e-07,7.90760874737229e-07,9.67478230575033e-08))
body_22.SetInertiaXY(chrono.ChVectorD(-3.48261176953014e-23,-1.95582460258107e-22,-8.68817535840234e-08))
body_22.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-4.17192939730159e-18,5.58956732701871e-20,-0.0175577824053523),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_4_1_shape = chrono.ChObjShapeFile() 
body_4_1_shape.SetFilename(shapes_dir +'body_4_1.obj') 
body_4_1_shape.SetColor(chrono.ChColor(0.843137254901961,0.843137254901961,0)) 
body_4_1_shape.SetFading(0.75) 
body_4_1_level = chrono.ChAssetLevel() 
body_4_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_4_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_4_1_level.GetAssets().push_back(body_4_1_shape) 
body_22.GetAssets().push_back(body_4_1_level) 

# Auxiliary marker (coordinate system feature)
marker_22_1 =chrono.ChMarker()
marker_22_1.SetName('LL-Act-Base')
body_22.AddMarker(marker_22_1)
marker_22_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.00458541792951949,0.197826416124386,-0.0496663006051211),chrono.ChQuaternionD(-7.49692727233603E-16,-1.82307019644277E-17,0.0612944440164548,0.998119727854687)))

# Auxiliary marker (coordinate system feature)
marker_22_2 =chrono.ChMarker()
marker_22_2.SetName('UL-Act-Base')
body_22.AddMarker(marker_22_2)
marker_22_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.00458541792951949,0.19905,-0.0397414407824669),chrono.ChQuaternionD(-7.49692727233603E-16,-1.82307019644277E-17,0.0612944440164548,0.998119727854687)))

exported_items.append(body_22)



# Rigid body part
body_23= chrono.ChBodyAuxRef()
body_23.SetName('Spibot-LEG-5/Actuator_rod-2')
body_23.SetPos(chrono.ChVectorD(-0.00458541792951961,0.202276969559096,-0.0135665122268584))
body_23.SetRot(chrono.ChQuaternionD(-7.71668169498235e-16,1.39039309819502e-17,0.0612944440164548,0.998119727854687))
body_23.SetMass(0.00140945245841084)
body_23.SetInertiaXX(chrono.ChVectorD(2.33089158373325e-06,2.2924754092872e-06,5.80446626983817e-08))
body_23.SetInertiaXY(chrono.ChVectorD(1.80339987042541e-22,-1.57048284776771e-22,-2.79722781950336e-07))
body_23.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-1.65060230227876e-19,-2.34447212110501e-18,0.0545976735175364),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_5_1_shape = chrono.ChObjShapeFile() 
body_5_1_shape.SetFilename(shapes_dir +'body_5_1.obj') 
body_5_1_level = chrono.ChAssetLevel() 
body_5_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_5_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_5_1_level.GetAssets().push_back(body_5_1_shape) 
body_23.GetAssets().push_back(body_5_1_level) 

# Auxiliary marker (coordinate system feature)
marker_23_1 =chrono.ChMarker()
marker_23_1.SetName('UL-Act-Shaft')
body_23.AddMarker(marker_23_1)
marker_23_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.00458541792951961,0.209083154867199,0.041640520536656),chrono.ChQuaternionD(0.0612944440164548,0.998119727854687,7.92949071179202E-16,-6.92079175191906E-18)))

# Auxiliary marker (coordinate system feature)
marker_23_2 =chrono.ChMarker()
marker_23_2.SetName('LL-Act-Shaft')
body_23.AddMarker(marker_23_2)
marker_23_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.00458541792951961,0.213977490369656,0.0813399598272731),chrono.ChQuaternionD(0.0612944440164548,0.998119727854687,7.71668169498235E-16,-1.39039309819502E-17)))

exported_items.append(body_23)



# Rigid body part
body_24= chrono.ChBodyAuxRef()
body_24.SetName('Spibot-LEG-5/lower_limb-1')
body_24.SetPos(chrono.ChVectorD(-0.00448541792951918,0.119962547232601,0.201980084843176))
body_24.SetRot(chrono.ChQuaternionD(-2.22455947018378e-17,-4.02797981396485e-16,0.999906363697624,-0.0136844377668256))
body_24.SetMass(0.173763895224452)
body_24.SetInertiaXX(chrono.ChVectorD(0.000660134295478084,9.24661991701833e-06,0.000660165534953724))
body_24.SetInertiaXY(chrono.ChVectorD(7.06262268305152e-11,-8.67251424923095e-12,1.78379494763691e-05))
body_24.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(4.14273289964873e-09,-0.0143933772184335,3.59893950746433e-07),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_9_1_shape = chrono.ChObjShapeFile() 
body_9_1_shape.SetFilename(shapes_dir +'body_9_1.obj') 
body_9_1_shape.SetColor(chrono.ChColor(0.898039215686275,0.917647058823529,0.929411764705882)) 
body_9_1_shape.SetFading(0.75) 
body_9_1_level = chrono.ChAssetLevel() 
body_9_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_9_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_9_1_level.GetAssets().push_back(body_9_1_shape) 
body_24.GetAssets().push_back(body_9_1_level) 

# Auxiliary marker (coordinate system feature)
marker_24_1 =chrono.ChMarker()
marker_24_1.SetName('LowerLimbCenterRef')
body_24.AddMarker(marker_24_1)
marker_24_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.00448541792951918,0.119962547232601,0.201980084843176),chrono.ChQuaternionD(0.00967635874164769,0.707040570322173,-0.707040570322172,0.00967635874164766)))

# Auxiliary marker (coordinate system feature)
marker_24_2 =chrono.ChMarker()
marker_24_2.SetName('LL-UL-Ref')
body_24.AddMarker(marker_24_2)
marker_24_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.00448541792951926,0.219925094465202,0.199243453561842),chrono.ChQuaternionD(0.00967635874164769,0.707040570322173,-0.707040570322172,0.00967635874164766)))

# Collision shapes 
body_24.GetCollisionModel().ClearModel()
body_24.GetCollisionModel().AddSphere(0.01, chrono.ChVectorD(3.46944695195361E-17,-0.1,0))
body_24.GetCollisionModel().BuildModel()
body_24.SetCollide(True)

exported_items.append(body_24)



# Rigid body part
body_25= chrono.ChBodyAuxRef()
body_25.SetName('Spibot-LEG-5/Actuator_rod-1')
body_25.SetPos(chrono.ChVectorD(-0.00443541792951929,0.183604367474469,0.10510034576299))
body_25.SetRot(chrono.ChQuaternionD(0.99981736508553,0.0191111609649518,1.11042582715112e-16,6.80135819130063e-16))
body_25.SetMass(0.00140945245841084)
body_25.SetInertiaXX(chrono.ChVectorD(2.33089158373325e-06,2.32359704650629e-06,2.69230254792889e-08))
body_25.SetInertiaXY(chrono.ChVectorD(2.44361499952329e-22,3.546483036505e-22,-8.79609876724585e-08))
body_25.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-1.65060230227876e-19,-2.34447212110501e-18,0.0545976735175364),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_5_1_shape = chrono.ChObjShapeFile() 
body_5_1_shape.SetFilename(shapes_dir +'body_5_1.obj') 
body_5_1_level = chrono.ChAssetLevel() 
body_5_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_5_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_5_1_level.GetAssets().push_back(body_5_1_shape) 
body_25.GetAssets().push_back(body_5_1_level) 

# Auxiliary marker (coordinate system feature)
marker_25_1 =chrono.ChMarker()
marker_25_1.SetName('UL-Act-Shaft')
body_25.AddMarker(marker_25_1)
marker_25_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.00443541792951928,0.181478639120252,0.160684713205322),chrono.ChQuaternionD(-1.11042582715112E-16,-6.80135819130063E-16,0.99981736508553,0.0191111609649518)))

# Auxiliary marker (coordinate system feature)
marker_25_2 =chrono.ChMarker()
marker_25_2.SetName('LL-Act-Shaft')
body_25.AddMarker(marker_25_2)
marker_25_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.00443541792951927,0.179950025472276,0.200655494287447),chrono.ChQuaternionD(-1.11042582715112E-16,-6.80135819130063E-16,0.99981736508553,0.0191111609649518)))

exported_items.append(body_25)



# Rigid body part
body_26= chrono.ChBodyAuxRef()
body_26.SetName('Spibot-LEG-6/limb_body_connector-1')
body_26.SetPos(chrono.ChVectorD(-0.10458541792952,0.22995,-0.059741440782467))
body_26.SetRot(chrono.ChQuaternionD(0.5,0.5,0.5,0.5))
body_26.SetMass(0.0319301494979552)
body_26.SetInertiaXX(chrono.ChVectorD(2.21101734329624e-06,4.6562762681289e-06,4.83154745183424e-06))
body_26.SetInertiaXY(chrono.ChVectorD(3.20029254535218e-21,-6.14139976648451e-22,-4.4782629011157e-23))
body_26.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(0.01,0.00875766097763167,0.01),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_2_1_shape = chrono.ChObjShapeFile() 
body_2_1_shape.SetFilename(shapes_dir +'body_2_1.obj') 
body_2_1_level = chrono.ChAssetLevel() 
body_2_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_2_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_2_1_level.GetAssets().push_back(body_2_1_shape) 
body_26.GetAssets().push_back(body_2_1_level) 

# Auxiliary marker (coordinate system feature)
marker_26_1 =chrono.ChMarker()
marker_26_1.SetName('LB-UL-Ref')
body_26.AddMarker(marker_26_1)
marker_26_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.0945854179295196,0.23995,0.000258559217533025),chrono.ChQuaternionD(0.5,-0.5,0.5,0.5)))

# Auxiliary marker (coordinate system feature)
marker_26_2 =chrono.ChMarker()
marker_26_2.SetName('LB-B-Act-1')
body_26.AddMarker(marker_26_2)
marker_26_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.0945854179295196,0.23995,-0.059741440782467),chrono.ChQuaternionD(3.92523114670943E-17,-1.47196168001604E-16,0.707106781186547,0.707106781186548)))

exported_items.append(body_26)



# Rigid body part
body_27= chrono.ChBodyAuxRef()
body_27.SetName('Spibot-LEG-6/Actuator_rod-2')
body_27.SetPos(chrono.ChVectorD(-0.0945854179295198,0.202185177877465,-0.0135493514893872))
body_27.SetRot(chrono.ChQuaternionD(3.43313244580262e-16,5.21667355538171e-16,0.061408790939526,0.998112699245604))
body_27.SetMass(0.00140945245841084)
body_27.SetInertiaXX(chrono.ChVectorD(2.33089158373325e-06,2.29234710876006e-06,5.81729632255155e-08))
body_27.SetInertiaXY(chrono.ChVectorD(-2.59844795534394e-22,-2.12704903110003e-21,-2.80234717555911e-07))
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
marker_27_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.0945854179295197,0.209004012344094,0.041656120354595),chrono.ChQuaternionD(0.061408790939526,0.998112699245604,-3.43313244580262E-16,-5.21667355538171E-16)))

# Auxiliary marker (coordinate system feature)
marker_27_2 =chrono.ChMarker()
marker_27_2.SetName('LL-Act-Shaft')
body_27.AddMarker(marker_27_2)
marker_27_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.0945854179295197,0.213907443870659,0.0813544371862227),chrono.ChQuaternionD(0.061408790939526,0.998112699245604,-3.43313244580262E-16,-5.21667355538171E-16)))

exported_items.append(body_27)



# Rigid body part
body_28= chrono.ChBodyAuxRef()
body_28.SetName('Spibot-LEG-6/limb_body_connector-2')
body_28.SetPos(chrono.ChVectorD(-0.10458541792952,0.18895,-0.059741440782467))
body_28.SetRot(chrono.ChQuaternionD(0.499999999999999,0.5,0.499999999999999,0.500000000000001))
body_28.SetMass(0.0319301494979552)
body_28.SetInertiaXX(chrono.ChVectorD(2.21101734329624e-06,4.6562762681289e-06,4.83154745183424e-06))
body_28.SetInertiaXY(chrono.ChVectorD(6.11218250190685e-21,-5.41405655067889e-22,-9.34301549368991e-23))
body_28.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(0.01,0.00875766097763167,0.01),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_2_1_shape = chrono.ChObjShapeFile() 
body_2_1_shape.SetFilename(shapes_dir +'body_2_1.obj') 
body_2_1_level = chrono.ChAssetLevel() 
body_2_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_2_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_2_1_level.GetAssets().push_back(body_2_1_shape) 
body_28.GetAssets().push_back(body_2_1_level) 

# Auxiliary marker (coordinate system feature)
marker_28_1 =chrono.ChMarker()
marker_28_1.SetName('LB-UL-Ref')
body_28.AddMarker(marker_28_1)
marker_28_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.0945854179295197,0.19895,-0.039741440782467),chrono.ChQuaternionD(0.500000000000001,-0.5,0.499999999999999,0.500000000000001)))

# Auxiliary marker (coordinate system feature)
marker_28_2 =chrono.ChMarker()
marker_28_2.SetName('LB-B-Act-1')
body_28.AddMarker(marker_28_2)
marker_28_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.0945854179295197,0.19895,-0.059741440782467),chrono.ChQuaternionD(1.47196168001604E-16,-2.35513868802566E-16,0.707106781186547,0.707106781186548)))

exported_items.append(body_28)



# Rigid body part
body_29= chrono.ChBodyAuxRef()
body_29.SetName('Spibot-LEG-6/Actuator_body-1')
body_29.SetPos(chrono.ChVectorD(-0.0944354179295199,0.18351514448397,0.10622846674047))
body_29.SetRot(chrono.ChQuaternionD(4.86421757461406e-16,7.68116531523153e-16,-0.0188648585326012,0.999822042721876))
body_29.SetMass(0.00204159144576871)
body_29.SetInertiaXX(chrono.ChVectorD(8.08481090947278e-07,8.00453987649312e-07,8.70547101454196e-08))
body_29.SetInertiaXY(chrono.ChVectorD(5.48113273893796e-23,-1.28001808714525e-21,2.69691637897277e-08))
body_29.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-4.17192939730159e-18,5.58956732701871e-20,-0.0175577824053523),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_4_1_shape = chrono.ChObjShapeFile() 
body_4_1_shape.SetFilename(shapes_dir +'body_4_1.obj') 
body_4_1_shape.SetColor(chrono.ChColor(0.752941176470588,0.752941176470588,0.752941176470588)) 
body_4_1_shape.SetFading(0.75) 
body_4_1_level = chrono.ChAssetLevel() 
body_4_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_4_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_4_1_level.GetAssets().push_back(body_4_1_shape) 
body_29.GetAssets().push_back(body_4_1_level) 

# Auxiliary marker (coordinate system feature)
marker_29_1 =chrono.ChMarker()
marker_29_1.SetName('LL-Act-Base')
body_29.AddMarker(marker_29_1)
marker_29_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.09443541792952,0.185401294623342,0.0562640550292152),chrono.ChQuaternionD(4.86421757461406E-16,7.68116531523153E-16,-0.0188648585326012,0.999822042721876)))

# Auxiliary marker (coordinate system feature)
marker_29_2 =chrono.ChMarker()
marker_29_2.SetName('UL-Act-Base')
body_29.AddMarker(marker_29_2)
marker_29_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.09443541792952,0.185024064595468,0.0662569373714661),chrono.ChQuaternionD(4.86421757461406E-16,7.68116531523153E-16,-0.0188648585326012,0.999822042721876)))

exported_items.append(body_29)



# Rigid body part
body_30= chrono.ChBodyAuxRef()
body_30.SetName('Spibot-LEG-6/Actuator_rod-1')
body_30.SetPos(chrono.ChVectorD(-0.0944354179295197,0.183557492907471,0.10510665038927))
body_30.SetRot(chrono.ChQuaternionD(0.999822042721876,0.0188648585326011,4.85809026525555e-16,-3.47006447518253e-16))
body_30.SetMass(0.00140945245841084)
body_30.SetInertiaXX(chrono.ChVectorD(2.33089158373325e-06,2.32368316462911e-06,2.68369073564662e-08))
body_30.SetInertiaXY(chrono.ChVectorD(-3.181426806333e-24,2.20521208150982e-21,-8.68293883460943e-08))
body_30.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-1.65060230227876e-19,-2.34447212110501e-18,0.0545976735175364),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_5_1_shape = chrono.ChObjShapeFile() 
body_5_1_shape.SetFilename(shapes_dir +'body_5_1.obj') 
body_5_1_level = chrono.ChAssetLevel() 
body_5_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_5_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_5_1_level.GetAssets().push_back(body_5_1_shape) 
body_30.GetAssets().push_back(body_5_1_level) 

# Auxiliary marker (coordinate system feature)
marker_30_1 =chrono.ChMarker()
marker_30_1.SetName('UL-Act-Shaft')
body_30.AddMarker(marker_30_1)
marker_30_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.0944354179295196,0.18145915087742,0.16069205841804),chrono.ChQuaternionD(-4.85809026525555E-16,3.47006447518253E-16,0.999822042721876,0.0188648585326011)))

# Auxiliary marker (coordinate system feature)
marker_30_2 =chrono.ChMarker()
marker_30_2.SetName('LL-Act-Shaft')
body_30.AddMarker(marker_30_2)
marker_30_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.0944354179295196,0.179950230765922,0.200663587787044),chrono.ChQuaternionD(-4.85809026525555E-16,3.47006447518253E-16,0.999822042721876,0.0188648585326011)))

exported_items.append(body_30)



# Rigid body part
body_31= chrono.ChBodyAuxRef()
body_31.SetName('Spibot-LEG-6/Actuator_body-2')
body_31.SetPos(chrono.ChVectorD(-0.0945854179295196,0.203853431526565,-4.31239508392467e-05))
body_31.SetRot(chrono.ChQuaternionD(4.76283686992608e-16,1.68343598440916e-16,0.061408790939526,0.998112699245604))
body_31.SetMass(0.00204159144576871)
body_31.SetInertiaXX(chrono.ChVectorD(8.08481090947278e-07,7.90721024658857e-07,9.67876731358753e-08))
body_31.SetInertiaXY(chrono.ChVectorD(-3.73520924500303e-23,-3.5690196038101e-22,-8.70407605223369e-08))
body_31.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-4.17192939730159e-18,5.58956732701871e-20,-0.0175577824053523),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_4_1_shape = chrono.ChObjShapeFile() 
body_4_1_shape.SetFilename(shapes_dir +'body_4_1.obj') 
body_4_1_shape.SetColor(chrono.ChColor(0.843137254901961,0.843137254901961,0)) 
body_4_1_shape.SetFading(0.75) 
body_4_1_level = chrono.ChAssetLevel() 
body_4_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_4_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_4_1_level.GetAssets().push_back(body_4_1_shape) 
body_31.GetAssets().push_back(body_4_1_level) 

# Auxiliary marker (coordinate system feature)
marker_31_1 =chrono.ChMarker()
marker_31_1.SetName('LL-Act-Base')
body_31.AddMarker(marker_31_1)
marker_31_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.0945854179295196,0.197724142118359,-0.0496660199903738),chrono.ChQuaternionD(4.76283686992608E-16,1.68343598440916E-16,0.061408790939526,0.998112699245604)))

# Auxiliary marker (coordinate system feature)
marker_31_2 =chrono.ChMarker()
marker_31_2.SetName('UL-Act-Base')
body_31.AddMarker(marker_31_2)
marker_31_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.0945854179295196,0.19895,-0.0397414407824669),chrono.ChQuaternionD(4.76283686992608E-16,1.68343598440916E-16,0.061408790939526,0.998112699245604)))

exported_items.append(body_31)



# Rigid body part
body_32= chrono.ChBodyAuxRef()
body_32.SetName('Spibot-LEG-6/upper_limb_con-1')
body_32.SetPos(chrono.ChVectorD(-0.0944854179295194,0.229937685578569,0.0997560645125223))
body_32.SetRot(chrono.ChQuaternionD(0.474309196565301,0.524433776613957,0.474309196565301,0.524433776613958))
body_32.SetMass(0.0769386604687246)
body_32.SetInertiaXX(chrono.ChVectorD(1.49258444349848e-05,0.000288432303164964,0.000279898353184369))
body_32.SetInertiaXY(chrono.ChVectorD(2.78041757473149e-05,-1.19456679896249e-05,1.20207821825837e-06))
body_32.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-0.00433891891647107,-0.0160004109829567,1.89023205931516e-19),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_8_1_shape = chrono.ChObjShapeFile() 
body_8_1_shape.SetFilename(shapes_dir +'body_8_1.obj') 
body_8_1_level = chrono.ChAssetLevel() 
body_8_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_8_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_8_1_level.GetAssets().push_back(body_8_1_shape) 
body_32.GetAssets().push_back(body_8_1_level) 

# Auxiliary marker (coordinate system feature)
marker_32_1 =chrono.ChMarker()
marker_32_1.SetName('UL-LL-Ref')
body_32.AddMarker(marker_32_1)
marker_32_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.0944854179295194,0.219925371157137,0.199253569807512),chrono.ChQuaternionD(0.706217928997468,0.0354434304565329,0.706217928997468,0.0354434304565332)))

# Auxiliary marker (coordinate system feature)
marker_32_2 =chrono.ChMarker()
marker_32_2.SetName('UL-LB-Ref')
body_32.AddMarker(marker_32_2)
marker_32_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.0944854179295194,0.23995,0.000258559217533053),chrono.ChQuaternionD(0.706217928997468,0.0354434304565329,0.706217928997468,0.0354434304565332)))

exported_items.append(body_32)



# Rigid body part
body_33= chrono.ChBodyAuxRef()
body_33.SetName('Spibot-LEG-6/lower_limb-1')
body_33.SetPos(chrono.ChVectorD(-0.0944854179295196,0.119962685578569,0.201985142966013))
body_33.SetRot(chrono.ChQuaternionD(5.89180282262924e-17,-2.490186419911e-16,0.999906709594871,-0.0136591400592151))
body_33.SetMass(0.173763895224452)
body_33.SetInertiaXX(chrono.ChVectorD(0.000660134295478084,9.2448163779763e-06,0.000660167338492766))
body_33.SetInertiaXY(chrono.ChVectorD(7.0626665371779e-11,-8.66894053532824e-12,1.78050127939377e-05))
body_33.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(4.14273289964873e-09,-0.0143933772184335,3.59893950746433e-07),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_9_1_shape = chrono.ChObjShapeFile() 
body_9_1_shape.SetFilename(shapes_dir +'body_9_1.obj') 
body_9_1_shape.SetColor(chrono.ChColor(0.898039215686275,0.917647058823529,0.929411764705882)) 
body_9_1_shape.SetFading(0.75) 
body_9_1_level = chrono.ChAssetLevel() 
body_9_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_9_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_9_1_level.GetAssets().push_back(body_9_1_shape) 
body_33.GetAssets().push_back(body_9_1_level) 

# Auxiliary marker (coordinate system feature)
marker_33_1 =chrono.ChMarker()
marker_33_1.SetName('LowerLimbCenterRef')
body_33.AddMarker(marker_33_1)
marker_33_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.0944854179295196,0.119962685578569,0.201985142966013),chrono.ChQuaternionD(0.00965847056104777,0.707040814908462,-0.707040814908461,0.00965847056104785)))

# Auxiliary marker (coordinate system feature)
marker_33_2 =chrono.ChMarker()
marker_33_2.SetName('LL-UL-Ref')
body_33.AddMarker(marker_33_2)
marker_33_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.0944854179295196,0.219925371157137,0.199253569807512),chrono.ChQuaternionD(0.00965847056104777,0.707040814908462,-0.707040814908461,0.00965847056104785)))

# Collision shapes 
body_33.GetCollisionModel().ClearModel()
body_33.GetCollisionModel().AddSphere(0.01, chrono.ChVectorD(3.46944695195361E-17,-0.1,0))
body_33.GetCollisionModel().BuildModel()
body_33.SetCollide(True)

exported_items.append(body_33)



# Rigid body part
body_34= chrono.ChBodyAuxRef()
body_34.SetName('Spibot-LEG-2/upper_limb_con-1')
body_34.SetPos(chrono.ChVectorD(-0.00468541792952171,0.230461783385397,-0.299189906392774))
body_34.SetRot(chrono.ChQuaternionD(-0.473053335749247,0.52556687636923,0.47305333574925,-0.525566876369229))
body_34.SetMass(0.0769386604687246)
body_34.SetInertiaXX(chrono.ChVectorD(1.51981435130051e-05,0.000288160004086944,0.000279898353184369))
body_34.SetInertiaXY(chrono.ChVectorD(2.91113998073682e-05,1.19397802863133e-05,-1.25921502363168e-06))
body_34.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-0.00433891891647107,-0.0160004109829567,1.89023205931516e-19),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_8_1_shape = chrono.ChObjShapeFile() 
body_8_1_shape.SetFilename(shapes_dir +'body_8_1.obj') 
body_8_1_level = chrono.ChAssetLevel() 
body_8_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_8_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_8_1_level.GetAssets().push_back(body_8_1_shape) 
body_34.GetAssets().push_back(body_8_1_level) 

# Auxiliary marker (coordinate system feature)
marker_34_1 =chrono.ChMarker()
marker_34_1.SetName('UL-LL-Ref')
body_34.AddMarker(marker_34_1)
marker_34_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.0046854179295213,0.219973566770793,-0.398638372003085),chrono.ChQuaternionD(0.706131123818923,-0.0371326806765027,-0.706131123818926,0.0371326806765045)))

# Auxiliary marker (coordinate system feature)
marker_34_2 =chrono.ChMarker()
marker_34_2.SetName('UL-LB-Ref')
body_34.AddMarker(marker_34_2)
marker_34_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.00468541792952211,0.24095,-0.199741440782464),chrono.ChQuaternionD(0.706131123818923,-0.0371326806765027,-0.706131123818926,0.0371326806765045)))

exported_items.append(body_34)



# Rigid body part
body_35= chrono.ChBodyAuxRef()
body_35.SetName('Spibot-LEG-2/Actuator_rod-1')
body_35.SetPos(chrono.ChVectorD(-0.00473541792952059,0.184061266467541,-0.30406807015189))
body_35.SetRot(chrono.ChQuaternionD(-4.07363955450495e-16,-4.25114099730213e-16,0.999772762428254,-0.0213172115103763))
body_35.SetMass(0.00140945245841084)
body_35.SetInertiaXX(chrono.ChVectorD(2.33089158373325e-06,2.32277598573903e-06,2.77440862465437e-08))
body_35.SetInertiaXY(chrono.ChVectorD(7.83148663887013e-23,1.75687046812201e-21,-9.80926610168644e-08))
body_35.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-1.65060230227876e-19,-2.34447212110501e-18,0.0545976735175364),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_5_1_shape = chrono.ChObjShapeFile() 
body_5_1_shape.SetFilename(shapes_dir +'body_5_1.obj') 
body_5_1_level = chrono.ChAssetLevel() 
body_5_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_5_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_5_1_level.GetAssets().push_back(body_5_1_shape) 
body_35.GetAssets().push_back(body_5_1_level) 

# Auxiliary marker (coordinate system feature)
marker_35_1 =chrono.ChMarker()
marker_35_1.SetName('UL-Act-Shaft')
body_35.AddMarker(marker_35_1)
marker_35_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.00473541792952064,0.181690265589953,-0.359642515536783),chrono.ChQuaternionD(0.999772762428254,-0.0213172115103763,4.07363955450495E-16,4.25114099730213E-16)))

# Auxiliary marker (coordinate system feature)
marker_35_2 =chrono.ChMarker()
marker_35_2.SetName('LL-Act-Shaft')
body_35.AddMarker(marker_35_2)
marker_35_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.00473541792952067,0.179985276194833,-0.399606161656257),chrono.ChQuaternionD(0.999772762428254,-0.0213172115103763,4.07363955450495E-16,4.25114099730213E-16)))

exported_items.append(body_35)



# Rigid body part
body_36= chrono.ChBodyAuxRef()
body_36.SetName('Spibot-LEG-2/Actuator_body-1')
body_36.SetPos(chrono.ChVectorD(-0.00473541792952026,0.184002740205287,-0.305439880932714))
body_36.SetRot(chrono.ChQuaternionD(0.0213172115103764,0.999772762428254,3.6106597174907e-16,-6.58586550694684e-16))
body_36.SetMass(0.00204159144576871)
body_36.SetInertiaXX(chrono.ChVectorD(8.08481090947277e-07,8.00172218348168e-07,8.7336479446564e-08))
body_36.SetInertiaXY(chrono.ChVectorD(5.27591876181283e-23,-1.11952840016443e-21,3.04675305437994e-08))
body_36.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-4.17192939730159e-18,5.58956732701871e-20,-0.0175577824053523),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_4_1_shape = chrono.ChObjShapeFile() 
body_4_1_shape.SetFilename(shapes_dir +'body_4_1.obj') 
body_4_1_shape.SetColor(chrono.ChColor(0.752941176470588,0.752941176470588,0.752941176470588)) 
body_4_1_shape.SetFading(0.75) 
body_4_1_level = chrono.ChAssetLevel() 
body_4_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_4_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_4_1_level.GetAssets().push_back(body_4_1_shape) 
body_36.GetAssets().push_back(body_4_1_level) 

# Auxiliary marker (coordinate system feature)
marker_36_1 =chrono.ChMarker()
marker_36_1.SetName('LL-Act-Base')
body_36.AddMarker(marker_36_1)
marker_36_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.00473541792952019,0.186133976949187,-0.255485323283372),chrono.ChQuaternionD(0.0213172115103764,0.999772762428254,3.6106597174907E-16,-6.58586550694684E-16)))

# Auxiliary marker (coordinate system feature)
marker_36_2 =chrono.ChMarker()
marker_36_2.SetName('UL-Act-Base')
body_36.AddMarker(marker_36_2)
marker_36_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.00473541792952021,0.185707729600407,-0.26547623481324),chrono.ChQuaternionD(0.0213172115103764,0.999772762428254,3.6106597174907E-16,-6.58586550694684E-16)))

exported_items.append(body_36)



# Rigid body part
body_37= chrono.ChBodyAuxRef()
body_37.SetName('Spibot-LEG-2/Actuator_rod-2')
body_37.SetPos(chrono.ChVectorD(-0.00458541792952327,0.203107558750528,-0.185770304692669))
body_37.SetRot(chrono.ChQuaternionD(-0.0603233675631642,0.998178887437437,1.53293735686641e-16,-4.54163487044733e-16))
body_37.SetMass(0.00140945245841084)
body_37.SetInertiaXX(chrono.ChVectorD(2.33089158373325e-06,2.29355549039134e-06,5.69645815942349e-08))
body_37.SetInertiaXY(chrono.ChVectorD(-2.25717041044552e-22,-1.87314454639542e-21,-2.75373022896086e-07))
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
marker_37_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.00458541792952332,0.209806311951703,-0.240990476102668),chrono.ChQuaternionD(-1.53293735686641E-16,4.54163487044733E-16,-0.0603233675631642,0.998178887437437)))

# Auxiliary marker (coordinate system feature)
marker_37_2 =chrono.ChMarker()
marker_37_2.SetName('LL-Act-Shaft')
body_37.AddMarker(marker_37_2)
marker_37_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.00458541792952336,0.214623392905358,-0.280699363408735),chrono.ChQuaternionD(-1.53293735686641E-16,4.54163487044733E-16,-0.0603233675631642,0.998178887437437)))

exported_items.append(body_37)



# Rigid body part
body_38= chrono.ChBodyAuxRef()
body_38.SetName('Spibot-LEG-2/limb_body_connector-1')
body_38.SetPos(chrono.ChVectorD(0.00541458207048051,0.23095,-0.139741440782467))
body_38.SetRot(chrono.ChQuaternionD(-0.5,0.499999999999999,0.500000000000001,-0.5))
body_38.SetMass(0.0319301494979552)
body_38.SetInertiaXX(chrono.ChVectorD(2.21101734329624e-06,4.6562762681289e-06,4.83154745183424e-06))
body_38.SetInertiaXY(chrono.ChVectorD(-1.18371000549862e-21,4.9054649499014e-21,-2.35151348809742e-22))
body_38.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(0.01,0.00875766097763167,0.01),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_2_1_shape = chrono.ChObjShapeFile() 
body_2_1_shape.SetFilename(shapes_dir +'body_2_1.obj') 
body_2_1_level = chrono.ChAssetLevel() 
body_2_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_2_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_2_1_level.GetAssets().push_back(body_2_1_shape) 
body_38.GetAssets().push_back(body_2_1_level) 

# Auxiliary marker (coordinate system feature)
marker_38_1 =chrono.ChMarker()
marker_38_1.SetName('LB-UL-Ref')
body_38.AddMarker(marker_38_1)
marker_38_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.00458541792951952,0.24095,-0.199741440782467),chrono.ChQuaternionD(0.500000000000001,-0.499999999999999,-0.5,-0.5)))

# Auxiliary marker (coordinate system feature)
marker_38_2 =chrono.ChMarker()
marker_38_2.SetName('LB-B-Act-1')
body_38.AddMarker(marker_38_2)
marker_38_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.00458541792951951,0.24095,-0.139741440782467),chrono.ChQuaternionD(0.707106781186548,-0.707106781186547,-5.69158516272868E-16,6.77102372807378E-16)))

exported_items.append(body_38)



# Rigid body part
body_39= chrono.ChBodyAuxRef()
body_39.SetName('Spibot-LEG-2/Actuator_body-2')
body_39.SetPos(chrono.ChVectorD(-0.00458541792951916,0.204767080953654,-0.199450328088534))
body_39.SetRot(chrono.ChQuaternionD(-0.0603233675631642,0.998178887437437,2.28795512340495e-16,-1.25051751565981e-16))
body_39.SetMass(0.00204159144576871)
body_39.SetInertiaXX(chrono.ChVectorD(8.08481090947278e-07,7.91096347377987e-07,9.64123504167446e-08))
body_39.SetInertiaXY(chrono.ChVectorD(-3.49680014955984e-23,-3.16779661527629e-22,-8.55307206375246e-08))
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
marker_39_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.00458541792951915,0.198745729761586,-0.14981421895595),chrono.ChQuaternionD(-0.0603233675631642,0.998178887437437,2.28795512340495E-16,-1.25051751565981E-16)))

# Auxiliary marker (coordinate system feature)
marker_39_2 =chrono.ChMarker()
marker_39_2.SetName('UL-Act-Base')
body_39.AddMarker(marker_39_2)
marker_39_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.00458541792951915,0.19995,-0.159741440782467),chrono.ChQuaternionD(-0.0603233675631642,0.998178887437437,2.28795512340495E-16,-1.25051751565981E-16)))

exported_items.append(body_39)



# Rigid body part
body_40= chrono.ChBodyAuxRef()
body_40.SetName('Spibot-LEG-2/limb_body_connector-2')
body_40.SetPos(chrono.ChVectorD(0.00541458207048062,0.18995,-0.139741440782467))
body_40.SetRot(chrono.ChQuaternionD(0.499999999999999,-0.5,-0.5,0.500000000000001))
body_40.SetMass(0.0319301494979552)
body_40.SetInertiaXX(chrono.ChVectorD(2.21101734329624e-06,4.6562762681289e-06,4.83154745183424e-06))
body_40.SetInertiaXY(chrono.ChVectorD(1.78954801011537e-21,4.84409689084208e-21,-5.42274130830099e-22))
body_40.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(0.01,0.00875766097763167,0.01),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_2_1_shape = chrono.ChObjShapeFile() 
body_2_1_shape.SetFilename(shapes_dir +'body_2_1.obj') 
body_2_1_level = chrono.ChAssetLevel() 
body_2_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_2_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_2_1_level.GetAssets().push_back(body_2_1_shape) 
body_40.GetAssets().push_back(body_2_1_level) 

# Auxiliary marker (coordinate system feature)
marker_40_1 =chrono.ChMarker()
marker_40_1.SetName('LB-UL-Ref')
body_40.AddMarker(marker_40_1)
marker_40_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.00458541792951939,0.19995,-0.159741440782467),chrono.ChQuaternionD(0.5,-0.5,-0.500000000000001,-0.5)))

# Auxiliary marker (coordinate system feature)
marker_40_2 =chrono.ChMarker()
marker_40_2.SetName('LB-B-Act-1')
body_40.AddMarker(marker_40_2)
marker_40_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.0045854179295194,0.19995,-0.139741440782467),chrono.ChQuaternionD(0.707106781186547,-0.707106781186548,-6.47663139207057E-16,5.88784672006416E-16)))

exported_items.append(body_40)



# Rigid body part
body_41= chrono.ChBodyAuxRef()
body_41.SetName('Spibot-LEG-2/lower_limb-1')
body_41.SetPos(chrono.ChVectorD(-0.00468541792954347,0.119986783385396,-0.400264148199792))
body_41.SetRot(chrono.ChQuaternionD(0.999966957917602,0.008129149587611,-3.19199666601418e-16,6.66155825950785e-16))
body_41.SetMass(0.173763895224452)
body_41.SetInertiaXX(chrono.ChVectorD(0.000660134295478084,8.93030524396933e-06,0.000660481849626773))
body_41.SetInertiaXY(chrono.ChVectorD(-7.09372683780816e-11,-5.58394364494375e-12,1.05923171571601e-05))
body_41.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(4.14273289964873e-09,-0.0143933772184335,3.59893950746433e-07),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_9_1_shape = chrono.ChObjShapeFile() 
body_9_1_shape.SetFilename(shapes_dir +'body_9_1.obj') 
body_9_1_shape.SetColor(chrono.ChColor(0.898039215686275,0.917647058823529,0.929411764705882)) 
body_9_1_shape.SetFading(0.75) 
body_9_1_level = chrono.ChAssetLevel() 
body_9_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_9_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_9_1_level.GetAssets().push_back(body_9_1_shape) 
body_41.GetAssets().push_back(body_9_1_level) 

# Auxiliary marker (coordinate system feature)
marker_41_1 =chrono.ChMarker()
marker_41_1.SetName('LowerLimbCenterRef')
body_41.AddMarker(marker_41_1)
marker_41_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.00468541792954347,0.119986783385396,-0.400264148199792),chrono.ChQuaternionD(0.70708341690602,0.00574817679867977,0.00574817679867929,-0.707083416906019)))

# Auxiliary marker (coordinate system feature)
marker_41_2 =chrono.ChMarker()
marker_41_2.SetName('LL-UL-Ref')
body_41.AddMarker(marker_41_2)
marker_41_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(-0.0046854179295436,0.219973566770793,-0.398638372003076),chrono.ChQuaternionD(0.70708341690602,0.00574817679867977,0.00574817679867929,-0.707083416906019)))

# Collision shapes 
body_41.GetCollisionModel().ClearModel()
body_41.GetCollisionModel().AddSphere(0.01, chrono.ChVectorD(3.46944695195361E-17,-0.1,0))
body_41.GetCollisionModel().BuildModel()
body_41.SetCollide(True)

exported_items.append(body_41)



# Rigid body part
body_42= chrono.ChBodyAuxRef()
body_42.SetName('Spibot-LEG-3/Actuator_body-2')
body_42.SetPos(chrono.ChVectorD(0.0854145820705982,0.203949335899039,-0.199440263280939))
body_42.SetRot(chrono.ChQuaternionD(-0.0613573041433675,0.998115865632973,6.60439277210714e-16,-3.75407589151353e-16))
body_42.SetMass(0.00204159144576871)
body_42.SetInertiaXX(chrono.ChVectorD(8.08481090947278e-07,7.90738976939168e-07,9.67697208555643e-08))
body_42.SetInertiaXY(chrono.ChVectorD(2.83868701401142e-23,-5.46110204995743e-22,-8.69691668580235e-08))
body_42.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-4.17192939730159e-18,5.58956732701871e-20,-0.0175577824053523),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_4_1_shape = chrono.ChObjShapeFile() 
body_4_1_shape.SetFilename(shapes_dir +'body_4_1.obj') 
body_4_1_shape.SetColor(chrono.ChColor(0.843137254901961,0.843137254901961,0)) 
body_4_1_shape.SetFading(0.75) 
body_4_1_level = chrono.ChAssetLevel() 
body_4_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_4_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_4_1_level.GetAssets().push_back(body_4_1_shape) 
body_42.GetAssets().push_back(body_4_1_level) 

# Auxiliary marker (coordinate system feature)
marker_42_1 =chrono.ChMarker()
marker_42_1.SetName('LL-Act-Base')
body_42.AddMarker(marker_42_1)
marker_42_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(0.0854145820705982,0.197825166025243,-0.149816735158113),chrono.ChQuaternionD(-0.0613573041433675,0.998115865632973,6.60439277210714E-16,-3.75407589151353E-16)))

# Auxiliary marker (coordinate system feature)
marker_42_2 =chrono.ChMarker()
marker_42_2.SetName('UL-Act-Base')
body_42.AddMarker(marker_42_2)
marker_42_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(0.0854145820705982,0.199050000000002,-0.159741440782678),chrono.ChQuaternionD(-0.0613573041433675,0.998115865632973,6.60439277210714E-16,-3.75407589151353E-16)))

exported_items.append(body_42)



# Rigid body part
body_43= chrono.ChBodyAuxRef()
body_43.SetName('Spibot-LEG-3/Actuator_rod-2')
body_43.SetPos(chrono.ChVectorD(0.0854145820706589,0.202281481020655,-0.185925804151375))
body_43.SetRot(chrono.ChQuaternionD(-0.0613573041433672,0.998115865632973,3.74221866986509e-16,-2.45468345179992e-16))
body_43.SetMass(0.00140945245841084)
body_43.SetInertiaXX(chrono.ChVectorD(2.33089158373325e-06,2.29240490756803e-06,5.81151644175515e-08))
body_43.SetInertiaXY(chrono.ChVectorD(-1.02469023743301e-22,-8.55927013294124e-22,-2.80004216004943e-07))
body_43.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-1.65060230227876e-19,-2.34447212110501e-18,0.0545976735175364),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_5_1_shape = chrono.ChObjShapeFile() 
body_5_1_shape.SetFilename(shapes_dir +'body_5_1.obj') 
body_5_1_level = chrono.ChAssetLevel() 
body_5_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_5_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_5_1_level.GetAssets().push_back(body_5_1_shape) 
body_43.GetAssets().push_back(body_5_1_level) 

# Auxiliary marker (coordinate system feature)
marker_43_1 =chrono.ChMarker()
marker_43_1.SetName('UL-Act-Shaft')
body_43.AddMarker(marker_43_1)
marker_43_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(0.0854145820706589,0.209094620005254,-0.241131979188019),chrono.ChQuaternionD(-3.74221866986509E-16,2.45468345179992E-16,-0.0613573041433672,0.998115865632973)))

# Auxiliary marker (coordinate system feature)
marker_43_2 =chrono.ChMarker()
marker_43_2.SetName('LL-Act-Shaft')
body_43.AddMarker(marker_43_2)
marker_43_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(0.0854145820706588,0.213993955904291,-0.280830801686279),chrono.ChQuaternionD(-3.74221866986509E-16,2.45468345179992E-16,-0.0613573041433672,0.998115865632973)))

exported_items.append(body_43)



# Rigid body part
body_44= chrono.ChBodyAuxRef()
body_44.SetName('Spibot-LEG-3/limb_body_connector-1')
body_44.SetPos(chrono.ChVectorD(0.0954145820704804,0.23005,-0.139741440782467))
body_44.SetRot(chrono.ChQuaternionD(0.5,-0.5,-0.5,0.5))
body_44.SetMass(0.0319301494979552)
body_44.SetInertiaXX(chrono.ChVectorD(2.21101734329625e-06,4.6562762681289e-06,4.83154745183424e-06))
body_44.SetInertiaXY(chrono.ChVectorD(-1.15770396578399e-21,2.09155893330209e-21,-2.05962833254296e-22))
body_44.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(0.01,0.00875766097763167,0.01),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_2_1_shape = chrono.ChObjShapeFile() 
body_2_1_shape.SetFilename(shapes_dir +'body_2_1.obj') 
body_2_1_level = chrono.ChAssetLevel() 
body_2_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_2_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_2_1_level.GetAssets().push_back(body_2_1_shape) 
body_44.GetAssets().push_back(body_2_1_level) 

# Auxiliary marker (coordinate system feature)
marker_44_1 =chrono.ChMarker()
marker_44_1.SetName('LB-UL-Ref')
body_44.AddMarker(marker_44_1)
marker_44_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(0.0854145820704803,0.24005,-0.199741440782467),chrono.ChQuaternionD(0.5,-0.5,-0.5,-0.5)))

# Auxiliary marker (coordinate system feature)
marker_44_2 =chrono.ChMarker()
marker_44_2.SetName('LB-B-Act-1')
body_44.AddMarker(marker_44_2)
marker_44_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(0.0854145820704804,0.24005,-0.139741440782467),chrono.ChQuaternionD(0.707106781186548,-0.707106781186547,-1.47196168001604E-16,3.92523114670944E-16)))

exported_items.append(body_44)



# Rigid body part
body_45= chrono.ChBodyAuxRef()
body_45.SetName('Spibot-LEG-3/limb_body_connector-2')
body_45.SetPos(chrono.ChVectorD(0.0954145820704804,0.18905,-0.139741440782467))
body_45.SetRot(chrono.ChQuaternionD(0.5,-0.5,-0.5,0.5))
body_45.SetMass(0.0319301494979552)
body_45.SetInertiaXX(chrono.ChVectorD(2.21101734329625e-06,4.6562762681289e-06,4.83154745183424e-06))
body_45.SetInertiaXY(chrono.ChVectorD(1.81555404983e-21,2.22566131394197e-21,-2.54610359180035e-22))
body_45.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(0.01,0.00875766097763167,0.01),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_2_1_shape = chrono.ChObjShapeFile() 
body_2_1_shape.SetFilename(shapes_dir +'body_2_1.obj') 
body_2_1_level = chrono.ChAssetLevel() 
body_2_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_2_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_2_1_level.GetAssets().push_back(body_2_1_shape) 
body_45.GetAssets().push_back(body_2_1_level) 

# Auxiliary marker (coordinate system feature)
marker_45_1 =chrono.ChMarker()
marker_45_1.SetName('LB-UL-Ref')
body_45.AddMarker(marker_45_1)
marker_45_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(0.0854145820704804,0.19905,-0.159741440782467),chrono.ChQuaternionD(0.5,-0.5,-0.5,-0.5)))

# Auxiliary marker (coordinate system feature)
marker_45_2 =chrono.ChMarker()
marker_45_2.SetName('LB-B-Act-1')
body_45.AddMarker(marker_45_2)
marker_45_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(0.0854145820704804,0.19905,-0.139741440782467),chrono.ChQuaternionD(0.707106781186547,-0.707106781186548,-2.55140024536114E-16,2.94392336003208E-16)))

exported_items.append(body_45)



# Rigid body part
body_46= chrono.ChBodyAuxRef()
body_46.SetName('Spibot-LEG-3/upper_limb_con-1')
body_46.SetPos(chrono.ChVectorD(0.0853145820708271,0.230015109783085,-0.299236671715402))
body_46.SetRot(chrono.ChQuaternionD(0.47424969631791,-0.524487583782847,-0.474249696317912,0.524487583782847))
body_46.SetMass(0.0769386604687246)
body_46.SetInertiaXX(chrono.ChVectorD(1.49384760895325e-05,0.000288419671510416,0.000279898353184369))
body_46.SetInertiaXY(chrono.ChVectorD(2.78662316887681e-05,1.19453949297354e-05,-1.20478866770172e-06))
body_46.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-0.00433891891647107,-0.0160004109829567,1.89023205931516e-19),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_8_1_shape = chrono.ChObjShapeFile() 
body_8_1_shape.SetFilename(shapes_dir +'body_8_1.obj') 
body_8_1_level = chrono.ChAssetLevel() 
body_8_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_8_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_8_1_level.GetAssets().push_back(body_8_1_shape) 
body_46.GetAssets().push_back(body_8_1_level) 

# Auxiliary marker (coordinate system feature)
marker_46_1 =chrono.ChMarker()
marker_46_1.SetName('UL-LL-Ref')
body_46.AddMarker(marker_46_1)
marker_46_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(0.0853145820708272,0.219980219566137,-0.398731902648015),chrono.ChQuaternionD(0.706213903383054,-0.0355235508989423,-0.706213903383055,0.0355235508989437)))

# Auxiliary marker (coordinate system feature)
marker_46_2 =chrono.ChMarker()
marker_46_2.SetName('UL-LB-Ref')
body_46.AddMarker(marker_46_2)
marker_46_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(0.085314582070827,0.240050000000033,-0.19974144078279),chrono.ChQuaternionD(0.706213903383054,-0.0355235508989423,-0.706213903383055,0.0355235508989437)))

exported_items.append(body_46)



# Rigid body part
body_47= chrono.ChBodyAuxRef()
body_47.SetName('Spibot-LEG-3/Actuator_rod-1')
body_47.SetPos(chrono.ChVectorD(0.085264582072917,0.183641818915434,-0.304056711733687))
body_47.SetRot(chrono.ChQuaternionD(-2.9148670895373e-16,-7.28716772384326e-16,0.99981760749978,-0.0190984746358225))
body_47.SetMass(0.00140945245841084)
body_47.SetInertiaXX(chrono.ChVectorD(2.33089158373325e-06,2.32360150945019e-06,2.69185625353857e-08))
body_47.SetInertiaXY(chrono.ChVectorD(6.61427126001671e-23,1.24527685518299e-21,-8.79027041966102e-08))
body_47.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-1.65060230227876e-19,-2.34447212110501e-18,0.0545976735175364),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_5_1_shape = chrono.ChObjShapeFile() 
body_5_1_shape.SetFilename(shapes_dir +'body_5_1.obj') 
body_5_1_level = chrono.ChAssetLevel() 
body_5_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_5_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_5_1_level.GetAssets().push_back(body_5_1_shape) 
body_47.GetAssets().push_back(body_5_1_level) 

# Auxiliary marker (coordinate system feature)
marker_47_1 =chrono.ChMarker()
marker_47_1.SetName('UL-Act-Shaft')
body_47.AddMarker(marker_47_1)
marker_47_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(0.085264582072917,0.181517501142512,-0.359641133103344),chrono.ChQuaternionD(0.99981760749978,-0.0190984746358225,2.9148670895373E-16,7.28716772384326E-16)))

# Auxiliary marker (coordinate system feature)
marker_47_2 =chrono.ChMarker()
marker_47_2.SetName('LL-Act-Shaft')
body_47.AddMarker(marker_47_2)
marker_47_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(0.0852645820729169,0.179989901845129,-0.399611952964671),chrono.ChQuaternionD(0.99981760749978,-0.0190984746358225,2.9148670895373E-16,7.28716772384326E-16)))

exported_items.append(body_47)



# Rigid body part
body_48= chrono.ChBodyAuxRef()
body_48.SetName('Spibot-LEG-3/Actuator_body-1')
body_48.SetPos(chrono.ChVectorD(0.085264582074149,0.183579089220438,-0.305698082841388))
body_48.SetRot(chrono.ChQuaternionD(0.0190984746358224,0.99981760749978,5.60841244861822e-16,-2.94653862136816e-16))
body_48.SetMass(0.00204159144576871)
body_48.SetInertiaXX(chrono.ChVectorD(8.08481090947278e-07,8.00428625592335e-07,8.70800722023971e-08))
body_48.SetInertiaXY(chrono.ChVectorD(3.07954664503823e-23,-5.98672011346964e-22,2.73025351461545e-08))
body_48.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-4.17192939730159e-18,5.58956732701871e-20,-0.0175577824053523),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_4_1_shape = chrono.ChObjShapeFile() 
body_4_1_shape.SetFilename(shapes_dir +'body_4_1.obj') 
body_4_1_shape.SetColor(chrono.ChColor(0.752941176470588,0.752941176470588,0.752941176470588)) 
body_4_1_shape.SetFading(0.75) 
body_4_1_level = chrono.ChAssetLevel() 
body_4_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_4_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_4_1_level.GetAssets().push_back(body_4_1_shape) 
body_48.GetAssets().push_back(body_4_1_level) 

# Auxiliary marker (coordinate system feature)
marker_48_1 =chrono.ChMarker()
marker_48_1.SetName('LL-Act-Base')
body_48.AddMarker(marker_48_1)
marker_48_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(0.085264582074149,0.185488588342167,-0.255734558014729),chrono.ChQuaternionD(0.0190984746358224,0.99981760749978,5.60841244861822E-16,-2.94653862136816E-16)))

# Auxiliary marker (coordinate system feature)
marker_48_2 =chrono.ChMarker()
marker_48_2.SetName('UL-Act-Base')
body_48.AddMarker(marker_48_2)
marker_48_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(0.085264582074149,0.185106688517821,-0.265727262980061),chrono.ChQuaternionD(0.0190984746358224,0.99981760749978,5.60841244861822E-16,-2.94653862136816E-16)))

exported_items.append(body_48)



# Rigid body part
body_49= chrono.ChBodyAuxRef()
body_49.SetName('Spibot-LEG-3/lower_limb-1')
body_49.SetPos(chrono.ChVectorD(0.0853145820721626,0.119990109767233,-0.400138297179064))
body_49.SetRot(chrono.ChQuaternionD(0.999975274152147,0.00703214649573876,2.91440750083748e-16,6.6615028590571e-16))
body_49.SetMass(0.173763895224452)
body_49.SetInertiaXX(chrono.ChVectorD(0.000660134295478084,8.88696136174702e-06,0.000660525193508996))
body_49.SetInertiaXY(chrono.ChVectorD(-7.092484609592e-11,-5.7395712170536e-12,9.16267049850927e-06))
body_49.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(4.14273289964873e-09,-0.0143933772184335,3.59893950746433e-07),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_9_1_shape = chrono.ChObjShapeFile() 
body_9_1_shape.SetFilename(shapes_dir +'body_9_1.obj') 
body_9_1_shape.SetColor(chrono.ChColor(0.898039215686275,0.917647058823529,0.929411764705882)) 
body_9_1_shape.SetFading(0.75) 
body_9_1_level = chrono.ChAssetLevel() 
body_9_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_9_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_9_1_level.GetAssets().push_back(body_9_1_shape) 
body_49.GetAssets().push_back(body_9_1_level) 

# Auxiliary marker (coordinate system feature)
marker_49_1 =chrono.ChMarker()
marker_49_1.SetName('LowerLimbCenterRef')
body_49.AddMarker(marker_49_1)
marker_49_1.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(0.0853145820721626,0.119990109767233,-0.400138297179064),chrono.ChQuaternionD(0.707089297371861,0.0049724784734339,0.00497247847343431,-0.70708929737186)))

# Auxiliary marker (coordinate system feature)
marker_49_2 =chrono.ChMarker()
marker_49_2.SetName('LL-UL-Ref')
body_49.AddMarker(marker_49_2)
marker_49_2.Impose_Abs_Coord(chrono.ChCoordsysD(chrono.ChVectorD(0.0853145820721624,0.219980219550366,-0.398731902655073),chrono.ChQuaternionD(0.707089297371861,0.0049724784734339,0.00497247847343431,-0.70708929737186)))

# Collision shapes 
body_49.GetCollisionModel().ClearModel()
body_49.GetCollisionModel().AddSphere(0.01, chrono.ChVectorD(3.46944695195361E-17,-0.1,0))
body_49.GetCollisionModel().BuildModel()
body_49.SetCollide(True)

exported_items.append(body_49)




# Mate constraint: Concentric1 [MateConcentric] type:1 align:1 flip:False
#   Entity 0: C::E name: body_1 , SW name: body-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_3 , SW name: Spibot-LEG-1/limb_body_connector-2 ,  SW ref.type:2 (2)

link_1 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.0945854179295196,0.23,-0.139741440782467)
dA = chrono.ChVectorD(-7.61150456358265e-17,-1,2.46519032881566e-32)
cB = chrono.ChVectorD(-0.0945854179295196,0.18995,-0.139741440782467)
dB = chrono.ChVectorD(-1.66533453693774e-16,1,-1.2490009027033e-15)
link_1.SetFlipped(True)
link_1.Initialize(body_1,body_3,False,cA,cB,dA,dB)
link_1.SetName("Concentric1")
exported_items.append(link_1)

link_2 = chrono.ChLinkMateGeneric()
link_2.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.0945854179295196,0.23,-0.139741440782467)
cB = chrono.ChVectorD(-0.0945854179295196,0.18995,-0.139741440782467)
dA = chrono.ChVectorD(-7.61150456358265e-17,-1,2.46519032881566e-32)
dB = chrono.ChVectorD(-1.66533453693774e-16,1,-1.2490009027033e-15)
link_2.Initialize(body_1,body_3,False,cA,cB,dA,dB)
link_2.SetName("Concentric1")
exported_items.append(link_2)


# Mate constraint: Distance1 [MateDistanceDim] type:5 align:1 flip:False
#   Entity 0: C::E name: body_3 , SW name: Spibot-LEG-1/limb_body_connector-2 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_1 , SW name: body-1 ,  SW ref.type:2 (2)

link_3 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(-0.10458541792952,0.20995,-0.139741440782467)
cB = chrono.ChVectorD(-0.00458541792951962,0.21,-0.099741440782467)
dA = chrono.ChVectorD(-1.66533453693774e-16,1,-1.2490009027033e-15)
dB = chrono.ChVectorD(-7.61150456358265e-17,-1,2.46519032881566e-32)
link_3.Initialize(body_3,body_1,False,cA,cB,dB)
link_3.SetDistance(-5E-05)
link_3.SetName("Distance1")
exported_items.append(link_3)

link_4 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.10458541792952,0.20995,-0.139741440782467)
dA = chrono.ChVectorD(-1.66533453693774e-16,1,-1.2490009027033e-15)
cB = chrono.ChVectorD(-0.00458541792951962,0.21,-0.099741440782467)
dB = chrono.ChVectorD(-7.61150456358265e-17,-1,2.46519032881566e-32)
link_4.SetFlipped(True)
link_4.Initialize(body_3,body_1,False,cA,cB,dA,dB)
link_4.SetName("Distance1")
exported_items.append(link_4)


# Mate constraint: Concentric2 [MateConcentric] type:1 align:1 flip:False
#   Entity 0: C::E name: body_1 , SW name: body-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_38 , SW name: Spibot-LEG-2/limb_body_connector-1 ,  SW ref.type:2 (2)

link_5 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.00458541792951963,0.23,-0.139741440782467)
dA = chrono.ChVectorD(-7.61150456358265e-17,-1,2.46519032881566e-32)
cB = chrono.ChVectorD(-0.00458541792951949,0.23095,-0.139741440782467)
dB = chrono.ChVectorD(-1.83186799063151e-15,1,6.10622663543836e-16)
link_5.SetFlipped(True)
link_5.Initialize(body_1,body_38,False,cA,cB,dA,dB)
link_5.SetName("Concentric2")
exported_items.append(link_5)

link_6 = chrono.ChLinkMateGeneric()
link_6.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.00458541792951963,0.23,-0.139741440782467)
cB = chrono.ChVectorD(-0.00458541792951949,0.23095,-0.139741440782467)
dA = chrono.ChVectorD(-7.61150456358265e-17,-1,2.46519032881566e-32)
dB = chrono.ChVectorD(-1.83186799063151e-15,1,6.10622663543836e-16)
link_6.Initialize(body_1,body_38,False,cA,cB,dA,dB)
link_6.SetName("Concentric2")
exported_items.append(link_6)


# Mate constraint: Distance2 [MateDistanceDim] type:5 align:1 flip:False
#   Entity 0: C::E name: body_40 , SW name: Spibot-LEG-2/limb_body_connector-2 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_1 , SW name: body-1 ,  SW ref.type:2 (2)

link_7 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(-0.0145854179295194,0.20995,-0.139741440782467)
cB = chrono.ChVectorD(-0.00458541792951962,0.21,-0.099741440782467)
dA = chrono.ChVectorD(-1.83186799063151e-15,1,-5.55111512312578e-16)
dB = chrono.ChVectorD(-7.61150456358265e-17,-1,2.46519032881566e-32)
link_7.Initialize(body_40,body_1,False,cA,cB,dB)
link_7.SetDistance(-5E-05)
link_7.SetName("Distance2")
exported_items.append(link_7)

link_8 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.0145854179295194,0.20995,-0.139741440782467)
dA = chrono.ChVectorD(-1.83186799063151e-15,1,-5.55111512312578e-16)
cB = chrono.ChVectorD(-0.00458541792951962,0.21,-0.099741440782467)
dB = chrono.ChVectorD(-7.61150456358265e-17,-1,2.46519032881566e-32)
link_8.SetFlipped(True)
link_8.Initialize(body_40,body_1,False,cA,cB,dA,dB)
link_8.SetName("Distance2")
exported_items.append(link_8)


# Mate constraint: Concentric3 [MateConcentric] type:1 align:1 flip:False
#   Entity 0: C::E name: body_1 , SW name: body-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_10 , SW name: Spibot-LEG-4/limb_body_connector-1 ,  SW ref.type:2 (2)

link_9 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.0854145820704804,0.23,-0.059741440782467)
dA = chrono.ChVectorD(-7.61150456358265e-17,-1,2.46519032881566e-32)
cB = chrono.ChVectorD(0.0854145820704803,0.23005,-0.059741440782467)
dB = chrono.ChVectorD(0,1,0)
link_9.SetFlipped(True)
link_9.Initialize(body_1,body_10,False,cA,cB,dA,dB)
link_9.SetName("Concentric3")
exported_items.append(link_9)

link_10 = chrono.ChLinkMateGeneric()
link_10.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(0.0854145820704804,0.23,-0.059741440782467)
cB = chrono.ChVectorD(0.0854145820704803,0.23005,-0.059741440782467)
dA = chrono.ChVectorD(-7.61150456358265e-17,-1,2.46519032881566e-32)
dB = chrono.ChVectorD(0,1,0)
link_10.Initialize(body_1,body_10,False,cA,cB,dA,dB)
link_10.SetName("Concentric3")
exported_items.append(link_10)


# Mate constraint: Concentric4 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_1 , SW name: body-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_44 , SW name: Spibot-LEG-3/limb_body_connector-1 ,  SW ref.type:1 (1)

link_11 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.0854145820704804,0.23,-0.139741440782467)
dA = chrono.ChVectorD(-7.61150456358265e-17,-1,2.46519032881566e-32)
cB = chrono.ChVectorD(0.0854145820704804,0.25005,-0.139741440782467)
dB = chrono.ChVectorD(8.04911692853238e-16,-1,-4.9960036108132e-16)
link_11.Initialize(body_44,body_1,False,cB,cA,dB,dA)
link_11.SetName("Concentric4")
exported_items.append(link_11)

link_12 = chrono.ChLinkMateGeneric()
link_12.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(0.0854145820704804,0.23,-0.139741440782467)
cB = chrono.ChVectorD(0.0854145820704804,0.25005,-0.139741440782467)
dA = chrono.ChVectorD(-7.61150456358265e-17,-1,2.46519032881566e-32)
dB = chrono.ChVectorD(8.04911692853238e-16,-1,-4.9960036108132e-16)
link_12.Initialize(body_44,body_1,False,cB,cA,dB,dA)
link_12.SetName("Concentric4")
exported_items.append(link_12)


# Mate constraint: Concentric5 [MateConcentric] type:1 align:1 flip:False
#   Entity 0: C::E name: body_1 , SW name: body-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_21 , SW name: Spibot-LEG-5/limb_body_connector-1 ,  SW ref.type:2 (2)

link_13 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.00458541792951963,0.23,-0.059741440782467)
dA = chrono.ChVectorD(-7.61150456358265e-17,-1,2.46519032881566e-32)
cB = chrono.ChVectorD(-0.00458541792951962,0.23005,-0.059741440782467)
dB = chrono.ChVectorD(-2.77555756156289e-17,1,1.66533453693774e-16)
link_13.SetFlipped(True)
link_13.Initialize(body_1,body_21,False,cA,cB,dA,dB)
link_13.SetName("Concentric5")
exported_items.append(link_13)

link_14 = chrono.ChLinkMateGeneric()
link_14.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.00458541792951963,0.23,-0.059741440782467)
cB = chrono.ChVectorD(-0.00458541792951962,0.23005,-0.059741440782467)
dA = chrono.ChVectorD(-7.61150456358265e-17,-1,2.46519032881566e-32)
dB = chrono.ChVectorD(-2.77555756156289e-17,1,1.66533453693774e-16)
link_14.Initialize(body_1,body_21,False,cA,cB,dA,dB)
link_14.SetName("Concentric5")
exported_items.append(link_14)


# Mate constraint: Concentric6 [MateConcentric] type:1 align:1 flip:False
#   Entity 0: C::E name: body_1 , SW name: body-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_26 , SW name: Spibot-LEG-6/limb_body_connector-1 ,  SW ref.type:2 (2)

link_15 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.0945854179295196,0.23,-0.059741440782467)
dA = chrono.ChVectorD(-7.61150456358265e-17,-1,2.46519032881566e-32)
cB = chrono.ChVectorD(-0.0945854179295196,0.22995,-0.059741440782467)
dB = chrono.ChVectorD(-1.94289029309402e-16,1,1.36002320516582e-15)
link_15.SetFlipped(True)
link_15.Initialize(body_1,body_26,False,cA,cB,dA,dB)
link_15.SetName("Concentric6")
exported_items.append(link_15)

link_16 = chrono.ChLinkMateGeneric()
link_16.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.0945854179295196,0.23,-0.059741440782467)
cB = chrono.ChVectorD(-0.0945854179295196,0.22995,-0.059741440782467)
dA = chrono.ChVectorD(-7.61150456358265e-17,-1,2.46519032881566e-32)
dB = chrono.ChVectorD(-1.94289029309402e-16,1,1.36002320516582e-15)
link_16.Initialize(body_1,body_26,False,cA,cB,dA,dB)
link_16.SetName("Concentric6")
exported_items.append(link_16)


# Mate constraint: Distance3 [MateDistanceDim] type:5 align:1 flip:True
#   Entity 0: C::E name: body_26 , SW name: Spibot-LEG-6/limb_body_connector-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_1 , SW name: body-1 ,  SW ref.type:2 (2)

link_17 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(-0.0845854179295196,0.22995,-0.059741440782467)
cB = chrono.ChVectorD(-0.00458541792951962,0.23,-0.099741440782467)
dA = chrono.ChVectorD(1.94289029309402e-16,-1,-1.36002320516582e-15)
dB = chrono.ChVectorD(7.61150456358265e-17,1,-2.46519032881566e-32)
link_17.Initialize(body_26,body_1,False,cA,cB,dB)
link_17.SetDistance(5E-05)
link_17.SetName("Distance3")
exported_items.append(link_17)

link_18 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.0845854179295196,0.22995,-0.059741440782467)
dA = chrono.ChVectorD(1.94289029309402e-16,-1,-1.36002320516582e-15)
cB = chrono.ChVectorD(-0.00458541792951962,0.23,-0.099741440782467)
dB = chrono.ChVectorD(7.61150456358265e-17,1,-2.46519032881566e-32)
link_18.SetFlipped(True)
link_18.Initialize(body_26,body_1,False,cA,cB,dA,dB)
link_18.SetName("Distance3")
exported_items.append(link_18)


# Mate constraint: Distance4 [MateDistanceDim] type:5 align:1 flip:False
#   Entity 0: C::E name: body_21 , SW name: Spibot-LEG-5/limb_body_connector-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_1 , SW name: body-1 ,  SW ref.type:2 (2)

link_19 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(0.00541458207048038,0.23005,-0.059741440782467)
cB = chrono.ChVectorD(-0.00458541792951962,0.23,-0.099741440782467)
dA = chrono.ChVectorD(2.77555756156289e-17,-1,-1.66533453693774e-16)
dB = chrono.ChVectorD(7.61150456358265e-17,1,-2.46519032881566e-32)
link_19.Initialize(body_21,body_1,False,cA,cB,dB)
link_19.SetDistance(-5E-05)
link_19.SetName("Distance4")
exported_items.append(link_19)

link_20 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.00541458207048038,0.23005,-0.059741440782467)
dA = chrono.ChVectorD(2.77555756156289e-17,-1,-1.66533453693774e-16)
cB = chrono.ChVectorD(-0.00458541792951962,0.23,-0.099741440782467)
dB = chrono.ChVectorD(7.61150456358265e-17,1,-2.46519032881566e-32)
link_20.SetFlipped(True)
link_20.Initialize(body_21,body_1,False,cA,cB,dA,dB)
link_20.SetName("Distance4")
exported_items.append(link_20)


# Mate constraint: Distance5 [MateDistanceDim] type:5 align:1 flip:False
#   Entity 0: C::E name: body_10 , SW name: Spibot-LEG-4/limb_body_connector-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_1 , SW name: body-1 ,  SW ref.type:2 (2)

link_21 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(0.0954145820704804,0.23005,-0.059741440782467)
cB = chrono.ChVectorD(-0.00458541792951962,0.23,-0.099741440782467)
dA = chrono.ChVectorD(0,-1,0)
dB = chrono.ChVectorD(7.61150456358265e-17,1,-2.46519032881566e-32)
link_21.Initialize(body_10,body_1,False,cA,cB,dB)
link_21.SetDistance(-5E-05)
link_21.SetName("Distance5")
exported_items.append(link_21)

link_22 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.0954145820704804,0.23005,-0.059741440782467)
dA = chrono.ChVectorD(0,-1,0)
cB = chrono.ChVectorD(-0.00458541792951962,0.23,-0.099741440782467)
dB = chrono.ChVectorD(7.61150456358265e-17,1,-2.46519032881566e-32)
link_22.SetFlipped(True)
link_22.Initialize(body_10,body_1,False,cA,cB,dA,dB)
link_22.SetName("Distance5")
exported_items.append(link_22)


# Mate constraint: Distance6 [MateDistanceDim] type:5 align:1 flip:False
#   Entity 0: C::E name: body_44 , SW name: Spibot-LEG-3/limb_body_connector-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_1 , SW name: body-1 ,  SW ref.type:2 (2)

link_23 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(0.0754145820704804,0.23005,-0.139741440782467)
cB = chrono.ChVectorD(-0.00458541792951962,0.23,-0.099741440782467)
dA = chrono.ChVectorD(8.04911692853238e-16,-1,-4.9960036108132e-16)
dB = chrono.ChVectorD(7.61150456358265e-17,1,-2.46519032881566e-32)
link_23.Initialize(body_44,body_1,False,cA,cB,dB)
link_23.SetDistance(-5E-05)
link_23.SetName("Distance6")
exported_items.append(link_23)

link_24 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.0754145820704804,0.23005,-0.139741440782467)
dA = chrono.ChVectorD(8.04911692853238e-16,-1,-4.9960036108132e-16)
cB = chrono.ChVectorD(-0.00458541792951962,0.23,-0.099741440782467)
dB = chrono.ChVectorD(7.61150456358265e-17,1,-2.46519032881566e-32)
link_24.SetFlipped(True)
link_24.Initialize(body_44,body_1,False,cA,cB,dA,dB)
link_24.SetName("Distance6")
exported_items.append(link_24)


# Mate constraint: Concentric3 [MateConcentric] type:1 align:1 flip:False
#   Entity 0: C::E name: body_8 , SW name: Spibot-LEG-1/upper_limb_con-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_9 , SW name: Spibot-LEG-1/lower_limb-1 ,  SW ref.type:2 (2)

link_1 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.097135417929517,0.21996873658654,-0.398637862534044)
dA = chrono.ChVectorD(1,1.36002320516582e-15,-4.16333634234434e-15)
cB = chrono.ChVectorD(-0.0846854179295453,0.219968736586566,-0.39863786253404)
dB = chrono.ChVectorD(-1,-4.9960036108132e-16,8.88178419700125e-16)
link_1.SetFlipped(True)
link_1.Initialize(body_8,body_9,False,cA,cB,dA,dB)
link_1.SetName("Concentric3")
exported_items.append(link_1)

link_2 = chrono.ChLinkMateGeneric()
link_2.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.097135417929517,0.21996873658654,-0.398637862534044)
cB = chrono.ChVectorD(-0.0846854179295453,0.219968736586566,-0.39863786253404)
dA = chrono.ChVectorD(1,1.36002320516582e-15,-4.16333634234434e-15)
dB = chrono.ChVectorD(-1,-4.9960036108132e-16,8.88178419700125e-16)
link_2.Initialize(body_8,body_9,False,cA,cB,dA,dB)
link_2.SetName("Concentric3")
exported_items.append(link_2)


# Mate constraint: Concentric4 [MateConcentric] type:1 align:1 flip:False
#   Entity 0: C::E name: body_9 , SW name: Spibot-LEG-1/lower_limb-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_6 , SW name: Spibot-LEG-1/Actuator_rod-1 ,  SW ref.type:2 (2)

link_3 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.0846854179295453,0.17998186388196,-0.399662563127205)
dA = chrono.ChVectorD(-1,-4.9960036108132e-16,8.88178419700125e-16)
cB = chrono.ChVectorD(-0.0971354179295116,0.17998186388193,-0.399662563127203)
dB = chrono.ChVectorD(1,4.71844785465692e-16,-1.49880108324396e-15)
link_3.SetFlipped(True)
link_3.Initialize(body_9,body_6,False,cA,cB,dA,dB)
link_3.SetName("Concentric4")
exported_items.append(link_3)

link_4 = chrono.ChLinkMateGeneric()
link_4.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.0846854179295453,0.17998186388196,-0.399662563127205)
cB = chrono.ChVectorD(-0.0971354179295116,0.17998186388193,-0.399662563127203)
dA = chrono.ChVectorD(-1,-4.9960036108132e-16,8.88178419700125e-16)
dB = chrono.ChVectorD(1,4.71844785465692e-16,-1.49880108324396e-15)
link_4.Initialize(body_9,body_6,False,cA,cB,dA,dB)
link_4.SetName("Concentric4")
exported_items.append(link_4)


# Mate constraint: Concentric6 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_6 , SW name: Spibot-LEG-1/Actuator_rod-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_7 , SW name: Spibot-LEG-1/Actuator_body-1 ,  SW ref.type:2 (2)

link_5 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.0947354179295113,0.184030947904593,-0.30474889225426)
dA = chrono.ChVectorD(1.66533453693773e-15,0.0426219370806572,0.999091272346773)
cB = chrono.ChVectorD(-0.0947354179295057,0.182722868264751,-0.335411293853498)
dB = chrono.ChVectorD(1.60982338570648e-15,0.042621937080657,0.999091272346773)
link_5.Initialize(body_6,body_7,False,cA,cB,dA,dB)
link_5.SetName("Concentric6")
exported_items.append(link_5)

link_6 = chrono.ChLinkMateGeneric()
link_6.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.0947354179295113,0.184030947904593,-0.30474889225426)
cB = chrono.ChVectorD(-0.0947354179295057,0.182722868264751,-0.335411293853498)
dA = chrono.ChVectorD(1.66533453693773e-15,0.0426219370806572,0.999091272346773)
dB = chrono.ChVectorD(1.60982338570648e-15,0.042621937080657,0.999091272346773)
link_6.Initialize(body_6,body_7,False,cA,cB,dA,dB)
link_6.SetName("Concentric6")
exported_items.append(link_6)


# Mate constraint: Concentric11 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_5 , SW name: Spibot-LEG-1/Actuator_rod-2 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_4 , SW name: Spibot-LEG-1/Actuator_body-2 ,  SW ref.type:2 (2)

link_7 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.0945854179295178,0.203182426562587,-0.186389926620584)
dA = chrono.ChVectorD(1.99840144432528e-15,-0.120416066726271,0.992723511796802)
cB = chrono.ChVectorD(-0.094585417929518,0.207174964003576,-0.219304851490275)
dB = chrono.ChVectorD(1.83186799063151e-15,-0.120416066726272,0.992723511796802)
link_7.Initialize(body_5,body_4,False,cA,cB,dA,dB)
link_7.SetName("Concentric11")
exported_items.append(link_7)

link_8 = chrono.ChLinkMateGeneric()
link_8.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.0945854179295178,0.203182426562587,-0.186389926620584)
cB = chrono.ChVectorD(-0.094585417929518,0.207174964003576,-0.219304851490275)
dA = chrono.ChVectorD(1.99840144432528e-15,-0.120416066726271,0.992723511796802)
dB = chrono.ChVectorD(1.83186799063151e-15,-0.120416066726272,0.992723511796802)
link_8.Initialize(body_5,body_4,False,cA,cB,dA,dB)
link_8.SetName("Concentric11")
exported_items.append(link_8)


# Mate constraint: Concentric12 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_8 , SW name: Spibot-LEG-1/upper_limb_con-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_2 , SW name: Spibot-LEG-1/limb_body_connector-1 ,  SW ref.type:2 (2)

link_9 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.0971354179295163,0.240950000000001,-0.199741440782482)
dA = chrono.ChVectorD(1,1.36002320516582e-15,-4.16333634234434e-15)
cB = chrono.ChVectorD(-0.10458541792952,0.24095,-0.199741440782467)
dB = chrono.ChVectorD(1,1.38777878078145e-16,-2.22044604925031e-16)
link_9.Initialize(body_8,body_2,False,cA,cB,dA,dB)
link_9.SetName("Concentric12")
exported_items.append(link_9)

link_10 = chrono.ChLinkMateGeneric()
link_10.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.0971354179295163,0.240950000000001,-0.199741440782482)
cB = chrono.ChVectorD(-0.10458541792952,0.24095,-0.199741440782467)
dA = chrono.ChVectorD(1,1.36002320516582e-15,-4.16333634234434e-15)
dB = chrono.ChVectorD(1,1.38777878078145e-16,-2.22044604925031e-16)
link_10.Initialize(body_8,body_2,False,cA,cB,dA,dB)
link_10.SetName("Concentric12")
exported_items.append(link_10)


# Mate constraint: Concentric13 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_4 , SW name: Spibot-LEG-1/Actuator_body-2 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_3 , SW name: Spibot-LEG-1/limb_body_connector-2 ,  SW ref.type:2 (2)

link_11 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.102185417929518,0.19995,-0.159741440782467)
dA = chrono.ChVectorD(1,7.21644966006352e-16,-1.55431223447522e-15)
cB = chrono.ChVectorD(-0.10458541792952,0.19995,-0.159741440782467)
dB = chrono.ChVectorD(1,1.38777878078145e-16,5.55111512312578e-17)
link_11.Initialize(body_4,body_3,False,cA,cB,dA,dB)
link_11.SetName("Concentric13")
exported_items.append(link_11)

link_12 = chrono.ChLinkMateGeneric()
link_12.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.102185417929518,0.19995,-0.159741440782467)
cB = chrono.ChVectorD(-0.10458541792952,0.19995,-0.159741440782467)
dA = chrono.ChVectorD(1,7.21644966006352e-16,-1.55431223447522e-15)
dB = chrono.ChVectorD(1,1.38777878078145e-16,5.55111512312578e-17)
link_12.Initialize(body_4,body_3,False,cA,cB,dA,dB)
link_12.SetName("Concentric13")
exported_items.append(link_12)


# Mate constraint: Concentric17 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_2 , SW name: Spibot-LEG-1/limb_body_connector-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_3 , SW name: Spibot-LEG-1/limb_body_connector-2 ,  SW ref.type:2 (2)

link_13 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.0945854179295196,0.23095,-0.139741440782467)
dA = chrono.ChVectorD(-1.38777878078145e-16,1,-5.55111512312578e-17)
cB = chrono.ChVectorD(-0.0945854179295196,0.18995,-0.139741440782467)
dB = chrono.ChVectorD(-1.66533453693773e-16,1,-1.2490009027033e-15)
link_13.Initialize(body_2,body_3,False,cA,cB,dA,dB)
link_13.SetName("Concentric17")
exported_items.append(link_13)

link_14 = chrono.ChLinkMateGeneric()
link_14.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.0945854179295196,0.23095,-0.139741440782467)
cB = chrono.ChVectorD(-0.0945854179295196,0.18995,-0.139741440782467)
dA = chrono.ChVectorD(-1.38777878078145e-16,1,-5.55111512312578e-17)
dB = chrono.ChVectorD(-1.66533453693773e-16,1,-1.2490009027033e-15)
link_14.Initialize(body_2,body_3,False,cA,cB,dA,dB)
link_14.SetName("Concentric17")
exported_items.append(link_14)


# Mate constraint: Parallel14 [MateParallel] type:3 align:0 flip:False
#   Entity 0: C::E name: body_8 , SW name: Spibot-LEG-1/upper_limb_con-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_6 , SW name: Spibot-LEG-1/Actuator_rod-1 ,  SW ref.type:2 (2)

link_15 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.0971354179295165,0.23045936829327,-0.299189651658263)
dA = chrono.ChVectorD(-1,-1.36002320516582e-15,4.16333634234434e-15)
cB = chrono.ChVectorD(-0.0971354179295116,0.17998186388193,-0.399662563127203)
dB = chrono.ChVectorD(-1,-4.71844785465692e-16,1.49880108324396e-15)
link_15.Initialize(body_8,body_6,False,cA,cB,dA,dB)
link_15.SetName("Parallel14")
exported_items.append(link_15)


# Mate constraint: Parallel15 [MateParallel] type:3 align:0 flip:False
#   Entity 0: C::E name: body_8 , SW name: Spibot-LEG-1/upper_limb_con-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_5 , SW name: Spibot-LEG-1/Actuator_rod-2 ,  SW ref.type:2 (2)

link_16 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.0922354179295164,0.186132623231202,-0.255483992065765)
dA = chrono.ChVectorD(-1,-1.36002320516582e-15,4.16333634234434e-15)
cB = chrono.ChVectorD(-0.096985417929518,0.209805310232532,-0.240989719769408)
dB = chrono.ChVectorD(-1,-5.27355936696949e-16,1.88737914186277e-15)
link_16.Initialize(body_8,body_5,False,cA,cB,dA,dB)
link_16.SetName("Parallel15")
exported_items.append(link_16)


# Mate constraint: Distance10 [MateDistanceDim] type:5 align:1 flip:False
#   Entity 0: C::E name: body_8 , SW name: Spibot-LEG-1/upper_limb_con-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_9 , SW name: Spibot-LEG-1/lower_limb-1 ,  SW ref.type:2 (2)

link_17 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(-0.0971354179295165,0.23045936829327,-0.299189651658263)
cB = chrono.ChVectorD(-0.0971854179295453,0.230143981136195,-0.408459491643065)
dA = chrono.ChVectorD(-1,-1.36002320516582e-15,4.16333634234434e-15)
dB = chrono.ChVectorD(1,3.60822483003176e-16,-8.88178419700125e-16)
link_17.Initialize(body_8,body_9,False,cA,cB,dB)
link_17.SetDistance(0)
link_17.SetName("Distance10")
exported_items.append(link_17)

link_18 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.0971354179295165,0.23045936829327,-0.299189651658263)
dA = chrono.ChVectorD(-1,-1.36002320516582e-15,4.16333634234434e-15)
cB = chrono.ChVectorD(-0.0971854179295453,0.230143981136195,-0.408459491643065)
dB = chrono.ChVectorD(1,3.60822483003176e-16,-8.88178419700125e-16)
link_18.SetFlipped(True)
link_18.Initialize(body_8,body_9,False,cA,cB,dA,dB)
link_18.SetName("Distance10")
exported_items.append(link_18)


# Mate constraint: Distance11 [MateDistanceDim] type:5 align:1 flip:False
#   Entity 0: C::E name: body_6 , SW name: Spibot-LEG-1/Actuator_rod-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_9 , SW name: Spibot-LEG-1/lower_limb-1 ,  SW ref.type:2 (2)

link_19 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(-0.0971354179295116,0.17998186388193,-0.399662563127203)
cB = chrono.ChVectorD(-0.0971854179295453,0.230143981136195,-0.408459491643065)
dA = chrono.ChVectorD(-1,-4.71844785465692e-16,1.49880108324396e-15)
dB = chrono.ChVectorD(1,3.60822483003176e-16,-8.88178419700125e-16)
link_19.Initialize(body_6,body_9,False,cA,cB,dB)
link_19.SetDistance(0)
link_19.SetName("Distance11")
exported_items.append(link_19)

link_20 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.0971354179295116,0.17998186388193,-0.399662563127203)
dA = chrono.ChVectorD(-1,-4.71844785465692e-16,1.49880108324396e-15)
cB = chrono.ChVectorD(-0.0971854179295453,0.230143981136195,-0.408459491643065)
dB = chrono.ChVectorD(1,3.60822483003176e-16,-8.88178419700125e-16)
link_20.SetFlipped(True)
link_20.Initialize(body_6,body_9,False,cA,cB,dA,dB)
link_20.SetName("Distance11")
exported_items.append(link_20)


# Mate constraint: Distance12 [MateDistanceDim] type:5 align:1 flip:True
#   Entity 0: C::E name: body_8 , SW name: Spibot-LEG-1/upper_limb_con-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_2 , SW name: Spibot-LEG-1/limb_body_connector-1 ,  SW ref.type:2 (2)

link_21 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(-0.0971354179295165,0.23045936829327,-0.299189651658263)
cB = chrono.ChVectorD(-0.0970854179295196,0.23095,-0.209741440782467)
dA = chrono.ChVectorD(-1,-1.36002320516582e-15,4.16333634234434e-15)
dB = chrono.ChVectorD(1,1.38777878078145e-16,-4.44089209850063e-16)
link_21.Initialize(body_8,body_2,False,cA,cB,dB)
link_21.SetDistance(0)
link_21.SetName("Distance12")
exported_items.append(link_21)

link_22 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.0971354179295165,0.23045936829327,-0.299189651658263)
dA = chrono.ChVectorD(-1,-1.36002320516582e-15,4.16333634234434e-15)
cB = chrono.ChVectorD(-0.0970854179295196,0.23095,-0.209741440782467)
dB = chrono.ChVectorD(1,1.38777878078145e-16,-4.44089209850063e-16)
link_22.SetFlipped(True)
link_22.Initialize(body_8,body_2,False,cA,cB,dA,dB)
link_22.SetName("Distance12")
exported_items.append(link_22)


# Mate constraint: Distance13 [MateDistanceDim] type:5 align:1 flip:True
#   Entity 0: C::E name: body_4 , SW name: Spibot-LEG-1/Actuator_body-2 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_8 , SW name: Spibot-LEG-1/upper_limb_con-1 ,  SW ref.type:2 (2)

link_23 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(-0.092185417929518,0.19995,-0.159741440782467)
cB = chrono.ChVectorD(-0.0922354179295164,0.186132623231202,-0.255483992065765)
dA = chrono.ChVectorD(1,7.21644966006352e-16,-1.55431223447522e-15)
dB = chrono.ChVectorD(-1,-1.36002320516582e-15,4.16333634234434e-15)
link_23.Initialize(body_4,body_8,False,cA,cB,dB)
link_23.SetDistance(0)
link_23.SetName("Distance13")
exported_items.append(link_23)

link_24 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.092185417929518,0.19995,-0.159741440782467)
dA = chrono.ChVectorD(1,7.21644966006352e-16,-1.55431223447522e-15)
cB = chrono.ChVectorD(-0.0922354179295164,0.186132623231202,-0.255483992065765)
dB = chrono.ChVectorD(-1,-1.36002320516582e-15,4.16333634234434e-15)
link_24.SetFlipped(True)
link_24.Initialize(body_4,body_8,False,cA,cB,dA,dB)
link_24.SetName("Distance13")
exported_items.append(link_24)


# Mate constraint: Distance14 [MateDistanceDim] type:5 align:1 flip:False
#   Entity 0: C::E name: body_3 , SW name: Spibot-LEG-1/limb_body_connector-2 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_2 , SW name: Spibot-LEG-1/limb_body_connector-1 ,  SW ref.type:2 (2)

link_25 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(-0.10458541792952,0.20995,-0.139741440782467)
cB = chrono.ChVectorD(-0.10458541792952,0.23095,-0.139741440782467)
dA = chrono.ChVectorD(-1.66533453693773e-16,1,-1.2490009027033e-15)
dB = chrono.ChVectorD(1.38777878078145e-16,-1,5.55111512312578e-17)
link_25.Initialize(body_3,body_2,False,cA,cB,dB)
link_25.SetDistance(0)
link_25.SetName("Distance14")
exported_items.append(link_25)

link_26 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.10458541792952,0.20995,-0.139741440782467)
dA = chrono.ChVectorD(-1.66533453693773e-16,1,-1.2490009027033e-15)
cB = chrono.ChVectorD(-0.10458541792952,0.23095,-0.139741440782467)
dB = chrono.ChVectorD(1.38777878078145e-16,-1,5.55111512312578e-17)
link_26.SetFlipped(True)
link_26.Initialize(body_3,body_2,False,cA,cB,dA,dB)
link_26.SetName("Distance14")
exported_items.append(link_26)


# Mate constraint: Concentric21 [MateConcentric] type:1 align:1 flip:False
#   Entity 0: C::E name: body_8 , SW name: Spibot-LEG-1/upper_limb_con-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_7 , SW name: Spibot-LEG-1/Actuator_body-1 ,  SW ref.type:2 (2)

link_27 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.0897354179295162,0.186132623231202,-0.255483992065765)
dA = chrono.ChVectorD(-1,-1.36002320516582e-15,4.16333634234434e-15)
cB = chrono.ChVectorD(-0.102335417929506,0.186132623231204,-0.255483992065756)
dB = chrono.ChVectorD(1,3.88578058618805e-16,-1.77635683940025e-15)
link_27.SetFlipped(True)
link_27.Initialize(body_8,body_7,False,cA,cB,dA,dB)
link_27.SetName("Concentric21")
exported_items.append(link_27)

link_28 = chrono.ChLinkMateGeneric()
link_28.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.0897354179295162,0.186132623231202,-0.255483992065765)
cB = chrono.ChVectorD(-0.102335417929506,0.186132623231204,-0.255483992065756)
dA = chrono.ChVectorD(-1,-1.36002320516582e-15,4.16333634234434e-15)
dB = chrono.ChVectorD(1,3.88578058618805e-16,-1.77635683940025e-15)
link_28.Initialize(body_8,body_7,False,cA,cB,dA,dB)
link_28.SetName("Concentric21")
exported_items.append(link_28)


# Mate constraint: Concentric22 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_8 , SW name: Spibot-LEG-1/upper_limb_con-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_5 , SW name: Spibot-LEG-1/Actuator_rod-2 ,  SW ref.type:2 (2)

link_29 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.0897354179295163,0.209805310232533,-0.240989719769422)
dA = chrono.ChVectorD(-1,-1.36002320516582e-15,4.16333634234434e-15)
cB = chrono.ChVectorD(-0.0869854179295179,0.209805310232532,-0.240989719769408)
dB = chrono.ChVectorD(-1,-5.27355936696949e-16,1.88737914186277e-15)
link_29.Initialize(body_8,body_5,False,cA,cB,dA,dB)
link_29.SetName("Concentric22")
exported_items.append(link_29)

link_30 = chrono.ChLinkMateGeneric()
link_30.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.0897354179295163,0.209805310232533,-0.240989719769422)
cB = chrono.ChVectorD(-0.0869854179295179,0.209805310232532,-0.240989719769408)
dA = chrono.ChVectorD(-1,-1.36002320516582e-15,4.16333634234434e-15)
dB = chrono.ChVectorD(-1,-5.27355936696949e-16,1.88737914186277e-15)
link_30.Initialize(body_8,body_5,False,cA,cB,dA,dB)
link_30.SetName("Concentric22")
exported_items.append(link_30)


# Mate constraint: Concentric3 [MateConcentric] type:1 align:1 flip:False
#   Entity 0: C::E name: body_13 , SW name: Spibot-LEG-4/upper_limb_con-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_15 , SW name: Spibot-LEG-4/lower_limb-1 ,  SW ref.type:2 (2)

link_1 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.0879645820704804,0.219925094103436,0.199243453525253)
dA = chrono.ChVectorD(-1,-5.27355936696949e-16,-5.55111512312578e-17)
cB = chrono.ChVectorD(0.0755145820704805,0.219925094103436,0.199243453525253)
dB = chrono.ChVectorD(1,1.11022302462516e-16,-6.10622663543836e-16)
link_1.SetFlipped(True)
link_1.Initialize(body_13,body_15,False,cA,cB,dA,dB)
link_1.SetName("Concentric3")
exported_items.append(link_1)

link_2 = chrono.ChLinkMateGeneric()
link_2.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(0.0879645820704804,0.219925094103436,0.199243453525253)
cB = chrono.ChVectorD(0.0755145820704805,0.219925094103436,0.199243453525253)
dA = chrono.ChVectorD(-1,-5.27355936696949e-16,-5.55111512312578e-17)
dB = chrono.ChVectorD(1,1.11022302462516e-16,-6.10622663543836e-16)
link_2.Initialize(body_13,body_15,False,cA,cB,dA,dB)
link_2.SetName("Concentric3")
exported_items.append(link_2)


# Mate constraint: Concentric4 [MateConcentric] type:1 align:1 flip:False
#   Entity 0: C::E name: body_15 , SW name: Spibot-LEG-4/lower_limb-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_11 , SW name: Spibot-LEG-4/Actuator_rod-1 ,  SW ref.type:2 (2)

link_3 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.0755145820704806,0.179950025203841,0.200655496893087)
dA = chrono.ChVectorD(1,1.11022302462516e-16,-6.10622663543836e-16)
cB = chrono.ChVectorD(0.0879645820704805,0.179950025203841,0.200655496893087)
dB = chrono.ChVectorD(-1,-8.88178419700125e-16,2.44249065417534e-15)
link_3.SetFlipped(True)
link_3.Initialize(body_15,body_11,False,cA,cB,dA,dB)
link_3.SetName("Concentric4")
exported_items.append(link_3)

link_4 = chrono.ChLinkMateGeneric()
link_4.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(0.0755145820704806,0.179950025203841,0.200655496893087)
cB = chrono.ChVectorD(0.0879645820704805,0.179950025203841,0.200655496893087)
dA = chrono.ChVectorD(1,1.11022302462516e-16,-6.10622663543836e-16)
dB = chrono.ChVectorD(-1,-8.88178419700125e-16,2.44249065417534e-15)
link_4.Initialize(body_15,body_11,False,cA,cB,dA,dB)
link_4.SetName("Concentric4")
exported_items.append(link_4)


# Mate constraint: Concentric6 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_11 , SW name: Spibot-LEG-4/Actuator_rod-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_16 , SW name: Spibot-LEG-4/Actuator_body-1 ,  SW ref.type:2 (2)

link_5 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.0855645820704802,0.183580482659281,0.105724891824625)
dA = chrono.ChVectorD(-2.1094237467878e-15,0.0382153416362048,-0.999269527036439)
cB = chrono.ChVectorD(0.0855645820704803,0.182415851357719,0.136178121340725)
dB = chrono.ChVectorD(-1.11022302462516e-16,0.0382153416362048,-0.999269527036439)
link_5.Initialize(body_11,body_16,False,cA,cB,dA,dB)
link_5.SetName("Concentric6")
exported_items.append(link_5)

link_6 = chrono.ChLinkMateGeneric()
link_6.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(0.0855645820704802,0.183580482659281,0.105724891824625)
cB = chrono.ChVectorD(0.0855645820704803,0.182415851357719,0.136178121340725)
dA = chrono.ChVectorD(-2.1094237467878e-15,0.0382153416362048,-0.999269527036439)
dB = chrono.ChVectorD(-1.11022302462516e-16,0.0382153416362048,-0.999269527036439)
link_6.Initialize(body_11,body_16,False,cA,cB,dA,dB)
link_6.SetName("Concentric6")
exported_items.append(link_6)


# Mate constraint: Concentric11 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_14 , SW name: Spibot-LEG-4/Actuator_rod-2 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_12 , SW name: Spibot-LEG-4/Actuator_body-2 ,  SW ref.type:2 (2)

link_7 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.0854145820746712,0.202353443519983,-0.012946208551888)
dA = chrono.ChVectorD(-6.10622663543836e-16,-0.122358386741013,-0.992485982366571)
cB = chrono.ChVectorD(0.0854145820735133,0.206391503203577,0.01980771815803)
dB = chrono.ChVectorD(4.44089209850063e-16,-0.122358386741013,-0.992485982366571)
link_7.Initialize(body_14,body_12,False,cA,cB,dA,dB)
link_7.SetName("Concentric11")
exported_items.append(link_7)

link_8 = chrono.ChLinkMateGeneric()
link_8.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(0.0854145820746712,0.202353443519983,-0.012946208551888)
cB = chrono.ChVectorD(0.0854145820735133,0.206391503203577,0.01980771815803)
dA = chrono.ChVectorD(-6.10622663543836e-16,-0.122358386741013,-0.992485982366571)
dB = chrono.ChVectorD(4.44089209850063e-16,-0.122358386741013,-0.992485982366571)
link_8.Initialize(body_14,body_12,False,cA,cB,dA,dB)
link_8.SetName("Concentric11")
exported_items.append(link_8)


# Mate constraint: Concentric12 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_13 , SW name: Spibot-LEG-4/upper_limb_con-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_10 , SW name: Spibot-LEG-4/limb_body_connector-1 ,  SW ref.type:2 (2)

link_9 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.0879645820704804,0.24005,0.000258559217533053)
dA = chrono.ChVectorD(-1,-5.27355936696949e-16,-5.55111512312578e-17)
cB = chrono.ChVectorD(0.0954145820704804,0.24005,0.000258559217532942)
dB = chrono.ChVectorD(-1,8.32667268468867e-17,2.22044604925031e-16)
link_9.Initialize(body_13,body_10,False,cA,cB,dA,dB)
link_9.SetName("Concentric12")
exported_items.append(link_9)

link_10 = chrono.ChLinkMateGeneric()
link_10.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(0.0879645820704804,0.24005,0.000258559217533053)
cB = chrono.ChVectorD(0.0954145820704804,0.24005,0.000258559217532942)
dA = chrono.ChVectorD(-1,-5.27355936696949e-16,-5.55111512312578e-17)
dB = chrono.ChVectorD(-1,8.32667268468867e-17,2.22044604925031e-16)
link_10.Initialize(body_13,body_10,False,cA,cB,dA,dB)
link_10.SetName("Concentric12")
exported_items.append(link_10)


# Mate constraint: Concentric13 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_12 , SW name: Spibot-LEG-4/Actuator_body-2 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_17 , SW name: Spibot-LEG-4/limb_body_connector-2 ,  SW ref.type:2 (2)

link_11 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.0930145820735133,0.199049999999116,-0.0397414407839641)
dA = chrono.ChVectorD(-1,-7.21644966006352e-16,5.55111512312578e-17)
cB = chrono.ChVectorD(0.0954145820704804,0.19905,-0.039741440782467)
dB = chrono.ChVectorD(-1,1.38777878078145e-16,-5.55111512312578e-17)
link_11.Initialize(body_12,body_17,False,cA,cB,dA,dB)
link_11.SetName("Concentric13")
exported_items.append(link_11)

link_12 = chrono.ChLinkMateGeneric()
link_12.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(0.0930145820735133,0.199049999999116,-0.0397414407839641)
cB = chrono.ChVectorD(0.0954145820704804,0.19905,-0.039741440782467)
dA = chrono.ChVectorD(-1,-7.21644966006352e-16,5.55111512312578e-17)
dB = chrono.ChVectorD(-1,1.38777878078145e-16,-5.55111512312578e-17)
link_12.Initialize(body_12,body_17,False,cA,cB,dA,dB)
link_12.SetName("Concentric13")
exported_items.append(link_12)


# Mate constraint: Concentric17 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_10 , SW name: Spibot-LEG-4/limb_body_connector-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_17 , SW name: Spibot-LEG-4/limb_body_connector-2 ,  SW ref.type:2 (2)

link_13 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.0854145820704804,0.23005,-0.0597414407824671)
dA = chrono.ChVectorD(2.77555756156289e-17,1,0)
cB = chrono.ChVectorD(0.0854145820704804,0.18905,-0.0597414407824671)
dB = chrono.ChVectorD(2.77555756156289e-17,1,1.19348975147204e-15)
link_13.Initialize(body_10,body_17,False,cA,cB,dA,dB)
link_13.SetName("Concentric17")
exported_items.append(link_13)

link_14 = chrono.ChLinkMateGeneric()
link_14.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(0.0854145820704804,0.23005,-0.0597414407824671)
cB = chrono.ChVectorD(0.0854145820704804,0.18905,-0.0597414407824671)
dA = chrono.ChVectorD(2.77555756156289e-17,1,0)
dB = chrono.ChVectorD(2.77555756156289e-17,1,1.19348975147204e-15)
link_14.Initialize(body_10,body_17,False,cA,cB,dA,dB)
link_14.SetName("Concentric17")
exported_items.append(link_14)


# Mate constraint: Parallel14 [MateParallel] type:3 align:0 flip:False
#   Entity 0: C::E name: body_13 , SW name: Spibot-LEG-4/upper_limb_con-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_11 , SW name: Spibot-LEG-4/Actuator_rod-1 ,  SW ref.type:2 (2)

link_15 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.0879645820704805,0.229987547051718,0.0997510063713931)
dA = chrono.ChVectorD(1,5.27355936696949e-16,5.55111512312578e-17)
cB = chrono.ChVectorD(0.0879645820704805,0.179950025203841,0.200655496893087)
dB = chrono.ChVectorD(1,8.88178419700125e-16,-2.44249065417534e-15)
link_15.Initialize(body_13,body_11,False,cA,cB,dA,dB)
link_15.SetName("Parallel14")
exported_items.append(link_15)


# Mate constraint: Parallel15 [MateParallel] type:3 align:0 flip:False
#   Entity 0: C::E name: body_13 , SW name: Spibot-LEG-4/upper_limb_con-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_14 , SW name: Spibot-LEG-4/Actuator_rod-2 ,  SW ref.type:2 (2)

link_16 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.0830645820704805,0.185473078688615,0.0562365591778095)
dA = chrono.ChVectorD(1,5.27355936696949e-16,5.55111512312578e-17)
cB = chrono.ChVectorD(0.0878145820746712,0.209083154790739,0.0416405204782733)
dB = chrono.ChVectorD(1,2.4980018054066e-16,-6.66133814775094e-16)
link_16.Initialize(body_13,body_14,False,cA,cB,dA,dB)
link_16.SetName("Parallel15")
exported_items.append(link_16)


# Mate constraint: Distance10 [MateDistanceDim] type:5 align:1 flip:False
#   Entity 0: C::E name: body_13 , SW name: Spibot-LEG-4/upper_limb_con-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_15 , SW name: Spibot-LEG-4/lower_limb-1 ,  SW ref.type:2 (2)

link_17 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(0.0879645820704805,0.229987547051718,0.0997510063713931)
cB = chrono.ChVectorD(0.0880145820704805,0.230195012597463,0.20896604444157)
dA = chrono.ChVectorD(1,5.27355936696949e-16,5.55111512312578e-17)
dB = chrono.ChVectorD(-1,-3.60822483003176e-16,6.10622663543836e-16)
link_17.Initialize(body_13,body_15,False,cA,cB,dB)
link_17.SetDistance(0)
link_17.SetName("Distance10")
exported_items.append(link_17)

link_18 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.0879645820704805,0.229987547051718,0.0997510063713931)
dA = chrono.ChVectorD(1,5.27355936696949e-16,5.55111512312578e-17)
cB = chrono.ChVectorD(0.0880145820704805,0.230195012597463,0.20896604444157)
dB = chrono.ChVectorD(-1,-3.60822483003176e-16,6.10622663543836e-16)
link_18.SetFlipped(True)
link_18.Initialize(body_13,body_15,False,cA,cB,dA,dB)
link_18.SetName("Distance10")
exported_items.append(link_18)


# Mate constraint: Distance11 [MateDistanceDim] type:5 align:1 flip:False
#   Entity 0: C::E name: body_11 , SW name: Spibot-LEG-4/Actuator_rod-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_15 , SW name: Spibot-LEG-4/lower_limb-1 ,  SW ref.type:2 (2)

link_19 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(0.0879645820704805,0.179950025203841,0.200655496893087)
cB = chrono.ChVectorD(0.0880145820704805,0.230195012597463,0.20896604444157)
dA = chrono.ChVectorD(1,8.88178419700125e-16,-2.44249065417534e-15)
dB = chrono.ChVectorD(-1,-3.60822483003176e-16,6.10622663543836e-16)
link_19.Initialize(body_11,body_15,False,cA,cB,dB)
link_19.SetDistance(0)
link_19.SetName("Distance11")
exported_items.append(link_19)

link_20 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.0879645820704805,0.179950025203841,0.200655496893087)
dA = chrono.ChVectorD(1,8.88178419700125e-16,-2.44249065417534e-15)
cB = chrono.ChVectorD(0.0880145820704805,0.230195012597463,0.20896604444157)
dB = chrono.ChVectorD(-1,-3.60822483003176e-16,6.10622663543836e-16)
link_20.SetFlipped(True)
link_20.Initialize(body_11,body_15,False,cA,cB,dA,dB)
link_20.SetName("Distance11")
exported_items.append(link_20)


# Mate constraint: Distance12 [MateDistanceDim] type:5 align:1 flip:True
#   Entity 0: C::E name: body_13 , SW name: Spibot-LEG-4/upper_limb_con-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_10 , SW name: Spibot-LEG-4/limb_body_connector-1 ,  SW ref.type:2 (2)

link_21 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(0.0879645820704805,0.229987547051718,0.0997510063713931)
cB = chrono.ChVectorD(0.0879145820704804,0.23005,0.0102585592175329)
dA = chrono.ChVectorD(1,5.27355936696949e-16,5.55111512312578e-17)
dB = chrono.ChVectorD(-1,1.11022302462516e-16,4.44089209850063e-16)
link_21.Initialize(body_13,body_10,False,cA,cB,dB)
link_21.SetDistance(0)
link_21.SetName("Distance12")
exported_items.append(link_21)

link_22 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.0879645820704805,0.229987547051718,0.0997510063713931)
dA = chrono.ChVectorD(1,5.27355936696949e-16,5.55111512312578e-17)
cB = chrono.ChVectorD(0.0879145820704804,0.23005,0.0102585592175329)
dB = chrono.ChVectorD(-1,1.11022302462516e-16,4.44089209850063e-16)
link_22.SetFlipped(True)
link_22.Initialize(body_13,body_10,False,cA,cB,dA,dB)
link_22.SetName("Distance12")
exported_items.append(link_22)


# Mate constraint: Distance13 [MateDistanceDim] type:5 align:1 flip:True
#   Entity 0: C::E name: body_12 , SW name: Spibot-LEG-4/Actuator_body-2 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_13 , SW name: Spibot-LEG-4/upper_limb_con-1 ,  SW ref.type:2 (2)

link_23 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(0.0830145820735132,0.199049999999116,-0.0397414407839642)
cB = chrono.ChVectorD(0.0830645820704805,0.185473078688615,0.0562365591778095)
dA = chrono.ChVectorD(-1,-7.21644966006352e-16,5.55111512312578e-17)
dB = chrono.ChVectorD(1,5.27355936696949e-16,5.55111512312578e-17)
link_23.Initialize(body_12,body_13,False,cA,cB,dB)
link_23.SetDistance(0)
link_23.SetName("Distance13")
exported_items.append(link_23)

link_24 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.0830145820735132,0.199049999999116,-0.0397414407839642)
dA = chrono.ChVectorD(-1,-7.21644966006352e-16,5.55111512312578e-17)
cB = chrono.ChVectorD(0.0830645820704805,0.185473078688615,0.0562365591778095)
dB = chrono.ChVectorD(1,5.27355936696949e-16,5.55111512312578e-17)
link_24.SetFlipped(True)
link_24.Initialize(body_12,body_13,False,cA,cB,dA,dB)
link_24.SetName("Distance13")
exported_items.append(link_24)


# Mate constraint: Distance14 [MateDistanceDim] type:5 align:1 flip:False
#   Entity 0: C::E name: body_17 , SW name: Spibot-LEG-4/limb_body_connector-2 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_10 , SW name: Spibot-LEG-4/limb_body_connector-1 ,  SW ref.type:2 (2)

link_25 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(0.0954145820704804,0.20905,-0.059741440782467)
cB = chrono.ChVectorD(0.0954145820704804,0.23005,-0.0597414407824671)
dA = chrono.ChVectorD(2.77555756156289e-17,1,1.19348975147204e-15)
dB = chrono.ChVectorD(-2.77555756156289e-17,-1,0)
link_25.Initialize(body_17,body_10,False,cA,cB,dB)
link_25.SetDistance(0)
link_25.SetName("Distance14")
exported_items.append(link_25)

link_26 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.0954145820704804,0.20905,-0.059741440782467)
dA = chrono.ChVectorD(2.77555756156289e-17,1,1.19348975147204e-15)
cB = chrono.ChVectorD(0.0954145820704804,0.23005,-0.0597414407824671)
dB = chrono.ChVectorD(-2.77555756156289e-17,-1,0)
link_26.SetFlipped(True)
link_26.Initialize(body_17,body_10,False,cA,cB,dA,dB)
link_26.SetName("Distance14")
exported_items.append(link_26)


# Mate constraint: Concentric21 [MateConcentric] type:1 align:1 flip:False
#   Entity 0: C::E name: body_13 , SW name: Spibot-LEG-4/upper_limb_con-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_16 , SW name: Spibot-LEG-4/Actuator_body-1 ,  SW ref.type:2 (2)

link_27 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.0805645820704806,0.185473078688615,0.0562365591778095)
dA = chrono.ChVectorD(1,5.27355936696949e-16,5.55111512312578e-17)
cB = chrono.ChVectorD(0.0931645820704804,0.185473078688615,0.0562365591778096)
dB = chrono.ChVectorD(-1,-7.7715611723761e-16,3.88578058618805e-16)
link_27.SetFlipped(True)
link_27.Initialize(body_13,body_16,False,cA,cB,dA,dB)
link_27.SetName("Concentric21")
exported_items.append(link_27)

link_28 = chrono.ChLinkMateGeneric()
link_28.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(0.0805645820704806,0.185473078688615,0.0562365591778095)
cB = chrono.ChVectorD(0.0931645820704804,0.185473078688615,0.0562365591778096)
dA = chrono.ChVectorD(1,5.27355936696949e-16,5.55111512312578e-17)
dB = chrono.ChVectorD(-1,-7.7715611723761e-16,3.88578058618805e-16)
link_28.Initialize(body_13,body_16,False,cA,cB,dA,dB)
link_28.SetName("Concentric21")
exported_items.append(link_28)


# Mate constraint: Concentric22 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_13 , SW name: Spibot-LEG-4/upper_limb_con-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_14 , SW name: Spibot-LEG-4/Actuator_rod-2 ,  SW ref.type:2 (2)

link_29 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.0805645820704805,0.209083154791965,0.0416405204803566)
dA = chrono.ChVectorD(1,5.27355936696949e-16,5.55111512312578e-17)
cB = chrono.ChVectorD(0.0778145820746712,0.209083154790739,0.0416405204782733)
dB = chrono.ChVectorD(1,2.4980018054066e-16,-6.66133814775094e-16)
link_29.Initialize(body_13,body_14,False,cA,cB,dA,dB)
link_29.SetName("Concentric22")
exported_items.append(link_29)

link_30 = chrono.ChLinkMateGeneric()
link_30.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(0.0805645820704805,0.209083154791965,0.0416405204803566)
cB = chrono.ChVectorD(0.0778145820746712,0.209083154790739,0.0416405204782733)
dA = chrono.ChVectorD(1,5.27355936696949e-16,5.55111512312578e-17)
dB = chrono.ChVectorD(1,2.4980018054066e-16,-6.66133814775094e-16)
link_30.Initialize(body_13,body_14,False,cA,cB,dA,dB)
link_30.SetName("Concentric22")
exported_items.append(link_30)


# Mate constraint: Concentric3 [MateConcentric] type:1 align:1 flip:False
#   Entity 0: C::E name: body_18 , SW name: Spibot-LEG-5/upper_limb_con-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_24 , SW name: Spibot-LEG-5/lower_limb-1 ,  SW ref.type:2 (2)

link_1 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.00203541792952089,0.219925094465202,0.199243453561842)
dA = chrono.ChVectorD(-1,-5.82867087928207e-16,2.22044604925031e-16)
cB = chrono.ChVectorD(-0.0144854179295192,0.219925094465202,0.199243453561842)
dB = chrono.ChVectorD(1,6.66133814775094e-16,0)
link_1.SetFlipped(True)
link_1.Initialize(body_18,body_24,False,cA,cB,dA,dB)
link_1.SetName("Concentric3")
exported_items.append(link_1)

link_2 = chrono.ChLinkMateGeneric()
link_2.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.00203541792952089,0.219925094465202,0.199243453561842)
cB = chrono.ChVectorD(-0.0144854179295192,0.219925094465202,0.199243453561842)
dA = chrono.ChVectorD(-1,-5.82867087928207e-16,2.22044604925031e-16)
dB = chrono.ChVectorD(1,6.66133814775094e-16,0)
link_2.Initialize(body_18,body_24,False,cA,cB,dA,dB)
link_2.SetName("Concentric3")
exported_items.append(link_2)


# Mate constraint: Concentric4 [MateConcentric] type:1 align:1 flip:False
#   Entity 0: C::E name: body_24 , SW name: Spibot-LEG-5/lower_limb-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_25 , SW name: Spibot-LEG-5/Actuator_rod-1 ,  SW ref.type:2 (2)

link_3 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.0144854179295192,0.179950025472276,0.200655494287447)
dA = chrono.ChVectorD(1,6.66133814775094e-16,0)
cB = chrono.ChVectorD(-0.00203541792951933,0.179950025472276,0.200655494287447)
dB = chrono.ChVectorD(-1,-1.41553435639707e-15,1.66533453693773e-16)
link_3.SetFlipped(True)
link_3.Initialize(body_24,body_25,False,cA,cB,dA,dB)
link_3.SetName("Concentric4")
exported_items.append(link_3)

link_4 = chrono.ChLinkMateGeneric()
link_4.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.0144854179295192,0.179950025472276,0.200655494287447)
cB = chrono.ChVectorD(-0.00203541792951933,0.179950025472276,0.200655494287447)
dA = chrono.ChVectorD(1,6.66133814775094e-16,0)
dB = chrono.ChVectorD(-1,-1.41553435639707e-15,1.66533453693773e-16)
link_4.Initialize(body_24,body_25,False,cA,cB,dA,dB)
link_4.SetName("Concentric4")
exported_items.append(link_4)


# Mate constraint: Concentric6 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_25 , SW name: Spibot-LEG-5/Actuator_rod-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_20 , SW name: Spibot-LEG-5/Actuator_body-1 ,  SW ref.type:2 (2)

link_5 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.00443541792951929,0.183580482886219,0.105724889217399)
dA = chrono.ChVectorD(-2.77555756156289e-16,0.038215341199407,-0.999269527053143)
cB = chrono.ChVectorD(-0.00443541792951929,0.182415851494434,0.136178121441285)
dB = chrono.ChVectorD(-5.55111512312578e-16,0.0382153411994069,-0.999269527053143)
link_5.Initialize(body_25,body_20,False,cA,cB,dA,dB)
link_5.SetName("Concentric6")
exported_items.append(link_5)

link_6 = chrono.ChLinkMateGeneric()
link_6.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.00443541792951929,0.183580482886219,0.105724889217399)
cB = chrono.ChVectorD(-0.00443541792951929,0.182415851494434,0.136178121441285)
dA = chrono.ChVectorD(-2.77555756156289e-16,0.038215341199407,-0.999269527053143)
dB = chrono.ChVectorD(-5.55111512312578e-16,0.0382153411994069,-0.999269527053143)
link_6.Initialize(body_25,body_20,False,cA,cB,dA,dB)
link_6.SetName("Concentric6")
exported_items.append(link_6)


# Mate constraint: Concentric11 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_23 , SW name: Spibot-LEG-5/Actuator_rod-2 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_22 , SW name: Spibot-LEG-5/Actuator_body-2 ,  SW ref.type:2 (2)

link_7 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.00458541792951961,0.202353443551322,-0.0129462084879424)
dA = chrono.ChVectorD(5.55111512312578e-17,-0.122358387561416,-0.992485982265427)
cB = chrono.ChVectorD(-0.00458541792951961,0.206391503253685,0.0198077181534587)
dB = chrono.ChVectorD(1.66533453693773e-16,-0.122358387561416,-0.992485982265428)
link_7.Initialize(body_23,body_22,False,cA,cB,dA,dB)
link_7.SetName("Concentric11")
exported_items.append(link_7)

link_8 = chrono.ChLinkMateGeneric()
link_8.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.00458541792951961,0.202353443551322,-0.0129462084879424)
cB = chrono.ChVectorD(-0.00458541792951961,0.206391503253685,0.0198077181534587)
dA = chrono.ChVectorD(5.55111512312578e-17,-0.122358387561416,-0.992485982265427)
dB = chrono.ChVectorD(1.66533453693773e-16,-0.122358387561416,-0.992485982265428)
link_8.Initialize(body_23,body_22,False,cA,cB,dA,dB)
link_8.SetName("Concentric11")
exported_items.append(link_8)


# Mate constraint: Concentric12 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_18 , SW name: Spibot-LEG-5/upper_limb_con-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_21 , SW name: Spibot-LEG-5/limb_body_connector-1 ,  SW ref.type:2 (2)

link_9 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.00203541792952111,0.24005,0.000258559217533066)
dA = chrono.ChVectorD(-1,-5.82867087928207e-16,2.22044604925031e-16)
cB = chrono.ChVectorD(0.0054145820704804,0.24005,0.000258559217533011)
dB = chrono.ChVectorD(-1,-5.55111512312578e-17,0)
link_9.Initialize(body_18,body_21,False,cA,cB,dA,dB)
link_9.SetName("Concentric12")
exported_items.append(link_9)

link_10 = chrono.ChLinkMateGeneric()
link_10.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.00203541792952111,0.24005,0.000258559217533066)
cB = chrono.ChVectorD(0.0054145820704804,0.24005,0.000258559217533011)
dA = chrono.ChVectorD(-1,-5.82867087928207e-16,2.22044604925031e-16)
dB = chrono.ChVectorD(-1,-5.55111512312578e-17,0)
link_10.Initialize(body_18,body_21,False,cA,cB,dA,dB)
link_10.SetName("Concentric12")
exported_items.append(link_10)


# Mate constraint: Concentric13 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_22 , SW name: Spibot-LEG-5/Actuator_body-2 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_19 , SW name: Spibot-LEG-5/limb_body_connector-2 ,  SW ref.type:2 (2)

link_11 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.00301458207048044,0.19905,-0.0397414407824669)
dA = chrono.ChVectorD(-1,-1.47104550762833e-15,-5.55111512312578e-17)
cB = chrono.ChVectorD(0.0054145820704804,0.19905,-0.039741440782467)
dB = chrono.ChVectorD(-1,-2.77555756156289e-17,-2.22044604925031e-16)
link_11.Initialize(body_22,body_19,False,cA,cB,dA,dB)
link_11.SetName("Concentric13")
exported_items.append(link_11)

link_12 = chrono.ChLinkMateGeneric()
link_12.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(0.00301458207048044,0.19905,-0.0397414407824669)
cB = chrono.ChVectorD(0.0054145820704804,0.19905,-0.039741440782467)
dA = chrono.ChVectorD(-1,-1.47104550762833e-15,-5.55111512312578e-17)
dB = chrono.ChVectorD(-1,-2.77555756156289e-17,-2.22044604925031e-16)
link_12.Initialize(body_22,body_19,False,cA,cB,dA,dB)
link_12.SetName("Concentric13")
exported_items.append(link_12)


# Mate constraint: Concentric17 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_21 , SW name: Spibot-LEG-5/limb_body_connector-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_19 , SW name: Spibot-LEG-5/limb_body_connector-2 ,  SW ref.type:2 (2)

link_13 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.0045854179295195,0.23005,-0.059741440782467)
dA = chrono.ChVectorD(0,1,1.11022302462516e-16)
cB = chrono.ChVectorD(-0.00458541792951961,0.18905,-0.059741440782467)
dB = chrono.ChVectorD(0,1,1.33226762955019e-15)
link_13.Initialize(body_21,body_19,False,cA,cB,dA,dB)
link_13.SetName("Concentric17")
exported_items.append(link_13)

link_14 = chrono.ChLinkMateGeneric()
link_14.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.0045854179295195,0.23005,-0.059741440782467)
cB = chrono.ChVectorD(-0.00458541792951961,0.18905,-0.059741440782467)
dA = chrono.ChVectorD(0,1,1.11022302462516e-16)
dB = chrono.ChVectorD(0,1,1.33226762955019e-15)
link_14.Initialize(body_21,body_19,False,cA,cB,dA,dB)
link_14.SetName("Concentric17")
exported_items.append(link_14)


# Mate constraint: Parallel14 [MateParallel] type:3 align:0 flip:False
#   Entity 0: C::E name: body_18 , SW name: Spibot-LEG-5/upper_limb_con-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_25 , SW name: Spibot-LEG-5/Actuator_rod-1 ,  SW ref.type:2 (2)

link_15 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.00203541792952089,0.229987547232601,0.0997510063896872)
dA = chrono.ChVectorD(1,5.82867087928207e-16,-2.22044604925031e-16)
cB = chrono.ChVectorD(-0.00203541792951933,0.179950025472276,0.200655494287447)
dB = chrono.ChVectorD(1,1.41553435639707e-15,-1.66533453693773e-16)
link_15.Initialize(body_18,body_25,False,cA,cB,dA,dB)
link_15.SetName("Parallel14")
exported_items.append(link_15)


# Mate constraint: Parallel15 [MateParallel] type:3 align:0 flip:False
#   Entity 0: C::E name: body_18 , SW name: Spibot-LEG-5/upper_limb_con-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_23 , SW name: Spibot-LEG-5/Actuator_rod-2 ,  SW ref.type:2 (2)

link_16 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.0069354179295209,0.185473078790387,0.0562365592770337)
dA = chrono.ChVectorD(1,5.82867087928207e-16,-2.22044604925031e-16)
cB = chrono.ChVectorD(-0.00218541792951965,0.209083154867199,0.0416405205366562)
dB = chrono.ChVectorD(1,1.58206781009085e-15,-5.55111512312578e-17)
link_16.Initialize(body_18,body_23,False,cA,cB,dA,dB)
link_16.SetName("Parallel15")
exported_items.append(link_16)


# Mate constraint: Distance10 [MateDistanceDim] type:5 align:1 flip:False
#   Entity 0: C::E name: body_18 , SW name: Spibot-LEG-5/upper_limb_con-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_24 , SW name: Spibot-LEG-5/lower_limb-1 ,  SW ref.type:2 (2)

link_17 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(-0.00203541792952089,0.229987547232601,0.0997510063896872)
cB = chrono.ChVectorD(-0.00198541792951923,0.230195012316596,0.208966045156968)
dA = chrono.ChVectorD(1,5.82867087928207e-16,-2.22044604925031e-16)
dB = chrono.ChVectorD(-1,-9.15933995315754e-16,5.55111512312578e-17)
link_17.Initialize(body_18,body_24,False,cA,cB,dB)
link_17.SetDistance(0)
link_17.SetName("Distance10")
exported_items.append(link_17)

link_18 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.00203541792952089,0.229987547232601,0.0997510063896872)
dA = chrono.ChVectorD(1,5.82867087928207e-16,-2.22044604925031e-16)
cB = chrono.ChVectorD(-0.00198541792951923,0.230195012316596,0.208966045156968)
dB = chrono.ChVectorD(-1,-9.15933995315754e-16,5.55111512312578e-17)
link_18.SetFlipped(True)
link_18.Initialize(body_18,body_24,False,cA,cB,dA,dB)
link_18.SetName("Distance10")
exported_items.append(link_18)


# Mate constraint: Distance11 [MateDistanceDim] type:5 align:1 flip:False
#   Entity 0: C::E name: body_25 , SW name: Spibot-LEG-5/Actuator_rod-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_24 , SW name: Spibot-LEG-5/lower_limb-1 ,  SW ref.type:2 (2)

link_19 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(-0.00203541792951933,0.179950025472276,0.200655494287447)
cB = chrono.ChVectorD(-0.00198541792951923,0.230195012316596,0.208966045156968)
dA = chrono.ChVectorD(1,1.41553435639707e-15,-1.66533453693773e-16)
dB = chrono.ChVectorD(-1,-9.15933995315754e-16,5.55111512312578e-17)
link_19.Initialize(body_25,body_24,False,cA,cB,dB)
link_19.SetDistance(0)
link_19.SetName("Distance11")
exported_items.append(link_19)

link_20 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.00203541792951933,0.179950025472276,0.200655494287447)
dA = chrono.ChVectorD(1,1.41553435639707e-15,-1.66533453693773e-16)
cB = chrono.ChVectorD(-0.00198541792951923,0.230195012316596,0.208966045156968)
dB = chrono.ChVectorD(-1,-9.15933995315754e-16,5.55111512312578e-17)
link_20.SetFlipped(True)
link_20.Initialize(body_25,body_24,False,cA,cB,dA,dB)
link_20.SetName("Distance11")
exported_items.append(link_20)


# Mate constraint: Distance12 [MateDistanceDim] type:5 align:1 flip:True
#   Entity 0: C::E name: body_18 , SW name: Spibot-LEG-5/upper_limb_con-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_21 , SW name: Spibot-LEG-5/limb_body_connector-1 ,  SW ref.type:2 (2)

link_21 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(-0.00203541792952089,0.229987547232601,0.0997510063896872)
cB = chrono.ChVectorD(-0.00208541792951944,0.23005,0.010258559217533)
dA = chrono.ChVectorD(1,5.82867087928207e-16,-2.22044604925031e-16)
dB = chrono.ChVectorD(-1,-5.55111512312578e-17,2.77555756156289e-16)
link_21.Initialize(body_18,body_21,False,cA,cB,dB)
link_21.SetDistance(0)
link_21.SetName("Distance12")
exported_items.append(link_21)

link_22 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.00203541792952089,0.229987547232601,0.0997510063896872)
dA = chrono.ChVectorD(1,5.82867087928207e-16,-2.22044604925031e-16)
cB = chrono.ChVectorD(-0.00208541792951944,0.23005,0.010258559217533)
dB = chrono.ChVectorD(-1,-5.55111512312578e-17,2.77555756156289e-16)
link_22.SetFlipped(True)
link_22.Initialize(body_18,body_21,False,cA,cB,dA,dB)
link_22.SetName("Distance12")
exported_items.append(link_22)


# Mate constraint: Distance13 [MateDistanceDim] type:5 align:1 flip:True
#   Entity 0: C::E name: body_22 , SW name: Spibot-LEG-5/Actuator_body-2 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_18 , SW name: Spibot-LEG-5/upper_limb_con-1 ,  SW ref.type:2 (2)

link_23 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(-0.00698541792951957,0.19905,-0.0397414407824669)
cB = chrono.ChVectorD(-0.0069354179295209,0.185473078790387,0.0562365592770337)
dA = chrono.ChVectorD(-1,-1.47104550762833e-15,-5.55111512312578e-17)
dB = chrono.ChVectorD(1,5.82867087928207e-16,-2.22044604925031e-16)
link_23.Initialize(body_22,body_18,False,cA,cB,dB)
link_23.SetDistance(0)
link_23.SetName("Distance13")
exported_items.append(link_23)

link_24 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.00698541792951957,0.19905,-0.0397414407824669)
dA = chrono.ChVectorD(-1,-1.47104550762833e-15,-5.55111512312578e-17)
cB = chrono.ChVectorD(-0.0069354179295209,0.185473078790387,0.0562365592770337)
dB = chrono.ChVectorD(1,5.82867087928207e-16,-2.22044604925031e-16)
link_24.SetFlipped(True)
link_24.Initialize(body_22,body_18,False,cA,cB,dA,dB)
link_24.SetName("Distance13")
exported_items.append(link_24)


# Mate constraint: Distance14 [MateDistanceDim] type:5 align:1 flip:False
#   Entity 0: C::E name: body_19 , SW name: Spibot-LEG-5/limb_body_connector-2 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_21 , SW name: Spibot-LEG-5/limb_body_connector-1 ,  SW ref.type:2 (2)

link_25 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(0.0054145820704804,0.20905,-0.0597414407824669)
cB = chrono.ChVectorD(0.00541458207048051,0.23005,-0.059741440782467)
dA = chrono.ChVectorD(0,1,1.33226762955019e-15)
dB = chrono.ChVectorD(0,-1,-1.11022302462516e-16)
link_25.Initialize(body_19,body_21,False,cA,cB,dB)
link_25.SetDistance(0)
link_25.SetName("Distance14")
exported_items.append(link_25)

link_26 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.0054145820704804,0.20905,-0.0597414407824669)
dA = chrono.ChVectorD(0,1,1.33226762955019e-15)
cB = chrono.ChVectorD(0.00541458207048051,0.23005,-0.059741440782467)
dB = chrono.ChVectorD(0,-1,-1.11022302462516e-16)
link_26.SetFlipped(True)
link_26.Initialize(body_19,body_21,False,cA,cB,dA,dB)
link_26.SetName("Distance14")
exported_items.append(link_26)


# Mate constraint: Concentric21 [MateConcentric] type:1 align:1 flip:False
#   Entity 0: C::E name: body_18 , SW name: Spibot-LEG-5/upper_limb_con-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_20 , SW name: Spibot-LEG-5/Actuator_body-1 ,  SW ref.type:2 (2)

link_27 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.00943541792952096,0.185473078790387,0.0562365592770335)
dA = chrono.ChVectorD(1,5.82867087928207e-16,-2.22044604925031e-16)
cB = chrono.ChVectorD(0.00316458207048076,0.185473078790387,0.0562365592770337)
dB = chrono.ChVectorD(-1,-1.33226762955019e-15,3.88578058618805e-16)
link_27.SetFlipped(True)
link_27.Initialize(body_18,body_20,False,cA,cB,dA,dB)
link_27.SetName("Concentric21")
exported_items.append(link_27)

link_28 = chrono.ChLinkMateGeneric()
link_28.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.00943541792952096,0.185473078790387,0.0562365592770335)
cB = chrono.ChVectorD(0.00316458207048076,0.185473078790387,0.0562365592770337)
dA = chrono.ChVectorD(1,5.82867087928207e-16,-2.22044604925031e-16)
dB = chrono.ChVectorD(-1,-1.33226762955019e-15,3.88578058618805e-16)
link_28.Initialize(body_18,body_20,False,cA,cB,dA,dB)
link_28.SetName("Concentric21")
exported_items.append(link_28)


# Mate constraint: Concentric22 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_18 , SW name: Spibot-LEG-5/upper_limb_con-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_23 , SW name: Spibot-LEG-5/Actuator_rod-2 ,  SW ref.type:2 (2)

link_29 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.00943541792952096,0.209083154867199,0.0416405205366562)
dA = chrono.ChVectorD(1,5.82867087928207e-16,-2.22044604925031e-16)
cB = chrono.ChVectorD(-0.0121854179295197,0.209083154867199,0.0416405205366561)
dB = chrono.ChVectorD(1,1.58206781009085e-15,-5.55111512312578e-17)
link_29.Initialize(body_18,body_23,False,cA,cB,dA,dB)
link_29.SetName("Concentric22")
exported_items.append(link_29)

link_30 = chrono.ChLinkMateGeneric()
link_30.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.00943541792952096,0.209083154867199,0.0416405205366562)
cB = chrono.ChVectorD(-0.0121854179295197,0.209083154867199,0.0416405205366561)
dA = chrono.ChVectorD(1,5.82867087928207e-16,-2.22044604925031e-16)
dB = chrono.ChVectorD(1,1.58206781009085e-15,-5.55111512312578e-17)
link_30.Initialize(body_18,body_23,False,cA,cB,dA,dB)
link_30.SetName("Concentric22")
exported_items.append(link_30)


# Mate constraint: Concentric3 [MateConcentric] type:1 align:1 flip:False
#   Entity 0: C::E name: body_32 , SW name: Spibot-LEG-6/upper_limb_con-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_33 , SW name: Spibot-LEG-6/lower_limb-1 ,  SW ref.type:2 (2)

link_1 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.0920354179295193,0.219925371157137,0.199253569807512)
dA = chrono.ChVectorD(-1,-3.33066907387547e-16,-2.22044604925031e-16)
cB = chrono.ChVectorD(-0.10448541792952,0.219925371157137,0.199253569807512)
dB = chrono.ChVectorD(1,3.88578058618805e-16,1.11022302462516e-16)
link_1.SetFlipped(True)
link_1.Initialize(body_32,body_33,False,cA,cB,dA,dB)
link_1.SetName("Concentric3")
exported_items.append(link_1)

link_2 = chrono.ChLinkMateGeneric()
link_2.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.0920354179295193,0.219925371157137,0.199253569807512)
cB = chrono.ChVectorD(-0.10448541792952,0.219925371157137,0.199253569807512)
dA = chrono.ChVectorD(-1,-3.33066907387547e-16,-2.22044604925031e-16)
dB = chrono.ChVectorD(1,3.88578058618805e-16,1.11022302462516e-16)
link_2.Initialize(body_32,body_33,False,cA,cB,dA,dB)
link_2.SetName("Concentric3")
exported_items.append(link_2)


# Mate constraint: Concentric4 [MateConcentric] type:1 align:1 flip:False
#   Entity 0: C::E name: body_33 , SW name: Spibot-LEG-6/lower_limb-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_30 , SW name: Spibot-LEG-6/Actuator_rod-1 ,  SW ref.type:2 (2)

link_3 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.10448541792952,0.179950230765922,0.200663587787044)
dA = chrono.ChVectorD(1,3.88578058618805e-16,1.11022302462516e-16)
cB = chrono.ChVectorD(-0.0920354179295195,0.179950230765922,0.200663587787044)
dB = chrono.ChVectorD(-1,6.93889390390723e-16,9.43689570931383e-16)
link_3.SetFlipped(True)
link_3.Initialize(body_33,body_30,False,cA,cB,dA,dB)
link_3.SetName("Concentric4")
exported_items.append(link_3)

link_4 = chrono.ChLinkMateGeneric()
link_4.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.10448541792952,0.179950230765922,0.200663587787044)
cB = chrono.ChVectorD(-0.0920354179295195,0.179950230765922,0.200663587787044)
dA = chrono.ChVectorD(1,3.88578058618805e-16,1.11022302462516e-16)
dB = chrono.ChVectorD(-1,6.93889390390723e-16,9.43689570931383e-16)
link_4.Initialize(body_33,body_30,False,cA,cB,dA,dB)
link_4.SetName("Concentric4")
exported_items.append(link_4)


# Mate constraint: Concentric6 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_30 , SW name: Spibot-LEG-6/Actuator_rod-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_29 , SW name: Spibot-LEG-6/Actuator_body-1 ,  SW ref.type:2 (2)

link_5 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.0944354179295197,0.183533916030729,0.10573120553566)
dA = chrono.ChVectorD(-9.99200722162641e-16,0.0377230027874489,-0.99928823422509)
cB = chrono.ChVectorD(-0.0944354179295199,0.182383454400346,0.136207113767222)
dB = chrono.ChVectorD(-1.16573417585641e-15,0.0377230027874489,-0.99928823422509)
link_5.Initialize(body_30,body_29,False,cA,cB,dA,dB)
link_5.SetName("Concentric6")
exported_items.append(link_5)

link_6 = chrono.ChLinkMateGeneric()
link_6.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.0944354179295197,0.183533916030729,0.10573120553566)
cB = chrono.ChVectorD(-0.0944354179295199,0.182383454400346,0.136207113767222)
dA = chrono.ChVectorD(-9.99200722162641e-16,0.0377230027874489,-0.99928823422509)
dB = chrono.ChVectorD(-1.16573417585641e-15,0.0377230027874489,-0.99928823422509)
link_6.Initialize(body_30,body_29,False,cA,cB,dA,dB)
link_6.SetName("Concentric6")
exported_items.append(link_6)


# Mate constraint: Concentric11 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_27 , SW name: Spibot-LEG-6/Actuator_rod-2 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_31 , SW name: Spibot-LEG-6/Actuator_body-2 ,  SW ref.type:2 (2)

link_7 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.0945854179295198,0.202261793995068,-0.012929065288893)
dA = chrono.ChVectorD(-9.43689570931383e-16,-0.122585788164119,-0.992457920790691)
cB = chrono.ChVectorD(-0.0945854179295197,0.206305147289847,0.0198060344649746)
dB = chrono.ChVectorD(-1.66533453693773e-16,-0.122585788164119,-0.992457920790691)
link_7.Initialize(body_27,body_31,False,cA,cB,dA,dB)
link_7.SetName("Concentric11")
exported_items.append(link_7)

link_8 = chrono.ChLinkMateGeneric()
link_8.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.0945854179295198,0.202261793995068,-0.012929065288893)
cB = chrono.ChVectorD(-0.0945854179295197,0.206305147289847,0.0198060344649746)
dA = chrono.ChVectorD(-9.43689570931383e-16,-0.122585788164119,-0.992457920790691)
dB = chrono.ChVectorD(-1.66533453693773e-16,-0.122585788164119,-0.992457920790691)
link_8.Initialize(body_27,body_31,False,cA,cB,dA,dB)
link_8.SetName("Concentric11")
exported_items.append(link_8)


# Mate constraint: Concentric12 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_32 , SW name: Spibot-LEG-6/upper_limb_con-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_26 , SW name: Spibot-LEG-6/limb_body_connector-1 ,  SW ref.type:2 (2)

link_9 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.0920354179295193,0.23995,0.000258559217532955)
dA = chrono.ChVectorD(-1,-3.33066907387547e-16,-2.22044604925031e-16)
cB = chrono.ChVectorD(-0.0845854179295197,0.23995,0.000258559217533011)
dB = chrono.ChVectorD(-1,-1.11022302462516e-16,-2.22044604925031e-16)
link_9.Initialize(body_32,body_26,False,cA,cB,dA,dB)
link_9.SetName("Concentric12")
exported_items.append(link_9)

link_10 = chrono.ChLinkMateGeneric()
link_10.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.0920354179295193,0.23995,0.000258559217532955)
cB = chrono.ChVectorD(-0.0845854179295197,0.23995,0.000258559217533011)
dA = chrono.ChVectorD(-1,-3.33066907387547e-16,-2.22044604925031e-16)
dB = chrono.ChVectorD(-1,-1.11022302462516e-16,-2.22044604925031e-16)
link_10.Initialize(body_32,body_26,False,cA,cB,dA,dB)
link_10.SetName("Concentric12")
exported_items.append(link_10)


# Mate constraint: Concentric13 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_31 , SW name: Spibot-LEG-6/Actuator_body-2 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_28 , SW name: Spibot-LEG-6/limb_body_connector-2 ,  SW ref.type:2 (2)

link_11 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.0869854179295197,0.19895,-0.0397414407824669)
dA = chrono.ChVectorD(-1,9.71445146547012e-16,2.77555756156289e-16)
cB = chrono.ChVectorD(-0.0845854179295197,0.19895,-0.039741440782467)
dB = chrono.ChVectorD(-1,-8.32667268468867e-17,-4.9960036108132e-16)
link_11.Initialize(body_31,body_28,False,cA,cB,dA,dB)
link_11.SetName("Concentric13")
exported_items.append(link_11)

link_12 = chrono.ChLinkMateGeneric()
link_12.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.0869854179295197,0.19895,-0.0397414407824669)
cB = chrono.ChVectorD(-0.0845854179295197,0.19895,-0.039741440782467)
dA = chrono.ChVectorD(-1,9.71445146547012e-16,2.77555756156289e-16)
dB = chrono.ChVectorD(-1,-8.32667268468867e-17,-4.9960036108132e-16)
link_12.Initialize(body_31,body_28,False,cA,cB,dA,dB)
link_12.SetName("Concentric13")
exported_items.append(link_12)


# Mate constraint: Concentric17 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_26 , SW name: Spibot-LEG-6/limb_body_connector-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_28 , SW name: Spibot-LEG-6/limb_body_connector-2 ,  SW ref.type:2 (2)

link_13 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.0945854179295196,0.22995,-0.059741440782467)
dA = chrono.ChVectorD(-1.38777878078145e-16,1,1.36002320516582e-15)
cB = chrono.ChVectorD(-0.0945854179295196,0.18895,-0.0597414407824671)
dB = chrono.ChVectorD(-1.11022302462516e-16,1,2.55351295663786e-15)
link_13.Initialize(body_26,body_28,False,cA,cB,dA,dB)
link_13.SetName("Concentric17")
exported_items.append(link_13)

link_14 = chrono.ChLinkMateGeneric()
link_14.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.0945854179295196,0.22995,-0.059741440782467)
cB = chrono.ChVectorD(-0.0945854179295196,0.18895,-0.0597414407824671)
dA = chrono.ChVectorD(-1.38777878078145e-16,1,1.36002320516582e-15)
dB = chrono.ChVectorD(-1.11022302462516e-16,1,2.55351295663786e-15)
link_14.Initialize(body_26,body_28,False,cA,cB,dA,dB)
link_14.SetName("Concentric17")
exported_items.append(link_14)


# Mate constraint: Parallel14 [MateParallel] type:3 align:0 flip:False
#   Entity 0: C::E name: body_32 , SW name: Spibot-LEG-6/upper_limb_con-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_30 , SW name: Spibot-LEG-6/Actuator_rod-1 ,  SW ref.type:2 (2)

link_15 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.0920354179295193,0.229937685578568,0.0997560645125223)
dA = chrono.ChVectorD(1,3.33066907387547e-16,2.22044604925031e-16)
cB = chrono.ChVectorD(-0.0920354179295195,0.179950230765922,0.200663587787044)
dB = chrono.ChVectorD(1,-6.93889390390723e-16,-9.43689570931383e-16)
link_15.Initialize(body_32,body_30,False,cA,cB,dA,dB)
link_15.SetName("Parallel14")
exported_items.append(link_15)


# Mate constraint: Parallel15 [MateParallel] type:3 align:0 flip:False
#   Entity 0: C::E name: body_32 , SW name: Spibot-LEG-6/upper_limb_con-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_27 , SW name: Spibot-LEG-6/Actuator_rod-2 ,  SW ref.type:2 (2)

link_16 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.0969354179295193,0.185401294623342,0.0562640550292153)
dA = chrono.ChVectorD(1,3.33066907387547e-16,2.22044604925031e-16)
cB = chrono.ChVectorD(-0.0921854179295196,0.209004012344094,0.0416561203545951)
dB = chrono.ChVectorD(1,-7.49400541621981e-16,-9.99200722162641e-16)
link_16.Initialize(body_32,body_27,False,cA,cB,dA,dB)
link_16.SetName("Parallel15")
exported_items.append(link_16)


# Mate constraint: Distance10 [MateDistanceDim] type:5 align:1 flip:False
#   Entity 0: C::E name: body_32 , SW name: Spibot-LEG-6/upper_limb_con-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_33 , SW name: Spibot-LEG-6/lower_limb-1 ,  SW ref.type:2 (2)

link_17 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(-0.0920354179295193,0.229937685578568,0.0997560645125223)
cB = chrono.ChVectorD(-0.0919854179295198,0.230194797030844,0.208976681049519)
dA = chrono.ChVectorD(1,3.33066907387547e-16,2.22044604925031e-16)
dB = chrono.ChVectorD(-1,-5.55111512312578e-16,-1.11022302462516e-16)
link_17.Initialize(body_32,body_33,False,cA,cB,dB)
link_17.SetDistance(0)
link_17.SetName("Distance10")
exported_items.append(link_17)

link_18 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.0920354179295193,0.229937685578568,0.0997560645125223)
dA = chrono.ChVectorD(1,3.33066907387547e-16,2.22044604925031e-16)
cB = chrono.ChVectorD(-0.0919854179295198,0.230194797030844,0.208976681049519)
dB = chrono.ChVectorD(-1,-5.55111512312578e-16,-1.11022302462516e-16)
link_18.SetFlipped(True)
link_18.Initialize(body_32,body_33,False,cA,cB,dA,dB)
link_18.SetName("Distance10")
exported_items.append(link_18)


# Mate constraint: Distance11 [MateDistanceDim] type:5 align:1 flip:False
#   Entity 0: C::E name: body_30 , SW name: Spibot-LEG-6/Actuator_rod-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_33 , SW name: Spibot-LEG-6/lower_limb-1 ,  SW ref.type:2 (2)

link_19 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(-0.0920354179295195,0.179950230765922,0.200663587787044)
cB = chrono.ChVectorD(-0.0919854179295198,0.230194797030844,0.208976681049519)
dA = chrono.ChVectorD(1,-6.93889390390723e-16,-9.43689570931383e-16)
dB = chrono.ChVectorD(-1,-5.55111512312578e-16,-1.11022302462516e-16)
link_19.Initialize(body_30,body_33,False,cA,cB,dB)
link_19.SetDistance(0)
link_19.SetName("Distance11")
exported_items.append(link_19)

link_20 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.0920354179295195,0.179950230765922,0.200663587787044)
dA = chrono.ChVectorD(1,-6.93889390390723e-16,-9.43689570931383e-16)
cB = chrono.ChVectorD(-0.0919854179295198,0.230194797030844,0.208976681049519)
dB = chrono.ChVectorD(-1,-5.55111512312578e-16,-1.11022302462516e-16)
link_20.SetFlipped(True)
link_20.Initialize(body_30,body_33,False,cA,cB,dA,dB)
link_20.SetName("Distance11")
exported_items.append(link_20)


# Mate constraint: Distance12 [MateDistanceDim] type:5 align:1 flip:True
#   Entity 0: C::E name: body_32 , SW name: Spibot-LEG-6/upper_limb_con-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_26 , SW name: Spibot-LEG-6/limb_body_connector-1 ,  SW ref.type:2 (2)

link_21 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(-0.0920354179295193,0.229937685578568,0.0997560645125223)
cB = chrono.ChVectorD(-0.0920854179295196,0.22995,0.010258559217533)
dA = chrono.ChVectorD(1,3.33066907387547e-16,2.22044604925031e-16)
dB = chrono.ChVectorD(-1,-1.11022302462516e-16,0)
link_21.Initialize(body_32,body_26,False,cA,cB,dB)
link_21.SetDistance(0)
link_21.SetName("Distance12")
exported_items.append(link_21)

link_22 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.0920354179295193,0.229937685578568,0.0997560645125223)
dA = chrono.ChVectorD(1,3.33066907387547e-16,2.22044604925031e-16)
cB = chrono.ChVectorD(-0.0920854179295196,0.22995,0.010258559217533)
dB = chrono.ChVectorD(-1,-1.11022302462516e-16,0)
link_22.SetFlipped(True)
link_22.Initialize(body_32,body_26,False,cA,cB,dA,dB)
link_22.SetName("Distance12")
exported_items.append(link_22)


# Mate constraint: Distance13 [MateDistanceDim] type:5 align:1 flip:True
#   Entity 0: C::E name: body_31 , SW name: Spibot-LEG-6/Actuator_body-2 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_32 , SW name: Spibot-LEG-6/upper_limb_con-1 ,  SW ref.type:2 (2)

link_23 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(-0.0969854179295196,0.19895,-0.0397414407824669)
cB = chrono.ChVectorD(-0.0969354179295193,0.185401294623342,0.0562640550292153)
dA = chrono.ChVectorD(-1,9.71445146547012e-16,2.77555756156289e-16)
dB = chrono.ChVectorD(1,3.33066907387547e-16,2.22044604925031e-16)
link_23.Initialize(body_31,body_32,False,cA,cB,dB)
link_23.SetDistance(0)
link_23.SetName("Distance13")
exported_items.append(link_23)

link_24 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.0969854179295196,0.19895,-0.0397414407824669)
dA = chrono.ChVectorD(-1,9.71445146547012e-16,2.77555756156289e-16)
cB = chrono.ChVectorD(-0.0969354179295193,0.185401294623342,0.0562640550292153)
dB = chrono.ChVectorD(1,3.33066907387547e-16,2.22044604925031e-16)
link_24.SetFlipped(True)
link_24.Initialize(body_31,body_32,False,cA,cB,dA,dB)
link_24.SetName("Distance13")
exported_items.append(link_24)


# Mate constraint: Distance14 [MateDistanceDim] type:5 align:1 flip:False
#   Entity 0: C::E name: body_28 , SW name: Spibot-LEG-6/limb_body_connector-2 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_26 , SW name: Spibot-LEG-6/limb_body_connector-1 ,  SW ref.type:2 (2)

link_25 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(-0.0845854179295196,0.20895,-0.0597414407824669)
cB = chrono.ChVectorD(-0.0845854179295196,0.22995,-0.059741440782467)
dA = chrono.ChVectorD(-1.11022302462516e-16,1,2.55351295663786e-15)
dB = chrono.ChVectorD(1.38777878078145e-16,-1,-1.36002320516582e-15)
link_25.Initialize(body_28,body_26,False,cA,cB,dB)
link_25.SetDistance(0)
link_25.SetName("Distance14")
exported_items.append(link_25)

link_26 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.0845854179295196,0.20895,-0.0597414407824669)
dA = chrono.ChVectorD(-1.11022302462516e-16,1,2.55351295663786e-15)
cB = chrono.ChVectorD(-0.0845854179295196,0.22995,-0.059741440782467)
dB = chrono.ChVectorD(1.38777878078145e-16,-1,-1.36002320516582e-15)
link_26.SetFlipped(True)
link_26.Initialize(body_28,body_26,False,cA,cB,dA,dB)
link_26.SetName("Distance14")
exported_items.append(link_26)


# Mate constraint: Concentric21 [MateConcentric] type:1 align:1 flip:False
#   Entity 0: C::E name: body_32 , SW name: Spibot-LEG-6/upper_limb_con-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_29 , SW name: Spibot-LEG-6/Actuator_body-1 ,  SW ref.type:2 (2)

link_27 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.0994354179295194,0.185401294623342,0.0562640550292152)
dA = chrono.ChVectorD(1,3.33066907387547e-16,2.22044604925031e-16)
cB = chrono.ChVectorD(-0.08683541792952,0.185401294623342,0.0562640550292151)
dB = chrono.ChVectorD(-1,9.43689570931383e-16,1.55431223447522e-15)
link_27.SetFlipped(True)
link_27.Initialize(body_32,body_29,False,cA,cB,dA,dB)
link_27.SetName("Concentric21")
exported_items.append(link_27)

link_28 = chrono.ChLinkMateGeneric()
link_28.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.0994354179295194,0.185401294623342,0.0562640550292152)
cB = chrono.ChVectorD(-0.08683541792952,0.185401294623342,0.0562640550292151)
dA = chrono.ChVectorD(1,3.33066907387547e-16,2.22044604925031e-16)
dB = chrono.ChVectorD(-1,9.43689570931383e-16,1.55431223447522e-15)
link_28.Initialize(body_32,body_29,False,cA,cB,dA,dB)
link_28.SetName("Concentric21")
exported_items.append(link_28)


# Mate constraint: Concentric22 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_32 , SW name: Spibot-LEG-6/upper_limb_con-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_27 , SW name: Spibot-LEG-6/Actuator_rod-2 ,  SW ref.type:2 (2)

link_29 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.0994354179295194,0.209004012344094,0.0416561203545952)
dA = chrono.ChVectorD(1,3.33066907387547e-16,2.22044604925031e-16)
cB = chrono.ChVectorD(-0.10218541792952,0.209004012344094,0.041656120354595)
dB = chrono.ChVectorD(1,-7.49400541621981e-16,-9.99200722162641e-16)
link_29.Initialize(body_32,body_27,False,cA,cB,dA,dB)
link_29.SetName("Concentric22")
exported_items.append(link_29)

link_30 = chrono.ChLinkMateGeneric()
link_30.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.0994354179295194,0.209004012344094,0.0416561203545952)
cB = chrono.ChVectorD(-0.10218541792952,0.209004012344094,0.041656120354595)
dA = chrono.ChVectorD(1,3.33066907387547e-16,2.22044604925031e-16)
dB = chrono.ChVectorD(1,-7.49400541621981e-16,-9.99200722162641e-16)
link_30.Initialize(body_32,body_27,False,cA,cB,dA,dB)
link_30.SetName("Concentric22")
exported_items.append(link_30)


# Mate constraint: Concentric3 [MateConcentric] type:1 align:1 flip:False
#   Entity 0: C::E name: body_34 , SW name: Spibot-LEG-2/upper_limb_con-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_41 , SW name: Spibot-LEG-2/lower_limb-1 ,  SW ref.type:2 (2)

link_1 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.00713541792952133,0.219973566770793,-0.398638372003085)
dA = chrono.ChVectorD(1,2.85882428840978e-15,3.77475828372553e-15)
cB = chrono.ChVectorD(0.00531458207045632,0.219973566770793,-0.398638372003076)
dB = chrono.ChVectorD(-1,-1.41553435639707e-15,-5.55111512312578e-16)
link_1.SetFlipped(True)
link_1.Initialize(body_34,body_41,False,cA,cB,dA,dB)
link_1.SetName("Concentric3")
exported_items.append(link_1)

link_2 = chrono.ChLinkMateGeneric()
link_2.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.00713541792952133,0.219973566770793,-0.398638372003085)
cB = chrono.ChVectorD(0.00531458207045632,0.219973566770793,-0.398638372003076)
dA = chrono.ChVectorD(1,2.85882428840978e-15,3.77475828372553e-15)
dB = chrono.ChVectorD(-1,-1.41553435639707e-15,-5.55111512312578e-16)
link_2.Initialize(body_34,body_41,False,cA,cB,dA,dB)
link_2.SetName("Concentric3")
exported_items.append(link_2)


# Mate constraint: Concentric4 [MateConcentric] type:1 align:1 flip:False
#   Entity 0: C::E name: body_41 , SW name: Spibot-LEG-2/lower_limb-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_35 , SW name: Spibot-LEG-2/Actuator_rod-1 ,  SW ref.type:2 (2)

link_3 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.00531458207045654,0.179985276194835,-0.399606161656244)
dA = chrono.ChVectorD(-1,-1.41553435639707e-15,-5.55111512312578e-16)
cB = chrono.ChVectorD(-0.00713541792952066,0.179985276194833,-0.399606161656257)
dB = chrono.ChVectorD(1,8.32667268468867e-16,-7.21644966006352e-16)
link_3.SetFlipped(True)
link_3.Initialize(body_41,body_35,False,cA,cB,dA,dB)
link_3.SetName("Concentric4")
exported_items.append(link_3)

link_4 = chrono.ChLinkMateGeneric()
link_4.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(0.00531458207045654,0.179985276194835,-0.399606161656244)
cB = chrono.ChVectorD(-0.00713541792952066,0.179985276194833,-0.399606161656257)
dA = chrono.ChVectorD(-1,-1.41553435639707e-15,-5.55111512312578e-16)
dB = chrono.ChVectorD(1,8.32667268468867e-16,-7.21644966006352e-16)
link_4.Initialize(body_41,body_35,False,cA,cB,dA,dB)
link_4.SetName("Concentric4")
exported_items.append(link_4)


# Mate constraint: Concentric6 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_35 , SW name: Spibot-LEG-2/Actuator_rod-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_36 , SW name: Spibot-LEG-2/Actuator_body-1 ,  SW ref.type:2 (2)

link_5 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.00473541792952059,0.184034626008242,-0.304692502122507)
dA = chrono.ChVectorD(4.9960036108132e-16,0.0426247348779925,0.999091152986844)
cB = chrono.ChVectorD(-0.00473541792952026,0.182723998158947,-0.335412615522319)
dB = chrono.ChVectorD(7.7715611723761e-16,0.0426247348779925,0.999091152986844)
link_5.Initialize(body_35,body_36,False,cA,cB,dA,dB)
link_5.SetName("Concentric6")
exported_items.append(link_5)

link_6 = chrono.ChLinkMateGeneric()
link_6.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.00473541792952059,0.184034626008242,-0.304692502122507)
cB = chrono.ChVectorD(-0.00473541792952026,0.182723998158947,-0.335412615522319)
dA = chrono.ChVectorD(4.9960036108132e-16,0.0426247348779925,0.999091152986844)
dB = chrono.ChVectorD(7.7715611723761e-16,0.0426247348779925,0.999091152986844)
link_6.Initialize(body_35,body_36,False,cA,cB,dA,dB)
link_6.SetName("Concentric6")
exported_items.append(link_6)


# Mate constraint: Concentric11 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_37 , SW name: Spibot-LEG-2/Actuator_rod-2 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_39 , SW name: Spibot-LEG-2/Actuator_body-2 ,  SW ref.type:2 (2)

link_7 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.00458541792952327,0.203182825640429,-0.186390756056826)
dA = chrono.ChVectorD(5.55111512312578e-16,-0.120427023841358,0.992722182651679)
cB = chrono.ChVectorD(-0.00458541792951928,0.207175621430481,-0.219304771741567)
dB = chrono.ChVectorD(1.11022302462516e-16,-0.120427023841358,0.992722182651679)
link_7.Initialize(body_37,body_39,False,cA,cB,dA,dB)
link_7.SetName("Concentric11")
exported_items.append(link_7)

link_8 = chrono.ChLinkMateGeneric()
link_8.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.00458541792952327,0.203182825640429,-0.186390756056826)
cB = chrono.ChVectorD(-0.00458541792951928,0.207175621430481,-0.219304771741567)
dA = chrono.ChVectorD(5.55111512312578e-16,-0.120427023841358,0.992722182651679)
dB = chrono.ChVectorD(1.11022302462516e-16,-0.120427023841358,0.992722182651679)
link_8.Initialize(body_37,body_39,False,cA,cB,dA,dB)
link_8.SetName("Concentric11")
exported_items.append(link_8)


# Mate constraint: Concentric12 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_34 , SW name: Spibot-LEG-2/upper_limb_con-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_38 , SW name: Spibot-LEG-2/limb_body_connector-1 ,  SW ref.type:2 (2)

link_9 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.00713541792952199,0.24095,-0.199741440782464)
dA = chrono.ChVectorD(1,2.85882428840978e-15,3.77475828372553e-15)
cB = chrono.ChVectorD(-0.0145854179295195,0.24095,-0.199741440782467)
dB = chrono.ChVectorD(1,1.74860126378462e-15,-2.22044604925031e-16)
link_9.Initialize(body_34,body_38,False,cA,cB,dA,dB)
link_9.SetName("Concentric12")
exported_items.append(link_9)

link_10 = chrono.ChLinkMateGeneric()
link_10.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.00713541792952199,0.24095,-0.199741440782464)
cB = chrono.ChVectorD(-0.0145854179295195,0.24095,-0.199741440782467)
dA = chrono.ChVectorD(1,2.85882428840978e-15,3.77475828372553e-15)
dB = chrono.ChVectorD(1,1.74860126378462e-15,-2.22044604925031e-16)
link_10.Initialize(body_34,body_38,False,cA,cB,dA,dB)
link_10.SetName("Concentric12")
exported_items.append(link_10)


# Mate constraint: Concentric13 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_39 , SW name: Spibot-LEG-2/Actuator_body-2 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_40 , SW name: Spibot-LEG-2/limb_body_connector-2 ,  SW ref.type:2 (2)

link_11 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.0121854179295191,0.19995,-0.159741440782467)
dA = chrono.ChVectorD(1,5.27355936696949e-16,-1.66533453693773e-16)
cB = chrono.ChVectorD(-0.0145854179295194,0.19995,-0.159741440782467)
dB = chrono.ChVectorD(1,1.77635683940025e-15,0)
link_11.Initialize(body_39,body_40,False,cA,cB,dA,dB)
link_11.SetName("Concentric13")
exported_items.append(link_11)

link_12 = chrono.ChLinkMateGeneric()
link_12.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.0121854179295191,0.19995,-0.159741440782467)
cB = chrono.ChVectorD(-0.0145854179295194,0.19995,-0.159741440782467)
dA = chrono.ChVectorD(1,5.27355936696949e-16,-1.66533453693773e-16)
dB = chrono.ChVectorD(1,1.77635683940025e-15,0)
link_12.Initialize(body_39,body_40,False,cA,cB,dA,dB)
link_12.SetName("Concentric13")
exported_items.append(link_12)


# Mate constraint: Concentric17 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_38 , SW name: Spibot-LEG-2/limb_body_connector-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_40 , SW name: Spibot-LEG-2/limb_body_connector-2 ,  SW ref.type:2 (2)

link_13 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.0045854179295195,0.23095,-0.139741440782467)
dA = chrono.ChVectorD(-1.77635683940025e-15,1,6.38378239159465e-16)
cB = chrono.ChVectorD(-0.0045854179295195,0.18995,-0.139741440782467)
dB = chrono.ChVectorD(-1.83186799063151e-15,1,-5.82867087928207e-16)
link_13.Initialize(body_38,body_40,False,cA,cB,dA,dB)
link_13.SetName("Concentric17")
exported_items.append(link_13)

link_14 = chrono.ChLinkMateGeneric()
link_14.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.0045854179295195,0.23095,-0.139741440782467)
cB = chrono.ChVectorD(-0.0045854179295195,0.18995,-0.139741440782467)
dA = chrono.ChVectorD(-1.77635683940025e-15,1,6.38378239159465e-16)
dB = chrono.ChVectorD(-1.83186799063151e-15,1,-5.82867087928207e-16)
link_14.Initialize(body_38,body_40,False,cA,cB,dA,dB)
link_14.SetName("Concentric17")
exported_items.append(link_14)


# Mate constraint: Parallel14 [MateParallel] type:3 align:0 flip:False
#   Entity 0: C::E name: body_34 , SW name: Spibot-LEG-2/upper_limb_con-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_35 , SW name: Spibot-LEG-2/Actuator_rod-1 ,  SW ref.type:2 (2)

link_15 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.00713541792952166,0.230461783385397,-0.299189906392774)
dA = chrono.ChVectorD(-1,-2.85882428840978e-15,-3.77475828372553e-15)
cB = chrono.ChVectorD(-0.00713541792952066,0.179985276194833,-0.399606161656257)
dB = chrono.ChVectorD(-1,-8.32667268468867e-16,7.21644966006352e-16)
link_15.Initialize(body_34,body_35,False,cA,cB,dA,dB)
link_15.SetName("Parallel14")
exported_items.append(link_15)


# Mate constraint: Parallel15 [MateParallel] type:3 align:0 flip:False
#   Entity 0: C::E name: body_34 , SW name: Spibot-LEG-2/upper_limb_con-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_37 , SW name: Spibot-LEG-2/Actuator_rod-2 ,  SW ref.type:2 (2)

link_16 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.00223541792952164,0.186133976949189,-0.255485323283369)
dA = chrono.ChVectorD(-1,-2.85882428840978e-15,-3.77475828372553e-15)
cB = chrono.ChVectorD(-0.00698541792952345,0.209806311951703,-0.240990476102668)
dB = chrono.ChVectorD(-1,-3.60822483003176e-16,8.88178419700125e-16)
link_16.Initialize(body_34,body_37,False,cA,cB,dA,dB)
link_16.SetName("Parallel15")
exported_items.append(link_16)


# Mate constraint: Distance10 [MateDistanceDim] type:5 align:1 flip:False
#   Entity 0: C::E name: body_34 , SW name: Spibot-LEG-2/upper_limb_con-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_41 , SW name: Spibot-LEG-2/lower_limb-1 ,  SW ref.type:2 (2)

link_17 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(-0.00713541792952166,0.230461783385397,-0.299189906392774)
cB = chrono.ChVectorD(-0.00718541792954364,0.230134822729004,-0.408474472721944)
dA = chrono.ChVectorD(-1,-2.85882428840978e-15,-3.77475828372553e-15)
dB = chrono.ChVectorD(1,1.19348975147204e-15,5.55111512312578e-16)
link_17.Initialize(body_34,body_41,False,cA,cB,dB)
link_17.SetDistance(0)
link_17.SetName("Distance10")
exported_items.append(link_17)

link_18 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.00713541792952166,0.230461783385397,-0.299189906392774)
dA = chrono.ChVectorD(-1,-2.85882428840978e-15,-3.77475828372553e-15)
cB = chrono.ChVectorD(-0.00718541792954364,0.230134822729004,-0.408474472721944)
dB = chrono.ChVectorD(1,1.19348975147204e-15,5.55111512312578e-16)
link_18.SetFlipped(True)
link_18.Initialize(body_34,body_41,False,cA,cB,dA,dB)
link_18.SetName("Distance10")
exported_items.append(link_18)


# Mate constraint: Distance11 [MateDistanceDim] type:5 align:1 flip:False
#   Entity 0: C::E name: body_35 , SW name: Spibot-LEG-2/Actuator_rod-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_41 , SW name: Spibot-LEG-2/lower_limb-1 ,  SW ref.type:2 (2)

link_19 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(-0.00713541792952066,0.179985276194833,-0.399606161656257)
cB = chrono.ChVectorD(-0.00718541792954364,0.230134822729004,-0.408474472721944)
dA = chrono.ChVectorD(-1,-8.32667268468867e-16,7.21644966006352e-16)
dB = chrono.ChVectorD(1,1.19348975147204e-15,5.55111512312578e-16)
link_19.Initialize(body_35,body_41,False,cA,cB,dB)
link_19.SetDistance(0)
link_19.SetName("Distance11")
exported_items.append(link_19)

link_20 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.00713541792952066,0.179985276194833,-0.399606161656257)
dA = chrono.ChVectorD(-1,-8.32667268468867e-16,7.21644966006352e-16)
cB = chrono.ChVectorD(-0.00718541792954364,0.230134822729004,-0.408474472721944)
dB = chrono.ChVectorD(1,1.19348975147204e-15,5.55111512312578e-16)
link_20.SetFlipped(True)
link_20.Initialize(body_35,body_41,False,cA,cB,dA,dB)
link_20.SetName("Distance11")
exported_items.append(link_20)


# Mate constraint: Distance12 [MateDistanceDim] type:5 align:1 flip:True
#   Entity 0: C::E name: body_34 , SW name: Spibot-LEG-2/upper_limb_con-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_38 , SW name: Spibot-LEG-2/limb_body_connector-1 ,  SW ref.type:2 (2)

link_21 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(-0.00713541792952166,0.230461783385397,-0.299189906392774)
cB = chrono.ChVectorD(-0.00708541792951956,0.23095,-0.209741440782467)
dA = chrono.ChVectorD(-1,-2.85882428840978e-15,-3.77475828372553e-15)
dB = chrono.ChVectorD(1,1.74860126378462e-15,-4.9960036108132e-16)
link_21.Initialize(body_34,body_38,False,cA,cB,dB)
link_21.SetDistance(0)
link_21.SetName("Distance12")
exported_items.append(link_21)

link_22 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.00713541792952166,0.230461783385397,-0.299189906392774)
dA = chrono.ChVectorD(-1,-2.85882428840978e-15,-3.77475828372553e-15)
cB = chrono.ChVectorD(-0.00708541792951956,0.23095,-0.209741440782467)
dB = chrono.ChVectorD(1,1.74860126378462e-15,-4.9960036108132e-16)
link_22.SetFlipped(True)
link_22.Initialize(body_34,body_38,False,cA,cB,dA,dB)
link_22.SetName("Distance12")
exported_items.append(link_22)


# Mate constraint: Distance13 [MateDistanceDim] type:5 align:1 flip:True
#   Entity 0: C::E name: body_39 , SW name: Spibot-LEG-2/Actuator_body-2 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_34 , SW name: Spibot-LEG-2/upper_limb_con-1 ,  SW ref.type:2 (2)

link_23 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(-0.0021854179295191,0.19995,-0.159741440782467)
cB = chrono.ChVectorD(-0.00223541792952164,0.186133976949189,-0.255485323283369)
dA = chrono.ChVectorD(1,5.27355936696949e-16,-1.66533453693773e-16)
dB = chrono.ChVectorD(-1,-2.85882428840978e-15,-3.77475828372553e-15)
link_23.Initialize(body_39,body_34,False,cA,cB,dB)
link_23.SetDistance(0)
link_23.SetName("Distance13")
exported_items.append(link_23)

link_24 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.0021854179295191,0.19995,-0.159741440782467)
dA = chrono.ChVectorD(1,5.27355936696949e-16,-1.66533453693773e-16)
cB = chrono.ChVectorD(-0.00223541792952164,0.186133976949189,-0.255485323283369)
dB = chrono.ChVectorD(-1,-2.85882428840978e-15,-3.77475828372553e-15)
link_24.SetFlipped(True)
link_24.Initialize(body_39,body_34,False,cA,cB,dA,dB)
link_24.SetName("Distance13")
exported_items.append(link_24)


# Mate constraint: Distance14 [MateDistanceDim] type:5 align:1 flip:False
#   Entity 0: C::E name: body_40 , SW name: Spibot-LEG-2/limb_body_connector-2 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_38 , SW name: Spibot-LEG-2/limb_body_connector-1 ,  SW ref.type:2 (2)

link_25 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(-0.0145854179295195,0.20995,-0.139741440782467)
cB = chrono.ChVectorD(-0.0145854179295195,0.23095,-0.139741440782467)
dA = chrono.ChVectorD(-1.83186799063151e-15,1,-5.82867087928207e-16)
dB = chrono.ChVectorD(1.77635683940025e-15,-1,-6.38378239159465e-16)
link_25.Initialize(body_40,body_38,False,cA,cB,dB)
link_25.SetDistance(0)
link_25.SetName("Distance14")
exported_items.append(link_25)

link_26 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.0145854179295195,0.20995,-0.139741440782467)
dA = chrono.ChVectorD(-1.83186799063151e-15,1,-5.82867087928207e-16)
cB = chrono.ChVectorD(-0.0145854179295195,0.23095,-0.139741440782467)
dB = chrono.ChVectorD(1.77635683940025e-15,-1,-6.38378239159465e-16)
link_26.SetFlipped(True)
link_26.Initialize(body_40,body_38,False,cA,cB,dA,dB)
link_26.SetName("Distance14")
exported_items.append(link_26)


# Mate constraint: Concentric21 [MateConcentric] type:1 align:1 flip:False
#   Entity 0: C::E name: body_34 , SW name: Spibot-LEG-2/upper_limb_con-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_36 , SW name: Spibot-LEG-2/Actuator_body-1 ,  SW ref.type:2 (2)

link_27 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.000264582070478303,0.186133976949189,-0.255485323283369)
dA = chrono.ChVectorD(-1,-2.85882428840978e-15,-3.77475828372553e-15)
cB = chrono.ChVectorD(-0.0123354179295203,0.186133976949187,-0.255485323283372)
dB = chrono.ChVectorD(1,6.93889390390723e-16,-1.33226762955019e-15)
link_27.SetFlipped(True)
link_27.Initialize(body_34,body_36,False,cA,cB,dA,dB)
link_27.SetName("Concentric21")
exported_items.append(link_27)

link_28 = chrono.ChLinkMateGeneric()
link_28.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(0.000264582070478303,0.186133976949189,-0.255485323283369)
cB = chrono.ChVectorD(-0.0123354179295203,0.186133976949187,-0.255485323283372)
dA = chrono.ChVectorD(-1,-2.85882428840978e-15,-3.77475828372553e-15)
dB = chrono.ChVectorD(1,6.93889390390723e-16,-1.33226762955019e-15)
link_28.Initialize(body_34,body_36,False,cA,cB,dA,dB)
link_28.SetName("Concentric21")
exported_items.append(link_28)


# Mate constraint: Concentric22 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_34 , SW name: Spibot-LEG-2/upper_limb_con-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_37 , SW name: Spibot-LEG-2/Actuator_rod-2 ,  SW ref.type:2 (2)

link_29 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.000264582070478192,0.209806311951705,-0.240990476102659)
dA = chrono.ChVectorD(-1,-2.85882428840978e-15,-3.77475828372553e-15)
cB = chrono.ChVectorD(0.00301458207047667,0.209806311951703,-0.240990476102668)
dB = chrono.ChVectorD(-1,-3.60822483003176e-16,8.88178419700125e-16)
link_29.Initialize(body_34,body_37,False,cA,cB,dA,dB)
link_29.SetName("Concentric22")
exported_items.append(link_29)

link_30 = chrono.ChLinkMateGeneric()
link_30.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(0.000264582070478192,0.209806311951705,-0.240990476102659)
cB = chrono.ChVectorD(0.00301458207047667,0.209806311951703,-0.240990476102668)
dA = chrono.ChVectorD(-1,-2.85882428840978e-15,-3.77475828372553e-15)
dB = chrono.ChVectorD(-1,-3.60822483003176e-16,8.88178419700125e-16)
link_30.Initialize(body_34,body_37,False,cA,cB,dA,dB)
link_30.SetName("Concentric22")
exported_items.append(link_30)


# Mate constraint: Concentric3 [MateConcentric] type:1 align:1 flip:False
#   Entity 0: C::E name: body_46 , SW name: Spibot-LEG-3/upper_limb_con-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_49 , SW name: Spibot-LEG-3/lower_limb-1 ,  SW ref.type:2 (2)

link_1 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.0828645820708273,0.219980219566137,-0.398731902648015)
dA = chrono.ChVectorD(1,1.85962356624714e-15,6.10622663543836e-16)
cB = chrono.ChVectorD(0.0953145820721624,0.219980219550366,-0.398731902655073)
dB = chrono.ChVectorD(-1,-1.4432899320127e-15,4.44089209850063e-16)
link_1.SetFlipped(True)
link_1.Initialize(body_46,body_49,False,cA,cB,dA,dB)
link_1.SetName("Concentric3")
exported_items.append(link_1)

link_2 = chrono.ChLinkMateGeneric()
link_2.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(0.0828645820708273,0.219980219566137,-0.398731902648015)
cB = chrono.ChVectorD(0.0953145820721624,0.219980219550366,-0.398731902655073)
dA = chrono.ChVectorD(1,1.85962356624714e-15,6.10622663543836e-16)
dB = chrono.ChVectorD(-1,-1.4432899320127e-15,4.44089209850063e-16)
link_2.Initialize(body_46,body_49,False,cA,cB,dA,dB)
link_2.SetName("Concentric3")
exported_items.append(link_2)


# Mate constraint: Concentric4 [MateConcentric] type:1 align:1 flip:False
#   Entity 0: C::E name: body_49 , SW name: Spibot-LEG-3/lower_limb-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_47 , SW name: Spibot-LEG-3/Actuator_rod-1 ,  SW ref.type:2 (2)

link_3 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.0953145820721624,0.179989901829091,-0.399611952966998)
dA = chrono.ChVectorD(-1,-1.4432899320127e-15,4.44089209850063e-16)
cB = chrono.ChVectorD(0.0828645820729169,0.179989901845129,-0.399611952964671)
dB = chrono.ChVectorD(1,1.4432899320127e-15,-5.55111512312578e-16)
link_3.SetFlipped(True)
link_3.Initialize(body_49,body_47,False,cA,cB,dA,dB)
link_3.SetName("Concentric4")
exported_items.append(link_3)

link_4 = chrono.ChLinkMateGeneric()
link_4.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(0.0953145820721624,0.179989901829091,-0.399611952966998)
cB = chrono.ChVectorD(0.0828645820729169,0.179989901845129,-0.399611952964671)
dA = chrono.ChVectorD(-1,-1.4432899320127e-15,4.44089209850063e-16)
dB = chrono.ChVectorD(1,1.4432899320127e-15,-5.55111512312578e-16)
link_4.Initialize(body_49,body_47,False,cA,cB,dA,dB)
link_4.SetName("Concentric4")
exported_items.append(link_4)


# Mate constraint: Concentric6 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_47 , SW name: Spibot-LEG-3/Actuator_rod-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_48 , SW name: Spibot-LEG-3/Actuator_body-1 ,  SW ref.type:2 (2)

link_5 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.085264582072917,0.183617950176413,-0.30468125579402)
dA = chrono.ChVectorD(5.55111512312578e-16,0.0381899824345665,0.99927049653317)
cB = chrono.ChVectorD(0.085264582074149,0.182433389747401,-0.335676197737383)
dB = chrono.ChVectorD(3.33066907387547e-16,0.0381899824345664,0.99927049653317)
link_5.Initialize(body_47,body_48,False,cA,cB,dA,dB)
link_5.SetName("Concentric6")
exported_items.append(link_5)

link_6 = chrono.ChLinkMateGeneric()
link_6.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(0.085264582072917,0.183617950176413,-0.30468125579402)
cB = chrono.ChVectorD(0.085264582074149,0.182433389747401,-0.335676197737383)
dA = chrono.ChVectorD(5.55111512312578e-16,0.0381899824345665,0.99927049653317)
dB = chrono.ChVectorD(3.33066907387547e-16,0.0381899824345664,0.99927049653317)
link_6.Initialize(body_47,body_48,False,cA,cB,dA,dB)
link_6.SetName("Concentric6")
exported_items.append(link_6)


# Mate constraint: Concentric11 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_43 , SW name: Spibot-LEG-3/Actuator_rod-2 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_42 , SW name: Spibot-LEG-3/Actuator_body-2 ,  SW ref.type:2 (2)

link_7 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.0854145820706589,0.202358033144078,-0.18654609825291)
dA = chrono.ChVectorD(3.88578058618805e-16,-0.122483397475925,0.992470562456517)
cB = chrono.ChVectorD(0.0854145820705983,0.206399003848558,-0.219289674530069)
dB = chrono.ChVectorD(7.21644966006352e-16,-0.122483397475926,0.992470562456517)
link_7.Initialize(body_43,body_42,False,cA,cB,dA,dB)
link_7.SetName("Concentric11")
exported_items.append(link_7)

link_8 = chrono.ChLinkMateGeneric()
link_8.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(0.0854145820706589,0.202358033144078,-0.18654609825291)
cB = chrono.ChVectorD(0.0854145820705983,0.206399003848558,-0.219289674530069)
dA = chrono.ChVectorD(3.88578058618805e-16,-0.122483397475925,0.992470562456517)
dB = chrono.ChVectorD(7.21644966006352e-16,-0.122483397475926,0.992470562456517)
link_8.Initialize(body_43,body_42,False,cA,cB,dA,dB)
link_8.SetName("Concentric11")
exported_items.append(link_8)


# Mate constraint: Concentric12 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_46 , SW name: Spibot-LEG-3/upper_limb_con-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_44 , SW name: Spibot-LEG-3/limb_body_connector-1 ,  SW ref.type:2 (2)

link_9 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.082864582070827,0.240050000000033,-0.19974144078279)
dA = chrono.ChVectorD(1,1.85962356624714e-15,6.10622663543836e-16)
cB = chrono.ChVectorD(0.0754145820704804,0.24005,-0.199741440782467)
dB = chrono.ChVectorD(1,7.7715611723761e-16,-3.88578058618805e-16)
link_9.Initialize(body_46,body_44,False,cA,cB,dA,dB)
link_9.SetName("Concentric12")
exported_items.append(link_9)

link_10 = chrono.ChLinkMateGeneric()
link_10.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(0.082864582070827,0.240050000000033,-0.19974144078279)
cB = chrono.ChVectorD(0.0754145820704804,0.24005,-0.199741440782467)
dA = chrono.ChVectorD(1,1.85962356624714e-15,6.10622663543836e-16)
dB = chrono.ChVectorD(1,7.7715611723761e-16,-3.88578058618805e-16)
link_10.Initialize(body_46,body_44,False,cA,cB,dA,dB)
link_10.SetName("Concentric12")
exported_items.append(link_10)


# Mate constraint: Concentric13 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_42 , SW name: Spibot-LEG-3/Actuator_body-2 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_45 , SW name: Spibot-LEG-3/limb_body_connector-2 ,  SW ref.type:2 (2)

link_11 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.0778145820705982,0.199050000000002,-0.159741440782678)
dA = chrono.ChVectorD(1,1.33226762955019e-15,-7.7715611723761e-16)
cB = chrono.ChVectorD(0.0754145820704804,0.19905,-0.159741440782467)
dB = chrono.ChVectorD(1,7.7715611723761e-16,-1.11022302462516e-16)
link_11.Initialize(body_42,body_45,False,cA,cB,dA,dB)
link_11.SetName("Concentric13")
exported_items.append(link_11)

link_12 = chrono.ChLinkMateGeneric()
link_12.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(0.0778145820705982,0.199050000000002,-0.159741440782678)
cB = chrono.ChVectorD(0.0754145820704804,0.19905,-0.159741440782467)
dA = chrono.ChVectorD(1,1.33226762955019e-15,-7.7715611723761e-16)
dB = chrono.ChVectorD(1,7.7715611723761e-16,-1.11022302462516e-16)
link_12.Initialize(body_42,body_45,False,cA,cB,dA,dB)
link_12.SetName("Concentric13")
exported_items.append(link_12)


# Mate constraint: Concentric17 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_44 , SW name: Spibot-LEG-3/limb_body_connector-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_45 , SW name: Spibot-LEG-3/limb_body_connector-2 ,  SW ref.type:2 (2)

link_13 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.0854145820704804,0.23005,-0.139741440782467)
dA = chrono.ChVectorD(-8.04911692853238e-16,1,4.9960036108132e-16)
cB = chrono.ChVectorD(0.0854145820704804,0.18905,-0.139741440782467)
dB = chrono.ChVectorD(-8.04911692853238e-16,1,-6.93889390390723e-16)
link_13.Initialize(body_44,body_45,False,cA,cB,dA,dB)
link_13.SetName("Concentric17")
exported_items.append(link_13)

link_14 = chrono.ChLinkMateGeneric()
link_14.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(0.0854145820704804,0.23005,-0.139741440782467)
cB = chrono.ChVectorD(0.0854145820704804,0.18905,-0.139741440782467)
dA = chrono.ChVectorD(-8.04911692853238e-16,1,4.9960036108132e-16)
dB = chrono.ChVectorD(-8.04911692853238e-16,1,-6.93889390390723e-16)
link_14.Initialize(body_44,body_45,False,cA,cB,dA,dB)
link_14.SetName("Concentric17")
exported_items.append(link_14)


# Mate constraint: Parallel14 [MateParallel] type:3 align:0 flip:False
#   Entity 0: C::E name: body_46 , SW name: Spibot-LEG-3/upper_limb_con-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_47 , SW name: Spibot-LEG-3/Actuator_rod-1 ,  SW ref.type:2 (2)

link_15 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.082864582070827,0.230015109783085,-0.299236671715402)
dA = chrono.ChVectorD(-1,-1.85962356624714e-15,-6.10622663543836e-16)
cB = chrono.ChVectorD(0.0828645820729169,0.179989901845129,-0.399611952964671)
dB = chrono.ChVectorD(-1,-1.4432899320127e-15,5.55111512312578e-16)
link_15.Initialize(body_46,body_47,False,cA,cB,dA,dB)
link_15.SetName("Parallel14")
exported_items.append(link_15)


# Mate constraint: Parallel15 [MateParallel] type:3 align:0 flip:False
#   Entity 0: C::E name: body_46 , SW name: Spibot-LEG-3/upper_limb_con-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_43 , SW name: Spibot-LEG-3/Actuator_rod-2 ,  SW ref.type:2 (2)

link_16 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.0877645820708272,0.185488588341557,-0.255734558013537)
dA = chrono.ChVectorD(-1,-1.85962356624714e-15,-6.10622663543836e-16)
cB = chrono.ChVectorD(0.0830145820706589,0.209094620005254,-0.241131979188019)
dB = chrono.ChVectorD(-1,-7.7715611723761e-16,4.44089209850063e-16)
link_16.Initialize(body_46,body_43,False,cA,cB,dA,dB)
link_16.SetName("Parallel15")
exported_items.append(link_16)


# Mate constraint: Distance10 [MateDistanceDim] type:5 align:1 flip:False
#   Entity 0: C::E name: body_46 , SW name: Spibot-LEG-3/upper_limb_con-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_49 , SW name: Spibot-LEG-3/lower_limb-1 ,  SW ref.type:2 (2)

link_17 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(0.082864582070827,0.230015109783085,-0.299236671715402)
cB = chrono.ChVectorD(0.0828145820721624,0.230119869981078,-0.408590274180988)
dA = chrono.ChVectorD(-1,-1.85962356624714e-15,-6.10622663543836e-16)
dB = chrono.ChVectorD(1,1.19348975147204e-15,-5.55111512312578e-16)
link_17.Initialize(body_46,body_49,False,cA,cB,dB)
link_17.SetDistance(0)
link_17.SetName("Distance10")
exported_items.append(link_17)

link_18 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.082864582070827,0.230015109783085,-0.299236671715402)
dA = chrono.ChVectorD(-1,-1.85962356624714e-15,-6.10622663543836e-16)
cB = chrono.ChVectorD(0.0828145820721624,0.230119869981078,-0.408590274180988)
dB = chrono.ChVectorD(1,1.19348975147204e-15,-5.55111512312578e-16)
link_18.SetFlipped(True)
link_18.Initialize(body_46,body_49,False,cA,cB,dA,dB)
link_18.SetName("Distance10")
exported_items.append(link_18)


# Mate constraint: Distance11 [MateDistanceDim] type:5 align:1 flip:False
#   Entity 0: C::E name: body_47 , SW name: Spibot-LEG-3/Actuator_rod-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_49 , SW name: Spibot-LEG-3/lower_limb-1 ,  SW ref.type:2 (2)

link_19 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(0.0828645820729169,0.179989901845129,-0.399611952964671)
cB = chrono.ChVectorD(0.0828145820721624,0.230119869981078,-0.408590274180988)
dA = chrono.ChVectorD(-1,-1.4432899320127e-15,5.55111512312578e-16)
dB = chrono.ChVectorD(1,1.19348975147204e-15,-5.55111512312578e-16)
link_19.Initialize(body_47,body_49,False,cA,cB,dB)
link_19.SetDistance(0)
link_19.SetName("Distance11")
exported_items.append(link_19)

link_20 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.0828645820729169,0.179989901845129,-0.399611952964671)
dA = chrono.ChVectorD(-1,-1.4432899320127e-15,5.55111512312578e-16)
cB = chrono.ChVectorD(0.0828145820721624,0.230119869981078,-0.408590274180988)
dB = chrono.ChVectorD(1,1.19348975147204e-15,-5.55111512312578e-16)
link_20.SetFlipped(True)
link_20.Initialize(body_47,body_49,False,cA,cB,dA,dB)
link_20.SetName("Distance11")
exported_items.append(link_20)


# Mate constraint: Distance12 [MateDistanceDim] type:5 align:1 flip:True
#   Entity 0: C::E name: body_46 , SW name: Spibot-LEG-3/upper_limb_con-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_44 , SW name: Spibot-LEG-3/limb_body_connector-1 ,  SW ref.type:2 (2)

link_21 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(0.082864582070827,0.230015109783085,-0.299236671715402)
cB = chrono.ChVectorD(0.0829145820704803,0.23005,-0.209741440782467)
dA = chrono.ChVectorD(-1,-1.85962356624714e-15,-6.10622663543836e-16)
dB = chrono.ChVectorD(1,7.7715611723761e-16,-6.10622663543836e-16)
link_21.Initialize(body_46,body_44,False,cA,cB,dB)
link_21.SetDistance(0)
link_21.SetName("Distance12")
exported_items.append(link_21)

link_22 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.082864582070827,0.230015109783085,-0.299236671715402)
dA = chrono.ChVectorD(-1,-1.85962356624714e-15,-6.10622663543836e-16)
cB = chrono.ChVectorD(0.0829145820704803,0.23005,-0.209741440782467)
dB = chrono.ChVectorD(1,7.7715611723761e-16,-6.10622663543836e-16)
link_22.SetFlipped(True)
link_22.Initialize(body_46,body_44,False,cA,cB,dA,dB)
link_22.SetName("Distance12")
exported_items.append(link_22)


# Mate constraint: Distance13 [MateDistanceDim] type:5 align:1 flip:True
#   Entity 0: C::E name: body_42 , SW name: Spibot-LEG-3/Actuator_body-2 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_46 , SW name: Spibot-LEG-3/upper_limb_con-1 ,  SW ref.type:2 (2)

link_23 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(0.0878145820705982,0.199050000000002,-0.159741440782678)
cB = chrono.ChVectorD(0.0877645820708272,0.185488588341557,-0.255734558013537)
dA = chrono.ChVectorD(1,1.33226762955019e-15,-7.7715611723761e-16)
dB = chrono.ChVectorD(-1,-1.85962356624714e-15,-6.10622663543836e-16)
link_23.Initialize(body_42,body_46,False,cA,cB,dB)
link_23.SetDistance(0)
link_23.SetName("Distance13")
exported_items.append(link_23)

link_24 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.0878145820705982,0.199050000000002,-0.159741440782678)
dA = chrono.ChVectorD(1,1.33226762955019e-15,-7.7715611723761e-16)
cB = chrono.ChVectorD(0.0877645820708272,0.185488588341557,-0.255734558013537)
dB = chrono.ChVectorD(-1,-1.85962356624714e-15,-6.10622663543836e-16)
link_24.SetFlipped(True)
link_24.Initialize(body_42,body_46,False,cA,cB,dA,dB)
link_24.SetName("Distance13")
exported_items.append(link_24)


# Mate constraint: Distance14 [MateDistanceDim] type:5 align:1 flip:False
#   Entity 0: C::E name: body_45 , SW name: Spibot-LEG-3/limb_body_connector-2 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_44 , SW name: Spibot-LEG-3/limb_body_connector-1 ,  SW ref.type:2 (2)

link_25 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(0.0754145820704804,0.20905,-0.139741440782467)
cB = chrono.ChVectorD(0.0754145820704804,0.23005,-0.139741440782467)
dA = chrono.ChVectorD(-8.04911692853238e-16,1,-6.93889390390723e-16)
dB = chrono.ChVectorD(8.04911692853238e-16,-1,-4.9960036108132e-16)
link_25.Initialize(body_45,body_44,False,cA,cB,dB)
link_25.SetDistance(0)
link_25.SetName("Distance14")
exported_items.append(link_25)

link_26 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.0754145820704804,0.20905,-0.139741440782467)
dA = chrono.ChVectorD(-8.04911692853238e-16,1,-6.93889390390723e-16)
cB = chrono.ChVectorD(0.0754145820704804,0.23005,-0.139741440782467)
dB = chrono.ChVectorD(8.04911692853238e-16,-1,-4.9960036108132e-16)
link_26.SetFlipped(True)
link_26.Initialize(body_45,body_44,False,cA,cB,dA,dB)
link_26.SetName("Distance14")
exported_items.append(link_26)


# Mate constraint: Concentric21 [MateConcentric] type:1 align:1 flip:False
#   Entity 0: C::E name: body_46 , SW name: Spibot-LEG-3/upper_limb_con-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_48 , SW name: Spibot-LEG-3/Actuator_body-1 ,  SW ref.type:2 (2)

link_27 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.0902645820708272,0.185488588341557,-0.255734558013537)
dA = chrono.ChVectorD(-1,-1.85962356624714e-15,-6.10622663543836e-16)
cB = chrono.ChVectorD(0.0776645820741491,0.185488588342166,-0.255734558014729)
dB = chrono.ChVectorD(1,1.11022302462516e-15,-6.10622663543836e-16)
link_27.SetFlipped(True)
link_27.Initialize(body_46,body_48,False,cA,cB,dA,dB)
link_27.SetName("Concentric21")
exported_items.append(link_27)

link_28 = chrono.ChLinkMateGeneric()
link_28.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(0.0902645820708272,0.185488588341557,-0.255734558013537)
cB = chrono.ChVectorD(0.0776645820741491,0.185488588342166,-0.255734558014729)
dA = chrono.ChVectorD(-1,-1.85962356624714e-15,-6.10622663543836e-16)
dB = chrono.ChVectorD(1,1.11022302462516e-15,-6.10622663543836e-16)
link_28.Initialize(body_46,body_48,False,cA,cB,dA,dB)
link_28.SetName("Concentric21")
exported_items.append(link_28)


# Mate constraint: Concentric22 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_46 , SW name: Spibot-LEG-3/upper_limb_con-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_43 , SW name: Spibot-LEG-3/Actuator_rod-2 ,  SW ref.type:2 (2)

link_29 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.0902645820708271,0.209094620005282,-0.241131979188044)
dA = chrono.ChVectorD(-1,-1.85962356624714e-15,-6.10622663543836e-16)
cB = chrono.ChVectorD(0.0930145820706588,0.209094620005254,-0.241131979188019)
dB = chrono.ChVectorD(-1,-7.7715611723761e-16,4.44089209850063e-16)
link_29.Initialize(body_46,body_43,False,cA,cB,dA,dB)
link_29.SetName("Concentric22")
exported_items.append(link_29)

link_30 = chrono.ChLinkMateGeneric()
link_30.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(0.0902645820708271,0.209094620005282,-0.241131979188044)
cB = chrono.ChVectorD(0.0930145820706588,0.209094620005254,-0.241131979188019)
dA = chrono.ChVectorD(-1,-1.85962356624714e-15,-6.10622663543836e-16)
dB = chrono.ChVectorD(-1,-7.7715611723761e-16,4.44089209850063e-16)
link_30.Initialize(body_46,body_43,False,cA,cB,dA,dB)
link_30.SetName("Concentric22")
exported_items.append(link_30)

