# Context Propagation

**Exam Weight**: The OpenTelemetry API and SDK (46%)

## Learning Objectives

- Understand context propagation in OpenTelemetry
- Learn W3C Trace Context propagation
- Understand propagation mechanisms
- Configure context propagation
- Debug context propagation

## Prerequisites

- System is running
- Understanding of distributed tracing
- Basic knowledge of HTTP headers

## Exercise Tasks

### Task 1: Understand Context Propagation

**Description**: Learn how context propagation works in the system.

**Expected Outcome**:

- Understand trace context
- Learn how context is propagated
- Identify propagation mechanisms
- Understand W3C Trace Context

**Hints**:

- Context carries trace information
- Propagated via HTTP headers
- W3C Trace Context standard
- Automatic with instrumentation

**Reference Files**:

- Both service files
- OpenTelemetry context propagation documentation

### Task 2: Verify Automatic Propagation

**Description**: Verify that context propagation works automatically.

**Expected Outcome**:

- Make cross-service requests
- Verify context propagation
- Check trace context in headers
- See correlated traces in Jaeger

**Hints**:

- Make Node service call Python service
- Check HTTP headers for trace context
- Verify traces are correlated
- Automatic with instrumentation

**Reference Files**:

- Both service files
- Jaeger UI for trace correlation

### Task 3: Inspect Trace Context

**Description**: Inspect and understand trace context structure.

**Expected Outcome**:

- Inspect trace context headers
- Understand trace ID and span ID
- Understand context format
- Document context structure

**Hints**:

- Trace context: `traceparent` header
- Contains trace ID and span ID
- W3C Trace Context format
- Check HTTP headers

**Reference Files**:

- HTTP request/response headers
- W3C Trace Context specification

### Task 4: Configure Propagation

**Description**: Configure or customize context propagation.

**Expected Outcome**:

- Understand propagation configuration
- Configure propagators if needed
- Understand propagation options
- Know when customization is needed

**Hints**:

- Default propagators work automatically
- Can configure custom propagators
- Usually not needed for basic use
- Advanced scenarios may need customization

**Reference Files**:

- OpenTelemetry propagation documentation
- Propagator configuration

## Verification Steps

1. **Context Understanding Verification**:
   - Understand trace context concept
   - Know how context is structured
   - Understand W3C standard

2. **Automatic Propagation Verification**:
   - Verify context propagates between services
   - Check traces are correlated
   - Understand automatic behavior

3. **Context Inspection Verification**:
   - Can inspect trace context headers
   - Understand context format
   - Know context components

4. **Configuration Verification**:
   - Understand propagation configuration
   - Know when customization needed
   - Understand default behavior

## Solution

See [Solution: Context Propagation](../solutions/12-api-sdk-context-propagation.md)
