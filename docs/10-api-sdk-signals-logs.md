# Signals: Logs

**Exam Weight**: The OpenTelemetry API and SDK (46%)

## Learning Objectives

- Understand logs signal in OpenTelemetry
- Learn log record structure
- Integrate logging with OpenTelemetry
- Understand log correlation with traces
- Learn log best practices

## Prerequisites

- System is running
- Understanding of traces and metrics
- Basic knowledge of logging

## Exercise Tasks

### Task 1: Understand Log Signal

**Description**: Learn about OpenTelemetry log signal structure.

**Expected Outcome**:

- Understand log record components
- Learn log severity levels
- Understand log attributes
- Know log signal structure

**Hints**:

- Logs: timestamp, severity, body, attributes
- Severity: TRACE, DEBUG, INFO, WARN, ERROR, FATAL
- Logs can be correlated with traces
- Log signal is newer in OpenTelemetry

**Reference Files**:

- OpenTelemetry Logs documentation
- Log signal specification

### Task 2: Add Logging Instrumentation

**Description**: Add OpenTelemetry logging to a service.

**Expected Outcome**:

- Install logging SDK
- Configure log exporter
- Emit logs with OpenTelemetry
- Verify logs are exported

**Hints**:

- Use OpenTelemetry logging SDK
- Configure log processor and exporter
- Emit logs using logging API
- Export logs via OTLP

**Reference Files**:

- OpenTelemetry Logs SDK documentation
- Service files for integration

### Task 3: Correlate Logs with Traces

**Description**: Correlate log records with trace context.

**Expected Outcome**:

- Add trace context to logs
- Understand log-trace correlation
- Query correlated logs
- Use trace ID in logs

**Hints**:

- Include trace ID in log attributes
- Use context propagation
- Correlate logs with spans
- Check log backends for correlation

**Reference Files**:

- OpenTelemetry context documentation
- Log correlation best practices

### Task 4: Configure Log Processing

**Description**: Configure log processing and export.

**Expected Outcome**:

- Configure log processor
- Configure log exporter
- Set log levels
- Understand log pipeline

**Hints**:

- Logs go through processors
- Export logs to backends
- Configure log levels
- Understand log pipeline similar to traces

**Reference Files**:

- OpenTelemetry Logs SDK
- Processor and exporter documentation

## Verification Steps

1. **Log Signal Verification**:
   - Understand log record structure
   - Know log components
   - Understand severity levels

2. **Logging Instrumentation Verification**:
   - Verify logs are emitted
   - Check log export works
   - Understand logging setup

3. **Log-Trace Correlation Verification**:
   - Verify trace context in logs
   - Correlate logs with traces
   - Understand correlation value

4. **Log Processing Verification**:
   - Verify log processing works
   - Check log export
   - Understand log pipeline

## Solution

See [Solution: Signals - Logs](../solutions/10-api-sdk-signals-logs.md)
