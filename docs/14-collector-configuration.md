# Collector Configuration

**Exam Weight**: The OpenTelemetry Collector (26%)

## Learning Objectives

- Understand OpenTelemetry Collector configuration
- Learn configuration file structure
- Configure receivers, processors, exporters
- Understand pipeline configuration
- Learn configuration best practices

## Prerequisites

- System is running
- Understanding of Collector architecture
- Access to `otel-config.yaml`

## Exercise Tasks

### Task 1: Examine Collector Configuration

**Description**: Examine the current Collector configuration file.

**Expected Outcome**:

- Understand configuration file structure
- Identify receivers section
- Identify processors section
- Identify exporters section
- Identify pipelines section

**Hints**:

- Configuration is YAML format
- Sections: receivers, processors, exporters, service
- Service section defines pipelines
- Check `otel-config.yaml`

**Reference Files**:

- `otel-config.yaml` (complete file)

### Task 2: Modify Receiver Configuration

**Description**: Modify receiver configuration.

**Expected Outcome**:

- Understand OTLP receiver configuration
- Modify receiver settings
- Add receiver endpoints
- Understand receiver protocols

**Hints**:

- OTLP receiver supports gRPC and HTTP
- Can configure ports and endpoints
- Receivers receive telemetry data
- Modify in `otel-config.yaml`

**Reference Files**:

- `otel-config.yaml` (lines 1-6)
- OpenTelemetry Collector receivers documentation

### Task 3: Modify Processor Configuration

**Description**: Modify processor configuration.

**Expected Outcome**:

- Understand batch processor
- Modify processor settings
- Add processor configuration
- Understand processor options

**Hints**:

- Batch processor batches data
- Can configure batch size, timeout
- Processors process data
- Modify in `otel-config.yaml`

**Reference Files**:

- `otel-config.yaml` (lines 7-9)
- OpenTelemetry Collector processors documentation

### Task 4: Modify Exporter Configuration

**Description**: Modify exporter configuration.

**Expected Outcome**:

- Understand exporter configuration
- Modify exporter endpoints
- Configure exporter settings
- Understand exporter options

**Hints**:

- Exporters send data to backends
- Jaeger exporter for traces
- Prometheus exporter for metrics
- Modify endpoints and settings

**Reference Files**:

- `otel-config.yaml` (lines 10-15)
- OpenTelemetry Collector exporters documentation

### Task 5: Modify Pipeline Configuration

**Description**: Modify pipeline configuration.

**Expected Outcome**:

- Understand pipeline structure
- Modify pipeline components
- Add or remove pipeline stages
- Understand pipeline flow

**Hints**:

- Pipelines: receivers → processors → exporters
- Separate pipelines for traces and metrics
- Define in service.pipelines section
- Modify pipeline composition

**Reference Files**:

- `otel-config.yaml` (lines 16-25)
- OpenTelemetry Collector pipelines documentation

## Verification Steps

1. **Configuration Understanding Verification**:
   - Understand configuration structure
   - Know all configuration sections
   - Understand configuration format

2. **Receiver Configuration Verification**:
   - Verify receiver changes work
   - Check receiver receives data
   - Understand receiver options

3. **Processor Configuration Verification**:
   - Verify processor changes
   - Check processor behavior
   - Understand processor options

4. **Exporter Configuration Verification**:
   - Verify exporter changes
   - Check data reaches backends
   - Understand exporter options

5. **Pipeline Configuration Verification**:
   - Verify pipeline changes
   - Check pipeline flow
   - Understand pipeline structure

## Solution

See [Solution: Collector Configuration](../solutions/14-collector-configuration.md)
