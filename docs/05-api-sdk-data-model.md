# Data Model

**Exam Weight**: The OpenTelemetry API and SDK (46%)

## Learning Objectives

- Understand OpenTelemetry data model components
- Learn about Spans, Metrics, Logs, and Resources
- Understand span structure and lifecycle
- Understand metric data points
- Learn about resource attributes

## Prerequisites

- System is running
- Understanding of telemetry data fundamentals
- Basic knowledge of OpenTelemetry concepts

## Exercise Tasks

### Task 1: Examine Span Data Model

**Description**: Understand the span data model by examining spans in the system.

**Expected Outcome**:

- Identify span components: name, start time, end time, status
- Understand span attributes and events
- Understand span relationships (parent-child)
- Document span structure

**Hints**:

- Check Jaeger UI for span details
- Look at code where spans are created
- Understand span lifecycle: start → add attributes/events → end
- Spans represent operations

**Reference Files**:

- `service-python/app.py` (line 26)
- `service-node/app.js`
- Jaeger UI span details

### Task 2: Examine Metric Data Model

**Description**: Understand the metric data model by examining metrics in the system.

**Expected Outcome**:

- Identify metric components: name, type, value, labels
- Understand different metric types (counter, gauge, histogram)
- Understand metric data points
- Document metric structure

**Hints**:

- Check Prometheus for metric structure
- Look at code where metrics are created
- Current system uses counters
- Metrics have labels for dimensionality

**Reference Files**:

- `service-node/app.js` (lines 19-20, 27)
- `service-python/app.py` (lines 21-22, 27)
- Prometheus UI

### Task 3: Understand Resource Model

**Description**: Examine and understand the resource data model.

**Expected Outcome**:

- Identify resource attributes
- Understand resource identification
- Learn how resources group telemetry
- Add resource attributes

**Hints**:

- Resources identify the source of telemetry
- Check `service-python/app.py` for resource creation
- Resource attributes apply to all telemetry from that resource
- Use semantic conventions for resource attributes

**Reference Files**:

- `service-python/app.py` (line 13)
- OpenTelemetry resource documentation

### Task 4: Create Different Metric Types

**Description**: Extend the system to use different metric types.

**Expected Outcome**:

- Add a gauge metric to track current value
- Add a histogram metric to track distribution
- Understand when to use each metric type
- Verify metrics in Prometheus

**Hints**:

- Counter: cumulative values (requests_total)
- Gauge: current value (memory usage)
- Histogram: distribution (response time)
- Use Meter API to create different types

**Reference Files**:

- `service-node/app.js` (Meter API usage)
- `service-python/app.py` (Meter API usage)
- OpenTelemetry metrics documentation

## Verification Steps

1. **Span Model Verification**:
   - Verify you understand span components
   - Check span structure in Jaeger
   - Understand span lifecycle

2. **Metric Model Verification**:
   - Verify metric structure in Prometheus
   - Understand metric types
   - Check metric labels

3. **Resource Model Verification**:
   - Verify resource attributes in traces
   - Understand resource identification
   - Check resource grouping

4. **Metric Types Verification**:
   - Verify new metric types appear in Prometheus
   - Understand differences between types
   - Know when to use each type

## Solution

See [Solution: Data Model](../solutions/05-api-sdk-data-model.md)
