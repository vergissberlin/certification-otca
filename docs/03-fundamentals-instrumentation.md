# Instrumentation

**Exam Weight**: Fundamentals of Observability (18%)

## Learning Objectives

- Understand automatic vs manual instrumentation
- Learn when to use each approach
- Implement manual instrumentation
- Configure automatic instrumentation
- Understand instrumentation libraries

## Prerequisites

- System is running
- Understanding of traces and spans
- Basic knowledge of Node.js and Python

## Exercise Tasks

### Task 1: Identify Instrumentation Types

**Description**: Examine the system to identify automatic and manual instrumentation.

**Expected Outcome**:

- List all automatic instrumentation in use
- List all manual instrumentation in use
- Understand the difference between them
- Document which approach is used where

**Hints**:

- Check `service-node/app.js` for Express instrumentation
- Check `service-python/app.py` for Flask instrumentation
- Look for manual span creation
- Automatic instrumentation requires setup but no code changes

**Reference Files**:

- `service-node/app.js` (lines 22-24, 26-29)
- `service-python/app.py` (lines 16-17, 24-28)
- `service-node/package.json`
- `service-python/requirements.txt`

### Task 2: Add Manual Instrumentation

**Description**: Add manual spans to track specific operations.

**Expected Outcome**:

- Add a manual span in the Node.js service
- Add span attributes to the manual span
- Add events to the span
- Verify the span appears in Jaeger

**Hints**:

- Use `tracer.startSpan()` or `tracer.startActiveSpan()`
- Get tracer from the TracerProvider
- Add attributes with `span.setAttribute()`
- Add events with `span.addEvent()`

**Reference Files**:

- `service-node/app.js`
- `service-python/app.py` (line 26 for reference)

### Task 3: Configure Automatic Instrumentation

**Description**: Modify automatic instrumentation configuration.

**Expected Outcome**:

- Configure Express instrumentation to capture request bodies
- Configure Flask instrumentation options
- Understand instrumentation configuration parameters
- Apply configuration changes

**Hints**:

- Check instrumentation library documentation
- Express instrumentation: `@opentelemetry/instrumentation-express`
- Flask instrumentation: `opentelemetry-instrumentation-flask`
- Configuration is passed when creating instrumentation

**Reference Files**:

- `service-node/app.js` (line 23)
- `service-python/app.py` (line 17)

### Task 4: Combine Automatic and Manual Instrumentation

**Description**: Use both automatic and manual instrumentation together.

**Expected Outcome**:

- Create a manual span within an automatically instrumented request
- Understand span hierarchy (parent-child relationships)
- Add manual instrumentation for business logic
- Verify nested spans in Jaeger

**Hints**:

- Automatic instrumentation creates parent spans
- Manual spans can be children of automatic spans
- Use context propagation to maintain relationships
- Check span hierarchy in Jaeger UI

**Reference Files**:

- Both service files
- Jaeger UI for span hierarchy visualization

## Verification Steps

1. **Instrumentation Type Verification**:
   - Can you identify which spans are automatic vs manual?
   - Check Jaeger to see span sources
   - Verify both types appear in traces

2. **Manual Instrumentation Verification**:
   - Verify new manual spans appear in Jaeger
   - Check span attributes and events
   - Verify span timing is correct

3. **Configuration Verification**:
   - Verify instrumentation configuration changes take effect
   - Check that new data is captured
   - Verify no errors in logs

4. **Combined Instrumentation Verification**:
   - Check Jaeger for span hierarchy
   - Verify parent-child relationships
   - Understand how automatic and manual spans relate

## Solution

See [Solution: Instrumentation](../solutions/03-fundamentals-instrumentation.md)
