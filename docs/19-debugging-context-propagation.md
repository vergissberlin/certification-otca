# Debugging: Context Propagation

**Exam Weight**: Maintaining and Debugging Observability Pipelines (10%)

## Learning Objectives

- Debug context propagation issues
- Identify context propagation problems
- Verify context propagation
- Fix context propagation issues
- Understand propagation debugging tools

## Prerequisites

- System is running
- Understanding of context propagation
- Access to Jaeger UI and service logs

## Exercise Tasks

### Task 1: Identify Context Propagation Issues

**Description**: Learn to identify when context propagation is broken.

**Expected Outcome**:

- Understand symptoms of broken propagation
- Identify orphaned traces
- Recognize missing trace context
- Document propagation issues

**Hints**:

- Broken propagation: separate traces instead of one
- Missing trace IDs in logs
- Orphaned spans
- Check Jaeger for trace correlation

**Reference Files**:

- Jaeger UI
- Service logs
- Trace correlation

### Task 2: Inspect Trace Context

**Description**: Inspect trace context to verify propagation.

**Expected Outcome**:

- Inspect HTTP headers for trace context
- Verify trace context format
- Check trace ID propagation
- Document context inspection

**Hints**:

- Check `traceparent` header
- Verify W3C Trace Context format
- Check trace ID consistency
- Use HTTP inspection tools

**Reference Files**:

- HTTP request/response headers
- W3C Trace Context specification

### Task 3: Debug Propagation Problems

**Description**: Debug and fix context propagation issues.

**Expected Outcome**:

- Identify propagation failure points
- Fix propagation configuration
- Verify propagation works
- Document debugging process

**Hints**:

- Check instrumentation configuration
- Verify propagator setup
- Check network/proxy issues
- Test propagation end-to-end

**Reference Files**:

- Service configuration
- Instrumentation setup
- Network configuration

### Task 4: Verify Propagation in Production-like Scenarios

**Description**: Test context propagation in various scenarios.

**Expected Outcome**:

- Test propagation across services
- Test propagation with errors
- Test propagation with async operations
- Verify propagation reliability

**Hints**:

- Test normal flow
- Test error scenarios
- Test async operations
- Verify in all scenarios

**Reference Files**:

- All service files
- Various test scenarios

## Verification Steps

1. **Issue Identification Verification**:
   - Can identify propagation issues
   - Recognize symptoms
   - Understand problem indicators

2. **Context Inspection Verification**:
   - Can inspect trace context
   - Verify context format
   - Understand context structure

3. **Debugging Verification**:
   - Can debug propagation issues
   - Fix problems
   - Verify fixes work

4. **Scenario Testing Verification**:
   - Test various scenarios
   - Verify propagation works
   - Understand reliability

## Solution

See [Solution: Debugging Context Propagation](../solutions/19-debugging-context-propagation.md)
