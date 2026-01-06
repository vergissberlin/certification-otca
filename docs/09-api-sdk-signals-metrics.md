# Signals: Metrics

**Exam Weight**: The OpenTelemetry API and SDK (46%)

## Learning Objectives

- Understand metrics signal in detail
- Learn metric types (counter, gauge, histogram)
- Create and use metrics
- Understand metric aggregation
- Learn metric best practices

## Prerequisites

- System is running
- Understanding of metrics basics
- Access to Prometheus UI

## Exercise Tasks

### Task 1: Create Different Metric Types

**Description**: Create counter, gauge, and histogram metrics.

**Expected Outcome**:

- Create a counter metric
- Create a gauge metric
- Create a histogram metric
- Understand when to use each type

**Hints**:

- Counter: cumulative, increasing values
- Gauge: current value, can go up/down
- Histogram: distribution of values
- Use Meter API to create metrics

**Reference Files**:

- `service-node/app.js` (lines 19-20 for counter example)
- `service-python/app.py` (lines 21-22 for counter example)
- OpenTelemetry Metrics API documentation

### Task 2: Add Metric Labels

**Description**: Add labels to metrics for dimensionality.

**Expected Outcome**:

- Add labels to existing metrics
- Understand label cardinality
- Query labeled metrics in Prometheus
- Use labels effectively

**Hints**:

- Labels add dimensions to metrics
- High cardinality can be problematic
- Use labels for filtering and grouping
- Check Prometheus for labeled metrics

**Reference Files**:

- Both service files
- Prometheus UI for querying

### Task 3: Record Metric Values

**Description**: Record values for different metric types.

**Expected Outcome**:

- Record counter increments
- Record gauge values
- Record histogram observations
- Understand recording methods

**Hints**:

- Counter: `add(value)`
- Gauge: `record(value)`
- Histogram: `record(value)`
- Record at appropriate points

**Reference Files**:

- Both service files
- OpenTelemetry Metrics API

### Task 4: Understand Metric Aggregation

**Description**: Understand how metrics are aggregated.

**Expected Outcome**:

- Understand default aggregation
- Query aggregated metrics in Prometheus
- Use aggregation functions
- Understand temporal aggregation

**Hints**:

- Metrics aggregate over time
- Prometheus provides aggregation functions
- Use `sum()`, `rate()`, `avg()` in PromQL
- Understand aggregation intervals

**Reference Files**:

- Prometheus UI
- PromQL documentation

## Verification Steps

1. **Metric Types Verification**:
   - Verify all metric types appear in Prometheus
   - Understand differences between types
   - Know when to use each type

2. **Labels Verification**:
   - Verify labels in Prometheus
   - Query metrics by labels
   - Understand label impact

3. **Recording Verification**:
   - Verify metric values update
   - Check recording methods work
   - Understand value recording

4. **Aggregation Verification**:
   - Query aggregated metrics
   - Understand aggregation behavior
   - Use aggregation functions

## Solution

See [Solution: Signals - Metrics](../solutions/09-api-sdk-signals-metrics.md)
