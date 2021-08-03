import qiskit
import qiskit_superstaq as qss

# SuperstaQ token retrieved through API
token = "ya29.a0ARrdaM9-JrnWggt7-G-JSsz8l28KI81BSvRJycfFUyFIqljgCJlUhQ11qR0qwwsYkITwrwaYFYJrxEcMVc_ErywO_5pSLRdde7Rpwo5DMztXyXuFFf718fay0FyVF1vDJMRn1M9HShnXHaohs-F_god37VIMgw"

# Create provider using authorization token
superstaq = qss.superstaq_provider.SuperstaQProvider(token, url = "https://127.0.0.1:5000")

# Retrieve backend from superstaq provider
backend = superstaq.get_backend("ibmq_qasm_simulator")

# Standard bell circuit
qc1 = qiskit.QuantumCircuit(2, 2)
qc1.h(0)
qc1.cx(0, 1)
qc1.measure([0, 1], [0, 1])

# 3-qubit GHZ state
qc2 = qiskit.QuantumCircuit(3, 3)
qc2.h(0)
qc2.cx(0, 1)
qc2.cx(0, 2)
qc2.measure([0, 1, 2], [0, 1, 2])


"""
Submit list of jobs to backend. Circuits submitted simultaneously
will run with the same backend and the same number of shots.
"""
job = backend.run([qc1, qc2], shots=100)

# List of result counts
print(job.result().get_counts())

# ith result counts (0-indexed)
print(job.result().get_counts(1))

# The status of the circuit furthest behind in the queue.
print(job.status())
