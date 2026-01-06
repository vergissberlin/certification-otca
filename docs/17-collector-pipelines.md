# Collector Pipelines

**Exam Weight**: The OpenTelemetry Collector (26%)

## Learning Objectives

- Understand Collector pipeline architecture
- Learn pipeline components
- Configure pipelines
- Understand pipeline flow
- Learn pipeline best practices

## Prerequisites

- System is running
- Understanding of Collector configuration
- Access to `otel-config.yaml`

## Exercise Tasks

### Task 1: Understand Pipeline Architecture

**Description**: Understand how Collector pipelines work.

**Expected Outcome**:

- Understand pipeline concept
- Learn pipeline components
- Understand data flow
- Document pipeline architecture

**Hints**:

- Pipelines: receivers → processors → exporters
- Separate pipelines for each signal
- Defined in service.pipelines
- Data flows through pipeline

**Reference Files**:

- `otel-config.yaml` (lines 16-25)
- OpenTelemetry Collector pipelines documentation

### Task 2: Examine Current Pipelines

**Description**: Examine the pipelines currently configured.

**Expected Outcome**:

- Identify trace pipeline
- Identify metrics pipeline
- Understand pipeline composition
- Document pipeline flow

**Hints**:

- Trace pipeline: otlp → batch → jaeger
- Metrics pipeline: otlp → batch → prometheus
- Check `otel-config.yaml`
- Understand each stage

**Reference Files**:

- `otel-config.yaml` (lines 17-25)

### Task 3: Modify Pipeline Components

**Description**: Modify pipeline component order or composition.

**Expected Outcome**:

- Add processors to pipeline
- Remove processors from pipeline
- Reorder pipeline components
- Understand component order impact

**Hints**:

- Processor order matters
- Some processors depend on others
- Add/remove in pipeline definition
- Test pipeline changes

**Reference Files**:

- `otel-config.yaml`
- Processor documentation

### Task 4: Create Multiple Pipelines

**Description**: Create additional pipelines for different purposes.

**Expected Outcome**:

- Create new pipeline
- Configure pipeline for specific use case
- Understand multiple pipeline scenarios
- Test new pipeline

**Hints**:

- Can have multiple pipelines per signal
- Different pipelines for different backends
- Useful for routing data
- Define in service.pipelines

**Reference Files**:

- `otel-config.yaml`
- Multiple pipelines documentation

## Verification Steps

1. **Pipeline Architecture Verification**:
   - Understand pipeline concept
   - Know pipeline components
   - Understand data flow

2. **Current Pipelines Verification**:
   - Understand existing pipelines
   - Know pipeline composition
   - Understand pipeline flow

3. **Pipeline Modification Verification**:
   - Verify pipeline changes work
   - Check component order impact
   - Understand modifications

4. **Multiple Pipelines Verification**:
   - Verify new pipeline works
   - Understand multiple pipeline use cases
   - Know when to use multiple pipelines

## Solution

See [Solution: Collector Pipelines](../solutions/17-collector-pipelines.md)
