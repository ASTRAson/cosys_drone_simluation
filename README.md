# Using cosys and unreal for synthetic dataset generation to train ML models with YOLO

This repository contains the simulation and detection framework for object monitoring using drones.

##  Overview
The project uses **Unreal Engine 5.5.4** integrated with **Cosys-AirSim** to create a realistic virtual environment where a machine learning model is trained and tested for object detection.

## Technologies Used
* **Simulator:** Unreal Engine 5.5.4 + Cosys-AirSim
* **Language:** Python 3.9
* **Computer Vision:** YOLO (Trained via Roboflow)
* **Reference Hardware:** Dell G15 (GTX 1650, 16GB RAM, Intel i5-10500H)

## Repository Structure
* `/simulation`: AirSim configurations (`settings.json`).
* `/scripts`: Python scripts for drone control, telemetry collection, and model training using Ultralytics.
* `/results`: Model weights (`.pt`) and inference scripts.

## Dataset and Model
The dataset used was synthetically generated within the virtual environment and labeled via **Roboflow**.
> [https://app.roboflow.com/ufpa-qpnhs/abacaxi_deteccao_drone/models/abacaxi_deteccao_drone/1](https://app.roboflow.com/ufpa-qpnhs/abacaxi_deteccao_drone/models/abacaxi_deteccao_drone/1)

## How to Start (Installation Guide)

Follow these steps to set up the environment on your machine.


### 1. Python Environment Setup
I recommend using a virtual environment to manage dependencies:

# Create virtual environment
```bash
python -m venv venv
```
# Activate environment
```bash
.\venv\Scripts\activate
```
# clone this repository
```
git clone https://github.com/ASTRAson/cosys_drone_simluation.git
```

### 2. Cloning the Original Cosys-AirSim Repository
To use the simulator framework, you must clone the official **Cosys-AirSim** repository, which contains the core plugin and environment source code.

# Clone the official Cosys-AirSim repository with submodules
```bash
git clone https://github.com/cosys-lab/Cosys-AirSim.git
```
# in your terminal run the requirements.txt script to install all the necessary packages
```bash
pip install -r requirements.txt
```

### 3. Visual Studio 2022 Configuration
To compile the environment and the Cosys-AirSim plugin, you must install **Visual Studio 2022** with specific workloads.

* **Workloads Required**:
    * **Desktop development with C++**: Essential for core C++ compilation of the simulator components.
    * **Game development with C++**: Required for Unreal Engine 5.5.4 integration and project building.
* **Individual Components**:
    * **MSVC v143** (Latest).
    * **Windows 10/11 SDK** (Match your current OS version).
    * **.NET Framework 4.8.1 targeting pack**.

### 4. Simulator Configuration (AirSim)
To ensure the drone and sensors operate correctly for remote area monitoring, you must link your `settings.json`.
1. Locate your AirSim folder at `Documents/AirSim`.
2. Copy the `settings.json` file provided in the `/simulation/settings/` folder of this repository into that directory.

### 5. Running the Project
1. Open the `drone.uproject` file in **Unreal Engine 5.5.4**.
2. If prompted to rebuild missing modules (such as the AirSim plugin), click **Yes**.
3. This will open a blank unreal map, and you can build your environment as you desire from there.
4. Press **Play** in the editor.
5. Once you've set up your environment to your liking, run the simulation and then, while the simulation is running, execute your control script from the `/scripts` directory:
   ```bash
   python scripts/drone.py

