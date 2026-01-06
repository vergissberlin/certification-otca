# Composability and Extension

**Exam Weight**: The OpenTelemetry API and SDK (46%)

## Learning Objectives

- Understand OpenTelemetry's composable architecture
- Learn about processors and their role
- Learn about exporters and their role
- Understand how to extend OpenTelemetry
- Learn about custom components

## Prerequisites

- System is running
- Understanding of SDK pipelines
- Basic knowledge of OpenTelemetry SDK

## Exercise Tasks

### Task 1: Identify Composable Components

**Description**: Examine the system to identify composable SDK components.

**Expected Outcome**:

- Identify processors in use
- Identify exporters in use
- Understand component composition
- Document the component architecture

**Hints**:

- Check both service files for processors
- Look for exporters
- Understand how components are composed
- Components are pluggable and replaceable

**Reference Files**:

- `service-node/app.js` (lines 13, 17)
- `service-python/app.py` (lines 15, 19)
- `otel-config.yaml`

### Task 2: Modify Span Processors

**Description**: Change or configure span processors.

**Expected Outcome**:

- Understand BatchSpanProcessor configuration
- Modify batch processor settings
- Understand processor options
- Apply configuration changes

**Hints**:

- BatchSpanProcessor has configuration options
- Can configure batch size, timeout
- Processors process spans before export
- Check processor documentation

**Reference Files**:

- `service-node/app.js` (line 13)
- `service-python/app.py` (line 15)
- OpenTelemetry SDK documentation

### Task 3: Understand Exporter Composition

**Description**: Understand how exporters work and can be composed.

**Expected Outcome**:

- Understand OTLP exporter configuration
- Learn about different exporter types
- Understand exporter composition
- Know when to use different exporters

**Hints**:

- Exporters send data to backends
- OTLP exporter is protocol-agnostic
- Can have multiple exporters
- Exporters are composable

**Reference Files**:

- `service-node/app.js` (OTLP exporters)
- `service-python/app.py` (OTLP exporters)
- OpenTelemetry exporter documentation

### Task 4: Add Custom Span Processor

**Description**: Create a simple custom span processor.

**Expected Outcome**:

- Create a custom span processor
- Understand processor interface
- Add custom processing logic
- Integrate custom processor

**Hints**:

- Processors implement SpanProcessor interface
- Can modify spans before export
- Can add filtering or transformation
- Use for custom business logic

**Reference Files**:

- OpenTelemetry SDK documentation
- Processor interface documentation

## Verification Steps

1. **Component Identification Verification**:
   - Can you identify all composable components?
   - Understand component roles?
   - Know how components fit together?

2. **Processor Modification Verification**:
   - Verify processor configuration changes
   - Check that changes take effect
   - Understand processor behavior

3. **Exporter Composition Verification**:
   - Understand exporter configuration
   - Know different exporter types
   - Understand exporter composition

4. **Custom Processor Verification**:
   - Verify custom processor works
   - Check custom processing logic
   - Understand extension points

## Solution

See [Solution: Composability and Extension](../solutions/06-api-sdk-composability-extension.md)
