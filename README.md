# two-qubit-example

## Description
This is a very simple two qubit example that can be used to demonstrate how biasing the coupler between two qubits results in either the two qubits sampled after annealing having the same spin or the opposite spin as indicated by the Ising model.

## Installation
Recommend installing this into a Python virtual environment:
```
python3 -m venv <my_env>
```

This has been tested with Python 3.6 through Python 3.9. Once installed into the virtual environment, activate the virtual environment using:
```
source <my_env>/bin/activate
```
Install the requirements using:
```
cd <my_env>
pip install -r src/requirements.txt
```
Finally, you need to install the D-Wave Inspector:
```
dwave install inspector
```

## Configuration
You need to set specify an API token to run the example using a D-Wave quantum computer. Use the command:
```
dwave config create
```

and enter your API token, available from the D-Wave Leap dashboard, when prompted. If you haven't registered for Leap already, it's easy and free - sign up here: https://cloud.dwavesys.com/leap/signup/

## Running
Start the example using:
```
python two-qubit-example.py
```
Try changing the line which sets the coupler to the commented one, run again, and observe the difference in the qubits sampled. 

