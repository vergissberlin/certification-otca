# Signals: Tracing

**Exam Weight**: The OpenTelemetry API and SDK (46%)

## Learning Objectives

- Understand tracing signal in detail
- Learn to create and manage spans
- Understand span lifecycle
- Learn span attributes and events
- Understand distributed tracing

## Prerequisites

- System is running
- Understanding of spans and traces
- Basic knowledge of tracing concepts

## Exercise Tasks

### Task 1: Create Manual Spans

**Description**: Create spans manually in both services.

**Expected Outcome**:

- Create spans using Tracer API
- Understand span creation methods
- Add span attributes
- End spans properly

**Hints**:

- Use `tracer.startSpan()` or `tracer.startActiveSpan()`
- Get tracer from TracerProvider
- Add attributes with `span.setAttribute()`
- Always end spans

**Reference Files**:

- `service-python/app.py` (line 26 for reference)
- `service-node/app.js`
- OpenTelemetry Tracing API documentation

### Task 2: Add Span Attributes and Events

**Description**: Enhance spans with attributes and events.

**Expected Outcome**:

- Add multiple span attributes
- Add span events
- Understand attribute types
- Use semantic conventions

**Hints**:

- Attributes: key-value pairs
- Events: timestamped occurrences
- Use semantic conventions when possible
- Add business context

**Reference Files**:

- Both service files
- OpenTelemetry semantic conventions

### Task 3: Understand Span Status

**Description**: Set and understand span status.

**Expected Outcome**:

- Set span status (OK, ERROR)
- Understand status codes
- Set error status with descriptions
- Verify status in Jaeger

**Hints**:

- Status: UNSET, OK, ERROR
- Set status on errors
- Add error descriptions
- Check status in Jaeger UI

**Reference Files**:

- Both service files
- OpenTelemetry span status documentation

### Task 4: Create Distributed Traces

**Description**: Create traces that span multiple services.

**Expected Outcome**:

- Make Node service call Python service
- Propagate trace context
- See distributed trace in Jaeger
- Understand context propagation

**Hints**:

- Make HTTP call from Node to Python
- Context propagation happens automatically
- Check Jaeger for cross-service traces
- Understand trace context headers

**Reference Files**:

- Both service files
- Jaeger UI for trace visualization

## Verification Steps

1. **Manual Span Verification**:
   - Verify spans appear in Jaeger
   - Check span names and attributes
   - Understand span lifecycle

2. **Attributes and Events Verification**:
   - Verify attributes in Jaeger
   - Check events are recorded
   - Understand attribute structure

3. **Status Verification**:
   - Verify status codes in Jaeger
   - Check error status handling
   - Understand status meaning

4. **Distributed Trace Verification**:
   - Verify cross-service traces in Jaeger
   - Check context propagation
   - Understand distributed tracing

## Solution

See [Solution: Signals - Tracing](../solutions/08-api-sdk-signals-tracing.md)
