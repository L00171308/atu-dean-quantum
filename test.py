import boto3
from braket.aws import AwsDevice
from braket.devices import LocalSimulator
from braket.circuits import Circuit

# create the circuit
bell = Circuit().h(0).cnot(0, 1)
print(bell)

local_sim = LocalSimulator()

result = local_sim.run(bell, shots=1000).result()
counts = result.measurement_counts
print(counts)

plt.bar(counts.keys(), counts.values());
plt.xlabel('bitstrings');
plt.ylabel('counts');
