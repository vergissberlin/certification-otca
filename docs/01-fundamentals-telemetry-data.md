# Telemetry Data

**Exam Weight**: Fundamentals of Observability (18%)

## Learning Objectives

- Understand the three types of telemetry data: traces, metrics, and logs
- Identify telemetry data in the system
- Differentiate between different telemetry signal types
- Understand when to use each type of telemetry

## Prerequisites

- System is running (`docker-compose up`)
- Basic understanding of observability concepts
- Access to Jaeger UI (<http://localhost:16686>) and Prometheus UI (<http://localhost:9090>)

## Exercise Tasks

### Task 1: Identify Telemetry Types in the System

**Description**: Examine the current system and identify what types of telemetry data are being generated.

**Expected Outcome**:

- List all telemetry types currently generated
- Identify which services generate which types
- Document the differences between the telemetry types you observe

**Hints**:

- Check `service-node/app.js` and `service-python/app.py`
- Look at what's exported to the Collector
- Examine Jaeger UI and Prometheus UI

**Reference Files**:

- `service-node/app.js`
- `service-python/app.py`
- `otel-config.yaml`

### Task 2: Generate and Observe Traces

**Description**: Generate trace data and observe it in Jaeger UI.

**Expected Outcome**:

- Generate multiple traces by making requests
- View traces in Jaeger UI
- Identify span structure and hierarchy
- Understand trace context and span relationships

**Hints**:

- Make requests to both services: `curl http://localhost:3000/hello` and `curl http://localhost:5000/hello`
- In Jaeger, look for service names and trace structure
- Examine span details and attributes

**Reference Files**:

- `service-node/app.js` (lines 12-14, 26-29)
- `service-python/app.py` (lines 13-16, 24-28)

### Task 3: Generate and Observe Metrics

**Description**: Generate metric data and observe it in Prometheus UI.

**Expected Outcome**:

- Generate metrics by making requests
- Query metrics in Prometheus
- Understand metric types (counter, gauge, histogram)
- View metric values over time

**Hints**:

- Make multiple requests to generate metric data
- In Prometheus, query: `requests_total`
- Try different time ranges
- Examine metric labels

**Reference Files**:

- `service-node/app.js` (lines 16-20, 27)
- `service-python/app.py` (lines 19-22, 27)
- `prometheus.yml`

### Task 4: Compare Traces vs Metrics

**Description**: Create a comparison document explaining when to use traces vs metrics.

**Expected Outcome**:

- Document use cases for traces
- Document use cases for metrics
- Explain the differences in data structure
- Provide examples from the system

**Hints**:

- Traces show request flows and timing
- Metrics show aggregated measurements
- Consider what questions each answers

## Verification Steps

1. **Traces Verification**:
   - Open Jaeger UI (<http://localhost:16686>)
   - Search for traces from both services
   - Verify you can see span details and timing information

2. **Metrics Verification**:
   - Open Prometheus UI (<http://localhost:9090>)
   - Query `requests_total`
   - Verify metric values increase with requests
   - Check metric labels (service names)

3. **Comparison Verification**:
   - Can you answer: "How long did request X take?" (traces)
   - Can you answer: "How many requests per second?" (metrics)
   - Understand when each is appropriate

## Solution

See [Solution: Telemetry Data](../solutions/01-fundamentals-telemetry-data.md)
