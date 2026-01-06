# SDK Pipelines

**Exam Weight**: The OpenTelemetry API and SDK (46%)

## Learning Objectives

- Understand SDK pipeline architecture
- Learn trace pipeline components
- Learn metrics pipeline components
- Understand pipeline flow
- Configure pipeline components

## Prerequisites

- System is running
- Understanding of processors and exporters
- Basic knowledge of SDK architecture

## Exercise Tasks

### Task 1: Identify Trace Pipeline

**Description**: Examine and understand the trace pipeline in the system.

**Expected Outcome**:

- Identify trace pipeline components
- Understand pipeline flow
- Document trace pipeline
- Understand component order

**Hints**:

- Pipeline: TracerProvider → Processor → Exporter
- Check service files for pipeline setup
- BatchSpanProcessor is used
- OTLP exporter sends data

**Reference Files**:

- `service-node/app.js` (lines 12-14)
- `service-python/app.py` (lines 13-16)
- OpenTelemetry SDK documentation

### Task 2: Identify Metrics Pipeline

**Description**: Examine and understand the metrics pipeline in the system.

**Expected Outcome**:

- Identify metrics pipeline components
- Understand pipeline flow
- Document metrics pipeline
- Understand component order

**Hints**:

- Pipeline: MeterProvider → Reader → Exporter
- PeriodicExportingMetricReader is used
- OTLP exporter sends metrics
- Different from trace pipeline

**Reference Files**:

- `service-node/app.js` (lines 16-18)
- `service-python/app.py` (lines 19-20)
- OpenTelemetry SDK documentation

### Task 3: Modify Pipeline Configuration

**Description**: Modify pipeline component configuration.

**Expected Outcome**:

- Modify processor configuration
- Modify exporter configuration
- Understand configuration options
- Apply configuration changes

**Hints**:

- BatchSpanProcessor has config options
- PeriodicExportingMetricReader has config
- Exporters have endpoint configuration
- Modify in code

**Reference Files**:

- Both service files
- Processor and exporter documentation

### Task 4: Understand Pipeline Flow

**Description**: Trace data flow through the pipeline.

**Expected Outcome**:

- Understand data flow from creation to export
- Document pipeline stages
- Understand processing steps
- Know where data is transformed

**Hints**:

- Data created by instrumentation
- Processed by processors
- Exported by exporters
- Each stage can modify data

**Reference Files**:

- All pipeline components
- OpenTelemetry SDK architecture

## Verification Steps

1. **Trace Pipeline Verification**:
   - Can you identify all components?
   - Understand pipeline flow?
   - Know component order?

2. **Metrics Pipeline Verification**:
   - Can you identify all components?
   - Understand pipeline flow?
   - Know differences from trace pipeline?

3. **Configuration Verification**:
   - Verify configuration changes
   - Check pipeline behavior
   - Understand config options

4. **Pipeline Flow Verification**:
   - Understand data flow
   - Know processing stages
   - Understand transformations

## Solution

See [Solution: SDK Pipelines](../solutions/11-api-sdk-pipelines.md)
