//
// PROJECT CHRONO - http://projectchrono.org
//
// Copyright (c) 2013 Project Chrono
// All rights reserved.
//
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file at the top level of the distribution
// and at http://projectchrono.org/license-chrono.txt.
//

// A very simple Spider-inspired robot designed in solidworks and imported
// into chrono as a .py file using the Chrono::Engine add-in. The result is 
// visualized with Irrlicht.

#include "chrono/physics/ChSystem.h"
#include "chrono/physics/ChBodyEasy.h"
#include "chrono/physics/ChLinkMate.h"
#include "chrono/assets/ChTexture.h"
#include "chrono/assets/ChColorAsset.h"
#include "chrono_irrlicht/ChIrrApp.h"
#include "chrono_python/ChPython.h"
#include <irrlicht.h>

// Use the namespace of Chrono

using namespace chrono;
using namespace chrono::irrlicht;
using namespace chrono::collision;

// Use the main namespaces of Irrlicht

using namespace irr;
using namespace irr::core;
using namespace irr::scene;
using namespace irr::video;
using namespace irr::io;
using namespace irr::gui;

int main(int argc, char* argv[]) {
	// Create a Chrono::Engine physical system
	ChSystem mphysicalSystem;

	// Set the collision margins. This is expecially important for
	// very large or very small objects! Do this before creating shapes.
	ChCollisionModel::SetDefaultSuggestedEnvelope(0.001);
	ChCollisionModel::SetDefaultSuggestedMargin(0.001);

	//
	// LOAD THE SYSTEM
	//

	// The Python engine. This is necessary in order to parse the files that
	// have been saved using the SolidWorks add-in for Chrono::Engine.
	//D:\Documents\ME - Graduate\Research\Projects\Project Chrono\SpiderBot\ChFiles\Spiderbot_build\Release
	//D:\chrono_build\bin\data

	ChPythonEngine my_python;
	//std::string myFilePathChronoData("../../../../../../../../../chrono_build/bin/data/solid_works/Spider_Simple");
	//std::string myFilePathChronoData("../../../../../../../../../chrono_build/bin/data/solid_works/Spiderbot");
	//std::string myFilePathChronoData("../data/solid_works/Spiderbot");
	std::string myFilePathChronoData("../data/solid_works/Spiderbot_Test");
	try {
		// This is the instruction that loads the .py (as saved from SolidWorks) and
		// fills the system.
		//   In this example, we load a mechanical system that represents
		// a (quite simplified & approximated) clock escapement, that has been
		// modeled in SolidWorks and saved using the Chrono Add-in for SolidWorks.
		
		//my_python.ImportSolidWorksSystem(GetChronoDataFile("solid_works/Spider_Simple").c_str(),
		//	mphysicalSystem);  // note, don't type the .py suffix in filename..


		//my_python.ImportSolidWorksSystem(GetChronoDataFile("solid_works/swiss_escapement").c_str(),
		//	mphysicalSystem);

		// THIS MUST BE THE PATH FROM Spiderbot.exe TO THE LOCATION OF THE .py file.
		my_python.ImportSolidWorksSystem(myFilePathChronoData.c_str(),
			mphysicalSystem);
	}
	catch (ChException myerror) {
		GetLog() << myerror.what();
	}
	//std::cout << GetChronoDataFile("solid_works/swiss_escapement").c_str();
	// From this point, your ChSystem has been populated with objects and
	// assets load from the .py files. So you can proceed and fetch
	// single items, modify them, or add constraints between them, etc.
	// For example you can add other bodies, etc.

	// Log out all the names of the items inserted in the system:
	GetLog() << "SYSTEM ITEMS: \n";
	mphysicalSystem.ShowHierarchy(GetLog());

	ChSystem::IteratorPhysicsItems myiter = mphysicalSystem.IterBeginPhysicsItems();
	while (myiter.HasItem()) {
		GetLog() << "item:" << typeid(*myiter).name() << "\n";
		++myiter;
	}

	//Fetch all bodies in the system

	//BODY
	std::shared_ptr<ChPhysicsItem> Bodyp = mphysicalSystem.Search("Body-2");
	std::shared_ptr<ChPhysicsItem>  BM1p = mphysicalSystem.Search("Body-2^BM-1");
	std::shared_ptr<ChPhysicsItem>  BM2p = mphysicalSystem.Search("Body-2^BM-2");
	std::shared_ptr<ChPhysicsItem>  BM3p = mphysicalSystem.Search("Body-2^BM-3");
	std::shared_ptr<ChPhysicsItem>  BM4p = mphysicalSystem.Search("Body-2^BM-4");
	std::shared_ptr<ChPhysicsItem>  BM5p = mphysicalSystem.Search("Body-2^BM-5");
	std::shared_ptr<ChPhysicsItem>  BM6p = mphysicalSystem.Search("Body-2^BM-6");
	//
	auto Body = std::dynamic_pointer_cast<ChBody>(Bodyp);
	auto BM1 = std::dynamic_pointer_cast<ChMarker>(BM1p);
	auto BM2 = std::dynamic_pointer_cast<ChMarker>(BM2p);
	auto BM3 = std::dynamic_pointer_cast<ChMarker>(BM3p);
	auto BM4 = std::dynamic_pointer_cast<ChMarker>(BM4p);
	auto BM5 = std::dynamic_pointer_cast<ChMarker>(BM5p);
	auto BM6 = std::dynamic_pointer_cast<ChMarker>(BM6p);

	//LEG 1
	//Bodies
	std::shared_ptr<ChPhysicsItem> L1LLp = mphysicalSystem.Search("Spibot-LEG-1^lower_limb-1");
	std::shared_ptr<ChPhysicsItem> L1ULp = mphysicalSystem.Search("Spibot-LEG-1^upper_limb-1");
	std::shared_ptr<ChPhysicsItem> L1LB1p = mphysicalSystem.Search("Spibot-LEG-1^limb_body_connector-1");
	std::shared_ptr<ChPhysicsItem> L1LB2p = mphysicalSystem.Search("Spibot-LEG-1^limb_body_connector_b-2");
	std::shared_ptr<ChPhysicsItem> L1AB1p = mphysicalSystem.Search("Spibot-LEG-1^Actuator_body-1");
	std::shared_ptr<ChPhysicsItem> L1AB2p = mphysicalSystem.Search("Spibot-LEG-1^Actuator_body_b-2");
	std::shared_ptr<ChPhysicsItem> L1AR1p = mphysicalSystem.Search("Spibot-LEG-1^Actuator_rod-1");
	std::shared_ptr<ChPhysicsItem> L1AR2p = mphysicalSystem.Search("Spibot-LEG-1^Actuator_rod_b-2");
	//Markers
	std::shared_ptr<ChPhysicsItem> L1LLASp = mphysicalSystem.Search("Spibot-Leg-1^Actuator_rod-1^LL-Act-Shaft");
	std::shared_ptr<ChPhysicsItem> L1LLABp = mphysicalSystem.Search("Spibot-Leg-1^Actuator_body-1^LL-Act-Base");
	std::shared_ptr<ChPhysicsItem> L1ULASp = mphysicalSystem.Search("Spibot-Leg-1^Actuator_rod_b-2^UL-Act-Shaft");
	std::shared_ptr<ChPhysicsItem> L1ULABp = mphysicalSystem.Search("Spibot-Leg-1^Actuator_body_b-2^UL-Act-Base");
	std::shared_ptr<ChPhysicsItem> L1LBAp = mphysicalSystem.Search("Spibot-Leg-1^limb_body_connector_b-2^LB-B-Act-1");

	//LEG 2
	std::shared_ptr<ChPhysicsItem> L2LLp = mphysicalSystem.Search("Spibot-LEG-2^lower_limb-1");
	std::shared_ptr<ChPhysicsItem> L2ULp = mphysicalSystem.Search("Spibot-LEG-2^upper_limb-1");
	std::shared_ptr<ChPhysicsItem> L2LB1p = mphysicalSystem.Search("Spibot-LEG-2^limb_body_connector-1");
	std::shared_ptr<ChPhysicsItem> L2LB2p = mphysicalSystem.Search("Spibot-LEG-2^limb_body_connector_b-2");
	std::shared_ptr<ChPhysicsItem> L2AB1p = mphysicalSystem.Search("Spibot-LEG-2^Actuator_body-1");
	std::shared_ptr<ChPhysicsItem> L2AB2p = mphysicalSystem.Search("Spibot-LEG-2^Actuator_body_b-2");
	std::shared_ptr<ChPhysicsItem> L2AR1p = mphysicalSystem.Search("Spibot-LEG-2^Actuator_rod-1");
	std::shared_ptr<ChPhysicsItem> L2AR2p = mphysicalSystem.Search("Spibot-LEG-2^Actuator_rod_b-2");
	//Markers
	std::shared_ptr<ChPhysicsItem> L2LLASp = mphysicalSystem.Search("Spibot-Leg-2^Actuator_rod-1^LL-Act-Shaft");
	std::shared_ptr<ChPhysicsItem> L2LLABp = mphysicalSystem.Search("Spibot-Leg-2^Actuator_body-1^LL-Act-Base");
	std::shared_ptr<ChPhysicsItem> L2ULASp = mphysicalSystem.Search("Spibot-Leg-2^Actuator_rod_b-2^UL-Act-Shaft");
	std::shared_ptr<ChPhysicsItem> L2ULABp = mphysicalSystem.Search("Spibot-Leg-2^Actuator_body_b-2^UL-Act-Base");
	std::shared_ptr<ChPhysicsItem> L2LBAp = mphysicalSystem.Search("Spibot-Leg-2^limb_body_connector_b-2^LB-B-Act-1");

	//LEG 3
	std::shared_ptr<ChPhysicsItem> L3LLp = mphysicalSystem.Search("Spibot-LEG-3^lower_limb-1");
	std::shared_ptr<ChPhysicsItem> L3ULp = mphysicalSystem.Search("Spibot-LEG-3^upper_limb-1");
	std::shared_ptr<ChPhysicsItem> L3LB1p = mphysicalSystem.Search("Spibot-LEG-3^limb_body_connector-1");
	std::shared_ptr<ChPhysicsItem> L3LB2p = mphysicalSystem.Search("Spibot-LEG-3^limb_body_connector_b-2");
	std::shared_ptr<ChPhysicsItem> L3AB1p = mphysicalSystem.Search("Spibot-LEG-3^Actuator_body-1");
	std::shared_ptr<ChPhysicsItem> L3AB2p = mphysicalSystem.Search("Spibot-LEG-3^Actuator_body_b-2");
	std::shared_ptr<ChPhysicsItem> L3AR1p = mphysicalSystem.Search("Spibot-LEG-3^Actuator_rod-1");
	std::shared_ptr<ChPhysicsItem> L3AR2p = mphysicalSystem.Search("Spibot-LEG-3^Actuator_rod_b-2");
	//Markers
	std::shared_ptr<ChPhysicsItem> L3LLASp = mphysicalSystem.Search("Spibot-Leg-3^Actuator_rod-1^LL-Act-Shaft");
	std::shared_ptr<ChPhysicsItem> L3LLABp = mphysicalSystem.Search("Spibot-Leg-3^Actuator_body-1^LL-Act-Base");
	std::shared_ptr<ChPhysicsItem> L3ULASp = mphysicalSystem.Search("Spibot-Leg-3^Actuator_rod_b-2^UL-Act-Shaft");
	std::shared_ptr<ChPhysicsItem> L3ULABp = mphysicalSystem.Search("Spibot-Leg-3^Actuator_body_b-2^UL-Act-Base");
	std::shared_ptr<ChPhysicsItem> L3LBAp = mphysicalSystem.Search("Spibot-Leg-3^limb_body_connector_b-2^LB-B-Act-1");

	//LEG 4
	std::shared_ptr<ChPhysicsItem> L4LLp = mphysicalSystem.Search("Spibot-LEG-4^lower_limb-1");
	std::shared_ptr<ChPhysicsItem> L4ULp = mphysicalSystem.Search("Spibot-LEG-4^upper_limb-1");
	std::shared_ptr<ChPhysicsItem> L4LB1p = mphysicalSystem.Search("Spibot-LEG-4^limb_body_connector-1");
	std::shared_ptr<ChPhysicsItem> L4LB2p = mphysicalSystem.Search("Spibot-LEG-4^limb_body_connector_b-2");
	std::shared_ptr<ChPhysicsItem> L4AB1p = mphysicalSystem.Search("Spibot-LEG-4^Actuator_body-1");
	std::shared_ptr<ChPhysicsItem> L4AB2p = mphysicalSystem.Search("Spibot-LEG-4^Actuator_body_b-2");
	std::shared_ptr<ChPhysicsItem> L4AR1p = mphysicalSystem.Search("Spibot-LEG-4^Actuator_rod-1");
	std::shared_ptr<ChPhysicsItem> L4AR2p = mphysicalSystem.Search("Spibot-LEG-4^Actuator_rod_b-2");
	//Markers
	std::shared_ptr<ChPhysicsItem> L4LLASp = mphysicalSystem.Search("Spibot-Leg-4^Actuator_rod-1^LL-Act-Shaft");
	std::shared_ptr<ChPhysicsItem> L4LLABp = mphysicalSystem.Search("Spibot-Leg-4^Actuator_body-1^LL-Act-Base");
	std::shared_ptr<ChPhysicsItem> L4ULASp = mphysicalSystem.Search("Spibot-Leg-4^Actuator_rod_b-2^UL-Act-Shaft");
	std::shared_ptr<ChPhysicsItem> L4ULABp = mphysicalSystem.Search("Spibot-Leg-4^Actuator_body_b-2^UL-Act-Base");
	std::shared_ptr<ChPhysicsItem> L4LBAp = mphysicalSystem.Search("Spibot-Leg-4^limb_body_connector_b-2^LB-B-Act-1");
	
	//LEG 5
	std::shared_ptr<ChPhysicsItem> L5LLp = mphysicalSystem.Search("Spibot-LEG-5^lower_limb-1");
	std::shared_ptr<ChPhysicsItem> L5ULp = mphysicalSystem.Search("Spibot-LEG-5^upper_limb-1");
	std::shared_ptr<ChPhysicsItem> L5LB1p = mphysicalSystem.Search("Spibot-LEG-5^limb_body_connector-1");
	std::shared_ptr<ChPhysicsItem> L5LB2p = mphysicalSystem.Search("Spibot-LEG-5^limb_body_connector_b-2");
	std::shared_ptr<ChPhysicsItem> L5AB1p = mphysicalSystem.Search("Spibot-LEG-5^Actuator_body-1");
	std::shared_ptr<ChPhysicsItem> L5AB2p = mphysicalSystem.Search("Spibot-LEG-5^Actuator_body_b-2");
	std::shared_ptr<ChPhysicsItem> L5AR1p = mphysicalSystem.Search("Spibot-LEG-5^Actuator_rod-1");
	std::shared_ptr<ChPhysicsItem> L5AR2p = mphysicalSystem.Search("Spibot-LEG-5^Actuator_rod_b-2");
	//Markers
	std::shared_ptr<ChPhysicsItem> L5LLASp = mphysicalSystem.Search("Spibot-Leg-5^Actuator_rod-1^LL-Act-Shaft");
	std::shared_ptr<ChPhysicsItem> L5LLABp = mphysicalSystem.Search("Spibot-Leg-5^Actuator_body-1^LL-Act-Base");
	std::shared_ptr<ChPhysicsItem> L5ULASp = mphysicalSystem.Search("Spibot-Leg-5^Actuator_rod_b-2^UL-Act-Shaft");
	std::shared_ptr<ChPhysicsItem> L5ULABp = mphysicalSystem.Search("Spibot-Leg-5^Actuator_body_b-2^UL-Act-Base");
	std::shared_ptr<ChPhysicsItem> L5LBAp = mphysicalSystem.Search("Spibot-Leg-5^limb_body_connector_b-2^LB-B-Act-1");

	//LEG 6
	std::shared_ptr<ChPhysicsItem> L6LLp = mphysicalSystem.Search("Spibot-LEG-6^lower_limb-1");
	std::shared_ptr<ChPhysicsItem> L6ULp = mphysicalSystem.Search("Spibot-LEG-6^upper_limb-1");
	std::shared_ptr<ChPhysicsItem> L6LB1p = mphysicalSystem.Search("Spibot-LEG-6^limb_body_connector-1");
	std::shared_ptr<ChPhysicsItem> L6LB2p = mphysicalSystem.Search("Spibot-LEG-6^limb_body_connector_b-2");
	std::shared_ptr<ChPhysicsItem> L6AB1p = mphysicalSystem.Search("Spibot-LEG-6^Actuator_body-1");
	std::shared_ptr<ChPhysicsItem> L6AB2p = mphysicalSystem.Search("Spibot-LEG-6^Actuator_body_b-2");
	std::shared_ptr<ChPhysicsItem> L6AR1p = mphysicalSystem.Search("Spibot-LEG-6^Actuator_rod-1");
	std::shared_ptr<ChPhysicsItem> L6AR2p = mphysicalSystem.Search("Spibot-LEG-6^Actuator_rod_b-2");
	//Markers
	std::shared_ptr<ChPhysicsItem> L6LLASp = mphysicalSystem.Search("Spibot-Leg-6^Actuator_rod-1^LL-Act-Shaft");
	std::shared_ptr<ChPhysicsItem> L6LLABp = mphysicalSystem.Search("Spibot-Leg-6^Actuator_body-1^LL-Act-Base");
	std::shared_ptr<ChPhysicsItem> L6ULASp = mphysicalSystem.Search("Spibot-Leg-6^Actuator_rod_b-2^UL-Act-Shaft");
	std::shared_ptr<ChPhysicsItem> L6ULABp = mphysicalSystem.Search("Spibot-Leg-6^Actuator_body_b-2^UL-Act-Base");
	std::shared_ptr<ChPhysicsItem> L6LBAp = mphysicalSystem.Search("Spibot-Leg-6^limb_body_connector_b-2^LB-B-Act-1");
	
	//ChBodies
	//L1
	auto L1LL = std::dynamic_pointer_cast<ChBody>(L1LLp);
	auto L1UL = std::dynamic_pointer_cast<ChBody>(L1ULp);
	auto L1LB1 = std::dynamic_pointer_cast<ChBody>(L1LB1p);
	auto L1LB2 = std::dynamic_pointer_cast<ChBody>(L1LB2p);
	auto L1AB1 = std::dynamic_pointer_cast<ChBody>(L1AB1p);
	auto L1AB2 = std::dynamic_pointer_cast<ChBody>(L1AB2p);
	auto L1AR1 = std::dynamic_pointer_cast<ChBody>(L1AR1p);
	auto L1AR2 = std::dynamic_pointer_cast<ChBody>(L1AR2p);
	//L2
	auto L2LL = std::dynamic_pointer_cast<ChBody>(L2LLp);
	auto L2UL = std::dynamic_pointer_cast<ChBody>(L2ULp);
	auto L2LB1 = std::dynamic_pointer_cast<ChBody>(L2LB1p);
	auto L2LB2 = std::dynamic_pointer_cast<ChBody>(L2LB2p);
	auto L2AB1 = std::dynamic_pointer_cast<ChBody>(L2AB1p);
	auto L2AB2 = std::dynamic_pointer_cast<ChBody>(L2AB2p);
	auto L2AR1 = std::dynamic_pointer_cast<ChBody>(L2AR1p);
	auto L2AR2 = std::dynamic_pointer_cast<ChBody>(L2AR2p);
	//L3
	auto L3LL = std::dynamic_pointer_cast<ChBody>(L3LLp);
	auto L3UL = std::dynamic_pointer_cast<ChBody>(L3ULp);
	auto L3LB1 = std::dynamic_pointer_cast<ChBody>(L3LB1p);
	auto L3LB2 = std::dynamic_pointer_cast<ChBody>(L3LB2p);
	auto L3AB1 = std::dynamic_pointer_cast<ChBody>(L3AB1p);
	auto L3AB2 = std::dynamic_pointer_cast<ChBody>(L3AB2p);
	auto L3AR1 = std::dynamic_pointer_cast<ChBody>(L3AR1p);
	auto L3AR2 = std::dynamic_pointer_cast<ChBody>(L3AR2p);
	//L4
	auto L4LL = std::dynamic_pointer_cast<ChBody>(L4LLp);
	auto L4UL = std::dynamic_pointer_cast<ChBody>(L4ULp);
	auto L4LB1 = std::dynamic_pointer_cast<ChBody>(L4LB1p);
	auto L4LB2 = std::dynamic_pointer_cast<ChBody>(L4LB2p);
	auto L4AB1 = std::dynamic_pointer_cast<ChBody>(L4AB1p);
	auto L4AB2 = std::dynamic_pointer_cast<ChBody>(L4AB2p);
	auto L4AR1 = std::dynamic_pointer_cast<ChBody>(L4AR1p);
	auto L4AR2 = std::dynamic_pointer_cast<ChBody>(L4AR2p);
	//L5
	auto L5LL = std::dynamic_pointer_cast<ChBody>(L5LLp);
	auto L5UL = std::dynamic_pointer_cast<ChBody>(L5ULp);
	auto L5LB1 = std::dynamic_pointer_cast<ChBody>(L5LB1p);
	auto L5LB2 = std::dynamic_pointer_cast<ChBody>(L5LB2p);
	auto L5AB1 = std::dynamic_pointer_cast<ChBody>(L5AB1p);
	auto L5AB2 = std::dynamic_pointer_cast<ChBody>(L5AB2p);
	auto L5AR1 = std::dynamic_pointer_cast<ChBody>(L5AR1p);
	auto L5AR2 = std::dynamic_pointer_cast<ChBody>(L5AR2p);
	//L6
	auto L6LL = std::dynamic_pointer_cast<ChBody>(L6LLp);
	auto L6UL = std::dynamic_pointer_cast<ChBody>(L6ULp);
	auto L6LB1 = std::dynamic_pointer_cast<ChBody>(L6LB1p);
	auto L6LB2 = std::dynamic_pointer_cast<ChBody>(L6LB2p);
	auto L6AB1 = std::dynamic_pointer_cast<ChBody>(L6AB1p);
	auto L6AB2 = std::dynamic_pointer_cast<ChBody>(L6AB2p);
	auto L6AR1 = std::dynamic_pointer_cast<ChBody>(L6AR1p);
	auto L6AR2 = std::dynamic_pointer_cast<ChBody>(L6AR2p);
	//ChMarkers
	//L1
	auto L1LLAS = std::dynamic_pointer_cast<ChMarker>(L1LLASp);
	auto L1LLAB = std::dynamic_pointer_cast<ChMarker>(L1LLABp);
	auto L1ULAS = std::dynamic_pointer_cast<ChMarker>(L1ULASp);
	auto L1ULAB = std::dynamic_pointer_cast<ChMarker>(L1ULABp);
	auto L1LBA = std::dynamic_pointer_cast<ChMarker>(L1LBAp);
	//L2
	auto L2LLAS = std::dynamic_pointer_cast<ChMarker>(L2LLASp);
	auto L2LLAB = std::dynamic_pointer_cast<ChMarker>(L2LLABp);
	auto L2ULAS = std::dynamic_pointer_cast<ChMarker>(L2ULASp);
	auto L2ULAB = std::dynamic_pointer_cast<ChMarker>(L2ULABp);
	auto L2LBA = std::dynamic_pointer_cast<ChMarker>(L2LBAp);
	//L3
	auto L3LLAS = std::dynamic_pointer_cast<ChMarker>(L3LLASp);
	auto L3LLAB = std::dynamic_pointer_cast<ChMarker>(L3LLABp);
	auto L3ULAS = std::dynamic_pointer_cast<ChMarker>(L3ULASp);
	auto L3ULAB = std::dynamic_pointer_cast<ChMarker>(L3ULABp);
	auto L3LBA = std::dynamic_pointer_cast<ChMarker>(L3LBAp);
	//L4
	auto L4LLAS = std::dynamic_pointer_cast<ChMarker>(L4LLASp);
	auto L4LLAB = std::dynamic_pointer_cast<ChMarker>(L4LLABp);
	auto L4ULAS = std::dynamic_pointer_cast<ChMarker>(L4ULASp);
	auto L4ULAB = std::dynamic_pointer_cast<ChMarker>(L4ULABp);
	auto L4LBA = std::dynamic_pointer_cast<ChMarker>(L4LBAp);
	//L5
	auto L5LLAS = std::dynamic_pointer_cast<ChMarker>(L5LLASp);
	auto L5LLAB = std::dynamic_pointer_cast<ChMarker>(L5LLABp);
	auto L5ULAS = std::dynamic_pointer_cast<ChMarker>(L5ULASp);
	auto L5ULAB = std::dynamic_pointer_cast<ChMarker>(L5ULABp);
	auto L5LBA = std::dynamic_pointer_cast<ChMarker>(L5LBAp);
	//L6
	auto L6LLAS = std::dynamic_pointer_cast<ChMarker>(L6LLASp);
	auto L6LLAB = std::dynamic_pointer_cast<ChMarker>(L6LLABp);
	auto L6ULAS = std::dynamic_pointer_cast<ChMarker>(L6ULASp);
	auto L6ULAB = std::dynamic_pointer_cast<ChMarker>(L6ULABp);
	auto L6LBA = std::dynamic_pointer_cast<ChMarker>(L6LBAp);
	
	//Set up motion functions to be used by actuators
	auto rampup = std::make_shared<ChFunction_Ramp>();
	rampup->Set_ang(0.5);
	auto fconst = std::make_shared<ChFunction_Const>();
	fconst->Set_yconst(5.0);
	auto rampdown = std::make_shared<ChFunction_Ramp>();
	rampdown->Set_ang(-0.5);
	auto step_seq = std::make_shared<ChFunction_Sequence>();
	
	//step_seq->InsertFunct(rampup, 1.0, 1, true);
	step_seq->InsertFunct(fconst, 1.0, 1, true);
	//step_seq->InsertFunct(rampdown, 1.0, 1, true);

	auto repeat_seq = std::make_shared<ChFunction_Repeat>();
	repeat_seq->Set_fa(step_seq);
	repeat_seq->Set_window_length(1.0);
	repeat_seq->Set_window_start(0.0);
	repeat_seq->Set_window_phase(1.0);


	//Set up engine between actuator markers.
	auto L1LLact = std::make_shared<ChLinkLinActuator>();
	//	L1LLact->Initialize(L1AR1, L1AB1, ChCoordsys<>(ChVector<>(0, 0, 0)));
	L1LLact->Initialize(L1LLAS, L1LLAB);
	L1LLact->Set_dist_funct(repeat_seq);
	//	L1LLact->SetUpMarkers( L1LLAS, L1LLAB);

	auto L1ULact = std::make_shared<ChLinkLinActuator>();
	L1LLact->Initialize(L1ULAS, L1ULAB);
	L1LLact->Set_dist_funct(repeat_seq);
	GetLog() << "\n\n Body1:" << L1LLact->GetBody1() << "\n\n";
	GetLog() << "\n Body2:" << L1LLact->GetBody2() << "\n\n";


	//auto L1LLact = std::make_shared<ChLinkMarkers>();
	//L1LLact->Initialize(L1AR1, L1AB1, ChCoordsys<>(ChVector<>(0, 0, 0)));
	//L1LLact->SetUpMarkers(L1LLAS, L1LLAB);

	//Add Floor
	auto mrigidFloor = std::make_shared<ChBodyEasyBox>(3, 0.1, 3,  // x,y,z size
		1000,         // density
		true,         // collide enable
		true);        // visualization
	mrigidFloor->SetPos(ChVector<>(0, -1.125, 0));
	mrigidFloor->SetBodyFixed(true);
	auto ftexture = std::make_shared<ChTexture>(GetChronoDataFile("../data/concrete.jpg"));
	mrigidFloor->AddAsset(ftexture);
	mphysicalSystem.Add(mrigidFloor);

	//Add a torsional spring to 

	//std::shared_ptr<ChPhysicsItem> myitemA = mphysicalSystem.Search("truss^escapement-1");
	//std::shared_ptr<ChPhysicsItem> myitemB = mphysicalSystem.Search("balance^escapement-1");
	//std::shared_ptr<ChPhysicsItem> myitemC = mphysicalSystem.Search("anchor^escapement-1");
	//auto mescape_wheel = std::dynamic_pointer_cast<ChBody>(myitemE);
	//auto mtruss = std::dynamic_pointer_cast<ChBody>(myitemA);
	//auto mbalance = std::dynamic_pointer_cast<ChBody>(myitemB);
	//auto manchor = std::dynamic_pointer_cast<ChBody>(myitemC);

	//if (mescape_wheel && mtruss && mbalance && manchor) {

	//	 Set a constant torque to escape wheel, in a
	//	 very simple way:
	//	mescape_wheel->Set_Scr_torque(ChVector<>(0, -0.03, 0));

	//	 Add a torsional spring
	//	std::shared_ptr<ChLinkLockFree> mspring(new ChLinkLockFree);
	//	mspring->Initialize(mtruss, mbalance, CSYSNORM);  // origin does not matter, it's only torque
	//	mspring->GetForce_Ry()->Set_K(0.24);
	//	mspring->GetForce_Ry()->Set_active(1);
	//	mphysicalSystem.Add(mspring);

	//	 Set an initial angular velocity to the balance:
	//	mbalance->SetWvel_par(ChVector<>(0, 5, 0));

	//	 Set no friction in all parts
	//	mbalance->GetMaterialSurface()->SetFriction(0);
	//	mescape_wheel->GetMaterialSurface()->SetFriction(0);
	//	manchor->GetMaterialSurface()->SetFriction(0);
	//}
	//else
	//	GetLog() << "Error: cannot one or more objects from their names in the C::E system! \n\n";

	//
	// THE VISUALIZATION
	//

	// Now, suppose one is interested in showing an animation of
	// the simulated system. There are different options, for instance
	// one could use the unit_POSTPROCESSING approach for rendering in
	// POVray, or you can open an Irrlicht 3D realtime view and show
	// it, as in the following example code:

	// Create the Irrlicht visualization (open the Irrlicht device,
	// bind a simple user interface, etc. etc.)
	ChIrrApp application(&mphysicalSystem, L"Import a SolidWorks system", core::dimension2d<u32>(800, 600), false);

	// Easy shortcuts to add camera, lights, logo and sky in Irrlicht scene:
	application.AddTypicalLogo();
	application.AddTypicalSky();
	application.AddTypicalCamera(vector3df(0, 0.25, 0.25), vector3df(0, 0, -0.1));
	application.AddLightWithShadow(vector3df(-0.5, 0.5, 0), vector3df(0, 0, 0), 1, 0.2, 1.2, 30, 512,
		video::SColorf(1, 0.9, 0.9));
	application.AddLightWithShadow(vector3df(0.5, 0.5, 0.5), vector3df(0, 0, 0), 1, 0.2, 1.2, 30, 512,
		video::SColorf(0.6, 0.8, 1));

	// ==IMPORTANT!== Use this function for adding a ChIrrNodeAsset to all items
	// in the system. These ChIrrNodeAsset assets are 'proxies' to the Irrlicht meshes.
	// If you need a finer control on which item really needs a visualization proxy in
	// Irrlicht, just use application.AssetBind(myitem); on a per-item basis.

	application.AssetBindAll();

	// ==IMPORTANT!== Use this function for 'converting' into Irrlicht meshes the assets
	// that you added to the bodies into 3D shapes, they can be visualized by Irrlicht!

	application.AssetUpdateAll();

	// This is to enable shadow maps (shadow casting with soft shadows) in Irrlicht
	// for all objects (or use application.AddShadow(..) for enable shadow on a per-item basis)

	application.AddShadowAll();

	//
	// THE SIMULATION LOOP
	//

	// set a low stabilization value because objects are small!

	mphysicalSystem.SetSolverType(ChSolver::Type::MINRES);
	mphysicalSystem.SetMaxItersSolverSpeed(44);
	application.GetSystem()->SetMaxPenetrationRecoverySpeed(0.1);
	application.SetStepManage(true);
	application.SetTimestep(0.0005);
	application.SetTryRealtime(true);

	while (application.GetDevice()->run()) {
		application.BeginScene();

		application.DrawAll();

		application.DoStep();

		application.EndScene();
	}
	//std::cout << "Press ENTER to continue...";
	//std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');

	return 0;
}