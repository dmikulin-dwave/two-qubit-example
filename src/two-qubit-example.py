import dimod
import dwave.inspector
from dwave.system import DWaveSampler, EmbeddingComposite

# Define problem as two Python dictionaries: h for linear terms, J for quadratic terms
# Let's put a tiny bias onto each qubit
h = {'A': 0.01 , 'B': 0.01}

# Now let's set the coupler between them to -1 or +1. Uncomment the desired line
J = {('A','B'): -1}
#J = {('A','B'): +1}

# Build the BQM
bqm = dimod.BQM.from_ising(h,J)

# Get sampler
sampler = EmbeddingComposite(DWaveSampler(solver="Advantage_system4.1"))

# Sample
sampleset = sampler.sample(bqm, num_reads=1000, label="two_qubit_demo")

# Print results
print(sampleset)  

# Inspect using the D-Wave Inspector
dwave.inspector.show(bqm, sampleset)
